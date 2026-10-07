#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Python-only acceptance/rejection controls for cleanup expression comparison.

These small serialized environments exercise evidence-preservation safeguards.
They do not invoke Lean or claim that test fixtures are a checked Lean environment.
Run from the repository root: python3 scripts/test_cleanup_fingerprints.py
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import compare_cleanup_fingerprints as compare


PUBLIC_DATA = "FreeEntropy.publicData"
PUBLIC_FUNCTION = "FreeEntropy.publicFunction"
PUBLIC_THEOREM = "FreeEntropy.publicTheorem"
PUBLIC_WITNESS = "FreeEntropy.publicWitness"
OLD_PROOF = "_private.FreeEntropy.Fixture.1.FreeEntropy.bound"
NEW_PROOF = "_private.FreeEntropy.Fixture.0.FreeEntropy.bound"
DEAD_PROOF = "_private.FreeEntropy.Fixture.0.FreeEntropy.dead"


def name_tree(name):
    result = ["anonymous"]
    for component in name.split("."):
        result = (["num", result, int(component)] if component.isdecimal()
                  else ["str", result, component])
    return result


def declaration(name, kind, type_root, value_root=None, public=False):
    return {
        "name": name, "name_tree": name_tree(name), "kind": kind,
        "module": "FreeEntropy.Fixture", "public_audit_seed": public,
        "level_parameters": [], "type_root": type_root, "value_root": value_root,
        "value_class": "data" if value_root is not None else "proof_omitted",
        "is_unsafe": False, "is_partial": False,
    }


def fixture():
    """Include a data value whose proof component refers to the private helper."""
    nodes = [
        ["sort", ["zero"]],                                      # 0: Prop
        ["sort", ["succ", ["zero"]]],                          # 1: Type
        ["const", name_tree("Nat"), []],                         # 2: Nat
        ["const", name_tree("True"), []],                        # 3: True
        ["nat_literal", 7],                                      # 4: 7
        ["bvar", 0],                                             # 5: bound variable
        ["forall", name_tree("x"), 2, 2, "explicit"],           # 6: Nat -> Nat
        ["lam", name_tree("x"), 2, 5, "explicit"],              # 7: identity
        ["const", name_tree(OLD_PROOF), []],                      # 8: private proof
        ["lam", name_tree("x"), 2, 3, "explicit"],              # 9: fun _ => True
        ["const", name_tree("Subtype"), [["succ", ["zero"]]]], # 10
        ["app", 10, 2],                                          # 11
        ["app", 11, 9],                                          # 12: subtype type
        ["const", name_tree("Subtype.mk"), [["succ", ["zero"]]]], # 13
        ["app", 13, 2],                                          # 14
        ["app", 14, 9],                                          # 15
        ["app", 15, 4],                                          # 16
        ["app", 16, 8],                                          # 17: witness with proof
    ]
    declarations = [
        declaration(PUBLIC_DATA, "definition", 2, 4, public=True),
        declaration(PUBLIC_FUNCTION, "definition", 6, 7, public=True),
        declaration(PUBLIC_THEOREM, "theorem", 3, public=True),
        declaration(PUBLIC_WITNESS, "definition", 12, 17, public=True),
        declaration(OLD_PROOF, "theorem", 3),
        declaration(DEAD_PROOF, "theorem", 3),
    ]
    return {
        "schema_version": compare.SCHEMA,
        "seed_provenance": {
            "schema_version": "qmdl-cleanup-seeds-v1",
            "proof_sources_sha256": "0" * 64,
            "pin_sha256": {"lean-toolchain": "1" * 64, "lake-manifest.json": "2" * 64},
            "public_declarations": sorted(d["name"] for d in declarations if d["public_audit_seed"]),
        },
        "nodes": nodes, "declarations": declarations,
    }


