#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Small safety and evidence controls for the elaboration reproducer.

Uses disposable directories and synthetic logs. Never invokes Lean, Lake,
project benchmarks, or dependency setup.

Run: python3 scripts/test_elaboration_tools.py
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parent


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BENCHMARK = load("benchmark_elaboration")
SUMMARY = load("summarize_elaboration")
PROFILE = load("profile_elaboration")


def write(path, contents=b"preserve me"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(contents)
    return path


class ArtifactSafetyControls(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="qmdl-elaboration-controls-")
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name).resolve()
        self.root = self.directory / "repo"
        self.lean = self.root / "lean"
        self.build = self.lean / ".lake/build"
        self.library = self.build / "lib/lean"
        self.ir = self.build / "ir"
        self.library.mkdir(parents=True)
        self.ir.mkdir(parents=True)
        self.addCleanup(patch.stopall)
        patch.object(BENCHMARK, "ROOT", self.root).start()
        patch.object(BENCHMARK, "LEAN", self.lean).start()

    def test_invalidation_preserves_dependencies_comparator_and_audit(self):
        dependency = write(self.lean / ".lake/packages/mathlib/.lake/build/lib/lean/Mathlib/Basic.olean")
        comparator = write(self.library / "ComparatorChallenges/Challenge.olean")
        comparator_root = write(self.library / "ComparatorChallenges.olean")
        audit = write(self.library / "Audit.olean")
        own = []
        for name in BENCHMARK.ROOTS:
            own.extend([
                write(self.library / (name + ".olean")),
                write(self.library / (name + ".ilean")),
                write(self.library / (name + ".olean.hash")),
                write(self.library / (name + ".trace")),
                write(self.ir / (name + ".c")),
                write(self.ir / (name + ".setup.json")),
            ])
        own.extend([
            write(self.library / "FreeEntropy/Proof.olean"),
            write(self.ir / "FreeEntropy/Proof.c"),
        ])
        before = BENCHMARK.dependencies()
        removed = BENCHMARK.invalidate_own()
        self.assertTrue(removed)
        self.assertTrue(all(not path.exists() for path in own))
        for path in [dependency, comparator, comparator_root, audit]:
            self.assertEqual(path.read_bytes(), b"preserve me")
        self.assertEqual(BENCHMARK.dependencies(), before)

    def test_shared_build_symlink_is_rejected_without_deleting_contents(self):
        import shutil
        shutil.rmtree(self.build)
        shared = self.directory / "shared-build"
        marker = write(shared / "lib/lean/FreeEntropy/Proof.olean")
        self.build.symlink_to(shared, target_is_directory=True)
        with self.assertRaises(ValueError):
            BENCHMARK.invalidate_own()
        self.assertEqual(marker.read_bytes(), b"preserve me")

    def test_escaping_own_artifact_symlink_is_rejected(self):
        outside = self.directory / "outside"
        marker = write(outside / "Proof.olean")
        (self.library / "FreeEntropy").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            BENCHMARK.invalidate_own()
        self.assertEqual(marker.read_bytes(), b"preserve me")

    def test_dangling_escaping_symlink_is_rejected(self):
        (self.library / "FreeEntropy.olean").symlink_to(self.directory / "missing-external.olean")
        with self.assertRaises(ValueError):
            BENCHMARK.invalidate_own()

    def test_all_paths_are_validated_before_any_own_artifact_is_deleted(self):
        first = write(self.library / "FreeEntropy/Proof.olean")
        outside = write(self.directory / "external-theorem.olean")
        (self.library / "Theorem1.olean").symlink_to(outside)
        with self.assertRaises(ValueError):
            BENCHMARK.invalidate_own()
        self.assertTrue(first.exists(), "preflight rejection must precede all artifact deletion")
        self.assertEqual(first.read_bytes(), b"preserve me")
        self.assertEqual(outside.read_bytes(), b"preserve me")

    def test_intermediate_library_path_cannot_escape_to_another_checkout(self):
        self.library.rmdir()
        outside = self.directory / "other-checkout-library"
        marker = write(outside / "FreeEntropy/Proof.olean")
        self.library.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            BENCHMARK.invalidate_own()
        self.assertEqual(marker.read_bytes(), b"preserve me")


