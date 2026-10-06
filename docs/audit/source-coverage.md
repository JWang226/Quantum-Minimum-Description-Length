---
title: Manuscript argument inventory
---

<!-- Copyright (c) 2026 Free Entropy formalization contributors.
     See LICENSE and NOTICE for license and attribution. -->

# Article source coverage and argument inventory

Retrospective source-first argument inventory for Article Theorem 1 achievability and average/uniform converse and Article Theorem 2 original PRV Choi-cloner accuracy.

Adapted inventory, direct-use edges, external boundaries and explicit source-gap principles from build-proof-dependency-graph. This is not the skill author-freeze workflow: no new frozen anchors, declaration files, manifest, draft sorry, author approval, or Lean certification is asserted.

**Scope limit:** All recognizable theorem-like environments, proof environments, labels, citation commands and cross-reference commands in raw Article source. Manual proof/prose regions cover substantive selected arguments at a finite coarse granularity; no claim of exhaustive extraction of every unnamed mathematical fact or of external literature.

**This is source topology, not Lean proof status.** Records retain PROPOSED status after a bounded independent adversarial review; no exhaustive node-by-node topology seal is claimed. Metadata contributes navigation links only.

## Source identity

| File | SHA-256 | Lines | Mathematical scope |
|---|---|---:|---|
| article.tex | `09fc0a6bb205180cd820be94d843a1dc0d4342a543492e30dde54e367ae843a9` | 2268 | Primary mathematical audit corpus for named Article roots and their source argument closure. |
| letter.tex | `0b6a2c45b1565c3e9aadcdaa1c6631a2d7e2e2ec259b7382d04bcbce83622260` | 443 | Companion free-entropy/geometric statements concern a different mathematical claim family; hashed for source identity only, not audited as part of Article compression/cloning roots. |

## Counts and root boundaries

75 nodes; 137 edges between grouped source results and proof steps; 407 inventory entries (255 mapped, 152 excluded). 14 explicit external inputs. No global standing-assumption leaves. No alternative proof routes.

Root closure sizes: thm:qmdl: 75, thm:main: 47.

Unreachable nodes: none.

The endpoint split is achievability (`thm:achievability`), Haar-average converse (`thm:converse`), uniform converse (`thm:qmdl#uniform-converse`), and original Choi-channel accuracy (`thm:main`). `prop:choi` is a supporting proposition.

## Source questions and limitations

- Three SOURCE_GAP notes identify uncited/unproved standard representation-theory inputs (Cartan-duality, GT counting, Casimir eigenvalue). They do not by themselves establish a false manuscript claim or a missing Lean proof.
- Weyl asymptotic lemma does not spell out dependence on constants in lambda_i=nx_i+O(sqrt n zeta_n); source applications use a fixed uniform target/typical sequence. No stronger uniformity is inferred.
- No genuinely alternative proof of a selected root is offered by this source. The reverse-channel proposition groups the scaled-adjoint and Petz identities. The cloning error argument uses the scaled-adjoint conclusion; the grouped source closure includes Petz, but it is not an indispensable premise of that error estimate. YCH and the diagram are excluded illustrative/repeated arguments.
- Article Theorem 2 is thm:main (cloning accuracy). prop:choi is the supporting Cartan intertwiner proposition, not Theorem 2 itself.
- Manual regions are finite coarse slices and may include routine algebra and unexpanded standard functional-analysis facts. Mechanical coverage checks cannot establish mathematical completeness.
- Nodes and inventory remain proposed records. The independent review checks important boundaries and extraction counts; stronger node-by-node topology claims require additional review.

## Conventions

- All logarithms base two; memory is log dimension rather than rounded physical-qubit count. ([article.tex:77–83](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L77-L83))
- d and spectrum fixed as n grows; constants are not uniform near collisions or vanishing positive eigenvalues. ([article.tex:99–99](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L99-L99))
- GL(d,C) rational highest weights may be negative, but input/output partitions extend to singular matrices; auxiliary rational evaluation at rho requires invertibility. ([article.tex:322–338](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L322-L338))
- Trace distance has factor 1/2; Haar measure normalized; no reference/purification preservation required. ([article.tex:77–83](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L77-L83))
- D is coordinate l1 norm of omega; |delta| is positive-simple-root depth. b_mu contains terminal gap for r<d; g_mu does not. ([article.tex:1146–1168](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1146-L1168))
- Unknown eigenbasis enters only through unitary orbit; channels may depend on n and x but not g. ([article.tex:77–80](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L77-L80))

## Nodes

### `def:code` — Known-spectrum CPTP coding task

Kind: definition; statement: [article.tex:77–83](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L77-L83); proof: —.

**Hypotheses:** Known spectrum x; sole retained finite memory includes all classical registers.

**Quantifiers:** Fix n,x; choose CPTP E,D; take supremum over g.

**Conclusion:** Memory cost is log_2(dim M); error is supremum of half trace norm over the U(d) orbit; encoder/decoder independent of g.

**Constant scope:** Not applicable.

Direct prerequisites: none.

### `eq:result` — QMDL expression L_{d,r}(n,x)

Kind: definition; statement: [article.tex:86–90](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L86-L90); proof: —.

**Hypotheses:** Fixed d and rank r; x_1>...>x_r>0.

**Quantifiers:** For each n.

**Conclusion:** r(2d-r-1)/2 log_2 n + sum_{i<j<=r} log_2(x_i-x_j) + (d-r)sum_i log_2 x_i - sum_{k=d-r}^{d-1}log_2(k!).

**Constant scope:** d,r,x fixed in asymptotic limits; empty products/sums allowed.

Direct prerequisites: none.

### `ext:schur-weyl` — Schur-Weyl decomposition and supported partitions

Kind: external; statement: [article.tex:295–316](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L295-L316); proof: —.

**Hypotheses:** Finite-dimensional tensor powers; polynomial irreps.

**Quantifiers:** All n and density matrices.

**Conclusion:** Tensor-power state decomposes into q_{lambda,n} rho_lambda tensor maximally mixed multiplicity state; rank-r source supports <=r rows.

**Constant scope:** No asymptotic constant.

**Notes:** Standard named theorem invoked, not reproved; source has no precise citation at this site. External-result boundary, not an inferred Lean axiom.

Direct prerequisites: none.

### `def:schur-data` — Representation states and Schur-label distribution

Kind: definition; statement: [article.tex:295–316](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L295-L316); proof: —.

**Hypotheses:** Partitions label polynomial GL(d,C) irreps.

**Quantifiers:** For each partition lambda of n.

**Conclusion:** rho_lambda is normalized irrep state; q_lambda,n=s_lambda(x) dim M_lambda; tau_lambda=I/dim M_lambda.

**Constant scope:** Not applicable.

Direct prerequisites: `ext:schur-weyl`.

### `def:rational-weights` — Rational weights and singular-state domain

Kind: definition; statement: [article.tex:322–338](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L322-L338); proof: [article.tex:399–408](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L399-L408).

**Hypotheses:** Input/output weights in compression are partitions.

**Quantifiers:** For any dominant integral lambda and applicable matrix A.

**Conclusion:** General dominant integral auxiliary weights allowed; rational reps require invertibility if determinant power is negative; for rank-deficient Cartan state comparisons auxiliary weight is a partition.

**Constant scope:** Not applicable.

Direct prerequisites: none.

### `def:covariance` — U(d)-covariant channel and conjugation action

Kind: definition; statement: [article.tex:340–346](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L340-L346); proof: —.

**Hypotheses:** Channels between irreducible representation matrix algebras.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** N intertwines unitary conjugation actions.

**Constant scope:** Not applicable.

Direct prerequisites: none.

### `def:dominance` — Dominance order and dominant rearrangement

Kind: definition; statement: [article.tex:377–400](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L377-L400); proof: —.

**Hypotheses:** Dominant integral weights.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** Equal total weights compare partial sums; omega=(nu-mu)^+ is dominant rearrangement.

**Constant scope:** Not applicable.

Direct prerequisites: none.

### `ext:schur-lemma` — Schur lemma and Haar twirling

Kind: external; statement: [article.tex:368–374](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L368-L374); proof: [article.tex:885–886](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L885-L886).

**Hypotheses:** Finite-dimensional irreducible unitary representation of compact group.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** Commutants on irreducible representations are scalar; normalized Haar twirl of rank-one projector is I/dim H.

**Constant scope:** Not applicable.

Direct prerequisites: none.

### `ext:choi-covariance` — Choi positivity, trace and covariance characterization

Kind: external; statement: [article.tex:358–374](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L358-L374); proof: —.

**Hypotheses:** Finite-dimensional channels and unitary representations.

**Quantifiers:** For every such map.

**Conclusion:** Covariance iff Choi commutes with dual-input tensor output; PSD Choi and correct partial trace give CPTP.

**Constant scope:** No asymptotic constant.

**Notes:** Cited gschwendtner2021programmability Lemma 11 for covariance; Choi CP/TP correspondence used as standard linear-algebra input. External sources not independently verified here.

Direct prerequisites: none.

### `ext:prv` — Multiplicity-one PRV component

Kind: external; statement: [article.tex:390–400](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L390-L400); proof: —.

**Hypotheses:** Dominant integral weights mu,nu.

**Quantifiers:** For every representation pair.

**Conclusion:** Dual-input tensor output has multiplicity-one PRV weight (nu-mu)^+ identified in the source as dominance minimum.

**Constant scope:** No asymptotic constant.

**Notes:** Cited parthasarathy1967 and kumar1988proof. General PRV assertion accepted only as cited external boundary; no independent source-paper validation in this inventory.

Direct prerequisites: none.

### `ext:cartan-duality` — Cartan component uniqueness and tensor-Hom duality

Kind: external; statement: [article.tex:1255–1264](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1255-L1264); proof: [article.tex:1905–1910](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1905-L1910).

**Hypotheses:** nu=mu+omega, dominant integral weights.

**Quantifiers:** For all such weights.

**Conclusion:** The highest-weight sum component has multiplicity one; Hom(nu,mu tensor omega) is isomorphic to Hom(mu* tensor nu,omega).

**Constant scope:** No asymptotic constant.

**Notes:** SOURCE_GAP: the manuscript uses these standard representation-theoretic inputs without a complete proof or precise theorem citation at their use sites; recorded as an external provenance boundary, not a demonstrated mathematical defect.

Direct prerequisites: none.

### `def:gen-cloner` — Original normalized PRV Choi contraction

Kind: definition; statement: [article.tex:412–424](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L412-L424); proof: —.

**Hypotheses:** Irreps mu,nu; Pi_omega is unique PRV component projector.

**Quantifiers:** For any mu,nu, and input operator X.

**Conclusion:** C_mu->nu(X)=Tr_mu[(d_mu/d_omega)Pi_omega(X^T tensor I_nu)], omega=(nu-mu)^+.

**Constant scope:** Not applicable.

Direct prerequisites: `ext:prv`, `def:dominance`, `def:rational-weights`.

### `def:gen-cloner#channel` — The PRV contraction is a covariant CPTP channel

Kind: step; statement: [article.tex:426–432](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L426-L432); proof: [article.tex:426–432](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L426-L432).

**Hypotheses:** Generalized cloner of def:gen-cloner.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** PSD projector yields CP; Schur partial trace and normalization give TP and covariance.

**Constant scope:** Not applicable.

Direct prerequisites: `def:gen-cloner`, `ext:choi-covariance`, `ext:schur-lemma`, `def:covariance`.

### `prop:choi` — Cartan intertwiner has original PRV Choi operator

Kind: proposition; statement: [article.tex:442–456](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L442-L456); proof: [article.tex:457–458](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L457-L458); [article.tex:1853–1936](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1853-L1936).

**Hypotheses:** mu,nu,omega dominant integral; nu=mu+omega; V is Cartan isometric intertwiner.

**Quantifiers:** For every such triple and V; channel formula for every operator X.

**Conclusion:** The Cartan formula (d_mu/d_nu)V†(X tensor I_omega)V has J=(d_mu/d_omega)Pi_omega, hence equals the original cloner.

**Constant scope:** Dimension ratios exact; no limiting constant.

Direct prerequisites: `prop:choi#normalization`, `def:gen-cloner#channel`.

### `prop:choi#gram` — Contracted intertwiner gives a Gram Choi matrix

Kind: step; statement: [article.tex:1854–1897](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1854-L1897); proof: [article.tex:1854–1897](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1854-L1897).

**Hypotheses:** Cartan formula and chosen orthonormal bases.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** Define tilde V: H_mu* tensor H_nu -> H_omega by contraction; J=(d_mu/d_nu)tilde V†tilde V.

**Constant scope:** Not applicable.

Direct prerequisites: none.

### `prop:choi#support` — Gram matrix is scalar on the unique omega component

Kind: step; statement: [article.tex:1899–1910](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1899-L1910); proof: [article.tex:1899–1910](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1899-L1910).

**Hypotheses:** nu=mu+omega and Cartan isometry V.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** tilde V intertwines, has support only on omega, and tilde V†tilde V is proportional to Pi_omega.

**Constant scope:** Not applicable.

Direct prerequisites: `prop:choi#gram`, `ext:cartan-duality`, `ext:schur-lemma`.

### `prop:choi#normalization` — Trace fixes the Choi-projector coefficient

Kind: step; statement: [article.tex:1911–1935](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1911-L1935); proof: [article.tex:1911–1935](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1911-L1935).

**Hypotheses:** V is isometry; Tr Pi_omega=d_omega.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** Tr tilde V†tilde V=d_nu, so tilde V†tilde V=(d_nu/d_omega)Pi_omega and J=(d_mu/d_omega)Pi_omega.

**Constant scope:** Not applicable.

Direct prerequisites: `prop:choi#gram`, `prop:choi#support`.

### `prop:reverse` — Reverse PRV cloner is normalized adjoint and Petz map

Kind: proposition; statement: [article.tex:540–552](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L540-L552); proof: [article.tex:553–555](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L553-L555); [article.tex:1939–2024](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1939-L2024).

**Hypotheses:** Generalized cloning map on finite irreducible representation spaces.

**Quantifiers:** For every representation pair and operator X.

**Conclusion:** C_nu->mu=(d_nu/d_mu) C_mu->nu†, equal to Petz recovery at I_mu/d_mu.

**Constant scope:** Not applicable.

Direct prerequisites: `prop:reverse#petz`, `prop:reverse#dual`.

### `prop:reverse#petz` — Petz map simplifies using invariant maximally mixed states

Kind: step; statement: [article.tex:1940–1954](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1940-L1954); proof: [article.tex:1940–1954](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1940-L1954).

**Hypotheses:** Generalized cloner is covariant CPTP.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** C(I_mu/d_mu)=I_nu/d_nu and Petz recovery equals scaled adjoint.

**Constant scope:** Not applicable.

Direct prerequisites: `def:gen-cloner#channel`, `ext:schur-lemma`, `ext:petz-formula`.

### `ext:petz-formula` — Petz recovery formula

Kind: external; statement: [article.tex:1946–1953](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1946-L1953); proof: —.

**Hypotheses:** Faithful scalar reference state and faithful scalar output.

**Quantifiers:** For all X.

**Conclusion:** Petz map for sigma,C is sigma^(1/2) C†(C(sigma)^(-1/2) X C(sigma)^(-1/2)) sigma^(1/2).

**Constant scope:** Exact equality.

**Notes:** Formula used by name and evaluated in source; no local citation or derivation of the general formula.

Direct prerequisites: none.

### `prop:reverse#kraus` — Vectorized PRV basis gives Kraus and adjoint formulas

Kind: step; statement: [article.tex:1956–1987](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1956-L1987); proof: [article.tex:1956–1987](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1956-L1987).

**Hypotheses:** Orthonormal basis of PRV projector range.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** Orthonormal PRV vectorizations yield C(X)=(d_mu/d_omega)sum K_a X K_a†; scaled adjoint uses K_a†.

**Constant scope:** Not applicable.

Direct prerequisites: `def:gen-cloner`.

### `prop:reverse#dual` — Adjoint Kraus space is reversed PRV component

Kind: step; statement: [article.tex:1989–2022](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1989-L2022); proof: [article.tex:1989–2022](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1989-L2022).

**Hypotheses:** HS-orthonormal K_a spanning omega component.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** Adjoint is antiunitary and carries dual omega*=(mu-nu)^+; Choi normalization matches reverse cloner.

**Constant scope:** Not applicable.

Direct prerequisites: `prop:reverse#kraus`, `ext:prv`, `def:gen-cloner`.

### `def:weight-data` — Supported weight offsets, projectors, and eigenvalues

Kind: definition; statement: [article.tex:1155–1184](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1155-L1184); proof: [article.tex:1218–1253](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1218-L1253).

**Hypotheses:** Partitions length <=r and strictly decreasing nonzero x.

**Quantifiers:** Every partition and supported offset.

**Conclusion:** delta is positive-simple-root offset with depth sum c_i; supported offsets lie in Q_+^(r); rho_lambda=sum p_lambda(delta)Pi_lambda-delta, p=x^(lambda-delta)/s_lambda(x); b_mu includes terminal gap if r<d.

**Constant scope:** Depth is not coordinate l1 norm D.

Direct prerequisites: `ext:weight-theory`.

### `ext:weight-theory` — Highest-weight and Schur-polynomial facts

Kind: external; statement: [article.tex:1155–1191](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1155-L1191); proof: [article.tex:1218–1235](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1218-L1235).

**Hypotheses:** Finite-dimensional rational/polynomial GL(d) irreps.

**Quantifiers:** For all such irreps.

**Conclusion:** Weights lower highest weight by positive roots; highest line unique; lowering operators span; Schur polynomial normalizes representation state.

**Constant scope:** No asymptotic constant.

**Notes:** General references fulton1991representation and macdonald1995symmetric; not externally reverified.

Direct prerequisites: none.

### `eq:verma_multiplicity_bound` — PBW/Verma multiplicity upper bound on supported roots

Kind: step; statement: [article.tex:1186–1198](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1186-L1198); proof: [article.tex:1186–1198](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1186-L1198).

