# Lean formalization and reproduction

The Lean development proves the two main statements of the current
[[Article]]: optimal known-spectrum memory (`thm:qmdl`) and finite cloning
accuracy (`thm:main`). [[proof-structure|The proof map]] explains the route
from actual representations and channels to those endpoints. The frozen
[v0.1.0-rc1 release](releases/v0.1.0-rc1.md) provides source archives and checksums.
Software is licensed under **Apache-2.0**, credited to **Jinzhao Wang and
contributors**; manuscripts and third-party files retain their rights and notices. The
[Lean explorer](proof-explorer.md) lets you search the declarations, inspect
their compiled types and follow direct references in either direction.

The [[correspondence|Paper ↔ Lean correspondence]] connects each mapped Article
and Letter statement to its source label, informal proof guide, exact Lean
declarations and coverage notes. It also explains how to review whether the
informal and formal statements match.

## What is checked

| Result | Formal statement | Scope |
| --- | --- | --- |
| [[results/achievability|Theorem 1, achievability]] | `FreeEntropy.theorem1_achievability` | Actual CPTP encoders and decoders, exact additive memory constant, uniform error $O(\log n/\sqrt n)$. |
| [[results/converse|Theorem 1, converse]] | `FreeEntropy.theorem1_converse` | The matching lower bound for arbitrary physical codes with vanishing Haar-average error. |
| Worst-case converse | `FreeEntropy.theorem1_converse_of_uniform` | Vanishing worst-case error implies the same lower bound. |
| [[results/cloning-fidelity|Theorem 2, original channels]] | `FreeEntropy.ExteriorRepresentation.theorem2_cloning_accuracy_choi` | Both normalized Choi-projector channel bounds, for supported rows and dominant signed difference. |
| Theorem 2, physical specification | `FreeEntropy.ExteriorRepresentation.theorem2_cloning_accuracy_physical` | Both bounds for any isometric physical embeddings and PRV copies satisfying the representation equations. |
| Physical realization existence | `FreeEntropy.ExteriorRepresentation.theorem2_physical_realizations_exist` | All embeddings required by the physical specification exist for every admissible pair of rows. |

The constructed Cartan and Petz forms are also connected to the original
channels by proved identities. Theorem 1 includes $d=1$ and all positive
ranks; Theorem 2 is stated for $d\ge2$ and includes rank one and equal rows.
Positive eigenvalues are distinct and fixed in the asymptotic limit.

The original final statements do not take representation existence, dimensions,
weight bounds, covariance, concentration or source-transfer estimates as
unproved premises. The library supplies these inputs. The precise statements
and their source labels are connected by
[the manuscript-to-Lean map](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/natural-language-map.json).

