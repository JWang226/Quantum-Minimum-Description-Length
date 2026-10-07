#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Python-only runner controls; synthetic snapshots are not Lean environments."""
import copy
import hashlib
from pathlib import Path
import tempfile
import unittest

from compare_cleanup_fingerprints import canonical, instance_blueprints
from run_cleanup_instance_witnesses import bind_fresh_pairs, evidence_path, find_exact_roots


def snapshots(omit=None, reverse=False):
    nodes, memo = [], {}

    def insert(tree):
        node = ["app", insert(tree[1]), insert(tree[2])] if tree[0] == "app" else tree
        key = canonical(node)
        if key not in memo:
            memo[key] = len(nodes)
            nodes.append(node)
        return memo[key]

    pairs = list(instance_blueprints().items())
    for identifier, pair in reversed(pairs) if reverse else pairs:
        for field in ("before_expr", "after_expr"):
            if (identifier, field) != omit:
                insert(pair[field])
    return {"schema_version": "qmdl-cleanup-fingerprints-v1",
            "nodes": nodes, "seed_provenance": {"identity": "registered"}}


def template():
    pairs = []
    for identifier, expected in instance_blueprints().items():
        row = {"id": identifier}
        for field in ("before_expr", "after_expr", "type_expr"):
            row[field] = expected[field]
            row[field + "_sha256"] = hashlib.sha256(canonical(expected[field]).encode()).hexdigest()
        pairs.append(row)
    return {"schema_version": "qmdl-cleanup-instance-pairs-v1",
            "before_source_provenance": {"identity": "registered"},
            "after_source_provenance": {"identity": "registered"}, "pairs": pairs}


class RunnerControls(unittest.TestCase):
    def setUp(self):
        self.before, self.after, self.input = snapshots(), snapshots(reverse=True), template()

    def bind(self):
        return bind_fresh_pairs(self.input, self.before, self.after, "beforeHash", "afterHash", "strictHash")

    def test_rebinds_actual_hashes_and_differently_numbered_roots(self):
        result = self.bind()
        self.assertEqual(result["before_snapshot_sha256"], "beforeHash")
        self.assertEqual(result["after_snapshot_sha256"], "afterHash")
        self.assertEqual(result["strict_comparison_sha256"], "strictHash")
        pair = result["pairs"][0]
        self.assertNotEqual(pair["before_snapshot_root"], pair["after_snapshot_root"])

    def test_never_changes_registered_trees(self):
        result = self.bind()
        for old, fresh in zip(self.input["pairs"], result["pairs"]):
            for field in ("before_expr", "after_expr", "type_expr"):
                self.assertEqual(old[field], fresh[field])

    def test_wrong_source_identity_rejected(self):
        self.before["seed_provenance"]["identity"] = "unreviewed"
        with self.assertRaisesRegex(ValueError, "source/pin/audit"):
            self.bind()

    def test_missing_pair_rejected(self):
        self.input["pairs"].pop()
        with self.assertRaisesRegex(ValueError, "Exactly"):
            self.bind()

    def test_duplicate_pair_rejected(self):
        self.input["pairs"][1] = copy.deepcopy(self.input["pairs"][0])
        with self.assertRaisesRegex(ValueError, "Exactly"):
            self.bind()

    def test_new_term_rejected_even_with_recomputed_digest(self):
        self.input["pairs"][0]["before_expr"] = ["const", ["str", ["anonymous"], "Nat"], []]
        self.input["pairs"][0]["before_expr_sha256"] = hashlib.sha256(
            canonical(self.input["pairs"][0]["before_expr"]).encode()).hexdigest()
        with self.assertRaisesRegex(ValueError, "Unregistered"):
            self.bind()

    def test_wrong_full_implicit_type_rejected(self):
        self.input["pairs"][1]["type_expr"] = self.input["pairs"][1]["type_expr"][1]
        with self.assertRaisesRegex(ValueError, "Unregistered"):
            self.bind()

    def test_wrong_tree_digest_rejected(self):
        self.input["pairs"][0]["before_expr_sha256"] = "wrong"
        with self.assertRaisesRegex(ValueError, "digest"):
            self.bind()

    def test_missing_exact_observed_term_rejected(self):
        self.before = snapshots(omit=("IntPartialOrder", "before_expr"))
        with self.assertRaisesRegex(ValueError, "absent"):
            self.bind()

    def test_future_dag_child_rejected(self):
        self.before["nodes"].append(["app", len(self.before["nodes"]), 0])
        with self.assertRaisesRegex(ValueError, "topologically"):
            self.bind()

    def test_unknown_expr_constructor_rejected(self):
        self.before["nodes"].append(["custom_node"])
        with self.assertRaisesRegex(ValueError, "Unknown"):
            self.bind()

    def test_whole_term_matching_does_not_match_head_alone(self):
        head = ["const", ["str", ["str", ["anonymous"], "PartialOrder"], "unrelated"], []]
        self.assertEqual(find_exact_roots(self.before, head), [])

    def test_safe_scratch_path_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            path, relative = evidence_path(root, Path(".verify-work/fresh/instance-witnesses.json"))
            self.assertEqual(relative, ".verify-work/fresh/instance-witnesses.json")
            self.assertTrue(path.is_relative_to(root))

    def test_absolute_and_parent_paths_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            for value in (Path("/tmp/out.json"), Path("../out.json"), Path("scratch/../out.json")):
                with self.assertRaises(ValueError):
                    evidence_path(root, value)

    def test_in_root_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / "target").mkdir()
            (root / "link").symlink_to(root / "target", target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "symlink"):
                evidence_path(root, Path("link/out.json"))


if __name__ == "__main__":
    unittest.main()