**Hypotheses:** delta in Q_+^(r).

**Quantifiers:** Every lambda and such delta.

**Conclusion:** m_lambda(delta)<=P_d(delta)=P_r(delta) for delta supported in first r coordinates.

**Constant scope:** Not applicable.

Direct prerequisites: `ext:weight-theory`.

### `lem:kostka` — Multiplicity monotonicity under dominant addition

Kind: lemma; statement: [article.tex:1200–1204](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1200-L1204); proof: [article.tex:1205–1216](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1205-L1216).

**Hypotheses:** mu,omega dominant integral weights; delta in Q_+.

**Quantifiers:** All mu,omega,delta.

**Conclusion:** m_mu(delta)<=m_mu+omega(delta).

**Constant scope:** Not applicable.

Direct prerequisites: `ext:gt-patterns`.

### `ext:gt-patterns` — Gelfand-Tsetlin patterns count weight multiplicities

Kind: external; statement: [article.tex:1206–1210](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1206-L1210); proof: —.

**Hypotheses:** Dominant integral highest weights.

**Quantifiers:** For each weight.

**Conclusion:** Integral interlacing GT patterns encode weight multiplicities and weight is successive row-sum differences.

**Constant scope:** No asymptotic constant.

**Notes:** SOURCE_GAP: GT counting is asserted without proof or precise citation at this site; the source proves the subsequent injection. This is an external provenance boundary.

Direct prerequisites: none.

### `def:cartan-projectors` — Embedded target and retained highest-weight projectors

Kind: definition; statement: [article.tex:1255–1279](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1255-L1279); proof: —.

**Hypotheses:** nu=mu+omega and Cartan embedding V; supported delta.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** P_delta=V Pi_nu-delta V† and Q_delta=Pi_mu-delta tensor |omega><omega| share total-weight sector nu-delta.

**Constant scope:** Not applicable.

Direct prerequisites: `prop:choi`, `def:weight-data`, `ext:cartan-duality`.

### `ext:casimir` — Ambient GL(d) quadratic Casimir and its scalar eigenvalue

Kind: external; statement: [article.tex:1281–1292](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1281-L1292); proof: —.

**Hypotheses:** Invariant inner product and ambient GL(d) generators, including rank-deficient state case.

**Quantifiers:** Every finite-dimensional irrep and tensor constituent.

**Conclusion:** C_2=sum H_i^2+sum(E_-E_++E_+E_-); c_lambda=(lambda,lambda+2varrho) on each constituent.

**Constant scope:** Ambient d, not rank r.

**Notes:** SOURCE_GAP: Casimir action/eigenvalue is stated as standard input without proof or a precise citation at this site. The following local slice-gap and deficit calculations are supplied in the source.

Direct prerequisites: none.

### `ext:kostant` — Kostant multiplicity formula

Kind: external; statement: [article.tex:2122–2132](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2122-L2132); proof: —.

**Hypotheses:** Dominant integral lambda; positive roots of GL(d).

**Quantifiers:** For every delta.

**Conclusion:** m_lambda(delta)=sum_w sgn(w)P_d(delta-[lambda+varrho-w(lambda+varrho)]).

**Constant scope:** No asymptotic constant.

**Notes:** Cited kostant1959multiplicity; cited paper not independently checked here.

Direct prerequisites: none.

### `lem:shallow_multiplicities` — Shallow weight multiplicities equal root partitions

Kind: lemma; statement: [article.tex:1397–1406](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1397-L1406); proof: [article.tex:1408–1410](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1408-L1410); [article.tex:2121–2167](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2121-L2167).

**Hypotheses:** 2<=r<=d; dominant integral lambda; delta in Q_+^(r); |delta|<=g_lambda=min_{i<r}(lambda_i-lambda_i+1).

**Quantifiers:** For every such lambda,r,delta.

**Conclusion:** m_lambda(delta)=P_r(delta).

**Constant scope:** Not applicable.

Direct prerequisites: `lem:shallow_multiplicities#vanishing`, `eq:verma_multiplicity_bound`.

### `lem:shallow_multiplicities#vanishing` — Nonidentity Weyl terms vanish at shallow depth

Kind: step; statement: [article.tex:2133–2158](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2133-L2158); proof: [article.tex:2133–2158](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2133-L2158).

**Hypotheses:** Depth <=g_lambda with support in first r-1 simple roots.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** First moved coordinate k has shifted-root coefficient >=lambda_k-lambda_k+1+1>c_k, so nonidentity Kostant term is zero.

**Constant scope:** Not applicable.

Direct prerequisites: `ext:kostant`.

### `lem:perturbation` — Highest-weight projectors are close at shallow depth

Kind: lemma; statement: [article.tex:1412–1433](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1412-L1433); proof: [article.tex:1435–1500](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1435-L1500).

**Hypotheses:** mu,nu partitions <=r rows; omega=nu-mu dominant; for r>=2, |delta|<=g_mu.

**Quantifiers:** Every eligible pair and supported shallow delta.

**Conclusion:** Equal ranks and ||P_delta-Q_delta||<=sqrt(2(delta,omega)/(g_mu+2))<=sqrt(2|delta|D/(g_mu+2)); for r=1 projectors coincide.

**Constant scope:** Bound depends exactly on D,g_mu,delta; no hidden state constant.

Direct prerequisites: `lem:perturbation#projector-norm`.

### `lem:perturbation#rank` — Shallow projectors have equal rank

Kind: step; statement: [article.tex:1436–1445](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1436-L1445); proof: [article.tex:1436–1445](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1436-L1445).

**Hypotheses:** Depth condition; dominant omega.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** g_nu>=g_mu and shallow multiplicity identity give rank P=rank Q=m_mu(delta); zero cases coincide.

**Constant scope:** Not applicable.

Direct prerequisites: `lem:shallow_multiplicities`, `def:cartan-projectors`.

### `eq:casimir_slice_gap` — Total-weight Casimir has gap at least g_mu+2

Kind: step; statement: [article.tex:1447–1464](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1447-L1464); proof: [article.tex:1447–1464](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1447-L1464).

**Hypotheses:** Other constituent chi=nu-eta has eta,delta-eta in Q_+; eta supported in first r roots.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** c_nu I-C_2 >=(g_mu+2)(I-P_delta) on weight sector nu-delta.

**Constant scope:** Not applicable.

Direct prerequisites: `ext:casimir`, `def:cartan-projectors`.

### `eq:casimir_deficit_compression` — Compress Casimir deficit to auxiliary highest-weight line

Kind: step; statement: [article.tex:1466–1480](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1466-L1480); proof: [article.tex:1466–1480](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1466-L1480).

**Hypotheses:** Q has auxiliary highest weight; represented root adjoints obey source convention.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** Q_delta(c_nu I-C_2)Q_delta=2(delta,omega)Q_delta.

**Constant scope:** Not applicable.

Direct prerequisites: `ext:casimir`, `def:weight-data`, `def:cartan-projectors`.

### `lem:perturbation#projector-norm` — Casimir deficit controls equal-rank projector norm

Kind: step; statement: [article.tex:1481–1499](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1481-L1499); proof: [article.tex:1481–1499](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1481-L1499).

**Hypotheses:** Equal ranks and previous Casimir estimates.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** ||(I-P)Q||^2<=2(delta,omega)/(g_mu+2), and equal ranks identify this with ||P-Q||^2.

**Constant scope:** Not applicable.

Direct prerequisites: `eq:casimir_slice_gap`, `eq:casimir_deficit_compression`, `lem:perturbation#rank`.

### `lem:tail` — Uniform mean depth

Kind: lemma; statement: [article.tex:1507–1521](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1507-L1521); proof: [article.tex:1522–1545](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1522-L1545).

**Hypotheses:** Fixed strictly decreasing nonzero spectrum; mu partition <=r rows.

**Quantifiers:** For all mu; one constant K(x) for every representation.

**Conclusion:** sum_delta |delta|p_mu(delta)m_mu(delta)<=K(x)=N q_x/(1-q_x)^(N+1), N=binom(r,2); r=1 gives zero.

**Constant scope:** Depends only on fixed nonzero spectrum/rank; not on mu.

Direct prerequisites: `lem:tail#count`.

### `lem:tail#count` — Depth generating-function envelope

Kind: step; statement: [article.tex:1523–1538](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1523-L1538); proof: [article.tex:1523–1538](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1523-L1538).

**Hypotheses:** r>=2; s_mu(x)>=x^mu.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** p_mu(delta)<=q_x^|delta|; total multiplicity at depth t <=binom(t+N-1,N-1).

**Constant scope:** Not applicable.

Direct prerequisites: `def:weight-data`, `eq:verma_multiplicity_bound`.

### `lem:ratio` — Eigenvalue normalization ratio

Kind: lemma; statement: [article.tex:1551–1563](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1551-L1563); proof: [article.tex:1564–1594](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1564-L1594).

**Hypotheses:** Partition and dominance assumptions; distinct positive nonzero spectrum.

**Quantifiers:** Every pair; ratio independent of delta.

**Conclusion:** Z=x^omega s_mu/s_nu=p_nu(delta)/p_mu(delta); r=1 Z=1; r>=2 0<=1-Z<=K(x)/(g_mu+1).

**Constant scope:** K(x) independent of mu,nu.

Direct prerequisites: `def:weight-data`, `lem:kostka`, `lem:shallow_multiplicities`, `lem:tail`.

### `ext:weyl-dimension` — Exact Weyl dimension formula

Kind: external; statement: [article.tex:682–685](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L682-L685); proof: —.

**Hypotheses:** Dominant integral weights.

**Quantifiers:** For every representation.

**Conclusion:** d_lambda=product_{i<j}(lambda_i-lambda_j+j-i)/(j-i).

**Constant scope:** Exact formula.

**Notes:** Named formula; source does not reprove it or provide a local citation.

Direct prerequisites: none.

### `lem:dim_ratio` — Weyl dimension ratio deficit

Kind: lemma; statement: [article.tex:1598–1607](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1598-L1607); proof: [article.tex:1608–1624](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1608-L1624).

**Hypotheses:** Partition/dominance hypotheses of thm:main.

**Quantifiers:** Every eligible pair.

**Conclusion:** 0<=1-d_mu/d_nu<=sum (omega_i-omega_j)/(mu_i-mu_j+j-i)<=binom(d,2)D/(b_mu+1).

**Constant scope:** Explicit dimension-only coefficient binom(d,2).

Direct prerequisites: `ext:weyl-dimension`, `def:weight-data`.

### `ext:trace-analysis` — Finite-dimensional trace norm and positive-part identities

Kind: external; statement: [article.tex:756–785](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L756-L785); proof: [article.tex:1359–1385](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1359-L1385); [article.tex:1695–1705](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1695-L1705).

**Hypotheses:** Finite-dimensional Hermitian operators, states, channels as appropriate.

**Quantifiers:** Universal over local carriers.

**Conclusion:** Trace distance is CPTP-contracting, convex, <=1 on states; isometry invariant; block/tensor norm rules; Tr X_+=max_{0<=L<=I}Tr(LX).

**Constant scope:** No asymptotic constant.

**Notes:** Standard linear-algebra boundary. Positive-deficit consequence is actually derived in source at 1695-1705.

Direct prerequisites: none.

### `thm:main#branch` — Retain highest-weight Kraus branch and compare its deficit

Kind: step; statement: [article.tex:1341–1391](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1341-L1391); proof: [article.tex:1341–1391](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1341-L1391).

**Hypotheses:** Cartan pair and normalized representation states.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** Embedded C>=K_omega, with K=(d_mu/d_nu)P_nu(X tensor |omega><omega|)P_nu; forward error <=Tr(embedded rho_nu-K(rho_mu))_+.

**Constant scope:** Not applicable.

Direct prerequisites: `prop:choi`, `def:cartan-projectors`, `def:weight-data`, `ext:trace-analysis`.

### `thm:main#all-depth` — Extend shallow projector bound to all depths

Kind: step; statement: [article.tex:1629–1668](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1629-L1668); proof: [article.tex:1629–1668](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1629-L1668).

**Hypotheses:** Integer D and offsets; r>=2 or explicit pure-rank case.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** D=0 gives identity channels; for D>=1 cap e_delta=min(1,2|delta|D/(g_mu+2)) controls both PQP and QPQ; r=1 e_0=0.

**Constant scope:** Not applicable.

Direct prerequisites: `prop:choi`, `prop:reverse`, `lem:perturbation`.

### `eq:averaged_projector_deficit` — Average the capped projector deficits

Kind: step; statement: [article.tex:1669–1683](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1669-L1683); proof: [article.tex:1669–1683](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1669-L1683).

**Hypotheses:** Both partition states satisfy same fixed spectrum assumptions.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** M_lambda=sum e_delta p_lambda m_lambda<=2DK(x)/(g_mu+2), lambda in {mu,nu}; for r=1 M=0.

**Constant scope:** Not applicable.

Direct prerequisites: `thm:main#all-depth`, `lem:tail`, `def:cartan-projectors`.

### `eq:positive_deficit_trace` — Positive remainder controls trace distance plus missing trace

Kind: step; statement: [article.tex:1695–1707](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1695-L1707); proof: [article.tex:1695–1707](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1695-L1707).

**Hypotheses:** All the displayed local matrix hypotheses.

**Quantifiers:** All such matrices on same finite carrier.

**Conclusion:** A>=B-R, A>=0,Tr A<=1,B state,R>=0 imply (||A-B||_1+1-Tr A)/2=Tr(B-A)_+<=Tr R.

**Constant scope:** Not applicable.

Direct prerequisites: `ext:trace-analysis`.

### `eq:forward_finite_deficit` — Forward channel finite deficit estimate

Kind: step; statement: [article.tex:1709–1756](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1709-L1756); proof: [article.tex:1709–1756](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1709-L1756).

**Hypotheses:** Generalized cloner in Cartan case; state and weight hypotheses.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** Forward error <=1-d_mu/d_nu+M_nu via positive remainder R_f.

**Constant scope:** Not applicable.

Direct prerequisites: `lem:ratio`, `lem:dim_ratio`, `thm:main#branch`, `thm:main#all-depth`, `eq:averaged_projector_deficit`, `eq:positive_deficit_trace`.

### `eq:reverse_finite_deficit` — Reverse channel finite deficit estimate

Kind: step; statement: [article.tex:1758–1801](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1758-L1801); proof: [article.tex:1758–1801](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1758-L1801).

**Hypotheses:** Same Cartan pair and local state assumptions.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** Reverse channel is Tr_omega(V X V†); retain highest-weight term to get reverse error <=1-Z+M_mu.

**Constant scope:** Not applicable.

Direct prerequisites: `prop:choi`, `prop:reverse`, `def:cartan-projectors`, `thm:main#all-depth`, `lem:ratio`, `eq:averaged_projector_deficit`, `eq:positive_deficit_trace`.

### `thm:main#constant` — Collect finite bounds with one spectrum-dependent constant

Kind: step; statement: [article.tex:1803–1826](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1803-L1826); proof: [article.tex:1803–1826](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1803-L1826).

**Hypotheses:** D>=1 in nonidentity case; b_mu<=g_mu for r>=2.

**Quantifiers:** One constant for every eligible mu,nu.

**Conclusion:** For all ranks, C_{d,x}=binom(d,2)+3K(x) works for both directions; r=1 has zero reverse error.

**Constant scope:** Only d and fixed nonzero spectrum; independent of weights.

Direct prerequisites: `eq:forward_finite_deficit`, `eq:reverse_finite_deficit`, `eq:averaged_projector_deficit`, `lem:dim_ratio`, `lem:ratio`, `lem:tail`.

### `thm:main` — Theorem 2: original Choi-cloner accuracy

Kind: theorem; statement: [article.tex:562–580](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L562-L580); proof: [article.tex:1130–1140](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1130-L1140); [article.tex:1628–1827](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1628-L1827).

**Hypotheses:** rho on C^d,d>=2,rank r<=d; x_1>...>x_r>0; mu,nu partitions <=r rows; omega=nu-mu dominant integral; original PRV cloning maps.

**Quantifiers:** Fix d,x; exists C_{d,x}; for every admissible mu,nu, both directional bounds.

**Conclusion:** Both half-trace-norm errors <=C_{d,x} ||nu-mu||_1/(b_mu+1).

**Constant scope:** C depends only on d and nonzero spectrum; not mu,nu; D is coordinate l1 norm, b includes terminal row gap when r<d.

Direct prerequisites: `thm:main#constant`, `thm:main#all-depth`, `def:gen-cloner#channel`.

### `def:typical-target` — Typical set and padded fixed target

Kind: definition; statement: [article.tex:608–627](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L608-L627); proof: —.

**Hypotheses:** Fixed spectrum, n; supported partitions.

**Quantifiers:** For every n.

**Conclusion:** epsilon_n=sqrt(n/2)log_2 n; typical max row deviation <=epsilon_n; Lambda_i=ceil(nx_i+(r-i+1)(2epsilon_n+1)) for i<=r and zero after r.

**Constant scope:** Target independent of g and measured lambda.

Direct prerequisites: none.

### `lem:weyl_asymptotic` — Weyl asymptotic through additive constant

Kind: lemma; statement: [article.tex:671–680](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L671-L680); proof: [article.tex:681–701](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L681-L701).

**Hypotheses:** Fixed d and distinct positive x_1>...>x_r; lambda_i=nx_i+O(sqrt n zeta_n) for i<=r, zero later; zeta_n=o(sqrt n); lambda need not partition n.

**Quantifiers:** For every sequence of such partitions.

**Conclusion:** log_2 dim H_lambda=L_{d,r}(n,x)+O(zeta_n/sqrt n+1/n).

**Constant scope:** d,x fixed; source does not explicitly specify dependence on constants in row O-bounds; standard inherited O-constant dependence.

Direct prerequisites: `ext:weyl-dimension`, `eq:result`.

### `thm:achievability#code` — Construct full-space CPTP encoder and decoder

Kind: step; statement: [article.tex:705–729](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L705-L729); proof: [article.tex:743–755](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L743-L755).

