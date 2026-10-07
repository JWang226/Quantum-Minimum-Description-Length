<!-- Copyright (c) 2026 Free Entropy formalization contributors.
See LICENSE and NOTICE for license and attribution. -->

# Elaboration report: 2026-10-06, after cleanup

**Both complete project-only builds passed.** The retained cleanup narrows
one tactic import without changing source proof bodies or statement text. Observed full
build wall time fell 4.15%, while measured total CPU rose 5.83%. Shared-machine
load and opposing shifts across unchanged files prevent a whole-project causal
speedup claim. The six GT samples and nine after-hotspot profiles are complete.
The later Lean audit, statement applications, catalog checks, qualified compiled
preservation comparison, and fresh Nanoda replay passed. The raw compiled AST
comparison records 15 syntactic differences; preservation holds after only two
exact kernel-checked instance substitutions. Fresh Comparator passed all three
statement/constant comparisons, axiom checks and Lean kernel replays.

## 1. Setup and provenance

The reporting and optimization methods use the requested
[lean-elaboration-test skill](https://github.com/scottnarmstrong/LeanAutoformalizationSkills/blob/601fe274276d93052ef645f0ff2c1a355e8e5b16/skills/lean-elaboration-test/SKILL.md)
and [lean-elaboration skill](https://github.com/scottnarmstrong/LeanAutoformalizationSkills/blob/601fe274276d93052ef645f0ff2c1a355e8e5b16/skills/lean-elaboration/SKILL.md),
pinned to commit `601fe274276d93052ef645f0ff2c1a355e8e5b16`.

| Field | Baseline | After cleanup |
| --- | --- | --- |
| Source commit | `4c496959aa1462a6b6a6faf5535ea2a3caf9c119` | `4c2054c47d6c81615f5687fe5ac3f1c4dd1ea1d9` |
| UTC measurement window | 2026-10-06 22:32:09–23:11:35 UTC | 2026-10-06 23:19:59–23:57:48 UTC |
| Host | macOS 27.2, arm64; 8 reported logical CPUs | Same recorded host |
| Lean | 4.29.0-rc6 (`00659f8e…`) | Same exact recorded Lean build |
| Timer | GNU time `-v` | Same GNU time executable and option |
| Build target | `All` | `All` |
| Lean thread setting | `LEAN_NUM_THREADS=4` | `LEAN_NUM_THREADS=4` |
| Runner hash | `363f92aaadef7b4c6151fd4c43a17148f6c213a1ff30d92fb737440687985098` | `12f3d80a94dc1ed05da6cf1a84e6b80d78270f38742e27958114f124f4efd00b` |
| Source snapshot hash | `08fd4c03d6a037c5964d3299ae8e4cdb2d3cc94b89d0f5005f2b5477d3fd3f3b` | `025c85ba4bda4486d17f4d36d8970fe1ab299064781a398e9e4a538b0cfce5b1` |
| Raw build-log hash | `a7149000a5f6fc36bf70cd79d82ac2c836f72c356620635a69f2b48debbd2ceb` | `0b93d8e3ee13e12574d1213452aa18dca3b989b5ddab294c981f7b4ac01e7c68` |

Both snapshots invalidate only project proof artifacts and retain dependency
oleans. The timed Lean command, timer, target, thread setting, host and pins
match. The runner hash differs because guards were strengthened between runs:
all removal paths are now preflighted, dangling/escaping symlinks rejected,
build events anchored, and helper provenance recorded at launch. Those guards
operate outside the timed Lean command. The original baseline runner was
archived at launch and its hash bound after completion.

OS page caches and shared-machine load remain uncontrolled. The baseline had
high system CPU and page-fault counters; its process inventory included another
reference-analysis process. The measured CPU utilization rose from 117.81%
to 130.07%, while the logged
elapsed/wall overlap proxy stayed near 3.9. This does not establish matched
contention or identical effective CPU availability. Host-wide memory snapshots
are available: the baseline samples at 22:48:20
and 23:03:02 UTC report swap usage of `2153.00M` and `2355.44M`; an after
mid-run sample reports `2059.38M`. Their counters are for the whole host,
not solely this build. GNU time reports `Swaps: 0` for its own resource
accounting, which does not establish that the host had no swapping. These
snapshots do not cover the full measurement windows or establish matched
memory pressure.

## 2. Size snapshot

Both snapshots use the requested skill's Git-based lexical line/header counter.
The after counts refer to `4c2054c47d6c81615f5687fe5ac3f1c4dd1ea1d9`;
source counts are separate from the completed build checks reported below.

| Quantity | Baseline | After | Change |
| --- | ---: | ---: | ---: |
| Full committed Lean files | 285 | 286 | +1 |
| Full-tree physical lines | 38,921 | 39,082 | +161 |
| Full-tree non-comment code lines | 30,880 | 31,016 | +136 |
| Production proof modules | 270 | 270 | 0 |
| Facade / reader-entry modules | 4 | 4 | 0 |
| Production measured Lean files | 274 | 274 | 0 |
| Production physical lines | 35,927 | 35,928 | +1 |
| Production non-comment code lines | 28,021 | 28,022 | +1 |
| Comment-only files excluded, full tree / production | 0 / 0 | 0 / 0 | 0 |
| Legacy headers, full tree | 285 | 285 | 0 |
| Legacy headers, production scope | 274 | 274 | 0 |
| Distinct production modules actually built | 274 | 274 | 0 |

Full-tree growth is instrumentation: the new
`scripts/export_cleanup_fingerprints.lean` contributes 160 physical lines and
135 code lines. The sole production growth is one import line, replacing one
umbrella import with two provider imports. The exporter uses the new `module`
header, so the full-tree count of legacy headers stays at 285 despite adding
a file. The production source proof/library bodies and statement text are unchanged.

The comparable timed scope remains the same 270 proof modules plus four
entry/facade files. `All` statically imports that full production scope.
Comparator specifications/configuration, generated axiom probes and exporter
scripts account for the remaining committed Lean files and are outside this
timed build. The completed after log confirms all 274 own `Built` events, without missing,
repeated or upstream compilation events.

Legacy production syntax is retained, with its `module`-header exception
recorded explicitly. No export-semantics migration was attempted.

## 3. Headline before/after table

| Quantity | Before | After | Absolute change | Observed percentage change / scope |
| --- | ---: | ---: | ---: | --- |
| Wall time | 2,362.93s (39:22.93) | 2,264.92s (37:44.92) | −98.01s | −4.15%; single builds, shared load |
| User CPU time | 1,249.26s | 1,362.32s | +113.06s | +9.05% |
| System CPU time | 1,534.45s | 1,583.66s | +49.21s | +3.21% |
| Total measured CPU time | 2,783.71s | 2,945.98s | +162.27s | +5.83% |
| Average CPU utilization | 117.81% | 130.07% | +12.26 percentage points | +10.41% relative |
| Maximum RSS, bytes | 3,318,497,280 | 2,946,777,088 | −371,720,192 | −11.20%; process/child maximum |
| Maximum RSS, GiB | 3.09 | 2.74 | −0.35 | Not summed simultaneous memory |
| Planned Lake jobs | 3,752 | 3,306 | −446 | −11.89%; includes cached dependencies/facets |
| Own build events / distinct modules | 274 / 274 | 274 / 274 | 0 | Matched full production scope |
| Timing-visible modules / fraction | 274 / 100% | 274 / 100% | 0 | No imputed times |
| Logged module elapsed sum | 9,188.80s | 8,690.90s | −497.90s | −5.42%; elapsed proxy, not CPU |
| Logged elapsed sum / wall time | 3.889 | 3.837 | −0.052 | −1.33%; overlap proxy |
| Logged elapsed ms / code line | 327.93 | 310.15 | −17.78 | −5.42%; elapsed proxy |
| Ideal CPU work floor / eight logical cores | 347.96s | 368.25s | +20.28s | Dedicated equal cores assumed |
| Longest weighted own import path | 1,442.50s / 36 modules | 1,235.90s / 41 modules | −206.60s | −14.32%; contention-sensitive weights |

Both artifacts satisfy the project-only validity requirements. That is a scope
and source/cache-stability statement, **not** a controlled timing experiment.
The comparison parser emits one contention signal: substantial opposite shifts
across modules. Its automatic two-signal threshold is not reached, but that
threshold does not certify comparable load.

Of the same 274 modules, 137 grew and 103 shrank by more than 15%. Only the
GT import header changed in production source. For example, `RaisingKernel`
rose 19→57s, `UnitaryDecompositionBasic` 14→57s and `ExteriorWeights` 10→54s,
while `WeylTranslation` fell 123→40s and `LiePBWDimension` 96→25s. These shifts
and the higher measured CPU cost prevent attributing the 4.15% shorter wall
run to a whole-project improvement. No permanent throughput or CPU saving is
established by this pair of snapshots.

The ideal work floors assume equal dedicated logical cores; the observed
import-path weights inherit contention. The internal project import DAG is
identical in both revisions. The longest weighted path switches from a
36-module chain ending at the Theorem 1 route to a 41-module chain ending at
`Theorem2Choi`, `Theorem2` and `All`, because observed weights changed. This is
a scheduling diagnostic, not evidence of a changed proof dependency chain or
an uncontended bottleneck.

## 4. Build health and rule compliance

| Check | Before | After |
| --- | --- | --- |
| Process exit / runner status | 0 / `passed` | 0 / `passed` |
| Complete project rebuild | `true` | `true` |
| Valid measurement record | `true` | `true` |
| Errors / unauthorized sorry diagnostics | 0 / 0 | 0 / 0 |
| Warning count | 131 | 131 |
| Upstream `Built` events | 0 | 0 |
| Missing / repeated own module events | 0 / 0 | 0 / 0 |
| Source snapshot unchanged within run | Yes | Yes |
| Dependency olean count/stat snapshots unchanged | Yes | Yes |
| Files above 1,500 lines | 0 | 0 |
| Heartbeat override occurrences | 121 | 121 |
| Linter suppression lines | 68 | 68 |

The artifact guard compares dependency olean counts, paths, sizes and
modification times, not full cryptographic cached-content hashes. The same
Mathlib cache of 7,805 oleans was retained. Neither `lake clean` nor
`lake update` was used.

| Warning kind | Before | After |
| --- | ---: | ---: |
| Deprecated declaration | 2 | 2 |
| Unnecessary sequence focus | 2 | 2 |
| Unnecessary simpa | 9 | 9 |
| Unreachable tactic | 2 | 2 |
| Unused section variables | 51 | 51 |
| Unused simp argument | 61 | 61 |
| Unused tactic | 3 | 3 |
| Unused variable | 1 | 1 |

The performance intervention did not reduce warnings, raise heartbeat limits,
or suppress additional diagnostics. A fresh final-source Lean audit passed
for all 2,499 public declarations, with no placeholders or project-added
axioms and only `propext`, `Classical.choice`, and `Quot.sound` permitted.
Fresh statement applications also passed, and the exported endpoint binder
lists match the recorded lists. The refreshed compiled catalog contains
4,526 declarations (2,499 public and 2,027 auxiliary) across 270 proof modules.
Catalog and correspondence consistency checks passed with all 33 Article and
9 Letter locators retained. These checks ran outside both timed snapshots.
These runs do not establish a new source-first manuscript or human review.

The [raw compiled comparison](metadata/elaboration/2026-10-06/cleanup-comparison.json)
has status `review_required`: 15 retained declaration ASTs differ syntactically,
including three public signatures and four data values. The import change
selected different foundation instance paths for `IntPartialOrder` and
`RealCharZero` in the `FreeEntropy.GTDimension` namespace in `GTDeterminant.lean`;
source proof bodies and statement text remain
unchanged. The four final theorem names, universes and raw compiled types
already match without substitutions. There are no added or unexpected removed
declarations; the single removed declaration is the reviewed unused private proof.

| Compiled comparison quantity | Raw strict comparison | Reviewed comparison |
| --- | ---: | ---: |
| Declaration counts, before → after | 4,527 → 4,526 | 4,527 → 4,526 |
| Public declarations, each snapshot | 2,499 | 2,499 |
| Data values, each snapshot | 863 | 863 |
| Retained declarations with residual AST differences | 15 | 0 |
| Public signature differences | 3 | 0 |
| Data-value differences | 4 | 0 |
| Status | `review_required` | `passed`, qualified below |

Lean's kernel accepted literal `Eq.refl` certificates for the two exact closed
instance-expression pairs, with only the permitted standard axioms. It rejected
the false `Nat.zero = Nat.succ Nat.zero` control with exit status 1. The
[reviewed comparison](metadata/elaboration/2026-10-06/cleanup-reviewed-comparison.json)
applies only those two ground substitutions and finds zero residual differences
across all 4,526 retained declarations, including 2,499 public types and 863
data values. This establishes the reported preservation modulo these
kernel-confirmed definitional equalities; raw AST identity is not the result.
The [instance witnesses](metadata/elaboration/2026-10-06/instance-witnesses.json)
and [fresh scratch-run validation](metadata/elaboration/2026-10-06/instance-runner-validation.json)
retain the positive/negative kernel evidence and a newly exercised reproducer.
Its 15 Python guard controls also passed; those synthetic controls are distinct
from the actual kernel checks.

Fresh Nanoda replay passed all three solution cases after rebuilding its pinned
source with Rust 1.90.0. It checked 59,959, 62,881 and 58,851 declarations for
achievability, converse and Choi cloning, respectively; these overlapping
dependency-closure counts must not be added. All seven acceptance/rejection
control groups passed. The [fresh result](metadata/elaboration/2026-10-06/verification/nanoda-result.json)
and [verification records](metadata/elaboration/2026-10-06/verification/) bind
the cleanup proof fingerprint and actual executions. These were local
unsandboxed checks. Fresh Comparator passed all three statement/constant
comparisons, axiom checks and Lean kernel replays; the wrapper exited 0.
Refreshing metadata hashes is not a new checker pass.

## 5. Heavy tail and top 30 files

| Logged elapsed threshold | Before | After | Count change |
| --- | ---: | ---: | ---: |
| At least 10 seconds | 264 | 273 | +9 |
| At least 20 seconds | 161 | 225 | +64 |
| At least 30 seconds | 115 | 151 | +36 |
| At least 40 seconds | 89 | 75 | -14 |

The ≥10/20/30-second tiers worsened while the ≥40-second tier improved. The
heavy tail therefore did not improve uniformly, despite its lower maximum
and logged-duration sum. All durations are visible, so the tier changes are
not caused by missing log events.

| After rank | Module | Before elapsed | After elapsed | Change |
| --- | --- | ---: | ---: | ---: |
| 1 | `FreeEntropy.TensorWeightBasis` | 148.0s | 76.0s | -72.0s |
| 2 | `FreeEntropy.RaisingKernel` | 19.0s | 57.0s | +38.0s |
| 3 | `FreeEntropy.UnitaryDecompositionBasic` | 14.0s | 57.0s | +43.0s |
| 4 | `FreeEntropy.ExteriorWeights` | 10.0s | 54.0s | +44.0s |
| 5 | `FreeEntropy.LieDecomposition` | 51.0s | 54.0s | +3.0s |
| 6 | `FreeEntropy.TensorLieCyclicity` | 14.0s | 54.0s | +40.0s |
| 7 | `FreeEntropy.SchurWeylWeightMultiplicity` | 11.0s | 53.0s | +42.0s |
| 8 | `FreeEntropy.TensorLieRestriction` | 12.0s | 53.0s | +41.0s |
| 9 | `FreeEntropy.TensorPowers` | 14.0s | 53.0s | +39.0s |
| 10 | `FreeEntropy.CyclicWeightHighest` | 9.8s | 52.0s | +42.2s |
| 11 | `FreeEntropy.TensorTorusIntertwiner` | 10.0s | 52.0s | +42.0s |
| 12 | `FreeEntropy.CanonicalChoi` | 15.0s | 51.0s | +36.0s |
| 13 | `FreeEntropy.ConstructedLieCloning` | 74.0s | 50.0s | -24.0s |
| 14 | `FreeEntropy.ExteriorMultiplicity` | 73.0s | 50.0s | -23.0s |
| 15 | `FreeEntropy.ScalarCommutantIrreducible` | 16.0s | 50.0s | +34.0s |
| 16 | `FreeEntropy.CanonicalDualCyclicHighest` | 38.0s | 49.0s | +11.0s |
| 17 | `FreeEntropy.ChoiContraction` | 34.0s | 49.0s | +15.0s |
| 18 | `FreeEntropy.OccupationRatio` | 11.0s | 49.0s | +38.0s |
| 19 | `FreeEntropy.OccupationWerner` | 10.0s | 49.0s | +39.0s |
| 20 | `FreeEntropy.RankOneEndpoints` | 41.0s | 49.0s | +8.0s |
| 21 | `FreeEntropy.ReverseChoi` | 34.0s | 49.0s | +15.0s |
| 22 | `FreeEntropy.Theorem2Canonical` | 27.0s | 49.0s | +22.0s |
| 23 | `FreeEntropy.Theorem2RankOneGT` | 25.0s | 49.0s | +24.0s |
| 24 | `FreeEntropy.TypicalCanonicalRows` | 13.0s | 49.0s | +36.0s |
| 25 | `FreeEntropy.CartanChannel` | 24.0s | 48.0s | +24.0s |
| 26 | `FreeEntropy.CloningFromRows` | 38.0s | 48.0s | +10.0s |
| 27 | `FreeEntropy.CoordinateWeightSpace` | 72.0s | 48.0s | -24.0s |
| 28 | `FreeEntropy.Twirling` | 16.0s | 48.0s | +32.0s |
| 29 | `FreeEntropy.CanonicalCharacter` | 52.0s | 47.0s | -5.0s |
| 30 | `FreeEntropy.CartanMultiplicity` | 62.0s | 47.0s | -15.0s |

These build ranks select own-file profile candidates. They do not alone
identify expensive proof bodies or separate import loading from shared-host
contention. Serial after profiles of the nine-module union of original/new top-five
modules are reported below.

## 6. Per-family aggregation

Stable module-name prefix groups localize the one broad namespace/directory.
The family module counts are unchanged. These sums are elapsed proxies, not
namespace CPU measurements; opposite group shifts require profile evidence.

| Module family | Modules | Before logged sum | After logged sum | Change |
| --- | ---: | ---: | ---: | ---: |
| `FreeEntropy.Canonical` | 24 | 756.0s | 832.0s | +76.0s |
| `FreeEntropy.Lie` | 26 | 1002.0s | 828.0s | -174.0s |
| `FreeEntropy.Exterior` | 30 | 1329.0s | 821.0s | -508.0s |
| `FreeEntropy.Tensor` | 20 | 732.5s | 692.0s | -40.5s |
| `FreeEntropy.Schur` | 19 | 600.0s | 617.0s | +17.0s |
| `FreeEntropy.Occupation` | 15 | 402.0s | 500.0s | +98.0s |
| `FreeEntropy.Weyl` | 14 | 537.3s | 413.0s | -124.3s |
| `FreeEntropy.Cartan` | 12 | 267.0s | 389.0s | +122.0s |
| `FreeEntropy.GT` | 11 | 391.0s | 322.0s | -69.0s |
| `FreeEntropy.Physical` | 9 | 230.0s | 312.0s | +82.0s |
| `FreeEntropy.Unitary` | 7 | 293.2s | 228.0s | -65.2s |
| `FreeEntropy.Theorem` | 7 | 191.0s | 208.0s | +17.0s |
| `FreeEntropy.Cyclic` | 6 | 310.8s | 200.0s | -110.8s |
| `FreeEntropy.Casimir` | 4 | 46.4s | 132.0s | +85.6s |
| `FreeEntropy.Trace` | 3 | 73.0s | 118.0s | +45.0s |
| `FreeEntropy.Cloning` | 3 | 70.0s | 107.0s | +37.0s |
| `FreeEntropy.Orbit` | 3 | 111.0s | 103.0s | -8.0s |
| `FreeEntropy.Constructed` | 2 | 125.0s | 94.0s | -31.0s |
| `FreeEntropy.Reverse` | 3 | 72.0s | 92.0s | +20.0s |
| `FreeEntropy.Rank` | 3 | 66.0s | 86.0s | +20.0s |
| `FreeEntropy.Signed` | 2 | 124.0s | 84.0s | -40.0s |
| `FreeEntropy.Pure` | 3 | 72.0s | 79.0s | +7.0s |
| `FreeEntropy.Specified` | 2 | 133.0s | 76.0s | -57.0s |
| `FreeEntropy.Typical` | 2 | 25.0s | 72.0s | +47.0s |
| `facades` | 4 | 62.0s | 71.9s | +9.9s |
| `FreeEntropy.Torus` | 2 | 76.0s | 70.0s | -6.0s |
| `FreeEntropy.Sector` | 2 | 36.0s | 63.0s | +27.0s |
| `FreeEntropy.Raising` | 1 | 19.0s | 57.0s | +38.0s |
| `FreeEntropy.Quantum` | 2 | 80.5s | 55.0s | -25.5s |
| `FreeEntropy.Word` | 2 | 116.0s | 53.0s | -63.0s |
| `FreeEntropy.Kostant` | 2 | 91.0s | 51.0s | -40.0s |
| `FreeEntropy.Weight` | 2 | 53.0s | 51.0s | -2.0s |
| `FreeEntropy.Scalar` | 1 | 16.0s | 50.0s | +34.0s |
| `FreeEntropy.Choi` | 1 | 34.0s | 49.0s | +15.0s |
| `FreeEntropy.Coordinate` | 1 | 72.0s | 48.0s | -24.0s |
| `FreeEntropy.Twirling` | 1 | 16.0s | 48.0s | +32.0s |
| `FreeEntropy.Geometric` | 1 | 50.0s | 47.0s | -3.0s |
| `FreeEntropy.Projector` | 1 | 26.0s | 47.0s | +21.0s |
| `FreeEntropy.Atypical` | 1 | 9.6s | 42.0s | +32.4s |
| `FreeEntropy.Polynomial` | 1 | 19.0s | 38.0s | +19.0s |
| `FreeEntropy.Spectral` | 1 | 29.0s | 37.0s | +8.0s |
| `FreeEntropy.Multiplicity` | 1 | 10.0s | 34.0s | +24.0s |
| `FreeEntropy.Constant` | 1 | 22.0s | 32.0s | +10.0s |
| `FreeEntropy.Isometric` | 1 | 17.0s | 31.0s | +14.0s |
| `FreeEntropy.Spectrum` | 1 | 61.0s | 29.0s | -32.0s |
| `FreeEntropy.Proofs` | 1 | 7.5s | 28.0s | +20.5s |
| `FreeEntropy.Identity` | 1 | 10.0s | 25.0s | +15.0s |
| `FreeEntropy.Root` | 1 | 62.0s | 25.0s | -37.0s |
| `FreeEntropy.Highest` | 1 | 15.0s | 23.0s | +8.0s |
| `FreeEntropy.Concentration` | 1 | 19.0s | 21.0s | +2.0s |
| `FreeEntropy.Finite` | 1 | 25.0s | 21.0s | -4.0s |
| `FreeEntropy.One` | 1 | 10.0s | 21.0s | +11.0s |
| `FreeEntropy.Channels` | 1 | 24.0s | 20.0s | -4.0s |
| `FreeEntropy.Optimal` | 1 | 10.0s | 20.0s | +10.0s |
| `FreeEntropy.Mean` | 1 | 19.0s | 17.0s | -2.0s |
| `FreeEntropy.Statements` | 1 | 7.0s | 17.0s | +10.0s |
| `FreeEntropy.Protocol` | 1 | 18.0s | 15.0s | -3.0s |
| `FreeEntropy.Supported` | 1 | 59.0s | 15.0s | -44.0s |
| `FreeEntropy.Gelfand` | 1 | 29.0s | 14.0s | -15.0s |

## 7. Serial warm own-file profiles and A/B evidence

Five baseline hotspots were profiled serially after the baseline build. Import
was the largest phase in all five; it accounted for 65–85% of wall in four and
48.1% in `TensorWeightBasis`. Tensor's tactic phase was also substantial (17.9s),
with three large `refine` events totaling 15.81s; the evidence did not justify
speculative typeclass caches or a broad simp/arithmetical tactic rewrite.

The import lever was tested at `FreeEntropy.GTDeterminant` with three sequential
before samples followed by three sequential after samples. All exited zero
and each sample's source hash remained unchanged. Total CPU is user plus system
CPU for that command, distinct from profiler elapsed phases.

| Sample within batch | Before wall | After wall | Before total CPU | After total CPU | Before import | After import |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 52.44s | 15.76s | 15.56s | 7.88s | 43.50s | 9.78s |
| 2 | 26.35s | 10.30s | 11.71s | 6.10s | 17.80s | 5.67s |
| 3 | 39.11s | 11.24s | 12.45s | 6.11s | 32.70s | 6.64s |
| Median | 39.11s | 11.24s | 12.45s | 6.11s | 32.70s | 6.64s |

| GT median metric | Absolute change | Observed reduction |
| --- | ---: | ---: |
| Command wall time | −27.87s | 71.3% |
| Total process CPU | −6.34s | 50.9% |
| Import elapsed phase | −26.06s | 79.7% |

The numbered rows are separate sequential batches, not randomized paired
experiments. The before wall range was 26.35–52.44s; after was 10.30–15.76s.
Both raw distributions and medians are provided. Import phase reduction exceeds
the skill's retention threshold, and no proof-local phase increased materially.
Shared-host scheduling and uncontrolled cache warmth limit exact causal
attribution of the percentages. Profiler phases are elapsed timers and are
not immune to machine load.

### Original five hotspots: serial before/after observations

All nine after-profile commands passed, with unchanged source hashes within
each sample. The five original files also have identical source hashes across
the before/after batches. Their after batch finished at
`2026-10-07T00:02:54.373430+00:00`; its run label follows the 2026-10-06 build
campaign. GNU time, Lean pin, four-thread setting and serial execution match.

| Original hotspot | Before wall | After wall | Before total CPU | After total CPU | Before import | After import |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `FreeEntropy.TensorWeightBasis` | 66.90s | 62.76s | 33.79s | 37.12s | 32.20s | 20.90s |
| `FreeEntropy.WeylTranslation` | 25.68s | 22.78s | 10.98s | 11.03s | 18.60s | 15.40s |
| `FreeEntropy.WeylCoefficient` | 19.57s | 12.96s | 9.03s | 7.06s | 13.00s | 7.88s |
| `FreeEntropy.LieDeterminantTwist` | 35.49s | 18.35s | 13.23s | 9.46s | 23.20s | 11.70s |
| `FreeEntropy.LiePBWDimension` | 48.76s | 16.63s | 14.38s | 9.53s | 41.40s | 9.95s |

Static import analysis places **none of these nine profile modules among the
43 consumers of the changed GT header**. Their sources and import closures
therefore supply controls for unrelated timing shifts, not evidence of a GT
speedup. Each hotspot has one sample per relevant batch; these observations
are not the three-sample intervention experiment. Lower import times across
unchanged closures demonstrate the influence of machine/cache state.

| Original hotspot, after | Elaboration | Typeclass inference | Simp | Tactic execution | Interpretation | Type checking |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `FreeEntropy.TensorWeightBasis` | 0.468s | 13.600s | 0.739s | 20.300s | 2.160s | 0.655s |
| `FreeEntropy.WeylTranslation` | 0.079s | 1.270s | 0.201s | 0.133s | 2.080s | 0.069s |
| `FreeEntropy.WeylCoefficient` | 0.023s | 0.433s | 0.070s | 0.152s | 1.300s | 0.039s |
| `FreeEntropy.LieDeterminantTwist` | 0.140s | 0.935s | 0.346s | 0.440s | 1.980s | 0.166s |
| `FreeEntropy.LiePBWDimension` | 0.087s | 0.770s | 0.162s | 0.191s | 2.420s | 0.093s |

`TensorWeightBasis` remains the principal local candidate: after import is
20.9s (33.3% of wall), tactic execution is 20.3s (32.3%), and typeclass inference
is 13.6s (21.7%). Three `refine` events took 6.82, 5.61 and 5.64 seconds, totaling
18.07s. The largest simp event is 404ms. No concentrated repeated expensive
closed head-class search was identified; typeclass inference is still below
the quarter-of-wall dominance screen. Its source and import closure were
unchanged; no local tactic improvement was applied or demonstrated.

The other four original files still have import as their largest phase,
roughly 60–68% of after command wall. Their largest local phase remains below
five seconds. Single-sample shifts do not justify proof-body rewrites.

### Four new top-build candidates: serial after profiles

| New candidate | Wall | Total CPU | Import | Typeclass | Simp | Tactics | Interpretation |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `FreeEntropy.RaisingKernel` | 13.05s | 7.95s | 7.90s | 0.469s | 0.135s | 0.172s | 1.59s |
| `FreeEntropy.UnitaryDecompositionBasic` | 21.15s | 14.07s | 9.88s | 5.830s | 0.670s | 0.931s | 2.26s |
| `FreeEntropy.ExteriorWeights` | 26.67s | 10.64s | 19.50s | 0.967s | 0.250s | 0.248s | 2.81s |
| `FreeEntropy.LieDecomposition` | 41.72s | 18.15s | 31.30s | 5.890s | 0.984s | 1.710s | 2.14s |

- `RaisingKernel`: import is 60.5% of wall. No local phase exceeds five seconds;
  the raw output identifies unused simp arguments rather than a hot simplifier.
- `UnitaryDecompositionBasic`: import is 46.7% of wall and typeclass inference
  is 5.83s (27.6%), so both qualify for the dominant-phase screen. Visible named
  searches include `CoeFun`, `Submodule.HasOrthogonalProjection`, `MulHomClass`
  and `DecidablePred`; each reported event is at most 253ms. The cumulative
  cost is diffuse. A cache is not justified without tracing a recurring costly
  closed search and demonstrating its benefit with A/B measurements.
- `ExteriorWeights`: import is 73.1% of wall; local phases are small. The only
  visible class searches are `Nonempty` events at 103–126ms. No proof edit is
  indicated by the profile.
- `LieDecomposition`: import is 75.0% of wall. Typeclass inference totals 5.89s
  but only 14.1% of wall. Named events cover several distinct classes, with
  the largest at 432ms. The largest simp event is 418ms. No broad cache or
  simplifier sweep follows from this single import-heavy sample.

Native phase categories can overlap and omit work; they need not sum to wall.
All unmodified-hotspot comparisons remain shared-host observations. Their
changed timings are deliberately excluded from the claimed GT intervention
benefit. The successful second full build establishes compatibility; it does
not establish a whole-project CPU improvement.

Before GT source hash:
`6af9a884d352729a6ffc7d186d8c1cd43a8ace8afe233db8096039f41fa06e55`.
After GT source hash:
`c9735432180f29c8ac1df5a15448c088769c586d0f9ac404c18ce562ceb0257b`.
Public raw profile evidence is under
`metadata/elaboration/2026-10-06/{profiles-before,profiles-after,gt-before,gt-after}/`.
Each JSON record binds sample source and raw output hashes.

## 8. Findings and retained changes, ranked by actionability

1. **Retained: narrow `GTDeterminant` tactic imports.** Commit
   `4c2054c47d6c81615f5687fe5ac3f1c4dd1ea1d9` replaces the umbrella
   `Mathlib.Tactic` with `Mathlib.Tactic.Linarith` and
   `Mathlib.Tactic.Positivity`. This applies skill lever 1. Its only production
   changes are two import lines replacing one; source proof bodies and statement
   text are byte-identical. The isolated file compiled in all six serial samples.
   Static source-closure analysis predicts 2,982→1,426 expanded Mathlib files
   and 43 downstream consumers. The observed import-phase and CPU reductions
   support keeping the change. The complete second build now passes all
   consumers; its mixed wall/CPU/heavy-tail results do not establish a
   whole-project performance gain.

2. **Deferred: Tensor proof-local attribution.** Its large `refine` events
   supply a candidate for a focused dependent-call/unification investigation,
   and remains substantial after the second build, but no local intervention
   was applied. No typeclass cache, file split,
   broad simplifier rewrite, or heartbeat increase was introduced.

3. **Reproducer safety controls.** Benchmark removal paths are preflighted
   before deletion, escaping and shared build paths rejected, profiles record
   source stability, and build-log parsing distinguishes progress events from
   quoted diagnostic text. These are verification safeguards outside the
   timed Lean command; they are not proof-performance improvements.

The complete second snapshot confirms compatibility and mixed performance
observations. Effective CPU utilization rose; total CPU rose 5.83%; smaller
heavy-tail tiers worsened; the weighted path switched with unchanged internal
imports. Shared load and host memory pressure prevent an uncontended bottleneck
model or a broad causal gain claim.

## 9. What is not established

- Both full builds and the GT serial experiment are complete. Exact causal
  whole-project speedup and run-to-run variance are not established.
- Fresh dependency installation cost is excluded from both snapshots.
- OS page-cache state, concurrent machine activity and effective available
  cores are uncontrolled; matching a thread setting alone does not establish
  identical parallelism.
- One full before/after build cannot establish run-to-run variance.
- Logged module duration sums and weighted paths are scheduling diagnostics,
  not independent serial CPU measurements.
- GNU time's baseline maximum RSS is 3,318,497,280 bytes (3.09 GiB); it is
  a process/child maximum and does not sum simultaneous process memory. The
  after maximum is 2,946,777,088 bytes (2.74 GiB).
- Mid-run host memory/swap snapshots show memory pressure but cannot attribute
  host-wide swapping to this build or establish complete matched-load traces.
- Unprofiled tails, sub-threshold events and unattributed elaboration remain
  unresolved unless explicitly investigated.
- Compiled preservation is qualified by the two exact kernel-checked ground
  substitutions. The raw strict comparison retains its 15 syntactic differences;
  no unrestricted normalization or raw AST identity claim is made.

## 10. Exact reproduction methodology

Use the same toolchain/dependency pins and GNU time for both snapshots. Each
output directory must be new. Run from the checkout containing the source
revision being measured and the published helper scripts. Prepare the
dependency cache through the documented repository setup. Never run
`lake clean` or `lake update` for this experiment.

The before reproduction checkpoint is
`07d563cc77ef4ac8a439911f827162d277da4432`; it includes the helper scripts and
identical production Lean sources/pins to the original measured baseline.
The after source is `4c2054c47d6c81615f5687fe5ac3f1c4dd1ea1d9`. Both use the
published guarded runner hash
`12f3d80a94dc1ed05da6cf1a84e6b80d78270f38742e27958114f124f4efd00b`.
The launch-archived baseline helper hash differs as described in section 1.

After completing the before reproduction in the same isolated checkout,
run these commands from its repository root:

```sh
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
python3 scripts/profile_elaboration.py \
  --threads 4 \
  --modules FreeEntropy.TensorWeightBasis FreeEntropy.WeylTranslation \
    FreeEntropy.WeylCoefficient FreeEntropy.LieDeterminantTwist \
    FreeEntropy.LiePBWDimension FreeEntropy.RaisingKernel \
    FreeEntropy.UnitaryDecompositionBasic FreeEntropy.ExteriorWeights \
    FreeEntropy.LieDecomposition \
  --output .verify-work/elaboration-reproduction/after-profiles
```

The nine named modules reproduce the actual after-profile selection: the union
of original and new top-five build files. A new machine can separately select
its own hotspots with `--summary RUN/summary.json --top 5`. The runner removes
only owned artifacts; the serial profiler requests no olean/ilean/IR outputs
and records source stability. Root selection follows the script's location,
not an unrelated current directory.

## 11. Evidence pointers and prior report roles

- [Before-cleanup report](ELABORATION_REPORT_2026-10-06_BEFORE.md): the clean
  GNU-timer baseline after the dead-code sweep.
- Public evidence root: [metadata/elaboration/2026-10-06](metadata/elaboration/2026-10-06/),
  with [before build records](metadata/elaboration/2026-10-06/before/),
  [after build records](metadata/elaboration/2026-10-06/after/),
  [baseline warm profiles](metadata/elaboration/2026-10-06/profiles-before/),
  [after warm profiles](metadata/elaboration/2026-10-06/profiles-after/),
  and [GT before](metadata/elaboration/2026-10-06/gt-before/)/
  [GT after](metadata/elaboration/2026-10-06/gt-after/) samples.
- Reproduction checkpoint `07d563cc77ef4ac8a439911f827162d277da4432`
  contains the helper scripts and has identical production Lean sources/pins
  to the original measured baseline. The after revision is
  `4c2054c47d6c81615f5687fe5ac3f1c4dd1ea1d9`.
- The fresh final-source Lean audit passed all 2,499 public declarations.
  [Its summary](metadata/elaboration/2026-10-06/verification/lean-summary.json)
  and the [fresh statement check record](metadata/elaboration/2026-10-06/verification/statement-checks.json)
  bind the separate checks. Actual statement applications, binder export,
  and catalog/correspondence checks passed. Compiled preservation passed modulo
  the two exact kernel-checked instance pairs, preserving the separate
  [raw strict report](metadata/elaboration/2026-10-06/cleanup-comparison.json)
  and [qualified report](metadata/elaboration/2026-10-06/cleanup-reviewed-comparison.json).
  [Nanoda's fresh three-case result](metadata/elaboration/2026-10-06/verification/nanoda-result.json)
  passed, as did all three fresh Comparator comparisons, axiom checks and Lean
  kernel replays. Linux-sandboxed execution is not asserted.
- The aborted preliminary BSD-timer run and historical replayed/no-timing
  build logs are excluded from the comparison.
