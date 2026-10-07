#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Compare compiled cleanup snapshots, including actual data definition values.

Seed generation:
  python3 scripts/compare_cleanup_fingerprints.py --seeds-from lean/Audit.lean \
    --seed-output .verify-work/cleanup-seeds.json

Run export_cleanup_fingerprints.lean from each matching compiled Lean project:
  lake env lean --run /path/to/scripts/export_cleanup_fingerprints.lean \
    /path/to/cleanup-seeds.json /path/to/snapshot.json

Comparison:
  python3 scripts/compare_cleanup_fingerprints.py before.json after.json \
    --report .verify-work/cleanup-comparison.json

Separate reviewed comparison (the strict report is preserved):
  python3 scripts/compare_cleanup_fingerprints.py before.json after.json \
    --strict-report metadata/elaboration/2026-10-06/cleanup-comparison.json \
    --reviewed-instance-pairs metadata/elaboration/2026-10-06/instance-pairs.json \
    --instance-witnesses metadata/elaboration/2026-10-06/instance-witnesses.json \
    --report .verify-work/cleanup-reviewed-comparison.json

This optional mode recognizes exactly two hardcoded, closed foundation-instance
terms and validates their source-bound recorded literal kernel Eq.refl witnesses.
It canonicalizes only those exact whole subterms on both sides; no arbitrary
instance, type, proof, data value, or expression head is ignored. Every other
expression and declaration field retains the strict structural comparison.

An explicitly reviewed compiler rename of a private proof may be supplied as
--allow-renamed-proof-aux OLD=NEW. Each pair must name an actually removed and
added non-public proof declaration with an identical compiled type after the
same exact constant-name substitutions. Descendants are never renamed by an
unrestricted prefix rule: any generated auxiliary needs its own reviewed pair.

This is structural comparison of exported expressions, not a proof checker or
mathematical review. Exact node interning is used for equality; diagnostic SHA-256
Merkle fingerprints do not determine the pass/fail result. Expr.mdata is omitted
by the exporter. No normalization, unfolding or proof-irrelevance quotient is
applied in strict mode, so harmless expression differences require inspection. Theorem
and proposition proof values are intentionally outside this comparison. Cached
artifacts must separately be verified to match their declared source provenance.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


SCHEMA = "qmdl-cleanup-fingerprints-v1"
CHILDREN = {
    "bvar": (), "sort": (), "const": (), "app": (1, 2),
    "lam": (2, 3), "forall": (2, 3), "let": (2, 3, 4),
    "nat_literal": (), "string_literal": (), "proj": (3,),
}
ARITY = {"bvar": 2, "sort": 2, "const": 3, "app": 3, "lam": 5,
         "forall": 5, "let": 6, "nat_literal": 2, "string_literal": 2, "proj": 4}


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f"duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(path.read_text(), object_pairs_hook=unique)


