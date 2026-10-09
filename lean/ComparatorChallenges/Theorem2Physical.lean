/-
Copyright (c) 2026 Free Entropy formalization contributors.
See LICENSE and NOTICE in the repository root for license and attribution.
-/

import FreeEntropy.CanonicalOrbit
import FreeEntropy.SignedAuxiliaryModel
import FreeEntropy.CanonicalRowBounds
import FreeEntropy.Theorem2
import FreeEntropy.ChoiContraction

/-! Independently stated physical Theorem 2 specification. Raw tensor-source
normalization and Choi contractions are redeclared. Tensor embeddings and PRV
copies are arbitrary isometries satisfying explicit representation equations.
The existence root prevents a vacuous interface. Canonical representation
coordinates and numerical bounds remain shared; no final theorem, physical-state
bridge or canonical Choi-projector construction is imported. The two challenge holes are
intentional and are excluded from production proof auditing. -/
noncomputable section
open Matrix
open scoped BigOperators Kronecker

namespace FreeEntropy.SchurWeyl
variable {d r : ℕ}
variable {A : Type*} [Fintype A] [DecidableEq A]

def physicalIsometricState (n : ℕ) (J : Matrix (Fin n → Fin d) A ℂ)
    (ρ : Matrix (Fin d) (Fin d) ℂ) : Matrix A A ℂ :=
  let B := Jᴴ * Matrix.of (fun x y : Fin n → Fin d => ∏ t : Fin n, ρ (x t) (y t)) * J
  if B.trace.re = 0 then (Fintype.card A : ℝ)⁻¹ • (1 : Matrix A A ℂ)
  else B.trace.re⁻¹ • B

/-- The source density, independently expanded from the spectrum and eigenbasis. -/
def physicalSpectrumDensity (s : FixedSpectrum d r) (U : Matrix.unitaryGroup (Fin d) ℂ) :
    Matrix (Fin d) (Fin d) ℂ :=
  U.val * Matrix.diagonal (fun j => (s.eigenvalue j.val : ℂ)) * U.valᴴ

end FreeEntropy.SchurWeyl

namespace FreeEntropy.ExteriorRepresentation
open CartanChoi CartanLieCloning TraceDistance SchurWeyl
set_option backward.isDefEq.respectTransparency false
variable {d r : ℕ}

/-- Literal normalized Choi contraction from any isometric PRV copy. -/
def physicalPrvMap {A B C : Type*} [Fintype A] [DecidableEq A]
    [Fintype B] [DecidableEq B] [Fintype C] [DecidableEq C]
    (W : Matrix (A × B) C ℂ) (X : Matrix A A ℂ) : Matrix B B ℂ :=
  partialTraceInput
    ((((Fintype.card A : ℝ) / Fintype.card C) • (W * Wᴴ)) * (X.transpose ⊗ₖ 1))

