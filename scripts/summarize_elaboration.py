#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Summarize a project-only elaboration benchmark without running Lean.

Usage:
  python3 scripts/summarize_elaboration.py RUN_DIR
  python3 scripts/summarize_elaboration.py AFTER_DIR --compare BEFORE_DIR/summary.json

RUN_DIR contains result.json and build.txt. Source/import information is read
from the recorded Git commit, not from an edited working tree. This script uses
only the Python standard library. A sum of Lake's per-module elapsed durations
is a scheduling proxy, never a measurement of CPU consumption.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
from typing import Any


ANSI = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
BUILT = re.compile(
    r"^\s*(?:[✔⚠ℹ✓✖✘]\s*)?\[\d+\s*/\s*\d+\]\s+Built\s+(?P<target>[^\s(]+)"
    r"(?:\s+\((?P<value>[0-9]+(?:\.[0-9]+)?)\s*(?P<unit>ms|s)\))?"
)
PROGRESS = re.compile(r"\[(\d+)\s*/\s*(\d+)\]")
WARNING = re.compile(r"^warning:\s*(?:(.*?\.lean):(\d+):(\d+):\s*)?(.*)$")
LINTER = re.compile(r"set_option\s+(linter\.[\w.]+)\s+false")
IMPORT = re.compile(r"^\s*(?:(?:public|meta)\s+)*import\s+(.+)$", re.MULTILINE)
FAMILY = re.compile(r"[A-Z]+(?=[A-Z][a-z]|$)|[A-Z][a-z]+|[a-z]+")
ENTRY_MODULES = {"FreeEntropy", "Theorem1", "Theorem2", "All"}


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True)


def proof_sources(repo: Path, ref: str) -> dict[str, str]:
    """The production proof library and its four reader-facing roots."""
    paths = git(repo, "ls-tree", "-r", "--name-only", ref, "--", "lean").splitlines()
    selected = []
    for relative in paths:
        path = Path(relative)
        if path.suffix != ".lean":
            continue
        module = ".".join(path.relative_to("lean").with_suffix("").parts)
        if module in ENTRY_MODULES or module.startswith("FreeEntropy."):
            selected.append((module, relative))
    requests = "".join(f"{ref}:{relative}\n" for _, relative in selected).encode()
    raw = subprocess.run(
        ["git", "-C", str(repo), "cat-file", "--batch"],
        input=requests, stdout=subprocess.PIPE, check=True,
    ).stdout
    sources, cursor = {}, 0
    for module, relative in selected:
        end = raw.index(b"\n", cursor)
        header = raw[cursor:end].decode()
        if not re.search(r" blob \d+$", header):
            raise ValueError(f"Cannot read recorded source {ref}:{relative}: {header}")
        size = int(header.rsplit(" ", 1)[1])
        cursor = end + 1
        sources[module] = raw[cursor:cursor + size].decode()
        cursor += size + 1
    return sources


def strip_comments(text: str) -> str:
    """Retain line structure, strings and code; erase nested Lean comments."""
    out, i, depth, in_string = [], 0, 0, False
    while i < len(text):
        if depth:
            if text.startswith("/-", i):
                depth += 1
                out.extend("  ")
                i += 2
            elif text.startswith("-/", i):
                depth -= 1
                out.extend("  ")
                i += 2
            else:
                out.append("\n" if text[i] == "\n" else " ")
                i += 1
        elif in_string:
            out.append(text[i])
            if text[i] == "\\" and i + 1 < len(text):
                out.append(text[i + 1])
                i += 2
            else:
                if text[i] == '"':
                    in_string = False
                i += 1
        elif text.startswith("/-", i):
            depth = 1
            out.extend("  ")
            i += 2
        elif text.startswith("--", i):
            end = text.find("\n", i)
            end = len(text) if end < 0 else end
            out.extend(" " * (end - i))
            i = end
        else:
            out.append(text[i])
            in_string = text[i] == '"'
            i += 1
    return "".join(out)


def imports(sources: dict[str, str]) -> dict[str, list[str]]:
    graph = {}
    for module, source in sources.items():
        dependencies = []
        for line in IMPORT.findall(strip_comments(source)):
            dependencies.extend(name for name in line.split() if name in sources)
        graph[module] = sorted(set(dependencies))
    return graph


