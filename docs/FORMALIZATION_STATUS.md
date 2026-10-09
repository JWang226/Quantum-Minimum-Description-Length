# Formalization status and scope

The Lean development proves the requested conclusions of manuscript Theorems 1 and 2 for actual finite complex matrices and completely positive trace-preserving channels. It does **not** claim to formalize the entire manuscript. The source manuscript is [article.tex](../article.tex); the primary statement locators are its TeX labels, not theorem numbering alone.

## Main results

| Manuscript statement | Lean declaration | Source |
| --- | --- | --- |
| Theorem 1, achievability (`thm:qmdl`, `thm:achievability`) | `FreeEntropy.theorem1_achievability` | [Theorem1Complete.lean](../lean/FreeEntropy/Theorem1Complete.lean) |
| Theorem 1, Haar-average converse (`thm:qmdl`, `thm:converse`) | `FreeEntropy.theorem1_converse` | [Theorem1Complete.lean](../lean/FreeEntropy/Theorem1Complete.lean) |
| Theorem 1, worst-case converse | `FreeEntropy.theorem1_converse_of_uniform` | [Theorem1Complete.lean](../lean/FreeEntropy/Theorem1Complete.lean) |
| Theorem 2, original Choi-projector formulas (`thm:main`) | `FreeEntropy.ExteriorRepresentation.theorem2_cloning_accuracy_choi` | [Theorem2Choi.lean](../lean/FreeEntropy/Theorem2Choi.lean) |
| Theorem 2, equivalent Cartan formulas | `FreeEntropy.ExteriorRepresentation.theorem2_cartan_cloning_accuracy` | [Theorem2Canonical.lean](../lean/FreeEntropy/Theorem2Canonical.lean) |
| Theorem 2, literal Petz recovery expression | `FreeEntropy.ExteriorRepresentation.theorem2_cloning_accuracy_petz` | [Theorem2Petz.lean](../lean/FreeEntropy/Theorem2Petz.lean) |
| Theorem 2, independently stated physical source and PRV formulas | `FreeEntropy.ExteriorRepresentation.theorem2_cloning_accuracy_physical` | [Theorem2Physical.lean](../lean/FreeEntropy/Theorem2Physical.lean) |
| Existence of all physical-interface realizations | `FreeEntropy.ExteriorRepresentation.theorem2_physical_realizations_exist` | [Theorem2Physical.lean](../lean/FreeEntropy/Theorem2Physical.lean) |

The original [machine-readable mapping](../metadata/natural-language-map.json)
locates the original endpoints, their definitions and principal supporting
lemmas. The [physical interface map](../metadata/physical-interface-map.json)
records the two additional roots and their specification. Both use manuscript
labels, fully qualified Lean names and source locators. Labels and declaration
names are authoritative; line numbers are navigation hints that may change.

## What the endpoints mean

Theorem 1 fixes a normalized spectrum with distinct positive eigenvalues and permits zero eigenvalues. The source is the literal tensor power of `U diag(x) U†`, with `U` ranging over the actual unitary group. Constructed encoders and decoders do not depend on `U`. Memory cost is the base-two logarithm of the dimension of the entire retained register. Achievability includes the manuscript's additive constant and a worst-case error of order `log(n)/sqrt(n)`. The converse applies to arbitrary physical CPTP codes with vanishing normalized-Haar average error. All positive ranks and dimensions, including dimension one, are covered.

Theorem 2 uses supported antitone natural rows and a dominant integral difference, which can have negative entries. It proves both original normalized Choi-projector error bounds for every unitary eigenbasis. The exact row L1 difference and minimum supported adjacent gap are computed in Lean. Rank one and coincident rows are included. Its explicit admissible constant is

`choose(d,2) + 3*N*q/(1-q)^(N+1)`, where `N=choose(r,2)`.

The original final theorem endpoints do not take representation existence, decomposition, dimension formulas, multiplicity bounds, spectral normalization, covariance, concentration, local cloning errors or source-transfer estimates as unproved premises. These are constructed or proved in their dependencies. Earlier conditional reductions remain useful intermediate lemmas; their hypotheses should not be confused with those of the final endpoints.

The October 8 physical interface extension quantifies over arbitrary tensor
embeddings and PRV isometries satisfying explicit representation equations.
It independently restates the density matrix, tensor entries, trace
normalization and Choi contractions using `W * Wᴴ`. Its companion existence
theorem proves all required realizations exist, and the solution derives
state/projector identification. Those conditions are not unresolved existence
claims. The expected statements still share canonical representation
coordinates, unitary actions, Lie generators, the auxiliary model, numerical
bounds and matrix primitives. The [physical interface map](../metadata/physical-interface-map.json)
and [specification-boundary explanation](audit/comparator-scope.md) record this
scope; the extension does not independently rebuild representation theory.

