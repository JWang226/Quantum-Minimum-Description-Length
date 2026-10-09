#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Validate the additive physical-interface review's source/evidence bindings.

This is a bounded freshness check. It does not rerun Lean, Comparator, or Nanoda,
decide mathematical correspondence, or establish independent human review. The
fixed baseline anchors prevent this extension record from silently rewriting the
earlier source snapshot or its four compiled endpoint statements.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BRIDGE = Path("metadata/statement-audit/physical-interface-bridge.json")
BASELINE_REVISION = "955bffc9278533adc219dd86012e9a2bc07c992b"
BASELINE_PROOF_SHA256 = "e7068771d301aaac3156ecc7cd0a1a4b3868a894a1d0988ce897420786ba2c3f"
BASELINE_MANIFEST_PATH = "metadata/verification/2026-10-08/historical/statement-manifest.json"
BASELINE_MANIFEST_SHA256 = "946a2e1076c75e7faee7ae6f07a1a1bca47f3ae750fb9af75746e93189ef8106"
RETAINED_MODULE_COUNT = 270
ADDED_MODULES = {
    "lean/FreeEntropy/ForwardChoiUniqueness.lean",
    "lean/FreeEntropy/PhysicalStateUniqueness.lean",
    "lean/FreeEntropy/Theorem2Physical.lean",
}
ENDPOINT_STATEMENTS = {
    "FreeEntropy.theorem1_achievability":
        "bc798eb5054b03f6c5230a66803c13ae7972bf04cbdd5285357c375e7bdb947c",
    "FreeEntropy.theorem1_converse":
        "29e0af015e6e2e4662354eb96f80fb5eed384bf0d2f2550421b408331ad086f4",
    "FreeEntropy.theorem1_converse_of_uniform":
        "638322dfbe72637518e73fc3031b429e11930c144e10dc8074729f5e63efdfe2",
    "FreeEntropy.ExteriorRepresentation.theorem2_cloning_accuracy_choi":
        "933ef0789f3ab7d358acfb28268ff9031bcd1d8895c877abc54a8529314adfad",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text())


def digest(value, context):
    require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value),
            f"invalid SHA-256: {context}")
    return value


def local(root: Path, name: str) -> Path:
    require(isinstance(name, str) and name and "\\" not in name,
            f"invalid repository path: {name}")
    relative = Path(name)
    require(not relative.is_absolute() and ".." not in relative.parts
            and relative.as_posix() == name, f"noncanonical repository path: {name}")
    path = (root / relative).resolve()
    require(path.is_relative_to(root.resolve()), f"path escapes repository: {name}")
    require(path.is_file(), f"missing file: {name}")
    return path


def file_binding(root: Path, record, context):
    require(isinstance(record, dict) and {"path", "sha256"} <= record.keys(),
            f"missing file binding: {context}")
    expected = digest(record["sha256"], context)
    path = local(root, record["path"])
    require(sha(path.read_bytes()) == expected, f"stale file binding: {context}: {record['path']}")
    return path


def module_bindings(root: Path, bindings, context):
    require(isinstance(bindings, dict), f"invalid module bindings: {context}")
    for name, expected in bindings.items():
        require(isinstance(name, str) and re.fullmatch(r"lean/FreeEntropy/[^/]+\.lean", name),
                f"nonproduction module in {context}: {name}")
        require(sha(local(root, name).read_bytes()) == digest(expected, name),
                f"{context} module changed: {name}")


def proof_digest(root: Path, names) -> str:
    # This is the existing audit/catalog byte convention: sorted basename,
    # NUL separator, and the exact source bytes, with no JSON serialization.
    return sha(b"".join(Path(name).name.encode() + b"\0" + local(root, name).read_bytes()
                        for name in sorted(names)))


def endpoint_index(items, context):
    require(isinstance(items, list) and all(isinstance(item, dict) and "name" in item for item in items),
            f"invalid endpoint/declaration list: {context}")
    names = [item["name"] for item in items]
    require(all(isinstance(name, str) for name in names) and len(names) == len(set(names)),
            f"duplicate/invalid endpoint names: {context}")
    return {item["name"]: item for item in items}