def warning_kind(message: str) -> str:
    kinds = [
        ("automatically included section variable", "unused_section_variables"),
        ("This simp argument is unused", "unused_simp_argument"),
        ("try 'simp' instead of 'simpa'", "unnecessary_simpa"),
        ("Try `simp at this`", "unnecessary_simpa"),
        ("Used `tac1 <;> tac2`", "unnecessary_sequence_focus"),
        ("this tactic is never executed", "unreachable_tactic"),
        ("unused variable", "unused_variable"),
        ("declaration uses 'sorry'", "sorry"),
    ]
    for needle, kind in kinds:
        if needle in message:
            return kind
    if "has been deprecated" in message:
        return "deprecated_declaration"
    if "tactic does nothing" in message:
        return "unused_tactic"
    return "other"


def parse_log(text: str, own_modules: set[str]) -> dict[str, Any]:
    events, warnings, errors, sorry_lines, replayed = [], [], [], [], []
    planned_jobs = 0
    current_warning = None
    for line_number, raw in enumerate(text.splitlines(), 1):
        line = ANSI.sub("", raw)
        progress = PROGRESS.search(line)
        if progress:
            planned_jobs = max(planned_jobs, int(progress[2]))
            current_warning = None
        match = BUILT.search(line)
        if match:
            target = match["target"]
            module = target.split(":", 1)[0]
            value = match["value"]
            seconds = None if value is None else float(value)
            if seconds is not None and match["unit"] == "ms":
                seconds /= 1000
            events.append({
                "target": target,
                "module": module,
                "facet": target.split(":", 1)[1] if ":" in target else None,
                "seconds": seconds,
                "own_module": module in own_modules,
                "line": line_number,
            })
        if "Replayed " in line:
            replayed.append({"line": line_number, "text": line})
        warning = WARNING.match(line)
        if warning:
            message = warning[4]
            current_warning = {
                "path": warning[1],
                "source_line": int(warning[2]) if warning[2] else None,
                "source_column": int(warning[3]) if warning[3] else None,
                "message": message,
                "kind": warning_kind(message),
                "linter": None,
                "log_line": line_number,
            }
            warnings.append(current_warning)
        elif current_warning:
            linter = LINTER.search(line)
            if linter:
                current_warning["linter"] = linter[1]
        if re.search(r"(?:^|\s)error:", line):
            errors.append({"line": line_number, "text": line})
            current_warning = None
        if re.search(r"\bsorryAx\b|declaration uses ['`]sorry['`]", line):
            sorry_lines.append({"line": line_number, "text": line})
    own_events = [e for e in events if e["own_module"] and e["facet"] is None]
    upstream_events = [e for e in events if not e["own_module"]]
    return {
        "build_events": events,
        "own_module_events": own_events,
        "upstream_built_events": upstream_events,
        "planned_jobs_from_log": planned_jobs,
        "warnings": warnings,
        "warning_kinds": dict(sorted(Counter(w["kind"] for w in warnings).items())),
        "warning_linters": dict(sorted(Counter(w["linter"] or "unclassified" for w in warnings).items())),
        "errors": errors,
        "sorry_lines": sorry_lines,
        "replayed_event_count": len(replayed),
    }


def module_family(module: str) -> str:
    if module in ENTRY_MODULES:
        return "facades"
    part = module.split(".")[1]
    match = FAMILY.match(part)
    return "FreeEntropy." + (match[0] if match else part)


def reachable(graph: dict[str, list[str]], root: str) -> set[str]:
    seen, todo = set(), [root]
    while todo:
        node = todo.pop()
        if node not in seen:
            seen.add(node)
            todo.extend(graph.get(node, []))
    return seen


def weighted_path(graph: dict[str, list[str]], weights: dict[str, float]) -> dict[str, Any]:
    """Longest own-import chain; missing event durations contribute zero."""
    memo, visiting = {}, set()

    def solve(module: str) -> tuple[float, list[str]]:
        if module in visiting:
            raise ValueError(f"Cycle in project import graph at {module}")
        if module in memo:
            return memo[module]
        visiting.add(module)
        best = max((solve(dep) for dep in graph[module]), key=lambda x: x[0], default=(0.0, []))
        value = best[0] + weights.get(module, 0.0), best[1] + [module]
        memo[module] = value
        visiting.remove(module)
        return value

    value, chain = solve("All")
    return {
        "logged_elapsed_seconds": value,
        "modules_dependency_first": chain,
        "module_seconds": [weights.get(module) for module in chain],
        "missing_duration_modules": [module for module in chain if module not in weights],
        "interpretation": (
            "Longest weighted project import path to All, using one observed elapsed duration per module. "
            "Missing logged durations contribute zero. Parallel-build contention is embedded in the weights; "
            "this is a scheduling diagnostic, not an independently measured serial critical-path duration."
        ),
    }


