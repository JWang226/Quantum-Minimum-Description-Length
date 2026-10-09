#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Run compiled acceptance/rejection controls for the physical specification guard.

All fixture declarations must elaborate before rejection can count as success.
Only temporary test fixtures contain deliberate proof holes. The guard starts
from theorem types, so the harmless expected root's hole must be ignored while
direct, definition-body and opaque-body specification leaks must be rejected.
This is a guard regression test, not a Lean/Comparator/Nanoda proof audit.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MODULE = "PhysicalSpecControls"
FIXTURE = """import FreeEntropy.CanonicalOrbit
noncomputable section
open Matrix
namespace PhysicalSpecControls
open FreeEntropy FreeEntropy.ExteriorRepresentation

-- The root body is deliberately a challenge hole and must not be traversed.
theorem good : True := by sorry
def definitionRoot : Prop := True

def hiddenState (s : FixedSpectrum 2 1) (mu : Fin 2 → ℕ)
    (U : Matrix.unitaryGroup (Fin 2) ℂ) := canonicalOrbitState s mu U

noncomputable opaque opaqueState (s : FixedSpectrum 2 1) (mu : Fin 2 → ℕ)
    (U : Matrix.unitaryGroup (Fin 2) ℂ) : Matrix (IrrepIndex mu) (IrrepIndex mu) ℂ :=
  canonicalOrbitState s mu U

theorem direct (s : FixedSpectrum 2 1) (mu : Fin 2 → ℕ)
    (U : Matrix.unitaryGroup (Fin 2) ℂ) :
    canonicalOrbitState s mu U = canonicalOrbitState s mu U := by sorry

theorem definitionBody (s : FixedSpectrum 2 1) (mu : Fin 2 → ℕ)
    (U : Matrix.unitaryGroup (Fin 2) ℂ) :
    hiddenState s mu U = hiddenState s mu U := by sorry

theorem opaqueBody (s : FixedSpectrum 2 1) (mu : Fin 2 → ℕ)
    (U : Matrix.unitaryGroup (Fin 2) ℂ) :
    opaqueState s mu U = opaqueState s mu U := by sorry

theorem otherRoot : good = good := rfl
end PhysicalSpecControls
"""


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lake-project", type=Path, default=ROOT / "lean",
                        help="Existing pinned Lean build with CanonicalOrbit already compiled")
    parser.add_argument("--report", type=Path,
                        help="Write source-bound success metadata after every control passes")
    args = parser.parse_args()
    project = args.lake_project.resolve()
    lake = shutil.which("lake") or str(Path.home() / ".elan/bin/lake")
    guard = ROOT / "scripts/check_physical_spec.lean"
    if not Path(lake).is_file() or not guard.is_file() or not (project / "lean-toolchain").is_file():
        parser.error("An installed Lake, the specification guard, and a pinned Lean project are required")
    started = datetime.now(timezone.utc).isoformat()

    def command(argv, **kwargs):
        return subprocess.run(argv, cwd=project, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, timeout=180, **kwargs)

    path_result = command([lake, "env", "printenv", "LEAN_PATH"])
    if path_result.returncode != 0:
        raise RuntimeError("Unable to read pinned Lean search path: " + path_result.stdout.decode())
    paths = path_result.stdout.decode().strip()
    outcomes = []
    with tempfile.TemporaryDirectory(prefix="qmdl-physical-spec-controls-") as temporary:
        work = Path(temporary)
        source = work / (MODULE + ".lean")
        olean = work / (MODULE + ".olean")
        source.write_text(FIXTURE)
        compile_result = command([lake, "env", "lean", "-R", str(work), "-o", str(olean), str(source)])
        if compile_result.returncode != 0 or not olean.is_file() or "error:" in compile_result.stdout.decode():
            raise AssertionError("Control fixture failed to elaborate; this is not an accepted rejection:\n"
                                 + compile_result.stdout.decode())
        environment = dict(os.environ, LEAN_PATH=str(work) + os.pathsep + paths)

        def check(label, names, reason=None):
            report = work / (label + ".json")
            result = command([lake, "env", "lean", "--run", str(guard), str(report), MODULE,
                              *[MODULE + "." + name for name in names]], env=environment)
            output = result.stdout.decode()
            item = {"id": label, "theorem_roots": [MODULE + "." + n for n in names],
                    "fixture_elaboration": "passed", "guard_exit_status": result.returncode,
                    "guard_output_sha256": sha(result.stdout)}
            if reason is None:
                if result.returncode != 0 or not report.is_file():
                    raise AssertionError("Valid expected theorem type rejected:\n" + output)
                data = json.loads(report.read_text())
                if (data["status"] != "passed" or data["module"] != MODULE
                        or any(root["root_proof_body_traversed"] for root in data["roots"])):
                    raise AssertionError("Valid guard report does not confirm type-only traversal")
                item.update({"status": "accepted", "guard_report_sha256": sha(report.read_bytes())})
            else:
                if result.returncode == 0 or reason not in output:
                    raise AssertionError(f"{label} was not rejected for {reason!r}:\n" + output)
                if report.exists():
                    raise AssertionError("Rejected control left a success report: " + label)
                item.update({"status": "rejected", "expected_reason": reason})
            outcomes.append(item)
            print(f"PHYSICAL SPEC CONTROL PASSED: {label} ({item['status']})", flush=True)

        check("valid_root_hole_excluded", ["good"])
        forbidden = "Forbidden constructed state/projector/proof dependency: FreeEntropy.ExteriorRepresentation.canonicalOrbitState"
        check("direct_state_dependency", ["direct"], forbidden)
        check("definition_body_dependency", ["definitionBody"], forbidden)
        check("opaque_body_dependency", ["opaqueBody"], forbidden)
        check("missing_root", ["missing"], "Missing expected theorem: PhysicalSpecControls.missing")
        check("non_theorem_root", ["definitionRoot"], "Expected root is not a theorem: PhysicalSpecControls.definitionRoot")
        check("root_used_in_another_type", ["good", "otherRoot"],
              "Challenge proof root referenced in expected type closure: PhysicalSpecControls.good")
        record = {
            "schema_version": "qmdl-physical-spec-controls-v1", "status": "passed",
            "started_at_utc": started, "completed_at_utc": datetime.now(timezone.utc).isoformat(),
            "mode": "fresh_compiled_guard_controls", "sandboxed": False,
            "lean_toolchain": (project / "lean-toolchain").read_text().strip(),
            "runner_sha256": sha(Path(__file__).read_bytes()), "guard_sha256": sha(guard.read_bytes()),
            "lake_manifest_sha256": sha((project / "lake-manifest.json").read_bytes()),
            "fixture_source_sha256": sha(source.read_bytes()), "fixture_olean_sha256": sha(olean.read_bytes()),
            "fixture_compile_output_sha256": sha(compile_result.stdout), "checks": outcomes,
            "policy": "All fixture declarations elaborated before guard controls ran. Accepted challenge proof body is deliberately excluded. Only rejection for each specified guard diagnostic counts; compilation failure is not a successful rejection. These controls do not certify the manuscript or production proofs.",
        }
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(record, indent=2) + "\n")
    print(f"PHYSICAL SPECIFICATION CONTROLS PASSED: {len(outcomes)} fresh compiled controls.")


if __name__ == "__main__":
    main()