**Hypotheses:** Rank-r tensor source and fixed target.

**Quantifiers:** For all inputs to full physical carrier; depends on n,x only.

**Conclusion:** Encoder measures blocks, traces multiplicity, clones to Lambda, and replaces unsupported complement; decoder resamples q, reverse clones, appends tau, undoes Schur.

**Constant scope:** Memory exactly H_Lambda; d=1 handled as known singleton orbit.

Direct prerequisites: `def:code`, `def:schur-data`, `def:gen-cloner#channel`, `def:typical-target`, `def:schur-data`.

### `thm:achievability#padding` — Padding discharges Cartan dominance and finite-bound scales

Kind: step; statement: [article.tex:731–740](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L731-L740); proof: [article.tex:810–819](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L810-L819).

**Hypotheses:** Distinct positive fixed x; typicality; sufficiently large n.

**Quantifiers:** Uniformly for all typical lambda at each n.

**Conclusion:** For typical lambda, Lambda-lambda is nonnegative dominant, b_lambda=Omega(n), and ||Lambda-lambda||_1=O(sqrt n log n).

**Constant scope:** Constants depend on d,r,x; not lambda or g.

Direct prerequisites: `def:typical-target`.

### `thm:achievability#error-split` — Reference target splits reconstruction error

Kind: step; statement: [article.tex:749–785](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L749-L785); proof: [article.tex:749–785](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L749-L785).

**Hypotheses:** Physical encoder/decoder and source block decomposition.

**Quantifiers:** For every orbit state; uniform by covariance.

**Conclusion:** Total error <=two average cloning errors <=typical forward max+typical reverse max+2 atypical mass.

**Constant scope:** Not applicable.

Direct prerequisites: `thm:achievability#code`, `ext:trace-analysis`.

### `ext:schur-large-deviation` — Pointwise Schur-Weyl concentration bound

Kind: external; statement: [article.tex:788–800](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L788-L800); proof: —.

**Hypotheses:** Schur distribution for rank-r source.

**Quantifiers:** Every supported lambda.

**Conclusion:** q_lambda,n<=(n+1)^(r(r-1)/2) 2^(-n D(lambda/n||x)) on supported diagrams.

**Constant scope:** Dimension/rank polynomial prefactor.

**Notes:** Pointwise result specifically attributed to christandl2006spectra; lemma also cites yang2016efficient,o2021quantum,hayashi2017group. External literature not independently verified here.

Direct prerequisites: none.

### `ext:pinsker` — Pinsker inequality with base-two divergence

Kind: external; statement: [article.tex:800–800](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L800-L800); proof: —.

**Hypotheses:** Probability distributions; D measured in bits.

**Quantifiers:** All such distributions.

**Conclusion:** D(p||x)>=(2/ln 2) TV(p,x)^2.

**Constant scope:** Explicit 2/ln2 normalization.

**Notes:** Named standard inequality without separate local citation.

Direct prerequisites: none.

### `lem:tail_prob` — Schur-label Sanov event bound

Kind: lemma; statement: [article.tex:788–799](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L788-L799); proof: [article.tex:800–800](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L800-L800).

**Hypotheses:** lambda drawn from Schur distribution; t>0.

**Quantifiers:** For every t>0, n and fixed source.

**Conclusion:** Pr[TV(lambda/n,x)>t]<=(n+1)^(r(r+1)/2) exp(-2nt^2).

**Constant scope:** Rank-sensitive polynomial prefactor.

Direct prerequisites: `ext:schur-large-deviation`, `ext:pinsker`.

### `eq:tail_prob_bound` — Typical complement is superpolynomially small

Kind: step; statement: [article.tex:801–808](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L801-L808); proof: [article.tex:801–808](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L801-L808).

**Hypotheses:** Source supported on <=r rows; typical max-deviation threshold.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** Atypical mass <=(n+1)^(r(r+1)/2) exp(-(log n)^2/4).

**Constant scope:** Not applicable.

Direct prerequisites: `def:typical-target`, `lem:tail_prob`.

### `thm:achievability#typical-error` — Apply finite cloning theorem uniformly on typical set

Kind: step; statement: [article.tex:810–828](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L810-L828); proof: [article.tex:810–828](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L810-L828).

**Hypotheses:** d>=2, sufficiently large n, typical lambda; fixed spectrum.

**Quantifiers:** Uniformly over all typical lambda.

**Conclusion:** Both typical cloning errors are O(log n/sqrt n).

**Constant scope:** Only d,r,x and padded target constants.

Direct prerequisites: `thm:achievability#padding`, `thm:main`.

### `thm:achievability#rate` — Combine typical and atypical errors

Kind: step; statement: [article.tex:829–835](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L829-L835); proof: [article.tex:829–835](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L829-L835).

**Hypotheses:** Constructed code and fixed spectrum.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** Total worst-case reconstruction error is O(log n/sqrt n).

**Constant scope:** Not applicable.

Direct prerequisites: `thm:achievability#error-split`, `thm:achievability#typical-error`, `eq:tail_prob_bound`.

### `thm:achievability#memory` — Evaluate padded target memory

Kind: step; statement: [article.tex:837–843](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L837-L843); proof: [article.tex:837–843](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L837-L843).

**Hypotheses:** Fixed padded target with rows nx_i+O(sqrt n log n).

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** log dim H_Lambda=L_{d,r}(n,x)+o(1).

**Constant scope:** Not applicable.

Direct prerequisites: `def:typical-target`, `lem:weyl_asymptotic`.

### `thm:achievability` — Theorem 1 achievability component

Kind: theorem; statement: [article.tex:645–661](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L645-L661); proof: [article.tex:704–844](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L704-L844).

**Hypotheses:** Fixed density matrix rank r<=d with strictly decreasing nonzero spectrum.

**Quantifiers:** Fix d,r,x; exists sequence of codes independent of g; uniform error over all g.

**Conclusion:** Exists CPTP code sequence with memory L_{d,r}(n,x)+o(1) and supremum error O(log n/sqrt n).

**Constant scope:** Only d,r,x; no uniform collision/zero-eigenvalue claim.

Direct prerequisites: `thm:achievability#code`, `thm:achievability#rate`, `thm:achievability#memory`.

### `prop:compact_orbit_memory` — Finite memory bound for irreducible compact-group orbits

Kind: proposition; statement: [article.tex:854–876](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L854-L876); proof: [article.tex:877–894](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L877-L894).

**Hypotheses:** Continuous irreducible unitary representation of compact G on finite H; normalized Haar; tau with simple largest eigenvalue p0, gap gamma=p0-p1>0; arbitrary CPTP E,D.

**Quantifiers:** For every finite M and CPTP code; average error over G.

**Conclusion:** dim M>=dim H (1-average_delta/gamma).

**Constant scope:** Exact dependence only through gamma and average error; no covariance assumption on code.

Direct prerequisites: `prop:compact_orbit_memory#average`.

### `prop:compact_orbit_memory#order` — Code factorization gives operator order bound

Kind: step; statement: [article.tex:878–884](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L878-L884); proof: [article.tex:878–884](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L878-L884).

**Hypotheses:** Channels CPTP and tau<=p1 I+gamma P.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** Phi(tau_g)<=p1 Phi(I)+gamma D(I_M), since E(P_g) is state <=I_M.

**Constant scope:** Not applicable.

Direct prerequisites: `ext:trace-analysis`.

### `prop:compact_orbit_memory#average` — Haar-average rank-one test counts memory dimension

Kind: step; statement: [article.tex:885–893](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L885-L893); proof: [article.tex:885–893](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L885-L893).

**Hypotheses:** Rank-one P_g and preceding order bound; irreducibility.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** p0-average_delta<=p1+gamma dim M/dim H; rearrangement proves memory bound.

**Constant scope:** Not applicable.

Direct prerequisites: `prop:compact_orbit_memory#order`, `ext:schur-lemma`, `ext:trace-analysis`.

### `lem:sector_gap` — Uniform simple top eigenvalue and positive spectral gap

Kind: lemma; statement: [article.tex:901–913](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L901-L913); proof: [article.tex:914–916](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L914-L916); [article.tex:2027–2081](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2027-L2081).

**Hypotheses:** Strictly decreasing positive nonzero spectrum; partitions <=r rows.

**Quantifiers:** One gamma_x for every partition lambda.

**Conclusion:** Every supported rho_lambda has simple largest eigenvalue with gap >=gamma_x=(1-q_x)product_{i<j<=r}(1-x_j/x_i)>0; q_x=0 if r=1.

**Constant scope:** Only fixed nonzero spectrum; independent of lambda.

Direct prerequisites: `lem:sector_gap#normalizer`.

### `lem:sector_gap#top` — Nonhighest weights have eigenvalue ratio at most q_x

Kind: step; statement: [article.tex:2028–2043](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2028-L2043); proof: [article.tex:2028–2043](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2028-L2043).

**Hypotheses:** Supported weight decomposition; x adjacent ratios <1.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** r=1 state pure; otherwise highest line unique and all other positive eigenvalues <=q_x p0.

**Constant scope:** Not applicable.

Direct prerequisites: `def:weight-data`.

### `lem:sector_gap#normalizer` — Root partition product bounds highest eigenvalue below

Kind: step; statement: [article.tex:2045–2079](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2045-L2079); proof: [article.tex:2045–2079](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2045-L2079).

**Hypotheses:** Nonnegative convergent root-partition series and fixed ordered positive x.

**Quantifiers:** Universal over the local objects in the cited source region.

**Conclusion:** p0^(-1)<=product_{i<j<=r}(1-x_j/x_i)^(-1); hence gamma>=gamma_x.

**Constant scope:** Not applicable.

Direct prerequisites: `eq:verma_multiplicity_bound`, `def:weight-data`, `lem:sector_gap#top`.

### `thm:converse#transport` — Transfer arbitrary physical code to padded target orbit

Kind: step; statement: [article.tex:941–981](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L941-L981); proof: [article.tex:941–981](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L941-L981).

**Hypotheses:** Arbitrary physical code; A_n,B_n are constructed achievability channels.

**Quantifiers:** Every g first, then normalized Haar average.

**Conclusion:** E_n composed B_n and A_n composed D_n use same M_n and have target Haar-average error <=average_delta_n+e_n, e_n=O(log n/sqrt n).

**Constant scope:** Transfer error uniform in g and depends only on fixed d,r,x.

Direct prerequisites: `thm:achievability#code`, `thm:achievability#typical-error`, `eq:tail_prob_bound`, `thm:achievability#error-split`, `ext:trace-analysis`.

### `thm:converse#finite` — Apply uniform-gap orbit bound and take logarithm

Kind: step; statement: [article.tex:982–988](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L982-L988); proof: [article.tex:982–988](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L982-L988).

**Hypotheses:** average_delta_n->0, e_n->0, fixed gamma_x>0; target irrep orbit.

**Quantifiers:** All sufficiently large n; arbitrary original code sequence.

**Conclusion:** For sufficiently large n, |M_n|>=log dim H_Lambda + log(1-(average_delta_n+e_n)/gamma_x)=log dim H_Lambda+o(1).

**Constant scope:** Gap fixed in n; logarithm eventually defined and tends to zero.

Direct prerequisites: `thm:converse#transport`, `prop:compact_orbit_memory`, `lem:sector_gap`.

### `thm:converse` — Theorem 1 Haar-average converse component

Kind: theorem; statement: [article.tex:923–939](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L923-L939); proof: [article.tex:940–993](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L940-L993).

**Hypotheses:** Fixed rank-r density matrix with distinct positive nonzero spectrum; arbitrary CPTP code sequence; average reconstruction error ->0.

**Quantifiers:** For every such sequence; asymptotic lower bound as n->infinity.

**Conclusion:** For every vanishing-Haar-average-error physical code sequence, |M_n|>=L_{d,r}(n,x)+o(1), equivalently liminf(|M_n|-L)>=0.

**Constant scope:** Fixed d,r,x; no rate demanded of arbitrary code error.

Direct prerequisites: `thm:converse#finite`, `lem:weyl_asymptotic`, `def:typical-target`.

### `thm:qmdl#uniform-converse` — Uniform-error converse follows from Haar-average converse

Kind: step; statement: [article.tex:92–99](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L92-L99); proof: [article.tex:918–921](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L918-L921).

**Hypotheses:** Normalized Haar measure and nonnegative errors; all other thm:qmdl hypotheses.

**Quantifiers:** Every uniformly vanishing-error code sequence.

**Conclusion:** Supremum error ->0 implies Haar-average error ->0, hence same liminf memory bound.

**Constant scope:** Not applicable.

Direct prerequisites: `thm:converse`, `def:code`.

### `thm:qmdl` — Theorem 1 optimal memory through additive constant

Kind: theorem; statement: [article.tex:85–98](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L85-L98); proof: [article.tex:99–99](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L99-L99).

**Hypotheses:** Fixed d and rank-r density matrix; x_1>...>x_r>0; code task as defined.

**Quantifiers:** Fix d,r,x; exists achieving sequence; independently for every vanishing-error sequence, lower bound.

**Conclusion:** Exists codes with |M_n|=L+o(1), error O(log n/sqrt n); every code sequence with uniform or Haar-average error ->0 has liminf(|M_n|-L)>=0.

**Constant scope:** Only fixed d,r,x; not uniform near eigenvalue collisions or zero; not every prescribed error schedule.

Direct prerequisites: `thm:achievability`, `thm:converse`, `thm:qmdl#uniform-converse`, `eq:result`.

## Direct dependency evidence