def comparison(current: dict[str, Any], before: dict[str, Any]) -> dict[str, Any]:
    keys = [
        "elapsed_seconds", "user_cpu_seconds", "sys_cpu_seconds", "cpu_percent",
        "max_rss_bytes", "logged_module_elapsed_seconds", "logged_elapsed_to_wall_ratio",
        "logged_elapsed_ms_per_code_line", "warning_count",
    ]
    deltas = {}
    for key in keys:
        old, new = before["headline"].get(key), current["headline"].get(key)
        if isinstance(old, (int, float)) and isinstance(new, (int, float)):
            deltas[key] = {
                "before": old, "after": new, "delta": new - old,
                "percent_change": 100 * (new - old) / old if old else None,
            }
    old_modules = before.get("module_elapsed_seconds", {})
    module_deltas = {
        name: {"before": old_modules[name], "after": value, "delta": value - old_modules[name]}
        for name, value in current["module_elapsed_seconds"].items() if name in old_modules
    }
    caveats = []
    old_setup, setup = before["setup"], current["setup"]
    for field in ["timing_tool", "command", "host", "lean_version"]:
        old, new = old_setup.get(field), setup.get(field)
        if old is not None and new is not None and old != new:
            caveats.append(f"{field} differs; direct comparisons require review.")
    old_ratio = before["headline"].get("logged_elapsed_to_wall_ratio")
    new_ratio = current["headline"].get("logged_elapsed_to_wall_ratio")
    contention_signals = []
    if old_ratio and new_ratio and abs(new_ratio / old_ratio - 1) > 0.15:
        caveats.append("Logged elapsed/wall ratio differs by more than 15%; wall-time trend may reflect scheduling or contention.")
        if new_ratio > old_ratio:
            contention_signals.append("Logged elapsed/wall ratio increased by more than 15%.")
    old_cpu, new_cpu = before["headline"].get("cpu_percent"), current["headline"].get("cpu_percent")
    if old_cpu and new_cpu and abs(new_cpu / old_cpu - 1) > 0.15:
        caveats.append("Average measured CPU utilization differs by more than 15%; matched effective parallelism is not established.")
    old_user, new_user = before["headline"].get("user_cpu_seconds"), current["headline"].get("user_cpu_seconds")
    old_sum, new_sum = before["headline"].get("logged_module_elapsed_seconds"), current["headline"].get("logged_module_elapsed_seconds")
    if None not in (old_user, new_user, old_sum, new_sum) and new_user < old_user and new_sum > old_sum:
        contention_signals.append("User CPU fell while the sum of logged elapsed durations rose.")
    materially_up = sum(item["after"] > 1.15 * item["before"] for item in module_deltas.values() if item["before"] >= 1)
    materially_down = sum(item["after"] < 0.85 * item["before"] for item in module_deltas.values() if item["before"] >= 1)
    if materially_up >= 5 and materially_down >= 5:
        contention_signals.append("At least five modules grew and five shrank by more than 15%; review edited modules and load before attributing trends.")
    if len(contention_signals) >= 2:
        caveats.append("At least two contention signals fired; skip structural conclusions based solely on this build comparison.")
    if before["size"]["built_module_count"] != current["size"]["built_module_count"]:
        caveats.append("Built module counts differ; scope is not identical.")
    if not current["build_health"]["no_upstream_built"] or not before["build_health"]["no_upstream_built"]:
        caveats.append("A run compiled non-project targets; project-only timing claims are invalid.")
    if not current["build_health"].get("measurement_valid") or not before["build_health"].get("measurement_valid"):
        caveats.append("At least one run is not a validated complete project snapshot; do not interpret its before/after timings as a valid experiment.")
    caveats.append("Logged module elapsed durations are a contention-sensitive proxy, not CPU measurements.")
    old_families = before.get("module_families", {})
    family_deltas = {}
    for family in sorted(set(old_families) | set(current["module_families"])):
        old = old_families.get(family, {}).get("logged_elapsed_seconds", 0)
        new = current["module_families"].get(family, {}).get("logged_elapsed_seconds", 0)
        family_deltas[family] = {"before": old, "after": new, "delta": new - old}
    return {
        "baseline_source_commit": before["setup"].get("source_commit"),
        "headline_deltas": deltas,
        "heavy_tail_deltas": {
            tier: current["heavy_tail"][tier] - before["heavy_tail"].get(tier, 0)
            for tier in current["heavy_tail"]
        },
        "module_deltas": module_deltas,
        "family_deltas": family_deltas,
        "contention_signals": contention_signals,
        "caveats": caveats,
    }


