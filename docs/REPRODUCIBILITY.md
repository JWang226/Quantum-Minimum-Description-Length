# Reproducing the Lean verification

The proof project stays in `lean/`; the manuscript sources, PDFs, bibliography
and TeX support files are in `manuscript/`. Verification does not compile or modify the manuscript.

For the simplest fresh-checkout workflow, start with
[the verification guide](verify.md): `bash scripts/verify.sh all` runs the
Lean audit, physical specification guard and controls, local Comparator
diagnostic and independent Nanoda checks, with
fresh logs and a nonzero exit status on failure. The commands below document
the individual tools and evidence packaging.

Current `main` checks four configurations and six theorem roots, including the
physical bound and realization-existence theorem. The frozen `v0.1.0-rc1`
release retains three configurations and four roots; checking that tag does
not check the October 8 physical-interface extension. Current execution
evidence is recorded in
[`verification-result.json`](../metadata/verification/2026-10-08/verification-result.json).

## Pinned environment

The checked toolchain is **Lean 4.29.0-rc6**, recorded in
[`lean-toolchain`](../lean/lean-toolchain). Mathlib is pinned to
`f156f7abd91ac67adb22bf999e5a71ba22e22e41`. The full dependency revisions are
recorded in [`lake-manifest.json`](../lean/lake-manifest.json); keep this file
when copying the project. Do not run `lake update` as part of reproduction.

