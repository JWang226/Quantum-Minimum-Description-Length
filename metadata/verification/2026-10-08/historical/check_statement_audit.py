#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Check retrospective audit bindings; optionally recompile its exact-type probes.

The default is a structural freshness check, not a mathematical reviewer. The
--lean mode also builds the two endpoint modules, compiles transient anonymous
applications, and checks their reported axioms. Neither mode reruns Comparator
or Nanoda. Reports keep their original agent-review status.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
AUDIT = Path("metadata/statement-audit")
ROOTS = {
    "FreeEntropy.theorem1_achievability",
    "FreeEntropy.theorem1_converse",
    "FreeEntropy.theorem1_converse_of_uniform",
    "FreeEntropy.ExteriorRepresentation.theorem2_cloning_accuracy_choi",
}
AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
REQUIRED_INPUTS = {
    "article.tex", "letter.tex", "free.bib", "lean/lean-toolchain",
    "lean/lakefile.toml", "lean/lake-manifest.json", "docs/assets/lean-catalog.json",
    "scripts/check_statement_audit.py", "scripts/export_statement_audit.lean",
    "metadata/statement-audit/theorem1.json", "metadata/statement-audit/theorem2.json",
    "metadata/statement-audit/source-coverage.json", "metadata/statement-audit/probes.json",
    "metadata/statement-audit/checks.json", "metadata/statement-audit/compiled-binders.json",
    "metadata/statement-audit/adversarial-review.json", "scripts/test_statement_audit.py",
    "metadata/statement-audit/theorem1-output.txt", "metadata/statement-audit/theorem2-output.txt",
    "docs/audit.md", "docs/audit/theorem1.md", "docs/audit/theorem2.md",
    "docs/audit/source-coverage.md", "docs/audit/independent-review.md",
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text())


def require(condition, message):
    if not condition:
        raise ValueError(message)


def proof_sha(root: Path) -> str:
    return sha(b"".join(p.name.encode() + b"\0" + p.read_bytes()
                        for p in sorted((root / "lean/FreeEntropy").glob("*.lean"))))


def local(root: Path, name: str) -> Path:
    path = (root / name).resolve()
    require(path.is_relative_to(root.resolve()), f"path escapes repository: {name}")
    require(path.is_file(), f"missing file: {name}")
    return path


def check(root: Path):
    manifest = read_json(root / AUDIT / "manifest.json")
    require(manifest["schema_version"] == 1, "unknown audit schema")
    require(manifest["review_kind"] == "retrospective_agent_review", "unexpected review claim")
    require(manifest["human_review"] == "not_established", "human review status requires a new review record")
    require(manifest["proof_sources_sha256"] == proof_sha(root), "proof sources changed; audit needs review")
    require(REQUIRED_INPUTS <= manifest["file_sha256"].keys(), "audit manifest omits required input/report bindings")
    for name, expected in manifest["file_sha256"].items():
        require(sha(local(root, name).read_bytes()) == expected, f"audit input/report changed: {name}")

    catalog = read_json(root / "docs/assets/lean-catalog.json")
    require(catalog["proof_sources_sha256"] == manifest["proof_sources_sha256"], "catalog source mismatch")
    declarations = {x["name"]: x for x in catalog["declarations"] + catalog["auxiliary_declarations"]}
    require({x["name"] for x in manifest["endpoints"]} == ROOTS, "missing or unexpected endpoint")
    for item in manifest["endpoints"]:
        current = declarations[item["name"]]
        require(current["kind"] == "theorem", f"endpoint is not a theorem: {item['name']}")
        require(sha(current["statement"].encode()) == item["compiled_statement_sha256"],
                f"compiled statement snapshot changed: {item['name']}")
        require(current["statement"] == item["compiled_statement"], f"statement text differs from snapshot: {item['name']}")
        require(current["file"] == item["file"] and current["line"] == item["line"],
                f"endpoint location changed: {item['name']}")

    probes = read_json(root / AUDIT / "probes.json")
    require(ROOTS <= {n for p in probes for n in p["axiom_roots"]}, "probe root coverage mismatch")
    for probe in probes:
        require(not re.search(r"\b(sorry|admit|axiom)\b", probe["lean_source"]),
                f"proof placeholder/declaration in probe: {probe['id']}")
        require("example" in probe["lean_source"], f"missing anonymous application: {probe['id']}")

    coverage = read_json(root / AUDIT / "source-coverage.json")
    check_coverage(root, coverage)
    check_review_tables(root, manifest)
    record = read_json(root / AUDIT / "checks.json")
    require(record["status"] == "passed" and record["proof_sources_sha256"] == manifest["proof_sources_sha256"],
            "recorded Lean probes failed or cover different sources")
    require(record["probe_bundle_sha256"] == sha((root / AUDIT / "probes.json").read_bytes()), "recorded probes changed")
    require(record["compiled_binders_sha256"] == sha((root / AUDIT / "compiled-binders.json").read_bytes()),
            "recorded compiled binders changed")
    require({p["id"] for p in probes} == {c["id"] for c in record["checks"]}, "recorded check list differs")
    for probe in probes:
        result = next(c for c in record["checks"] if c["id"] == probe["id"])
        require(result["status"] == "passed" and result["probe_sha256"] == sha(probe["lean_source"].encode()),
                "probe result does not match current source")
        require(set(result["axioms"]) == set(probe["axiom_roots"]), "recorded axiom roots differ")
        require(all(set(used) <= AXIOMS for used in result["axioms"].values()), "unpermitted recorded axiom")
        require(result["output_sha256"] == sha((root / AUDIT / (probe["id"] + "-output.txt")).read_bytes()),
                "recorded Lean output changed")
    return manifest, probes, coverage