def summarize(repo: Path, run: Path) -> dict[str, Any]:
    result = json.loads((run / "result.json").read_text())
    ref = result.get("source_commit") or result.get("commit")
    if not ref:
        raise ValueError("result.json must record source_commit (or commit)")
    sources = proof_sources(repo, ref)
    if not sources or "All" not in sources:
        raise ValueError("Recorded commit has no expected production proof sources/All root")
    graph = imports(sources)
    scope = reachable(graph, "All")
    log = parse_log((run / "build.txt").read_text(errors="replace"), set(sources))
    events = log["own_module_events"]
    by_module = defaultdict(list)
    for event in events:
        by_module[event["module"]].append(event)
    weights = {
        name: entries[-1]["seconds"]
        for name, entries in by_module.items() if entries[-1]["seconds"] is not None
    }
    elapsed_sum = sum(event["seconds"] for event in events if event["seconds"] is not None)
    stripped = {name: strip_comments(source) for name, source in sources.items()}
    comment_only = [name for name, source in stripped.items() if not source.strip()]
    counted = {name: source for name, source in sources.items() if name not in comment_only}
    code_lines = sum(sum(bool(line.strip()) for line in stripped[name].splitlines()) for name in counted)
    families = defaultdict(lambda: {"modules": 0, "logged_elapsed_seconds": 0.0})
    for name, seconds in weights.items():
        family = families[module_family(name)]
        family["modules"] += 1
        family["logged_elapsed_seconds"] += seconds
    wall = result.get("elapsed_seconds")
    caveats = [
        "This is a project-cold, dependency-warm build; upstream olean creation is outside scope.",
        "The sum of per-module logged elapsed durations is not cumulative CPU; simultaneous modules include overlap and contention.",
        "Maximum RSS follows the recorded timer's process/child accounting; it is not the sum of concurrent Lean process memory.",
        "No timing is imputed for own module events lacking elapsed values.",
        "Snapshot line counts include only the production proof library and four facade/entry modules; Comparator challenges and Audit probes are excluded.",
    ]
    duplicate_modules = {name: len(entries) for name, entries in by_module.items() if len(entries) > 1}
    if duplicate_modules:
        caveats.append("Some modules have repeated build events; per-module ranking uses the last, while event sum includes every build.")
    missing = sorted(scope - set(by_module))
    if missing:
        caveats.append("Some expected own modules have no Built event; a complete project-cold rebuild is not established.")
    legacy = [name for name, source in stripped.items() if not re.match(r"\s*module\b", source)]
    if legacy:
        caveats.append("Legacy Lean module syntax is retained; the skill's new module-header convention is not satisfied.")
    if log["upstream_built_events"]:
        caveats.append("Non-project Built events are present; inspect them and invalidate the timed run if they compile dependencies.")
    exit_status = result.get("exit_status", result.get("exit_code"))
    source_unchanged = result.get("source_snapshot_sha256") == result.get("source_snapshot_after_sha256") if "source_snapshot_sha256" in result and "source_snapshot_after_sha256" in result else None
    dependencies_unchanged = result.get("dependencies_before") == result.get("dependencies_after") if "dependencies_before" in result and "dependencies_after" in result else None
    complete_project_rebuild = set(by_module) == set(sources) and scope == set(sources)
    requirements = {
        "runner_status_passed": result.get("status") == "passed",
        "process_exit_zero": exit_status == 0,
        "complete_project_rebuild": complete_project_rebuild,
        "source_snapshot_unchanged": source_unchanged is True,
        "dependency_olean_snapshot_unchanged": dependencies_unchanged is True,
        "no_upstream_built": not log["upstream_built_events"],
        "no_error_messages": not log["errors"],
        "no_sorry_warnings_or_axioms": not log["sorry_lines"],
    }
    measurement_valid = all(requirements.values())
    if not measurement_valid:
        caveats.append("A successful raw process alone does not establish a valid snapshot; see measurement_invalid_reasons in build_health.")
    if len(weights) < len(by_module):
        caveats.append("Some own build events have no logged duration; the build can still be valid, but elapsed-sum and heavy-tail coverage are partial.")
    summary = {
        "schema_version": 1,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "run_directory": str(run),
        "setup": result,
        "size": {
            "source_commit": ref,
            "proof_module_count": len(sources),
            "non_comment_only_module_count": len(counted),
            "total_lines": sum(len(source.splitlines()) for source in counted.values()),
            "non_comment_code_lines": code_lines,
            "comment_only_modules_excluded": sorted(comment_only),
            "legacy_no_module_header_count": len(legacy),
            "all_import_closure_count": len(scope),
            "off_facade_modules": sorted(set(sources) - scope),
            "built_module_count": len(by_module),
            "timing_visible_module_count": len(weights),
            "timing_visible_fraction": len(weights) / len(by_module) if by_module else None,
            "expected_modules_without_build_event": missing,
            "repeated_module_builds": duplicate_modules,
        },
        "headline": {
            key: result.get(key) for key in [
                "elapsed_seconds", "user_cpu_seconds", "sys_cpu_seconds", "cpu_percent", "max_rss_bytes",
            ]
        } | {
            "logged_module_elapsed_seconds": elapsed_sum,
            "logged_elapsed_to_wall_ratio": elapsed_sum / wall if wall else None,
            "logged_elapsed_ms_per_code_line": 1000 * elapsed_sum / code_lines if code_lines else None,
            "planned_jobs": result.get("planned_jobs") or log["planned_jobs_from_log"],
            "own_module_build_events": len(events),
            "warning_count": len(log["warnings"]),
        },
        "build_health": {
            "exit_status": exit_status,
            "complete_project_rebuild": complete_project_rebuild,
            "measurement_valid": measurement_valid,
            "measurement_requirements": requirements,
            "measurement_invalid_reasons": [name for name, met in requirements.items() if not met],
            "error_count": len(log["errors"]),
            "sorry_warning_or_axiom_line_count": len(log["sorry_lines"]),
            "warning_count": len(log["warnings"]),
            "warning_kinds": log["warning_kinds"],
            "warning_linters": log["warning_linters"],
            "no_upstream_built": not log["upstream_built_events"],
            "upstream_built_events": log["upstream_built_events"],
            "replayed_event_count": log["replayed_event_count"],
            "source_snapshot_unchanged": source_unchanged,
            "dependency_olean_snapshot_unchanged": dependencies_unchanged,
            "heartbeat_overrides": [
                {"module": name, "line": i, "option": match[1], "value": match[2]}
                for name, source in stripped.items()
                for i, line in enumerate(source.splitlines(), 1)
                if (match := re.search(r"\bset_option\s+(\S*[Hh]eartbeats)\s+(\S+)", line))
            ],
            "linter_suppression_count": sum(len(re.findall(r"\bset_option\s+linter\.\S+\s+false\b", source)) for source in stripped.values()),
            "files_over_1500_lines": [
                {"module": name, "lines": len(source.splitlines())}
                for name, source in sources.items() if len(source.splitlines()) > 1500
            ],
            "warnings": log["warnings"],
            "errors": log["errors"],
            "sorry_lines": log["sorry_lines"],
        },
        "heavy_tail": {f"at_least_{threshold}s": sum(value >= threshold for value in weights.values()) for threshold in [10, 20, 30, 40]},
        "top_30_modules": [
            {"module": name, "logged_elapsed_seconds": seconds, "family": module_family(name)}
            for name, seconds in sorted(weights.items(), key=lambda x: (-x[1], x[0]))[:30]
        ],
        "module_elapsed_seconds": dict(sorted(weights.items())),
        "module_families": dict(sorted(families.items())),
        "weighted_import_path": weighted_path(graph, weights),
        "project_import_graph": graph,
        "caveats": caveats,
    }
    cpu = result.get("user_cpu_seconds")
    system = result.get("sys_cpu_seconds")
    cores = result.get("logical_cpus", result.get("logical_cpu_count", result.get("host_logical_cpu_count")))
    if isinstance(cpu, (int, float)) and isinstance(system, (int, float)) and isinstance(cores, int) and cores > 0:
        summary["host_work_floor_seconds"] = (cpu + system) / cores
        summary["caveats"].append("Host CPU work floor assumes all recorded logical cores are equally available; Apple performance/efficiency cores and competing load limit that model.")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("run_directory", type=Path)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compare", type=Path, help="Earlier summary.json for a before/after comparison")
    args = parser.parse_args()
    run = args.run_directory.resolve()
    summary = summarize(args.repo.resolve(), run)
    if args.compare:
        summary["comparison"] = comparison(summary, json.loads(args.compare.read_text()))
    output = args.output or run / "summary.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {output}; {summary['size']['built_module_count']} own modules, "
          f"{summary['headline']['warning_count']} warnings, "
          f"{summary['headline']['logged_module_elapsed_seconds']:.3f}s logged module elapsed sum.")


if __name__ == "__main__":
    main()
