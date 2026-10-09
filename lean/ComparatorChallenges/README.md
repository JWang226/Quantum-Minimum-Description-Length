# Comparator challenges

These files follow the [ten-proofs challenge format](https://github.com/openai/ten-proofs/tree/main/ComparatorChallenges)
and the [September 29 AGMAI release recommendations](https://agmai.org/general-sep29/).
They contain independently written expected statements, with intentional `sorry`
holes. They are **not proofs**, are not imported by `FreeEntropy` or `All`, and are
excluded from the proof library's no-holes audit. Comparator checks the solution's
proof, including its transitive axiom closure.

| Configuration | Expected declarations | Solution module |
| --- | --- | --- |
| `Theorem1Achievability.json` | `FreeEntropy.theorem1_achievability` | `FreeEntropy.Theorem1Complete` |
| `Theorem1Converse.json` | `FreeEntropy.theorem1_converse`, `FreeEntropy.theorem1_converse_of_uniform` | `FreeEntropy.Theorem1Complete` |
| `Theorem2Choi.json` | `FreeEntropy.ExteriorRepresentation.theorem2_cloning_accuracy_choi` | `FreeEntropy.Theorem2Choi` |
| `Theorem2Physical.json` | `FreeEntropy.ExteriorRepresentation.theorem2_cloning_accuracy_physical`, `FreeEntropy.ExteriorRepresentation.theorem2_physical_realizations_exist` | `FreeEntropy.Theorem2Physical` |

Current `main` has four configurations and six theorem roots. The frozen
`v0.1.0-rc1` release has the original three configurations and four roots;
its tag and source archive do not include the physical interface extension.

Theorem 1's expected interface independently restates the spectrum, genuine CPTP
channels, tensor-power density matrices, trace distance, Haar-average and worst-case
error, and the complete QMDL formula. Its sole project import is the construction of
normalized Haar measure. Theorem 2 independently restates the literal partial-trace
Choi contractions in `Theorem2Choi`; its constructed representation, state, and
projector definitions are imported. This original trust boundary is explicit in
`trusted-boundary.json`. The additional `Theorem2Physical` challenge restates
the tensor-source normalization and Choi contractions, and quantifies over
arbitrary isometric embeddings satisfying explicit representation equations.
No challenge is an alias of a target proposition.

### Shared definitions and specification independence

An imported definition is still compared. If only the solution's
`canonicalOrbitState` differs from the fixed expected export, the pinned
Comparator rejects its differing body and dependencies. If a shared project
definition is changed and both environments are rebuilt from that change,
agreement between the new exports does not itself establish agreement with the
paper. Other Lean proofs may fail, and the recorded source hashes become stale;
a matching comparison alone is not a certificate of unchanged mathematical
meaning. Theorem 1 has the same distinction for its shared Haar construction,
with a narrower project interface.

For Theorem 2, the separately proved identification
`SchurWeyl.canonicalWeightTensorState_eq_orbit` identifies the supported physical
tensor block with `canonicalOrbitState`. The third Theorem 2 application in
[the statement probes](../../metadata/statement-audit/probes.json) rewrites both
states using this bridge and then applies the endpoint. Its
[recorded check](../../metadata/statement-audit/checks.json) passed, including the
bridge's axiom audit. This is a checked composition of mathematical
identifications, not an independently restated state/projector specification.

### Physical Theorem 2 extension

The new [physical challenge](Theorem2Physical.lean) uses a linear inclusion from
the irrep into tensor space, `Jᴴ * J = 1`, and literal matrix-entry products at
degree `∑ j, mu j`. `physicalIsometricState` normalizes the compression
`Jᴴ * ρ^⊗n * J` by its trace and explicitly supplies the maximally mixed
zero-trace fallback. The density matrix and normalized Choi contractions are
also independently redeclared. The forward and reverse projectors are `W * Wᴴ`
for arbitrary isometries satisfying the specified Lie intertwining equations.

The [solution](../FreeEntropy/Theorem2Physical.lean) proves two roots: both
error bounds for every such choice, and existence of all four embeddings for
every admissible pair of rows. The latter prevents a vacuous specification.
The proofs derive state and projector identification rather than assuming them.

This reduces the shared boundary; it does not independently reconstruct the
representation theory. The canonical coordinate indices, unitary
representations, Lie generators and auxiliary representation remain shared,
as do the numerical bounds and matrix primitives. The
[physical interface map](../../metadata/physical-interface-map.json) records
these objects and the [audit extension bridge](../../metadata/statement-audit/physical-interface-bridge.json)
separates this addition from the historical statement audit. It is not a new
human correspondence review.

[`check_physical_spec.lean`](../../scripts/check_physical_spec.lean) follows the
compiled expected theorem types and their transitive declaration dependencies,
rejecting references to the canonical orbit-state, source-state or Choi-projector
constructions and final proof modules. It excludes the deliberate root proof
holes, and checks their two types. Its negative controls are in
[`test_physical_spec.py`](../../scripts/test_physical_spec.py). The `all` and
`comparator` reproducer modes run this guard and its controls; the
[closure report](../../metadata/verification/2026-10-08/physical-spec.json) lists
the remaining shared dependencies. This check establishes a dependency boundary,
not semantic agreement with the manuscript.

See [the website explanation](https://jwang226.github.io/Quantum-Minimum-Description-Length/audit/comparator-scope/)
for the source snapshot and recorded probe scope.

## Exact tooling and scope

Lean is pinned to `v4.29.0-rc6`. The project pins
[Comparator's matching tag](https://github.com/leanprover/comparator/tree/v4.29.0-rc6)
at commit `a4f696825c583ed8a5b4060d9a0faa5b882d365b`, with its locked
Lean4Checker and lean4export dependencies. The matching version accepts exactly
`challenge_module`, `solution_module`, `theorem_names`, `permitted_axioms`, and
`enable_nanoda`. It has no `permittedConstants` field or declaration-renaming map:
the same qualified declaration name is looked up in both environments. Definitions
referenced by the expected type are compared recursively, not silently allowlisted.
The separate trust-boundary inventory is documentation, not an extra Comparator
configuration field.

Only `propext`, `Quot.sound`, and `Classical.choice` are permitted solution axioms.
The committed configurations set `enable_nanoda` to false for the baseline Lean
kernel replay. The explicit Nanoda modes below add an independent Rust checker.
The challenge holes do not permit `sorryAx` in the solution.

## Sandboxed reproduction on Linux

Run as an unprivileged user on Linux with full Landlock ABI 9 support (Linux 7.1
or newer) and real `landrun` on `PATH`; the script refuses macOS and root. Its
strict preflight deliberately omits `--best-effort` and fails before Comparator
if any capability requested by the pinned Landrun is unsupported. From `lean/`:

```bash
./check_comparator.sh
# Or one case:
./check_comparator.sh ComparatorChallenges/Theorem2Choi.json
# Also invoke real Nanoda inside the upstream sandbox:
./check_comparator.sh --nanoda
```

The script builds the pinned Comparator and lean4export, exposes the real exporter
on `PATH`, and calls the unmodified upstream `lake exe comparator` for each JSON.
It contains no sandbox bypass or fake Landrun implementation.
The `--nanoda` option requires `nanoda_bin` on `PATH` and generates temporary
copies of the JSON configurations with `enable_nanoda: true`; it does not edit
the committed configurations or alter the pinned upstream Comparator.

For a pinned Landrun source build (Go 1.24 or newer), outside this repository:

```bash
git clone https://github.com/Zouuup/landrun.git
cd landrun
git checkout 811cfff51ceaf3d9843708aa6d22e9b84ccac8b4
go build -o landrun cmd/landrun/main.go
export PATH="$PWD:$PATH"
```

Consult [Landrun's requirements](https://github.com/Zouuup/landrun/tree/811cfff51ceaf3d9843708aa6d22e9b84ccac8b4)
and [Comparator's current sandbox guidance](https://github.com/leanprover/comparator#usage).
The pinned historical Comparator uses Landrun's `--best-effort` flag; the preceding
strict probe verifies full support for the pinned Landrun feature set. Current upstream
guidance additionally restricts AF_UNIX when running untrusted solutions, for
example through an appropriate `systemd-run` unit. A build on a machine with no
working sandbox is not a sandboxed verification result. The optional Comparator CI
job is manually enabled on a capable runner; ordinary hosted Ubuntu support is not
assumed. Its configuration has not been executed on the development Mac.

## Local diagnostic on macOS or Linux

```bash
python3 ComparatorConfig/check_local.py
```

This separately named, **unsandboxed** diagnostic exports both environments, calls
the pinned Comparator's exact statement/constant comparison and axiom checker, and
replays the solution export with Lean4Checker in Lean's kernel. It never invokes
Landrun or Nanoda. Use it only for trusted local sources; it is not a substitute for
the sandboxed run above.

## Independent Nanoda replay on macOS or Linux

The pin in `ComparatorConfig/nanoda-toolchain.json` selects upstream
[Nanoda 0.4.19](https://github.com/ammkrn/nanoda_lib/tree/3a2407216ee84a75f9e1aead6803d0578be06ae7)
at commit `3a2407216ee84a75f9e1aead6803d0578be06ae7`, built with Rust 1.90.0 and its
committed Cargo lockfile. This is the upstream repository linked by the pinned
Comparator. With Git, Rustup, Python 3, the project Lean toolchain and a native
linker available, the following commands work from the repository root. On macOS
the linker is provided by Xcode Command Line Tools; on Linux use the platform's
C/C++ build toolchain.

```bash
nanoda_tools=$(mktemp -d)
git clone https://github.com/ammkrn/nanoda_lib.git "$nanoda_tools/nanoda"
git -C "$nanoda_tools/nanoda" checkout --detach 3a2407216ee84a75f9e1aead6803d0578be06ae7
rustup toolchain install 1.90.0 --profile minimal
CARGO_TARGET_DIR="$nanoda_tools/nanoda/target" \
  cargo +1.90.0 build --release --locked --manifest-path "$nanoda_tools/nanoda/Cargo.toml"
python3 lean/ComparatorConfig/check_nanoda.py \
  --nanoda-bin "$nanoda_tools/nanoda/target/release/nanoda_bin"
```

On current `main`, this checks all four configurations using actual solution exports, including the
Nat, String and quotient roots requested by the pinned Comparator's Nanoda mode.
Only the three standard axioms are allowed; an unpermitted axiom causes a hard
error. The wrapper verifies that every requested target occurs as a theorem in
the export, and Nanoda separately requires those declarations to exist. This
guards against the pinned exporter's missing-target panic returning exit code
zero with an incomplete export. The checker is **unsandboxed** and performs independent kernel replay only;
run the local Comparator diagnostic as well for expected-statement comparison.
It makes no tracked changes unless `--report PATH` is supplied. To expose the same
binary to the Linux `--nanoda` mode, add its `target/release` directory to `PATH`.
The wrapper disables optional pretty printing; target-presence validation is
performed by Nanoda's parser independently of printing.

## Recorded status

All four current configurations and six roots **passed** the October 8 local
diagnostic, including the universal physical bound and realization existence:
exact exported statements and referenced constants matched,
the solution axiom closures were accepted, and Lean kernel replay succeeded.
`verification-status.json` binds each recorded result to source and artifact
hashes. These are fresh exports from a source-matching local build with warm
dependency artifacts, not a new clean-checkout run. The October 8 extension is distinguished by the physical configuration
and its two roots; earlier three-configuration reports do not verify that addition.

The physical specification dependency guard and all seven acceptance/rejection
controls passed in the October 8 local run. This establishes the documented
dependency boundary and exercises its rejection paths; it does not establish
human correspondence review or replace the four-configuration proof checks.

All four current Nanoda cases and six roots **passed**, using fresh exports and
rerun acceptance/rejection controls. The physical-interface export checked
58,990 declarations with no errors. The reused checker binary's SHA-256 matches
the archived pinned source build; this invocation did not rebuild Rust. The
complete local wrapper exited zero with `VERIFICATION PASSED: all`. Current
source/export bindings are recorded in `ComparatorConfig/nanoda-status.json`
and the [execution record](../../metadata/verification/2026-10-08/verification-result.json).

The [historical three-configuration execution record](../../metadata/verification/2026-10-08/historical/nanoda-status.json)
retains its original hashes and scope; frozen rc1 is unchanged. The real
sandboxed Comparator run is **not run** on the development Mac: Landrun requires
a capable Linux host. These local checks are unsandboxed and do not establish
a new hosted CI result.