| Consumer | Prerequisite | Consumer source | Reason |
|---|---|---|---|
| def:schur-data | ext:schur-weyl | [article.tex:304–316](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L304-L316) | Defines distribution and block states supplied by Schur-Weyl decomposition. |
| def:gen-cloner | ext:prv | [article.tex:413–424](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L413-L424) | Multiplicity one makes the selected projector unambiguous. |
| def:gen-cloner | def:dominance | [article.tex:413–418](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L413-L418) | Definition selects dominant rearrangement of weight difference. |
| def:gen-cloner | def:rational-weights | [article.tex:413–418](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L413-L418) | Auxiliary PRV component may have general dominant integral highest weight. |
| def:gen-cloner#channel | def:gen-cloner | [article.tex:426–431](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L426-L431) | Uses the defining normalized projector. |
| def:gen-cloner#channel | ext:choi-covariance | [article.tex:426–432](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L426-L432) | Choi positivity and normalized partial trace imply CPTP. |
| def:gen-cloner#channel | ext:schur-lemma | [article.tex:426–431](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L426-L431) | Partial trace is scalar by irreducibility. |
| def:gen-cloner#channel | def:covariance | [article.tex:426–432](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L426-L432) | Covariance is inherited from invariant PRV projector. |
| prop:choi#support | prop:choi#gram | [article.tex:1899–1903](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1899-L1903) | Uses the contracted map just constructed. |
| prop:choi#support | ext:cartan-duality | [article.tex:1905–1910](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1905-L1910) | Uses Hom-space dimension equality and Cartan multiplicity one. |
| prop:choi#support | ext:schur-lemma | [article.tex:1903–1910](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1903-L1910) | Commuting positive operator is scalar on unique irreducible component. |
| prop:choi#normalization | prop:choi#gram | [article.tex:1929–1932](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1929-L1932) | Substitutes the computed coefficient into the Gram Choi formula. |
| prop:choi#normalization | prop:choi#support | [article.tex:1925–1927](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1925-L1927) | Scalar-on-projector description makes trace determine the coefficient. |
| prop:choi | prop:choi#normalization | [article.tex:1929–1935](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1929-L1935) | Completes the exact Choi identity. |
| prop:choi | def:gen-cloner#channel | [article.tex:1931–1935](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1931-L1935) | Identification with the defining PRV Choi operator supplies the channel interpretation. |
| prop:reverse#petz | def:gen-cloner#channel | [article.tex:1940–1943](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1940-L1943) | Uses covariance and trace preservation. |
| prop:reverse#petz | ext:schur-lemma | [article.tex:1940–1943](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1940-L1943) | Irreducibility fixes invariant output. |
| prop:reverse#petz | ext:petz-formula | [article.tex:1946–1953](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1946-L1953) | Substitutes scalar states in the standard Petz formula. |
| prop:reverse#kraus | def:gen-cloner | [article.tex:1964–1978](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1964-L1978) | Expands defining Choi projector as sum of rank-one vectorizations. |
| prop:reverse#dual | prop:reverse#kraus | [article.tex:2013–2016](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2013-L2016) | Uses the adjoint Kraus family and coefficient. |
| prop:reverse#dual | ext:prv | [article.tex:2007–2017](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2007-L2017) | Identifies dual irrep as reversed pair PRV component. |
| prop:reverse#dual | def:gen-cloner | [article.tex:2014–2017](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2014-L2017) | Recognizes the resulting normalized Choi operator as the reverse definition. |
| prop:reverse | prop:reverse#petz | [article.tex:2023–2023](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2023-L2023) | Combines the Petz simplification with reversed-channel identification. |
| prop:reverse | prop:reverse#dual | [article.tex:2017–2023](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2017-L2023) | Establishes the exact scaled-adjoint equality. |
| def:weight-data | ext:weight-theory | [article.tex:1218–1235](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1218-L1235) | Uses highest-weight decomposition and Schur normalizer. |
| eq:verma_multiplicity_bound | ext:weight-theory | [article.tex:1189–1194](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1189-L1194) | Ordered lowering-operator spanning bounds multiplicities by positive-root partitions. |
| lem:kostka | ext:gt-patterns | [article.tex:1206–1215](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1206-L1215) | Injective addition m_i,j -> m_i,j+omega_j is applied to the GT pattern model. |
| def:cartan-projectors | prop:choi | [article.tex:1260–1262](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1260-L1262) | Chooses the Cartan isometry from Proposition choi. |
| def:cartan-projectors | def:weight-data | [article.tex:1266–1279](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1266-L1279) | Uses weight projectors and their offsets. |
| def:cartan-projectors | ext:cartan-duality | [article.tex:1258–1264](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1258-L1264) | Uses unique highest-weight Cartan component and lower other constituents. |
| lem:shallow_multiplicities#vanishing | ext:kostant | [article.tex:2154–2158](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2154-L2158) | Applies support criterion for the partition-function terms in Kostant sum. |
| lem:shallow_multiplicities | lem:shallow_multiplicities#vanishing | [article.tex:2157–2158](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2157-L2158) | Leaves only identity term P_d(delta). |
| lem:shallow_multiplicities | eq:verma_multiplicity_bound | [article.tex:2160–2166](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2160-L2166) | Same positive-root support argument identifies P_d=P_r; source repeats argument explicitly. |
| lem:perturbation#rank | lem:shallow_multiplicities | [article.tex:1439–1444](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1439-L1444) | Applies lemma to both mu and nu with g_nu>=g_mu. |
| lem:perturbation#rank | def:cartan-projectors | [article.tex:1442–1444](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1442-L1444) | Ranks identify with source and target weight multiplicities. |
| eq:casimir_slice_gap | ext:casimir | [article.tex:1447–1459](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1447-L1459) | Uses scalar eigenvalues and c_nu-c_chi expansion. |
| eq:casimir_slice_gap | def:cartan-projectors | [article.tex:1448–1463](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1448-L1463) | Uses Cartan component and lower constituent support. |
| eq:casimir_deficit_compression | ext:casimir | [article.tex:1466–1479](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1466-L1479) | Expands tensor Casimir and scalar eigenvalues. |
| eq:casimir_deficit_compression | def:weight-data | [article.tex:1474–1476](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1474-L1476) | Highest-weight raising operators kill omega, so root-exchange terms vanish. |
| eq:casimir_deficit_compression | def:cartan-projectors | [article.tex:1474–1479](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1474-L1479) | Q fixes input weight mu-delta and auxiliary weight omega. |
| lem:perturbation#projector-norm | eq:casimir_slice_gap | [article.tex:1481–1485](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1481-L1485) | Compresses the operator gap to Q. |
| lem:perturbation#projector-norm | eq:casimir_deficit_compression | [article.tex:1481–1485](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1481-L1485) | Supplies compressed deficit value. |
| lem:perturbation#projector-norm | lem:perturbation#rank | [article.tex:1487–1497](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1487-L1497) | Equal-rank singular-value argument makes the two projector norms equal. |
| lem:perturbation | lem:perturbation#projector-norm | [article.tex:1498–1499](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1498-L1499) | Combines projector estimate with 0<=(delta,omega)<=\|delta\|D; r=1/zero cases supplied at proof start. |
| lem:tail#count | def:weight-data | [article.tex:1525–1529](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1525-L1529) | Uses monomial eigenvalues and highest-weight contribution to normalizer. |
| lem:tail#count | eq:verma_multiplicity_bound | [article.tex:1531–1536](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1531-L1536) | Bounds coefficients by product (1-z^\|alpha\|)^(-1) <= (1-z)^(-N). |
| lem:tail | lem:tail#count | [article.tex:1539–1543](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1539-L1543) | Differentiates the geometric generating function to sum the first moment. |
| lem:ratio | def:weight-data | [article.tex:1565–1569](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1565-L1569) | Normalizations express ratio deficit as multiplicity difference average. |
| lem:ratio | lem:kostka | [article.tex:1565–1569](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1565-L1569) | Multiplicities monotonically increase, proving nonnegative deficit. |
| lem:ratio | lem:shallow_multiplicities | [article.tex:1571–1572](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1571-L1572) | Difference vanishes below depth g_mu, since g_nu>=g_mu. |
| lem:ratio | lem:tail | [article.tex:1581–1592](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1581-L1592) | Integer-depth Markov bound controls remaining mass. |
| lem:dim_ratio | ext:weyl-dimension | [article.tex:1609–1620](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1609-L1620) | Expands dimension ratio as finite product and bounds its deficit. |
| lem:dim_ratio | def:weight-data | [article.tex:1622–1623](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1622-L1623) | Supported terminal gap makes each nonzero denominator >=b_mu+1. |
| thm:main#branch | prop:choi | [article.tex:1342–1349](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1342-L1349) | Converts original PRV cloner into Cartan formula. |
| thm:main#branch | def:cartan-projectors | [article.tex:1350–1357](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1350-L1357) | Defines embedded target weight blocks. |
| thm:main#branch | def:weight-data | [article.tex:1373–1376](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1373-L1376) | Expands retained input branch over weight eigenvalues. |
| thm:main#branch | ext:trace-analysis | [article.tex:1359–1385](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1359-L1385) | Uses isometric invariance and omitted positive branches with known trace. |
| thm:main#all-depth | prop:choi | [article.tex:1629–1630](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1629-L1630) | Zero auxiliary weight gives forward identity. |
| thm:main#all-depth | prop:reverse | [article.tex:1629–1630](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1629-L1630) | Gives reverse identity in D=0 case. |
| thm:main#all-depth | lem:perturbation | [article.tex:1642–1653](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1642-L1653) | Uses shallow bound and r=1 equality; deep case uses trivial projector norm <=1. |
| eq:averaged_projector_deficit | thm:main#all-depth | [article.tex:1674–1678](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1674-L1678) | Uses cap definition and linear depth bound. |
| eq:averaged_projector_deficit | lem:tail | [article.tex:1681–1683](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1681-L1683) | Uniform first moment bound applies to both partitions. |
| eq:averaged_projector_deficit | def:cartan-projectors | [article.tex:1670–1672](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1670-L1672) | Identifies ranks of the two projectors. |
| eq:positive_deficit_trace | ext:trace-analysis | [article.tex:1697–1705](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1697-L1705) | Uses positive-part identity and its variational formula, then supplies order proof. |
| eq:forward_finite_deficit | lem:ratio | [article.tex:1710–1711](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1710-L1711) | p_mu>=p_nu from Z<=1. |
| eq:forward_finite_deficit | lem:dim_ratio | [article.tex:1712–1712](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1712-L1712) | Dimension ratio lies in (0,1]. |
| eq:forward_finite_deficit | thm:main#branch | [article.tex:1714–1717](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1714-L1717) | Retained Kraus branch equals dimension ratio times PQP. |
| eq:forward_finite_deficit | thm:main#all-depth | [article.tex:1733–1744](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1733-L1744) | Weight projector lower bound controls remainder trace. |
| eq:forward_finite_deficit | eq:averaged_projector_deficit | [article.tex:1741–1744](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1741-L1744) | Recognizes sum of deficits as M_nu. |
| eq:forward_finite_deficit | eq:positive_deficit_trace | [article.tex:1746–1755](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1746-L1755) | Remainder bounds full channel including omitted trace. |
| eq:reverse_finite_deficit | prop:choi | [article.tex:1759–1764](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1759-L1764) | Adjoint of Cartan formula supplies partial trace. |
| eq:reverse_finite_deficit | prop:reverse | [article.tex:1759–1764](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1759-L1764) | Normalized adjoint cancels dimension coefficients. |
| eq:reverse_finite_deficit | def:cartan-projectors | [article.tex:1771–1776](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1771-L1776) | Weight constraints give P_delta J=P_delta Q_delta J. |
| eq:reverse_finite_deficit | thm:main#all-depth | [article.tex:1778–1784](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1778-L1784) | QPQ lower bound controls retained reverse branch. |
| eq:reverse_finite_deficit | lem:ratio | [article.tex:1785–1788](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1785-L1788) | Converts p_nu to Z p_mu. |
| eq:reverse_finite_deficit | eq:averaged_projector_deficit | [article.tex:1793–1800](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1793-L1800) | Normalizes sum of e_delta terms as M_mu. |
| eq:reverse_finite_deficit | eq:positive_deficit_trace | [article.tex:1796–1800](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1796-L1800) | Remainder bounds trace distance for normalized reverse output. |
| thm:main#constant | eq:forward_finite_deficit | [article.tex:1804–1813](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1804-L1813) | Substitutes forward deficit estimate. |
| thm:main#constant | eq:reverse_finite_deficit | [article.tex:1804–1817](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1804-L1817) | Substitutes reverse deficit estimate. |
| thm:main#constant | eq:averaged_projector_deficit | [article.tex:1804–1805](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1804-L1805) | Bounds M_mu,M_nu uniformly. |
| thm:main#constant | lem:dim_ratio | [article.tex:1806–1823](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1806-L1823) | Controls dimension loss including rank-one case. |
| thm:main#constant | lem:ratio | [article.tex:1807–1819](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1807-L1819) | Controls scalar loss including rank-one Z=1. |
| thm:main#constant | lem:tail | [article.tex:1824–1826](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1824-L1826) | Names K(x) and its rank-one convention. |
| thm:main | thm:main#constant | [article.tex:1803–1826](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1803-L1826) | Combines finite estimates with common constant. |
| thm:main | thm:main#all-depth | [article.tex:1629–1631](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1629-L1631) | Separately discharges D=0 identity case. |
| thm:main | def:gen-cloner#channel | [article.tex:1139–1140](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1139-L1140) | Covariance reduces all orbit states to diagonal representative. |
| lem:weyl_asymptotic | ext:weyl-dimension | [article.tex:682–700](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L682-L700) | Expands factors, cancels zero-row factors, evaluates factorial denominator. |
| lem:weyl_asymptotic | eq:result | [article.tex:690–700](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L690-L700) | Identifies remaining product/logarithm with defined QMDL expression. |
| thm:achievability#code | def:code | [article.tex:705–709](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L705-L709) | Checks covariance implies common orbit error and independence from g. |
| thm:achievability#code | def:schur-data | [article.tex:710–727](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L710-L727) | Rank support and block structure justify supported terms and complement. |
| thm:achievability#code | def:gen-cloner#channel | [article.tex:728–729](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L728-L729) | Each block map is CPTP including atypical non-Cartan pairs. |
| thm:achievability#code | def:typical-target | [article.tex:728–729](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L728-L729) | Memory is selected padded target. |
| thm:achievability#code | def:schur-data | [article.tex:743–748](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L743-L748) | Known distribution and regenerated multiplicity states define decoder. |
| thm:achievability#padding | def:typical-target | [article.tex:731–740](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L731-L740) | Ceiling inequality plus rowwise typicality proves dominant nonnegative difference. |
| thm:achievability#error-split | thm:achievability#code | [article.tex:752–768](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L752-L768) | Uses encoded mixture and decoder sampled independently of measured lambda. |
| thm:achievability#error-split | ext:trace-analysis | [article.tex:756–785](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L756-L785) | Triangle, contraction, block norm, convexity and maximal distance handle cross terms and two tails. |
| lem:tail_prob | ext:schur-large-deviation | [article.tex:800–800](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L800-L800) | Sums pointwise bound over <=(n+1)^r diagrams. |
| lem:tail_prob | ext:pinsker | [article.tex:800–800](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L800-L800) | Converts divergence exponent to total variation. |
| eq:tail_prob_bound | def:typical-target | [article.tex:801–803](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L801-L803) | Outside typical set forces TV>log n/(2sqrt(2n)). |
| eq:tail_prob_bound | lem:tail_prob | [article.tex:803–807](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L803-L807) | Instantiates t to convert deviation into explicit tail. |
| thm:achievability#typical-error | thm:achievability#padding | [article.tex:810–819](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L810-L819) | Discharges partition, dominance, positive-gap and norm-scale premises. |
| thm:achievability#typical-error | thm:main | [article.tex:820–828](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L820-L828) | Finite bidirectional bound gives the displayed rate. |
| thm:achievability#rate | thm:achievability#error-split | [article.tex:829–834](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L829-L834) | Uses two-maxima-plus-two-tails estimate. |
| thm:achievability#rate | thm:achievability#typical-error | [article.tex:829–834](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L829-L834) | Supplies rate for both maxima. |
| thm:achievability#rate | eq:tail_prob_bound | [article.tex:829–834](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L829-L834) | Superpolynomial tail is absorbed into the rate. |
| thm:achievability#memory | def:typical-target | [article.tex:837–839](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L837-L839) | Target has required row estimates and zero unsupported rows. |
| thm:achievability#memory | lem:weyl_asymptotic | [article.tex:839–842](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L839-L842) | Applies with zeta_n=log n. |
| thm:achievability | thm:achievability#code | [article.tex:705–729](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L705-L729) | Produces valid physical channels and d=1 case. |
| thm:achievability | thm:achievability#rate | [article.tex:829–835](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L829-L835) | Proves required error rate. |
| thm:achievability | thm:achievability#memory | [article.tex:837–843](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L837-L843) | Proves memory expansion. |
| prop:compact_orbit_memory#order | ext:trace-analysis | [article.tex:879–883](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L879-L883) | Positivity and trace-one PSD state eigenvalue bound. |
| prop:compact_orbit_memory#average | prop:compact_orbit_memory#order | [article.tex:885–891](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L885-L891) | Tests operator inequality against P_g. |
| prop:compact_orbit_memory#average | ext:schur-lemma | [article.tex:885–891](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L885-L891) | Twirl P_g=I/dim H and trace preservation yield dimensions. |
| prop:compact_orbit_memory#average | ext:trace-analysis | [article.tex:888–889](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L888-L889) | Testing against effect P_g changes probability by at most half trace norm. |
| prop:compact_orbit_memory | prop:compact_orbit_memory#average | [article.tex:893–893](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L893-L893) | Rearranges the averaged inequality. |
| lem:sector_gap#top | def:weight-data | [article.tex:2029–2043](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2029-L2043) | Uses supported offsets, highest-line dimension one, and scalar monomial eigenvalues. |
| lem:sector_gap#normalizer | eq:verma_multiplicity_bound | [article.tex:2046–2051](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2046-L2051) | Termwise multiplicity upper bound. |
| lem:sector_gap#normalizer | def:weight-data | [article.tex:2046–2063](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2046-L2063) | Schur normalization divided by highest monomial produces x^-delta series. |
| lem:sector_gap#normalizer | lem:sector_gap#top | [article.tex:2075–2079](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2075-L2079) | Combines p1<=q_x p0 with uniform p0 bound. |
| lem:sector_gap | lem:sector_gap#normalizer | [article.tex:2074–2079](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2074-L2079) | Completes uniform gap; rank-one case retained at proof start. |
| thm:converse#transport | thm:achievability#code | [article.tex:941–955](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L941-L955) | Uses both directions of physical-to-target channels without changing memory. |
| thm:converse#transport | thm:achievability#typical-error | [article.tex:945–952](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L945-L952) | Forward and reverse reference-state errors follow from separate cloning bounds. |
| thm:converse#transport | eq:tail_prob_bound | [article.tex:945–952](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L945-L952) | Atypical contribution is controlled as in achievability proof. |
| thm:converse#transport | thm:achievability#error-split | [article.tex:945–952](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L945-L952) | Reference-state estimates established within encoder/decoder triangle argument. |
| thm:converse#transport | ext:trace-analysis | [article.tex:956–980](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L956-L980) | CPTP contraction and triangle inequality permit averaging arbitrary physical code error. |
| thm:converse#finite | thm:converse#transport | [article.tex:982–986](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L982-L986) | Transferred code has required small Haar-average target error. |
| thm:converse#finite | prop:compact_orbit_memory | [article.tex:982–986](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L982-L986) | Applies to target irrep with same memory. |
| thm:converse#finite | lem:sector_gap | [article.tex:982–986](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L982-L986) | Discharges simple-top positive-gap premise uniformly in Lambda. |
| thm:converse | thm:converse#finite | [article.tex:982–988](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L982-L988) | Supplies memory lower bound up to vanishing log factor. |
| thm:converse | lem:weyl_asymptotic | [article.tex:989–992](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L989-L992) | Applies target row asymptotics to evaluate log dimension. |
| thm:converse | def:typical-target | [article.tex:989–992](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L989-L992) | Padded rows meet Weyl asymptotic hypotheses. |
| thm:qmdl#uniform-converse | thm:converse | [article.tex:918–921](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L918-L921) | Source explicitly says average-error converse applies to worst-case criterion. |
| thm:qmdl#uniform-converse | def:code | [article.tex:918–921](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L918-L921) | Worst-case error in eq:error dominates normalized-Haar average. |
| thm:qmdl | thm:achievability | [article.tex:99–99](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L99-L99) | Source states theorem combines achievability and converse. |
| thm:qmdl | thm:converse | [article.tex:99–99](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L99-L99) | Haar-average lower bound is the stronger lower-bound statement. |
| thm:qmdl | thm:qmdl#uniform-converse | [article.tex:96–99](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L96-L99) | Uniform criterion follows by average<=supremum. |
| thm:qmdl | eq:result | [article.tex:86–94](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L86-L94) | All statements use defined L_{d,r}. |

## Complete mechanical and coarse-region inventory

All raw occurrences use one-based current-source locators. Excluded entries are accounted for, not certified. Proof-region entries are a manual supplement, not an assertion that every unnamed claim has been atomized.