class CleanupControls(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix="qmdl-cleanup-controls-")
        self.addCleanup(directory.cleanup)
        self.directory = Path(directory.name)
        self.before_path = self.directory / "before.json"
        self.after_path = self.directory / "after.json"
        self.before = fixture()
        self.after = copy.deepcopy(self.before)

    def compare(self, removed=(), renamed=()):
        self.before_path.write_text(json.dumps(self.before))
        self.after_path.write_text(json.dumps(self.after))
        return compare.compare(self.before_path, self.after_path, removed, renamed)

    @staticmethod
    def get(snapshot, name):
        return next(d for d in snapshot["declarations"] if d["name"] == name)

    def remove(self, name, update_seeds=False):
        self.after["declarations"].remove(self.get(self.after, name))
        if update_seeds:
            self.after["seed_provenance"]["public_declarations"].remove(name)

    def rename(self, old=OLD_PROOF, new=NEW_PROOF):
        item = self.get(self.after, old)
        item["name"], item["name_tree"] = new, name_tree(new)
        if item["public_audit_seed"]:
            names = self.after["seed_provenance"]["public_declarations"]
            names[names.index(old)] = new
        for node in self.after["nodes"]:
            if node[0] == "const" and node[1] == name_tree(old):
                node[1] = name_tree(new)

    def test_unchanged_environment_passes(self):
        result = self.compare()
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["counts"]["public_signature_changes"], 0)
        self.assertEqual(result["counts"]["data_value_changes"], 0)

    def test_node_numbering_does_not_determine_identity(self):
        # Permute independent leaves, then rewrite every actual reference.
        order = [5, 4, 3, 2, 1, 0] + list(range(6, len(self.after["nodes"])))
        inverse = {old: new for new, old in enumerate(order)}
        children = {"app": (1, 2), "lam": (2, 3), "forall": (2, 3),
                    "let": (2, 3, 4), "proj": (3,)}
        nodes = [copy.deepcopy(self.after["nodes"][i]) for i in order]
        for node in nodes:
            for position in children.get(node[0], ()):
                node[position] = inverse[node[position]]
        self.after["nodes"] = nodes
        for item in self.after["declarations"]:
            item["type_root"] = inverse[item["type_root"]]
            if item["value_root"] is not None:
                item["value_root"] = inverse[item["value_root"]]
        self.assertEqual(self.compare()["status"], "passed")

    def test_public_type_change_requires_review(self):
        self.get(self.after, PUBLIC_THEOREM)["type_root"] = 2
        result = self.compare()
        self.assertEqual(result["status"], "review_required")
        self.assertEqual(result["counts"]["public_signature_changes"], 1)

    def test_actual_data_value_change_requires_review(self):
        self.after["nodes"][4][1] = 8
        result = self.compare()
        self.assertEqual(result["status"], "review_required")
        self.assertGreaterEqual(result["counts"]["data_value_changes"], 1)

    def test_implicit_binder_change_requires_review(self):
        self.after["nodes"][6][4] = "implicit"
        self.assertEqual(self.compare()["status"], "review_required")

    def test_binder_name_change_is_not_silently_alpha_quotiented(self):
        self.after["nodes"][6][1] = name_tree("y")
        self.assertEqual(self.compare()["status"], "review_required")

    def test_hierarchical_numeric_name_is_not_a_string_name(self):
        numeric = ["num", name_tree("Private"), 1]
        string = ["str", name_tree("Private"), "1"]
        self.before["nodes"][8][1] = numeric
        self.after["nodes"][8][1] = string
        self.assertEqual(self.compare()["status"], "review_required")

    def test_universe_parameter_change_requires_review(self):
        self.get(self.after, PUBLIC_FUNCTION)["level_parameters"] = [name_tree("u")]
        self.assertEqual(self.compare()["status"], "review_required")

    def test_actual_universe_level_change_requires_review(self):
        self.after["nodes"][10][2] = [["succ", ["succ", ["zero"]]]]
        self.assertEqual(self.compare()["status"], "review_required")

    def test_unsafe_declaration_change_requires_review(self):
        self.get(self.after, PUBLIC_DATA)["is_unsafe"] = True
        self.assertEqual(self.compare()["status"], "review_required")

    def test_partial_declaration_change_requires_review(self):
        self.get(self.after, PUBLIC_DATA)["is_partial"] = True
        self.assertEqual(self.compare()["status"], "review_required")

    def test_differing_dependency_pins_require_review(self):
        self.after["seed_provenance"]["pin_sha256"]["lake-manifest.json"] = "3" * 64
        result = self.compare()
        self.assertFalse(result["same_dependency_pins"])
        self.assertEqual(result["status"], "review_required")

    def test_missing_public_seed_declaration_is_rejected(self):
        self.remove(PUBLIC_THEOREM)
        with self.assertRaisesRegex(ValueError, "differ from source seeds"):
            self.compare()

    def test_public_deletion_with_modified_seed_set_still_requires_review(self):
        self.remove(PUBLIC_THEOREM, update_seeds=True)
        result = self.compare()
        self.assertEqual(result["status"], "review_required")
        self.assertIn(PUBLIC_THEOREM, result["unexpected_removed_declarations"])

    def test_public_proof_deletion_cannot_receive_private_exception(self):
        self.remove(PUBLIC_THEOREM, update_seeds=True)
        with self.assertRaisesRegex(ValueError, "non-public proof helper"):
            self.compare(removed=[PUBLIC_THEOREM])

    def test_dead_private_proof_removal_needs_explicit_exception(self):
        self.remove(DEAD_PROOF)
        self.assertEqual(self.compare()["status"], "review_required")
        result = self.compare(removed=[DEAD_PROOF])
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["allowed_removed_auxiliary_proofs"], [DEAD_PROOF])

    def test_nonproof_deletion_cannot_receive_proof_exception(self):
        self.before["declarations"].append(declaration("FreeEntropy.privateData", "definition", 2, 4))
        with self.assertRaisesRegex(ValueError, "non-public proof helper"):
            self.compare(removed=["FreeEntropy.privateData"])

    def test_vacuous_removal_exception_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "does not occur"):
            self.compare(removed=[DEAD_PROOF])

    def test_exact_private_proof_ordinal_rename_is_accepted(self):
        self.rename()
        self.assertEqual(self.compare()["status"], "review_required")
        result = self.compare(renamed=[f"{OLD_PROOF}={NEW_PROOF}"])
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["counts"]["data_value_changes"], 0)
        self.assertEqual(result["reviewed_renamed_auxiliary_proofs"][0]["after_name"], NEW_PROOF)

    def test_renamed_proof_with_changed_type_is_rejected(self):
        self.rename()
        self.get(self.after, NEW_PROOF)["type_root"] = 2
        with self.assertRaisesRegex(ValueError, "different compiled signature"):
            self.compare(renamed=[f"{OLD_PROOF}={NEW_PROOF}"])

    def test_renamed_proof_with_changed_universe_parameters_is_rejected(self):
        self.rename()
        self.get(self.after, NEW_PROOF)["level_parameters"] = [name_tree("u")]
        with self.assertRaisesRegex(ValueError, "different compiled signature"):
            self.compare(renamed=[f"{OLD_PROOF}={NEW_PROOF}"])

    def test_public_proof_rename_exception_is_rejected(self):
        renamed = "FreeEntropy.changedTheorem"
        self.rename(PUBLIC_THEOREM, renamed)
        with self.assertRaisesRegex(ValueError, "non-public proposition proofs"):
            self.compare(renamed=[f"{PUBLIC_THEOREM}={renamed}"])

    def test_nonproof_rename_exception_is_rejected(self):
        for snapshot, name in ((self.before, OLD_PROOF), (self.after, OLD_PROOF)):
            item = self.get(snapshot, name)
            item.update(kind="definition", type_root=2, value_root=4, value_class="data")
        self.rename()
        with self.assertRaisesRegex(ValueError, "non-public proposition proofs"):
            self.compare(renamed=[f"{OLD_PROOF}={NEW_PROOF}"])

    def test_rename_cannot_hide_changed_data_value(self):
        self.rename()
        self.after["nodes"][4][1] = 8
        result = self.compare(renamed=[f"{OLD_PROOF}={NEW_PROOF}"])
        self.assertEqual(result["status"], "review_required")
        self.assertGreaterEqual(result["counts"]["data_value_changes"], 1)

    def test_unreviewed_generated_descendant_is_not_prefix_renamed(self):
        old_child, new_child = OLD_PROOF + ".proof_1", NEW_PROOF + ".proof_1"
        self.before["declarations"].append(declaration(old_child, "theorem", 3))
        self.after["declarations"].append(declaration(new_child, "theorem", 3))
        self.rename()
        result = self.compare(renamed=[f"{OLD_PROOF}={NEW_PROOF}"])
        self.assertEqual(result["status"], "review_required")
        self.assertIn(old_child, result["unexpected_removed_declarations"])
        self.assertIn(new_child, result["added_declarations"])

    def test_separately_reviewed_generated_proof_can_be_renamed(self):
        old_child, new_child = OLD_PROOF + ".proof_1", NEW_PROOF + ".proof_1"
        self.before["declarations"].append(declaration(old_child, "theorem", 3))
        self.after["declarations"].append(declaration(new_child, "theorem", 3))
        self.rename()
        self.assertEqual(self.compare(renamed=[f"{OLD_PROOF}={NEW_PROOF}",
                                             f"{old_child}={new_child}"])["status"], "passed")

    def test_wrong_identity_mapping_is_rejected(self):
        self.rename()
        with self.assertRaisesRegex(ValueError, "removed/added pair"):
            self.compare(renamed=[f"{OLD_PROOF}=Does.Not.Exist"])

    def test_existing_target_identity_is_not_a_rename(self):
        self.rename()
        with self.assertRaisesRegex(ValueError, "removed/added pair"):
            self.compare(renamed=[f"{OLD_PROOF}={DEAD_PROOF}"])

    def test_vacuous_identity_mapping_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "vacuous proof rename"):
            self.compare(renamed=[f"{OLD_PROOF}={OLD_PROOF}"])

    def test_duplicate_rename_mapping_is_rejected(self):
        self.rename()
        with self.assertRaisesRegex(ValueError, "duplicate proof rename"):
            self.compare(renamed=[f"{OLD_PROOF}={NEW_PROOF}", f"{OLD_PROOF}={NEW_PROOF}"])

    def test_expression_cycle_is_rejected(self):
        self.after["nodes"][6][2] = 6
        with self.assertRaisesRegex(ValueError, "not topologically ordered"):
            self.compare()

    def test_data_value_omission_is_rejected(self):
        self.get(self.after, PUBLIC_DATA)["value_root"] = None
        with self.assertRaisesRegex(ValueError, "value class and expression disagree"):
            self.compare()


