#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Negative controls for source preservation and extension evidence freshness."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

import check_physical_extension as extension


class PhysicalExtensionControls(unittest.TestCase):
    def setUp(self):
        self.bridge = extension.read_json(extension.ROOT / extension.BRIDGE)
        self.temporary = tempfile.TemporaryDirectory(prefix="qmdl-physical-extension-control-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        paths = {
            extension.BRIDGE.as_posix(),
            "metadata/statement-audit/manifest.json",
            "docs/assets/lean-catalog.json",
            self.bridge["historical_manifest"]["path"],
            *self.bridge["retained_modules"],
            *self.bridge["added_modules"],
            *(binding["path"] for binding in self.bridge["evidence"].values()),
            *self.bridge.get("reader_changes", {}),
        }
        for name in paths:
            destination = self.root / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(extension.ROOT / name, destination)

    def test_current_bindings(self):
        extension.check(self.root)

    def test_retained_source_edit(self):
        name = next(iter(self.bridge["retained_modules"]))
        path = self.root / name
        path.write_bytes(path.read_bytes() + b"\n-- negative control\n")
        # Even rebinding the individual file cannot rewrite the fixed baseline.
        self.bridge["retained_modules"][name] = extension.sha(path.read_bytes())
        (self.root / extension.BRIDGE).write_text(json.dumps(self.bridge))
        with self.assertRaisesRegex(ValueError, "do not recover the baseline digest"):
            extension.check(self.root)

    def test_missing_added_module(self):
        (self.root / next(iter(self.bridge["added_modules"]))).unlink()
        with self.assertRaisesRegex(ValueError, "missing file"):
            extension.check(self.root)

    def test_stale_evidence(self):
        binding = next(iter(self.bridge["evidence"].values()))
        path = self.root / binding["path"]
        path.write_bytes(path.read_bytes() + b"\n")
        with self.assertRaisesRegex(ValueError, "stale file binding: evidence"):
            extension.check(self.root)


if __name__ == "__main__":
    unittest.main()