def check(root: Path):
    root = root.resolve()
    bridge = read_json(local(root, BRIDGE.as_posix()))
    require(type(bridge.get("schema_version")) is int and bridge["schema_version"] == 1,
            "unknown physical-interface bridge schema")
    require(bridge.get("review_kind") == "additive_agent_review", "unexpected extension review claim")
    require(bridge.get("human_review") == "not_established", "extension does not establish human review")
    require(bridge.get("baseline_revision") == BASELINE_REVISION, "extension baseline revision changed")
    require(bridge.get("baseline_proof_sources_sha256") == BASELINE_PROOF_SHA256,
            "extension baseline proof digest changed")
    require(bridge.get("retained_endpoint_statements") == ENDPOINT_STATEMENTS,
            "retained endpoint statement hashes differ from baseline")

    retained = bridge.get("retained_modules")
    added = bridge.get("added_modules")
    require(isinstance(retained, dict) and len(retained) == RETAINED_MODULE_COUNT,
            "extension must retain exactly 270 baseline production modules")
    require(isinstance(added, dict) and set(added) == ADDED_MODULES,
            "extension added-module set differs from the three reviewed modules")
    require(not set(retained) & set(added), "module listed as both retained and added")
    module_bindings(root, retained, "retained")
    module_bindings(root, added, "added")
    current_names = {p.relative_to(root).as_posix()
                     for p in (root / "lean/FreeEntropy").glob("*.lean") if p.is_file()}
    require(current_names == set(retained) | set(added),
            "production source set differs: missing or unreviewed module")
    require(proof_digest(root, retained) == BASELINE_PROOF_SHA256,
            "retained production sources do not recover the baseline digest")
    current_digest = proof_digest(root, current_names)
    require(bridge.get("current_proof_sources_sha256") == current_digest,
            "extension current proof digest is stale")

    historical_binding = bridge.get("historical_manifest")
    require(isinstance(historical_binding, dict)
            and historical_binding.get("path") == BASELINE_MANIFEST_PATH
            and historical_binding.get("sha256") == BASELINE_MANIFEST_SHA256,
            "historical statement manifest binding differs from the baseline bytes")
    historical = read_json(file_binding(root, historical_binding, "historical manifest"))
    require(historical.get("proof_sources_sha256") == BASELINE_PROOF_SHA256,
            "historical manifest has different proof sources")
    require(historical.get("review_kind") == "retrospective_agent_review"
            and historical.get("human_review") == "not_established", "historical review status changed")

    current = read_json(local(root, "metadata/statement-audit/manifest.json"))
    catalog = read_json(local(root, "docs/assets/lean-catalog.json"))
    require(current.get("human_review") == "not_established", "current manifest human review is not established")
    require(current.get("proof_sources_sha256") == current_digest
            and catalog.get("proof_sources_sha256") == current_digest,
            "current statement manifest/catalog source digest differs from the extension")
    old_endpoints = endpoint_index(historical.get("endpoints"), "historical manifest")
    new_endpoints = endpoint_index(current.get("endpoints"), "current manifest")
    declarations = endpoint_index(catalog.get("declarations", []) + catalog.get("auxiliary_declarations", []),
                                  "current catalog")
    require(set(old_endpoints) == set(ENDPOINT_STATEMENTS), "historical endpoint set changed")
    for name, expected in ENDPOINT_STATEMENTS.items():
        require(name in new_endpoints and name in declarations, f"retained endpoint missing: {name}")
        for label, item in (("historical", old_endpoints[name]), ("current", new_endpoints[name])):
            statement = item.get("compiled_statement")
            require(isinstance(statement, str) and sha(statement.encode()) == expected
                    and item.get("compiled_statement_sha256") == expected,
                    f"{label} endpoint statement changed: {name}")
        node = declarations[name]
        require(node.get("kind") == "theorem" and isinstance(node.get("statement"), str)
                and sha(node["statement"].encode()) == expected,
                f"catalog endpoint statement changed: {name}")

    reader_changes = bridge.get("reader_changes", {})
    require(isinstance(reader_changes, dict), "invalid reader-change review")
    original_bindings = historical.get("file_sha256", {})
    for name, review in reader_changes.items():
        require(not re.fullmatch(r"lean/FreeEntropy/[^/]+\.lean", name),
                f"reader change hides a production source change: {name}")
        require(isinstance(review, dict) and isinstance(review.get("scope"), str) and review["scope"].strip(),
                f"reader change lacks review scope: {name}")
        require(name in original_bindings and review.get("before_sha256") == original_bindings[name],
                f"reader change lacks original manifest binding: {name}")
        require(sha(local(root, name).read_bytes()) == digest(review.get("after_sha256"), name),
                f"reader change is stale: {name}")

    evidence = bridge.get("evidence")
    require(isinstance(evidence, dict) and evidence, "extension evidence bindings are missing")
    for name, binding in evidence.items():
        require(isinstance(name, str) and name.strip(), "unnamed extension evidence")
        file_binding(root, binding, f"evidence {name}")
    return bridge


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (default: this checkout)")
    args = parser.parse_args()
    try:
        bridge = check(args.root)
    except (ValueError, KeyError, TypeError, OSError) as error:
        raise SystemExit(f"PHYSICAL EXTENSION FRESHNESS FAILED: {error}") from error
    print(f"PHYSICAL EXTENSION FRESHNESS PASSED: {RETAINED_MODULE_COUNT} retained modules, "
          f"{len(ADDED_MODULES)} added modules, {len(ENDPOINT_STATEMENTS)} unchanged endpoint statements, "
          f"{len(bridge['evidence'])} bound evidence files.")
    print("Structural bindings only; mathematical correspondence and independent human review are not established by this check.")


if __name__ == "__main__":
    main()