def check_review_tables(root: Path, manifest):
    """Check report accounting, not the mathematical judgement of each bin."""
    bins = {"SOURCE", "STANDING", "TYPING", "RULED", "EXCESS"}
    endpoints = {x["name"]: x for x in manifest["endpoints"]}
    t1 = read_json(root / AUDIT / "theorem1.json")
    require({e["export"] for e in t1["endpoints"]} == ROOTS - {
        "FreeEntropy.ExteriorRepresentation.theorem2_cloning_accuracy_choi"}, "Theorem 1 report roots differ")
    for report in t1["endpoints"]:
        require([b["binder"] for b in report["outer_binders"]] ==
                [b["name"] for b in endpoints[report["export"]]["top_level_binders"]], "report omits outer binder")
        for table, count in (("outer_binders", "outer_counts"), ("expanded_input_binders", "expanded_counts")):
            rows = report[table]
            require(all(b["classification"] in bins and b["source_citation"] for b in rows), "invalid/unlocated binder classification")
            actual = {k: sum(b["classification"] == k for b in rows) for k in bins}
            require(actual == report[count], "Theorem 1 binder counts differ")
    t2 = read_json(root / AUDIT / "theorem2.json")
    rows = t2["binders"]
    require(all(b["bin"] in bins and b["source"] for b in rows), "invalid/unlocated Theorem 2 classification")
    require({k: sum(b["bin"] == k for b in rows) for k in bins} == t2["counts"], "Theorem 2 binder counts differ")
    expanded = list(dict.fromkeys(b["name"].split(".")[0] for b in rows))
    require(expanded == [b["name"] for b in endpoints[t2["target"]["export"]]["top_level_binders"]],
            "Theorem 2 expanded report omits a binder")