class LogEvidenceControls(unittest.TestCase):
    MODULES = {"FreeEntropy.A", "FreeEntropy.B", "All"}

    def test_warning_success_and_millisecond_events_remain_visible(self):
        log = """✔ [1/8] Built FreeEntropy.A (2.5s)
⚠ [2/8] Built FreeEntropy.B (925ms)
warning: FreeEntropy/B.lean:9:3: This simp argument is unused:
  helper
Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
✔ [3/8] Built All (8ms)
"""
        parsed = SUMMARY.parse_log(log, self.MODULES)
        self.assertEqual(len(parsed["own_module_events"]), 3)
        self.assertEqual([event["seconds"] for event in parsed["own_module_events"]], [2.5, 0.925, 0.008])
        self.assertEqual(parsed["planned_jobs_from_log"], 8)
        self.assertEqual(parsed["warning_linters"], {"linter.unusedSimpArgs": 1})
        self.assertEqual(parsed["upstream_built_events"], [])

    def test_diagnostic_text_cannot_masquerade_as_upstream_compilation(self):
        log = """warning: FreeEntropy/A.lean:2:0: string literal `Built Mathlib.Basic (12s)` is unused
info: sample output: [99/100] Built Mathlib.Bad (20s)
✔ [1/3] Replayed Mathlib.Basic
✔ [2/3] Built FreeEntropy.A (1s)
"""
        parsed = SUMMARY.parse_log(log, self.MODULES)
        self.assertEqual(parsed["upstream_built_events"], [])
        self.assertEqual(len(parsed["own_module_events"]), 1)

    def test_actual_upstream_compile_is_reported_but_own_ir_is_not_upstream(self):
        parsed = SUMMARY.parse_log("""✔ [1/3] Built Mathlib.Basic (2s)
✔ [2/3] Built FreeEntropy.A:c.o (60ms)
✔ [3/3] Built FreeEntropy.A (1s)
""", self.MODULES)
        self.assertEqual([event["target"] for event in parsed["upstream_built_events"]], ["Mathlib.Basic"])
        self.assertEqual(len(parsed["own_module_events"]), 1)
        self.assertEqual(parsed["build_events"][1]["facet"], "c.o")

    def test_linter_note_is_attributed_to_its_warning_only(self):
        parsed = SUMMARY.parse_log("""⚠ [1/3] Built FreeEntropy.A (2s)
warning: FreeEntropy/A.lean:2:0: This simp argument is unused:
Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
warning: FreeEntropy/A.lean:3:0: automatically included section variable(s) unused in theorem `x`:
Note: This linter can be disabled with `set_option linter.unusedSectionVars false`
✔ [2/3] Built FreeEntropy.B (1s)
""", self.MODULES)
        self.assertEqual([warning["linter"] for warning in parsed["warnings"]], ["linter.unusedSimpArgs", "linter.unusedSectionVars"])

    def test_replayed_only_run_is_detected_as_missing_every_own_build(self):
        with tempfile.TemporaryDirectory(prefix="qmdl-elaboration-log-") as temporary:
            run = Path(temporary)
            (run / "result.json").write_text(json.dumps({
                "source_commit": "fixture", "status": "passed", "exit_status": 0,
                "elapsed_seconds": 1.0, "user_cpu_seconds": 0.2, "sys_cpu_seconds": 0.1,
            }))
            (run / "build.txt").write_text("✔ [1/3] Replayed FreeEntropy.A\n✔ [2/3] Replayed All\nBuild completed successfully (3 jobs).\n")
            sources = {"FreeEntropy.A": "theorem a : True := by trivial\n", "All": "import FreeEntropy.A\n"}
            with patch.object(SUMMARY, "proof_sources", return_value=sources):
                result = SUMMARY.summarize(run, run)
            self.assertEqual(result["size"]["built_module_count"], 0)
            self.assertEqual(result["size"]["expected_modules_without_build_event"], ["All", "FreeEntropy.A"])
            self.assertTrue(any("complete project-cold rebuild is not established" in text for text in result["caveats"]))

    def test_missing_source_commit_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix="qmdl-elaboration-log-") as temporary:
            run = Path(temporary)
            (run / "result.json").write_text("{}")
            with self.assertRaisesRegex(ValueError, "source_commit"):
                SUMMARY.summarize(run, run)

    def test_unrelated_comments_do_not_create_import_dependencies(self):
        graph = SUMMARY.imports({
            "All": "import FreeEntropy.A\n/- import FreeEntropy.B /- nested -/ -/\n",
            "FreeEntropy.A": "-- import FreeEntropy.B\ntheorem a : True := by trivial\n",
            "FreeEntropy.B": "theorem b : True := by trivial\n",
        })
        self.assertEqual(SUMMARY.reachable(graph, "All"), {"All", "FreeEntropy.A"})

    def test_weighted_path_tracks_dependency_chain_not_sum_of_parallel_siblings(self):
        graph = {"All": ["FreeEntropy.A", "FreeEntropy.B"], "FreeEntropy.A": [], "FreeEntropy.B": []}
        value = SUMMARY.weighted_path(graph, {"All": 1.0, "FreeEntropy.A": 5.0, "FreeEntropy.B": 8.0})
        self.assertEqual(value["logged_elapsed_seconds"], 9.0)
        self.assertEqual(value["modules_dependency_first"], ["FreeEntropy.B", "All"])


