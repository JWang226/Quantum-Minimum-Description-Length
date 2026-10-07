#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Run the exact foundation kernel witnesses and bind their actual execution.

The inputs are freshly exported before/after snapshots and their strict report,
plus the published exact-pair template. The output directory is repository-relative
scratch beneath --evidence-root. --helper accepts the fixed helper copied outside
the two historical checkouts; its bytes must match the helper beside this runner.
The runner copies it into scratch, binds fresh snapshot/root/input hashes, executes
the kernel witnesses, then records actual helper/input/log/pin/exit-status evidence.
No historical snapshot, strict report, pair input or witness record is rewritten.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

from compare_cleanup_fingerprints import CHILDREN, canonical, compare, instance_blueprints, intern_closed_term, read_json


DELETED_PRIVATE_HELPER = "_private.FreeEntropy.ExteriorMultiplicity.0.FreeEntropy.ExteriorRepresentation.complex_weight_eq_iff"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def evidence_path(root: Path, value: Path) -> tuple[Path, str]:
    require(not value.is_absolute(), "Evidence paths must be relative to --evidence-root")
    require(".." not in value.parts, "Evidence paths must not contain parent traversal")
    cursor = root
    for part in value.parts:
        cursor /= part
        require(not cursor.is_symlink(), "Evidence paths must not traverse symlinks")
    path = cursor.resolve()
    try:
        relative = path.relative_to(root)
    except ValueError as exc:
        raise ValueError("Evidence path escapes --evidence-root") from exc
    return path, relative.as_posix()


def project_identity(project: Path) -> dict:
    files = sorted((project / "FreeEntropy").glob("*.lean"))
    require(files, "No matching production sources in --lean-project")
    return {
        "lean_toolchain": (project / "lean-toolchain").read_text().strip(),
        "pin_sha256": {name: sha(project / name) for name in
                       ("lean-toolchain", "lakefile.toml", "lake-manifest.json")},
        "proof_sources_sha256": hashlib.sha256(b"".join(
            path.name.encode() + b"\0" + path.read_bytes() for path in files)).hexdigest(),
        "audit_seed_file_sha256": sha(project / "Audit.lean"),
    }


def find_exact_roots(snapshot, tree) -> list[int]:
    """Find actual whole terms by exact shared interning, not raw node IDs/hashes."""
    intern, ids = {}, []
    for index, node in enumerate(snapshot["nodes"]):
        require(isinstance(node, list) and node and node[0] in CHILDREN, "Unknown snapshot expression node")
        exact = list(node)
        for field in CHILDREN[node[0]]:
            child = node[field]
            require(type(child) is int and 0 <= child < index, "Snapshot DAG is not topologically ordered")
            exact[field] = ids[child]
        key = canonical(exact)
        if key not in intern:
            intern[key] = len(intern)
        ids.append(intern[key])
    target, _ = intern_closed_term(tree, intern)
    return [index for index, identity in enumerate(ids) if identity == target]


def bind_fresh_pairs(template, before, after, before_hash, after_hash, strict_hash):
    require(template.get("schema_version") == "qmdl-cleanup-instance-pairs-v1", "Unsupported pair-input template")
    require(before.get("schema_version") == after.get("schema_version") == "qmdl-cleanup-fingerprints-v1",
            "Unsupported compiled snapshot schema")
    require(template["before_source_provenance"] == before["seed_provenance"]
            and template["after_source_provenance"] == after["seed_provenance"],
            "Fresh snapshots do not match the reviewed source/pin/audit identities")
    registered = instance_blueprints()
    require(len(template["pairs"]) == 2 and {p["id"] for p in template["pairs"]} == set(registered),
            "Exactly the two registered foundation pairs are required")
    result = dict(template)
    result.update(before_snapshot_sha256=before_hash, after_snapshot_sha256=after_hash,
                  strict_comparison_sha256=strict_hash)
    result["pairs"] = []
    for pair in template["pairs"]:
        row = dict(pair)
        for field in ("before_expr", "after_expr", "type_expr"):
            require(row[field] == registered[row["id"]][field], "Unregistered foundation term/type in template")
            require(row[field + "_sha256"] == hashlib.sha256(canonical(row[field]).encode()).hexdigest(),
                    "Template recursive expression digest differs")
        for side, snapshot in (("before", before), ("after", after)):
            roots = find_exact_roots(snapshot, row[side + "_expr"])
            require(roots, f"Reviewed {row['id']} {side} whole term is absent from the fresh snapshot")
            row[side + "_snapshot_root"] = roots[0]
        result["pairs"].append(row)
    return result