def generate_seeds(audit_path, output):
    text = audit_path.read_text()
    names = re.findall(r"^    `([^,\s]+),?$", text, re.M)
    require(names and len(names) == len(set(names)), "Audit.lean seed list absent or duplicated")
    lean = audit_path.resolve().parent
    sources = sorted((lean / "FreeEntropy").glob("*.lean"))
    require(sources, "proof sources absent beside Audit.lean")
    pins = {name: sha((lean / name).read_bytes())
            for name in ("lean-toolchain", "lakefile.toml", "lake-manifest.json")}
    result = {
        "schema_version": "qmdl-cleanup-seeds-v1",
        "proof_sources_sha256": sha(b"".join(
            path.name.encode() + b"\0" + path.read_bytes() for path in sources)),
        "lean_toolchain": (lean / "lean-toolchain").read_text().strip(),
        "pin_sha256": pins,
        "audit_seed_file_sha256": sha(audit_path.read_bytes()),
        "public_declarations": sorted(names),
        "provenance_policy": "Source identity only; matching compiled build must be established separately.",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Wrote {len(names)} public seeds to {output}")


def index_snapshot(path, intern, renames=None, name_trees=None, review=None, side=None):
    renames, name_trees = renames or {}, name_trees or {}
    snapshot = read_json(path)
    require(snapshot.get("schema_version") == SCHEMA, f"unsupported snapshot: {path}")
    seed = snapshot["seed_provenance"]
    require(seed.get("schema_version") == "qmdl-cleanup-seeds-v1", "unsupported seed provenance")
    names = seed["public_declarations"]
    require(names and len(names) == len(set(names)), "empty or duplicate public seed set")
    require(re.fullmatch(r"[0-9a-f]{64}", seed["proof_sources_sha256"]) is not None,
            "malformed source fingerprint")
    exact_ids, fingerprints, raw_ids, uses = [], [], [], []
    for index, node in enumerate(snapshot["nodes"]):
        require(isinstance(node, list) and node and node[0] in CHILDREN, "unknown expression node")
        require(len(node) == ARITY[node[0]], "incorrect expression node arity")
        exact = list(node)
        hashed = list(node)
        if node[0] == "const":
            replacement = name_trees.get(canonical(node[1]))
            if replacement is not None:
                exact[1] = hashed[1] = replacement
        for field in CHILDREN[node[0]]:
            child = node[field]
            require(type(child) is int and 0 <= child < index, "expression DAG is not topologically ordered")
            exact[field] = exact_ids[child]
            hashed[field] = fingerprints[child]
        replacement = None
        instance_uses = set()
        if review is not None:
            raw = list(node)
            for field in CHILDREN[node[0]]:
                raw[field] = raw_ids[node[field]]
                instance_uses.update(uses[node[field]])
            raw_key = canonical(raw)
            if raw_key not in review["raw_intern"]:
                review["raw_intern"][raw_key] = len(review["raw_intern"])
            raw_id = review["raw_intern"][raw_key]
            raw_ids.append(raw_id)
            replacement = review["aliases"].get(raw_id)
            if replacement is not None:
                instance_uses.add(replacement[2])
                review["matched_nodes"][side].setdefault(replacement[2], []).append({
                    "node": index, "registered_expr": replacement[3],
                })
            uses.append(frozenset(instance_uses))
        if replacement is not None:
            exact_ids.append(replacement[0])
            fingerprints.append(replacement[1])
        else:
            key = canonical(exact)
            if key not in intern:
                intern[key] = len(intern)
            exact_ids.append(intern[key])
            fingerprints.append(sha(canonical(hashed).encode()))

    def root(value):
        if value is None:
            return None, None
        require(type(value) is int and 0 <= value < len(exact_ids), "invalid expression root")
        return exact_ids[value], fingerprints[value]

    declarations = {}
    for declaration in snapshot["declarations"]:
        original_name = declaration["name"]
        name = renames.get(original_name, original_name)
        require(name not in declarations, f"duplicate compiled declaration: {name}")
        declaration = dict(declaration)
        declaration["name"] = name
        declaration["original_name"] = original_name
        if original_name in renames:
            declaration["name_tree"] = name_trees[canonical(declaration["name_tree"])]
        declaration["type_id"], declaration["type_sha256"] = root(declaration["type_root"])
        declaration["value_id"], declaration["value_sha256"] = root(declaration["value_root"])
        require(declaration["type_id"] is not None, f"missing compiled type: {name}")
        require(declaration["value_class"] in {"absent", "data", "proof_omitted"}, "unknown value class")
        require((declaration["value_id"] is not None) == (declaration["value_class"] == "data"),
                f"value class and expression disagree: {name}")
        declarations[name] = declaration
        if review is not None:
            for field in ("type_root", "value_root"):
                index = declaration[field]
                if index is not None and uses[index]:
                    review["declaration_uses"][side].append({
                        "declaration": name, "field": field,
                        "pair_ids": sorted(uses[index]),
                    })
    require({n for n, d in declarations.items() if d["public_audit_seed"]} == set(names),
            "exported public declarations differ from source seeds")
    return snapshot, declarations


def reviewed_renames(before_path, after_path, pairs):
    """Allow only explicit whole-constant renames of existing private proofs."""
    old_snapshot, new_snapshot = read_json(before_path), read_json(after_path)
    old = {d["name"]: d for d in old_snapshot["declarations"]}
    new = {d["name"]: d for d in new_snapshot["declarations"]}
    require(len(old) == len(old_snapshot["declarations"]) and
            len(new) == len(new_snapshot["declarations"]), "duplicate declaration in rename inputs")
    renames, name_trees, records = {}, {}, []
    for pair in pairs:
        require(pair.count("=") == 1, "proof rename must have the form OLD=NEW")
        source, target = pair.split("=")
        require(source and target and source != target, "empty or vacuous proof rename")
        require(source not in renames and target not in renames.values(), "duplicate proof rename")
        require(source in old and source not in new and target in new and target not in old,
                f"proof rename does not identify a removed/added pair: {pair}")
        for item in (old[source], new[target]):
            require(not item["public_audit_seed"] and item["value_class"] == "proof_omitted"
                    and item["kind"] in {"theorem", "definition", "opaque"},
                    f"only non-public proposition proofs may be renamed: {pair}")
        renames[source] = target
        name_trees[canonical(old[source]["name_tree"])] = new[target]["name_tree"]
        records.append({"before_name": source, "after_name": target})
    return renames, name_trees, records


def compare(before_path, after_path, allowed_removed, allowed_renames=(), review=None):
    renames, name_trees, rename_records = reviewed_renames(before_path, after_path, allowed_renames)
    intern = review["intern"] if review is not None else {}
    before, old = index_snapshot(before_path, intern, renames, name_trees, review, "before")
    after, new = index_snapshot(after_path, intern, review=review, side="after")
    old_seed, new_seed = before["seed_provenance"], after["seed_provenance"]
    same_pins = old_seed["pin_sha256"] == new_seed["pin_sha256"]
    removed, added = sorted(old.keys() - new.keys()), sorted(new.keys() - old.keys())
    require(set(allowed_removed) <= set(removed), "an allowed removal does not occur in the snapshots")
    for name in allowed_removed:
        require(not old[name]["public_audit_seed"] and old[name]["value_class"] == "proof_omitted",
                "only a non-public proof helper may receive an explicit removal exception")
    for item in rename_records:
        name = item["after_name"]
        require(old[name]["type_id"] == new[name]["type_id"] and
                old[name]["kind"] == new[name]["kind"] and
                old[name]["level_parameters"] == new[name]["level_parameters"],
                f"renamed proof has a different compiled signature: {item['before_name']}={name}")
        item["compiled_type_sha256_after_exact_name_remap"] = old[name]["type_sha256"]
    changes = []
    same_fields = ("name_tree", "kind", "module", "public_audit_seed", "level_parameters",
                   "type_id", "value_class", "value_id", "is_unsafe", "is_partial")
    for name in sorted(old.keys() & new.keys()):
        fields = [f for f in same_fields if old[name][f] != new[name][f]]
        if fields:
            changes.append({"name": name, "public_audit_seed": old[name]["public_audit_seed"],
                "changed_fields": fields,
                "before_type_sha256": old[name]["type_sha256"],
                "after_type_sha256": new[name]["type_sha256"],
                "before_value_sha256": old[name]["value_sha256"],
                "after_value_sha256": new[name]["value_sha256"]})
    public_types_changed = [x for x in changes if x["public_audit_seed"] and
                            set(x["changed_fields"]) - {"value_id"}]
    data_values_changed = [x for x in changes if "value_id" in x["changed_fields"]]
    unexpected_removed = sorted(set(removed) - set(allowed_removed))
    passed = same_pins and not changes and not added and not unexpected_removed
    return {
        "schema_version": "qmdl-cleanup-comparison-v1",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "review_required",
        "before_snapshot_sha256": sha(before_path.read_bytes()),
        "after_snapshot_sha256": sha(after_path.read_bytes()),
        "before_source_provenance": old_seed,
        "after_source_provenance": new_seed,
        "same_dependency_pins": same_pins,
        "counts": {
            "before_declarations": len(old), "after_declarations": len(new),
            "before_public_declarations": sum(d["public_audit_seed"] for d in old.values()),
            "after_public_declarations": sum(d["public_audit_seed"] for d in new.values()),
            "before_data_values": sum(d["value_class"] == "data" for d in old.values()),
            "after_data_values": sum(d["value_class"] == "data" for d in new.values()),
            "public_signature_changes": len(public_types_changed),
            "data_value_changes": len(data_values_changed), "changed_declarations": len(changes),
        },
        "allowed_removed_auxiliary_proofs": sorted(allowed_removed),
        "reviewed_renamed_auxiliary_proofs": rename_records,
        "unexpected_removed_declarations": unexpected_removed,
        "added_declarations": added, "changed_declarations": changes,
        "equality_policy": "Exact shared interning of serialized expression DAG nodes, independent of node numbering, after only the listed whole-constant private-proof renames; no generic prefix substitution. Renamed proof signatures must match. SHA-256 Merkle fingerprints are diagnostic only.",
        "scope": "Project declarations, every public audited compiled type, and every available non-proposition definition/opaque compiled value; proposition proof values omitted; Expr.mdata/cached fields omitted; no unfolding or normalization.",
        "limitations": "This is read-only comparison evidence, not a kernel check or semantic review. Source provenance and compiled artifact freshness must be established separately. Syntactic differences may be mathematically harmless and require review.",
    }


def instance_blueprints():
    """The two reviewed whole terms, not a general instance-erasure policy."""
    def name(value):
        result = ["anonymous"]
        for part in value.split("."):
            result = ["str", result, part]
        return result

    def const(value, polymorphic=False):
        return ["const", name(value), [["zero"]] if polymorphic else []]

    def app(function, *arguments):
        for argument in arguments:
            function = ["app", function, argument]
        return function

    integer, real = const("Int"), const("Real")
    old_order = const("instConditionallyCompleteLinearOrder")
    for projection in (
        "ConditionallyCompleteLinearOrder.toConditionallyCompleteLattice",
        "ConditionallyCompleteLattice.toConditionallyCompletePartialOrder",
        "ConditionallyCompletePartialOrder.toConditionallyCompletePartialOrderSup",
        "ConditionallyCompletePartialOrderSup.toPartialOrder",
    ):
        old_order = app(const(projection, True), integer, old_order)
    new_order = app(const("SemilatticeInf.toPartialOrder", True), integer,
                    app(const("Lattice.toSemilatticeInf", True), integer, const("instLatticeInt")))
    order_type = app(const("PartialOrder", True), integer)
    semiring_add_monoid = const("Real.semiring")
    for projection in (
        "Semiring.toNonAssocSemiring",
        "NonAssocSemiring.toAddCommMonoidWithOne",
        "AddCommMonoidWithOne.toAddMonoidWithOne",
    ):
        semiring_add_monoid = app(const(projection, True), real, semiring_add_monoid)
    old_add_monoid = const("Real.instRCLike")
    for projection in (
        "RCLike.toDenselyNormedField", "DenselyNormedField.toNormedField",
        "NormedField.toNormedCommRing", "NormedCommRing.toNormedRing",
        "NormedRing.toRing", "Ring.toAddGroupWithOne", "AddGroupWithOne.toAddMonoidWithOne",
    ):
        old_add_monoid = app(const(projection, True), real, old_add_monoid)
    char_zero_type = app(const("CharZero", True), real, semiring_add_monoid)
    return {
        "IntPartialOrder": {
            "before_expr": old_order, "after_expr": new_order,
            "type_expr": order_type,
            "inferred_before_type_expr": order_type,
            "inferred_after_type_expr": order_type,
            "equality_level": ["succ", ["zero"]],
        },
        "RealCharZero": {
            "before_expr": app(const("RCLike.charZero_rclike", True), real, const("Real.instRCLike")),
            "after_expr": app(const("IsStrictOrderedRing.toCharZero", True), real,
                              const("Real.semiring"), const("Real.partialOrder"),
                              const("Real.instIsStrictOrderedRing")),
            "type_expr": char_zero_type,
            "inferred_before_type_expr": app(const("CharZero", True), real, old_add_monoid),
            "inferred_after_type_expr": char_zero_type,
            "equality_level": ["zero"],
        },
    }


def intern_closed_term(tree, intern):
    """Intern exact recursive const/app trees; return identity and diagnostic hash."""
    require(isinstance(tree, list) and tree and tree[0] in {"const", "app"},
            "instance terms must be closed const/app trees")
    exact, hashed = list(tree), list(tree)
    if tree[0] == "app":
        require(len(tree) == 3, "invalid closed application")
        for field in (1, 2):
            exact[field], hashed[field] = intern_closed_term(tree[field], intern)
    else:
        require(len(tree) == 3, "invalid closed constant")
    key = canonical(exact)
    if key not in intern:
        intern[key] = len(intern)
    return intern[key], sha(canonical(hashed).encode())


def proper_subterms(tree):
    if tree[0] == "app":
        for child in tree[1:]:
            yield child
            yield from proper_subterms(child)


def closed_snapshot_term(snapshot, index):
    require(type(index) is int and 0 <= index < len(snapshot["nodes"]), "invalid instance snapshot root")
    node = snapshot["nodes"][index]
    require(isinstance(node, list) and len(node) == 3 and node[0] in {"const", "app"},
            "snapshot instance is not a closed const/app term")
    if node[0] == "const":
        return node
    require(all(type(child) is int and 0 <= child < index for child in node[1:]),
            "instance snapshot DAG is not topologically ordered")
    return ["app", closed_snapshot_term(snapshot, node[1]), closed_snapshot_term(snapshot, node[2])]


def public_evidence(root, name):
    """Read bound regular evidence beneath a repository, including local scratch.

    Accepting a local path does not publish it. Release paths are independently
    restricted by prepare_release.py's explicit publication allowlist.
    """
    require(isinstance(name, str) and name, "missing public evidence path")
    relative = Path(name)
    require(not relative.is_absolute() and ".." not in relative.parts, "unsafe public evidence path")
    path = root.resolve()
    for part in relative.parts:
        path /= part
        require(not path.is_symlink(), "symlink in public evidence path")
    require(path.is_file(), f"missing public evidence: {name}")
    return path.read_bytes()


def reviewed_context(before_path, after_path, strict_path, pairs_path, witnesses_path, root):
    """Accept only these exact pairs and source-bound literal kernel certificates.

    This validates recorded evidence; it does not itself execute Lean. Re-running
    the separately published helper establishes fresh kernel witness evidence.
    """
    strict = read_json(strict_path)
    pairs = read_json(pairs_path)
    witnesses = read_json(witnesses_path)
    before, after = read_json(before_path), read_json(after_path)
    require(pairs.get("schema_version") == "qmdl-cleanup-instance-pairs-v1", "unknown instance pair schema")
    require(witnesses.get("schema_version") == "qmdl-cleanup-instance-witnesses-v1", "unknown instance witness schema")
    require(witnesses.get("instance_pair_input") == pairs, "witness input differs from paired terms")
    expected_bindings = {
        "before_snapshot_sha256": sha(before_path.read_bytes()),
        "after_snapshot_sha256": sha(after_path.read_bytes()),
        "before_source_provenance": before["seed_provenance"],
        "after_source_provenance": after["seed_provenance"],
        "strict_comparison_sha256": sha(strict_path.read_bytes()),
    }
    for key, value in expected_bindings.items():
        require(pairs.get(key) == value, f"stale instance-pair binding: {key}")
        if key != "strict_comparison_sha256":
            require(strict.get(key) == value, f"stale strict comparison binding: {key}")
    require(before["seed_provenance"]["pin_sha256"] == after["seed_provenance"]["pin_sha256"],
            "instance witnesses require identical dependency pins")
    require(witnesses.get("kernel_check_explicitly_enabled") is True
            and witnesses.get("project_modules_imported") is False,
            "kernel witnesses must check in a foundation-only environment")
    allowed_axioms = {"propext", "Classical.choice", "Quot.sound"}
    require(witnesses.get("status") == "passed"
            and witnesses.get("allowed_axioms") == ["propext", "Classical.choice", "Quot.sound"],
            "kernel witness status or axiom policy differs")
    require(witnesses.get("foundation_imports") == [
        "Mathlib.Data.Int.ConditionallyCompleteOrder", "Mathlib.Analysis.RCLike.Basic"],
        "unexpected foundation witness imports")

    execution = witnesses["execution_evidence"]
    require(type(execution.get("exit_status")) is int and execution["exit_status"] == 0,
            "kernel witness execution did not succeed")
    require(isinstance(execution.get("helper_path"), str)
            and Path(execution["helper_path"]).name == "check_cleanup_instance_pairs.lean",
            "unexpected kernel witness helper")
    require(execution.get("input_sha256") == sha(pairs_path.read_bytes()), "witness input bytes differ")
    require(public_evidence(root, execution["input_path"]) == pairs_path.read_bytes(), "witness input path differs")
    for kind in ("helper", "log"):
        require(sha(public_evidence(root, execution[kind + "_path"])) == execution[kind + "_sha256"],
                f"kernel witness {kind} bytes changed")
    require(public_evidence(root, execution["helper_path"]) ==
            Path(__file__).with_name("check_cleanup_instance_pairs.lean").read_bytes(),
            "executed witness helper differs from the published/copied helper")
    seed = before["seed_provenance"]
    require(execution.get("lean_toolchain") == seed["lean_toolchain"] == after["seed_provenance"]["lean_toolchain"],
            "kernel witness toolchain differs")
    require(execution.get("pin_sha256") == seed["pin_sha256"], "kernel witness pin bindings differ")
    require(set(seed["pin_sha256"]) == {"lean-toolchain", "lakefile.toml", "lake-manifest.json"},
            "incomplete dependency pin bindings")
    for filename, expected_hash in seed["pin_sha256"].items():
        require(filename in {"lean-toolchain", "lakefile.toml", "lake-manifest.json"}, "unexpected pinned input")
        require(sha(public_evidence(root, "lean/" + filename)) == expected_hash,
                f"current witness environment pin differs: {filename}")

    expected = instance_blueprints()
    pair_rows = pairs["pairs"]
    certificate_rows = witnesses["pairs"]
    require(len(pair_rows) == len(certificate_rows) == 2, "exactly two registered instance pairs required")
    require({p["id"] for p in pair_rows} == set(expected)
            and {p["id"] for p in certificate_rows} == set(expected), "unknown or duplicate instance pair ID")
    certificates = {p["id"]: p for p in certificate_rows}
    review = {"intern": {}, "raw_intern": {}, "aliases": {},
              "matched_nodes": {"before": {}, "after": {}},
              "declaration_uses": {"before": [], "after": []}}
    roots = []
    for row in pair_rows:
        identifier = row["id"]
        blueprint, certificate = expected[identifier], certificates[identifier]
        for field in ("before_expr", "after_expr", "type_expr"):
            require(row[field] == blueprint[field], f"unregistered whole instance expression: {identifier}/{field}")
            require(row[field + "_sha256"] == sha(canonical(row[field]).encode()), "instance AST hash mismatch")
            require(certificate.get(field) == row[field], "kernel certificate terms differ")
        require(closed_snapshot_term(before, row["before_snapshot_root"]) == row["before_expr"]
                and closed_snapshot_term(after, row["after_snapshot_root"]) == row["after_expr"],
                "instance AST differs from its exact snapshot subterm")
        for field in ("inferred_before_type_expr", "inferred_after_type_expr"):
            require(certificate.get(field) == blueprint[field],
                    f"unregistered inferred instance type: {identifier}/{field}")
        require(certificate.get("kernel_eq_refl_checked") is True, "unchecked instance equality")
        theorem_name = certificate.get("theorem_name")
        require(theorem_name == "QMDLCleanupFoundationWitness." + identifier,
                "invalid foundation witness theorem name")
        axioms = certificate.get("axioms")
        require(isinstance(axioms, list) and all(isinstance(item, str) for item in axioms)
                and len(axioms) == len(set(axioms)) and set(axioms) <= allowed_axioms
                and certificate.get("axiom_policy_passed") is True,
                "kernel witness has unreviewed axioms")
        eq_name = ["str", ["anonymous"], "Eq"]
        refl_name = ["str", eq_name, "refl"]
        equality = ["app", ["app", ["app", ["const", eq_name, [blueprint["equality_level"]]],
                    row["type_expr"]], row["before_expr"]], row["after_expr"]]
        proof = ["app", ["app", ["const", refl_name, [blueprint["equality_level"]]],
                 row["type_expr"]], row["before_expr"]]
        require(certificate.get("equality_type_expr") == equality
                and certificate.get("eq_refl_proof_expr") == proof,
                "certificate is not the literal typed Eq.refl witness")
        destination, fingerprint = intern_closed_term(row["after_expr"], review["intern"])
        for field in ("before_expr", "after_expr"):
            raw_identity, _ = intern_closed_term(row[field], review["raw_intern"])
            require(raw_identity not in review["aliases"], "duplicate or ambiguous instance substitution")
            review["aliases"][raw_identity] = (destination, fingerprint, identifier, field)
            roots.append(row[field])
    for tree in roots:
        require(not any(child == other for child in proper_subterms(tree) for other in roots),
                "overlapping instance substitution terms")
    log = public_evidence(root, execution["log_path"]).decode("utf-8")
    require(all(f"Kernel-checked exact foundation pair {identifier}; axioms:" in log
                for identifier in expected)
            and "Kernel-checked 2 exact foundation instance pairs." in log,
            "kernel witness log lacks the two successful pair verdicts")
    return review, strict, pairs, witnesses


def compare_reviewed(before_path, after_path, allowed_removed, allowed_renames,
                     strict_path, pairs_path, witnesses_path, root):
    review, strict, pairs, witnesses = reviewed_context(
        before_path, after_path, strict_path, pairs_path, witnesses_path, root)
    raw_result = compare(before_path, after_path, allowed_removed, allowed_renames)
    # The preserved strict report may also carry separately recorded execution
    # evidence. Its structural verdict must still match a fresh raw comparison.
    for key, value in raw_result.items():
        if key != "checked_at_utc":
            require(strict.get(key) == value, f"strict structural verdict differs: {key}")
    require(strict["status"] == "review_required", "reviewed mode requires preserved raw differences")
    strict_comparer = strict.get("execution_evidence", {}).get("comparer")
    if strict_comparer is not None:
        archive_path = strict_comparer.get("archived_source_path")
        require(archive_path == "metadata/elaboration/2026-10-06/historical/strict-compare-cleanup-fingerprints.py",
                "unexpected archived strict comparer source")
        require(sha(public_evidence(root, archive_path)) == strict_comparer.get("sha256"),
                "archived strict comparer source bytes differ")
    result = compare(before_path, after_path, allowed_removed, allowed_renames, review)
    for identifier in instance_blueprints():
        require(review["matched_nodes"]["before"].get(identifier)
                and review["matched_nodes"]["after"].get(identifier), "unused instance substitution")
        require(any(item["registered_expr"] == "before_expr"
                    for item in review["matched_nodes"]["before"][identifier])
                and any(item["registered_expr"] == "after_expr"
                    for item in review["matched_nodes"]["after"][identifier]),
                "registered pair variants do not occur on their respective snapshot sides")
        used_to_review = False
        for change in strict["changed_declarations"]:
            fields = {"type_root" for field in change["changed_fields"] if field == "type_id"}
            fields.update("value_root" for field in change["changed_fields"] if field == "value_id")
            for side in ("before", "after"):
                used_to_review |= any(item["declaration"] == change["name"] and item["field"] in fields
                                      and identifier in item["pair_ids"]
                                      for item in review["declaration_uses"][side])
        require(used_to_review, "instance rule does not explain any preserved raw change")
    result.update(
        schema_version="qmdl-cleanup-reviewed-comparison-v1",
        strict_comparison_sha256=sha(strict_path.read_bytes()),
        strict_status=strict["status"], strict_counts=strict["counts"],
        instance_pairs_sha256=sha(pairs_path.read_bytes()),
        instance_witnesses_sha256=sha(witnesses_path.read_bytes()),
        reviewed_pair_ids=sorted(instance_blueprints()),
        matched_instance_nodes=review["matched_nodes"],
        instance_node_counts={side: {
            identifier: {
                "before_expr_matches": sum(x["registered_expr"] == "before_expr" for x in nodes),
                "after_expr_matches": sum(x["registered_expr"] == "after_expr" for x in nodes),
                "actual_substitutions": sum(x["registered_expr"] == "before_expr" for x in nodes),
            } for identifier, nodes in per_pair.items()
        } for side, per_pair in review["matched_nodes"].items()},
        occurrence_policy="Counts are unique serialized DAG nodes. Declaration/field use records include shared occurrences; expanded tree occurrence counts are not claimed.",
        instance_declaration_uses=review["declaration_uses"],
        kernel_witness_execution_evidence=witnesses["execution_evidence"],
        equality_policy="Exact whole const/app instance trees on both sides are canonicalized only for the two registered, source-bound kernel Eq.refl pairs. All remaining types, data values and declaration metadata use exact shared interning, with the separately listed private-proof renames/removal. No head/prefix substitution, proof/typeclass erasure, unfolding or generic normalization.",
        scope="Project declarations, every public audited compiled type and every available non-proposition definition/opaque compiled value, modulo only the registered whole foundation-instance pairs and separately listed private-proof renames/removal. Proposition proof values and Expr.mdata/cached fields remain omitted by the exporter. No generic normalization or unfolding.",
        limitations="This validates recorded structural and kernel-witness evidence; it does not execute Lean. The preserved strict report retains the raw syntactic changes. Fresh compiled source provenance, witness execution and full kernel audits are established separately.",
    )
    if strict_comparer is not None:
        result["archived_strict_comparer_source"] = {
            "path": strict_comparer["archived_source_path"], "sha256": strict_comparer["sha256"],
        }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("before", nargs="?", type=Path)
    parser.add_argument("after", nargs="?", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--allow-removed-aux", action="append", default=[], metavar="NAME")
    parser.add_argument("--allow-renamed-proof-aux", action="append", default=[], metavar="OLD=NEW")
    parser.add_argument("--reviewed-instance-pairs", type=Path,
                        help="separate bounded mode: the two registered whole foundation terms")
    parser.add_argument("--instance-witnesses", type=Path,
                        help="recorded source-bound kernel Eq.refl certificates")
    parser.add_argument("--strict-report", type=Path,
                        help="preserved raw comparison; never overwritten by reviewed mode")
    parser.add_argument("--evidence-root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="repository containing explicitly named public witness evidence")
    parser.add_argument("--seeds-from", type=Path, metavar="AUDIT_LEAN")
    parser.add_argument("--seed-output", type=Path)
    args = parser.parse_args()
    try:
        if args.seeds_from:
            require(args.seed_output and not args.before and not args.after and not args.report,
                    "seed mode requires --seed-output and no comparison arguments")
            require(not args.reviewed_instance_pairs and not args.instance_witnesses and not args.strict_report,
                    "instance review options cannot be used in seed mode")
            generate_seeds(args.seeds_from, args.seed_output)
            return
        require(args.before and args.after and args.report and not args.seed_output,
                "comparison requires before, after and --report")
        reviewed_options = (args.reviewed_instance_pairs, args.instance_witnesses, args.strict_report)
        require(not any(reviewed_options) or all(reviewed_options), "reviewed mode requires pairs, witnesses and strict report")
        if all(reviewed_options):
            require(args.report.resolve() not in {p.resolve() for p in
                    (args.before, args.after, *reviewed_options)}, "reviewed output must not overwrite input/strict evidence")
            report = compare_reviewed(args.before, args.after, args.allow_removed_aux,
                args.allow_renamed_proof_aux, args.strict_report, args.reviewed_instance_pairs,
                args.instance_witnesses, args.evidence_root)
        else:
            report = compare(args.before, args.after, args.allow_removed_aux, args.allow_renamed_proof_aux)
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n")
        print(f"CLEANUP STRUCTURAL COMPARISON {report['status'].upper()}: {report['counts']}")
        print(f"Comparison record: {args.report}")
        if report["status"] != "passed":
            parser.exit(1, "Changes require review; no automatic evidence rebinding was performed.\n")
    except (ValueError, KeyError, OSError) as exc:
        parser.exit(1, f"CLEANUP COMPARISON FAILED: {exc}\n")


if __name__ == "__main__":
    main()