/-- Every choice of physical tensor embeddings and PRV isometries satisfying
the representation equations has both manuscript error bounds. -/
theorem theorem2_cloning_accuracy_physical
    (s : FixedSpectrum d r) (hd : 2 ≤ d)
    (mu nu : Fin d → ℕ) (hmu : Antitone mu) (hnu : Antitone nu)
    (hmu_support : ∀ i : Fin d, r ≤ i.val → mu i = 0)
    (hnu_support : ∀ i : Fin d, r ≤ i.val → nu i = 0)
    (hinc : Antitone (fun i => (nu i : ℝ) - (mu i : ℝ)))
    (Jmu : Matrix (Fin (∑ j, mu j) → Fin d) (IrrepIndex mu) ℂ)
    (Jnu : Matrix (Fin (∑ j, nu j) → Fin d) (IrrepIndex nu) ℂ)
    (hJmu : Jmuᴴ * Jmu = 1) (hJnu : Jnuᴴ * Jnu = 1)
    (hJmuR : ∀ V : Matrix.unitaryGroup (Fin d) ℂ,
      Matrix.of (fun x y : Fin (∑ j, mu j) → Fin d => ∏ t : Fin (∑ j, mu j), V.val (x t) (y t)) * Jmu =
        Jmu * canonicalWeightRepresentation mu V)
    (hJnuR : ∀ V : Matrix.unitaryGroup (Fin d) ℂ,
      Matrix.of (fun x y : Fin (∑ j, nu j) → Fin d => ∏ t : Fin (∑ j, nu j), V.val (x t) (y t)) * Jnu =
        Jnu * canonicalWeightRepresentation nu V)
    (Wf : Matrix (IrrepIndex mu × IrrepIndex nu) (IrrepIndex (auxiliaryRow mu nu)) ℂ)
    (Wr : Matrix (IrrepIndex nu × IrrepIndex mu) (IrrepIndex (auxiliaryRow mu nu)) ℂ)
    (hWf : Wfᴴ * Wf = 1) (hWr : Wrᴴ * Wr = 1)
    (hWfR : ∀ i j,
      ((canonicalWeightModel mu).generators.dual.tensor (canonicalWeightModel nu).generators).E i j * Wf =
        Wf * (canonicalAuxiliaryModel mu nu).generators.E i j)
    (hWrR : ∀ i j,
      ((canonicalWeightModel nu).generators.dual.tensor (canonicalWeightModel mu).generators).E i j * Wr =
        Wr * (canonicalAuxiliaryModel mu nu).generators.dual.E i j)
    (U : Matrix.unitaryGroup (Fin d) ℂ) :
    traceDistance
      (physicalPrvMap Wf (physicalIsometricState (∑ j, mu j) Jmu (physicalSpectrumDensity s U)))
      (physicalIsometricState (∑ j, nu j) Jnu (physicalSpectrumDensity s U)) ≤
        Theorem2.cloningConstant d r s.qx * (differenceNorm mu nu : ℝ) /
          ((minimumRowGap mu r hd s.rank_pos : ℝ) + 1) ∧
    traceDistance
      (physicalPrvMap Wr (physicalIsometricState (∑ j, nu j) Jnu (physicalSpectrumDensity s U)))
      (physicalIsometricState (∑ j, mu j) Jmu (physicalSpectrumDensity s U)) ≤
        Theorem2.cloningConstant d r s.qx * (differenceNorm mu nu : ℝ) /
          ((minimumRowGap mu r hd s.rank_pos : ℝ) + 1) := by
  sorry

/-- The independently specified physical and PRV realizations exist for every
admissible pair; none of the universal theorem's interface premises is vacuous. -/
theorem theorem2_physical_realizations_exist
    (mu nu : Fin d → ℕ) (hmu : Antitone mu) (hnu : Antitone nu)
    (hinc : Antitone (fun i => (nu i : ℝ) - (mu i : ℝ))) :
    ∃ Jmu : Matrix (Fin (∑ j, mu j) → Fin d) (IrrepIndex mu) ℂ,
      ∃ Jnu : Matrix (Fin (∑ j, nu j) → Fin d) (IrrepIndex nu) ℂ,
        ∃ Wf : Matrix (IrrepIndex mu × IrrepIndex nu) (IrrepIndex (auxiliaryRow mu nu)) ℂ,
          ∃ Wr : Matrix (IrrepIndex nu × IrrepIndex mu) (IrrepIndex (auxiliaryRow mu nu)) ℂ,
            Jmuᴴ * Jmu = 1 ∧ Jnuᴴ * Jnu = 1 ∧
            (∀ V : Matrix.unitaryGroup (Fin d) ℂ,
              Matrix.of (fun x y : Fin (∑ j, mu j) → Fin d => ∏ t : Fin (∑ j, mu j), V.val (x t) (y t)) * Jmu =
                Jmu * canonicalWeightRepresentation mu V) ∧
            (∀ V : Matrix.unitaryGroup (Fin d) ℂ,
              Matrix.of (fun x y : Fin (∑ j, nu j) → Fin d => ∏ t : Fin (∑ j, nu j), V.val (x t) (y t)) * Jnu =
                Jnu * canonicalWeightRepresentation nu V) ∧
            Wfᴴ * Wf = 1 ∧ Wrᴴ * Wr = 1 ∧
            (∀ i j,
              ((canonicalWeightModel mu).generators.dual.tensor (canonicalWeightModel nu).generators).E i j * Wf =
                Wf * (canonicalAuxiliaryModel mu nu).generators.E i j) ∧
            (∀ i j,
              ((canonicalWeightModel nu).generators.dual.tensor (canonicalWeightModel mu).generators).E i j * Wr =
                Wr * (canonicalAuxiliaryModel mu nu).generators.dual.E i j) := by
  sorry

end FreeEntropy.ExteriorRepresentation