class ReviewedInstanceControls(unittest.TestCase):
    """Synthetic evidence controls, never substituted for actual kernel runs."""

    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix="qmdl-instance-controls-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.before_path, self.after_path = self.root / "before.json", self.root / "after.json"
        self.strict_path = self.root / "strict.json"
        self.pairs_path, self.witnesses_path = self.root / "pairs.json", self.root / "witnesses.json"
        self.before = fixture()
        self.after = copy.deepcopy(self.before)
        self.blueprints = compare.instance_blueprints()
        pins = {}
        for filename in ("lean-toolchain", "lakefile.toml", "lake-manifest.json"):
            path = self.root / "lean" / filename
            path.parent.mkdir(exist_ok=True)
            path.write_text("test-fixture-" + filename + "\n")
            pins[filename] = compare.sha(path.read_bytes())
        for snapshot in (self.before, self.after):
            snapshot["seed_provenance"].update(pin_sha256=pins, lean_toolchain="test-fixture-toolchain")
        self.roots = {side: {} for side in ("before", "after")}
        for side, snapshot, field in (("before", self.before, "before_expr"),
                                      ("after", self.after, "after_expr")):
            for identifier, blueprint in self.blueprints.items():
                self.roots[side][identifier] = self.append_term(snapshot, blueprint[field])
        self.get(self.before, PUBLIC_DATA)["value_root"] = self.roots["before"]["IntPartialOrder"]
        self.get(self.after, PUBLIC_DATA)["value_root"] = self.roots["after"]["IntPartialOrder"]
        self.get(self.before, PUBLIC_FUNCTION)["type_root"] = self.roots["before"]["RealCharZero"]
        self.get(self.after, PUBLIC_FUNCTION)["type_root"] = self.roots["after"]["RealCharZero"]
        # An unchanged data value retains the OLD whole instance on BOTH sides.
        old_in_after = self.append_term(self.after, self.blueprints["IntPartialOrder"]["before_expr"])
        self.get(self.before, PUBLIC_WITNESS)["value_root"] = self.roots["before"]["IntPartialOrder"]
        self.get(self.after, PUBLIC_WITNESS)["value_root"] = old_in_after
        rows = []
        certificates = []
        for identifier, blueprint in self.blueprints.items():
            row = {"id": identifier, "before_snapshot_root": self.roots["before"][identifier],
                   "after_snapshot_root": self.roots["after"][identifier]}
            for field in ("before_expr", "after_expr", "type_expr"):
                row[field] = copy.deepcopy(blueprint[field])
                row[field + "_sha256"] = compare.sha(compare.canonical(row[field]).encode())
            rows.append(row)
            level = blueprint["equality_level"]
            eq = ["const", name_tree("Eq"), [level]]
            refl = ["const", name_tree("Eq.refl"), [level]]
            certificates.append({
                "id": identifier, **{field: copy.deepcopy(row[field]) for field in
                                     ("before_expr", "after_expr", "type_expr")},
                "inferred_before_type_expr": copy.deepcopy(blueprint["inferred_before_type_expr"]),
                "inferred_after_type_expr": copy.deepcopy(blueprint["inferred_after_type_expr"]),
                "equality_type_expr": ["app", ["app", ["app", eq, row["type_expr"]],
                                                        row["before_expr"]], row["after_expr"]],
                "eq_refl_proof_expr": ["app", ["app", refl, row["type_expr"]], row["before_expr"]],
                "kernel_eq_refl_checked": True,
                "theorem_name": "QMDLCleanupFoundationWitness." + identifier,
                "axioms": ["propext", "Classical.choice", "Quot.sound"],
                "axiom_policy_passed": True,
            })
        self.pairs = {"schema_version": "qmdl-cleanup-instance-pairs-v1", "pairs": rows}
        self.witnesses = {
            "schema_version": "qmdl-cleanup-instance-witnesses-v1", "status": "passed",
            "pairs": certificates, "kernel_check_explicitly_enabled": True,
            "project_modules_imported": False,
            "allowed_axioms": ["propext", "Classical.choice", "Quot.sound"],
            "foundation_imports": ["Mathlib.Data.Int.ConditionallyCompleteOrder",
                                   "Mathlib.Analysis.RCLike.Basic"],
        }
        helper = self.root / "scripts/check_cleanup_instance_pairs.lean"
        helper.parent.mkdir()
        helper.write_bytes(Path(compare.__file__).with_name("check_cleanup_instance_pairs.lean").read_bytes())
        log = self.root / "witnesses.txt"
        log.write_text("\n".join(
            f"Kernel-checked exact foundation pair {identifier}; axioms: fixture"
            for identifier in self.blueprints) + "\nKernel-checked 2 exact foundation instance pairs.\n")
        self.witnesses["execution_evidence"] = {
            "helper_path": "scripts/check_cleanup_instance_pairs.lean",
            "helper_sha256": compare.sha(helper.read_bytes()),
            "log_path": "witnesses.txt", "log_sha256": compare.sha(log.read_bytes()),
            "input_path": "pairs.json", "lean_toolchain": "test-fixture-toolchain",
            "pin_sha256": pins, "exit_status": 0,
        }
        self.bind()

    get = staticmethod(CleanupControls.get)

    @staticmethod
    def append_term(snapshot, tree):
        node = copy.deepcopy(tree)
        if node[0] == "app":
            node = ["app", ReviewedInstanceControls.append_term(snapshot, tree[1]),
                    ReviewedInstanceControls.append_term(snapshot, tree[2])]
        try:
            return snapshot["nodes"].index(node)
        except ValueError:
            snapshot["nodes"].append(node)
            return len(snapshot["nodes"]) - 1

    def write_review(self):
        self.pairs_path.write_text(json.dumps(self.pairs))
        self.witnesses["instance_pair_input"] = copy.deepcopy(self.pairs)
        self.witnesses["execution_evidence"]["input_sha256"] = compare.sha(self.pairs_path.read_bytes())
        self.witnesses_path.write_text(json.dumps(self.witnesses))

    def bind(self):
        self.before_path.write_text(json.dumps(self.before))
        self.after_path.write_text(json.dumps(self.after))
        self.strict = compare.compare(self.before_path, self.after_path, [])
        self.strict_path.write_text(json.dumps(self.strict))
        self.pairs.update(
            before_snapshot_sha256=compare.sha(self.before_path.read_bytes()),
            after_snapshot_sha256=compare.sha(self.after_path.read_bytes()),
            before_source_provenance=copy.deepcopy(self.before["seed_provenance"]),
            after_source_provenance=copy.deepcopy(self.after["seed_provenance"]),
            strict_comparison_sha256=compare.sha(self.strict_path.read_bytes()),
        )
        self.write_review()

    def run_review(self):
        return compare.compare_reviewed(self.before_path, self.after_path, [], (),
            self.strict_path, self.pairs_path, self.witnesses_path, self.root)

    def test_two_exact_pairs_pass_while_strict_differences_remain_visible(self):
        strict_bytes = self.strict_path.read_bytes()
        report = self.run_review()
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["strict_status"], "review_required")
        self.assertEqual(report["strict_counts"]["changed_declarations"], 2)
        self.assertEqual(report["counts"]["changed_declarations"], 0)
        self.assertEqual(self.strict_path.read_bytes(), strict_bytes)

    def test_unchanged_old_term_on_both_sides_is_canonicalized_consistently(self):
        report = self.run_review()
        self.assertEqual(report["status"], "passed")
        counts = report["instance_node_counts"]["after"]["IntPartialOrder"]
        self.assertEqual(counts["before_expr_matches"], 1)
        self.assertEqual(counts["after_expr_matches"], 1)
        self.assertEqual(counts["actual_substitutions"], 1)

    def test_different_raw_inferred_real_types_require_the_checked_explicit_type(self):
        row = self.witnesses["pairs"][1]
        self.assertNotEqual(row["inferred_before_type_expr"], row["inferred_after_type_expr"])
        self.assertEqual(self.run_review()["status"], "passed")

    def test_unrelated_public_type_change_remains_a_change(self):
        self.get(self.after, PUBLIC_THEOREM)["type_root"] = 2
        self.bind()
        report = self.run_review()
        self.assertEqual(report["status"], "review_required")
        self.assertEqual(report["counts"]["public_signature_changes"], 1)

    def test_unrelated_data_change_remains_a_change(self):
        for snapshot in (self.before, self.after):
            snapshot["declarations"].append(declaration("FreeEntropy.unrelatedData", "definition", 2, 4))
        self.after["nodes"][4][1] = 8
        self.bind()
        self.assertEqual(self.run_review()["status"], "review_required")

    def test_public_metadata_change_remains_a_change(self):
        self.get(self.after, PUBLIC_DATA)["is_unsafe"] = True
        self.bind()
        self.assertEqual(self.run_review()["status"], "review_required")

    def test_arbitrary_whole_expression_rule_is_rejected_even_with_rebound_hashes(self):
        row = self.pairs["pairs"][0]
        row["before_expr"] = ["const", name_tree("Nat"), []]
        row["before_expr_sha256"] = compare.sha(compare.canonical(row["before_expr"]).encode())
        self.witnesses["pairs"][0]["before_expr"] = copy.deepcopy(row["before_expr"])
        self.write_review()
        with self.assertRaisesRegex(ValueError, "unregistered whole instance"):
            self.run_review()

    def test_project_constant_pair_is_rejected(self):
        self.pairs["pairs"][0]["before_expr"] = ["const", name_tree(PUBLIC_DATA), []]
        self.write_review()
        with self.assertRaisesRegex(ValueError, "unregistered whole instance"):
            self.run_review()

    def test_wrapper_head_or_prefix_is_not_a_registered_whole_term(self):
        row = self.pairs["pairs"][0]
        row["before_expr"] = ["app", ["const", name_tree("id"), [["zero"]]], row["before_expr"]]
        self.write_review()
        with self.assertRaisesRegex(ValueError, "unregistered whole instance"):
            self.run_review()

    def test_open_or_nonapplication_term_is_rejected(self):
        self.pairs["pairs"][0]["before_expr"] = ["bvar", 0]
        self.write_review()
        with self.assertRaisesRegex(ValueError, "unregistered whole instance"):
            self.run_review()

    def test_pair_type_cannot_be_replaced(self):
        self.pairs["pairs"][0]["type_expr"] = ["const", name_tree("Nat"), []]
        self.write_review()
        with self.assertRaisesRegex(ValueError, "unregistered whole instance"):
            self.run_review()

    def test_unknown_pair_id_is_rejected(self):
        self.pairs["pairs"][0]["id"] = "Arbitrary"
        self.write_review()
        with self.assertRaisesRegex(ValueError, "unknown or duplicate"):
            self.run_review()

    def test_duplicate_pair_id_is_rejected(self):
        self.pairs["pairs"][1]["id"] = self.pairs["pairs"][0]["id"]
        self.write_review()
        with self.assertRaisesRegex(ValueError, "unknown or duplicate"):
            self.run_review()

    def test_extra_pair_is_rejected(self):
        self.pairs["pairs"].append(copy.deepcopy(self.pairs["pairs"][0]))
        self.write_review()
        with self.assertRaisesRegex(ValueError, "exactly two"):
            self.run_review()

    def test_missing_pair_is_rejected(self):
        self.pairs["pairs"].pop()
        self.write_review()
        with self.assertRaisesRegex(ValueError, "exactly two"):
            self.run_review()

    def test_unused_rule_cannot_receive_a_review_exception(self):
        self.get(self.after, PUBLIC_FUNCTION)["type_root"] = self.append_term(
            self.after, self.blueprints["RealCharZero"]["before_expr"])
        self.bind()
        with self.assertRaisesRegex(ValueError, "does not explain any preserved raw change"):
            self.run_review()

    def test_tampered_ast_hash_is_rejected(self):
        self.pairs["pairs"][0]["before_expr_sha256"] = "0" * 64
        self.write_review()
        with self.assertRaisesRegex(ValueError, "AST hash mismatch"):
            self.run_review()

    def test_wrong_snapshot_subterm_root_is_rejected(self):
        self.pairs["pairs"][0]["before_snapshot_root"] = 2
        self.write_review()
        with self.assertRaisesRegex(ValueError, "exact snapshot subterm"):
            self.run_review()

    def test_stale_snapshot_hash_is_rejected(self):
        self.pairs["after_snapshot_sha256"] = "0" * 64
        self.write_review()
        with self.assertRaisesRegex(ValueError, "stale instance-pair binding"):
            self.run_review()

    def test_stale_source_binding_is_rejected(self):
        self.pairs["before_source_provenance"]["proof_sources_sha256"] = "3" * 64
        self.write_review()
        with self.assertRaisesRegex(ValueError, "stale instance-pair binding"):
            self.run_review()

    def test_stale_strict_hash_is_rejected(self):
        self.pairs["strict_comparison_sha256"] = "0" * 64
        self.write_review()
        with self.assertRaisesRegex(ValueError, "stale instance-pair binding"):
            self.run_review()

    def test_forged_raw_verdict_is_rejected_after_rebinding(self):
        self.strict["counts"]["changed_declarations"] = 0
        self.strict_path.write_text(json.dumps(self.strict))
        self.pairs["strict_comparison_sha256"] = compare.sha(self.strict_path.read_bytes())
        self.write_review()
        with self.assertRaisesRegex(ValueError, "strict structural verdict differs"):
            self.run_review()

    def test_unchecked_or_nonfoundation_certificate_is_rejected(self):
        for field, value in (("kernel_check_explicitly_enabled", False), ("project_modules_imported", True)):
            with self.subTest(field=field):
                original = self.witnesses[field]
                self.witnesses[field] = value
                self.write_review()
                with self.assertRaisesRegex(ValueError, "foundation-only"):
                    self.run_review()
                self.witnesses[field] = original

    def test_unchecked_pair_is_rejected(self):
        self.witnesses["pairs"][0]["kernel_eq_refl_checked"] = False
        self.write_review()
        with self.assertRaisesRegex(ValueError, "unchecked instance equality"):
            self.run_review()

    def test_nonliteral_reflexivity_certificate_is_rejected(self):
        self.witnesses["pairs"][0]["eq_refl_proof_expr"] = ["const", name_tree("True.intro"), []]
        self.write_review()
        with self.assertRaisesRegex(ValueError, "literal typed Eq.refl"):
            self.run_review()

    def test_unregistered_raw_inferred_type_is_rejected(self):
        self.witnesses["pairs"][1]["inferred_before_type_expr"] = self.blueprints["RealCharZero"]["type_expr"]
        self.write_review()
        with self.assertRaisesRegex(ValueError, "unregistered inferred instance type"):
            self.run_review()

    def test_wrong_witness_name_is_rejected(self):
        self.witnesses["pairs"][0]["theorem_name"] = PUBLIC_THEOREM
        self.write_review()
        with self.assertRaisesRegex(ValueError, "invalid foundation witness"):
            self.run_review()

    def test_custom_witness_axiom_is_rejected(self):
        self.witnesses["pairs"][0]["axioms"].append("FreeEntropy.fakeAxiom")
        self.write_review()
        with self.assertRaisesRegex(ValueError, "unreviewed axioms"):
            self.run_review()

    def test_unsuccessful_execution_is_rejected(self):
        for status in (1, False):
            with self.subTest(status=status):
                self.witnesses["execution_evidence"]["exit_status"] = status
                self.write_review()
                with self.assertRaisesRegex(ValueError, "did not succeed"):
                    self.run_review()

    def test_helper_log_and_current_pin_byte_tampering_is_rejected(self):
        paths = ("scripts/check_cleanup_instance_pairs.lean", "witnesses.txt", "lean/lake-manifest.json")
        for path in paths:
            with self.subTest(path=path):
                target = self.root / path
                original = target.read_bytes()
                target.write_bytes(original + b"tampered\n")
                with self.assertRaises(ValueError):
                    self.run_review()
                target.write_bytes(original)

    def test_rebound_log_without_success_verdict_is_rejected(self):
        (self.root / "witnesses.txt").write_text("Not a successful witness run.\n")
        self.witnesses["execution_evidence"]["log_sha256"] = compare.sha((self.root / "witnesses.txt").read_bytes())
        self.write_review()
        with self.assertRaisesRegex(ValueError, "lacks the two successful"):
            self.run_review()

    def test_absolute_and_escape_evidence_paths_are_rejected(self):
        for path in ("/tmp/witnesses.txt", "../witnesses.txt"):
            with self.subTest(path=path):
                self.witnesses["execution_evidence"]["log_path"] = path
                self.write_review()
                with self.assertRaisesRegex(ValueError, "unsafe public evidence"):
                    self.run_review()

    def test_local_scratch_evidence_and_copied_helper_are_accepted(self):
        scratch = self.root / ".verify-work/instance-control"
        scratch.mkdir(parents=True)
        execution = self.witnesses["execution_evidence"]
        for kind in ("input", "log", "helper"):
            old_path = self.root / execution[kind + "_path"]
            new_path = scratch / old_path.name
            new_path.write_bytes(old_path.read_bytes())
            execution[kind + "_path"] = new_path.relative_to(self.root).as_posix()
        self.write_review()
        (scratch / "pairs.json").write_bytes(self.pairs_path.read_bytes())
        self.assertEqual(self.run_review()["status"], "passed")

    def test_changed_helper_is_rejected_even_after_its_digest_is_rebound(self):
        path = self.root / self.witnesses["execution_evidence"]["helper_path"]
        path.write_bytes(path.read_bytes() + b"\n-- Modified helper\n")
        self.witnesses["execution_evidence"]["helper_sha256"] = compare.sha(path.read_bytes())
        self.write_review()
        with self.assertRaisesRegex(ValueError, "differs from the published/copied helper"):
            self.run_review()

    def test_symlink_evidence_is_rejected(self):
        (self.root / "alias.txt").symlink_to(self.root / "witnesses.txt")
        self.witnesses["execution_evidence"]["log_path"] = "alias.txt"
        self.write_review()
        with self.assertRaisesRegex(ValueError, "symlink in public evidence"):
            self.run_review()

    def test_cli_requires_the_complete_review_evidence_set(self):
        with patch("sys.argv", ["compare", str(self.before_path), str(self.after_path),
                                "--report", str(self.root / "reviewed.json"),
                                "--reviewed-instance-pairs", str(self.pairs_path)]):
            with self.assertRaises(SystemExit) as error:
                compare.main()
            self.assertEqual(error.exception.code, 1)

    def test_cli_cannot_overwrite_strict_report(self):
        original = self.strict_path.read_bytes()
        with patch("sys.argv", ["compare", str(self.before_path), str(self.after_path),
                "--report", str(self.strict_path), "--strict-report", str(self.strict_path),
                "--reviewed-instance-pairs", str(self.pairs_path),
                "--instance-witnesses", str(self.witnesses_path), "--evidence-root", str(self.root)]):
            with self.assertRaises(SystemExit) as error:
                compare.main()
            self.assertEqual(error.exception.code, 1)
        self.assertEqual(self.strict_path.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
