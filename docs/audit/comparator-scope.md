# Comparator's specification boundary

The original clarification was checked on 2026-10-08 against proof-source snapshot
`e61724d6550796acb71afed896a57797a7a78468` and the pinned Comparator revision
`a4f696825c583ed8a5b4060d9a0faa5b882d365b`. It supplements the
[statement audit](../audit.md); it does not change the original review's date,
source snapshot or agent-review status. The physical interface extension below
is a separate October 8 addition on `main`, after the frozen release candidate;
its source and check records are linked separately. No new human review is
claimed.

## Imported definitions are compared

Comparator recursively compares imported constants used in a statement, as
implemented in its pinned
[comparison routine](https://github.com/leanprover/comparator/blob/a4f696825c583ed8a5b4060d9a0faa5b882d365b/Comparator/Compare.lean).
It does not skip `canonicalOrbitState`. If only the solution's definition changes,
it disagrees with a fixed expected export and is rejected.

If a shared project definition changes and both environments are rebuilt from
that change, agreement between the new exports does not itself establish
agreement with the paper. Other identification proofs may fail, and old
source-bound evidence becomes stale. A successful new comparison alone cannot
certify unchanged mathematical meaning. This is the specification-independence
limitation identified in [Theorem 2's audit](theorem2.md#t2-f04-comparator-fixture-shares-the-deepest-source-facing-definitions),
separate from proof checking. Theorem 1 has the same distinction for its shared
Haar construction, with a narrower project interface.

## Existing physical-state identification

The theorem
[`SchurWeyl.canonicalWeightTensorState_eq_orbit`](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/e61724d6550796acb71afed896a57797a7a78468/lean/FreeEntropy/PhysicalOrbitChannels.lean#L23)
identifies the supported physical tensor block with `canonicalOrbitState`.
The third Theorem 2 application in the
[statement probes](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/e61724d6550796acb71afed896a57797a7a78468/metadata/statement-audit/probes.json)
rewrites both states through this bridge and applies the endpoint. Its
[recorded incremental check](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/e61724d6550796acb71afed896a57797a7a78468/metadata/statement-audit/checks.json)
passed on 2026-10-07 at 00:07 UTC, including the bridge's axiom audit. That run
used an existing build and was unsandboxed; it was not a fresh-checkout run.

This is a checked composition for the constructed representations. It does not
replace an independently specified representation and projector interface.

## Physical interface extension

The additional
[`Theorem2Physical` challenge](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/lean/ComparatorChallenges/Theorem2Physical.lean)
specifies a linear isometric inclusion

\[
J : \mathcal H_\mu \hookrightarrow (\mathbb C^d)^{\otimes |\mu|},
\qquad J^\dagger J=I,
\]

and the normalized compression of
\(J^\dagger\rho^{\otimes |\mu|}J\). Tensor degree is the literal sum of the
partition rows. The density matrix, tensor entries, trace normalization and
zero-trace fallback are independently restated. In the original implementation,
[`irrepTensorEmbedding`](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/e61724d6550796acb71afed896a57797a7a78468/lean/FreeEntropy/ExteriorPhysicalIrrep.lean#L43)
is a matrix whose rows index tensor space and whose columns index irrep space;
`tensorDegree_eq_sum` identifies the tensor degree for a partition.

A function between index types does not specify that linear isometry. Its
direction also matters: the tensor space is generally larger than the irrep.
For example, the tensor square of a two-dimensional space has dimension four,
while its symmetric-square irrep has dimension three.

The forward and reverse PRV copies are arbitrary matrices `W` with
`Wᴴ * W = 1`, satisfying the explicit Lie intertwining equations. Their
projectors are the literal `W * Wᴴ`, and the normalized Choi contractions are
independently restated. The
[`Theorem2Physical` solution](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/lean/FreeEntropy/Theorem2Physical.lean)
proves both error bounds for every qualifying choice of tensor and PRV
embeddings. A second root, `theorem2_physical_realizations_exist`, proves such
choices exist for every admissible pair of rows. These existence and
identification results discharge the interface conditions rather than leaving
conditional existence claims unresolved.

Current `main` checks this fourth configuration and both roots in Comparator and
Nanoda, bringing the totals to four configurations and six roots. The frozen
`v0.1.0-rc1` tag and archive retain three configurations and four roots; they do
not contain this extension. The
[physical interface map](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/physical-interface-map.json)
connects the raw objects and new declarations to the manuscript, and the
[audit extension bridge](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/statement-audit/physical-interface-bridge.json)
records the addition separately from the original audit.

## Remaining shared specification

The new expected statements avoid references to `canonicalOrbitState`, the
constructed tensor-source states, and the canonical Choi projector definitions.
They still share canonical irrep coordinate indices, unitary representations,
Lie generators and the auxiliary highest-weight model, together with numerical
bounds, trace distance and partial-trace primitives. Their full reconstruction
from an independently specified representation theory remains outside this
extension. Irreducibility, cyclicity and highest-weight identification remain
supported by the existing representation proofs and source correspondence;
they are not independently restated here.

The compiled dependency guard
[`check_physical_spec.lean`](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/scripts/check_physical_spec.lean)
starts at the two expected theorem types and follows the types, bodies and
structural metadata of referenced declarations. It rejects references to the
constructed states/projectors and final proof modules. Deliberate challenge
proof holes are excluded at the roots. Its
[negative controls](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/scripts/test_physical_spec.py)
and the guard run in the `all` reproducer. The
[closure report](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/verification/2026-10-08/physical-spec.json)
lists the remaining shared dependencies.

This makes the reduced specification boundary inspectable and reproducible.
It does not certify manuscript meaning or establish independent human review.
The supplied comments did not identify an incorrect endpoint or an unproved
production theorem.
