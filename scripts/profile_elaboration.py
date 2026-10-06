#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Serial warm Lean profiles; no artifact invalidation or olean writes.

Example: python3 scripts/profile_elaboration.py --output .verify-work/profiles \
  --summary .verify-work/before/summary.json --top 5
For A/B runs use --modules FreeEntropy.SomeFile --repeat 3.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary", type=Path)
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--modules", nargs="+")
    parser.add_argument("--repeat", type=int, default=1)
    parser.add_argument("--threads", type=int, default=4)
    args = parser.parse_args()
    if bool(args.modules) == bool(args.summary):
        parser.error("choose --modules or --summary")
    if args.repeat < 1:
        parser.error("--repeat must be positive")
    if args.threads < 1 or args.top < 1:
        parser.error("--threads and --top must be positive")
    modules = args.modules or [item["module"] for item in
        json.loads(args.summary.read_text())["top_30_modules"][:args.top]]
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    lake = shutil.which("lake") or str(Path.home() / ".elan/bin/lake")
    gtime = shutil.which("gtime") or next((str(p) for p in (
        Path("/opt/homebrew/bin/gtime"), Path("/usr/local/bin/gtime")) if p.is_file()), None)
    if not gtime and sys.platform.startswith("linux") and Path("/usr/bin/time").is_file():
        gtime = "/usr/bin/time"
    if not gtime:
        raise SystemExit("GNU time (gtime) is required for these profiles")
    samples = []
    for module in modules:
        if not re.fullmatch(r"FreeEntropy\.[A-Za-z0-9_]+|FreeEntropy|Theorem1|Theorem2|All", module):
            raise ValueError(f"not a project proof module: {module}")
        relative = module.replace(".", "/") + ".lean"
        source = ROOT / "lean" / relative
        for repeat in range(1, args.repeat + 1):
            source_before = hashlib.sha256(source.read_bytes()).hexdigest()
            command = [gtime, "-v", lake, "env", "lean", "--profile", relative]
            result = subprocess.run(command, cwd=ROOT / "lean",
                env=dict(os.environ, LEAN_NUM_THREADS=str(args.threads)),
                text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            filename = module + f"-{repeat}.txt"
            (out / filename).write_text(result.stdout)
            source_after = hashlib.sha256(source.read_bytes()).hexdigest()
            sample = {"module": module, "repeat": repeat, "exit_status": result.returncode,
                "command": command, "source_sha256": source_before,
                "source_after_sha256": source_after, "source_unchanged": source_before == source_after,
                "output": filename, "output_sha256": hashlib.sha256(result.stdout.encode()).hexdigest()}
            for label, key in (("User time (seconds)", "user_cpu_seconds"),
                               ("System time (seconds)", "sys_cpu_seconds")):
                match = re.search(re.escape(label) + r": ([\d.]+)", result.stdout)
                if match:
                    sample[key] = float(match[1])
            match = re.search(r"Elapsed \(wall clock\) time \(h:mm:ss or m:ss\): ([\d:.]+)", result.stdout)
            if match:
                elapsed = 0.0
                for component in match[1].split(":"):
                    elapsed = elapsed * 60 + float(component)
                sample["elapsed_seconds"] = elapsed
            # Preserve the native cumulative block verbatim for phase attribution.
            block = re.search(r"cumulative profiling times[^\n]*\n(.*?)(?=\n\s*Command being timed:|\Z)",
                              result.stdout, re.S | re.I)
            sample["cumulative_profile_block"] = block[0].strip() if block else None
            samples.append(sample)
            (out / "profiles.json").write_text(json.dumps({"recorded_at_utc":
                datetime.now(timezone.utc).isoformat(), "lean_num_threads": args.threads,
                "serial": True, "cache_condition": "warm imports; no olean/IR output requested",
                "samples": samples}, indent=2) + "\n")
            print(f"{module} sample {repeat}: exit {result.returncode}, wall {sample.get('elapsed_seconds')}s", flush=True)
            if source_before != source_after:
                raise SystemExit(f"source changed during profile: {source}")
            if result.returncode:
                raise SystemExit(f"profile failed: {out / filename}")


if __name__ == "__main__":
    main()