| ID | Kind | Source | Raw command / region opening | Disposition | Nodes or exclusion reason |
|---|---|---|---|---|---|
| ex:frontmatter | excluded_region | [article.tex:1–74](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1-L74) | \documentclass[a4paper,onecolumn,11pt]{quantumarticle} | EXCLUDED | Preamble, front matter, abstract, and section heading; descriptive abstract is not an additional proof obligation. |
| label:001 | label | [article.tex:73–73](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L73-L73) | \label{sec:intro} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| citation:001 | citation | [article.tex:75–75](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L75-L75) | \cite{schumacher1995quantum} | EXCLUDED | Historical motivation, not consumed in selected theorem proofs. |
| ex:intro-context | excluded_region | [article.tex:75–76](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L75-L76) | Schumacher compression characterizes the memory needed to preserve quantum information together with its correlations with a reference~\cite{schumacher1995quantum}. A different problem arises when one only needs to reconstruct many identical copies of a state whose eigenbasis is unknown. The memory must retain this unknown basis information, but need not preserve a purification. We determine the optimal memory cost through its additive constant and construct a protocol attaining it. | EXCLUDED | Historical motivation, not consumed in selected theorem proofs. |
| region:coding-task | proof_region | [article.tex:77–83](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L77-L83) | The task is to compress identical and independent copies of a density matrix whose spectrum $x=(x_1,\ldots,x_d)$ is known but whose eigenbasis is not. Fix a reference state $\rho$ with this spectrum and write $\rho_g:=U(g)\rho U(g)^\dagger$ for $g\in\mathrm U(d)$. Let $M_n$ be the sole retained memory, including any classical register, and write $\|M_n\|:=\log\dim M_n$; all logarithms are base two. The encoder $\E_n:\mathcal B((\mathbb C^d)^{\otimes n})\to\mathcal B(M_n)$ and decoder $\D_n:\mathcal B(M_n)\to\mathcal B((\mathbb C^d)^{\otimes n})$ are completely positive trace-preserving maps, which may depend on $n$ and $x$ but not on~$g$. They form a $(\|M_n\|,\delta)$-code if | MAPPED | def:code |
| label:002 | label | [article.tex:78–78](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L78-L78) | \label{eq:error} | MAPPED | def:code |
| citation:002 | citation | [article.tex:83–83](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L83-L83) | \cite{yang2018compression} | EXCLUDED | Historical/expository citation; operative input is recorded at its actual use site and this occurrence adds no root prerequisite. |
| label:003 | label | [article.tex:85–85](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L85-L85) | \label{thm:qmdl} | MAPPED | thm:qmdl, eq:result |
| region:qmdl-statement | proof_region | [article.tex:85–99](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L85-L99) | \begin{thm}[Optimal memory cost]\label{thm:qmdl} | MAPPED | thm:qmdl, eq:result |
| env:thm:001 | theorem_like_environment | [article.tex:85–98](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L85-L98) | \begin{thm} | MAPPED | thm:qmdl |
| label:004 | label | [article.tex:90–90](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L90-L90) | \label{eq:result} | MAPPED | thm:qmdl, eq:result |
| cross_reference:001 | cross_reference | [article.tex:99–99](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L99-L99) | \ref{thm:qmdl} | MAPPED | thm:qmdl, eq:result |
| cross_reference:002 | cross_reference | [article.tex:99–99](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L99-L99) | \ref{sec:direct} | MAPPED | thm:qmdl, eq:result |
| cross_reference:003 | cross_reference | [article.tex:99–99](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L99-L99) | \ref{sec:converse} | MAPPED | thm:qmdl, eq:result |
| citation:003 | citation | [article.tex:101–101](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L101-L101) | \cite{yang2016optimal,yang2018compression} | EXCLUDED | Historical comparison and overview citations; operative mathematical inputs are inventoried at their proof use sites. |
| ex:intro-comparison | excluded_region | [article.tex:101–107](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L101-L107) | Earlier work established the leading memory cost~\cite{yang2016optimal,yang2018compression}. For qubits, the protocol of Yang, Chiribella, and Hayashi (YCH) already has an achievable spectrum-dependent constant. We prove the matching converse through that constant and extend the construction to qudits. The coefficient of $\log n$ counts half the real dimension of the orbit, while the additive term resolves the eigenvalue dependence. | EXCLUDED | Historical comparison and overview citations; operative mathematical inputs are inventoried at their proof use sites. |
| citation:004 | citation | [article.tex:107–107](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L107-L107) | \cite{gschwendtner2021programmability,lee2022quantum,aschieri2024equivariant} | EXCLUDED | Historical comparison and overview citations; operative mathematical inputs are inventoried at their proof use sites. |
| ex:intro-summary | excluded_region | [article.tex:108–131](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L108-L131) | We select the Parthasarathy--Ranga Rao--Varadarajan (PRV) component, | EXCLUDED | Informal preview repeats graph results; no separate proof route. |
| citation:005 | citation | [article.tex:110–110](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L110-L110) | \cite{werner1998optimal} | EXCLUDED | Informal preview repeats graph results; no separate proof route. |
| cross_reference:004 | cross_reference | [article.tex:112–112](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L112-L112) | \ref{thm:main} | EXCLUDED | Informal preview repeats graph results; no separate proof route. |
| cross_reference:005 | cross_reference | [article.tex:123–123](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L123-L123) | \ref{prop:compact_orbit_memory} | EXCLUDED | Informal preview repeats graph results; no separate proof route. |
| ex:redundancy-preview | excluded_region | [article.tex:133–143](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L133-L143) | Universal lossless quantum data compression uses one code for every | EXCLUDED | Preview of lossless coding overhead, downstream application outside roots. |
| cross_reference:006 | cross_reference | [article.tex:141–141](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L141-L141) | \ref{sec:redundancy} | EXCLUDED | Preview of lossless coding overhead, downstream application outside roots. |
| cross_reference:007 | cross_reference | [article.tex:142–142](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L142-L142) | \ref{app:unknown_spectrum} | EXCLUDED | Preview of lossless coding overhead, downstream application outside roots. |
| ex:geometry | excluded_region | [article.tex:145–164](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L145-L164) | The spectral terms in the memory cost also have a geometric | EXCLUDED | Geometric/free-entropy comparison and companion Letter are not prerequisites for Article Theorems 1 or 2. |
| cross_reference:008 | cross_reference | [article.tex:146–146](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L146-L146) | \ref{thm:qmdl} | EXCLUDED | Geometric/free-entropy comparison and companion Letter are not prerequisites for Article Theorems 1 or 2. |
| citation:006 | citation | [article.tex:156–156](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L156-L156) | \cite{paper1} | EXCLUDED | Geometric/free-entropy comparison and companion Letter are not prerequisites for Article Theorems 1 or 2. |
| citation:007 | citation | [article.tex:159–159](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L159-L159) | \cite{voiculescu1993analogues,voiculescu1994analogues,voiculescu2002free} | EXCLUDED | Geometric/free-entropy comparison and companion Letter are not prerequisites for Article Theorems 1 or 2. |
| cross_reference:009 | cross_reference | [article.tex:166–166](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L166-L166) | \ref{sec:related_works} | EXCLUDED | Navigational roadmap only. |
| ex:roadmap | excluded_region | [article.tex:166–173](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L166-L173) | Section~\ref{sec:related_works} reviews prior compression results, | EXCLUDED | Navigational roadmap only. |
| cross_reference:010 | cross_reference | [article.tex:167–167](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L167-L167) | \ref{sec:review} | EXCLUDED | Navigational roadmap only. |
| cross_reference:011 | cross_reference | [article.tex:168–168](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L168-L168) | \ref{sec:cloner} | EXCLUDED | Navigational roadmap only. |
| cross_reference:012 | cross_reference | [article.tex:169–169](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L169-L169) | \ref{sec:direct} | EXCLUDED | Navigational roadmap only. |
| cross_reference:013 | cross_reference | [article.tex:169–169](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L169-L169) | \ref{sec:converse} | EXCLUDED | Navigational roadmap only. |
| cross_reference:014 | cross_reference | [article.tex:170–170](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L170-L170) | \ref{sec:redundancy} | EXCLUDED | Navigational roadmap only. |
| cross_reference:015 | cross_reference | [article.tex:173–173](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L173-L173) | \ref{sec:fidelity} | EXCLUDED | Navigational roadmap only. |
| ex:background | excluded_region | [article.tex:176–292](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L176-L292) | \section{Background}\label{sec:background}  | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| label:005 | label | [article.tex:176–176](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L176-L176) | \label{sec:background} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| label:006 | label | [article.tex:177–177](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L177-L177) | \label{sec:related_works} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| citation:008 | citation | [article.tex:179–179](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L179-L179) | \cite{rissanen1978modeling} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| citation:009 | citation | [article.tex:180–180](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L180-L180) | \cite{plesch2010efficient} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| citation:010 | citation | [article.tex:184–184](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L184-L184) | \cite{rozema2014quantum} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| citation:011 | citation | [article.tex:186–186](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L186-L186) | \cite{koashi2001compressibility,koashi2001possible} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| citation:012 | citation | [article.tex:188–188](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L188-L188) | \cite{yang2016optimal} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| citation:013 | citation | [article.tex:191–191](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L191-L191) | \cite{yang2018quantum,yang2018compressionfor} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| citation:014 | citation | [article.tex:192–192](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L192-L192) | \cite{hayashi2017minimum} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| citation:015 | citation | [article.tex:194–194](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L194-L194) | \cite{yang2016efficient} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| citation:016 | citation | [article.tex:195–195](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L195-L195) | \cite{yang2018compression} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| citation:017 | citation | [article.tex:201–201](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L201-L201) | \cite{yang2025compression} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| citation:018 | citation | [article.tex:202–202](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L202-L202) | \cite{pivoluska2022implementation,xu2024experimental} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| label:007 | label | [article.tex:208–208](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L208-L208) | \label{sec:review} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| citation:019 | citation | [article.tex:209–209](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L209-L209) | \cite{yang2016optimal} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| label:008 | label | [article.tex:224–224](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L224-L224) | \label{eq:schur} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| label:009 | label | [article.tex:230–230](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L230-L230) | \label{eq:qJ} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| citation:020 | citation | [article.tex:238–238](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L238-L238) | \cite{yang2016optimal} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| citation:021 | citation | [article.tex:259–259](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L259-L259) | \cite{werner1998optimal} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| label:010 | label | [article.tex:260–260](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L260-L260) | \label{eq:werner} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| label:011 | label | [article.tex:274–274](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L274-L274) | \label{eq:qubitcloning} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| label:012 | label | [article.tex:288–288](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L288-L288) | \label{eq:achievable_qubit} | EXCLUDED | Prior-work survey and YCH qubit illustrative protocol; general proof does not invoke its correctness as a prerequisite or offer it as an alternative derivation of full roots. |
| label:013 | label | [article.tex:293–293](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L293-L293) | \label{sec:cloner} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| region:schur-data | proof_region | [article.tex:295–318](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L295-L318) | For qudits, Schur--Weyl duality gives | MAPPED | def:schur-data, ext:schur-weyl |
| label:014 | label | [article.tex:305–305](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L305-L305) | \label{eq:schur_d} | MAPPED | def:schur-data, ext:schur-weyl |
| label:015 | label | [article.tex:313–313](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L313-L313) | \label{eq:qlambda_def} | MAPPED | def:schur-data, ext:schur-weyl |
| cross_reference:016 | cross_reference | [article.tex:318–318](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L318-L318) | \ref{sec:direct} | MAPPED | def:schur-data, ext:schur-weyl |
| label:016 | label | [article.tex:321–321](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L321-L321) | \label{sec:definition} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| region:rational-domain | proof_region | [article.tex:322–338](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L322-L338) | We use finite-dimensional rational irreducible representations of | MAPPED | def:rational-weights |
| region:covariance-definition | proof_region | [article.tex:340–346](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L340-L346) | A channel $\map N:\mathcal B(\h_\mu)\to\mathcal B(\h_\nu)$ between | MAPPED | def:covariance |
| label:017 | label | [article.tex:342–342](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L342-L342) | \label{eq:covariance} | MAPPED | def:covariance |
| cross_reference:017 | cross_reference | [article.tex:346–346](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L346-L346) | \ref{fig:covariance_diagram} | MAPPED | def:covariance |
| ex:covariance-figure | excluded_region | [article.tex:348–356](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L348-L356) | \begin{figure} | EXCLUDED | Figure restates covariance definition; no new proof obligation. |
| cross_reference:018 | cross_reference | [article.tex:354–354](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L354-L354) | \eqref{eq:covariance} | EXCLUDED | Figure restates covariance definition; no new proof obligation. |
| label:018 | label | [article.tex:355–355](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L355-L355) | \label{fig:covariance_diagram} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| region:choi-commutant | proof_region | [article.tex:358–374](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L358-L374) | Equivalently, the Choi operator satisfies | MAPPED | ext:choi-covariance, ext:schur-lemma |
| citation:022 | citation | [article.tex:359–359](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L359-L359) | \cite[Lemma~11]{gschwendtner2021programmability} | MAPPED | ext:choi-covariance |
| label:019 | label | [article.tex:364–364](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L364-L364) | \label{eq:decomp} | MAPPED | ext:choi-covariance, ext:schur-lemma |
| label:020 | label | [article.tex:369–369](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L369-L369) | \label{eq:covChoi} | MAPPED | ext:choi-covariance, ext:schur-lemma |
| citation:023 | citation | [article.tex:375–375](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L375-L375) | \cite{mancinska2025classification} | EXCLUDED | Comparison to broader covariant-channel classification, not used by construction. |
| cross_reference:019 | cross_reference | [article.tex:375–375](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L375-L375) | \eqref{eq:covChoi} | EXCLUDED | Comparison to broader covariant-channel classification, not used by construction. |
| ex:classification-comparison | excluded_region | [article.tex:375–375](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L375-L375) | The structure in~\eqref{eq:covChoi} may be viewed as a simpler, irrep-level version of the more general covariant-channel classification in~\cite{mancinska2025classification}. | EXCLUDED | Comparison to broader covariant-channel classification, not used by construction. |
| region:prv-selection | proof_region | [article.tex:377–408](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L377-L408) | We choose the projector onto the PRV component, denoted by $\omega$. | MAPPED | def:dominance, ext:prv, def:rational-weights |
| cross_reference:020 | cross_reference | [article.tex:379–379](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L379-L379) | \ref{thm:main} | MAPPED | def:dominance, ext:prv, def:rational-weights |
| label:021 | label | [article.tex:382–382](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L382-L382) | \label{eq:dominance} | MAPPED | def:dominance, ext:prv, def:rational-weights |
| citation:024 | citation | [article.tex:392–392](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L392-L392) | \cite{parthasarathy1967,kumar1988proof} | MAPPED | ext:prv |
| region:cloner-definition-and-channel | proof_region | [article.tex:410–432](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L410-L432) | We therefore define our \emph{generalized cloning map} as follows. | MAPPED | def:gen-cloner, def:gen-cloner#channel |
| env:defn:001 | theorem_like_environment | [article.tex:412–420](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L412-L420) | \begin{defn} | MAPPED | def:gen-cloner, def:gen-cloner#channel |
| label:022 | label | [article.tex:414–414](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L414-L414) | \label{eq:gen_cloner} | MAPPED | def:gen-cloner, def:gen-cloner#channel |
| region:cartan-statement | proof_region | [article.tex:434–458](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L434-L458) | For symmetric powers this recovers Werner's cloner. For general irreps, | MAPPED | prop:choi |
| label:023 | label | [article.tex:438–438](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L438-L438) | \label{sec:properties} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| cross_reference:021 | cross_reference | [article.tex:440–440](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L440-L440) | \eqref{eq:werner} | MAPPED | prop:choi |
| label:024 | label | [article.tex:442–442](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L442-L442) | \label{prop:choi} | MAPPED | prop:choi |
| env:prop:001 | theorem_like_environment | [article.tex:442–456](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L442-L456) | \begin{prop} | MAPPED | prop:choi |
| cross_reference:022 | cross_reference | [article.tex:457–457](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L457-L457) | \ref{app:proofs} | MAPPED | prop:choi |
| env:proof:001 | proof_environment | [article.tex:457–458](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L457-L458) | \begin{proof} | MAPPED | prop:choi |
| ex:cartan-interpretation | excluded_region | [article.tex:460–500](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L460-L500) | To interpret the channel, we factor the target state through the same | EXCLUDED | GL complexification and exact factorization explain cloning interpretation; finite-error proof uses original Choi/Cartan channel identity and weight decomposition, not this factorization. |
| cross_reference:023 | cross_reference | [article.tex:465–465](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L465-L465) | \ref{prop:choi} | EXCLUDED | GL complexification and exact factorization explain cloning interpretation; finite-error proof uses original Choi/Cartan channel identity and weight decomposition, not this factorization. |
| label:025 | label | [article.tex:484–484](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L484-L484) | \label{eq:cartan_factorization} | EXCLUDED | GL complexification and exact factorization explain cloning interpretation; finite-error proof uses original Choi/Cartan channel identity and weight decomposition, not this factorization. |
| label:026 | label | [article.tex:488–488](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L488-L488) | \label{eq:cloner_substitution} | EXCLUDED | GL complexification and exact factorization explain cloning interpretation; finite-error proof uses original Choi/Cartan channel identity and weight decomposition, not this factorization. |
| cross_reference:024 | cross_reference | [article.tex:497–497](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L497-L497) | \eqref{eq:werner} | EXCLUDED | GL complexification and exact factorization explain cloning interpretation; finite-error proof uses original Choi/Cartan channel identity and weight decomposition, not this factorization. |
| cross_reference:025 | cross_reference | [article.tex:500–500](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L500-L500) | \ref{thm:main} | EXCLUDED | GL complexification and exact factorization explain cloning interpretation; finite-error proof uses original Choi/Cartan channel identity and weight decomposition, not this factorization. |
| ex:qubit-specialization | excluded_region | [article.tex:503–526](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L503-L526) | \subsubsection{Identity and qubit cases} | EXCLUDED | Identity/qubit examples; D=0 identity is separately supplied in the actual theorem proof and does not require the qubit remark. |
| env:rem:001 | theorem_like_environment | [article.tex:510–512](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L510-L512) | \begin{rem} | EXCLUDED | Identity/qubit examples; D=0 identity is separately supplied in the actual theorem proof and does not require the qubit remark. |
| cross_reference:026 | cross_reference | [article.tex:511–511](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L511-L511) | \eqref{eq:werner} | EXCLUDED | Identity/qubit examples; D=0 identity is separately supplied in the actual theorem proof and does not require the qubit remark. |
| cross_reference:027 | cross_reference | [article.tex:526–526](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L526-L526) | \eqref{eq:qubitcloning} | EXCLUDED | Identity/qubit examples; D=0 identity is separately supplied in the actual theorem proof and does not require the qubit remark. |
| ex:prv-dimension-remark | excluded_region | [article.tex:528–534](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L528-L534) | \subsubsection{Dominance order and dimension} | EXCLUDED | Dominance versus smallest-dimension warning and purity-amplification application; neither is used in selected proofs. |
| label:027 | label | [article.tex:529–529](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L529-L529) | \label{rem:prv_not_dim_min} | EXCLUDED | Dominance versus smallest-dimension warning and purity-amplification application; neither is used in selected proofs. |
| env:rem:002 | theorem_like_environment | [article.tex:529–531](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L529-L531) | \begin{rem} | EXCLUDED | Dominance versus smallest-dimension warning and purity-amplification application; neither is used in selected proofs. |
| citation:025 | citation | [article.tex:534–534](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L534-L534) | \cite{keyl2001rate,li2025purity} | EXCLUDED | Dominance versus smallest-dimension warning and purity-amplification application; neither is used in selected proofs. |
| region:reverse-statement | proof_region | [article.tex:537–556](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L537-L556) | \subsubsection{Reverse cloner} | MAPPED | prop:reverse |
| label:028 | label | [article.tex:540–540](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L540-L540) | \label{prop:reverse} | MAPPED | prop:reverse |
| env:prop:002 | theorem_like_environment | [article.tex:540–552](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L540-L552) | \begin{prop} | MAPPED | prop:reverse |
| env:proof:002 | proof_environment | [article.tex:553–555](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L553-L555) | \begin{proof} | MAPPED | prop:reverse |
| cross_reference:028 | cross_reference | [article.tex:554–554](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L554-L554) | \ref{app:proofs} | MAPPED | prop:reverse |
| region:cloning-accuracy-statement | proof_region | [article.tex:558–586](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L558-L586) | \subsubsection{Approximation of representation states} | MAPPED | thm:main |
| label:029 | label | [article.tex:562–562](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L562-L562) | \label{thm:main} | MAPPED | thm:main |
| env:thm:002 | theorem_like_environment | [article.tex:562–580](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L562-L580) | \begin{thm} | MAPPED | thm:main |
| label:030 | label | [article.tex:574–574](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L574-L574) | \label{eq:cloning_trace_bound} | MAPPED | thm:main |
| cross_reference:029 | cross_reference | [article.tex:586–586](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L586-L586) | \ref{sec:fidelity} | MAPPED | thm:main |
| ex:commutativity | excluded_region | [article.tex:588–604](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L588-L604) | Covariance also gives a useful structural property of the output. | EXCLUDED | Commutativity proposition is a valid structural side result but is not invoked by the retained-branch proof, achievability, or converse; no artificial dependency added. |
| label:031 | label | [article.tex:589–589](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L589-L589) | \label{prop:commutativity} | EXCLUDED | Commutativity proposition is a valid structural side result but is not invoked by the retained-branch proof, achievability, or converse; no artificial dependency added. |
| env:prop:003 | theorem_like_environment | [article.tex:589–597](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L589-L597) | \begin{prop} | EXCLUDED | Commutativity proposition is a valid structural side result but is not invoked by the retained-branch proof, achievability, or converse; no artificial dependency added. |
| env:proof:003 | proof_environment | [article.tex:598–604](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L598-L604) | \begin{proof} | EXCLUDED | Commutativity proposition is a valid structural side result but is not invoked by the retained-branch proof, achievability, or converse; no artificial dependency added. |
| label:032 | label | [article.tex:606–606](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L606-L606) | \label{sec:direct} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| region:typical-target-protocol | proof_region | [article.tex:606–644](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L606-L644) | \section{Achievability}\label{sec:direct} | MAPPED | def:typical-target, thm:achievability#code |
| label:033 | label | [article.tex:611–611](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L611-L611) | \label{eq:typical_set} | MAPPED | def:typical-target, thm:achievability#code |
| label:034 | label | [article.tex:619–619](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L619-L619) | \label{eq:target_rep} | MAPPED | def:typical-target, thm:achievability#code |
| cross_reference:030 | cross_reference | [article.tex:630–630](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L630-L630) | \eqref{eq:optimal_encoder} | MAPPED | def:typical-target, thm:achievability#code |
| cross_reference:031 | cross_reference | [article.tex:633–633](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L633-L633) | \eqref{eq:target_rep} | MAPPED | def:typical-target, thm:achievability#code |
| cross_reference:032 | cross_reference | [article.tex:636–636](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L636-L636) | \eqref{eq:optimal_decoder} | MAPPED | def:typical-target, thm:achievability#code |
| cross_reference:033 | cross_reference | [article.tex:644–644](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L644-L644) | \ref{thm:qmdl} | MAPPED | def:typical-target, thm:achievability#code |
| label:035 | label | [article.tex:645–645](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L645-L645) | \label{thm:achievability} | MAPPED | thm:achievability |
| region:achievability-statement | proof_region | [article.tex:645–661](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L645-L661) | \begin{thm}[Achievability]\label{thm:achievability} | MAPPED | thm:achievability |
| env:thm:003 | theorem_like_environment | [article.tex:645–661](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L645-L661) | \begin{thm} | MAPPED | thm:achievability |
| cross_reference:034 | cross_reference | [article.tex:651–651](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L651-L651) | \eqref{eq:result} | MAPPED | thm:achievability |
| ex:pure-memory-specialcase | excluded_region | [article.tex:663–666](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L663-L666) | For pure states, we have | EXCLUDED | Displayed pure-state specialization of achieving cost; follows from root and is not its prerequisite. |
| label:036 | label | [article.tex:664–664](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L664-L664) | \label{eq:achievable_pure} | EXCLUDED | Displayed pure-state specialization of achieving cost; follows from root and is not its prerequisite. |
| region:weyl-asymptotic | proof_region | [article.tex:668–701](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L668-L701) | The memory size is $\log\dim\h_{\Lambda}$, which we evaluate | MAPPED | lem:weyl_asymptotic, ext:weyl-dimension |
| label:037 | label | [article.tex:671–671](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L671-L671) | \label{lem:weyl_asymptotic} | MAPPED | lem:weyl_asymptotic, ext:weyl-dimension |
| env:lem:001 | theorem_like_environment | [article.tex:671–680](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L671-L680) | \begin{lem} | MAPPED | lem:weyl_asymptotic |
| env:proof:004 | proof_environment | [article.tex:681–701](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L681-L701) | \begin{proof} | MAPPED | lem:weyl_asymptotic |
| label:038 | label | [article.tex:683–683](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L683-L683) | \label{eq:weyl_dim} | MAPPED | lem:weyl_asymptotic, ext:weyl-dimension |
| cross_reference:035 | cross_reference | [article.tex:704–704](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L704-L704) | \ref{thm:achievability} | MAPPED | thm:achievability#code |
| env:proof:005 | proof_environment | [article.tex:704–844](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L704-L844) | \begin{proof} | MAPPED | thm:achievability#code, thm:achievability#padding, thm:achievability#error-split, lem:tail_prob, eq:tail_prob_bound, thm:achievability#typical-error, thm:achievability#rate, thm:achievability#memory, thm:achievability |
| region:physical-encoder | proof_region | [article.tex:704–729](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L704-L729) | \begin{proof}[Proof of Theorem~\ref{thm:achievability}] | MAPPED | thm:achievability#code |
| label:039 | label | [article.tex:719–719](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L719-L719) | \label{eq:optimal_encoder} | MAPPED | thm:achievability#code |
| cross_reference:036 | cross_reference | [article.tex:729–729](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L729-L729) | \eqref{eq:gen_cloner} | MAPPED | thm:achievability#code |
| cross_reference:037 | cross_reference | [article.tex:729–729](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L729-L729) | \eqref{eq:target_rep} | MAPPED | thm:achievability#code |
| region:padding | proof_region | [article.tex:731–740](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L731-L740) | This padding ensures that $\Lambda-\lambda$ is dominant for every | MAPPED | thm:achievability#padding |
| region:decoder-and-error-split | proof_region | [article.tex:743–785](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L743-L785) | The corresponding decoder maps back to the original blocks: | MAPPED | thm:achievability#code, thm:achievability#error-split |
| label:040 | label | [article.tex:744–744](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L744-L744) | \label{eq:optimal_decoder} | MAPPED | thm:achievability#code, thm:achievability#error-split |
| label:041 | label | [article.tex:775–775](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L775-L775) | \label{eq:error_triangle} | MAPPED | thm:achievability#code, thm:achievability#error-split |
| cross_reference:038 | cross_reference | [article.tex:779–779](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L779-L779) | \eqref{eq:error_triangle} | MAPPED | thm:achievability#code, thm:achievability#error-split |
| label:042 | label | [article.tex:780–780](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L780-L780) | \label{eq:error_twoterms} | MAPPED | thm:achievability#code, thm:achievability#error-split |
| region:sanov-event | proof_region | [article.tex:787–800](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L787-L800) | The tail mass is controlled by Sanov's theorem via the following lemma: | MAPPED | lem:tail_prob, ext:schur-large-deviation, ext:pinsker |
| citation:026 | citation | [article.tex:788–788](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L788-L788) | \cite{yang2016efficient,christandl2006spectra,o2021quantum,hayashi2017group} | MAPPED | ext:schur-large-deviation |
| label:043 | label | [article.tex:788–788](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L788-L788) | \label{lem:tail_prob} | MAPPED | lem:tail_prob, ext:schur-large-deviation, ext:pinsker |
| env:lem:002 | theorem_like_environment | [article.tex:788–799](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L788-L799) | \begin{lem} | MAPPED | lem:tail_prob |
| citation:027 | citation | [article.tex:800–800](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L800-L800) | \cite{christandl2006spectra} | MAPPED | ext:schur-large-deviation |
| cross_reference:039 | cross_reference | [article.tex:800–800](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L800-L800) | \ref{lem:tail_prob} | MAPPED | ext:pinsker |
| region:atypical-tail | proof_region | [article.tex:801–808](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L801-L808) | The distribution $q_{\lambda,n}$ is supported on diagrams with at most $r$ rows. Hence, if $\lambda$ lies in its support but not in $\mathcal{T}_{x,n}$, then for some $i$, | MAPPED | eq:tail_prob_bound |
| cross_reference:040 | cross_reference | [article.tex:803–803](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L803-L803) | \ref{lem:tail_prob} | MAPPED | eq:tail_prob_bound |
| label:044 | label | [article.tex:804–804](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L804-L804) | \label{eq:tail_prob_bound} | MAPPED | eq:tail_prob_bound |
| cross_reference:041 | cross_reference | [article.tex:810–810](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L810-L810) | \eqref{eq:error_twoterms} | MAPPED | thm:achievability#padding, thm:achievability#typical-error |
| cross_reference:042 | cross_reference | [article.tex:810–810](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L810-L810) | \ref{thm:main} | MAPPED | thm:achievability#padding, thm:achievability#typical-error |
| region:typical-cloning | proof_region | [article.tex:810–828](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L810-L828) | For typical states $\lambda\in\mathcal{T}_{x,n}$, the two maxima in~\eqref{eq:error_twoterms} are the forward and reverse cloning errors of Theorem~\ref{thm:main}, applied with $\mu=\lambda$ and $\nu=\Lambda$. The dominance hypothesis holds by construction, and $b_\lambda=\Omega(n)$ uniformly on the typical set because the positive eigenvalues are distinct and, when $r<d$, $x_r>0$. | MAPPED | thm:achievability#padding, thm:achievability#typical-error |
| cross_reference:043 | cross_reference | [article.tex:820–820](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L820-L820) | \ref{thm:main} | MAPPED | thm:achievability#padding, thm:achievability#typical-error |
| cross_reference:044 | cross_reference | [article.tex:829–829](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L829-L829) | \eqref{eq:error_twoterms} | MAPPED | thm:achievability#rate |
| cross_reference:045 | cross_reference | [article.tex:829–829](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L829-L829) | \eqref{eq:tail_prob_bound} | MAPPED | thm:achievability#rate |
| region:total-rate | proof_region | [article.tex:829–835](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L829-L835) | Thus each typical maximum in~\eqref{eq:error_twoterms} has this order, and~\eqref{eq:tail_prob_bound} yields | MAPPED | thm:achievability#rate |
| region:memory-asymptotic | proof_region | [article.tex:837–844](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L837-L844) | The memory is $\h_{\Lambda}$. Since | MAPPED | thm:achievability#memory |
| cross_reference:046 | cross_reference | [article.tex:839–839](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L839-L839) | \ref{lem:weyl_asymptotic} | MAPPED | thm:achievability#memory |
| ex:koashi-context | excluded_region | [article.tex:846–852](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L846-L852) | \section{Converse}\label{sec:converse} | EXCLUDED | Koashi-Imoto citation motivates a separately proved finite orbit bound; proof does not invoke Koashi-Imoto theorem. |
| label:045 | label | [article.tex:846–846](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L846-L846) | \label{sec:converse} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| citation:028 | citation | [article.tex:849–849](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L849-L849) | \cite{koashi2001compressibility,koashi2001possible} | EXCLUDED | Koashi-Imoto citation motivates a separately proved finite orbit bound; proof does not invoke Koashi-Imoto theorem. |
| label:046 | label | [article.tex:854–854](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L854-L854) | \label{prop:compact_orbit_memory} | MAPPED | prop:compact_orbit_memory, prop:compact_orbit_memory#order, prop:compact_orbit_memory#average |
| region:orbit-bound | proof_region | [article.tex:854–894](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L854-L894) | \begin{prop}[Memory bound for irreducible orbits]\label{prop:compact_orbit_memory} | MAPPED | prop:compact_orbit_memory, prop:compact_orbit_memory#order, prop:compact_orbit_memory#average |
| env:prop:004 | theorem_like_environment | [article.tex:854–876](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L854-L876) | \begin{prop} | MAPPED | prop:compact_orbit_memory |
| label:047 | label | [article.tex:873–873](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L873-L873) | \label{eq:compact_orbit_memory} | MAPPED | prop:compact_orbit_memory, prop:compact_orbit_memory#order, prop:compact_orbit_memory#average |
| env:proof:006 | proof_environment | [article.tex:877–894](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L877-L894) | \begin{proof} | MAPPED | ext:schur-lemma, prop:compact_orbit_memory, prop:compact_orbit_memory#order, prop:compact_orbit_memory#average |
| ex:koashi-corollary | excluded_region | [article.tex:896–899](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L896-L899) | At zero error this recovers the Koashi--Imoto incompressibility bound | EXCLUDED | Zero-error interpretation/corollary of finite orbit proposition, not a prerequisite. |
| label:048 | label | [article.tex:901–901](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L901-L901) | \label{lem:sector_gap} | MAPPED | lem:sector_gap |
| region:gap-statement | proof_region | [article.tex:901–916](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L901-L916) | \begin{lem}[Uniform spectral gap]\label{lem:sector_gap} | MAPPED | lem:sector_gap |
| env:lem:003 | theorem_like_environment | [article.tex:901–913](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L901-L913) | \begin{lem} | MAPPED | lem:sector_gap |
| cross_reference:047 | cross_reference | [article.tex:911–911](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L911-L911) | \ref{prop:compact_orbit_memory} | MAPPED | lem:sector_gap |
| env:proof:007 | proof_environment | [article.tex:914–916](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L914-L916) | \begin{proof} | MAPPED | lem:sector_gap |
| cross_reference:048 | cross_reference | [article.tex:915–915](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L915-L915) | \ref{app:proofs} | MAPPED | lem:sector_gap |
| region:uniform-from-average | proof_region | [article.tex:918–921](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L918-L921) | We transfer an arbitrary compression code to the padded target | MAPPED | thm:qmdl#uniform-converse |
| cross_reference:049 | cross_reference | [article.tex:921–921](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L921-L921) | \eqref{eq:error} | MAPPED | thm:qmdl#uniform-converse |
| label:049 | label | [article.tex:923–923](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L923-L923) | \label{thm:converse} | MAPPED | thm:converse |
| region:converse-statement | proof_region | [article.tex:923–939](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L923-L939) | \begin{thm}[Converse]\label{thm:converse} | MAPPED | thm:converse |
| env:thm:004 | theorem_like_environment | [article.tex:923–939](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L923-L939) | \begin{thm} | MAPPED | thm:converse |
| cross_reference:050 | cross_reference | [article.tex:938–938](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L938-L938) | \eqref{eq:result} | MAPPED | thm:converse |
| env:proof:008 | proof_environment | [article.tex:940–993](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L940-L993) | \begin{proof} | MAPPED | thm:converse#transport, thm:converse#finite, thm:converse |
| region:code-transport | proof_region | [article.tex:940–981](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L940-L981) | \begin{proof} | MAPPED | thm:converse#transport |
| cross_reference:051 | cross_reference | [article.tex:943–943](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L943-L943) | \eqref{eq:optimal_encoder} | MAPPED | thm:converse#transport |
| cross_reference:052 | cross_reference | [article.tex:943–943](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L943-L943) | \eqref{eq:optimal_decoder} | MAPPED | thm:converse#transport |
| cross_reference:053 | cross_reference | [article.tex:982–982](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L982-L982) | \ref{prop:compact_orbit_memory} | MAPPED | thm:converse#finite, thm:converse |
| region:converse-limit | proof_region | [article.tex:982–993](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L982-L993) | Proposition~\ref{prop:compact_orbit_memory} and | MAPPED | thm:converse#finite, thm:converse |
| cross_reference:054 | cross_reference | [article.tex:983–983](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L983-L983) | \ref{lem:sector_gap} | MAPPED | thm:converse#finite, thm:converse |
| cross_reference:055 | cross_reference | [article.tex:989–989](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L989-L989) | \ref{lem:weyl_asymptotic} | MAPPED | thm:converse#finite, thm:converse |
| ex:lossless-overhead | excluded_region | [article.tex:995–1126](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L995-L1126) | \section{Universal quantum data compression and QMDL}\label{sec:redundancy} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| label:050 | label | [article.tex:995–995](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L995-L995) | \label{sec:redundancy} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| label:051 | label | [article.tex:1002–1002](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1002-L1002) | \label{eq:orbit_redundancy} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| cross_reference:056 | cross_reference | [article.tex:1006–1006](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1006-L1006) | \ref{thm:qmdl} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| cross_reference:057 | cross_reference | [article.tex:1007–1007](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1007-L1007) | \eqref{eq:block_entropy_limit} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| citation:029 | citation | [article.tex:1017–1017](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1017-L1017) | \cite{schumacher2001indeterminate,bostroem2002lossless,hayashi2010universal} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| label:052 | label | [article.tex:1037–1037](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1037-L1037) | \label{prop:orbit_redundancy} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| env:prop:005 | theorem_like_environment | [article.tex:1037–1052](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1037-L1052) | \begin{prop} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| label:053 | label | [article.tex:1040–1040](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1040-L1040) | \label{eq:orbit_minimax} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| label:054 | label | [article.tex:1047–1047](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1047-L1047) | \label{eq:invariant_split} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| env:proof:009 | proof_environment | [article.tex:1053–1070](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1053-L1070) | \begin{proof} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| cross_reference:058 | cross_reference | [article.tex:1075–1075](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1075-L1075) | \eqref{eq:orbit_minimax} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| label:055 | label | [article.tex:1084–1084](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1084-L1084) | \label{lem:block_entropy} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| env:lem:004 | theorem_like_environment | [article.tex:1084–1100](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1084-L1100) | \begin{lem} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| label:056 | label | [article.tex:1094–1094](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1094-L1094) | \label{eq:block_entropy_limit} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| env:proof:010 | proof_environment | [article.tex:1101–1103](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1101-L1103) | \begin{proof} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| cross_reference:059 | cross_reference | [article.tex:1102–1102](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1102-L1102) | \ref{app:proofs} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| cross_reference:060 | cross_reference | [article.tex:1105–1105](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1105-L1105) | \eqref{eq:block_entropy_limit} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| cross_reference:061 | cross_reference | [article.tex:1109–1109](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1109-L1109) | \ref{lem:block_entropy} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| cross_reference:062 | cross_reference | [article.tex:1110–1110](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1110-L1110) | \ref{lem:weyl_asymptotic} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| cross_reference:063 | cross_reference | [article.tex:1112–1112](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1112-L1112) | \eqref{eq:tail_prob_bound} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| cross_reference:064 | cross_reference | [article.tex:1119–1119](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1119-L1119) | \eqref{eq:orbit_minimax} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| cross_reference:065 | cross_reference | [article.tex:1120–1120](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1120-L1120) | \eqref{eq:orbit_redundancy} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| cross_reference:066 | cross_reference | [article.tex:1124–1124](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1124-L1124) | \eqref{eq:invariant_split} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| cross_reference:067 | cross_reference | [article.tex:1125–1125](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1125-L1125) | \ref{app:unknown_spectrum} | EXCLUDED | Universal lossless coding overhead and block entropy are downstream applications; excluded from requested Article Theorems 1/2 closure. |
| label:057 | label | [article.tex:1128–1128](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1128-L1128) | \label{sec:fidelity} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| region:technical-proof-overview | proof_region | [article.tex:1128–1153](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1128-L1153) | \section{Trace-distance bounds for generalized cloning}\label{sec:fidelity} | MAPPED | thm:main |
| cross_reference:068 | cross_reference | [article.tex:1130–1130](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1130-L1130) | \ref{thm:main} | MAPPED | thm:main |
| cross_reference:069 | cross_reference | [article.tex:1136–1136](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1136-L1136) | \ref{fig:cloning_proof} | MAPPED | thm:main |
| cross_reference:070 | cross_reference | [article.tex:1138–1138](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1138-L1138) | \ref{sec:prelim} | MAPPED | thm:main |
| label:058 | label | [article.tex:1144–1144](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1144-L1144) | \label{sec:prelim} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| cross_reference:071 | cross_reference | [article.tex:1147–1147](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1147-L1147) | \ref{thm:main} | MAPPED | thm:main |
| region:weight-preliminaries | proof_region | [article.tex:1155–1184](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1155-L1184) | We use the standard basis $e_i$ and the Euclidean | MAPPED | def:weight-data, ext:weight-theory |
| citation:030 | citation | [article.tex:1156–1156](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1156-L1156) | \cite{fulton1991representation} | MAPPED | ext:weight-theory |
| region:verma-bound | proof_region | [article.tex:1186–1198](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1186-L1198) | Let $\mathsf P_s(\delta)$ count the expressions of $\delta$ as a | MAPPED | eq:verma_multiplicity_bound |
| label:059 | label | [article.tex:1195–1195](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1195-L1195) | \label{eq:verma_multiplicity_bound} | MAPPED | eq:verma_multiplicity_bound |
| label:060 | label | [article.tex:1200–1200](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1200-L1200) | \label{lem:kostka} | MAPPED | lem:kostka, ext:gt-patterns |
| region:multiplicity-injection | proof_region | [article.tex:1200–1216](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1200-L1216) | \begin{lem}[Multiplicity monotonicity]\label{lem:kostka} | MAPPED | lem:kostka, ext:gt-patterns |
| env:lem:005 | theorem_like_environment | [article.tex:1200–1204](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1200-L1204) | \begin{lem} | MAPPED | lem:kostka |
| env:proof:011 | proof_environment | [article.tex:1205–1216](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1205-L1216) | \begin{proof} | MAPPED | lem:kostka |
| region:state-eigenvalues-and-gaps | proof_region | [article.tex:1218–1253](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1218-L1253) | For $\rho=\operatorname{diag}(x_1,\ldots,x_r,0,\ldots,0)$ and a | MAPPED | def:weight-data |
| citation:031 | citation | [article.tex:1235–1235](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1235-L1235) | \cite{macdonald1995symmetric} | MAPPED | ext:weight-theory |
| cross_reference:072 | cross_reference | [article.tex:1243–1243](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1243-L1243) | \ref{thm:main} | MAPPED | def:weight-data |
| region:cartan-weight-projectors | proof_region | [article.tex:1255–1279](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1255-L1279) | On $\mathcal H_\mu\otimes\mathcal H_\omega$, each Lie-algebra | MAPPED | def:cartan-projectors, ext:cartan-duality |
| cross_reference:073 | cross_reference | [article.tex:1261–1261](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1261-L1261) | \ref{prop:choi} | MAPPED | def:cartan-projectors, ext:cartan-duality |
| label:061 | label | [article.tex:1268–1268](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1268-L1268) | \label{eq:proj_mu_omega} | MAPPED | def:cartan-projectors, ext:cartan-duality |
| region:casimir-convention | proof_region | [article.tex:1281–1292](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1281-L1292) | The quadratic Casimir uses the generators of the ambient | MAPPED | ext:casimir |
| label:062 | label | [article.tex:1294–1294](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1294-L1294) | \label{sec:proof} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| ex:cloning-figure | excluded_region | [article.tex:1296–1339](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1296-L1339) | \begin{figure}[!t] | EXCLUDED | Diagram restates forward proof; not a separate conjunctive dependency or alternative route. |
| cross_reference:074 | cross_reference | [article.tex:1305–1305](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1305-L1305) | \eqref{eq:kraus_proj} | EXCLUDED | Diagram restates forward proof; not a separate conjunctive dependency or alternative route. |
| cross_reference:075 | cross_reference | [article.tex:1310–1310](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1310-L1310) | \ref{lem:ratio} | EXCLUDED | Diagram restates forward proof; not a separate conjunctive dependency or alternative route. |
| cross_reference:076 | cross_reference | [article.tex:1316–1316](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1316-L1316) | \eqref{eq:kraus_proj} | EXCLUDED | Diagram restates forward proof; not a separate conjunctive dependency or alternative route. |
| cross_reference:077 | cross_reference | [article.tex:1321–1321](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1321-L1321) | \ref{lem:dim_ratio} | EXCLUDED | Diagram restates forward proof; not a separate conjunctive dependency or alternative route. |
| cross_reference:078 | cross_reference | [article.tex:1325–1325](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1325-L1325) | \ref{lem:shallow_multiplicities} | EXCLUDED | Diagram restates forward proof; not a separate conjunctive dependency or alternative route. |
| cross_reference:079 | cross_reference | [article.tex:1325–1325](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1325-L1325) | \ref{lem:perturbation} | EXCLUDED | Diagram restates forward proof; not a separate conjunctive dependency or alternative route. |
| cross_reference:080 | cross_reference | [article.tex:1328–1328](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1328-L1328) | \ref{lem:tail} | EXCLUDED | Diagram restates forward proof; not a separate conjunctive dependency or alternative route. |
| label:063 | label | [article.tex:1338–1338](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1338-L1338) | \label{fig:cloning_proof} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| region:retained-branch | proof_region | [article.tex:1341–1391](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1341-L1391) | \emph{Stage 1: the highest-weight Kraus branch.} | MAPPED | thm:main#branch |
| cross_reference:081 | cross_reference | [article.tex:1344–1344](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1344-L1344) | \ref{prop:choi} | MAPPED | thm:main#branch |
| label:064 | label | [article.tex:1345–1345](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1345-L1345) | \label{eq:embedded_channel} | MAPPED | thm:main#branch |
| label:065 | label | [article.tex:1352–1352](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1352-L1352) | \label{eq:embedded_target} | MAPPED | thm:main#branch |
| label:066 | label | [article.tex:1360–1360](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1360-L1360) | \label{eq:isometric_invariance_forward} | MAPPED | thm:main#branch |
| label:067 | label | [article.tex:1365–1365](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1365-L1365) | \label{eq:kraus_proj} | MAPPED | thm:main#branch |
| label:068 | label | [article.tex:1372–1372](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1372-L1372) | \label{eq:forward_monotonicity} | MAPPED | thm:main#branch |
| label:069 | label | [article.tex:1382–1382](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1382-L1382) | \label{eq:branch_trace_comparison} | MAPPED | thm:main#branch |
| region:shallow-statement | proof_region | [article.tex:1393–1410](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1393-L1410) | \emph{Stage 2: estimating the projectors.} We first identify the | MAPPED | lem:shallow_multiplicities |
| label:070 | label | [article.tex:1397–1397](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1397-L1397) | \label{lem:shallow_multiplicities} | MAPPED | lem:shallow_multiplicities |
| env:lem:006 | theorem_like_environment | [article.tex:1397–1406](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1397-L1406) | \begin{lem} | MAPPED | lem:shallow_multiplicities |
| cross_reference:082 | cross_reference | [article.tex:1405–1405](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1405-L1405) | \ref{sec:prelim} | MAPPED | lem:shallow_multiplicities |
| env:proof:012 | proof_environment | [article.tex:1408–1410](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1408-L1410) | \begin{proof} | MAPPED | lem:shallow_multiplicities |
| cross_reference:083 | cross_reference | [article.tex:1409–1409](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1409-L1409) | \ref{app:proofs} | MAPPED | lem:shallow_multiplicities |
| label:071 | label | [article.tex:1412–1412](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1412-L1412) | \label{lem:perturbation} | MAPPED | lem:perturbation |
| region:perturbation-statement | proof_region | [article.tex:1412–1433](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1412-L1433) | \begin{lem}[Highest-weight subspace perturbation]\label{lem:perturbation} | MAPPED | lem:perturbation |
| env:lem:007 | theorem_like_environment | [article.tex:1412–1433](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1412-L1433) | \begin{lem} | MAPPED | lem:perturbation |
| cross_reference:084 | cross_reference | [article.tex:1417–1417](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1417-L1417) | \eqref{eq:proj_mu_omega} | MAPPED | lem:perturbation |
| label:072 | label | [article.tex:1427–1427](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1427-L1427) | \label{eq:projector_casimir_bound} | MAPPED | lem:perturbation |
| env:proof:013 | proof_environment | [article.tex:1435–1500](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1435-L1500) | \begin{proof} | MAPPED | lem:perturbation, lem:perturbation#rank, eq:casimir_slice_gap, eq:casimir_deficit_compression, lem:perturbation#projector-norm |
| region:projector-ranks | proof_region | [article.tex:1435–1445](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1435-L1445) | \begin{proof} | MAPPED | lem:perturbation#rank |
| cross_reference:085 | cross_reference | [article.tex:1439–1439](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1439-L1439) | \ref{lem:shallow_multiplicities} | MAPPED | lem:perturbation#rank |
| region:casimir-slice-gap | proof_region | [article.tex:1447–1464](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1447-L1464) | Restrict the total quadratic Casimir $C_2$ to this weight space. | MAPPED | eq:casimir_slice_gap |
| label:073 | label | [article.tex:1454–1454](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1454-L1454) | \label{eq:casimir_slice_gap} | MAPPED | eq:casimir_slice_gap |
| region:casimir-deficit | proof_region | [article.tex:1466–1480](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1466-L1480) | It remains to evaluate the Casimir deficit on $Q_\delta$. In the tensor-product | MAPPED | eq:casimir_deficit_compression |
| label:074 | label | [article.tex:1478–1478](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1478-L1478) | \label{eq:casimir_deficit_compression} | MAPPED | eq:casimir_deficit_compression |
| region:projector-norm | proof_region | [article.tex:1481–1500](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1481-L1500) | Consequently, | MAPPED | lem:perturbation#projector-norm |
| cross_reference:086 | cross_reference | [article.tex:1499–1499](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1499-L1499) | \eqref{eq:projector_casimir_bound} | MAPPED | lem:perturbation#projector-norm |
| region:mean-depth | proof_region | [article.tex:1502–1545](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1502-L1545) | \emph{Stage 3: averaging the block bounds.} | MAPPED | lem:tail, lem:tail#count |
| label:075 | label | [article.tex:1507–1507](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1507-L1507) | \label{lem:tail} | MAPPED | lem:tail, lem:tail#count |
| env:lem:008 | theorem_like_environment | [article.tex:1507–1521](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1507-L1521) | \begin{lem} | MAPPED | lem:tail |
| cross_reference:087 | cross_reference | [article.tex:1510–1510](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1510-L1510) | \ref{lem:sector_gap} | MAPPED | lem:tail, lem:tail#count |
| label:076 | label | [article.tex:1516–1516](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1516-L1516) | \label{eq:uniform_mean_depth} | MAPPED | lem:tail, lem:tail#count |
| env:proof:014 | proof_environment | [article.tex:1522–1545](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1522-L1545) | \begin{proof} | MAPPED | lem:tail, lem:tail#count |
| cross_reference:088 | cross_reference | [article.tex:1531–1531](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1531-L1531) | \eqref{eq:verma_multiplicity_bound} | MAPPED | lem:tail, lem:tail#count |
| region:eigenvalue-ratio | proof_region | [article.tex:1547–1594](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1547-L1594) | The eigenvalue ratio $p_\nu(\delta)/p_\mu(\delta)$ is independent | MAPPED | lem:ratio |
| label:077 | label | [article.tex:1551–1551](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1551-L1551) | \label{lem:ratio} | MAPPED | lem:ratio |
| env:lem:009 | theorem_like_environment | [article.tex:1551–1563](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1551-L1563) | \begin{lem} | MAPPED | lem:ratio |
| env:proof:015 | proof_environment | [article.tex:1564–1594](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1564-L1594) | \begin{proof} | MAPPED | lem:ratio |
| cross_reference:089 | cross_reference | [article.tex:1565–1565](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1565-L1565) | \ref{lem:kostka} | MAPPED | lem:ratio |
| cross_reference:090 | cross_reference | [article.tex:1572–1572](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1572-L1572) | \ref{lem:shallow_multiplicities} | MAPPED | lem:ratio |
| cross_reference:091 | cross_reference | [article.tex:1591–1591](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1591-L1591) | \ref{lem:tail} | MAPPED | lem:ratio |
| cross_reference:092 | cross_reference | [article.tex:1592–1592](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1592-L1592) | \eqref{eq:uniform_mean_depth} | MAPPED | lem:ratio |
| region:dimension-ratio | proof_region | [article.tex:1596–1624](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1596-L1624) | The other scalar factor is the ratio of representation dimensions. | MAPPED | lem:dim_ratio |
| label:078 | label | [article.tex:1598–1598](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1598-L1598) | \label{lem:dim_ratio} | MAPPED | lem:dim_ratio |
| env:lem:010 | theorem_like_environment | [article.tex:1598–1607](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1598-L1607) | \begin{lem} | MAPPED | lem:dim_ratio |
| cross_reference:093 | cross_reference | [article.tex:1600–1600](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1600-L1600) | \ref{thm:main} | MAPPED | lem:dim_ratio |
| env:proof:016 | proof_environment | [article.tex:1608–1624](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1608-L1624) | \begin{proof} | MAPPED | lem:dim_ratio |
| cross_reference:094 | cross_reference | [article.tex:1626–1626](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1626-L1626) | \ref{thm:main} | MAPPED | thm:main#all-depth |
| region:all-depth-estimate | proof_region | [article.tex:1626–1668](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1626-L1668) | We are now ready to complete the proof of Theorem~\ref{thm:main}. | MAPPED | thm:main#all-depth |
| cross_reference:095 | cross_reference | [article.tex:1628–1628](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1628-L1628) | \ref{thm:main} | MAPPED | thm:main#all-depth |
| env:proof:017 | proof_environment | [article.tex:1628–1827](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1628-L1827) | \begin{proof} | MAPPED | ext:trace-analysis, thm:main#all-depth, eq:averaged_projector_deficit, eq:positive_deficit_trace, eq:forward_finite_deficit, eq:reverse_finite_deficit, thm:main#constant, thm:main |
| cross_reference:096 | cross_reference | [article.tex:1630–1630](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1630-L1630) | \ref{prop:choi} | MAPPED | thm:main#all-depth |
| cross_reference:097 | cross_reference | [article.tex:1630–1630](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1630-L1630) | \ref{prop:reverse} | MAPPED | thm:main#all-depth |
| cross_reference:098 | cross_reference | [article.tex:1635–1635](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1635-L1635) | \ref{sec:prelim} | MAPPED | thm:main#all-depth |
| cross_reference:099 | cross_reference | [article.tex:1642–1642](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1642-L1642) | \ref{lem:perturbation} | MAPPED | thm:main#all-depth |
| cross_reference:100 | cross_reference | [article.tex:1652–1652](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1652-L1652) | \ref{lem:perturbation} | MAPPED | thm:main#all-depth |
| label:079 | label | [article.tex:1665–1665](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1665-L1665) | \label{eq:weight_block_bound} | MAPPED | thm:main#all-depth |
| region:averaged-deficits | proof_region | [article.tex:1669–1683](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1669-L1683) | The cap $e_\delta\le1$ ensures that both lower bounds have | MAPPED | eq:averaged_projector_deficit |
| cross_reference:101 | cross_reference | [article.tex:1670–1670](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1670-L1670) | \eqref{eq:proj_mu_omega} | MAPPED | eq:averaged_projector_deficit |
| label:080 | label | [article.tex:1674–1674](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1674-L1674) | \label{eq:averaged_projector_deficit} | MAPPED | eq:averaged_projector_deficit |
| cross_reference:102 | cross_reference | [article.tex:1681–1681](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1681-L1681) | \ref{lem:tail} | MAPPED | eq:averaged_projector_deficit |
| cross_reference:103 | cross_reference | [article.tex:1682–1682](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1682-L1682) | \eqref{eq:uniform_mean_depth} | MAPPED | eq:averaged_projector_deficit |
| cross_reference:104 | cross_reference | [article.tex:1685–1685](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1685-L1685) | \eqref{eq:branch_trace_comparison} | MAPPED | eq:positive_deficit_trace |
| region:positive-remainder | proof_region | [article.tex:1685–1707](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1685-L1707) | Equation~\eqref{eq:branch_trace_comparison} reduces the forward error | MAPPED | eq:positive_deficit_trace |
| cross_reference:105 | cross_reference | [article.tex:1694–1694](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1694-L1694) | \eqref{eq:branch_trace_comparison} | MAPPED | eq:positive_deficit_trace |
| label:081 | label | [article.tex:1699–1699](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1699-L1699) | \label{eq:positive_deficit_trace} | MAPPED | eq:positive_deficit_trace |
| region:forward-deficit | proof_region | [article.tex:1709–1756](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1709-L1756) | \emph{Forward channel.} | MAPPED | eq:forward_finite_deficit |
| cross_reference:106 | cross_reference | [article.tex:1710–1710](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1710-L1710) | \ref{lem:ratio} | MAPPED | eq:forward_finite_deficit |
| cross_reference:107 | cross_reference | [article.tex:1712–1712](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1712-L1712) | \ref{lem:dim_ratio} | MAPPED | eq:forward_finite_deficit |
| cross_reference:108 | cross_reference | [article.tex:1714–1714](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1714-L1714) | \eqref{eq:kraus_proj} | MAPPED | eq:forward_finite_deficit |
| cross_reference:109 | cross_reference | [article.tex:1714–1714](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1714-L1714) | \eqref{eq:proj_mu_omega} | MAPPED | eq:forward_finite_deficit |
| cross_reference:110 | cross_reference | [article.tex:1727–1727](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1727-L1727) | \eqref{eq:embedded_target} | MAPPED | eq:forward_finite_deficit |
| cross_reference:111 | cross_reference | [article.tex:1735–1735](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1735-L1735) | \eqref{eq:weight_block_bound} | MAPPED | eq:forward_finite_deficit |
| cross_reference:112 | cross_reference | [article.tex:1746–1746](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1746-L1746) | \eqref{eq:forward_monotonicity} | MAPPED | eq:forward_finite_deficit |
| cross_reference:113 | cross_reference | [article.tex:1747–1747](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1747-L1747) | \eqref{eq:positive_deficit_trace} | MAPPED | eq:forward_finite_deficit |
| cross_reference:114 | cross_reference | [article.tex:1750–1750](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1750-L1750) | \eqref{eq:branch_trace_comparison} | MAPPED | eq:forward_finite_deficit |
| label:082 | label | [article.tex:1752–1752](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1752-L1752) | \label{eq:forward_finite_deficit} | MAPPED | eq:forward_finite_deficit |
| region:reverse-deficit | proof_region | [article.tex:1758–1801](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1758-L1801) | \emph{Reverse channel.} | MAPPED | eq:reverse_finite_deficit |
| cross_reference:115 | cross_reference | [article.tex:1759–1759](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1759-L1759) | \ref{prop:choi} | MAPPED | eq:reverse_finite_deficit |
| cross_reference:116 | cross_reference | [article.tex:1760–1760](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1760-L1760) | \ref{prop:reverse} | MAPPED | eq:reverse_finite_deficit |
| cross_reference:117 | cross_reference | [article.tex:1773–1773](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1773-L1773) | \eqref{eq:proj_mu_omega} | MAPPED | eq:reverse_finite_deficit |
| cross_reference:118 | cross_reference | [article.tex:1778–1778](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1778-L1778) | \eqref{eq:embedded_target} | MAPPED | eq:reverse_finite_deficit |
| cross_reference:119 | cross_reference | [article.tex:1779–1779](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1779-L1779) | \eqref{eq:weight_block_bound} | MAPPED | eq:reverse_finite_deficit |
| cross_reference:120 | cross_reference | [article.tex:1788–1788](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1788-L1788) | \ref{lem:ratio} | MAPPED | eq:reverse_finite_deficit |
| cross_reference:121 | cross_reference | [article.tex:1796–1796](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1796-L1796) | \eqref{eq:positive_deficit_trace} | MAPPED | eq:reverse_finite_deficit |
| label:083 | label | [article.tex:1798–1798](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1798-L1798) | \label{eq:reverse_finite_deficit} | MAPPED | eq:reverse_finite_deficit |
| region:collect-constant | proof_region | [article.tex:1803–1827](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1803-L1827) | \emph{Collecting the estimates.} | MAPPED | thm:main#constant |
| cross_reference:122 | cross_reference | [article.tex:1804–1804](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1804-L1804) | \eqref{eq:averaged_projector_deficit} | MAPPED | thm:main#constant |
| cross_reference:123 | cross_reference | [article.tex:1805–1805](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1805-L1805) | \eqref{eq:forward_finite_deficit} | MAPPED | thm:main#constant |
| cross_reference:124 | cross_reference | [article.tex:1805–1805](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1805-L1805) | \eqref{eq:reverse_finite_deficit} | MAPPED | thm:main#constant |
| cross_reference:125 | cross_reference | [article.tex:1806–1806](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1806-L1806) | \ref{lem:dim_ratio} | MAPPED | thm:main#constant |
| cross_reference:126 | cross_reference | [article.tex:1807–1807](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1807-L1807) | \ref{lem:ratio} | MAPPED | thm:main#constant |
| cross_reference:127 | cross_reference | [article.tex:1819–1819](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1819-L1819) | \ref{lem:ratio} | MAPPED | thm:main#constant |
| cross_reference:128 | cross_reference | [article.tex:1820–1820](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1820-L1820) | \eqref{eq:forward_finite_deficit} | MAPPED | thm:main#constant |
| cross_reference:129 | cross_reference | [article.tex:1821–1821](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1821-L1821) | \eqref{eq:reverse_finite_deficit} | MAPPED | thm:main#constant |
| cross_reference:130 | cross_reference | [article.tex:1822–1822](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1822-L1822) | \ref{lem:dim_ratio} | MAPPED | thm:main#constant |
| cross_reference:131 | cross_reference | [article.tex:1826–1826](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1826-L1826) | \ref{lem:tail} | MAPPED | thm:main#constant |
| ex:acknowledgments | excluded_region | [article.tex:1830–1851](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1830-L1851) | \section\*{Acknowledgments} | EXCLUDED | Acknowledgments, AI-use disclosure and appendix heading; non-proof material. |
| cross_reference:132 | cross_reference | [article.tex:1843–1843](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1843-L1843) | \ref{lem:perturbation} | EXCLUDED | Acknowledgments, AI-use disclosure and appendix heading; non-proof material. |
| cross_reference:133 | cross_reference | [article.tex:1844–1844](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1844-L1844) | \ref{thm:main} | EXCLUDED | Acknowledgments, AI-use disclosure and appendix heading; non-proof material. |
| label:084 | label | [article.tex:1852–1852](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1852-L1852) | \label{app:proofs} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| cross_reference:134 | cross_reference | [article.tex:1853–1853](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1853-L1853) | \ref{prop:choi} | MAPPED | prop:choi#gram |
| env:proof:018 | proof_environment | [article.tex:1853–1936](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1853-L1936) | \begin{proof} | MAPPED | ext:cartan-duality, prop:choi, prop:choi#gram, prop:choi#support, prop:choi#normalization |
| region:choi-gram | proof_region | [article.tex:1853–1897](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1853-L1897) | \begin{proof}[Proof of Proposition~\ref{prop:choi}] | MAPPED | prop:choi#gram |
| region:choi-support | proof_region | [article.tex:1899–1910](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1899-L1910) | Contracting the $\mu$ factor of the intertwiner $V$ gives the intertwiner | MAPPED | prop:choi#support |
| region:choi-normalization | proof_region | [article.tex:1911–1936](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1911-L1936) | Its trace is | MAPPED | prop:choi#normalization |
| cross_reference:135 | cross_reference | [article.tex:1939–1939](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1939-L1939) | \ref{prop:reverse} | MAPPED | prop:reverse#petz, ext:petz-formula |
| env:proof:019 | proof_environment | [article.tex:1939–2024](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1939-L2024) | \begin{proof} | MAPPED | prop:reverse, prop:reverse#petz, prop:reverse#kraus, prop:reverse#dual |
| region:petz-formula | proof_region | [article.tex:1939–1954](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1939-L1954) | \begin{proof}[Proof of Proposition~\ref{prop:reverse}] | MAPPED | prop:reverse#petz, ext:petz-formula |
| region:reverse-kraus | proof_region | [article.tex:1956–1987](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1956-L1987) | Let | MAPPED | prop:reverse#kraus |
| region:reverse-dual | proof_region | [article.tex:1989–2024](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L1989-L2024) | Now the span | MAPPED | prop:reverse#dual |
| cross_reference:136 | cross_reference | [article.tex:2027–2027](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2027-L2027) | \ref{lem:sector_gap} | MAPPED | lem:sector_gap#top |
| env:proof:020 | proof_environment | [article.tex:2027–2081](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2027-L2081) | \begin{proof} | MAPPED | lem:sector_gap, lem:sector_gap#top, lem:sector_gap#normalizer |
| region:sector-top-eigenvalue | proof_region | [article.tex:2027–2043](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2027-L2043) | \begin{proof}[Proof of Lemma~\ref{lem:sector_gap}] | MAPPED | lem:sector_gap#top |
| cross_reference:137 | cross_reference | [article.tex:2030–2030](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2030-L2030) | \ref{sec:prelim} | MAPPED | lem:sector_gap#top |
| region:sector-normalizer | proof_region | [article.tex:2045–2081](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2045-L2081) | It remains to bound $p_0$ below uniformly in $\lambda$. | MAPPED | lem:sector_gap#normalizer |
| cross_reference:138 | cross_reference | [article.tex:2047–2047](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2047-L2047) | \eqref{eq:verma_multiplicity_bound} | MAPPED | lem:sector_gap#normalizer |
| cross_reference:139 | cross_reference | [article.tex:2084–2084](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2084-L2084) | \ref{lem:block_entropy} | EXCLUDED | Proof supports excluded block-entropy/lossless-overhead application, not selected roots. |
| ex:block-entropy-proof | excluded_region | [article.tex:2084–2118](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2084-L2118) | \begin{proof}[Proof of Lemma~\ref{lem:block_entropy}] | EXCLUDED | Proof supports excluded block-entropy/lossless-overhead application, not selected roots. |
| env:proof:021 | proof_environment | [article.tex:2084–2118](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2084-L2118) | \begin{proof} | EXCLUDED | Proof supports excluded block-entropy/lossless-overhead application, not selected roots. |
| cross_reference:140 | cross_reference | [article.tex:2086–2086](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2086-L2086) | \ref{sec:prelim} | EXCLUDED | Proof supports excluded block-entropy/lossless-overhead application, not selected roots. |
| cross_reference:141 | cross_reference | [article.tex:2097–2097](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2097-L2097) | \eqref{eq:verma_multiplicity_bound} | EXCLUDED | Proof supports excluded block-entropy/lossless-overhead application, not selected roots. |
| cross_reference:142 | cross_reference | [article.tex:2112–2112](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2112-L2112) | \ref{lem:shallow_multiplicities} | EXCLUDED | Proof supports excluded block-entropy/lossless-overhead application, not selected roots. |
| cross_reference:143 | cross_reference | [article.tex:2116–2116](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2116-L2116) | \eqref{eq:block_entropy_limit} | EXCLUDED | Proof supports excluded block-entropy/lossless-overhead application, not selected roots. |
| cross_reference:144 | cross_reference | [article.tex:2121–2121](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2121-L2121) | \ref{lem:shallow_multiplicities} | MAPPED | ext:kostant |
| env:proof:022 | proof_environment | [article.tex:2121–2167](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2121-L2167) | \begin{proof} | MAPPED | lem:shallow_multiplicities, lem:shallow_multiplicities#vanishing |
| region:kostant-formula | proof_region | [article.tex:2121–2132](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2121-L2132) | \begin{proof}[Proof of Lemma~\ref{lem:shallow_multiplicities}] | MAPPED | ext:kostant |
| citation:032 | citation | [article.tex:2125–2125](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2125-L2125) | \cite{kostant1959multiplicity} | MAPPED | ext:kostant |
| region:shallow-vanishing | proof_region | [article.tex:2133–2158](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2133-L2158) | Write $\delta=\sum_{i=1}^{d-1}c_i\alpha_i$. By hypothesis, | MAPPED | lem:shallow_multiplicities#vanishing |
| region:supported-root-partitions | proof_region | [article.tex:2160–2167](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2160-L2167) | Finally, each positive root has the expansion | MAPPED | lem:shallow_multiplicities |
| ex:unknown-spectrum | excluded_region | [article.tex:2170–2268](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2170-L2268) | \section{Additional cost of an unknown spectrum}\label{app:unknown_spectrum} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| label:085 | label | [article.tex:2170–2170](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2170-L2170) | \label{app:unknown_spectrum} | EXCLUDED | Section/appendix/figure label is navigational or repeats an argument; underlying mathematical regions are separately inventoried. |
| cross_reference:145 | cross_reference | [article.tex:2172–2172](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2172-L2172) | \ref{sec:redundancy} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| cross_reference:146 | cross_reference | [article.tex:2173–2173](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2173-L2173) | \eqref{eq:invariant_split} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| citation:033 | citation | [article.tex:2181–2181](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2181-L2181) | \cite[Eq.~(10)]{hayashi2010universal} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| citation:034 | citation | [article.tex:2182–2182](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2182-L2182) | \cite{matsumoto2007universal} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| cross_reference:147 | cross_reference | [article.tex:2196–2196](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2196-L2196) | \eqref{eq:block_entropy_limit} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| label:086 | label | [article.tex:2198–2198](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2198-L2198) | \label{eq:orbit_redundancy_fullrank} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| citation:035 | citation | [article.tex:2205–2205](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2205-L2205) | \cite{hayashi2010universal} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| label:087 | label | [article.tex:2206–2206](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2206-L2206) | \label{eq:hayashi_C} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| label:088 | label | [article.tex:2211–2211](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2211-L2211) | \label{eq:hayashi_pointwise} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| cross_reference:148 | cross_reference | [article.tex:2216–2216](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2216-L2216) | \eqref{eq:orbit_redundancy_fullrank} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| cross_reference:149 | cross_reference | [article.tex:2217–2217](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2217-L2217) | \eqref{eq:invariant_split} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| label:089 | label | [article.tex:2218–2218](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2218-L2218) | \label{eq:spectral_redundancy_uniform} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| citation:036 | citation | [article.tex:2225–2225](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2225-L2225) | \cite{clarke1990information} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| citation:037 | citation | [article.tex:2231–2231](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2231-L2231) | \cite{hayashi2010universal} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| label:090 | label | [article.tex:2232–2232](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2232-L2232) | \label{eq:hayashi_minimax} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| citation:038 | citation | [article.tex:2251–2251](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2251-L2251) | \cite{clarke1990information,clarke1994jeffreys} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| cross_reference:150 | cross_reference | [article.tex:2253–2253](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2253-L2253) | \eqref{eq:invariant_split} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |
| cross_reference:151 | cross_reference | [article.tex:2261–2261](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/490356f620c1ab963ff99585d6835c93e4324b37/article.tex#L2261-L2261) | \eqref{eq:orbit_redundancy} | EXCLUDED | Unknown-spectrum universal coding appendix and bibliography declarations; different compression criterion and no dependency of requested known-spectrum roots. |

## Mechanical extraction policy

Regex runs on raw TeX without stripping comments. Any recognizable audited command in comments would be counted and would require explicit disposition. No such commented occurrence was found in this snapshot.

Environment begins/ends are paired by same-environment stacks, including the lemma nested inside the achievability proof. Each proof is inventoried once as an environment; multiple substantive node mappings do not duplicate source occurrences. Every label, citation command and reference command is inventoried individually. Multi-key citation commands retain all keys.

Exact regex patterns are saved in the JSON. Source files and all recorded line bounds were checked locally; node IDs are unique, edges resolve, the graph is acyclic, every mapped inventory entry has node IDs, and every excluded entry has a reason. These structural checks do not verify the mathematics.

## Metadata navigation boundary

Only after reading/reconstructing the Article, candidate declaration/file/line links were copied from metadata/natural-language-map.json. No Lean implementation was read. All copied links are UNVERIFIED_LINK_ONLY; the source argument remains independent of metadata proof-status claims. The JSON retains these suggestions for the separate implementation audit.


## Audit records

See [[audit|the audit overview and reproducer]] and the [machine-readable review](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/statement-audit/source-coverage.json). The [fresh Lean check record](https://github.com/JWang226/Quantum-Minimum-Description-Length/blob/main/metadata/statement-audit/checks.json) records the final compilation status; any pending wording in the original review describes its state before integration.
