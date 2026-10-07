#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Rebuild only QMDL proof artifacts, preserving and checking dependency caches.

Run after the documented dependency cache setup. This deliberately excludes
Comparator specifications and the separate axiom-audit probe. Never runs lake
clean/update. Timings measure a project-cold, dependency-warm build of All.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
LEAN = ROOT / "lean"
ROOTS = ("FreeEntropy", "Theorem1", "Theorem2", "All")


def run_text(command, cwd=ROOT):
    return subprocess.check_output(command, cwd=cwd, text=True).strip()


def sources():
    paths = sorted((LEAN / "FreeEntropy").glob("*.lean"))
    paths += [LEAN / (name + ".lean") for name in ROOTS]
    paths += [LEAN / name for name in ("lean-toolchain", "lakefile.toml", "lake-manifest.json")]
    return hashlib.sha256(b"".join(str(p.relative_to(ROOT)).encode() + b"\0" + p.read_bytes()
                                   for p in paths)).hexdigest()


def dependencies():
    result = {}
    for package in sorted((LEAN / ".lake/packages").iterdir()):
        paths = sorted((package / ".lake/build/lib").rglob("*.olean"))
        records = [(str(p.relative_to(package)), p.stat().st_size, p.stat().st_mtime_ns)
                   for p in paths]
        result[package.name] = {"oleans": len(paths), "artifact_stat_sha256":
            hashlib.sha256(json.dumps(records, separators=(",", ":")).encode()).hexdigest()}
    if result.get("mathlib", {}).get("oleans", 0) == 0:
        raise ValueError("Mathlib cache is empty; restore it before measuring")
    return result


def invalidate_own():
    build = LEAN / ".lake/build"
    if build.is_symlink() or not build.resolve().is_relative_to(ROOT):
        raise ValueError("project build must be inside this checkout, not a shared symlink")
    removed = []
    for directory in (build / "lib/lean", build / "ir"):
        for name in ROOTS:
            targets = [directory / name, *directory.glob(name + ".*")]
            for path in targets:
                if not path.exists():
                    continue
                if path.is_symlink() or not path.resolve().is_relative_to(build.resolve()):
                    raise ValueError(f"unsafe artifact path: {path}")
                removed.append(str(path.relative_to(ROOT)))
                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    path.unlink()
    return removed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="new directory for logs and JSON")
    parser.add_argument("--threads", type=int, default=4, help="LEAN_NUM_THREADS for both snapshots")
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    commit = run_text(["git", "rev-parse", "HEAD"])
    if run_text(["git", "diff", "HEAD", "--", "lean"]):
        raise ValueError("commit Lean changes first: size and timing must refer to the same snapshot")
    if run_text(["git", "ls-files", "--others", "--exclude-standard", "--", "lean/FreeEntropy", "lean/*.lean"]):
        raise ValueError("untracked proof sources would not match the measured Git snapshot")
    before_source, before_deps = sources(), dependencies()
    inventory = subprocess.run(["ps", "-eo", "pid,etime,args"], text=True, capture_output=True).stdout
    (out / "processes-before.txt").write_text("\n".join(line for line in inventory.splitlines()
        if re.search(r"(?:^|/|\s)(?:lake|lean)(?: |$)", line)) + "\n")
    gtime = shutil.which("gtime") or next((str(p) for p in (
        Path("/opt/homebrew/bin/gtime"), Path("/usr/local/bin/gtime")) if p.is_file()), None)
    timer = [gtime, "-v"] if gtime else ["/usr/bin/time", "-l" if sys.platform == "darwin" else "-v"]
    lake = shutil.which("lake") or str(Path.home() / ".elan/bin/lake")
    command = [*timer, lake, "--no-ansi", "--no-cache", "build", "All"]
    record = {"source_commit": commit, "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "host": platform.platform(), "logical_cpus": os.cpu_count(),
        "timing_tool": "GNU time -v" if timer[-1] == "-v" else "macOS BSD time -l",
        "command": command, "lean_num_threads": args.threads,
        "lean_version": run_text([lake, "env", "lean", "--version"], LEAN),
        "cache_condition": "own proof artifacts invalidated; dependency oleans retained; OS cache uncontrolled",
        "source_snapshot_sha256": before_source, "dependencies_before": before_deps,
        "invalidated": invalidate_own(), "status": "running"}
    (out / "result.json").write_text(json.dumps(record, indent=2) + "\n")
    env = dict(os.environ, LEAN_NUM_THREADS=str(args.threads))
    started = time.monotonic()
    invalid = []
    with (out / "build.txt").open("w") as log:
        process = subprocess.Popen(command, cwd=LEAN, env=env, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, start_new_session=True)
        for line in process.stdout:
            log.write(line)
            log.flush()
            match = re.search(r"\bBuilt ([A-Za-z0-9_.]+)(?: |$)", line)
            if match and not any(match[1] == n or match[1].startswith(n + ".") for n in ROOTS):
                invalid.append(line.strip())
                os.killpg(process.pid, signal.SIGTERM)
        code = process.wait()
    text = (out / "build.txt").read_text()
    record.update(finished_at_utc=datetime.now(timezone.utc).isoformat(),
        observer_elapsed_seconds=time.monotonic() - started, exit_status=code,
        invalid_upstream_compiles=invalid, dependencies_after=dependencies(),
        source_snapshot_after_sha256=sources())
    if record["timing_tool"] == "macOS BSD time -l":
        match = re.search(r"([\d.]+)\s+real\s+([\d.]+)\s+user\s+([\d.]+)\s+sys", text)
        rss = re.search(r"(\d+)\s+maximum resident set size", text)
        if match:
            record.update(elapsed_seconds=float(match[1]), user_cpu_seconds=float(match[2]),
                          sys_cpu_seconds=float(match[3]))
        if rss:
            record["max_rss_bytes"] = int(rss[1])
    else:
        for label, key in (("User time (seconds)", "user_cpu_seconds"),
                           ("System time (seconds)", "sys_cpu_seconds")):
            match = re.search(re.escape(label) + r": ([\d.]+)", text)
            if match:
                record[key] = float(match[1])
        match = re.search(r"Elapsed \(wall clock\) time \(h:mm:ss or m:ss\): ([\d:.]+)", text)
        if match:
            elapsed = 0.0
            for component in match[1].split(":"):
                elapsed = elapsed * 60 + float(component)
            record["elapsed_seconds"] = elapsed
        match = re.search(r"Maximum resident set size \(kbytes\): (\d+)", text)
        if match:
            record["max_rss_bytes"] = int(match[1]) * 1024
    if "elapsed_seconds" in record:
        record["cpu_percent"] = 100 * (record["user_cpu_seconds"] + record["sys_cpu_seconds"]) / record["elapsed_seconds"]
    record["status"] = "passed" if (code == 0 and not invalid and before_deps == record["dependencies_after"]
        and before_source == record["source_snapshot_after_sha256"]) else "invalid_or_failed"
    record["build_log_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (out / "result.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({k: v for k, v in record.items() if k in (
        "status", "source_commit", "elapsed_seconds", "user_cpu_seconds", "sys_cpu_seconds", "cpu_percent", "max_rss_bytes")}))
    return 0 if record["status"] == "passed" else 1


if __name__ == "__main__":
    sys.exit(main())
