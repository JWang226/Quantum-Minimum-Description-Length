#!/usr/bin/env python3
# Copyright (c) 2026 Free Entropy formalization contributors.
# See LICENSE and NOTICE in the repository root for license and attribution.
"""Render the checked source maps as the website's correspondence tables.

This checks source locators and synchronizes documentation; it does not run
Lean, certify a new statement, or establish agreement between prose and types.
The descriptions and scope qualifications come from the reviewed source maps.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path
import re
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs/correspondence.md"
BEGIN = "<!-- BEGIN GENERATED CORRESPONDENCE -->"
END = "<!-- END GENERATED CORRESPONDENCE -->"
REPOSITORY = "https://github.com/JWang226/Quantum-Minimum-Description-Length"

# These groups and guide links are editorial navigation, not proof dependencies.
GROUPS = (
    ("Main results", "article-main-results", (
        "theorem1-achievability", "theorem1-converse-average",
        "theorem1-converse-uniform", "theorem2-choi", "theorem2-cartan",
        "theorem2-petz",
    ), "These are the final Article endpoints and their equivalent channel forms. "
       "Their precise hypotheses are visible in the linked compiled Lean statements."),
    ("Definitions", "article-definitions", (
        "fixed-spectrum", "quantum-channel", "physical-source", "trace-distance",
        "reconstruction-errors", "qmdl",
    ), "Definitions fix the meaning of the endpoint statements; they are not "
       "additional theorem certificates."),
    ("State and channel identifications", "article-identifications", (
        "representation-state", "finite-bound-parameters", "explicit-cloning-constant",
        "original-channel-definitions", "prv-projectors", "cartan-choi-identification",
        "petz-identification", "zero-increment",
    ), "These entries identify the actual objects used by Theorem 2. The canonical "
       "instances and restrictions recorded below matter: a correspondence is not "
       "a certificate for every broader formulation in the manuscript."),
    ("Compression and converse", "article-compression-converse", (
        "weyl-dimension", "padded-memory-dimension", "physical-code",
        "actual-concentration", "finite-orbit-memory", "uniform-gap",
    ), "These constructions and estimates supply Theorem 1. The formal proof uses "
       "sufficient intermediate bounds; the notes distinguish them from sharper "
       "or more general manuscript statements."),
    ("Finite-estimate lemmas", "article-finite-estimates", (
        "multiplicity-monotonicity", "root-coefficient-count", "shallow-multiplicities",
        "local-casimir-deficit", "mean-depth", "eigenvalue-ratio", "dimension-ratio",
    ), "Reusable intermediate statements may expose representation or scalar "
       "premises. Their required instances are constructed and their premises "
       "discharged before the final canonical endpoints."),
)

ROUTES = {
    "representations": (
        "proof-structure", "1-build-the-representations-and-their-dimensions",
        "Representations and dimensions",
    ),
    "finite": (
        "proof-structure", "2-prove-the-finite-cloning-bound-directly-in-trace-distance",
        "Finite cloning bound",
    ),
    "channels": (
        "proof-structure", "3-recover-the-manuscripts-channel-definitions",
        "Choi and Petz identifications",
    ),
    "compression": (
        "proof-structure", "4-transfer-the-bound-to-physical-tensor-sources",
        "Physical compression",
    ),
    "converse": (
        "proof-structure", "5-prove-the-converse-for-arbitrary-physical-codes",
        "Arbitrary-code converse",
    ),
    "letter": (
        "proof-structure", "relation-to-the-current-letter", "Letter coverage",
    ),
}

# (repository docs path without .md, optional heading, displayed guide label).
GUIDES = {
    "theorem1-achievability": [("results/achievability", "", "Achievability"), ROUTES["compression"]],
    "theorem1-converse-average": [("results/converse", "", "Converse"), ROUTES["converse"]],
    "theorem1-converse-uniform": [("results/converse", "", "Converse"), ROUTES["converse"]],
    "theorem2-choi": [("results/cloning-fidelity", "", "Cloning accuracy"), ROUTES["channels"]],
    "theorem2-cartan": [("results/cloning-fidelity", "", "Cloning accuracy"), ROUTES["finite"]],
    "theorem2-petz": [("results/propositions/reverse-cloner", "", "Reverse cloner"), ROUTES["channels"]],
    "fixed-spectrum": [("notation", "", "Notation"), ROUTES["representations"]],
    "quantum-channel": [("definitions/compression-code", "", "Compression code"), ROUTES["representations"]],
    "physical-source": [("concepts/schur-weyl-duality", "", "Physical sector decomposition"), ROUTES["compression"]],
    "trace-distance": [("results/cloning-fidelity", "", "Cloning accuracy"), ROUTES["finite"]],
    "reconstruction-errors": [("definitions/compression-code", "", "Compression code"), ROUTES["converse"]],
    "qmdl": [("concepts/quantum-minimum-description-length", "", "QMDL"), ROUTES["compression"]],
    "representation-state": [("definitions/normalized-gl-irrep", "", "Normalized representation state"), ROUTES["representations"]],
    "finite-bound-parameters": [("definitions/distance-between-irreps", "", "Distance between representations"), ROUTES["finite"]],
    "explicit-cloning-constant": [("results/lemmas/tail-mass", "", "Uniform mean depth"), ROUTES["finite"]],
    "original-channel-definitions": [("definitions/generalized-cloning-map-def", "", "Generalized cloning formula"), ROUTES["channels"]],
    "prv-projectors": [("concepts/prv-component", "", "PRV component"), ROUTES["channels"]],
    "cartan-choi-identification": [("results/propositions/choi-matrix-lemma", "", "Choi matrix identification"), ROUTES["channels"]],
    "petz-identification": [("results/propositions/reverse-cloner", "", "Reverse cloner and Petz identity"), ROUTES["channels"]],
    "zero-increment": [("results/cloning-fidelity", "", "Cloning accuracy"), ROUTES["channels"]],
    "weyl-dimension": [("concepts/weyl-dimension-formula", "", "Weyl dimension formula"), ROUTES["representations"]],
    "padded-memory-dimension": [("results/lemmas/weyl-dimension-asymptotic", "", "Dimension asymptotics"), ROUTES["compression"]],
    "physical-code": [("definitions/compression-code", "", "Compression code"), ROUTES["compression"]],
    "actual-concentration": [("results/lemmas/sanov-theorem", "", "Physical concentration"), ROUTES["compression"]],
    "finite-orbit-memory": [("results/propositions/orbit-sector-compression", "", "Haar-orbit memory bound"), ROUTES["converse"]],
    "uniform-gap": [("results/converse", "", "Converse"), ROUTES["converse"]],
    "multiplicity-monotonicity": [("results/lemmas/kostka-monotonicity", "", "Multiplicity monotonicity"), ROUTES["finite"]],
    "root-coefficient-count": [("concepts/kostant-partition-function", "", "Root coefficient counting"), ROUTES["finite"]],
    "shallow-multiplicities": [("results/lemmas/monotonicity-lemma", "", "Shallow multiplicities"), ROUTES["finite"]],
    "local-casimir-deficit": [("results/lemmas/perturbation-lemma", "", "Highest-weight projector deficit"), ROUTES["finite"]],
    "mean-depth": [("results/lemmas/tail-mass", "", "Uniform mean depth"), ROUTES["finite"]],
    "eigenvalue-ratio": [("results/lemmas/probability-ratio", "", "Eigenvalue ratio"), ROUTES["finite"]],
    "dimension-ratio": [("results/lemmas/dimension-ratio", "", "Dimension ratio"), ROUTES["finite"]],
    "letter-full-rank-qmdl": [("concepts/quantum-minimum-description-length", "", "QMDL"), ROUTES["letter"]],
    "letter-rank-deficient-qmdl": [("open-questions/degenerate-spectrum", "", "Degenerate-spectrum scope"), ROUTES["letter"]],
    "letter-error": [("definitions/compression-code", "", "Compression code"), ROUTES["letter"]],
    "letter-weyl": [("concepts/weyl-dimension-formula", "", "Weyl dimension formula"), ROUTES["letter"]],
    "letter-physical-entropy": [("definitions/physical-free-entropy-def", "", "Physical free entropy"), ROUTES["letter"]],
    "letter-hs-geometry": [("concepts/physical-free-entropy", "", "Hilbert–Schmidt geometry"), ROUTES["letter"]],
    "letter-entropy-relation": [("concepts/physical-free-entropy", "", "Physical entropy relation"), ROUTES["letter"]],
    "letter-degenerate-geometry": [("open-questions/degenerate-spectrum", "", "Degenerate-spectrum scope"), ROUTES["letter"]],
    "letter-double-scaling": [("definitions/scaling-regime", "", "Scaling regime"), ROUTES["letter"]],
}


def fail(message):
    raise SystemExit(f"FAILED: {message}")


def read_json(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def repository_file(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        fail(f"missing or invalid repository file: {relative}")
    return path


def check_hash(item):
    digest = hashlib.sha256(repository_file(item["file"]).read_bytes()).hexdigest()
    if digest != item["sha256"]:
        fail(f"source snapshot changed: {item['file']}")


def label_line(file, label):
    lines = repository_file(file).read_text(encoding="utf-8").splitlines()
    locations = [i for i, line in enumerate(lines, 1) if rf"\label{{{label}}}" in line]
    if len(locations) != 1:
        fail(f"expected one TeX label {label!r} in {file}, found {len(locations)}")
    return locations[0]


def load_and_check():
    article = read_json("metadata/natural-language-map.json")
    letter = read_json("metadata/letter-source-map.json")
    check_hash(article["manuscript"])
    check_hash(letter["manuscript"])
    for source in letter["source_files"]:
        check_hash(source)

    catalog = read_json("docs/assets/lean-catalog.json")
    # The two mapped structures are supplemental nodes, not public audit seeds.
    names = {
        item["name"]: item
        for key in ("declarations", "auxiliary_declarations")
        for item in catalog[key]
    }
    ids = set()
    for mapping in (article, letter):
        if mapping["review"]["status"] != "agent-reviewed":
            fail("the source map review status changed; review the page's prose")
        if mapping["review"]["independent_human_review"] != "not established":
            fail("the human review status changed; review the page's prose")
        for entry in mapping["entries"]:
            entry_id = entry["id"]
            if entry_id in ids or not re.fullmatch(r"[a-z0-9-]+", entry_id):
                fail(f"invalid or duplicate map id: {entry_id}")
            ids.add(entry_id)
            manuscript = entry["manuscript"]
            for anchor in manuscript["anchors"]:
                if label_line(manuscript["file"], anchor["label"]) != anchor["line"]:
                    fail(f"stale TeX line for {entry_id}: {anchor['label']}")
            for declaration in entry["lean"]:
                name = declaration["declaration"]
                node = names.get(name)
                if node is None:
                    fail(f"mapped Lean declaration absent from compiled catalog: {name}")
                for key in ("file", "line", "module"):
                    if node[key] != declaration[key]:
                        fail(f"mapped {key} differs from compiled catalog for {name}")
                source_lines = repository_file(declaration["file"]).read_text(encoding="utf-8").splitlines()
                if not 1 <= declaration["line"] <= len(source_lines):
                    fail(f"mapped Lean line outside its file: {name}")
            if entry_id not in GUIDES:
                fail(f"no curated proof guide for map entry: {entry_id}")

    article_ids = {entry["id"] for entry in article["entries"]}
    grouped_ids = [entry_id for _, _, entries, _ in GROUPS for entry_id in entries]
    if len(grouped_ids) != len(set(grouped_ids)) or set(grouped_ids) != article_ids:
        fail("Article table groups must cover each map entry exactly once")
    if set(GUIDES) != ids:
        fail("proof guide inventory and source-map inventory differ")
    for entry in letter["entries"]:
        if set(entry["article_entries"]) - article_ids:
            fail(f"unknown Article reference in {entry['id']}")
    for links in GUIDES.values():
        for page, _, _ in links:
            repository_file(f"docs/{page}.md")
    for item in article["not_claimed"]:
        for label in item["labels"]:
            label_line(article["manuscript"]["file"], label)
    return article, letter


def escape(value):
    return html.escape(str(value), quote=True)


def link(href, label, code=False):
    label = escape(label)
    if code:
        label = f"<code>{label}</code>"
    return f'<a href="{escape(href)}">{label}</a>'


def source_link(file, label, line):
    url = f"{REPOSITORY}/blob/main/{quote(file, safe='/')}#L{line}"
    return link(url, label, code=True)


def status(entry, group):
    value = entry["status"]
    if group == "letter":
        labels = {
            "consequence-of-article": "Consequence of Article",
            "definition-correspondence": "Definition correspondence",
            "not-formalized": "Not formalized",
        }
        if value not in labels:
            fail(f"unknown Letter status: {value}")
        return value, labels[value]
    if value == "defined":
        return "definition", "Definition"
    if value == "supporting-bound-proved" or (value == "proved" and group in (
        "article-compression-converse", "article-finite-estimates",
    )):
        return "supporting-bound-proved", "Supporting bound proved"
    if value == "proved":
        if group == "article-main-results":
            return "proved-endpoint", "Proved endpoint"
        return "proved-correspondence", "Proved correspondence"
    fail(f"unknown Article status: {value}")


def row(entry, group, article_titles):
    entry_id = entry["id"]
    state, state_label = status(entry, group)
    manuscript = entry["manuscript"]
    paper = f'<strong>{escape(entry["title"])}</strong>'
    paper += '<div class="qmdl-map-source">' + "<br>".join(
        source_link(manuscript["file"], anchor["label"], anchor["line"])
        for anchor in manuscript["anchors"]
    ) + "</div>"
    scope = f'<span class="qmdl-map-status" data-status="{state}">{state_label}</span>'
    scope += f'<p>{escape(entry["summary"])}</p>'
    if entry.get("notes"):
        scope += f'<p class="qmdl-map-notes">{escape(entry["notes"])}</p>'
    guide = "<br>".join(
        link(f"../{page}/" + (f"#{anchor}" if anchor else ""), label)
        for page, anchor, label in GUIDES[entry_id]
    )
    lean = "<br>".join(
        link("../proof-explorer/#declaration=" + quote(item["declaration"], safe="."),
             item["declaration"], code=True)
        + ' <span class="qmdl-map-source">('
        + link(f"{REPOSITORY}/blob/main/{quote(item['file'], safe='/')}#L{item['line']}",
               f"source L{item['line']}") + ")</span>"
        for item in entry["lean"]
    )
    if not lean:
        if entry["status"] == "definition-correspondence":
            lean = "Definition correspondence; see Article definitions."
        else:
            lean = "<strong>No Lean certificate.</strong>"
    if group == "letter" and entry["article_entries"]:
        lean += '<p class="qmdl-map-notes">Related Article entries:<br>' + "<br>".join(
            link(f"#{article_id}", article_titles[article_id])
            for article_id in entry["article_entries"]
        ) + "</p>"
    return (f'<tr id="{entry_id}" data-map-id="{entry_id}">\n'
            f'<td>{paper}</td>\n<td>{scope}</td>\n<td>{guide}</td>\n<td>{lean}</td>\n</tr>')


def table(title, entries, group, article_titles):
    lines = [
        f'<div class="qmdl-correspondence-table" role="region" tabindex="0" aria-label="{escape(title)} correspondence table">',
        "<table>",
        f'<caption>{escape(title)}: manuscript-to-Lean correspondence</caption>',
        "<thead><tr>",
        '<th scope="col">Paper statement</th>',
        '<th scope="col">Scope and formal meaning</th>',
        '<th scope="col">Proof guide</th>',
        '<th scope="col">Lean statements</th>',
        "</tr></thead>",
        "<tbody>",
    ]
    lines.extend(row(entry, group, article_titles) for entry in entries)
    lines += ["</tbody>", "</table>", "</div>"]
    return "\n".join(lines)


def render(article, letter):
    article_entries = {entry["id"]: entry for entry in article["entries"]}
    titles = {entry_id: entry["title"] for entry_id, entry in article_entries.items()}
    letter_counts = {
        value: sum(entry["status"] == value for entry in letter["entries"])
        for value in ("consequence-of-article", "definition-correspondence", "not-formalized")
    }
    lines = [
        "<!-- Generated by scripts/generate_correspondence.py from the two source maps. -->",
        "",
    ]
    for title, group, entry_ids, scope in GROUPS:
        lines += [f"## {title}", "", scope, "", table(
            title, [article_entries[entry_id] for entry_id in entry_ids], group, titles,
        ), ""]
    lines += [
        "## Letter correspondence",
        "",
        f"The Letter has {letter_counts['consequence-of-article']} consequences of the checked Article results, "
        f"{letter_counts['definition-correspondence']} definition correspondence, and "
        f"{letter_counts['not-formalized']} entries without a Lean certificate. "
        "A related Article link supplies context, not a certificate for an "
        "unformalized geometric or entropy claim.",
        "",
        table("Letter", letter["entries"], "letter", titles),
        "",
        "## Additional Article scope boundaries",
        "",
        "The Article source map also records the following exclusions. Some "
        "labels occur in mapped rows above because a restricted instance is "
        "covered while the broader claim is not.",
        "",
    ]
    for excluded in article["not_claimed"]:
        file = article["manuscript"]["file"]
        anchors = ", ".join(
            source_link(file, label, label_line(file, label))
            for label in excluded["labels"]
        )
        lines.append(f"- {anchors}: {escape(excluded['reason'])}")
    return "\n".join(lines).rstrip() + "\n"


def update_page(*, check=False):
    article, letter = load_and_check()
    if not PAGE.is_file():
        fail(f"missing correspondence page: {PAGE}")
    original = PAGE.read_text(encoding="utf-8")
    if original.count(BEGIN) != 1 or original.count(END) != 1:
        fail("the correspondence page must have exactly one pair of generation markers")
    start = original.index(BEGIN) + len(BEGIN)
    end = original.index(END)
    if end < start:
        fail("the correspondence generation markers are out of order")
    generated = original[:start] + "\n\n" + render(article, letter) + "\n" + original[end:]
    if check:
        if generated != original:
            fail("correspondence tables are stale; run python3 scripts/generate_correspondence.py")
        print(f"Correspondence tables are current: {len(article['entries'])} Article entries "
              f"and {len(letter['entries'])} Letter entries; source locators checked.")
    else:
        if generated != original:
            PAGE.write_text(generated, encoding="utf-8")
        print(f"Generated correspondence tables: {len(article['entries'])} Article entries "
              f"and {len(letter['entries'])} Letter entries.")


def on_pre_build(config, **kwargs):
    """MkDocs hook: reject stale correspondence before rendering or deployment."""
    update_page(check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the website tables are stale")
    args = parser.parse_args()
    update_page(check=args.check)


if __name__ == "__main__":
    main()
