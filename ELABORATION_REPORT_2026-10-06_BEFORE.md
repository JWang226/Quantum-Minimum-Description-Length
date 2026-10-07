<!-- Copyright (c) 2026 Free Entropy formalization contributors.
See LICENSE and NOTICE for license and attribution. -->

# Elaboration report: 2026-10-06, before cleanup

**Completed project-only baseline and five serial warm profiles.** The full
build passed at the recorded source revision. This snapshot follows the
dead-code sweep and precedes elaboration optimization. The GT import A/B below records the
subsequent measured cleanup decision; the complete second build is reported
separately in the after report.

## 1. Setup and provenance

The reporting and optimization methods use the requested
[lean-elaboration-test skill](https://github.com/scottnarmstrong/LeanAutoformalizationSkills/blob/601fe274276d93052ef645f0ff2c1a355e8e5b16/skills/lean-elaboration-test/SKILL.md)
and [lean-elaboration skill](https://github.com/scottnarmstrong/LeanAutoformalizationSkills/blob/601fe274276d93052ef645f0ff2c1a355e8e5b16/skills/lean-elaboration/SKILL.md),
pinned to commit `601fe274276d93052ef645f0ff2c1a355e8e5b16`.

| Field | Baseline |
| --- | --- |
| Source commit | `4c496959aa1462a6b6a6faf5535ea2a3caf9c119` |
| UTC start | `2026-10-06T22:32:09.100305+00:00` |
| UTC finish | `2026-10-06T23:11:35.870228+00:00` |
| Host | macOS 27.2, arm64; 8 reported logical CPUs |
| Lean | 4.29.0-rc6, commit `00659f8e6071d7e46131ed643bf8003b99b044e9` |
| Timing tool | GNU time, `-v`, `/opt/homebrew/bin/gtime` |
| Build target | `All` |
| Lean thread setting | `LEAN_NUM_THREADS=4` |
| Cache condition | Project artifacts invalidated; dependency oleans retained; OS cache uncontrolled |
| Source snapshot hash | `08fd4c03d6a037c5964d3299ae8e4cdb2d3cc94b89d0f5005f2b5477d3fd3f3b` |
| Build-log hash | `a7149000a5f6fc36bf70cd79d82ac2c836f72c356620635a69f2b48debbd2ceb` |
| Executed helper hash | `363f92aaadef7b4c6151fd4c43a17148f6c213a1ff30d92fb737440687985098` |
| Executed helper provenance | Archived at launch; hash bound after completion. Later guard revisions were outside the timed command. |
| Published reproducer helper hash | `12f3d80a94dc1ed05da6cf1a84e6b80d78270f38742e27958114f124f4efd00b` at checkpoint `07d563cc77ef4ac8a439911f827162d277da4432` |

The timed command, run from `lean/`, is:

```sh
LEAN_NUM_THREADS=4 /opt/homebrew/bin/gtime -v \
  "$HOME/.elan/bin/lake" --no-ansi --no-cache build All
```

The start inventory recorded a separate Lake/Lean reference-analysis process
(`cloning-dead-lean-refs.lean`). Other project work also used this shared machine;
the start inventory is not a continuous load trace. Co-running processes alone
do not invalidate the artifact scope, but this run does not provide controlled
contention or scheduling. Dependency/source snapshots remained unchanged and
no upstream module compilation occurred. High system CPU and the recorded page
fault/context-switch counters require caution about attributing build elapsed
time to proof work. Baseline host snapshots at 22:48:20 and 23:03:02 UTC
reported `vm.swapusage` used values of `2153.00M` and `2355.44M`, with increasing
host-wide swap counters. They are snapshots of the whole machine, not full-run
measurements attributable solely to the benchmark. GNU time's `Swaps: 0`
resource field does not imply that the host had no swapping.

## 2. Size snapshot

Counts come from the recorded Git revision using the requested skill's lexical
line-counting and module-header functions. Batched Git blob reads avoid repeated
per-file processes; they do not change the counter's rules.

| Quantity | Full committed Lean tree | Timed production scope |
| --- | ---: | ---: |
| Lean files | 285 | 274 |
| Non-comment-only files counted | 285 | 274 |
| Total lines | 38,921 | 35,927 |
| Non-comment code lines | 30,880 | 28,021 |
| Comment-only files excluded | 0 | 0 |
| Files without the new `module` keyword | 285 | 274 |

The production scope comprises 270 `FreeEntropy.*` modules and four facade or
reader-entry modules: `FreeEntropy`, `Theorem1`, `Theorem2`, and `All`. The other
11 committed Lean files are the generated axiom-audit probe, seven Comparator
challenge specifications, `ComparatorConfig.ReplayExports`, and two exporter
scripts. Those 11 are not part of this timed compilation scope.

`All` covers all 274 production modules. The log contains exactly 274 distinct
own-module `Built` events, with no missing, repeated, or off-facade production
modules; all 274 report elapsed durations. The total 3,752 Lake jobs also include
cached dependency and artifact-facet jobs and must not be interpreted as 3,752
compiled project files.

The project retains its legacy Lean module syntax. The elaboration skill's new
`module`-header convention is not satisfied. This measurement does not migrate
export semantics.

## 3. Headline measurements

| Quantity | Baseline |
| --- | ---: |
| Wall time | 2,362.93 s (39 min 22.93 s) |
| User CPU time | 1,249.26 s |
| System CPU time | 1,534.45 s |
| Total measured CPU time | 2,783.71 s |
| Average CPU utilization, computed from CPU / wall | 117.81% |
| GNU time's printed CPU utilization | 117% |
| Maximum RSS reported by GNU time | 3,318,497,280 bytes (3.09 GiB) |
| Planned Lake jobs | 3,752 |
| Own-module build events / distinct modules | 274 / 274 |
| Timing-visible modules / fraction | 274 / 100% |
| Sum of logged module elapsed durations | 9,188.80 s |
| Logged elapsed sum / wall time | 3.889 |
| Logged elapsed milliseconds / non-comment code line | 327.93 ms |
| Idealized CPU work floor on eight logical cores | 347.96 s |
| Longest observed weighted project import path | 1,442.50 s across 36 modules |

GNU time supplies measured process CPU. Lake's module durations are elapsed
durations under parallel load; their sum is a scheduling proxy, **not cumulative
CPU**. Their ratio to wall time measures observed overlap rather than dedicated
cores or useful proof execution. No module duration was imputed.

The idealized work floor divides measured CPU by eight reported logical cores;
those cores are heterogeneous and shared. The import-path weights inherit
contention from the parallel build. Comparing these two proxies does not
establish the uncontended work-bound or chain-bound regime. The weighted path
starts at `FreeEntropy.Weyl`, traverses the exterior/Lie/cloning development,
and ends at `FreeEntropy.Theorem1Complete`, `FreeEntropy`, and `All`; its full
module list is in the machine-readable summary.

Maximum RSS follows GNU time's process/child accounting and is not the sum of
memory held by simultaneous Lean processes. The timer also reported
13,960,195 major faults, 93,506,617 minor faults, and 56,005,205 involuntary
context switches. These are the timer's resource counters on macOS, not a
continuous host-memory or host-swap trace. System CPU exceeds user CPU; build
wall time therefore cannot be treated as proof-local elaboration time.

## 4. Build health and rule compliance

| Check | Result |
| --- | --- |
| Process exit status | 0 |
| Runner status | `passed` |
| Complete project rebuild | `true` |
| Independent summary measurement validity | `true` |
| Errors | 0 |
| Unauthorized sorry warnings / sorry axiom diagnostics | 0 |
| Warnings | 131 |
| Upstream `Built` events | 0 |
| Missing / repeated own-module events | 0 / 0 |
| Source snapshot changed within run | No |
| Dependency olean count/stat snapshots changed | No |
| Proof files above 1,500 lines | 0 |
| Existing heartbeat override occurrences | 121 |
| Existing linter suppression lines | 68 |

All required scope and artifact-stability checks passed. The dependency guard
compares olean path/count, file size, and modification-time snapshots; it is
not a full cryptographic content audit of every cached dependency olean. The
Mathlib cache contained 7,805 oleans. Dependencies were retained as inputs;
`lake clean` and `lake update` were not used.

| Warning kind | Count | Linter classification |
| --- | ---: | --- |
| Deprecated declaration | 2 | Unclassified deprecation diagnostic |
| Unnecessary sequence focus | 2 | `linter.unnecessarySeqFocus` |
| Unnecessary simpa | 9 | `linter.unnecessarySimpa` |
| Unreachable tactic | 2 | `linter.unreachableTactic` |
| Unused section variables | 51 | `linter.unusedSectionVars` |
| Unused simp argument | 61 | `linter.unusedSimpArgs` |
| Unused tactic | 3 | `linter.unusedTactic` |
| Unused variable | 1 | `linter.unusedVariables` |

Existing thresholds and linter suppressions were retained. Raising thresholds
or suppressing warnings does not demonstrate a performance improvement.

The later final-source Lean audit passed for all 2,499 public declarations,
with no placeholders or project-added axioms. Its permitted axiom set is
`propext`, `Classical.choice`, and `Quot.sound`. Fresh statement applications
also passed, and the exported endpoint binder lists match the recorded lists.
The refreshed compiled catalog contains 4,526 declarations (2,499 public and
2,027 auxiliary) across 270 proof modules; catalog and correspondence
consistency checks passed with all 33 Article and 9 Letter locators retained.
These checks ran outside this timed baseline. The later raw strict comparison
records 15 retained declaration AST differences, including three public
signatures and four data values; the four final theorem types are unchanged
in the raw comparison. A qualified comparison passed with zero residual
differences across 4,526 retained declarations, 2,499 public types and 863 data
values after only the two exact `IntPartialOrder`/`RealCharZero` ground
substitutions. Literal `Eq.refl` certificates for those pairs passed Lean's
kernel; its false-equality negative control was rejected. Raw AST identity
is not claimed. The fresh scratch reproducer and its 15 Python controls passed.

Fresh pinned-source Nanoda replay passed all three cases, checking 59,959,
62,881 and 58,851 declarations in their overlapping dependency closures;
all seven acceptance/rejection control groups passed. Fresh Comparator passed
all three statement/constant comparisons, axiom checks and Lean kernel replays.
These checks were unsandboxed and ran separately from the benchmarks.
No source-first manuscript or human review is claimed
by the fresh applications, catalog or bounded preservation checks.

## 5. Heavy tail and top 30 files

| Logged module elapsed threshold | Baseline file count |
| --- | ---: |
| At least 10 seconds | 264 |
| At least 20 seconds | 161 |
| At least 30 seconds | 115 |
| At least 40 seconds | 89 |

All production modules have visible durations. These are parallel-build elapsed
ranks, including import loading, artifact writes, scheduling, and contention.
They select warm-profile candidates; they do not identify expensive proof bodies
without profiles.

| Rank | Module | Logged elapsed seconds |
| --- | --- | ---: |
| 1 | `FreeEntropy.TensorWeightBasis` | 148.0 |
| 2 | `FreeEntropy.WeylTranslation` | 123.0 |
| 3 | `FreeEntropy.WeylCoefficient` | 99.0 |
| 4 | `FreeEntropy.LieDeterminantTwist` | 97.0 |
| 5 | `FreeEntropy.LiePBWDimension` | 96.0 |
| 6 | `FreeEntropy.SchurAchievability` | 96.0 |
| 7 | `FreeEntropy.CyclicWeightOrbit` | 95.0 |
| 8 | `FreeEntropy.ExteriorMonomialWeights` | 95.0 |
| 9 | `FreeEntropy.CyclicWeightStateBlocks` | 93.0 |
| 10 | `FreeEntropy.ExteriorCanonicalCyclicity` | 90.0 |
| 11 | `FreeEntropy.ExteriorMonomialColumns` | 84.0 |
| 12 | `FreeEntropy.CanonicalOrbit` | 82.0 |
| 13 | `FreeEntropy.SchurWeylConcentrationMonomial` | 82.0 |
| 14 | `FreeEntropy.ExteriorPhysicalIrrep` | 80.0 |
| 15 | `FreeEntropy.ExteriorCanonicalHighest` | 77.0 |
| 16 | `FreeEntropy.ConstructedLieCloning` | 74.0 |
| 17 | `FreeEntropy.ExteriorRootCounting` | 74.0 |
| 18 | `FreeEntropy.SchurWeylConcentrationGrouping` | 74.0 |
| 19 | `FreeEntropy.UnitaryDecomposition` | 74.0 |
| 20 | `FreeEntropy.ExteriorMultiplicity` | 73.0 |
| 21 | `FreeEntropy.SchurWeylConcentrationSupport` | 73.0 |
| 22 | `FreeEntropy.CoordinateWeightSpace` | 72.0 |
| 23 | `FreeEntropy.QuantumTransfer` | 72.0 |
| 24 | `FreeEntropy.SignedCartan` | 71.0 |
| 25 | `FreeEntropy.SpecifiedLieCloning` | 71.0 |
| 26 | `FreeEntropy.UnitaryCoordinates` | 70.0 |
| 27 | `FreeEntropy.WeylDimensionExtraction` | 70.0 |
| 28 | `FreeEntropy.TensorLieCyclicityPhysical` | 69.0 |
| 29 | `FreeEntropy.ExteriorWeightCoordinates` | 68.0 |
| 30 | `FreeEntropy.KostantWeightData` | 68.0 |

## 6. Per-family aggregation

The project uses one broad namespace and source directory. Stable module-name
prefix groups localize its workload; these are sums of elapsed proxies, not
separate CPU measurements. The four facade/entry files have their own group.

| Module family | Timed modules | Logged elapsed sum, seconds | Share of logged sum |
| --- | ---: | ---: | ---: |
| `FreeEntropy.Exterior` | 30 | 1329.0 | 14.46% |
| `FreeEntropy.Lie` | 26 | 1002.0 | 10.90% |
| `FreeEntropy.Canonical` | 24 | 756.0 | 8.23% |
| `FreeEntropy.Tensor` | 20 | 732.5 | 7.97% |
| `FreeEntropy.Schur` | 19 | 600.0 | 6.53% |
| `FreeEntropy.Weyl` | 14 | 537.3 | 5.85% |
| `FreeEntropy.Occupation` | 15 | 402.0 | 4.37% |
| `FreeEntropy.GT` | 11 | 391.0 | 4.26% |
| `FreeEntropy.Cyclic` | 6 | 310.8 | 3.38% |
| `FreeEntropy.Unitary` | 7 | 293.2 | 3.19% |
| `FreeEntropy.Cartan` | 12 | 267.0 | 2.91% |
| `FreeEntropy.Physical` | 9 | 230.0 | 2.50% |
| `FreeEntropy.Theorem` | 7 | 191.0 | 2.08% |
| `FreeEntropy.Specified` | 2 | 133.0 | 1.45% |
| `FreeEntropy.Constructed` | 2 | 125.0 | 1.36% |
| `FreeEntropy.Signed` | 2 | 124.0 | 1.35% |
| `FreeEntropy.Word` | 2 | 116.0 | 1.26% |
| `FreeEntropy.Orbit` | 3 | 111.0 | 1.21% |
| `FreeEntropy.Kostant` | 2 | 91.0 | 0.99% |
| `FreeEntropy.Quantum` | 2 | 80.5 | 0.88% |
| `FreeEntropy.Torus` | 2 | 76.0 | 0.83% |
| `FreeEntropy.Trace` | 3 | 73.0 | 0.79% |
| `FreeEntropy.Coordinate` | 1 | 72.0 | 0.78% |
| `FreeEntropy.Pure` | 3 | 72.0 | 0.78% |
| `FreeEntropy.Reverse` | 3 | 72.0 | 0.78% |
| `FreeEntropy.Cloning` | 3 | 70.0 | 0.76% |
| `FreeEntropy.Rank` | 3 | 66.0 | 0.72% |
| `FreeEntropy.Root` | 1 | 62.0 | 0.67% |
| `facades` | 4 | 62.0 | 0.67% |
| `FreeEntropy.Spectrum` | 1 | 61.0 | 0.66% |
| `FreeEntropy.Supported` | 1 | 59.0 | 0.64% |
| `FreeEntropy.Weight` | 2 | 53.0 | 0.58% |
| `FreeEntropy.Geometric` | 1 | 50.0 | 0.54% |
| `FreeEntropy.Casimir` | 4 | 46.4 | 0.50% |
| `FreeEntropy.Sector` | 2 | 36.0 | 0.39% |
| `FreeEntropy.Choi` | 1 | 34.0 | 0.37% |
| `FreeEntropy.Gelfand` | 1 | 29.0 | 0.32% |
| `FreeEntropy.Spectral` | 1 | 29.0 | 0.32% |
| `FreeEntropy.Projector` | 1 | 26.0 | 0.28% |
| `FreeEntropy.Finite` | 1 | 25.0 | 0.27% |
| `FreeEntropy.Typical` | 2 | 25.0 | 0.27% |
| `FreeEntropy.Channels` | 1 | 24.0 | 0.26% |
| `FreeEntropy.Constant` | 1 | 22.0 | 0.24% |
| `FreeEntropy.Concentration` | 1 | 19.0 | 0.21% |
| `FreeEntropy.Mean` | 1 | 19.0 | 0.21% |
| `FreeEntropy.Polynomial` | 1 | 19.0 | 0.21% |
| `FreeEntropy.Raising` | 1 | 19.0 | 0.21% |
| `FreeEntropy.Protocol` | 1 | 18.0 | 0.20% |
| `FreeEntropy.Isometric` | 1 | 17.0 | 0.19% |
| `FreeEntropy.Scalar` | 1 | 16.0 | 0.17% |
| `FreeEntropy.Twirling` | 1 | 16.0 | 0.17% |
| `FreeEntropy.Highest` | 1 | 15.0 | 0.16% |
| `FreeEntropy.Identity` | 1 | 10.0 | 0.11% |
| `FreeEntropy.Multiplicity` | 1 | 10.0 | 0.11% |
| `FreeEntropy.One` | 1 | 10.0 | 0.11% |
| `FreeEntropy.Optimal` | 1 | 10.0 | 0.11% |
| `FreeEntropy.Atypical` | 1 | 9.6 | 0.10% |
| `FreeEntropy.Proofs` | 1 | 7.5 | 0.08% |
| `FreeEntropy.Statements` | 1 | 7.0 | 0.08% |

## 7. Serial warm own-file profiles

The five highest ranked baseline files were profiled **one at a time**, after
the completed build, using the same Lean pin, GNU timer and four-thread setting.
All five commands exited zero. Source hashes before and after every profile
match, and no olean/ilean/IR outputs were requested. Raw outputs and source/output
hashes are recorded in `profiles-before/profiles.json`; the final record timestamp
is `2026-10-06T23:15:29.278509+00:00`.

Each file has one sample. These are serial own-file measurements with warm
imports, not a three-run A/B comparison. The machine remained shared; profiler
phase timers also measure elapsed work and are **not immune to contention**.

| Module | Build elapsed | Warm command wall | User CPU | System CPU | Import phase | Import / wall |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `FreeEntropy.TensorWeightBasis` | 148.0s | 66.90s | 25.25s | 8.54s | 32.20s | 48.1% |
| `FreeEntropy.WeylTranslation` | 123.0s | 25.68s | 4.44s | 6.54s | 18.60s | 72.4% |
| `FreeEntropy.WeylCoefficient` | 99.0s | 19.57s | 3.88s | 5.15s | 13.00s | 66.4% |
| `FreeEntropy.LieDeterminantTwist` | 97.0s | 35.49s | 5.76s | 7.47s | 23.20s | 65.4% |
| `FreeEntropy.LiePBWDimension` | 96.0s | 48.76s | 4.92s | 9.46s | 41.40s | 84.9% |

| Module | Elaboration | Typeclass inference | Simp | Tactic execution | Interpretation | Type checking |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `FreeEntropy.TensorWeightBasis` | 0.298s | 10.900s | 1.130s | 17.900s | 1.920s | 0.761s |
| `FreeEntropy.WeylTranslation` | 0.048s | 1.050s | 0.179s | 0.109s | 2.030s | 0.064s |
| `FreeEntropy.WeylCoefficient` | 0.031s | 0.464s | 0.074s | 0.131s | 2.460s | 0.047s |
| `FreeEntropy.LieDeterminantTwist` | 0.254s | 1.350s | 0.656s | 0.580s | 2.950s | 0.194s |
| `FreeEntropy.LiePBWDimension` | 0.096s | 1.080s | 0.202s | 0.251s | 2.360s | 0.117s |

Import is the largest recorded phase in all five files and exceeds half of
command wall time in four. `TensorWeightBasis` is the exception: import accounts
for 48.1% of wall, while tactic execution accounts for 26.8%. Both phases pass
the skill's dominant-phase screen (above five seconds and one quarter of wall).
Its typeclass total is 10.9 seconds but only 16.3% of wall, so it does not pass
that dominance screen.

The reported build durations exceed the subsequent warm command durations by
roughly 2.0–5.1 times. This demonstrates why build ranks need confirmation;
it does not partition the difference into serialization, concurrency, import
cache state or unrelated machine load.

The raw events above the profiler threshold give these routing observations:

- `TensorWeightBasis`: three `refine` events took 3.25, 6.96 and 5.60 seconds,
  accounting for 15.81 seconds of the 17.9-second tactic total. The largest
  reported simp event was 802 milliseconds; the other reported simp event was
  106 milliseconds. Visible typeclass events concerned `CoeFun`, `Fintype`
  and unattributed searches, all at or below 288 milliseconds. The large
  cumulative typeclass total does not identify a recurring expensive closed
  head-class search suitable for a cache.
- `WeylTranslation`: import took 18.6 seconds. The sole additional visible
  event was an `AddHomClass` search at 189 milliseconds.
- `WeylCoefficient`: import took 13.0 seconds. No large local phase or
  arithmetic-closer event was reported. The unused and unreachable simp
  diagnostics are cleanup evidence, not a measured performance benefit.
- `LieDeterminantTwist`: import took 23.2 seconds; the visible local events were
  a 181-millisecond rewrite, 145-millisecond simp, and 156-millisecond `CoeT`
  search. Its unused-simp and unnecessary-simpa warnings do not establish a
  slow simplifier.
- `LiePBWDimension`: import took 41.4 seconds. Visible local events included
  `Nonempty` at 123 milliseconds, simp at 157 milliseconds, and `Semiring`
  search at 188 milliseconds.

Cumulative phase categories can overlap and omit serialization; they need not
add to wall time. The unprofiled tail remains unclassified. No blanket
`nlinarith`, `simp only`, instance-cache or file-splitting sweep is justified
by these five samples.

The [after report](ELABORATION_REPORT_2026-10-06_AFTER.md) supplies the matched
single-sample observations and four newly ranked candidates. All nine after
profiles passed with stable sources. None of those nine files consumes the
changed GT import header, so its timing shifts are excluded from the GT
intervention claim.

## 8. Findings ranked by actionability

1. **Measure narrowing the tactic import at `FreeEntropy.GTDeterminant`.**
   This is skill lever 1, import-load reduction. Static source-import analysis
   predicts that replacing the `Mathlib.Tactic` umbrella with the required
   `Mathlib.Tactic.Linarith` and `Mathlib.Tactic.Positivity` providers reduces
   that module's expanded Mathlib closure from 2,982 to 1,426 files (1,556
   fewer, 52.2%). It predicts 43 downstream production consumers and no
   missing project/Mathlib sources. This aligns with the import-heavy serial
   profiles and has a clear falsification test: compile the narrowed file,
   verify each consumer, compare three serial samples per variant, then score
   a complete second build. The lexical tactic-provider screen is not an
   elaboration pass and does not prove instance/tactic compatibility.
   Three serial samples per variant subsequently passed, with stable source
   hashes. Median warm wall time fell from 39.11 to 11.24 seconds (71.3%);
   median total process CPU fell from 12.45 to 6.11 seconds (50.9%); median
   import phase fell from 32.70 to 6.64 seconds (79.7%). The import-only change
   was retained in `4c2054c47d6c81615f5687fe5ac3f1c4dd1ea1d9`. Source proof bodies and
   statement text were unchanged. The three before samples preceded the three
   after samples; cache warmth and shared load were not randomized or held
   fixed. These observations support retention without establishing that
   the entire elapsed improvement was caused by the edit. The complete after
   build now passes all consumers; mixed whole-project metrics are reported
   separately and do not establish a broad gain.

2. **Attribute the `TensorWeightBasis` `refine` events before changing proofs.**
   Its measured tactic total supplies a secondary local candidate beyond
   import load. The events currently lack declaration attribution. Investigate
   the exact dependent calls/unification context before considering lever 6
   (minimal-context helper extraction) or an explicit term annotation.
   No proof transformation has been tested or retained here. A typeclass
   cache is not justified: typeclass inference is not dominant, and the
   visible events do not show a costly repeated closed search.

3. **Leave the other four top-file proof bodies alone.**
   Their largest local phases are below the five-second dominant-phase floor;
   import loading accounts for 65–85% of their command wall times. Changing
   arithmetic closers or narrowing simp lists without a hot call would not
   address the measured bottleneck. Naming functions in `congr` is not
   supported by these raw profiles, which report no expensive congr events.

4. **Keep warning hygiene separate from speed claims.** The baseline records
   61 unused simp arguments, 51 unused section-variable diagnostics and other
   small warning groups. Safe removal of unused proof steps can be checked,
   but unused section-variable removal can change public theorem binders.
   Any such change needs signature review; suppressing the warning is not
   evidence of faster elaboration.

The baseline and top-five profiles are complete. One import-only intervention
was retained after the following serial A/B measurements. All six commands
exited zero and their source hashes were stable within each sample.

| GT sample | Before wall | After wall | Before total CPU | After total CPU | Before import | After import |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 52.44s | 15.76s | 15.56s | 7.88s | 43.50s | 9.78s |
| 2 | 26.35s | 10.30s | 11.71s | 6.10s | 17.80s | 5.67s |
| 3 | 39.11s | 11.24s | 12.45s | 6.11s | 32.70s | 6.64s |
| Median | 39.11s | 11.24s | 12.45s | 6.11s | 32.70s | 6.64s |

The rows number samples within their separate before/after batches; they are
not simultaneous or randomized paired runs. The import median decreases by
26.06 seconds, exceeding the skill's retention threshold. No proof-local
phase increased materially. Variability in the before batch and shared-host
phase timings prevent an exact causal attribution of the percentage changes.
The full after snapshot now passes. It reports mixed whole-project metrics,
including increased total CPU; see the after report for comparison limits.

The before source hash is
`6af9a884d352729a6ffc7d186d8c1cd43a8ace8afe233db8096039f41fa06e55`;
the after source hash is
`c9735432180f29c8ac1df5a15448c088769c586d0f9ac404c18ce562ceb0257b`.
Public evidence is archived at
`metadata/elaboration/2026-10-06/gt-before/profiles.json` and
`metadata/elaboration/2026-10-06/gt-after/profiles.json`.

## 9. What this measurement does not establish

- The baseline and top-five profiles are complete, and the GT import change
  has six serial measurements. Its complete second-build impact and broader
  causal whole-project optimization outcomes remain unestablished.
- Dependency build cost is deliberately outside scope; this is not a fresh
  uncached end-to-end installation measurement.
- Shared-machine wall time can reflect contention and scheduling. CPU and
  logged-duration trends require separate interpretation.
- Module timing sums and weighted import paths do not provide independent
  serial CPU measurements.
- A single before/after build does not estimate run-to-run variance.
- Unprofiled modules and profiler events below its threshold remain
  unattributed.
- Benchmark success alone does not establish informal/formal correspondence
  or independent kernel verification.

## 10. Reproduction methodology

Use the recorded Lean and dependency pins, Python 3.11+, Git, and GNU time.
Prepare dependency caches through the repository's documented setup; do not
run `lake clean` or `lake update`. The guarded runner removes only owned proof
artifacts and preserves the dependency and Comparator artifact trees.

The original measurement source is
`4c496959aa1462a6b6a6faf5535ea2a3caf9c119`. Use instrumentation checkpoint
`07d563cc77ef4ac8a439911f827162d277da4432` to reproduce it with the published
helpers; their production Lean sources and pins are identical. The full Git
size differs because instrumentation was added outside the timed library.
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
  --threads 4 \
  --modules FreeEntropy.TensorWeightBasis FreeEntropy.WeylTranslation \
    FreeEntropy.WeylCoefficient FreeEntropy.LieDeterminantTwist \
    FreeEntropy.LiePBWDimension \
  --output .verify-work/elaboration-reproduction/before-profiles
python3 scripts/profile_elaboration.py \
  --threads 4 --repeat 3 --modules FreeEntropy.GTDeterminant \
  --output .verify-work/elaboration-reproduction/gt-before
```

The named files reproduce the recorded hotspot selection; a new machine can
select its own top five with `--summary RUN/summary.json --top 5`. The helper
root is derived from its own location. The original baseline runner was
archived at launch; the published helper adds safety guards outside the same
timed Lean command. Cite the measured proof-source revision and helper revision
separately.

## 11. Evidence pointers and prior reports

- [After-cleanup report](ELABORATION_REPORT_2026-10-06_AFTER.md): completed
  second full snapshot and comparison, with the later Lean audit pass and
  the status of separate preservation and independent checker runs.
- [Fresh Lean audit summary](metadata/elaboration/2026-10-06/verification/lean-summary.json)
  and [statement applications/checks](metadata/elaboration/2026-10-06/verification/statement-checks.json)
  record separate final-source runs outside the timed measurements.
- Preservation evidence retains the [raw strict comparison](metadata/elaboration/2026-10-06/cleanup-comparison.json),
  [qualified comparison](metadata/elaboration/2026-10-06/cleanup-reviewed-comparison.json),
  [exact instance witnesses](metadata/elaboration/2026-10-06/instance-witnesses.json),
  and [fresh reproducer validation](metadata/elaboration/2026-10-06/instance-runner-validation.json).
  The [fresh Nanoda result](metadata/elaboration/2026-10-06/verification/nanoda-result.json)
  records a separate three-case pass for the cleanup sources.
- Public evidence directory: [metadata/elaboration/2026-10-06](metadata/elaboration/2026-10-06/).
  Its [before/](metadata/elaboration/2026-10-06/before/) records contain the
  build log and run/summary/size data;
  [profiles-before/](metadata/elaboration/2026-10-06/profiles-before/) contains
  the five serial profiles; [gt-before/](metadata/elaboration/2026-10-06/gt-before/)
  and [gt-after/](metadata/elaboration/2026-10-06/gt-after/) contain the
  six import-experiment samples. Host-memory snapshots and process inventories
  remain local, are summarized in this report, and are omitted from the public
  raw archive.
- Reproduction checkpoint `07d563cc77ef4ac8a439911f827162d277da4432`
  supplies the helper scripts and has identical production Lean sources/pins
  to the measured baseline `4c496959aa1462a6b6a6faf5535ea2a3caf9c119`.
  The after-cleanup source revision is
  `4c2054c47d6c81615f5687fe5ac3f1c4dd1ea1d9`.
- The aborted preliminary BSD-timer run is excluded from this GNU-timer
  baseline and all trend calculations.
- Historical build logs with replayed modules and no useful elapsed timings
  are not clean elaboration baselines.
