---
title: Statement audit
description: Retrospective checks of the Article's hypotheses, definitions and conclusions against four Lean theorem endpoints.
---

<!-- Copyright (c) 2026 Free Entropy formalization contributors.
     See LICENSE and NOTICE for license and attribution. -->

# Statement audit

This retrospective **agent review** compares four final Lean statements with the
current Article: Theorem 1's achievability, Haar-average converse and worst-case
converse, and Theorem 2's original Choi-projector bounds. It records what was
reviewed, the interpretation choices, and the limits of the review.

- [[audit/theorem1|Theorem 1: hypotheses, definitions and constants]]
- [[audit/theorem2|Theorem 2: supported rows, states and Choi channels]]
- [[audit/source-coverage|Manuscript argument inventory and source dependencies]]
- [[audit/independent-review|Independent adversarial review and resolved findings]]

Use [[correspondence|Paper ↔ Lean]] to navigate from a manuscript statement to its
formal declaration, and [the Lean explorer](proof-explorer.md) for compiled proof
dependencies. The source inventory on this page records dependencies in the
manuscript argument; its edges do not certify a Lean proof.

## Findings

The endpoint reviews and the independent adversarial pass found **no substantive
mismatch on the manuscript's stated domain, and no excess endpoint hypotheses**.
The expanded input tables contain 9 entries for achievability, 23 for each
converse, and 20 for cloning accuracy. These counts include the fields inside
the spectrum and channel packages rather than treating a bundle as one premise.

The review makes several boundaries explicit:

- The diagonal reference state describes the full fixed-spectrum unitary orbit.
  An additional API taking an arbitrary reference density matrix was not audited.
- Some internal definitions have total extensions beyond the source domain.
  The reports identify the hypotheses and proved identities that justify their
  use. Theorem 2's fresh application explicitly composes its physical normalized
  state identities with the cloning bound.
- The manuscript inventory has **75 nodes, 137 dependency use sites and 407
  entries**, including every recognizable theorem/proof environment, label,
  citation and cross-reference, plus 62 manually delimited mathematical regions.
  Some nodes group several conclusions of a proposition, so their closure can
  include more inputs than a particular consumer needs.
- Three source notes flag standard representation-theory inputs whose local
  derivation or precise citation is absent. These concern the manuscript's
  explanation and provenance; they do not identify missing Lean proofs.

The independent reviewer prompted fixes to the inventory checker and to the
Petz dependency description. Their report records both the findings and the
resolved checks. Individual graph nodes retain proposed status: this bounded
review does not claim a separate independent audit of every node and edge.

## Recorded Lean checks

All **seven anonymous applications compiled successfully**, covering the four
endpoint types, positivity of physical memory dimension, the CPTP status of the
literal Choi contractions, and Theorem 2 expressed using normalized physical
tensor restrictions. The actual compiled outer binder lists agree with the
recorded lists. Axiom reports for the endpoints and selected bridges use only
`propext`, `Classical.choice` and `Quot.sound`.

The [check record](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/statement-audit/checks.json),
[probe source](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/statement-audit/probes.json),
[compiled binders](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/statement-audit/compiled-binders.json)
and [snapshot manifest](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/statement-audit/manifest.json)
provide the machine-readable evidence. This was an incremental local Lean run.
The previously recorded Comparator and Nanoda results remain separately
documented in [[formalization|Scope and evidence]].

## Review method

Separate agents first reconstructed each theorem from the raw Article, before
reading its Lean implementation. They then inspected the endpoint binders,
expanded the relevant bundled hypotheses, reviewed the definitions that give the
statements their mathematical meaning, and checked how the final proofs supply
the estimates used by their conditional helper lemmas. Another agent inventoried
the manuscript's results, formulas, references and substantive proof regions.
A fresh adversarial reviewer then challenged the endpoint reports, source
inventory and checker implementation. That reviewer was independent of their
authors but was not blind to the reports; its exposure and scope are recorded.

Each binder is classified as a source premise, a standing assumption, a typing
requirement, an explicitly approved correction, or an excess hypothesis. The
reports also record normalization, quantifier order, constant dependence and
boundary cases. Anonymous Lean applications independently spell out selected
scalar formulas and error definitions, then use the existing endpoints to prove
those types. The reproducer also exports the actual compiled binder lists and
checks the endpoint axiom reports.

The review adapts the
[statement-audit](https://github.com/scottnarmstrong/LeanAutoformalizationSkills/blob/601fe274276d93052ef645f0ff2c1a355e8e5b16/skills/lean-statement-audit/SKILL.md)
and [source-inventory](https://github.com/scottnarmstrong/LeanAutoformalizationSkills/blob/601fe274276d93052ef645f0ff2c1a355e8e5b16/skills/build-proof-dependency-graph/SKILL.md)
methods from LeanAutoformalizationSkills. This is a review of existing proofs,
with dated source snapshots. It does not claim that collection's complete
author-approved frozen-statement workflow or its full audit seal. The project
checker is an original implementation; no third-party helper code is vendored.

## Reproduce the audit checks

From the repository root, with Python 3.11 or newer:

```sh
python3 scripts/check_statement_audit.py
```

This verifies the recorded source and report hashes, endpoint snapshots,
manuscript inventory and dependency structure. Success prints
`STATEMENT AUDIT RECORDS CURRENT`. It checks freshness and consistency; it does
not rerun a mathematical review.

After setting up the pinned Lean dependencies using [[verify|the verification
guide]], run:

```sh
python3 scripts/check_statement_audit.py --lean
```

This builds the two endpoint modules, exports their compiled binders, creates
temporary Lean files for the anonymous applications, and checks their axiom
reports. Success prints `STATEMENT AUDIT LEAN PROBES PASSED`. Each run writes
fresh logs and a result under `.verify-work/statement-audit/`. These checks use
the existing build cache and run locally without a sandbox.

To exercise the checker’s rejection controls:

```sh
python3 scripts/test_statement_audit.py
```

The controls check omitted source tokens, missing dependency edges, stale
source/closure data, incorrect locators, duplicate use sites and stale bindings.

The complete proof reproducer remains:

```sh
bash scripts/verify.sh all
```

That command covers Lean, Comparator and Nanoda. The statement-audit command
does not rerun the two export checkers.

## What this review establishes

The reports make the source-to-formal interpretation inspectable and bind it to
a specific source revision. A successful Lean application checks the formal
type written in that application. It cannot decide whether its definitions
faithfully represent the manuscript; that remains a mathematical review task.

The inventory checks all occurrences of the declared recognizable TeX syntax
against the source. Human interpretation is still needed to identify and assess
unnamed arguments. An item being inventoried, mapped or excluded is not a claim
that it has a Lean proof. In particular, source-level omissions and alternative
formal proof routes must be read with their explanations.

The review is limited to the four endpoints and the explicitly listed semantic
definitions and source regions. It is not a new line-by-line review of all 270
proof modules. Independent human peer review and manuscript-author endorsement
have not been established. The Letter's geometric entropy and large-dimension
claims retain the scope recorded in [[formalization|Scope and evidence]].
