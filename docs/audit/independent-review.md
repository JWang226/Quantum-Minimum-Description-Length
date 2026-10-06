---
title: Independent adversarial review
---

<!-- Copyright (c) 2026 Free Entropy formalization contributors.
     See LICENSE and NOTICE for license and attribution. -->

# Independent adversarial review

No in-domain discrepancy found in the four endpoint statements or selected source-facing definitions. Identified checker and grouped-closure wording issues were repaired and checked. Semantic correspondence remains bounded agent review, separate from mechanical proof checking.

## Identity and scope

Adversarial reviewer; not an endpoint-report author, source extractor, proof author or checker author. Reviewer: `/root/audit_adversarial_review`. Read raw article and implementation directly and challenged the drafts. The first batched read exposed draft endpoint reports concurrently with raw source, so this is explicitly not a blind source-first reconstruction. No repository edits were made.

This is a retrospective adversarial review, not an author-approved freeze/seal or human endorsement. No rewrite of Lean, fresh `sorry`, or approval procedure is called for. I did not reproduce the full 270-module proof or independently run the root reviewer’s Lean probes.

Article SHA-256: `09fc0a6bb205180cd820be94d843a1dc0d4342a543492e30dde54e367ae843a9`.

## Findings

### ADV-01 — Draft coverage checker does not establish inventory completeness

Severity: medium; status: RESOLVED_AND_RECHECKED.

- scripts/check_statement_audit.py:93–125 checks only provided inventory records and graph endpoints/cycles; it does not rescan article.tex or require root nodes/closures.
- The draft source-coverage.json uses edge keys from_node/to_node, while this draft checker expected from/to. Direct checking the actual draft raised KeyError: from.
- Nonmutating calls to check_coverage accepted a copy with empty nodes/inventory/edges, and a copy with all edges deleted. Hash checks outside this function can reject an un-rebaselined edit but do not establish extraction completeness.

A structure-only pass must not be represented as proof that every required source item or dependency was extracted. The present schema mismatch also blocks checking the real draft coverage.

Rescan supported raw tokens, validate their exact one-to-one locator/raw inventory; validate declared source hashes, locators, required roots and closure; use the actual edge schema. Preserve a semantic-completeness disclaimer.

Parent repaired checker: independent raw rescan, source hash and locator checks, required roots and reachability, recomputed per-root closure counts, and correct edge schema. Edge uniqueness includes consuming locator, preserving two legitimate uses of the same prerequisite. Fresh calls on integrated coverage accepted the current data and rejected missing token, empty edges and stale closure counts; see adversarial-checker-final-probes.json. Original finding is historical, not an outstanding blocker.

### ADV-02 — Petz is included through a grouped proposition, not needed by the finite cloning estimate

Severity: low; status: RESOLVED_WORDING_CLARIFIED.

- article.tex:540–552 states both normalized-adjoint and Petz characterizations in one proposition.
- article.tex:1759–1764 uses the normalized adjoint to derive the reverse partial trace; it does not use the Petz formula.
- source-coverage.json prop:reverse has prerequisites prop:reverse#petz and prop:reverse#dual, so T2 reaches ext:petz-formula by consuming the combined proposition.
- source-coverage scope ambiguity says Cartan and Petz forms are identities used conjunctively to prove the original Choi-channel theorem.

The 75/47 root closure is a closure of grouped source results. It is not a minimal list of indispensable facts. The conjunctive-Petz wording overstates the source proof dependency.

Clarify grouping and say the reverse-error proof consumes the scaled-adjoint part; retaining the Petz subargument as part of a grouped proposition is acceptable.

Parent clarified the integrated inventory as grouped-result closure, with the scaled-adjoint part consumed by T2; Petz remains part of the grouped supporting proposition. The graph retains 137 use-site edges, which need not mean 137 distinct ordered node pairs. No Lean change is indicated.

### ADV-03 — Binder fingerprint and byte freshness are not semantic correspondence certificates

Severity: info; status: ACCEPTED_LIMITATION.

- scripts/export_statement_audit.lean exports actual telescope names, binder kinds, types, proposition flags and conclusion.
- Draft run_lean compares only name/kind to the manifest; compiled_statement_sha256 is checked against catalog text in structural mode.
- Anonymous exact-type application probes supply the relevant elaboration check; neither mode reruns Comparator/Nanoda or proves natural-language correspondence.
- Current output says STATEMENT AUDIT RECORDS CURRENT and explicitly Structural freshness only; Lean mode is labeled incremental.

No false mathematical-success label was observed. A reader must distinguish actual binder inventory, exact-type probes, byte freshness, and semantic agent review.

Retain current scope labels; do not call a name/kind comparison full statement equality.

No required change if these scope limits remain explicit.

### ADV-04 — Important endpoint objections are resolved on the manuscript domain

