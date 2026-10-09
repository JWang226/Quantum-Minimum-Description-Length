/-
Copyright (c) 2026 Free Entropy formalization contributors.
See LICENSE and NOTICE in the repository root for license and attribution.
-/

import FreeEntropy.PhysicalOrbitChannels
import FreeEntropy.CartanGroupCovariance

/-!
# Physical states specified by arbitrary tensor-power embeddings

The source state below is restated directly from matrix entries and trace
normalization. Its agreement with the canonical orbit follows for every
isometric tensor-power intertwiner, not just the constructed embedding.
The representation and its coordinate index remain the canonical ones.
-/
noncomputable section
open Matrix
open scoped BigOperators MatrixOrder ComplexOrder

namespace FreeEntropy.SchurWeyl
open ExteriorRepresentation
set_option backward.isDefEq.respectTransparency false
variable {d r n : ℕ} {A : Type*} [Fintype A] [DecidableEq A]

/-- Literal normalized restriction of the physical tensor source to an
isometric summand. The zero-trace fallback is explicitly maximally mixed. -/
def physicalIsometricState (n : ℕ) (J : Matrix (Fin n → Fin d) A ℂ)
    (ρ : Matrix (Fin d) (Fin d) ℂ) : Matrix A A ℂ :=
  let B := Jᴴ * Matrix.of (fun x y : Fin n → Fin d => ∏ t : Fin n, ρ (x t) (y t)) * J
  if B.trace.re = 0 then (Fintype.card A : ℝ)⁻¹ • (1 : Matrix A A ℂ)
  else B.trace.re⁻¹ • B

theorem physicalIsometricState_eq_normalizedBlock [Nonempty A]
    (J : Matrix (Fin n → Fin d) A ℂ) (ρ : Matrix (Fin d) (Fin d) ℂ) :
    physicalIsometricState n J ρ = normalizedBlock (Jᴴ * TensorPowers.matrix n ρ * J) := rfl

/-- Any physical isometric copy of the same representation has the same
state; no source-block or state-identification equality is a hypothesis. -/
theorem physicalIsometricState_eq_weightTensorState (mu : Fin d → ℕ)
    (J : Matrix (Fin (tensorDegree mu) → Fin d) (IrrepIndex mu) ℂ)
    (hJ : Jᴴ * J = 1)
    (hJR : ∀ U : Matrix.unitaryGroup (Fin d) ℂ,
      TensorPowers.matrix (tensorDegree mu) U.val * J = J * canonicalWeightRepresentation mu U)
    {ρ : Matrix (Fin d) (Fin d) ℂ} (hρ : ρ.IsHermitian) :
    physicalIsometricState (tensorDegree mu) J ρ = canonicalWeightTensorState mu ρ := by
  letI : Nonempty (IrrepIndex mu) := Fin.pos_iff_nonempty.mp (irrep_dimension_pos mu)
  rw [physicalIsometricState_eq_normalizedBlock]
  have hs := source_blocks_equal (canonicalWeightRepresentation mu) J
    (canonicalPhysicalWeightEmbedding mu) hJ (canonicalPhysicalWeightEmbedding_isometry mu)
    hJR (canonicalPhysicalWeightEmbedding_intertwines mu) hρ
  rw [hs]
  unfold canonicalWeightTensorState canonicalTensorState
  have hQ := (canonicalWeightCoordinates mu).isometry
  have hQ' := mul_eq_one_comm.mp hQ
  have hn := normalizedBlock_unitary (canonicalWeightCoordinates mu).unitaryᴴ
    (by simpa using hQ') (by simpa using hQ) (canonicalTensorSource mu ρ)
  simp only [Matrix.conjTranspose_conjTranspose] at hn
  rw [← hn]
  congr 1
  simp only [canonicalPhysicalWeightEmbedding, canonicalTensorSource,
    Matrix.conjTranspose_mul, Matrix.mul_assoc]

/-- An independently normalized physical source equals the canonical orbit
for every genuine isometric embedding of the specified representation.
The tensor degree is the literal sum of the partition rows. -/
theorem physicalIsometricState_eq_orbit (s : FixedSpectrum d r) (mu : Fin d → ℕ)
    (hmu : Antitone mu) (hsupp : ∀ j, r ≤ j.val → mu j = 0)
    (J : Matrix (Fin (∑ j, mu j) → Fin d) (IrrepIndex mu) ℂ)
    (hJ : Jᴴ * J = 1)
    (hJR : ∀ V : Matrix.unitaryGroup (Fin d) ℂ,
      Matrix.of (fun x y : Fin (∑ j, mu j) → Fin d =>
        ∏ t : Fin (∑ j, mu j), V.val (x t) (y t)) * J =
        J * canonicalWeightRepresentation mu V)
    (U : Matrix.unitaryGroup (Fin d) ℂ) :
    physicalIsometricState (∑ j, mu j) J (physicalDensity s U) = canonicalOrbitState s mu U := by
  have h (m : ℕ) (hm : m = tensorDegree mu) :
      ∀ K : Matrix (Fin m → Fin d) (IrrepIndex mu) ℂ,
      Kᴴ * K = 1 →
      (∀ V : Matrix.unitaryGroup (Fin d) ℂ,
        Matrix.of (fun x y : Fin m → Fin d =>
          ∏ t : Fin m, V.val (x t) (y t)) * K =
          K * canonicalWeightRepresentation mu V) →
      physicalIsometricState m K (physicalDensity s U) =
        canonicalOrbitState s mu U := by
    subst m
    intro K hK hKR
    rw [physicalIsometricState_eq_weightTensorState mu K hK hKR
      (physicalDensity_positive s U).isHermitian]
    exact canonicalWeightTensorState_eq_orbit s mu hmu hsupp U
  exact h _ (tensorDegree_eq_sum mu hmu).symm J hJ hJR

/-- The physical tensor embedding exists at exactly the sum of the rows,
and satisfies the independently stated isometry and group-action conditions. -/
theorem exists_physicalWeightEmbeddingSum (mu : Fin d → ℕ) (hmu : Antitone mu) :
    ∃ J : Matrix (Fin (∑ j, mu j) → Fin d) (IrrepIndex mu) ℂ,
      Jᴴ * J = 1 ∧ ∀ U : Matrix.unitaryGroup (Fin d) ℂ,
        Matrix.of (fun x y : Fin (∑ j, mu j) → Fin d =>
          ∏ t : Fin (∑ j, mu j), U.val (x t) (y t)) * J =
          J * canonicalWeightRepresentation mu U := by
  have h (m : ℕ) (hm : m = tensorDegree mu) :
      ∃ J : Matrix (Fin m → Fin d) (IrrepIndex mu) ℂ,
      Jᴴ * J = 1 ∧ ∀ U : Matrix.unitaryGroup (Fin d) ℂ,
        Matrix.of (fun x y : Fin m → Fin d =>
          ∏ t : Fin m, U.val (x t) (y t)) * J =
          J * canonicalWeightRepresentation mu U := by
    subst m
    exact ⟨canonicalPhysicalWeightEmbedding mu, canonicalPhysicalWeightEmbedding_isometry mu,
      canonicalPhysicalWeightEmbedding_intertwines mu⟩
  exact h _ (tensorDegree_eq_sum mu hmu).symm

end FreeEntropy.SchurWeyl
