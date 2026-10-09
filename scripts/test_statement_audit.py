#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Negative controls for audit freshness and source-inventory validation."""
import copy
import unittest
from unittest.mock import patch

import check_statement_audit as audit


class AuditControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snapshot = audit.audited_snapshot(audit.ROOT)
        cls.reviewed_root = cls.snapshot.__enter__()

    @classmethod
    def tearDownClass(cls):
        cls.snapshot.__exit__(None, None, None)

    def setUp(self):
        root_patch = patch.object(audit, "ROOT", self.reviewed_root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        self.coverage = audit.read_json(audit.ROOT / audit.AUDIT / "source-coverage.json")

    def test_current_records(self):
        audit.check(audit.ROOT)

    def test_omitted_label_even_with_recounted_summary(self):
        data = copy.deepcopy(self.coverage)
        item = next(i for i in data["inventory"] if i["kind"] == "label")
        data["inventory"].remove(item)
        data["summary"]["inventory_items"] -= 1
        data["summary"]["inventory_by_kind"]["label"] -= 1
        data["summary"]["excluded_items" if item["disposition"] == "EXCLUDED" else "mapped_items"] -= 1
        with self.assertRaisesRegex(ValueError, "TeX inventory differs"):
            audit.check_coverage(audit.ROOT, data)

    def test_empty_graph_edges(self):
        self.coverage["edges"] = []
        with self.assertRaisesRegex(ValueError, "outside selected root closure"):
            audit.check_coverage(audit.ROOT, self.coverage)

    def test_stale_closure_size(self):
        self.coverage["summary"]["root_closure_sizes"]["thm:main"] = 1
        with self.assertRaisesRegex(ValueError, "stale source root closure"):
            audit.check_coverage(audit.ROOT, self.coverage)

    def test_wrong_source_locator_text(self):
        item = next(i for i in self.coverage["inventory"] if i["kind"] == "label")
        item["source"]["start_line"] = item["source"]["end_line"] = 1
        with self.assertRaisesRegex(ValueError, "does not occur at its locator"):
            audit.check_coverage(audit.ROOT, self.coverage)

    def test_source_hash_change(self):
        self.coverage["sources"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "stale manuscript"):
            audit.check_coverage(audit.ROOT, self.coverage)

    def test_duplicate_use_site(self):
        self.coverage["edges"].append(copy.deepcopy(self.coverage["edges"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate source dependency use site"):
            audit.check_coverage(audit.ROOT, self.coverage)

    def test_missing_required_file_binding(self):
        original = audit.read_json
        manifest = original(audit.ROOT / audit.AUDIT / "manifest.json")
        del manifest["file_sha256"]["article.tex"]
        with patch.object(audit, "read_json", side_effect=lambda p: manifest if p.name == "manifest.json" else original(p)):
            with self.assertRaisesRegex(ValueError, "omits required input"):
                audit.check(audit.ROOT)

    def test_stale_report_binding(self):
        original = audit.read_json
        manifest = original(audit.ROOT / audit.AUDIT / "manifest.json")
        manifest["file_sha256"]["metadata/statement-audit/theorem1.json"] = "0" * 64
        with patch.object(audit, "read_json", side_effect=lambda p: manifest if p.name == "manifest.json" else original(p)):
            with self.assertRaisesRegex(ValueError, "audit input/report changed"):
                audit.check(audit.ROOT)


class PublicationAuditControls(unittest.TestCase):
    def test_current_sources_match_recorded_mathematical_regions(self):
        audit.check_publication(audit.ROOT)

    def test_rejects_changed_theorem_formula(self):
        reviewed = audit.local(audit.ROOT, "article.tex").read_text()
        changed = reviewed.replace("L_{d,r}(n,x)", "L_{d,r}(n,x)+1", 1)
        self.assertNotEqual(changed, reviewed)
        with self.assertRaisesRegex(ValueError, "Mathematical statement/proof regions changed"):
            audit.check_mathematical_regions(changed, reviewed, "article.tex")

    def test_rejects_changed_proof(self):
        reviewed = audit.local(audit.ROOT, "article.tex").read_text()
        changed = reviewed.replace("\\begin{proof}", "\\begin{proof}\nFalse inference.", 1)
        self.assertNotEqual(changed, reviewed)
        with self.assertRaisesRegex(ValueError, "Mathematical statement/proof regions changed"):
            audit.check_mathematical_regions(changed, reviewed, "article.tex")


if __name__ == "__main__":
    unittest.main()