Install [elan](https://github.com/leanprover/elan), Python 3.11 or newer, Git,
and native compiler/linker tools (Xcode Command Line Tools on macOS). The
toolchain is selected automatically from `lean/lean-toolchain`. Internet
access is needed for the initial toolchain, public Git dependencies, and
mathlib's public compiled cache. Project proof artifacts are rebuilt locally.

Clone the public repository first:

```sh
git clone https://github.com/JWang226/Quantum-Minimum-Description-Length.git
cd Quantum-Minimum-Description-Length
export PATH="$HOME/.elan/bin:$PATH"
```

Then, from the repository root (or an unpacked source archive):

```sh
python3 -m venv .venv-release
. .venv-release/bin/activate
python3 -m pip install -r scripts/requirements-release.txt
python3 scripts/validate_artifacts.py --allow-stale-audit
cd lean
lake --version
lake exe cache get
bash check.sh
cd ..
python3 scripts/validate_artifacts.py
```

`check.sh` generates the declaration audit, builds `All` (including
`FreeEntropy` and the reader entrypoints), asks Lean
for the actual kernel dependencies of the audited declarations, and checks
the output. Success allows only `propext`, `Classical.choice`, and
`Quot.sound`; proof placeholders and custom axioms fail the core audit.
The report is written to `lean/verification/summary.json`. Raw build and
axiom logs are written beside it. These are generated evidence, not proof
inputs.

The separate comparator challenge templates deliberately contain expected
proof holes. They are not imported by `FreeEntropy` and are not counted as
proved declarations in the core audit. Comparator checking is a separate
check with its own tool and sandbox requirements; see the
[challenge documentation](../lean/ComparatorChallenges/README.md).
A successful core audit does not by itself
claim a successful comparator run.

## Statement comparison and independent kernel

From the repository root after the Lean build, run:

```sh
python3 lean/ComparatorConfig/check_local.py
```

This invokes the pinned Comparator's exact statement/constant and axiom checks,
then Lean kernel replay, for each of the four current challenge configurations.
For the separately implemented Nanoda kernel, follow the pinned Rust/source
build commands in the [challenge guide](../lean/ComparatorChallenges/README.md#independent-nanoda-replay-on-macos-or-linux),
then run `lean/ComparatorConfig/check_nanoda.py` with the resulting binary.
Both commands work on macOS and Linux and are explicitly unsandboxed.
Nanoda checks each exported solution's dependency closure with unpermitted
axioms treated as errors; it does not perform statement comparison itself.
The wrapper requires every requested root to be an exported theorem, and Nanoda
independently rejects missing roots. Exporter success alone is insufficient:
the pinned exporter can return zero after a missing-target panic.

The [Nanoda toolchain record](../lean/ComparatorConfig/nanoda-toolchain.json)
pins the checker source, Rust version and Cargo lockfile. Its
[execution record](../lean/ComparatorConfig/nanoda-status.json) binds the
actual checked exports, configuration and source bytes. Re-run locally to
check your checkout; a bundled report is historical evidence. Use
`--report /tmp/qmdl-nanoda-result.json` to retain a new portable report.
The optional report is written only after every requested case succeeds.
Use a fresh report path: a failed rerun does not overwrite an older report.

To test the checking pipeline itself with the same real exporter and kernel:

```sh
python3 scripts/test_nanoda_check.py --lake-project lean \
  --nanoda-bin /path/to/nanoda_bin
```

This accepts a valid theorem and requires rejection of missing targets,
non-theorem roots, forbidden axioms, proof holes, and an ill-typed proof.
Fixtures live only in a temporary directory, outside the proved library.

The current `all` and `comparator` wrapper modes also run the compiled physical
specification dependency guard and seven acceptance/rejection controls before
Comparator. For their separate commands and report scope, see
[the verification guide](verify.md#physical-specification-check). The
[physical interface map](../metadata/physical-interface-map.json) and
[audit extension bridge](../metadata/statement-audit/physical-interface-bridge.json)
record the independent raw state/Choi formulas and the remaining shared
representation coordinates. This guard checks a dependency boundary; it does
not establish independent human correspondence review.

## Source-only export

Do not zip the working manuscript directory: it can contain correspondence,
notes, older drafts, TeX build products, and local package symlinks.
[`prepare_release.py`](../scripts/prepare_release.py) uses an explicit
allowlist and rejects selected symlinks. It never copies `.lake/`, `.git/`,
private correspondence, working notes, or unrelated draft documents.

After a successful current audit and completion of the publication metadata:

```sh
python3 scripts/prepare_release.py --list
python3 scripts/prepare_release.py --output /tmp/free-entropy-source.tar.gz
```

The archive contains the current `article.tex` and `letter.tex`, their shared
`free.bib`, the Letter's `compression.pdf`, and required local class/style files,
proof and verification scripts, pinned configuration,
named publication metadata, the workflow, and a current portable audit
summary. `RELEASE_MANIFEST.json` records a SHA-256 digest for every selected
file and records every locked dependency. The named historical elaboration
evidence retains tool-reported local paths in benchmark and checker logs.
These paths describe earlier executions and are not reproducer prerequisites.
Private correspondence, credentials, caches and machine-specific build products
are excluded; CI uploads newly generated logs separately.
The exporter generates this manifest afresh inside each archive; no tracked
repository-root manifest represents the current mutable checkout.

The exporter checks that the audit's proof fingerprint matches the selected
proof source bytes. A stale summary makes the default export fail. It also
checks the Lean/mathlib pins and the exact SHA-256 of both supplied manuscripts:

```text
manuscript/article.tex  b16105860b6db50b877e1bc4ea74dc04e8d55d74e9511e77e68b0b6921933da7
manuscript/letter.tex   0b6a2c45b1565c3e9aadcdaa1c6631a2d7e2e2ec259b7382d04bcbce83622260
```

`--include-manuscript-pdf` adds the existing `article.pdf` without
regenerating it. The default package omits that PDF. The original
`quantumarticle.cls` and `utphys.bst` are included unchanged under their own
notices; the formalization's license does not override those notices.

The exporter checks file selection and verification fingerprints, not the
sufficiency of copyright permissions. The maintainer confirmed the software
Apache-2.0 grant, including the Cloning adaptations, on 2026-10-06; manuscripts
and third-party assets retain their rights and notices. The publication record
and outstanding review decisions
are in [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md).

For a clean build before fresh verification exists, use a preparation copy:

```sh
python3 scripts/prepare_release.py --allow-unverified \
  --directory /tmp/free-entropy-source
cd /tmp/free-entropy-source/lean
lake exe cache get
bash check.sh
cd ..
python3 -m venv .venv-release
. .venv-release/bin/activate
python3 -m pip install -r scripts/requirements-release.txt
python3 scripts/validate_artifacts.py
python3 scripts/prepare_release.py --output /tmp/free-entropy-verified.tar.gz
```

The destination must not already exist. `--allow-unverified` deliberately
omits the old audit summary and marks the manifest accordingly.
If an optional legacy record at `lean/verification/reproducibility.json` is
present, the exporter includes it only when its proof fingerprint, manuscript
hash, toolchain and dependency pins match the selected sources. A stale legacy
record is omitted in preparation mode and rejected in a verified export.
Current `main` instead archives that record under a dated historical path and
records the physical extension separately. Bundling an execution report is
not a new execution or clean-build result. Perform fresh clean-source checks
before releasing changed proof sources; the current incremental run does not
replace that evidence.
`--allow-incomplete-metadata` is also available for preparation only; it
lists missing publication files and must not be mistaken for a completed
release. Neither option publishes anything or initializes Git.

Archive ordering, permissions, ownership, and gzip/tar timestamps are
normalized. Identical selected bytes produce identical archive bytes with
the same Python/zlib implementation and `SOURCE_DATE_EPOCH` (default zero).

## Continuous integration

[`lean.yml`](../.github/workflows/lean.yml) checks an exported source copy on
Ubuntu 24.04, installs a versioned, checksum-verified elan bootstrap, fetches
the locked public dependencies, and runs the actual build and axiom audit.
It also compiles the separate expected-statement templates and runs the
physical specification guard and its controls; deliberate challenge proof
holes are not imported into the production library. The same job then
runs the local Comparator/Lean replay diagnostic, builds the pinned Nanoda
with Rust 1.90.0 and `cargo --locked`, and checks all four current solution exports.
These two checker steps are explicitly unsandboxed. The old copied Nanoda
report is removed before checking, so the uploaded success report must be
produced by that job's actual run. It creates a release archive only after
the checks succeed. GitHub actions
are pinned by commit. The workflow uploads reports and the source archive
as CI artifacts; it does not create a public release.
The updated physical-interface CI configuration is not evidence of a completed
hosted run; the completed rc1 run checks the earlier frozen sources.

A separate, manually enabled dependent CI job downloads that source archive
and invokes the unmodified pinned upstream Comparator on Linux with real Landrun. Landrun
is built from commit `811cfff51ceaf3d9843708aa6d22e9b84ccac8b4`; the
Comparator, Lean4Checker and lean4export revisions are locked in the Lean
manifest. Enable `run_comparator` through `workflow_dispatch` and select a
capable x86_64 Linux runner using `comparator_runner` (the CI bootstrap is
pinned for that architecture). The strict preflight requires
all features of the pinned Landrun (Landlock ABI 9 or newer); a default
Ubuntu 24.04 runner may not provide them and will fail rather than silently
weaken the check. The job launches the checker as the runner's non-root
UID/GID in a systemd service that also denies AF_UNIX sockets and new
privileges. Its log and job status are separate from the kernel audit. The
historical Comparator's sandbox limitations are documented in the challenge
README. This hosted-runner setup has not been executed locally, and an
unselected or unsupported job is not a completed Comparator run.

This packaging follows the reproducibility and statement-recording goals
of [AGMAI](https://agmai.org/general-sep29/) and the repository organization
illustrated by [OpenAI's ten-proofs](https://github.com/openai/ten-proofs).
See [`FORMALIZATION_STATUS.md`](FORMALIZATION_STATUS.md) for the statement
mapping and [`AI_PROVENANCE.md`](AI_PROVENANCE.md) for provenance. Workflow
configuration is not evidence that a hosted CI run has already occurred.

## Building the manuscript sources

The two supplied TeX sources are preserved byte-for-byte. A standard TeX
distribution needs `quantumarticle.cls` and `utphys.bst` (bundled) for the
Article and `revtex4-2` for the Letter. Both use the bundled `free.bib`; the
Letter also needs `compression.pdf`. From `manuscript/`, compile each
source with LaTeX, BibTeX, then two further LaTeX passes. Manuscript compilation
is separate from checking the Lean proofs. The
[companion source map](../metadata/letter-source-map.json) binds these inputs
by hash and distinguishes the Letter's geometric claims from the checked
Article statements.

## Completed clean source reproduction

The local clean reproduction completed on **2026-10-01 UTC** (2026-09-30
Pacific time) on macOS arm64. All 270 proof modules were compiled in an
exported source copy with no existing project proof artifacts and no package
directory symlinks. All twelve dependencies were real public Git checkouts
at the locked revisions; the official public mathlib cache was used.

The build and actual kernel audit passed for 1,873 proved declarations and
2,499 public declarations, with only the three permitted standard axioms.
`lake build All` and all eight artifact-validation checks also passed.
The byte-preserved historical
[`reproducibility.json`](../metadata/elaboration/2026-10-06/historical/lean-reproducibility.json) records
the actual platform, dependency pins, commands, source fingerprint, and
outcome without machine-specific paths. For the October 1 archive, its
fingerprint had to match the selected sources before export. The archived
historical copy is now included as labeled earlier evidence, rather than
required to match the cleanup sources. This completed local result
does not assert that hosted CI or the Linux-sandboxed Comparator has run.

## Additional independent check — 2026-10-01

A fresh clone of published commit `dc226a55023a47d1f4868a042d87d39238b7e2dd`
was rebuilt without existing project proof artifacts. Dependency caches were
reused after checking all twelve source revisions against the lockfile. All
270 project modules compiled, and the 2,499-declaration axiom audit and all
three Comparator/Lean replay cases passed.

Nanoda was rebuilt from its pinned source with Rust 1.90.0. The hardened helper
then checked **59,959**, **62,881**, and **58,851** declarations in the achievability,
converse, and Choi-cloning exports, respectively, with no errors. These counts
include shared dependencies and should not be added as distinct declarations.
All seven acceptance/rejection regression groups passed, including missing
targets, forbidden axioms, proof holes and an ill-typed proof term.

The review uncovered and fixed an exporter-related false-pass path: a missing
target could produce an incomplete export with exit code zero. The helper now
requires actual theorem roots, and Nanoda independently requires their presence.
CI runs the regression controls before checking the solution exports.
The theorem sources and manuscript were unchanged.

The historical [Nanoda record](../metadata/elaboration/2026-10-06/historical/nanoda-status.json) and
the October 1 entry in [reproducibility.json](../metadata/elaboration/2026-10-06/historical/lean-reproducibility.json)
bind this run to its source, checker, binary and export hashes. An agent-performed
review found no concrete mismatch between the final statements and the manuscript;
this does not establish independent human review. The checks were local and
unsandboxed; the Linux-sandboxed Comparator status remains separate.

These October 1 records are preserved without changing their bytes, dates,
counts, source fingerprints, or execution contexts. They describe the earlier
sources and are not fresh passes for the October 6 cleanup. The
[historical index](../metadata/elaboration/2026-10-06/historical/index.json)
records their original paths and hashes.

## Cleanup verification — October 6 campaign

The cleanup proof sources are at commit
`4c2054c47d6c81615f5687fe5ac3f1c4dd1ea1d9`, with proof-source SHA-256
`e7068771d301aaac3156ecc7cd0a1a4b3868a894a1d0988ce897420786ba2c3f`.
The bounded source change removes one unused private theorem and narrows
one tactic import; the retained source proof bodies and statement text
are unchanged. The
[source-delta review](../metadata/elaboration/2026-10-06/cleanup-delta-review.json)
records the exact scope and limits of that review. The
[cleanup review bridge](../metadata/elaboration/2026-10-06/cleanup-review-bridge.json)
will bind it to the completed fresh checks and compiled preservation evidence.
The original source-first manuscript review was not rerun, and independent
human review is not established.

The [before/after elaboration reports](elaboration.md) record two successful
project-only cold builds of `All`: all 270 proof modules and four facade/reader
entry modules compiled in each run, with project artifacts invalidated and
warm dependency artifacts retained. All twelve dependency revisions matched
the lockfile and had clean tracked source trees; dependency-directory symlinks
were present, as recorded in the
[dependency source check](../metadata/elaboration/2026-10-06/dependency-source-check.json).
This campaign did not install upstream dependencies into a new clean checkout.
Its measured cold state covers project proof artifacts only, unlike the
October 1 exported-source reproduction above.

A fresh final-source Lean audit passed all 2,499 public declarations with
no placeholders or project-added axioms and only `propext`, `Classical.choice`,
and `Quot.sound` permitted. It ran outside the timed build measurements.
The [campaign statement applications](../metadata/elaboration/2026-10-06/verification/statement-checks.json)
passed, and the actual exported endpoint binder lists agree with the recorded
lists. This was an incremental local run, not a source-first manuscript review.
The [portable verification records](../metadata/elaboration/2026-10-06/verification/)
retain the audit summary, fresh statement checks, binder export and raw probe
outputs separately from the measurements and historical records.
The [raw compiled comparison](../metadata/elaboration/2026-10-06/cleanup-comparison.json)
retains status `review_required`, with 15 retained declaration AST differences,
including three public signatures and four data values. The four final theorem
names, universes and raw compiled types match without substitutions. There are
no added or unexpected removed declarations; 4,527→4,526 reflects the reviewed
unused private theorem's removal.

The [qualified comparison](../metadata/elaboration/2026-10-06/cleanup-reviewed-comparison.json)
passed with zero residual differences across 4,526 retained declarations,
2,499 public types and 863 data values after only two exact ground substitutions
for `IntPartialOrder` and `RealCharZero`. The
[literal `Eq.refl` witnesses](../metadata/elaboration/2026-10-06/instance-witnesses.json)
establish their definitional equality in Lean's kernel using only the permitted
standard axioms. The same helper rejected the false `Nat.zero = Nat.succ Nat.zero`
control with exit status 1. The
[fresh scratch reproducer validation](../metadata/elaboration/2026-10-06/instance-runner-validation.json)
passed, as did its 15 Python guard controls. This is bounded preservation modulo
the two kernel-checked instance equalities, not a raw AST identity result.

Fresh Nanoda replay passed all three cases after rebuilding its pinned source
with Rust 1.90.0. The achievability, converse and Choi-cloning exports checked
59,959, 62,881 and 58,851 declarations, respectively, with no errors; these
overlapping dependency closures must not be added as distinct declarations.
All seven acceptance/rejection regression groups passed. The
[fresh Nanoda result](../metadata/elaboration/2026-10-06/verification/nanoda-result.json)
binds the cleanup source, checker, binary and actual export hashes. These local checks
were unsandboxed. Fresh Comparator passed all three statement/constant
comparisons, axiom checks and Lean kernel replays; its wrapper exited 0.
The [campaign source-bound report](../metadata/verification/2026-10-08/historical/comparator-status.json)
and [complete raw log](../metadata/elaboration/2026-10-06/verification/comparator.log)
record this new execution. This status is separate from a Linux-sandboxed
Comparator run. Successful builds and historical records do not establish a
new checker pass.

The campaign's compiled catalog contained 4,526
declarations: 2,499 public and 2,027 auxiliary, with 1,873 proved declarations
across 270 proof modules. Its generation and consistency check passed.
The correspondence consistency check also passed, retaining all 33 Article
and 9 Letter locators. These are compiled-export and documentation checks;
they do not replace kernel verification or establish a new manuscript review.

## Physical interface extension — October 8

The additive extension preserves the original 270 production modules and adds
three proof modules. The current `All` build and transitive axiom audit passed
for **273 modules**, **1,883 proved declarations** and **2,512 public
declarations**, at proof-source SHA-256
`33379ffb4c7547fdc221fb3696f360465d87aaad2247e12707a7b95e557b5cac`.
This local source-matching incremental run reused existing project and
dependency artifacts. It is not a clean-checkout build or a repeat of the
October 6 elaboration measurements.

The new physical challenge quantifies over arbitrary isometric tensor
embeddings and PRV copies with specified representation equations. The solution
proves both error bounds and existence of all required embeddings. Its expected
state and Choi formulas are independently restated; canonical representation
coordinates, Lie generators and numerical definitions remain shared. The
[compiled dependency closure](../metadata/verification/2026-10-08/physical-spec.json)
makes that remaining sharing inspectable, while
[the extension bridge](../metadata/statement-audit/physical-interface-bridge.json)
records the bounded addition without relabeling the original audit.

The specification guard and all seven acceptance/rejection controls passed in
the local October 8 run. Their scope is the expected type-dependency boundary,
separate from proof checking and source-to-manuscript interpretation.

The current four-configuration pipeline exports six roots. Its
[execution record](../metadata/verification/2026-10-08/verification-result.json)
distinguishes new checks from preserved history. All four Comparator
configurations passed exact statement/constant comparison, solution axiom
checks and Lean kernel replay, including both physical-interface roots.
The current Nanoda controls and all four fresh solution exports also passed,
including all six required theorem roots. The physical-interface export checked
58,990 declarations with no errors; its dependency closure overlaps the other
exports and must not be added to their counts. The invocation used the
previously built pinned binary, whose SHA-256 matches the archived source/pin
build. It is not a new Rust/source rebuild. The full wrapper exited zero with
`VERIFICATION PASSED: all`.
Comparator and Nanoda remain unsandboxed. Independent human review and a
Linux/Landrun verification remain unestablished.
The updated hosted CI configuration had not run when these local results were
recorded.

The old current-path reproduction record is preserved unchanged as
[`historical/lean-reproducibility.json`](../metadata/verification/2026-10-08/historical/lean-reproducibility.json).
The October 1 and October 6 records above retain their original counts, dates,
source fingerprints and build contexts. The frozen candidate and its completed
clean-source CI check cover the earlier library; they do not verify this
extension.
