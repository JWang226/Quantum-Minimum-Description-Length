#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Read-only source import analysis; never runs Lean or changes project files.

Run from the repository root:
  python3 metadata/elaboration/2026-10-06/static_import_closure.py \
    --output .verify-work/elaboration-2026-10-06/static-import-closure.json

The two scenarios override only FreeEntropy.GTDeterminant's import header.
Project and Mathlib source imports are expanded. Other names are counted as
unexpanded leaves: these are not complete Lean environment module counts.
"""
from __future__ import annotations

import argparse
import functools
import hashlib
import json
import pathlib
import re


BASE_IMPORTS = [
    "Mathlib.LinearAlgebra.Vandermonde",
    "Mathlib.RingTheory.Binomial",
    "Mathlib.Algebra.BigOperators.Intervals",
    "Mathlib.Data.Int.Interval",
    "Mathlib.Data.Real.Basic",
]
SCENARIOS = {
    "before": BASE_IMPORTS + ["Mathlib.Tactic"],
    "after": BASE_IMPORTS
    + ["Mathlib.Tactic.Linarith", "Mathlib.Tactic.Positivity"],
}
PROVIDERS = {
    "linear_combination": "Mathlib.Tactic.LinearCombination",
    "noncomm_ring": "Mathlib.Tactic.NoncommRing",
    "abel": "Mathlib.Tactic.Abel",
    "gcongr": "Mathlib.Tactic.GCongr",
    "filter_upwards": "Mathlib.Tactic.FilterUpwards",
    "fun_prop": "Mathlib.Tactic.FunProp",
    "continuity": "Mathlib.Tactic.Continuity",
    "fin_cases": "Mathlib.Tactic.FinCases",
    "tauto": "Mathlib.Tactic.Tauto",
    "ring_nf": "Mathlib.Tactic.Ring",
    "field_simp": "Mathlib.Tactic.FieldSimp",
    "norm_num": "Mathlib.Tactic.NormNum",
    "positivity": "Mathlib.Tactic.Positivity",
    "nlinarith": "Mathlib.Tactic.Linarith",
    "linarith": "Mathlib.Tactic.Linarith",
    "convert": "Mathlib.Tactic.Convert",
}
IMPORT_PATTERN = re.compile(
    r"(?m)^[ \t]*(?:(?:public|meta)\s+)*import[ \t]+([^\n]+)"
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=pathlib.Path, default=pathlib.Path("."))
    parser.add_argument("--output", type=pathlib.Path)
    args = parser.parse_args()
    repo = args.project.resolve()
    lean = repo / "lean"
    mathlib = lean / ".lake/packages/mathlib"
    files_read: dict[str, str] = {}

    def source_path(name: str) -> pathlib.Path | None:
        relative = pathlib.Path(name.replace(".", "/") + ".lean")
        if name.startswith("FreeEntropy."):
            return lean / relative
        if name == "Mathlib" or name.startswith("Mathlib."):
            return mathlib / relative
        return None

    @functools.cache
    def direct(name: str) -> tuple[str, ...]:
        path = source_path(name)
        if path is None or not path.is_file():
            return ()
        data = path.read_bytes()
        files_read[name] = hashlib.sha256(data).hexdigest()
        # Match the method used for the initial estimate. Import declarations
        # occur in these source headers. Stopping at the module docstring avoids
        # treating documentation examples (e.g. Exponential.lean) as imports.
        header = data.decode().split("/-!", 1)[0]
        header = re.sub(r"/\-.*?-/", "", header, flags=re.S)
        return tuple(
            name
            for match in IMPORT_PATTERN.finditer(header)
            for name in match.group(1).split("--", 1)[0].split()
        )

    def closure(seeds: list[str], scenario: str) -> set[str]:
        todo = list(seeds)
        seen: set[str] = set()
        while todo:
            name = todo.pop()
            if name in seen:
                continue
            seen.add(name)
            todo.extend(
                SCENARIOS[scenario]
                if name == "FreeEntropy.GTDeterminant"
                else direct(name)
            )
        return seen

    def counts(names: set[str]) -> dict[str, int]:
        project = sum(
            name.startswith("FreeEntropy.") and source_path(name).is_file()
            for name in names
        )
        mathlib_count = sum(
            (name == "Mathlib" or name.startswith("Mathlib."))
            and source_path(name).is_file()
            for name in names
        )
        missing = sum(
            source_path(name) is not None and not source_path(name).is_file()
            for name in names
        )
        return {
            "total_module_names": len(names),
            "expanded_project_files": project,
            "expanded_mathlib_files": mathlib_count,
            "unexpanded_external_names": len(names) - project - mathlib_count - missing,
            "missing_project_or_mathlib_sources": missing,
        }

    target = {
        scenario: closure(SCENARIOS[scenario], scenario)
        for scenario in SCENARIOS
    }
    consumers: list[dict] = []
    warnings: list[dict[str, str]] = []
    for path in sorted((lean / "FreeEntropy").glob("*.lean")):
        name = "FreeEntropy." + path.stem
        before = closure([name], "before")
        if "FreeEntropy.GTDeterminant" not in before:
            continue
        after = closure([name], "after")
        consumers.append(
            {
                "module": name,
                "before": counts(before),
                "after": counts(after),
                "removed_module_names": len(before - after),
                "umbrella_present_after": "Mathlib.Tactic" in after,
            }
        )
        text = path.read_text()
        for tactic, provider in PROVIDERS.items():
            if (
                re.search(r"\b" + tactic + r"\b", text)
                and provider in before
                and provider not in after
            ):
                warnings.append({"module": name, "tactic": tactic, "provider": provider})

    result = {
        "version": 1,
        "analysis_date": "2026-10-06",
        "status": "static_prediction_no_lean_execution",
        "method": {
            "expanded_sources": ["lean/FreeEntropy/*.lean", "Mathlib/**/*.lean"],
            "external_names": "Counted as unexpanded leaves, including Lean and other packages.",
            "parser": "Import headers before the first /-! module documentation; block and line comments removed; public/meta modifiers accepted.",
            "scope": "Scenario override changes only FreeEntropy.GTDeterminant imports. Target dependency counts exclude GTDeterminant itself; consumer counts include the named root.",
            "tactic_screen": "Lexical usage check for listed common tactics against source provider closures; neither an exhaustive tactic analysis nor an elaboration pass.",
            "limitations": [
                "Source import closure is not the compiled Lean environment closure.",
                "Unexpanded external modules may themselves have further imports.",
                "Consumers must be elaborated after the actual import edit.",
                "This method assumes imports precede module documentation in the traversed files.",
            ],
        },
        "scenario_imports": SCENARIOS,
        "target_dependency_counts": {s: counts(target[s]) for s in SCENARIOS},
        "target_removed_module_names": len(target["before"] - target["after"]),
        "target_removed_names": sorted(target["before"] - target["after"]),
        "target_added_names": sorted(target["after"] - target["before"]),
        "project_consumer_count": len(consumers),
        "consumers_without_umbrella_after": sum(not c["umbrella_present_after"] for c in consumers),
        "project_consumers": consumers,
        "tactic_providers_screened": PROVIDERS,
        "potential_tactic_import_breaks": warnings,
        "input_bindings": {
            "lean_toolchain": (lean / "lean-toolchain").read_text().strip(),
            "lake_manifest_sha256": hashlib.sha256((lean / "lake-manifest.json").read_bytes()).hexdigest(),
            "traversed_source_sha256": dict(sorted(files_read.items())),
            "calculation_script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        },
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
        print(json.dumps({"output": str(args.output), "target_dependency_counts": result["target_dependency_counts"], "project_consumer_count": len(consumers), "potential_tactic_import_breaks": warnings}, indent=2))
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