def run(args) -> None:
    root = args.evidence_root.resolve()
    output_directory, _ = evidence_path(root, args.output_directory)
    require(not output_directory.exists(), "Choose a new scratch output directory; existing evidence is preserved")
    fixed_helper = Path(__file__).with_name("check_cleanup_instance_pairs.lean")
    saved_helper = args.helper.resolve() if args.helper else fixed_helper
    require(saved_helper.name == "check_cleanup_instance_pairs.lean" and saved_helper.is_file(),
            "Exact saved Lean witness helper is missing")
    require(saved_helper.read_bytes() == fixed_helper.read_bytes(), "Saved helper differs from the fixed runner's helper")
    before, after = read_json(args.before), read_json(args.after)
    template = read_json(args.pairs)
    before_hash, after_hash = sha(args.before), sha(args.after)
    # A strict review-required result is expected for these fixed source versions.
    # Recompute it directly: no shell failure is masked or promoted to success.
    raw_strict = compare(args.before, args.after, [DELETED_PRIVATE_HELPER])
    require(raw_strict["status"] == "review_required", "The registered source pair has no raw deltas to review")
    if args.strict_report.exists():
        strict = read_json(args.strict_report)
        for field, value in raw_strict.items():
            if field != "checked_at_utc":
                require(strict.get(field) == value, f"Existing strict verdict differs from fresh comparison: {field}")
    else:
        absolute = args.strict_report.absolute()
        try:
            relative = absolute.relative_to(root)
        except ValueError as exc:
            raise ValueError("New strict report must remain beneath --evidence-root") from exc
        safe_strict, _ = evidence_path(root, relative)
        safe_strict.parent.mkdir(parents=True, exist_ok=True)
        safe_strict.write_text(json.dumps(raw_strict, indent=2) + "\n")
        strict = raw_strict
    strict_hash = sha(args.strict_report)
    require(strict["before_snapshot_sha256"] == before_hash
            and strict["after_snapshot_sha256"] == after_hash,
            "Strict report is bound to other snapshot bytes")
    require(strict["before_source_provenance"] == before["seed_provenance"]
            and strict["after_source_provenance"] == after["seed_provenance"],
            "Strict report source identity differs")
    data = bind_fresh_pairs(template, before, after, before_hash, after_hash, strict_hash)
    project = args.lean_project.resolve() if args.lean_project else root / "lean"
    identity = project_identity(project)
    expected = data["after_source_provenance"]
    for field, actual in identity.items():
        require(actual == expected[field], f"Pinned after-project identity mismatch: {field}")
    require(data["before_source_provenance"]["pin_sha256"] == identity["pin_sha256"],
            "Before/after dependency pins differ")
    output_directory.mkdir(parents=True)
    helper = output_directory / "check_cleanup_instance_pairs.lean"
    shutil.copyfile(saved_helper, helper)
    runner = output_directory / "run_cleanup_instance_witnesses.py"
    shutil.copyfile(Path(__file__), runner)
    inp, out, log = (output_directory / name for name in
                     ("instance-pairs.json", "instance-witnesses.json", "instance-witnesses.txt"))
    inp.write_text(json.dumps(data, indent=2) + "\n")
    input_relative, output_relative, log_relative = (path.relative_to(root).as_posix() for path in (inp, out, log))
    helper_hash, input_hash, runner_hash = sha(helper), sha(inp), sha(runner)
    command = [args.lake, "env", "lean", "--run", str(helper), str(inp), str(out)]
    with log.open("x") as stream:
        result = subprocess.run(command, cwd=project, stdout=stream, stderr=subprocess.STDOUT,
                                check=False)
    require(result.returncode == 0, f"Lean kernel-witness run failed with exit {result.returncode}; see {log_relative}")
    require(sha(helper) == helper_hash and sha(inp) == input_hash,
            "Helper or pair input changed during execution")
    require(sha(Path(__file__)) == runner_hash, "Fixed runner changed during execution")
    require(project_identity(project) == identity, "Pinned project changed during execution")
    witness = json.loads(out.read_text())
    require(witness.get("schema_version") == "qmdl-cleanup-instance-witnesses-v1"
            and witness.get("status") == "passed", "Runtime did not produce successful kernel certificates")
    require(witness["instance_pair_input"] == data, "Runtime certificate is bound to another input")
    require(witness.get("kernel_check_explicitly_enabled") is True
            and witness.get("project_modules_imported") is False,
            "Runtime certificate did not use the explicit foundation kernel boundary")
    log_text = log.read_text()
    for pair in witness["pairs"]:
        require(pair.get("kernel_eq_refl_checked") is True and pair.get("axiom_policy_passed") is True,
                "Missing actual kernel/axiom witness result")
        require(f"Kernel-checked exact foundation pair {pair['id']}; axioms:" in log_text,
                "Successful witness marker absent from execution log")
    witness["execution_evidence"] = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "helper_path": helper.relative_to(root).as_posix(), "helper_sha256": helper_hash,
        "input_path": input_relative, "input_sha256": input_hash,
        "log_path": log_relative, "log_sha256": sha(log),
        "lean_toolchain": identity["lean_toolchain"], "pin_sha256": identity["pin_sha256"],
        "exit_status": result.returncode,
        "runner_path": runner.relative_to(root).as_posix(), "runner_sha256": runner_hash,
        "runner_invocation_origin": "Fixed saved directory beside the comparer; recorded scratch copy is byte-identical to the executed runner source.",
        "command": "lake env lean --run <evidence-root>/" + helper.relative_to(root).as_posix() + " <evidence-root>/" +
                   input_relative + " <evidence-root>/" + output_relative,
        "working_directory": "source- and pin-matching --lean-project",
        "scope": "Fresh actual foundation kernel witnesses and transitive standard-axiom checks; snapshot equality and manuscript correspondence are checked separately.",
    }
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"Fresh pair input: {input_relative}")
    print(f"Fresh kernel witness evidence: {output_relative}")
    print(f"Execution log: {log_relative}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--before", required=True, type=Path)
    parser.add_argument("--after", required=True, type=Path)
    parser.add_argument("--strict-report", required=True, type=Path)
    parser.add_argument("--pairs", required=True, type=Path, help="Published exact-pair template")
    parser.add_argument("--output-directory", required=True, type=Path)
    parser.add_argument("--helper", type=Path)
    parser.add_argument("--evidence-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--lean-project", type=Path)
    parser.add_argument("--lake", default="lake")
    args = parser.parse_args()
    try:
        run(args)
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        parser.exit(1, f"CLEANUP WITNESS RUN FAILED: {exc}\n")


if __name__ == "__main__":
    main()