The October 8 physical specification extension independently restates the
tensor source, normalization and Choi contractions using arbitrary isometries.
Its existence root makes the representation conditions nonvacuous. It still
shares canonical representation coordinates and numerical definitions;
[Comparator's specification boundary](audit/comparator-scope.md) describes
this limit. The [physical interface map](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/physical-interface-map.json)
and [audit extension bridge](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/statement-audit/physical-interface-bridge.json)
record the addition separately from the historical four-endpoint audit and
frozen candidate.

## Verification evidence

The [[audit|retrospective statement audit]] separately reviews the manuscript
interpretation of the four primary endpoints. It includes expanded hypotheses,
definition scope, a source argument inventory, independent adversarial findings
and reproducible exact-type Lean applications. This remains agent review.

The current source record covers **273 proof modules**, **1,883 proved
declarations**, and **2,512 public declarations audited**. The October 8 build
of `All` and axiom audit used existing dependency and project artifacts; it was
a source-matching incremental run. The only allowed
axioms are Lean's `propext`, `Classical.choice` and `Quot.sound`.

| Check | Recorded local result | What it establishes |
| --- | --- | --- |
| Current Lean build and axiom audit | Passed, incremental | The formal proofs elaborate and their actual transitive axioms are permitted. |
| Physical specification guard and seven controls | Passed | The compiled expected types avoid the excluded state/projector and final-proof dependencies; forbidden fixtures are rejected. |
| Comparator and Lean export replay | All four configurations and six roots passed, unsandboxed | The expected statements and referenced definitions match the solution; exported proofs replay in Lean. |
| Nanoda 0.4.19 | All four configurations and six roots passed, unsandboxed | A separately implemented Rust kernel accepts the fresh exported solution dependencies. |
| Linux-sandboxed Comparator | Not run in the published local record | Requires a capable Linux host and real Landrun. |
| Independent human review | Not established | Mechanical checking does not itself certify the interpretation of the manuscript. |

Current `main` has four configurations and six roots: achievability, both
converse variants, Choi cloning, the physical cloning bound and physical
realization existence. Its `all` and `comparator` modes also run the compiled
specification boundary guard and seven acceptance/rejection controls.
The frozen `v0.1.0-rc1` retains three configurations and four roots, with
270 proof modules, 1,873 proved declarations and 2,499 audited public declarations.
Comparator challenge files intentionally contain expected-statement
proof holes; these fixtures are separate from the proved library. The
[challenge guide](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/lean/ComparatorChallenges/README.md)
records which definitions are independently restated and which are reused.

The local evidence is tied to source fingerprints, rather than to whichever
files happen to be present later. Consult the
[audit summary](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/lean/verification/summary.json),
[Comparator record](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/lean/ComparatorChallenges/verification-status.json)
and [Nanoda record](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/lean/ComparatorConfig/nanoda-status.json).
The [October 8 execution record](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/verification/2026-10-08/verification-result.json)
records the current extension separately from the earlier evidence.
The complete local wrapper run exited zero with `VERIFICATION PASSED: all`.
Nanoda controls and four fresh solution exports were checked with a reused
binary whose SHA-256 matches the preserved pinned source build. This did not
rebuild Rust or establish a new hosted CI result.
The [release-tag clean-source CI](https://github.com/JWang226/Quantum-Minimum-Description-Length/actions/runs/37566361840)
passed for exact release commit `4ce43849fba096ec2174097625711323f1ce5ee8`:
exported-source Lean build and axiom audit, expected-statement comparisons,
Lean replay, and pinned Nanoda controls and kernel checks. Dependencies were
fetched into the exported tree without the local checkout's package symlinks.
Comparator and Nanoda were unsandboxed; the separate Landrun job was skipped.
This is an actual completed run, separate from the preserved local evidence.
It verifies the frozen candidate's earlier sources and does not check the
later physical-interface extension.

## Reproduce the checks

Use [[verify|the verification guide]] for prerequisites, pinned tools, fresh
logs, success markers and the separate Linux sandbox procedure. From the
repository root, run:

```sh
bash scripts/verify.sh all
```

Success ends with `VERIFICATION PASSED: all`; a failed check returns nonzero.
The guide also documents separate `lean`, `comparator` and `nanoda` modes.
Comparator and Nanoda execution is local and unsandboxed.

## Limits of the claim

The current author-supplied [Article](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/manuscript/article.tex)
and [Letter](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/manuscript/letter.tex) are included
at the repository root, with their shared bibliography and the Letter's figure.
The Article source is unchanged from the independent proof check. The
[Letter source map](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/letter-source-map.json)
binds both source snapshots and records equation-level coverage.

The Letter's full-rank and rank-deficient QMDL formulas follow the checked
Article memory endpoints. Its ambient tube-volume expansion, explicit
$C_{d,r}$ comparison with $\tfrac12\chi_{\mathrm{phy}}(\rho;n^{-1})$, general
multiplicity geometry and conditional double-scaling bridge are manuscript
claims without separate Lean certificates.

This is not a formalization of the entire Article, Letter or Notes. In
particular, the later universal-coding overhead, block-entropy asymptotic,
unknown-spectrum discussion and broader free-entropy/programming claims
are outside the two-theorem certificate. General channel propositions are
not all established in their full paper-level generality. The proof also
uses some sufficient supporting bounds rather than the sharpest constants
in intermediate paper lemmas.

See the [formalization status](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/docs/FORMALIZATION_STATUS.md)
for precise scope, [formalization.yaml](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/formalization.yaml)
for machine-readable provenance, and
[the release checklist](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/docs/RELEASE_CHECKLIST.md)
for remaining human and sandbox review items and the confirmed licensing record.