def check_coverage(root: Path, coverage):
    """Rescan recognizable TeX; manual mathematical coverage remains reviewed data."""
    require(coverage["schema_version"] == "qmdl-retrospective-source-coverage-v1", "unknown coverage schema")
    source_text = {}
    for source in coverage["sources"]:
        path = local(root, source["file"])
        require(sha(path.read_bytes()) == source["sha256"], f"stale manuscript: {source['file']}")
        source_text[source["file"]] = path.read_text()
        require(len(source_text[source["file"]].splitlines()) == source["line_count"], "source line count changed")

    def validate_locations(value):
        if isinstance(value, dict):
            if {"file", "start_line", "end_line"} <= value.keys():
                require(value["file"] in source_text, f"unknown locator source: {value['file']}")
                require(1 <= value["start_line"] <= value["end_line"] <= len(source_text[value["file"]].splitlines()),
                        f"invalid source range: {value}")
            for child in value.values():
                validate_locations(child)
        elif isinstance(value, list):
            for child in value:
                validate_locations(child)

    validate_locations(coverage)
    nodes = {n["id"]: n for n in coverage["nodes"]}
    require(len(nodes) == len(coverage["nodes"]), "duplicate source node")
    require(set(coverage["roots"]) == {"thm:qmdl", "thm:main"} <= nodes.keys(), "source roots missing")
    inventory = coverage["inventory"]
    require(len({i["id"] for i in inventory}) == len(inventory), "duplicate inventory ID")
    patterns = {
        "label": r"\\label\{([^}]+)\}",
        "citation": r"\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}",
        "cross_reference": r"\\(?:eqref|ref|autoref|cref|Cref|pageref)\*?\{([^}]+)\}",
    }
    expected, actual = Counter(), Counter()
    text = source_text["article.tex"]
    for kind, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            expected[(kind, match[0], text.count("\n", 0, match.start()) + 1,
                      text.count("\n", 0, match.end() - 1) + 1)] += 1
    environment = r"\\(begin|end)\{(thm|lem|prop|defn|rem|cor|corollary|theorem|lemma|proposition|definition|remark|proof)\}"
    stacks = {}
    for match in re.finditer(environment, text):
        action, env = match.groups()
        line = text.count("\n", 0, match.start()) + 1
        if action == "begin":
            stacks.setdefault(env, []).append((match[0], line))
        else:
            require(bool(stacks.get(env)), f"unpaired source environment: {env}")
            token, start = stacks[env].pop()
            kind = "proof_environment" if env == "proof" else "theorem_like_environment"
            expected[(kind, token, start, line)] += 1
    require(not any(stacks.values()), "unclosed source environment")
    mechanical = {*patterns, "proof_environment", "theorem_like_environment"}
    for item in inventory:
        loc = item["source"]
        excerpt = "\n".join(source_text[loc["file"]].splitlines()[loc["start_line"] - 1:loc["end_line"]])
        require(item["raw"] in excerpt, f"inventory text does not occur at its locator: {item['id']}")
        if item["kind"] in mechanical:
            require(loc["file"] == "article.tex", "unexpected corpus for mechanical inventory")
            actual[(item["kind"], item["raw"], loc["start_line"], loc["end_line"])] += 1
        require(item["disposition"] in {"MAPPED", "EXCLUDED"}, f"unresolved inventory item: {item['id']}")
        if item["disposition"] == "EXCLUDED":
            require(bool(item["reason"].strip()), f"unexplained exclusion: {item['id']}")
        else:
            require(bool(item["node_ids"]) and set(item["node_ids"]) <= nodes.keys(),
                    f"unmapped inventory item: {item['id']}")
    require(actual == expected, f"TeX inventory differs from raw source: {sum((expected - actual).values())} missing, "
            f"{sum((actual - expected).values())} unexpected occurrences")
    graph = {n: [] for n in nodes}
    seen_edges = set()
    for edge in coverage["edges"]:
        source, target = edge["from_node"], edge["to_node"]
        require(source in nodes and target in nodes, "dangling source dependency")
        loc = edge["consuming_source"]
        key = (source, target, loc["file"], loc["start_line"], loc["end_line"])
        require(key not in seen_edges, "duplicate source dependency use site")
        seen_edges.add(key)
        require(bool(edge["reason"].strip()), "dependency missing rationale")
        require(edge["consuming_source"]["file"] == "article.tex", "dependency missing consumer source")
        graph[source].append(target)
    visiting, done = set(), set()

    def visit(n):
        require(n not in visiting, f"source dependency cycle at {n}")
        if n in done:
            return
        visiting.add(n)
        for dep in graph[n]:
            visit(dep)
        visiting.remove(n)
        done.add(n)

    for n in coverage["roots"]:
        visit(n)
    require(done == nodes.keys(), f"nodes outside selected root closure: {set(nodes) - done}")
    summary = coverage["summary"]
    require(summary["nodes"] == len(nodes) and summary["edges"] == len(seen_edges)
            and summary["inventory_items"] == len(inventory), "stale inventory counts")
    require(summary["inventory_by_kind"] == dict(Counter(i["kind"] for i in inventory)), "stale inventory kind counts")
    require(summary["mapped_items"] == sum(i["disposition"] == "MAPPED" for i in inventory), "stale mapped count")
    require(summary["excluded_items"] == sum(i["disposition"] == "EXCLUDED" for i in inventory), "stale excluded count")
    closures = {}
    for source in coverage["roots"]:
        reachable, todo = set(), [source]
        while todo:
            node = todo.pop()
            if node not in reachable:
                reachable.add(node)
                todo.extend(graph[node])
        closures[source] = len(reachable)
    require(summary["root_closure_sizes"] == closures, "stale source root closure counts")


