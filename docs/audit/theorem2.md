---
title: Theorem 2 audit
---

<!-- Copyright (c) 2026 Free Entropy formalization contributors.
     See LICENSE and NOTICE for license and attribution. -->

# Theorem 2 retrospective semantic audit

**Endpoint:** `FreeEntropy.ExteriorRepresentation.theorem2_cloning_accuracy_choi`, [lean/FreeEntropy/Theorem2Choi.lean:79–96](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/Theorem2Choi.lean#L79-L96). Source: [article.tex:562–580](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L562-L580), `thm:main` / `eq:cloning_trace_bound`.

**Assessment:** No substantive in-domain statement mismatch found. Every endpoint premise is SOURCE, STANDING, or TYPING. The actual representation states, signed auxiliary module, normalized Choi projectors, contractions and half trace norm match the source on the stated domain. This is a retrospective assessment, **not** a claim of satisfying the skill’s new-author freeze/seal workflow. Strict public-carrier, characterization packaging and consumption deviations are recorded below. Fresh compilation and axiom results are recorded in the audit overview.

Repository revision `490356f620c1ab963ff99585d6835c93e4324b37`; article SHA256 `09fc0a6bb205180cd820be94d843a1dc0d4342a543492e30dde54e367ae843a9`; exact statement-before-proof SHA256 `da0d3f67ed3f9cfc8ec632b53c75b6e2e71d7daa4c915c04bc3b311ef2828ad7`. Full file pins are in the JSON. No existing status document was used as proof evidence.

## Source-first reconstruction

Exact target: [article.tex:562–580](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L562-L580), thm:main / eq:cloning_trace_bound.

For each integer d≥2 and density matrix rho on C^d of rank r≤d, whose nonzero eigenvalues form a strictly decreasing list x_1>...>x_r>0, there exists a constant C_{d,x}, independent of rho's eigenbasis and of both partitions, such that for all partitions mu, nu with at most r rows and dominant integral signed difference omega=nu-mu, BOTH half-trace-norm errors of the forward and reverse generalized cloning maps between normalized irrep states are bounded by C_{d,x} D/(b_mu+1). D=sum_i |omega_i|, including negative omega coordinates; b_mu=min_{1≤i≤min(r,d-1)}(mu_i-mu_{i+1}). The same C and same b_mu control both directions. Constant dependence only on d and nonzero spectrum is part of the statement. A density matrix implies trace 1 and positivity, hence r≥1. Partitions are nonnegative weakly decreasing integer rows padded to d entries (299–302). No fixed total box count is required and mu,nu can have different sizes.

Source object definitions: the actual irreducible representation spaces H_mu,H_nu (299–316,322–338), rho_lambda=pi_lambda(rho)/Tr(pi_lambda(rho)) (310–312,476–485); PRV component in H_mu* tensor H_nu has highest weight sorted(nu-mu), multiplicity one (363–400,422–424). Its unique orthogonal projector Pi_omega determines J_omega=(d_mu/d_omega)Pi_omega, and C_mu→nu(sigma)=Tr_mu[J_omega(sigma^T tensor id_nu)] (412–432). Reverse uses swapped pair or equivalent dimension-scaled adjoint (540–551). The Cartan formula uses an isometric irrep intertwiner and does not redefine the representation carrier (442–455). Trace norm means Schatten trace norm; [article.tex:1147–1150](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1147-L1150) distinguishes operator norm from trace norm.

Boundary conventions: d=1 is explicitly outside theorem and separately trivial (581–582); r=1 is allowed; r<d includes supported gap mu_r-0=mu_r (582–583), while r=d takes only d-1 adjacent differences; b_mu=0 is allowed and denominator remains positive. omega=0 is allowed and both actual channels are identity (504,1629–1631). At full rank signed omega may contain negative entries and is a rational GL(d) irrep evaluated on invertible rho; at deficient rank trailing zeros plus dominance force omega to be a partition (402–408). Singular rho is allowed at r<d with polynomial input/output representations. No generic-gap-positive premise, no projector-overlap estimate premise, no abstract state/model premise, and no arbitrary-distance premise appear in the source.

## Quantifier and constant scope

Read outer-to-inner as `∀ d r, ∀ s : FixedSpectrum d r, d≥2 → ∀ mu nu, partition/support/dominance → ∀ U, forward_bound ∧ reverse_bound`. The source asserts a constant depending only on d and the nonzero spectrum; Lean supplies the manuscript proof’s sufficient explicit constant `choose(d,2)+3*choose(r,2)*qx/(1−qx)^(choose(r,2)+1)`. Although no outer existential C is written, the expression is independent of mu, nu and U, and hence enforces the required dependence. Rank is determined by the positive spectrum. Both bounds use the same C and same input gap. Replacing arbitrary rho by U diag(x) U† is the ordinary spectral parameterization; separate exact physical-state identification is documented below.

## Expanded binder table

The two implicit root binders are d and r. There are no instance binders on this export. s and U are replaced by their expanded fields below without double-counting their wrappers. Natural Fin/index/matrix instances are synthesized type infrastructure. STANDING items below are audited directly from the meanings of a rank-r density matrix and an orthonormal eigenbasis, rather than accepted from a preexisting “standing assumptions” file.

| Binder / field | Visibility | Expanded meaning | Bin | Exact source / rationale |
|---|---|---|---|---|
| d | implicit | ℕ | SOURCE | thm:main, 563. Ambient complex dimension; hd enforces d≥2. |
| r | implicit | ℕ | SOURCE | thm:main, 563. Rank; no hidden dependence on rows. |
| s.rank_pos | field of explicit s | 0 < r | STANDING | density matrix in thm:main, 563; trace-one convention. A positive trace-one matrix has at least one nonzero eigenvalue. This standing implication is independently checked mathematically here, not taken from a status file. |
| s.rank_le | field of explicit s | r ≤ d | SOURCE | thm:main, 563. Explicit rank bound. |
| s.eigenvalue | field of explicit s | ℕ → ℝ | SOURCE | thm:main, 563–564. 0-based positive spectrum, extended past r; values beyond d do not enter this theorem. |
| s.positive | field of explicit s | ∀ i, i < r → 0 < eigenvalue i | SOURCE | thm:main, 564. Every active eigenvalue positive. |
| s.decreasing | field of explicit s | ∀ i j, i < j → j < r → eigenvalue j < eigenvalue i | SOURCE | thm:main, 564. Strict order on active spectrum. |
| s.zero_padded | field of explicit s | ∀ i, r ≤ i → i < d → eigenvalue i = 0 | STANDING | thm:main, 563–564; rank-r spectrum convention. Coordinates of a rank-r spectrum padded to ambient d. |
| s.normalized | field of explicit s | ∑ i ∈ Finset.range r, eigenvalue i = 1 | STANDING | density matrix in thm:main, 563; eq:schur_d, 304–316. Trace-one density matrix means positive eigenvalues sum to one; standing meaning audited directly. |
| hd | explicit | 2 ≤ d | SOURCE | thm:main, 563. Exact endpoint convention. |
| mu | explicit | Fin d → ℕ | SOURCE | thm:main, 565; partition convention, 299–302. Nonnegative integer rows, no total box-count restriction. |
| nu | explicit | Fin d → ℕ | SOURCE | thm:main, 565; partition convention, 299–302. Independent target partition. |
| hmu | explicit | ∀ {i j}, i ≤ j → mu j ≤ mu i | SOURCE | thm:main, 565; partition convention, 299–302. Expanded Antitone mu. |
| hnu | explicit | ∀ {i j}, i ≤ j → nu j ≤ nu i | SOURCE | thm:main, 565; partition convention, 299–302. Expanded Antitone nu. |
| hmu_support | explicit | ∀ i : Fin d, r ≤ i.val → mu i = 0 | SOURCE | thm:main, 565. At most r rows. |
| hnu_support | explicit | ∀ i : Fin d, r ≤ i.val → nu i = 0 | SOURCE | thm:main, 565. At most r rows. |
| hinc | explicit | ∀ {i j}, i ≤ j → (nu j : ℝ)−mu j ≤ (nu i : ℝ)−mu i | SOURCE | thm:main, 566; 399–408. Dominant signed integral difference: integrality follows from natural rows; no coordinatewise nu≥mu requirement. |
| U.val | field of explicit U | Matrix (Fin d) (Fin d) ℂ | TYPING | thm:main, 563, normalized irrep states 571; covariance 340–345. Arbitrary choice of eigenbasis. The statement parameterizes all known-spectrum density matrices by U diag(x) U†. |
| U.property.1 | field of explicit U | U† \* U = 1 | STANDING | same eigenbasis convention; Mathlib/Algebra/Star/Unitary.lean:35–36. First unitary relation: semantic eigenbasis convention, independently checked from orthonormal eigenbasis meaning; not pure type formation or a channel/estimate assumption. |
| U.property.2 | field of explicit U | U \* U† = 1 | STANDING | same eigenbasis convention; Mathlib/Algebra/Star/Unitary.lean:35–36. Second unitary relation: semantic eigenbasis convention, independently checked from orthonormal eigenbasis meaning; redundant in finite square dimension but part of standard subtype. |

Counts: SOURCE=14, STANDING=5, TYPING=1, RULED=0, EXCESS=0. **No EXCESS.**

## Definition inventory and separate verdicts

The inventory follows project-owned meanings rather than treating names or codomains as evidence. `SCOPED_PASS` means the body and cited characterization agree on the endpoint’s source domain. A strict global carrier failure is not silently waived: it remains recorded, while its effect on the restricted endpoint is assessed separately. Literal formulas need no ∃! theorem; chosen coordinates are distinct from uniquely defined source projectors.

### `FixedSpectrum`

[lean/FreeEntropy/Statements.lean:25–32](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/Statements.lean#L25-L32). Source: thm:main 563–564.

Seven fields exactly expanded in binder table.

Fields normalize and strictly order first r eigenvalues; no theorem-shaped premise bundle.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `FixedSpectrum.adjacentRatio`, `FixedSpectrum.qx`

[lean/FreeEntropy/SpectrumBounds.lean:28–34](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/SpectrumBounds.lean#L28-L34). Source: lem:sector_gap 901–909.

q_i=x_(i+1)/x_i for i+1<r, otherwise zero; maximum over i<r.

adjacentRatio_nonneg/lt_one 36–49; qx_nonneg/lt_one 51–56; qx_rank_one 77–78. Zero is explicit source convention, not a fallback concealing missing proof.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `differenceNorm`

[lean/FreeEntropy/CanonicalRowBounds.lean:17–44](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalRowBounds.lean#L17-L44). Source: thm:main 568.

Σ_i Int.natAbs((nu_i:ℤ)−(mu_i:ℤ)); real cast equals Σ|nu_i−mu_i|.

differenceNorm_cast 20–27 and zero iff 29–41. Signed difference is preserved.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `supportedGapIndices`, `minimumRowGap`

[lean/FreeEntropy/CanonicalRowBounds.lean:46–80](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalRowBounds.lean#L46-L80). Source: thm:main 569, 582–583.

Minimum of mu_j−mu_(j+1) for j<d−1 and j<r, using nonempty finite infimum.

Nonempty proved from d≥2,r>0; natural subtraction agrees with integer difference under hmu (64–69); universal lower-bound characterization 72–80.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: FAIL strict source-only carrier <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS; STRICT_GLOBAL_FAIL

Carrier limitation: mu argument is not restricted to Antitone in the helper itself; natural subtraction on nonpartitions is a total extension not source b_mu.

### `MeanDepth.meanDepthConstant`

[lean/FreeEntropy/MeanDepth.lean:24–35](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/MeanDepth.lean#L24-L35). Source: lem:tail 1512–1513.

N*q/(1−q)^(N+1).

Formula literal; N=0 produces 0; used with 0≤q<1.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `Theorem2.cloningConstant`

[lean/FreeEntropy/Theorem2.lean:27–35](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/Theorem2.lean#L27-L35). Source: proof of thm:main 1824–1826.

choose(d,2)+3*meanDepthConstant(choose(r,2),q).

Exactly a sufficient constant given by manuscript proof; fixed before mu,nu,U. Nonnegativity follows from spectrum q bounds.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `OrbitMemory.tr`

[lean/FreeEntropy/OrbitMemory.lean:36–37](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/OrbitMemory.lean#L36-L37). Source: trace norm convention 1147–1150.

Real part of matrix trace.

On positive/Hermitian matrices imaginary part of trace is zero.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `TraceDistance.traceNorm`, `TraceDistance.traceDistance`

[lean/FreeEntropy/TraceDistance.lean:31–35](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/TraceDistance.lean#L31-L35). Source: eq:cloning_trace_bound 575–578; 1147–1150.

Re Tr sqrt(X†X); error is traceNorm(A−B)/2.

Mathlib Analysis/SpecialFunctions/ContinuousFunctionalCalculus/Abs.lean:46 defines CFC.abs a = sqrt(star a*a). Eigenvalue characterization for Hermitian difference 56–64; this is not an arbitrary norm parameter.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `Column`, `columnHeight`

[lean/FreeEntropy/ExteriorDominant.lean:18–25](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/ExteriorDominant.lean#L18-L25). Source: partition representation 299–302; 322–328.

Column index Fin(Σ rows); height counts i with column<mu_i. Zero-height columns are trivial factors.

tensorFirst_weight 59–80 proves actual highest row when hmu.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: FAIL strict source-only carrier <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS; STRICT_GLOBAL_FAIL

Carrier limitation: Non-antitone row functions are accepted and effectively sorted by column heights; no source highest-weight identity asserted without hmu.

### `Index`, `wedgeBasis`, `exteriorMatrix`

[lean/FreeEntropy/ExteriorRepresentation.lean:21–32](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/ExteriorRepresentation.lean#L21-L32). Source: actual polynomial irreps 299–302; 322–328.

Actual kth exterior power, basis indexed by k-subsets; matrix of exteriorPower.map.

exteriorMatrix_mul/adjoint/unitary 34–79; minors formula 48–59 identifies ordinary exterior representation.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `productMatrix`, `tensorMatrix`, `tensorRepresentation`

[lean/FreeEntropy/ExteriorTensor.lean:21–22](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/ExteriorTensor.lean#L21-L22), 81–102`. Source: actual polynomial irreps 299–302; 322–328.

Product of exterior representation matrices over Young-diagram columns.

Matrix multiplication, adjoint, unitary laws are proved; source carrier is actual exterior tensor construction.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `AmbientIndex`, `ambientRepresentation`, `highestBasisIndex`, `highestVector`, `highestSubspace`

[lean/FreeEntropy/ExteriorHighestRepresentation.lean:22–46](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/ExteriorHighestRepresentation.lean#L22-L46). Source: highest-weight irreps 299–302; 322–338.

Cyclic subspace generated by the tensor of first-basis exterior highest vectors.

highestSubspace_irreducible 36–45; actual torus weight equals mu under hmu 47–58; vector nonzero 60–61.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `IrrepIndex`, `irrepEmbedding`, `irrepMatrix`

[lean/FreeEntropy/ExteriorMatrixIrreducible.lean:20–51](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/ExteriorMatrixIrreducible.lean#L20-L51). Source: H_mu and d_mu, 299–302.

Fin(finrank highestSubspace); actual restricted unitary representation in an orthonormal basis.

Positive dimension 29–30, intertwining 35–38, irreducibility 40–43, unitarity 45–48, continuity 50–52.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: FAIL strict source-only carrier <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS; STRICT_GLOBAL_FAIL

Carrier limitation: IrrepIndex is exported for arbitrary natural row functions; source interpretation as the irrep of that row requires hmu.

### `WeightCoordinates`, `Generators.weightCoordinates`

[lean/FreeEntropy/LieWeightModel.lean:19–88](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/LieWeightModel.lean#L19-L88). Source: representation coordinate convention 299–302, 340–345.

Model plus change-of-basis matrix with isometry and exact generator conjugation. Chosen from proved existence.

exists_weightCoordinates builds every field using joint eigenbasis, actual highest vector/cyclicity and root cone (27–83); coordinate choice is not an endpoint binder.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `CyclicWeightModel`

[lean/FreeEntropy/CartanLieCloning.lean:81–92](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CartanLieCloning.lean#L81-L92). Source: highest-weight representation conventions 322–338; weight notation 1144 onwards.

Generators; row; weights; highest column; diagonal law; highest eigenvalue law; raising annihilation; cyclicity; dominance; integer root coefficients; exact root-cone equation.

All fields supplied by canonicalWeightCoordinates, not assumed at endpoint; expanded field inventory below.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `Generators`

[lean/FreeEntropy/LieMatrixCasimir.lean:34–39](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/LieMatrixCasimir.lean#L34-L39). Source: GL(d) representation 322–338.

Matrix gl(d) generators with E_ij†=E_ji and actual gl(d) commutator relations.

Fundamental and exterior/tensor generators are literal matrix constructions, then restricted to actual irrep; not a synthetic labeled representation.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `canonicalWeightCoordinates`, `canonicalWeightModel`, `canonicalWeightEmbedding`

[lean/FreeEntropy/ExteriorWeightCoordinates.lean:26–58](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/ExteriorWeightCoordinates.lean#L26-L58). Source: actual H_mu and representation, 299–302; 322–338.

Apply constructed weightCoordinates to irrepGenerators; model projection; embedding irrepEmbedding times coordinate unitary.

canonicalWeightModel_row 61–88 identifies highest row under hmu; exact embedding generator equation 48–58.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `canonicalWeight`

[lean/FreeEntropy/ExteriorWeightCoordinates.lean:111–127](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/ExteriorWeightCoordinates.lean#L111-L127). Source: weights of polynomial irrep, 299–302.

Select nonzero ambient embedding coordinate, take its natural occupation.

canonicalWeight_spec fixes selected value independently (115–117), supported embedding 119–127; total degree correct under hmu 130–132.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `rootWeightMonomial`, `CyclicWeightModel.relativeWeight`, `relativeNormalizer`, `relativeState`

[lean/FreeEntropy/CyclicWeightStates.lean:21–33](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CyclicWeightStates.lean#L21-L33). Source: rho_mu definition 310–312, 476–485; source weight states in sec:prelim.

Product of adjacent ratios raised to integer simple-root deficits; finite sum normalizer; diagonal normalized weights.

Highest coefficient is 1 (95–98), normalizer ≥1 for nonnegative ratios (100–105). Physical monomial equality proved in CanonicalMonomialState169–186.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: FAIL strict source-only carrier <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS; STRICT_GLOBAL_FAIL

Carrier limitation: relativeState accepts arbitrary real ratios, and canonical specialization accepts unsupported/nonpartition rows. State interpretation only on appropriate nonnegative/source domain.

### `canonicalWeightRepresentation`

[lean/FreeEntropy/CanonicalOrbit.lean:23–39](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalOrbit.lean#L23-L39). Source: unitary action 340–345.

Conjugate actual irrepMatrix by chosen weight-coordinate unitary.

Unitarity, continuity, irreducibility proved 28–39; UnitaryCoordinates17–23 gives exact W†R(U)W.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `canonicalOrbitState`

[lean/FreeEntropy/CanonicalOrbit.lean:41–45](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalOrbit.lean#L41-L45). Source: normalized irrep states thm:main571; rho_mu310–312,476–485.

R_mu(U)*relativeState(x ratios)*R_mu(U)†.

Positive and trace-one 47–64; exact physical source identification PhysicalOrbitChannels23–32 using hmu,hsupp.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: FAIL strict source-only carrier <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS; STRICT_GLOBAL_FAIL

Carrier limitation: Public helper admits partitions longer than rank and nonpartitions. For e.g. r=1,d=2, mu=(1,1), physical determinant block vanishes, source normalized state is undefined, but relative construction returns a normalized 1D state.

### `canonicalTensorSource`, `canonicalTensorState`

[lean/FreeEntropy/PhysicalCanonicalSector.lean:112–120](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/PhysicalCanonicalSector.lean#L112-L120). Source: eq:schur_d304–312; normalized representation state476–485.

Compress rho tensor-power by actual irrep tensor isometry; normalize block.

canonicalWeightTensorState-diagonal-orbit bridge CanonicalPhysicalOrbit60–75; positive monomial cancels in source domain.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: FAIL strict source-only carrier <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS; STRICT_GLOBAL_FAIL

Carrier limitation: canonicalTensorState uses normalizedBlock zero-trace fallback; not itself a source-only definition.

### `normalizedBlock`

[lean/FreeEntropy/SchurWeylNormalization.lean:28–30](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/SchurWeylNormalization.lean#L28-L30). Source: normalized rho_mu310–312,476–485.

If real trace zero use maximally mixed; else trace inverse times block.

On source-supported rows nonzero trace follows highest_monomial_pos and normalizer≥1; CanonicalMonomialState142–186 selects nonzero branch.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: FAIL strict source-only carrier <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS; STRICT_GLOBAL_FAIL

Carrier limitation: Zero-trace maximally mixed output is totalization, not source normalization. Strict checklist forbids admitting it globally as source object.

### `auxiliaryShift`, `auxiliaryRow`

[lean/FreeEntropy/SignedAuxiliaryModel.lean:18–45](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/SignedAuxiliaryModel.lean#L18-L45). Source: signed omega and determinant twists330–338,402–408.

shift=Σmu; auxiliaryRow_i=nu_i+(shift−mu_i), exactly nu_i−mu_i+shift.

le_auxiliaryShift ensures Nat subtraction never truncates; auxiliaryRow_antitone31–37, balance40–45.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `canonicalAuxiliaryModel`

[lean/FreeEntropy/SignedAuxiliaryModel.lean:51–75](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/SignedAuxiliaryModel.lean#L51-L75). Source: rational auxiliary representation330–338,402–408.

Actual polynomial model of shifted omega, then subtract same scalar from every generator diagonal/weight.

row exactly signed nu−mu55–63; exact sum row67–75. Representation dimensions unaffected by determinant twist; no requirement nu≥mu.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `CyclicWeightModel.shift`

[lean/FreeEntropy/CyclicWeightShift.lean:19–45](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CyclicWeightShift.lean#L19-L45). Source: determinant twist330–338.

Generator scalar shift; row and every weight shifted by c; same highest vector/root coefficients.

All commutator/cyclicity/weight laws proved. Used c=−sum mu (integer), though generic helper supports real Lie shifts.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `specifiedTopUnitary`, `specifiedCartanEmbedding`

[lean/FreeEntropy/SpecifiedLieCloning.lean:24–79](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/SpecifiedLieCloning.lean#L24-L79). Source: Cartan intertwiner prop:choi442–455.

Choose proved unitary intertwiner to constructed Cartan top, compose its adjoint with top embedding.

Exists theorem24–39; chosen W spec45–51; V isometry58–67 and intertwinement76–83. Uniqueness up to scalar supplied by CartanHomMultiplicity87–125, not an endpoint premise.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `CartanChoi.choi`, `CartanChoi.choiMap`

[lean/FreeEntropy/CartanChoi.lean:21–27](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CartanChoi.lean#L21-L27). Source: eq:gen_cloner414–418.

Unnormalized Choi on input-dual×output; sum X_aa′J_(a,c),(a′,c′).

choiMap_sectorMap36–58; literal transpose/partial trace identity ChoiContraction21–32.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `CartanChoi.projector`, `CartanChoi.embedding`

[lean/FreeEntropy/CartanChoi.lean:103–105](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CartanChoi.lean#L103-L105),140–142`. Source: Pi_omega multiplicity-one source390–424; prop:choi442–455.

Projector=(dim omega/dim nu)*reshuffle(V)†reshuffle(V); embedding=sqrt(dim omega/dim nu)*reshuffle(V)†.

Isometry/intertwinement144–172; idempotence114–128; Gram scalar derived via actual irreducible commutant77–101. Not merely an arbitrary projector.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `canonicalChoiProjector`, `canonicalChoiEmbedding`

[lean/FreeEntropy/CanonicalChoi.lean:24–33](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalChoi.lean#L24-L33). Source: eq:gen_cloner413–424.

Instantiate CartanChoi projector with actual canonical signed auxiliary and Cartan isometry.

Isometry36–41, intertwines43–49, Hermitian/idempotent57–67, rank70–75, multiplicity-one79–87, highest90–121, cyclic/range124–159; complete source-defining properties split over proved theorems.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `flipConjugate`, `reverseEmbedding`, `reverseProjector`

[lean/FreeEntropy/ReverseChoi.lean:20–30](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/ReverseChoi.lean#L20-L30). Source: reverse prop540–551; general PRV395–398.

Conjugate entries and swap tensor factors.

Reverse range/isometry32–50; idempotence62–69; Choi reverse normalization86–96.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `canonicalReverseChoiProjector`, `canonicalReverseChoiEmbedding`

[lean/FreeEntropy/CanonicalReverseChoi.lean:22–32](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalReverseChoi.lean#L22-L32). Source: reverse prop540–551; PRV395–398.

Reverse support from same canonical Cartan isometry.

Hermitian/idempotent/rank47–66; ReverseChoiRepresentation92–108 highest row (mu−nu)∘reverse and cyclic range; ReverseChoiMultiplicity147–185 multiplicity and uniqueness.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `partialTraceInput`

[lean/FreeEntropy/ChoiContraction.lean:17–18](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/ChoiContraction.lean#L17-L18). Source: eq:gen_cloner416–418.

Y↦[Σ_a Y_(a,c),(a,c′)]_(c,c′).

choiMap_eq_partialTraceInput21–32 proves exact product ordering and ordinary transpose, for all matrices.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `prvForward`, `prvReverse`

[lean/FreeEntropy/Theorem2Choi.lean:25–32](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/Theorem2Choi.lean#L25-L32),44–51`. Source: eq:gen_cloner414–418; reverse540–551.

Partial trace of normalized PRV projector times X^T⊗I, with input dimension numerator and auxiliary dimension denominator.

prvForward_eq36–41 and prvReverse_eq53–58; prv_maps_are_channels62–73. Equalities valid on ALL matrices and include mu=nu.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `canonicalForward`, `canonicalReverse`

[lean/FreeEntropy/CanonicalFullCloning.lean:27–39](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalFullCloning.lean#L27-L39). Source: identity504,1629–1631; prop:choi442–455.

Identity at equal rows, otherwise actual Cartan channel.

CanonicalCloningSelf99–151 proves Cartan formula identity at equal rows and exact equality of branchwise channel to Cartan on all matrices. Thus this branch does not invent off-source behavior.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `specifiedForward`, `specifiedReverse`

[lean/FreeEntropy/SpecifiedCloningChannels.lean:21–33](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/SpecifiedCloningChannels.lean#L21-L33). Source: prop:choi450–455; reverse540–551,1760–1764.

Forward=(dim mu/dim nu)V†(X⊗I)V; reverse=Tr_aux(VYV†), supplied as actual CPTP maps.

Balance proved via actual cyclic weights, isometry/intertwining; MatrixChannel fields constructed, never endpoint input.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `Channels.MatrixChannel`, `krausMap`, `amplify`

[lean/FreeEntropy/Channels.lean:39–41](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/Channels.lean#L39-L41),73–76,95–102`. Source: channel premise/definition340–345,426–432.

Complex-linear map, exact trace preserving, positive, every finite matrix amplification positive; Kraus sum and block amplification literal.

All channel laws proved by specifiedForward/Reverse; only used internally and existential channel conclusion, not as a root binder.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `TensorIndex`, `tensorWeight`, `tensorFirst`

[lean/FreeEntropy/ExteriorWeights.lean:137–141](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/ExteriorWeights.lean#L137-L141). Source: partition irreps299–302.

Dependent product of actual exterior-power indices; occupations sum across columns; first subsets define highest tensor.

tensorFirst_weight identifies exact partition row under antitone; no dummy one-dimensional carrier.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `cyclicSubspace`

[lean/FreeEntropy/CyclicHighestRepresentation.lean:20–22](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CyclicHighestRepresentation.lean#L20-L22). Source: irreducible highest-weight module322–338.

Complex span of the actual group orbit of v.

highestSubspace uses this literal span, then proves it irreducible; no arbitrary codomain inhabitant.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `embedding`, `restrictedMatrix`

[lean/FreeEntropy/UnitaryDecompositionMatrices.lean:22–23](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/UnitaryDecompositionMatrices.lean#L22-L23),90–98`. Source: coordinate realization of H_mu299–302.

Embedding columns are an actual stdOrthonormalBasis of subspace; restricted action is E†U(g)E.

embedding_isometry25–29 and embedding_projection47 onwards identify exact Hilbert projection; restrictedMatrix uses proved invariance.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `irrepGenerators`

[lean/FreeEntropy/ExteriorPhysicalIrrep.lean:63–78](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/ExteriorPhysicalIrrep.lean#L63-L78). Source: GL(d) module322–338.

Physical tensor Lie action restricted by actual irrepTensorEmbedding.

Intertwining67–71 and cyclicSpan top74–78 proved from actual representation irreducibility.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `Generators.dual`

[lean/FreeEntropy/LieDual.lean:15–26](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/LieDual.lean#L15-L26). Source: dual highest weights393–398; dual-source Choi363–366.

Generator E_ij maps to minus its ordinary transpose.

Actual gl(d) contragredient action with adjoint and commutator laws proved.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

### `constructedTensorDecomposition`

[lean/FreeEntropy/ConstructedTensorDecomposition.lean:21–57](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/ConstructedTensorDecomposition.lean#L21-L57). Source: Cartan component442–449; multiplicity390–398.

Full actual constituent decomposition with isometries, resolution and intertwinement; choose a proved top constituent and prove uniqueTop.

Top existence21–25; uniqueTop39–51 uses orthogonality and top-vector uniqueness; root coefficients52–57 from proved tensor cone. No extra top-existence assumption survives.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: OK on source domain <br>
CHARACTERIZATION: OK via cited existing theorems; strict workflow caveats below <br>
CHOICE_INDEPENDENCE: See choice inventory; no mathematical ambiguity found on source domain <br>
DEFINITION_VERDICT: SCOPED_PASS

### `reshuffle`, `unreshuffle`

[lean/FreeEntropy/CartanReshuffle.lean:20–27](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CartanReshuffle.lean#L20-L27). Source: Choi/Cartan equivalence442–455.

Reshuffle(V)_(b,(a,c))=V_((a,b),c), without conjugation; inverse exact.

Conjugation occurs later in Gram matrix, so Choi transpose orientation is correct; inverses rfl26–27.

BODY_MATCH: OK on endpoint source domain <br>
PUBLIC_CARRIER: OK <br>
WELL_DEFINEDNESS: N/A_LITERAL <br>
CHARACTERIZATION: N/A_LITERAL <br>
CHOICE_INDEPENDENCE: N/A <br>
DEFINITION_VERDICT: SCOPED_PASS

## Expanded internal bundles

`CyclicWeightModel` contains generators (including actual adjoint and gl(d) commutator laws), row, weight, highest column, diagonal generator identity, highest-vector eigenvalue identity, raising annihilation, cyclicity, dominance, natural root coefficients, and exact root-cone identity ([CartanLieCloning.lean:81–92](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CartanLieCloning.lean#L81-L92); [LieMatrixCasimir.lean:34–39](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/LieMatrixCasimir.lean#L34-L39)). `WeightCoordinates` adds a unitary matrix, isometry and generator conjugation ([LieWeightModel.lean:19–23](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/LieWeightModel.lean#L19-L23)). `MatrixChannel` contains a matrix function, additive and complex-homogeneous laws, exact trace preservation, positivity and positivity after every finite ancilla amplification ([Channels.lean:95–102](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/Channels.lean#L95-L102)).

None is a root premise. `canonicalWeightModel` uses an actual exterior representation and constructs every model field. `specifiedForward`/`specifiedReverse` construct all channel laws from actual Cartan geometry. These producers matter: the same bundles would be EXCESS if left as assumptions of the root.

## Actual premise discharge

| Consumption step | Exact proof locator | Supplied terms |
|---|---|---|
| Endpoint | [Theorem2Choi.lean:94–96](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/Theorem2Choi.lean#L94-L96) | prvForward_eq and prvReverse_eq require 0<d, discharged from hd by omega; then exact theorem2_cloning_accuracy with every root premise. |
| Orbit to diagonal errors | [Theorem2Canonical.lean:65–68](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/Theorem2Canonical.lean#L65-L68); [CanonicalCloningOrbit.lean:52–79](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalCloningOrbit.lean#L52-L79) | Actual proved covariance and unitary trace-distance invariance; row-support premises derive equality nu_i=mu_i=0 beyond r. |
| Exact row quantities | [CanonicalFullCloning.lean:109–111](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalFullCloning.lean#L109-L111) | D=differenceNorm, g=b=minimumRowGap; nonnegativity from Nat, hbg reflexive; hDnorm=differenceNorm_cast; hgap=minimumRowGap_cast_le. No scalar estimates remain assumptions. |
| Zero difference | [CanonicalFullCloning.lean:71–81](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalFullCloning.lean#L71-L81); [CanonicalCloningSelf.lean:99–151](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalCloningSelf.lean#L99-L151) | Equal rows uses identity with nonnegative bound; unequal rows proves 1≤D from integer L1. Cartan identity equivalence is separately proved and used in Choi equality, so zero is not a patched non-source channel. |
| Rank split | [CanonicalFullCloning.lean:83–90](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalFullCloning.lean#L83-L90); [CanonicalCloningBounds.lean:16–21](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalCloningBounds.lean#L16-L21) | r=1 uses actual ambient count theorem and qx=0 makes K=0; r≠1 gives r≥2 from rank_pos. Exact constant then reduced back to rank r. |
| Auxiliary | [CanonicalCloning.lean:54–55](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalCloning.lean#L54-L55); [SignedAuxiliaryModel.lean:51–75](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/SignedAuxiliaryModel.lean#L51-L75) | Concrete shifted exterior auxiliary replaces CyclicWeightModel witness; exact signed highest-weight addition proved from row dominance. |
| Mixture and normalization | [CanonicalCloningCore.lean:56–76](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalCloningCore.lean#L56-L76),102–112 | Offsets are union of finite actual supports filtered to rank; unsupported spectral ratios zero; mixture_eq_relativeState and state trace give exact normalization; ofSpecifiedCyclicWeights supplies projector geometry. |
| Multiplicity and finite estimates | [CanonicalCloningCore.lean:96–140](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalCloningCore.lean#L96-L140) | Shallow multiplicities from canonical_offsetMultiplicity_shallow_eq; monotonicity from weight_multiplicity_add_le; decay from relativeCoefficient_envelope; depth counts from canonical_offsetMultiplicity_rank_depth_le; dimensions and deficit from canonical_dimensionRatio_\*. |
| Finite scalar reduction | [Theorem2.lean:68–76](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/Theorem2.lean#L68-L76) | Mean depth derived from actual spectral envelopes and multiplicity counts; applies finite-block cloning theorem. These internal hypotheses are produced before use and are absent from exported root. |
| Literal Choi maps are channels | [Theorem2Choi.lean:69–73](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/Theorem2Choi.lean#L69-L73); [CanonicalChoi.lean:162–192](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalChoi.lean#L162-L192); [CanonicalReverseChoi.lean:81–106](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/lean/FreeEntropy/CanonicalReverseChoi.lean#L81-L106) | Exhibits canonicalForward/Reverse and exact all-matrices function equality; Choi normalization is dimensions of actual constructed spaces. |

The independently generated probe expands half trace norm, the manuscript sufficient constant and signed integer L1 sum, and applies the root by `exact`. A second exact application obtains actual CPTP channels for the literal contractions. A third anonymous theorem replaces both orbit states by the actual normalized physical tensor restrictions and explicitly rewrites both source-characterization bridges before applying the endpoint. File: `metadata/statement-audit/probes.json (theorem2)`. All three applications subsequently compiled successfully; the separate integration record contains the axiom checks.

## Choices and uniqueness

- **Orthonormal coordinate bases / irrepEmbedding / canonicalWeightCoordinates:** Actual finite-dimensional subspace basis and exists_weightCoordinates.some. Source representation is defined up to unitary coordinates. Proved conjugation intertwines representation and state; literal state bridge holds for selected coordinates. No arbitrary representation witness input. Not a unique coordinate object and should not be sold as one.
- **canonicalWeight:** Choose nonzero ambient coordinate. canonicalWeightEmbedding_weight and canonicalWeight_spec make its value the actual coordinate weight, independent of which nonzero ambient entry is selected.
- **weightCoeff:** Choose c in root cone during exists_weightCoordinates. Exact row−weight=offset(c); root offset is injective and coefficient identities are proved. Choice is constrained to actual weight differences, not an arbitrary family.
- **specifiedTopUnitary / specifiedCartanEmbedding:** Classical choice from proved existence of actual highest-weight unitary. CartanHomMultiplicity.tensor_intertwiner_scalar gives scalar freedom only; isometry makes modulus one, so projector/conjugation maps are invariant. Reverse projector uniqueness explicitly proves scalar cancellation. Strict separately packaged forward ∃! not identified.
- **PRV projector:** Explicit normalized Gram matrix of reshuffled specified Cartan embedding. Hermitian/idempotent, isometric auxiliary range, actual highest weight and cyclicity, one-dimensional Hom space; reverse full projector uniqueness exported. Not chosen from mere existence of arbitrary projector.

## Boundary cases

| Case | Assessment |
|---|---|
| d=0 or d=1 | Excluded by hd; d=1 separately trivial in source581–582. minimum uses no invented empty minimum. |
| r=0 | Excluded by FixedSpectrum.rank_pos, consequence of density normalization. |
| r=1 | qx=0, N=0, C=choose(d,2); supported gap mu_0−mu_1=mu_0; no active spectral-ratio division. Both bounds hold; manuscript proof sharper reverse zero is not itself a theorem2 conclusion. |
| r=d | Support premises vacuous; gap only d−1 adjacent pairs; signed differences may have negative entries. |
| 1≤r<d | Gap filter includes j=r−1 and mu_r=0, hence final supported row gap; omega trailing zeros and dominance force omega nonnegative. |
| D=0 / mu=nu | Both literal Choi maps equal identity, bound zero, checked by exact Cartan/self equivalence. |
| D>0 | Integrality gives D≥1 in proof; no D≥1 endpoint binder. |
| b_mu=0 | Allowed; denominator=1, no gap positivity assumption. |
| mu or nu zero partition | Allowed, actual irrep dimension positive (=1 mathematically); normalized state defined since top monomial=1. Dominance constrains which zero/nonzero pair combinations occur. |
| Negative determinant shift | Allowed at full rank; auxiliaryRow is polynomial realization plus generator twist; norm counts absolute signed differences. At deficient rank such negative dominant difference is impossible from support. |
| Eigenvalues collide or go to zero | Equality/collision inside positive spectrum excluded; rank-deficient spectra allowed via finite rank. No uniform-in-spectrum constant claim; qx→1 may blow up C as allowed. |
| Natural-number subtraction | differenceNorm casts before subtraction to ℤ; only gap uses Nat subtraction, justified by antitone. auxiliaryShift−mu_i nontruncated by summand≤sum. |
| Eigenvalue function beyond d | Unconstrained values never read in qx, normalized state or theorem conclusion. They add representation redundancy, not mathematical dependence. |
| Choice of eigenbasis | ∀U including all phases/degenerate zero-support basis choices. C independent of U and rows; arbitrary source density recovered by spectral diagonalization, not an extra estimate premise. |
| General non-Cartan irreps | The general source cloner definition includes atypical pairs, but thm:main explicitly restricts dominant difference. prvForward/Reverse only target this theorem domain; no claim of formalizing general non-Cartan definition. |
| Zero auxiliary dimension | Impossible: IrrepIndex dimension positivity proved; denominator does not silently use division by zero. |
| Off-source unsupported partition | Not an endpoint case: rejected by hmu_support/hnu_support. Public canonicalOrbitState total extension is not asserted to be physical normalized state there. |

## Findings, limitations and uncertainties

### T2-F01 — Source-correct endpoint uses total helper carriers

canonicalOrbitState, IrrepIndex, relativeState and minimumRowGap have larger public carriers than source definitions. Source restrictions are exactly d≥2, spectrum positive/ordered/normalized with 1≤r≤d, mu/nu antitone and zero outside rank. Root endpoint supplies these. normalizedBlock additionally has a zero-trace maximally-mixed fallback in a physical identification helper. This violates the strict skill public-carrier/no-fallback sealing test if those globally exported helpers are admitted as literal source objects. It is not a counterexample to the restricted theorem.

**Effect:** No in-domain discrepancy found; strict global definition seal withheld.

### T2-F02 — Physical-state characterization proved separately but not consumed by endpoint proof

PhysicalOrbitChannels.canonicalWeightTensorState_eq_orbit23–32 proves exact source-state identification from hmu and hsupp, using monomial normalizer positivity. Theorem2Choi proof rewrites Choi formulas and invokes Theorem2Canonical; that proof reduces orbit errors to relative states. Neither proof explicitly applies the physical-state characterization. A strict characterization-consumption workflow therefore is not satisfied by the selected root alone; existence of this real bridge establishes mathematical identification on its source domain, not its term-level use by that root. The new transient audit probe explicitly composes both bridge instances with the root to obtain the physical normalized-state formulation; this composition subsequently compiled successfully.

**Effect:** Representation-coordinate formulation mathematically matches source on restrictions; no claim that root proof consumes separate physical bridge.

### T2-F03 — PRV meaning established through split construction and Hom-space results, without frozen paired ∃! anchor

Forward projector has isometry, range, highest weight and multiplicity-one results; any intertwiner is scalar by CartanChoiMultiplicity.dual_embedding_scalar96–105. Reverse has explicit canonicalReverseChoiProjector_unique173–185. These establish the mathematical component and eliminate arbitrary component selection. Source projector is unique; the skill requires a separately frozen exact ∃! plus paired characterization and consumer dependency. No such versioned pair is identified, and forward exact projector uniqueness is not exported under an analogous unique theorem in inspected source. Do not label this repository as satisfying that fresh-author-seal workflow.

**Effect:** No substantive projector mismatch found; strict characterization/choice-independence packaging not certified.

### T2-F04 — Comparator fixture shares the deepest source-facing definitions

Fixture independently redeclares prvForward, prvReverse and the theorem. All three are literally identical to solution at audit time. It imports actual canonical representation/state/PRV definition modules, so it is not an independent mathematical audit of those semantics. JSON permits only propext, Quot.sound, Classical.choice and disables Nanoda. Existing verification status files were not used as evidence.

**Effect:** Useful exact expected-statement comparison, not a substitute for this semantic reconstruction.

### T2-F05 — Retrospective audit is not an author-approved freeze/seal

Source and selected declaration bytes are pinned by this report. No source-facing versioned declaration manifest, author ruling, paired characterization manifest or approved draft baseline was found. lake-manifest.json is a dependency lock, not that workflow manifest. No new sorry, reorganization, or author-endorsement claim is made.

**Effect:** Strict manifest/seal test N/A retrospective; no author approval inferred.

## Comparator fixture

Direct textual comparison on current bytes found the two Choi definitions and the entire theorem declaration before its proof identical between solution and fixture. The fixture proof is its deliberate `sorry`, not imported by the production endpoint. JSON targets the exact export and allows only `propext`, `Quot.sound`, `Classical.choice`; Nanoda is disabled there. This is a scoped statement/axiom fixture. It shares representation, normalized-state and PRV definition modules, so independently reconstructing those meanings was necessary. Comparison evidence: `theorem2-literal-comparison.json`.

## Verification boundary

Source and target identities are pinned. Source reconstruction predates Lean inspection. Selected semantic closure and actual producer-to-consumer proof assembly were read. No broad build or repository edit was performed by this reviewer. The integration runner subsequently compiled all three applications and checked the endpoint and bridge axiom reports successfully. Full author-approved manifest/seal status is not claimed. Uncertainties are workflow/coverage limits and the separately proved but unconsumed physical characterization, not an identified false source-domain mathematical assertion.


## Audit records

See [[audit|the audit overview and reproducer]] and the [machine-readable review](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/statement-audit/theorem2.json). The [fresh Lean check record](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/statement-audit/checks.json) records the final compilation status; the original structured review also preserves the reviewers’ pre-compilation status for provenance.