Severity: info; status: NO_COUNTEREXAMPLE_FOUND.

- Theorem1Complete.lean:23–66 has only spectrum/code/reliability inputs; scalar d=1 handled internally.
- Statements.lean:25–32 includes rank positivity, rank bound, ordered positive spectrum, zero padding, and trace-one normalization.
- PhysicalSchurProtocol.lean:25–48 and PhysicalCanonicalConverse.lean:31–55 use actual conjugated diagonal density tensors and normalized-Haar mean. PhysicalUniformError.lean:22–69 handles nonempty bounded supremum and average comparison.
- Channels.lean:95–102 requires complex linearity, trace preservation, positivity, and every finite ancilla amplification. SectorChannels.lean:73–74,122–124 sums channels into the same memory algebra, so there is no uncounted sector label.
- TraceDistance.lean:32–35 is Tr sqrt(X†X)/2 on the difference. WeylCombinatorics.lean:178–183 matches the full logarithmic/factorial expression.
- Theorem2Choi.lean:79–96 fixes explicit C(d,r,qx) before row/unitary dependence; CanonicalRowBounds.lean:17–22 uses integer subtraction before absolute value, and 46–55 computes the supported minimum gap.
- SignedAuxiliaryModel.lean:18–60 proves a determinant-shifted auxiliary realizes the signed difference; CanonicalChoi.lean:23–85 constructs projector/isometry/rank/multiplicity one.
- PhysicalOrbitChannels.lean:23–32 proves the normalized tensor-state bridge for antitone supported rows; CanonicalMonomialState.lean:169–186 proves its positive-normalizer reduction.

I found no excess hypothesis, weakened error criterion, missing classical memory, silently unsigned difference, missing terminal gap, or row/eigenbasis-dependent cloning constant in the selected endpoints.

Maintain source-domain restrictions and reported representation-coordinate/totalization limits.

Bounded independent adversarial corroboration, not an exhaustive transitive proof review or a global helper-definition seal.

## Independent coverage checks

- **raw-token-rescan — passed:** Independent regex patterns allowing whitespace matched all 90 labels, 38 citation commands, and 151 cross-reference commands, with identical line/raw multiplicities.
- **environment-count — passed:** Independent raw counts: 4 thm,10 lem,5 prop,1 defn,2 rem (22 theorem-like),22 proof. These match the inventory totals.
- **coarse-regions — passed_with_scope_limit:** Every nonblank line is inside a mapped/excluded coarse region except four section headings at 293,321,1294,1852; their labels are inventoried. This checks coverage of text locations, not granularity/semantic completeness.
- **source-gaps — scope_appropriate:** The three SOURCE_GAP labels concern uncited Cartan/Hom, GT counting and Casimir input provenance. Raw use sites support the reported absence of local derivations/precise citations. This is not evidence of false source results, Lean axioms, or omitted formal proofs.
- **exclusions — sampled_and_reasonable:** Read excluded Cartan-factorization interpretation, D=0 identity context, and closure-relevant raw proof; factorization and commutativity are not used by retained-branch error proof. Lossless overhead/unknown-spectrum results are downstream/outside the four endpoints. No important missing proof region was detected.
- **lean_execution — not_run_by_this_reviewer:** Parent runs compiled exact-type/axiom probes. This reviewer read definitions and proof applications but did not independently compile/rebuild the 270-module library.

## Remaining limits

The diagonal reference state parametrizes the full fixed-spectrum orbit mathematically; I did not find or prove an arbitrary-reference-state API wrapper. Internal normalizedBlock and arbitrary-row canonicalOrbitState are total beyond manuscript domains, while supported-row bridge arguments justify their endpoint use. The T2 root proof does not itself consume the separate physical-state bridge; that is a packaging/dependency fact, not an identified mathematical mismatch. Forward multiplicity-one and highest-weight range results support PRV identification without an exact paired author-frozen uniqueness declaration. These are appropriate retrospective limitations, not reasons to demand the unrelated full author-seal workflow.

The graph groups some compound statements. Its direct-use edges and external boundary records are useful source navigation; token coverage and byte hashes cannot decide that every unnamed premise has been identified or semantically matched to Lean.

## Final checker disposition

The integrated coverage passes the repaired checker. Fresh nonmutating mutations removing a label, removing every edge, or changing root closure sizes to 1/1 are rejected. The repeated source dependency is retained at its two separate consumer sites. These checks establish the described structural properties, not mathematical completeness. Final snapshots and probe evidence are in the JSON companions.

A new root-run anonymous physical-state probe explicitly consumes the normalization/physical-state bridge; its compilation was pending when this adversarial review closed. That supplements the check while the production endpoint proof remains unchanged.


The integration runner subsequently compiled the physical-state composition successfully. See [[audit|the audit overview]] for current results and the [structured review](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/statement-audit/adversarial-review.json).
