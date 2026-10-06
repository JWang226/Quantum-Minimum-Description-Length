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


if __name__ == "__main__":
    unittest.main()