def run_lean(root: Path, project: Path, manifest, probes):
    # An alternate existing build is allowed only when every proof source and pin
    # matches. Its caches do not turn this into a fresh-checkout verification.
    for source in (root / "lean/FreeEntropy").glob("*.lean"):
        other = project / "FreeEntropy" / source.name
        require(other.is_file() and source.read_bytes() == other.read_bytes(),
                f"alternate build source mismatch: {source.name}")
    for name in ("lean-toolchain", "lakefile.toml", "lake-manifest.json"):
        require((root / "lean" / name).read_bytes() == (project / name).read_bytes(),
                f"alternate build pin mismatch: {name}")
    lake = shutil.which("lake") or str(Path.home() / ".elan/bin/lake")
    require(Path(lake).is_file(), "lake missing; install the documented Lean toolchain")
    output = root / ".verify-work/statement-audit"
    output.mkdir(parents=True, exist_ok=True)
    run_dir = Path(tempfile.mkdtemp(prefix="run-", dir=output))
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "proof_sources_sha256": manifest["proof_sources_sha256"],
        "probe_bundle_sha256": sha((root / AUDIT / "probes.json").read_bytes()),
        "checker_sha256": sha((root / "scripts/check_statement_audit.py").read_bytes()),
        "exporter_sha256": sha((root / "scripts/export_statement_audit.lean").read_bytes()),
        "mode": "incremental_exact_type_probes", "sandboxed": False,
        "fresh_checkout": False, "status": "running", "checks": [],
    }

    def run(command, log_name):
        result = subprocess.run(command, cwd=project, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (run_dir / log_name).write_text(result.stdout)
        require(result.returncode == 0, f"Lean check failed; see {run_dir / log_name}")
        require("error:" not in result.stdout, f"Lean reported error; see {run_dir / log_name}")
        return result.stdout

    try:
        run([lake, "build", "FreeEntropy.Theorem1Complete", "FreeEntropy.Theorem2Choi"], "build.txt")
        binder_path = run_dir / "compiled-binders.json"
        run([lake, "env", "lean", "--run", str(root / "scripts/export_statement_audit.lean"),
             str(binder_path)], "binder-export.txt")
        binders = read_json(binder_path)
        expected = {e["name"]: e["top_level_binders"] for e in manifest["endpoints"]}
        require({b["name"] for b in binders} == ROOTS, "compiled binder roots differ")
        for item in binders:
            actual = [{"name": b["name"], "kind": b["kind"]} for b in item["binders"]]
            require(actual == expected[item["name"]], f"compiled binder list differs: {item['name']}")
        record["compiled_binders_sha256"] = sha(binder_path.read_bytes())
        for probe in probes:
            # Only the review record is durable; the anonymous Lean file is temporary.
            with tempfile.TemporaryDirectory(prefix="qmdl-statement-probe-") as tmp:
                path = Path(tmp) / "Probe.lean"
                path.write_text(probe["lean_source"])
                text = run([lake, "env", "lean", str(path)], probe["id"] + ".txt")
            axioms = {}
            for name in probe["axiom_roots"]:
                match = re.search(re.escape("'" + name + "' depends on axioms:") + r"\s*\[([^\]]*)\]", text)
                require(match is not None, f"missing axiom report for {name}")
                used = {a.strip() for a in match[1].split(",") if a.strip()}
                require(used <= AXIOMS, f"unpermitted axioms for {name}: {used - AXIOMS}")
                axioms[name] = sorted(used)
            record["checks"].append({"id": probe["id"], "status": "passed",
                "probe_sha256": sha(probe["lean_source"].encode()),
                "axioms": axioms, "output_sha256": sha(text.encode())})
        record["status"] = "passed"
    except Exception as exc:
        record["status"] = "failed"
        record["error"] = str(exc)
        raise
    finally:
        (run_dir / "result.json").write_text(json.dumps(record, indent=2) + "\n")
        print(f"Lean probe record: {run_dir / 'result.json'}")
    print("STATEMENT AUDIT LEAN PROBES PASSED (incremental build; source interpretation remains agent-reviewed)")


def on_pre_build(config, **kwargs):
    check(ROOT)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--lean", action="store_true", help="also build endpoint modules and compile transient probes")
    parser.add_argument("--lean-project", type=Path, help="matching existing Lean build directory (requires --lean)")
    args = parser.parse_args()
    if args.lean_project and not args.lean:
        parser.error("--lean-project requires --lean")
    try:
        root = args.root.resolve()
        manifest, probes, coverage = check(root)
        print(f"STATEMENT AUDIT RECORDS CURRENT: {len(manifest['endpoints'])} endpoints; "
              f"{len(coverage['inventory'])} source inventory items")
        print("Structural freshness only; this does not certify mathematical correspondence.")
        if args.lean:
            run_lean(root, (args.lean_project or root / "lean").resolve(), manifest, probes)
    except (KeyError, OSError, ValueError) as exc:
        parser.exit(1, f"STATEMENT AUDIT FAILED: {exc}\n")


if __name__ == "__main__":
    main()
