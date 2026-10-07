<!-- Copyright (c) 2026 Free Entropy formalization contributors.
See LICENSE and NOTICE for license and attribution. -->

# Elaboration cleanup and measurements

The cleanup follows the requested order: dead-code sweep, full production
baseline, measured elaboration cleanup, and a second full production build.
Both complete project-only builds and the serial GT experiment passed.
The full build ran 4.15% shorter, but measured total CPU rose 5.83% and
unchanged files shifted in opposite directions. **A whole-project causal
speedup is not established.**

Fresh Lean auditing, statement applications, qualified compiled preservation,
and all three Nanoda cases passed. Raw compiled expressions differ in 15
retained declarations; preservation holds after two exact instance substitutions
whose definitional equalities were checked by Lean's kernel. Fresh Comparator
passed all three statement/constant comparisons, axiom checks and kernel replays.

[Detailed before report](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/ELABORATION_REPORT_2026-10-06_BEFORE.md) ·
[Detailed after report](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/ELABORATION_REPORT_2026-10-06_AFTER.md) ·
[Raw evidence](https://github.com/JWang226/Quantum-Minimum-Description-Length/tree/main/metadata/elaboration/2026-10-06)

The raw archive contains both full logs, source/size records, serial profiles
and the six-sample GT experiment, with source/output hashes.

## What was measured

Both full snapshots use Lean 4.29.0-rc6, the pinned dependency lockfile,
GNU time `-v`, `LEAN_NUM_THREADS=4`, and the explicit `All` target. The runner
invalidates only this repository's proof artifacts and retains dependency
oleans. Its source/dependency guards and full-module log check distinguish a
valid project snapshot from a successful cached or partial process.

The baseline compiled all 270 proof modules plus four entry/facade files:
274 measured files, 35,927 lines, and 28,021 non-comment code lines. The full
committed tree contained 285 Lean files; Comparator specifications, probes
and exporter scripts account for the difference. Legacy module syntax is
retained and recorded as an exception to the skill's `module`-header convention.

| Measurement | Baseline | After cleanup | Observed change |
| --- | ---: | ---: | --- |
| Full build wall time | 39 min 22.93 s | 37 min 44.92 s | −4.15% |
| Full build user CPU | 1,249.26 s | 1,362.32 s | +9.05% |
| Full build system CPU | 1,534.45 s | 1,583.66 s | +3.21% |
| Full build total CPU | 2,783.71 s | 2,945.98 s | +5.83% |
| Maximum RSS, process/child maximum | 3.09 GiB | 2.74 GiB | −11.20% |
| Own modules compiled | 274 | 274 | Same full scope |
| Errors / unauthorized sorry diagnostics | 0 / 0 | 0 / 0 | Both clean |
| Warning count | 131 | 131 | Unchanged |

Both builds retained unchanged dependency artifacts and stable source snapshots;
no upstream compilation occurred. Timing data is complete for all 274 modules.
Of those modules, 137 took over 15% longer and 103 over 15% less time. The
≥10/20/30-second tiers grew; the ≥40-second tier shrank. These mixed results,
shared load, and host memory pressure rule out a broad performance claim from
this single pair of builds. Logged elapsed sums are not CPU measurements.

## Retained import change

`FreeEntropy.GTDeterminant` now imports `Mathlib.Tactic.Linarith` and
`Mathlib.Tactic.Positivity` in place of the tactic umbrella. Source proof bodies and
statement text are unchanged. Three serial warm profiles in each variant passed
with stable source hashes.

| GT median, three samples per variant | Before | After | Observed reduction |
| --- | ---: | ---: | ---: |
| Command wall time | 39.11 s | 11.24 s | 71.3% |
| Total process CPU | 12.45 s | 6.11 s | 50.9% |
| Import elapsed phase | 32.70 s | 6.64 s | 79.7% |

Static import analysis predicts a Mathlib closure of 2,982→1,426 files and
43 downstream consumers. The complete second build passed every production
consumer;
the static analysis itself is not an elaboration proof.

These are observations on a shared machine. The before and after profile
batches were sequential, with uncontrolled OS cache warmth and concurrent
load. Their medians do not establish an exact causal speedup. Profiler phases
measure elapsed work and can overlap; the sum of logged build durations is
also an elapsed proxy, **not cumulative CPU**. The baseline's high system CPU
and page-fault counters limit wall-time interpretation.

## Hotspot profiles and scope of the gain

Five baseline hotspots and the nine-module union of original/new top-five files
were profiled serially. All commands passed with stable source hashes. None of
those nine files is a consumer of the changed GT header; their import closures
are unchanged, so their observed timing shifts are controls for machine/cache
state and are excluded from the GT improvement claim.

| Original hotspot, one sample per batch | Before wall | After wall | Before import | After import |
| --- | ---: | ---: | ---: | ---: |
| `FreeEntropy.TensorWeightBasis` | 66.90s | 62.76s | 32.20s | 20.90s |
| `FreeEntropy.WeylTranslation` | 25.68s | 22.78s | 18.60s | 15.40s |
| `FreeEntropy.WeylCoefficient` | 19.57s | 12.96s | 13.00s | 7.88s |
| `FreeEntropy.LieDeterminantTwist` | 35.49s | 18.35s | 23.20s | 11.70s |
| `FreeEntropy.LiePBWDimension` | 48.76s | 16.63s | 41.40s | 9.95s |

`TensorWeightBasis` still has substantial `refine` cost (20.3s tactic phase),
and `UnitaryDecompositionBasic` has diffuse typeclass cost (5.83s). The other
new candidates are import-heavy. These profiles support focused future
attribution; they did not justify additional proof-body rewrites, caches or
threshold increases. Detailed phase/event tables are in the reports.

## Reproduce the two source variants

Use Git, Python 3.11+, elan, native compiler tools, and GNU time (`gtime` on
macOS or `/usr/bin/time -v` on Linux). The instrumented before checkpoint
`07d563cc77ef4ac8a439911f827162d277da4432` contains the helper scripts and has
identical production Lean sources and pins to the original measured baseline
`4c496959aa1462a6b6a6faf5535ea2a3caf9c119`. The after source is
`4c2054c47d6c81615f5687fe5ac3f1c4dd1ea1d9`.

Run from a fresh clone with new output directories:

```sh
git clone https://github.com/JWang226/Quantum-Minimum-Description-Length.git
cd Quantum-Minimum-Description-Length
export PATH="$HOME/.elan/bin:$PATH"

git switch --detach 07d563cc77ef4ac8a439911f827162d277da4432
cd lean
lake exe cache get
cd ..
python3 scripts/test_elaboration_tools.py
python3 scripts/benchmark_elaboration.py \
  --threads 4 --output .verify-work/elaboration-reproduction/before
python3 scripts/summarize_elaboration.py \
  .verify-work/elaboration-reproduction/before
python3 scripts/profile_elaboration.py \
  --threads 4 --repeat 3 --modules FreeEntropy.GTDeterminant \
  --output .verify-work/elaboration-reproduction/gt-before

git switch --detach 4c2054c47d6c81615f5687fe5ac3f1c4dd1ea1d9
python3 scripts/test_elaboration_tools.py
python3 scripts/profile_elaboration.py \
  --threads 4 --repeat 3 --modules FreeEntropy.GTDeterminant \
  --output .verify-work/elaboration-reproduction/gt-after
python3 scripts/benchmark_elaboration.py \
  --threads 4 --output .verify-work/elaboration-reproduction/after
python3 scripts/summarize_elaboration.py \
  .verify-work/elaboration-reproduction/after \
  --compare .verify-work/elaboration-reproduction/before/summary.json
```

The profile commands run serially and request no olean/ilean/IR output. To
profile the five full-build hotspots, use `--summary RUN/summary.json --top 5`
instead of `--modules`, with a fresh `--output` directory. These measurements
can be expensive; the recorded baseline took about 39 minutes on this shared
host. Do not run `lake clean` or `lake update`; dependency compilation makes
a project-only benchmark invalid.

Proof verification is a separate check:

```sh
bash scripts/verify.sh lean
```

The [verification guide](verify.md) also documents Comparator and Nanoda.
Performance results are not substitutes for those proof checks or the
[statement audit](audit.md).

## Reproduce the compiled preservation comparison

The cleanup comparison exports actual compiled expression trees. It compares
every project declaration type and every available non-proposition definition
value, including all public audit seeds. Proof values and kernel-irrelevant
metadata are omitted. This is structural comparison evidence; the Lean,
Comparator and Nanoda checks separately verify proofs.

From the fresh clone used above, return to the published `main` and save the
comparison helpers before switching source revisions. Use a new reproduction
directory; the witness runner refuses to overwrite an existing output:

```sh
git switch main
mkdir -p .verify-work
mkdir .verify-work/cleanup-reproduction
cp scripts/export_cleanup_fingerprints.lean \
  scripts/compare_cleanup_fingerprints.py \
  scripts/check_cleanup_instance_pairs.lean \
  scripts/run_cleanup_instance_witnesses.py \
  .verify-work/cleanup-reproduction/
cp metadata/elaboration/2026-10-06/instance-pairs.json \
  .verify-work/cleanup-reproduction/

git switch --detach 9c97dbf8cb5d7913fcc7b33d812f94cb1f1738bf
cd lean
lake exe cache get
lake build All
cd ..
python3 .verify-work/cleanup-reproduction/compare_cleanup_fingerprints.py \
  --seeds-from lean/Audit.lean \
  --seed-output .verify-work/cleanup-reproduction/before-seeds.json
cd lean
lake env lean --run ../.verify-work/cleanup-reproduction/export_cleanup_fingerprints.lean \
  ../.verify-work/cleanup-reproduction/before-seeds.json \
  ../.verify-work/cleanup-reproduction/before.json
cd ..

git switch --detach 4c2054c47d6c81615f5687fe5ac3f1c4dd1ea1d9
cd lean
lake build All
cd ..
python3 .verify-work/cleanup-reproduction/compare_cleanup_fingerprints.py \
  --seeds-from lean/Audit.lean \
  --seed-output .verify-work/cleanup-reproduction/after-seeds.json
cd lean
lake env lean --run ../.verify-work/cleanup-reproduction/export_cleanup_fingerprints.lean \
  ../.verify-work/cleanup-reproduction/after-seeds.json \
  ../.verify-work/cleanup-reproduction/after.json
cd ..
python3 .verify-work/cleanup-reproduction/run_cleanup_instance_witnesses.py \
  --before .verify-work/cleanup-reproduction/before.json \
  --after .verify-work/cleanup-reproduction/after.json \
  --strict-report .verify-work/cleanup-reproduction/strict.json \
  --pairs .verify-work/cleanup-reproduction/instance-pairs.json \
  --helper .verify-work/cleanup-reproduction/check_cleanup_instance_pairs.lean \
  --evidence-root . --lean-project lean \
  --output-directory .verify-work/cleanup-reproduction/witnesses
python3 .verify-work/cleanup-reproduction/compare_cleanup_fingerprints.py \
  .verify-work/cleanup-reproduction/before.json \
  .verify-work/cleanup-reproduction/after.json \
  --allow-removed-aux \
  _private.FreeEntropy.ExteriorMultiplicity.0.FreeEntropy.ExteriorRepresentation.complex_weight_eq_iff \
  --strict-report .verify-work/cleanup-reproduction/strict.json \
  --reviewed-instance-pairs .verify-work/cleanup-reproduction/witnesses/instance-pairs.json \
  --instance-witnesses .verify-work/cleanup-reproduction/witnesses/instance-witnesses.json \
  --evidence-root . \
  --report .verify-work/cleanup-reproduction/reviewed.json
```

The runner first writes a fresh raw comparison with status `review_required`:
15 retained declarations differ syntactically, including three public signatures
and four data values. It then finds the two exact registered foundation instance
trees in these new snapshots and checks their equality with literal `Eq.refl`
certificates in Lean's kernel. The separate reviewed comparison should report
`passed`, with zero remaining type or data-value changes. All four final theorem
types already match in the raw comparison.

The single removal exception names the reviewed unused private proof. Reviewed
mode permits only the exact `IntPartialOrder` and `RealCharZero` instance pairs;
any other retained change fails. It does not erase typeclasses or apply generic
normalization. The raw report is preserved separately. The saved helper files
keep their original names because the witness runner imports the adjacent
comparer. They are verification tools, separate from the timed proof-source
revisions. This fresh scratch workflow was actually exercised and passed; see
the [runner validation record](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/elaboration/2026-10-06/instance-runner-validation.json).

The fresh final-source Lean audit passed all 2,499 public declarations with
no placeholders or project-added axioms; its permitted axioms are `propext`,
`Classical.choice`, and `Quot.sound`. Actual statement applications and binder
export passed, as did catalog and correspondence checks. These checks ran
outside the two timed snapshots.

The [raw strict comparison](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/elaboration/2026-10-06/cleanup-comparison.json)
retains status `review_required` and 15 syntactic changes, including three
public signatures and four data values. The four final theorem names,
universes and raw types already match. The
[qualified comparison](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/elaboration/2026-10-06/cleanup-reviewed-comparison.json)
passed with zero residual changes across 4,526 retained declarations, 2,499
public types and 863 data values after only the exact `IntPartialOrder` and
`RealCharZero` ground substitutions. The
[literal `Eq.refl` witnesses](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/elaboration/2026-10-06/instance-witnesses.json)
passed the kernel, and the false `Nat.zero = Nat.succ Nat.zero` control was
rejected. The freshly exercised scratch reproducer and its 15 Python controls
also passed. The preservation result is qualified by those two kernel-checked
definitional equalities; it does not assert raw AST identity.

Fresh Nanoda replay passed after rebuilding its pinned source with Rust 1.90.0:
59,959, 62,881 and 58,851 declarations checked in the achievability, converse
and Choi-cloning dependency closures, respectively. These counts overlap.
All seven acceptance/rejection control groups passed. The
[fresh verification records](https://github.com/JWang226/Quantum-Minimum-Description-Length/tree/main/metadata/elaboration/2026-10-06/verification)
bind the cleanup source and actual runs. Fresh Comparator passed all three
statement/constant comparisons, axiom checks and Lean kernel replays; its wrapper
exited 0. These checks were unsandboxed. No Linux-sandboxed execution, new
source-first manuscript review or human review is claimed.