class ProfileEvidenceControls(unittest.TestCase):
    OUTPUT = """cumulative profiling times:
  elaboration: 1.2s
  import: 2.0s
\tCommand being timed: "mock lean"
\tUser time (seconds): 3.20
\tSystem time (seconds): 0.10
\tElapsed (wall clock) time (h:mm:ss or m:ss): 0:03.40
"""

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="qmdl-profile-controls-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.source = write(self.root / "lean/FreeEntropy/A.lean", b"theorem a : True := by trivial\n")
        self.output = self.root / "profiles"
        self.addCleanup(patch.stopall)
        patch.object(PROFILE, "ROOT", self.root).start()
        patch.object(PROFILE.shutil, "which", side_effect=lambda binary: "/mock/" + binary).start()

    def argv(self, module="FreeEntropy.A", repeat=1):
        return ["profile_elaboration.py", "--output", str(self.output), "--modules", module, "--repeat", str(repeat)]

    def test_profile_never_requests_output_artifacts_and_retains_phase_evidence(self):
        result = subprocess.CompletedProcess([], 0, self.OUTPUT)
        with patch.object(PROFILE.sys, "argv", self.argv(repeat=2)), patch.object(PROFILE.subprocess, "run", return_value=result) as run:
            PROFILE.main()
        self.assertEqual(run.call_count, 2)
        for call in run.call_args_list:
            command = call.args[0]
            self.assertIn("--profile", command)
            self.assertFalse({"-o", "--o", "-i", "--i", "-c", "--c"} & set(command))
        recorded = json.loads((self.output / "profiles.json").read_text())
        self.assertEqual(len(recorded["samples"]), 2)
        self.assertIn("elaboration: 1.2s", recorded["samples"][0]["cumulative_profile_block"])
        self.assertNotIn("Command being timed", recorded["samples"][0]["cumulative_profile_block"])

    def test_profile_rejects_external_module_without_invoking_any_process(self):
        with patch.object(PROFILE.sys, "argv", self.argv(module="Mathlib.Basic")), patch.object(PROFILE.subprocess, "run") as run:
            with self.assertRaises(ValueError):
                PROFILE.main()
        run.assert_not_called()

    def test_profile_does_not_accept_a_source_that_changed_during_measurement(self):
        def changed_source(*args, **kwargs):
            self.source.write_text("theorem a : True := True.intro\n")
            return subprocess.CompletedProcess([], 0, self.OUTPUT)

        with patch.object(PROFILE.sys, "argv", self.argv()), patch.object(PROFILE.subprocess, "run", side_effect=changed_source):
            with self.assertRaises((ValueError, SystemExit)):
                PROFILE.main()


if __name__ == "__main__":
    unittest.main(verbosity=2)
