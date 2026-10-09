# Check the proof yourself

The supplied proof can be checked on macOS or Linux. Run the commands below from
a fresh clone of [JWang226/Quantum-Minimum-Description-Length](https://github.com/JWang226/Quantum-Minimum-Description-Length)
or an unpacked source archive. The wrapper
fetches the locked dependencies, checks the Lean proof, compares its final
statements with the expected statements, and replays the proofs in a separate
Rust kernel. It does not compile or change the manuscripts.

For the separate source-to-statement review, see [[audit|the statement audit]].
Its freshness check is `python3 scripts/check_statement_audit.py`; after Lean
setup, add `--lean` to compile the recorded anonymous applications and check
their axiom reports.

[Comparator's specification boundary](audit/comparator-scope.md) explains which
definitions are shared with the expected statements and how the existing
physical-state identification is checked. Current `main` also checks the
physical Theorem 2 interface described below; the frozen candidate retains its
original interface.

## Prerequisites

Install [elan](https://github.com/leanprover/elan), Python 3.11 or newer, Git,
[Rustup](https://rustup.rs/), and native compiler/linker tools. On macOS the
native tools come from Xcode Command Line Tools; on Linux use a C/C++ build
toolchain. Initial dependency and checker builds require internet access.

Lean is selected by `lean/lean-toolchain`; all Lean dependency revisions are
locked in `lean/lake-manifest.json`. Keep those files and do not run `lake update`.
The wrapper puts the usual elan and Cargo installation directories on `PATH`.
Rustup is needed for the default Nanoda source build, but not for `lean` or
`comparator` mode.

## Run every check

```bash
git clone https://github.com/JWang226/Quantum-Minimum-Description-Length.git
cd Quantum-Minimum-Description-Length
bash scripts/verify.sh
```

### Frozen candidate

Check the frozen [`v0.1.0-rc1`](releases/v0.1.0-rc1.md) release candidate with:

```bash
git clone --branch v0.1.0-rc1 --single-branch https://github.com/JWang226/Quantum-Minimum-Description-Length.git
cd Quantum-Minimum-Description-Length
bash scripts/verify.sh all
```

Or download the release's source asset, compare its SHA-256 with the attached
checksum file, and extract it:

```bash
tar -xzf quantum-minimum-description-length-v0.1.0-rc1.tar.gz
cd free-entropy-formalization
bash scripts/verify.sh all
```

The archive contains the proof-check inputs; these commands do not require a
root `.git` directory. Internet access and the prerequisites above are still
needed for fetching dependencies and building the pinned checkers.

The frozen candidate checks three Comparator configurations and four theorem
roots. Current `main` adds the physical Theorem 2 configuration, for four
configurations and six roots, plus a specification dependency guard and its
negative controls. Checking the frozen tag does not check this later addition.

The default is `all`. Each invocation creates a new `.verify-work/run-*`
directory and prints its location. Logs are streamed to the terminal and saved
there. If any requested stage fails, the command exits nonzero and prints
`VERIFICATION FAILED` with the failing stage. It prints `VERIFICATION PASSED: all`
only after every requested stage succeeds. Argument or prerequisite failures
exit before a run directory is created.

The stages are:

| Stage | What it checks | Saved output |
| --- | --- | --- |
| `lean` | Fetch the public mathlib cache, build `All`, and audit the actual transitive axioms of the proof library. | `lean.log`, `lean-summary.json` |
| `physical-spec` | Check the compiled dependency closure of the two expected physical-interface theorem types. | `physical-spec.log`, `physical-spec.json` |
| `physical-spec-controls` | Check that the specification guard accepts an allowed fixture and rejects forbidden dependencies. | `physical-spec-controls.log`, `physical-spec-controls.json` |
| `comparator` | Compare the four current expected-statement configurations with the solutions, check the solution axioms, and replay their exports in Lean's kernel. | `comparator.log` |
| `nanoda-build` | Build the unmodified pinned Nanoda source with Rust 1.90.0 and `cargo --locked`; verify the source, package, compiler and lockfile pins. | `nanoda-build.log`, `nanoda-source/` |
| `nanoda-controls` | Accept a valid proof and reject missing targets, non-theorem roots, forbidden axioms, proof holes, and an ill-typed proof. | `nanoda-controls.log` |
| `nanoda` | Check all four current solution exports with Nanoda, requiring the named theorem roots and allowing only the three standard axioms. | `nanoda.log`, `nanoda-result.json` |

Both kernel checks allow only `propext`, `Classical.choice`, and `Quot.sound`.
On current `main`, the four configurations cover six declarations: Theorem 1
achievability, its Haar-average and uniform converses, Theorem 2's original
Choi-channel bound, the physical bound for arbitrary qualifying embeddings,
and existence of those embeddings. Deliberate holes in the expected-statement templates are not proofs and
are excluded from the audited production library.

The initial build uses mathlib's public compiled cache and rebuilds the project
proofs. Comparator/Lean and Nanoda subsequently replay the exported final proofs
and their dependencies. A successful run verifies those formal statements; it
does not replace review of their correspondence with the manuscripts. See
[[proof-structure]] and [[formalization]].

### Physical specification check

The additional
[`Theorem2Physical` solution](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/lean/FreeEntropy/Theorem2Physical.lean)
uses independently stated tensor-source normalization and normalized Choi
contractions. Its universal bound applies to arbitrary isometric embeddings
satisfying representation equations; a second checked theorem proves that such
embeddings exist. Canonical representation coordinates and numerical bounds
remain shared. See the
[interface map](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/physical-interface-map.json)
and [audit extension bridge](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/statement-audit/physical-interface-bridge.json).

The `all` and `comparator` modes also run
[`check_physical_spec.lean`](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/scripts/check_physical_spec.lean)
and its
[negative controls](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/scripts/test_physical_spec.py).
The guard starts at the two expected theorem types and follows their compiled
dependencies, including declaration bodies. It rejects dependence on the
canonical state/projector constructions and final proof modules. The deliberate
challenge proof holes are excluded from this traversal. The
[closure report](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/verification/2026-10-08/physical-spec.json)
lists the remaining shared declarations. This boundary check complements
Comparator and kernel replay; it is not an independent human correspondence
review.

To run only the guard and its controls after Lean setup, from the repository
root:

```bash
mkdir -p .verify-work/physical-spec
cd lean
lake build ComparatorChallenges.Theorem2Physical
lake env lean --run ../scripts/check_physical_spec.lean ../.verify-work/physical-spec/boundary.json
cd ..
python3 scripts/test_physical_spec.py --lake-project lean --report .verify-work/physical-spec/controls.json
```

The guard reports `PHYSICAL SPECIFICATION BOUNDARY PASSED` only when the
expected dependency boundary is satisfied. Its report describes theorem types
and referenced definitions; proof validity is checked by the Lean, Comparator
and Nanoda stages above.

## Run one layer

```bash
bash scripts/verify.sh lean
bash scripts/verify.sh comparator
bash scripts/verify.sh nanoda
```

Each command runs only the named layer and its required preparation. The
Comparator and Nanoda helpers build the Lean modules they need; their individual
modes do not perform the complete library-wide axiom audit. They still require
elan, Python, Git, and the pinned Lean dependencies. Run `lean` first to fetch the
public cache and check the entire library.

For a previously built Nanoda binary, use an absolute path:

```bash
bash scripts/verify.sh all --nanoda-bin /absolute/path/to/nanoda_bin
```

This option is valid for `all` and `nanoda`. It skips the Rust/source build and
runs the same controls and proof checks. You are responsible for the binary's
provenance; the wrapper does not infer that it came from the pinned source.
The fresh Nanoda report records its SHA-256. The standard build uses source
commit `3a2407216ee84a75f9e1aead6803d0578be06ae7`, package version 0.4.19, and
the compiler and lockfile recorded in
[nanoda-toolchain.json](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/lean/ComparatorConfig/nanoda-toolchain.json).

## Read the verdict

The Lean log ends with `PASS: <count> declarations; no placeholders or custom
axioms.` Current `main` produces four `LOCAL DIAGNOSTIC PASSED:` lines and four
`NANODA PASSED (UNSANDBOXED):` lines; the frozen candidate produces three of each
and has a recorded count of 2499 audited declarations. The wrapper's final success line means that
all stages selected for that invocation returned success.

Use the newly printed run directory and the command's exit status. Reports
already committed in the repository describe earlier runs; their presence does
not mean your run passed. A failed run never receives a success result from this
wrapper. `run-info.json` records the invocation, and `result.txt` records its
outcome. Preflight failures produce an error instead of those files.

## Separate sandboxed verification

The Comparator and Nanoda steps above are **unsandboxed** and are intended for
trusted local sources. No mode automatically invokes the Linux sandbox.

The separate
[Linux/Landrun procedure](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/lean/ComparatorChallenges/README.md#sandboxed-reproduction-on-linux)
requires an unprivileged Linux account and the full features of the pinned
Landrun. Missing sandbox support is a failure, not a successful verification.
Local macOS checks do not establish a sandboxed Comparator result.

For individual helper commands, evidence history, metadata validation,
source-only archives and CI details, see
[Reproducibility](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/docs/REPRODUCIBILITY.md).

## Measure elaboration

[[elaboration|The elaboration reports]] give the cleanup's before/after source
checkpoints, full-build measurements, serial profiles and reproducer commands.
That workflow preserves dependency caches and measures all production modules.
Use the proof checks above to verify correctness.
