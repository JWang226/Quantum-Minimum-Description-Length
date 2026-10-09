/-
Copyright (c) 2026 Free Entropy formalization contributors.
See LICENSE and NOTICE in the repository root for license and attribution.
-/

import FreeEntropy.CanonicalChoi

/-! The forward PRV support projector is independent of the choice of its
isometric intertwiner. The hypotheses specify the representation equations
directly, rather than requiring the particular constructed Choi embedding. -/
noncomputable section
open Matrix
namespace FreeEntropy.CartanChoi
open LieMatrixCasimir CartanLieCloning
set_option backward.isDefEq.respectTransparency false
variable {d : ℕ} {A B C : Type*} [Fintype A] [DecidableEq A]
  [Fintype B] [DecidableEq B] [Fintype C] [DecidableEq C]
  [Nonempty A] [Nonempty B] [Nonempty C]

/-- Every forward auxiliary copy is a scalar multiple of the normalized Choi
isometry. This follows from the proved Cartan multiplicity, not a multiplicity
assumption supplied by the caller. -/
theorem forward_embedding_scalar
    (M : CyclicWeightModel d A) (N : CyclicWeightModel d B)
    (S : CyclicWeightModel d C) (hrow : S.row = M.row + N.row)
    (V : Matrix (A × B) C ℂ) (hViso : Vᴴ * V = 1)
    (hV : ∀ i j, (M.generators.tensor N.generators).E i j * V = V * S.generators.E i j)
    (W : Matrix (A × C) B ℂ)
    (hW : ∀ i j, (M.generators.dual.tensor S.generators).E i j * W =
      W * N.generators.E i j) :
    ∃ c : ℂ, W = c • embedding V := by
  obtain ⟨c, hc⟩ := dual_embedding_scalar M N S hrow V hViso hV W hW
  have hr : (Real.sqrt ((Fintype.card B : ℝ) / Fintype.card C) : ℂ) ≠ 0 := by
    exact_mod_cast (Real.sqrt_pos.mpr (div_pos
      (by exact_mod_cast Fintype.card_pos (α := B))
      (by exact_mod_cast Fintype.card_pos (α := C)))).ne'
  have he : embedding V =
      (Real.sqrt ((Fintype.card B : ℝ) / Fintype.card C) : ℂ) • (reshuffle V)ᴴ := by
    ext a b
    simp only [embedding, Matrix.smul_apply, Complex.real_smul, smul_eq_mul]
  refine ⟨c / (Real.sqrt ((Fintype.card B : ℝ) / Fintype.card C) : ℂ), ?_⟩
  rw [he, smul_smul, div_mul_cancel₀ _ hr]
  exact hc

/-- Isometry fixes the scalar's norm, hence all forward auxiliary copies have
the same orthogonal support projector. -/
theorem forwardProjector_unique
    (M : CyclicWeightModel d A) (N : CyclicWeightModel d B)
    (S : CyclicWeightModel d C) (hrow : S.row = M.row + N.row)
    (V : Matrix (A × B) C ℂ) (hViso : Vᴴ * V = 1)
    (hV : ∀ i j, (M.generators.tensor N.generators).E i j * V = V * S.generators.E i j)
    (W : Matrix (A × C) B ℂ) (hWiso : Wᴴ * W = 1)
    (hW : ∀ i j, (M.generators.dual.tensor S.generators).E i j * W =
      W * N.generators.E i j) : W * Wᴴ = projector V := by
  obtain ⟨c, hc⟩ := forward_embedding_scalar M N S hrow V hViso hV W hW
  have hJ := embedding_isometry M N S V hViso hV
  have hp : c * star c = 1 := by
    rw [hc, Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, smul_smul,
      hJ] at hWiso
    have he := congrArg (fun X : Matrix B B ℂ => X N.highestBasis N.highestBasis) hWiso
    simpa only [Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul, mul_one, one_mul,
      mul_comm] using he
  rw [hc, Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, smul_smul,
    hp, one_smul, embedding_projector]

end FreeEntropy.CartanChoi

namespace FreeEntropy.ExteriorRepresentation
open CartanLieCloning CartanChoi
set_option backward.isDefEq.respectTransparency false
variable {d : ℕ}
local instance (mu : Fin d → ℕ) : Nonempty (IrrepIndex mu) :=
  Fin.pos_iff_nonempty.mp (irrep_dimension_pos mu)

/-- Every intertwiner from the actual auxiliary model into input-dual × output
is the constructed forward Choi isometry up to a scalar. -/
theorem canonicalChoi_embedding_unique (mu nu : Fin d → ℕ)
    (hmu : Antitone mu) (hnu : Antitone nu)
    (hinc : Antitone (fun i => (nu i : ℝ) - (mu i : ℝ)))
    (W : Matrix (IrrepIndex mu × IrrepIndex nu) (IrrepIndex (auxiliaryRow mu nu)) ℂ)
    (hW : ∀ i j,
      ((canonicalWeightModel mu).generators.dual.tensor (canonicalWeightModel nu).generators).E i j * W =
        W * (canonicalAuxiliaryModel mu nu).generators.E i j) :
    ∃ c : ℂ, W = c • canonicalChoiEmbedding mu nu hmu hnu hinc :=
  forward_embedding_scalar _ _ _ (canonicalAuxiliaryModel_hrow mu nu hmu hnu hinc)
    (specifiedCartanEmbedding _ _ _ (canonicalAuxiliaryModel_hrow mu nu hmu hnu hinc))
    (specifiedCartanEmbedding_isometry _ _ _ (canonicalAuxiliaryModel_hrow mu nu hmu hnu hinc))
    (specifiedCartanEmbedding_intertwines _ _ _ (canonicalAuxiliaryModel_hrow mu nu hmu hnu hinc)) W hW

/-- The forward PRV projector is uniquely characterized by an isometric copy of
its auxiliary representation satisfying the literal generator equations. -/
theorem canonicalChoiProjector_unique (mu nu : Fin d → ℕ)
    (hmu : Antitone mu) (hnu : Antitone nu)
    (hinc : Antitone (fun i => (nu i : ℝ) - (mu i : ℝ)))
    (W : Matrix (IrrepIndex mu × IrrepIndex nu) (IrrepIndex (auxiliaryRow mu nu)) ℂ)
    (hWiso : Wᴴ * W = 1)
    (hW : ∀ i j,
      ((canonicalWeightModel mu).generators.dual.tensor (canonicalWeightModel nu).generators).E i j * W =
        W * (canonicalAuxiliaryModel mu nu).generators.E i j) :
    W * Wᴴ = canonicalChoiProjector mu nu hmu hnu hinc :=
  forwardProjector_unique _ _ _ (canonicalAuxiliaryModel_hrow mu nu hmu hnu hinc)
    (specifiedCartanEmbedding _ _ _ (canonicalAuxiliaryModel_hrow mu nu hmu hnu hinc))
    (specifiedCartanEmbedding_isometry _ _ _ (canonicalAuxiliaryModel_hrow mu nu hmu hnu hinc))
    (specifiedCartanEmbedding_intertwines _ _ _ (canonicalAuxiliaryModel_hrow mu nu hmu hnu hinc))
    W hWiso hW

end FreeEntropy.ExteriorRepresentation