## Fidelity and boundaries

The current companion [Letter](../letter.tex) is bundled with
[its figure](../compression.pdf) and the shared bibliography. The
[companion source map](../metadata/letter-source-map.json) records exact
source hashes and relates its labeled equations to the Article declarations.
The Letter's known-spectrum QMDL formulas (`eq:result_qmdl`,
`eq:rank_def_qmdl`) specialize Theorem 1. Its physical tube-volume definition
and expansions, the explicit half-entropy offset at resolution `n^-1`, and
the conditional large-dimension bridge (`rem:bridge`) have no separate Lean
certificates. Arbitrary repeated positive eigenvalues remain outside the
memory endpoints even though the Letter derives their geometric entropy.

The formalization uses a diagonal reference state and all unitary conjugations to represent the known-spectrum family. Matrix carriers and row indices are explicit and zero-based. The converse uses an extended-real `liminf`. These choices encode the manuscript's conclusions.

The proof is not a line-by-line transcription. For example, the physical concentration proof uses its own polynomial prefactor; the final canonical converse uses the positive uniform gap `(1-q)^(choose(d,2)+1)` rather than requiring the manuscript's sharper intermediate constant. The padded target's precise dimension asymptotic is proved. Explicit replacement channels handle atypical sectors. These choices suffice for the stated theorem conclusions.

The Choi, Cartan and Petz identifications are proved for the actual canonical pairs needed by Theorem 2. This does not assert a construction of the generalized PRV channel for every arbitrary pair of dominant integral weights. The later universal-coding redundancy, block-entropy and unknown-spectrum discussion is outside the requested scope. The mapping also distinguishes exact auxiliary statements from supporting bounds or specializations.

## Verification and review

The current source-matching incremental build of `All` and axiom audit passed
for **273 proof modules**, **1,883 proved declarations** and **2,512 public
declarations audited**, at proof-source SHA-256
`33379ffb4c7547fdc221fb3696f360465d87aaad2247e12707a7b95e557b5cac`.
It reused existing Lean dependency and project artifacts; it is not a new
clean-checkout result. The proof development has no unresolved `sorry`/`admit`
placeholders and no project-specific axioms. Its audited dependencies use only
`propext`, `Classical.choice` and `Quot.sound`, the standard Lean axioms allowed
by the project. See the [current audit summary](../lean/verification/summary.json).

The earlier October 6 campaign covered 270 modules, 1,873 proved declarations
and 2,499 public declarations. It rebuilt project proof artifacts while
retaining verified warm dependency artifacts; it did not reinstall dependencies.
Its [reproducibility record](../metadata/verification/2026-10-08/historical/lean-reproducibility.json)
is preserved as historical evidence. The current extension has a separate
[execution record](../metadata/verification/2026-10-08/verification-result.json)
and [audit extension bridge](../metadata/statement-audit/physical-interface-bridge.json).

