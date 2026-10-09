# Comparator's specification boundary

This clarification was checked on 2026-10-08 against proof-source snapshot
`e61724d6550796acb71afed896a57797a7a78468` and the pinned Comparator revision
`a4f696825c583ed8a5b4060d9a0faa5b882d365b`. It supplements the
[statement audit](../audit.md); it does not change the original review's date,
source snapshot or agent-review status. No new human review or kernel run is
claimed here.

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

## A stronger independent interface

An independently specified expected-statement interface should describe a
linear isometric inclusion

\[
J : \mathcal H_\mu \hookrightarrow (\mathbb C^d)^{\otimes |\mu|},
\qquad J^\dagger J=I,
\]

and the normalized compression of
\(J^\dagger\rho^{\otimes |\mu|}J\). In the implementation,
[`irrepTensorEmbedding`](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/e61724d6550796acb71afed896a57797a7a78468/lean/FreeEntropy/ExteriorPhysicalIrrep.lean#L43)
is a matrix whose rows index tensor space and whose columns index irrep space;
`tensorDegree_eq_sum` identifies the tensor degree for a partition.

A function between index types does not specify that linear isometry. Its
direction also matters: the tensor space is generally larger than the irrep.
For example, the tensor square of a two-dimensional space has dimension four,
while its symmetric-square irrep has dimension three.

The interface must also characterize the representation and PRV projector,
including irreducibility, cyclicity and highest weight, and transport state and
channel coordinates consistently. The current challenge is not claimed to
provide this stronger independently restated specification. It is a useful
further correspondence check; the supplied comments did not identify an
incorrect endpoint or an unproved production theorem.