The separate [release-tag clean-source CI](https://github.com/JWang226/Quantum-Minimum-Description-Length/actions/runs/37566361840) passed for exact `v0.1.0-rc1` commit `4ce43849fba096ec2174097625711323f1ce5ee8`. It built an exported source copy with fresh locked dependency checkouts and the public Mathlib cache, without the local checkout's package symlinks. Lean compilation and the transitive axiom audit, all three expected-statement comparisons and kernel replays, and pinned Nanoda controls and proof checks passed. Comparator and Nanoda were unsandboxed; the optional Linux/Landrun job was skipped.

That release check covers the frozen candidate's 270 modules and 2,499 audited
public declarations, rather than the later physical extension. Counts describe
particular audited source fingerprints. Running `lean/check.sh` rebuilds and
regenerates the local evidence. A new source archive includes the current
portable summary and named dated execution records; CI generates fresh logs.

The project is **agent-reviewed**. Agents checked the mathematical interpretation of the endpoints as well as Lean compilation and the axiom dependencies. Independent human peer review and manuscript-author endorsement have not been established and are not claimed. Kernel checking verifies the formal statements; it does not by itself certify the choice of those statements as a faithful interpretation of prose.

A [retrospective statement audit](https://jwang226.github.io/Quantum-Minimum-Description-Length/audit/)
adds expanded binder tables, selected definition reviews, a manuscript argument
inventory, and a separate adversarial agent review. Seven fresh anonymous Lean
applications compiled, including the physical-state formulation of Theorem 2.
No excess endpoint hypotheses or substantive mismatch on the manuscript domain
were found. The reports explicitly retain limits concerning total helper domains,
grouped source dependencies and the depth of semantic review; they do not claim
an exhaustive independent audit of all proof modules or a human/author seal.
The original four-endpoint audit and its source snapshots retain their dates
and scope. The physical-interface bridge records the additive extension
separately; it does not relabel the earlier audit as a new source-first review.

The additional Comparator entrypoints are:

- [Theorem1Achievability.json](../lean/ComparatorChallenges/Theorem1Achievability.json)
- [Theorem1Converse.json](../lean/ComparatorChallenges/Theorem1Converse.json), covering both converse variants
- [Theorem2Choi.json](../lean/ComparatorChallenges/Theorem2Choi.json)
- [Theorem2Physical.json](../lean/ComparatorChallenges/Theorem2Physical.json), covering the universal physical bound and realization existence

Current `main` has four configurations and six roots. Its `all` and `comparator`
reproducers include a compiled specification dependency guard and seven
acceptance/rejection controls, which passed in the October 8 local run.
The guard checks the expected theorem types and
their transitive declarations, excluding the deliberate challenge root proof
holes. It rejects dependence on the canonical state/projector constructions
and final proof modules. This enforces the documented shared boundary; it does
not certify manuscript interpretation.

All four current configurations and six theorem roots passed unsandboxed
Comparator statement/definition comparison, axiom checks and Lean kernel
replay. They use freshly exported proofs from the current source-matching local
build; this is not a new clean-checkout run.

All four current solution exports and six roots also passed pinned Nanoda
0.4.19, including the physical-interface export's 58,990 declarations with no
errors. The freshly exported proofs and rerun acceptance/rejection controls
were checked with a reused binary whose SHA-256 matches the preserved pinned
source build. This was unsandboxed and did not rebuild Rust. The full local
wrapper exited zero with `VERIFICATION PASSED: all`.

The historical three-configuration checks cover the earlier four roots, and
the frozen candidate retains that configuration set. The current [Comparator record](../lean/ComparatorChallenges/verification-status.json),
[Nanoda record](../lean/ComparatorConfig/nanoda-status.json) and
[extension execution record](../metadata/verification/2026-10-08/verification-result.json)
bind their respective runs to source and export hashes. A Linux-sandboxed
Comparator run has not occurred.

Comparator challenge modules deliberately contain expected-statement proof holes. Those are specification fixtures, not unresolved proofs in `lean/FreeEntropy/`, and are kept outside the production proof audit. Consult the [execution report](../lean/ComparatorChallenges/verification-status.json) for the checked source fingerprints and the [challenge documentation](../lean/ComparatorChallenges/README.md) for the imported definitions that form the trusted statement boundary.

## Dependencies and provenance

The source requires the Lean toolchain and mathlib revision pinned in [lean-toolchain](../lean/lean-toolchain), [lakefile.toml](../lean/lakefile.toml) and [lake-manifest.json](../lean/lake-manifest.json). There are no missing local proof imports or imports of another private project. Any local `.lake/packages` symlinks are replaceable dependency caches, not proof sources required from another repository. Source provenance comments in `Channels.lean` and `CartanChannel.lean` credit adapted algebra from the previously available local Cloning development. [NOTICE](../NOTICE) identifies the affected files. The earlier source was identified privately at commit `dca79dc637649a44d41125387e534d0f6b747b84` and matched against the adaptation record. The maintainer confirmed authority to license the adaptations included here under Apache-2.0 on 2026-10-06; NOTICE records that confirmation.

The implementation and agent review used Codex with GPT-6-family agents. The exact deployed model version, reliable elapsed work time, token count and monetary cost are unknown; no estimates are presented as measured facts. Software is credited to **Jinzhao Wang and contributors**; older collective headers refer to that contributor credit. Manuscript authorship is separately listed in [formalization.yaml](../formalization.yaml). See [AI_PROVENANCE.md](AI_PROVENANCE.md) for the provenance record. The confirmed software license is **Apache-2.0**, as granted by [LICENSE](../LICENSE). Manuscripts, figure and third-party files retain their existing rights and notices.

The root metadata follows the [v0.3 formalization.yaml schema](https://github.com/mathlib-initiative/formalization.yaml/blob/main/schema/v0.3.schema.json), using the [OpenAI ten-proofs metadata](https://github.com/openai/ten-proofs/blob/main/formalization.yaml) as a format example. No affiliation, review claim, authorship or license from that example is transferred to this project.
