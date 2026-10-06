/-
Copyright (c) 2026 Free Entropy formalization contributors.
See LICENSE and NOTICE in the repository root for license and attribution.
-/
import Lean

/-! Read the actual endpoint telescopes, including implicit and instance binders.
This exports review evidence; it does not decide manuscript correspondence. -/
open Lean Meta

private def binderKind : BinderInfo → String
  | .default => "explicit"
  | .implicit => "implicit"
  | .strictImplicit => "strict_implicit"
  | .instImplicit => "instance"

private def inspect (name : Name) : MetaM Json := do
  let ci ← getConstInfo name
  forallTelescope ci.type fun xs result => do
    let mut binders : Array Json := #[]
    for x in xs do
      let decl ← x.fvarId!.getDecl
      binders := binders.push <| Json.mkObj [
        ("name", toJson decl.userName.toString),
        ("kind", toJson (binderKind decl.binderInfo)),
        ("type", toJson (← ppExpr decl.type).pretty),
        ("is_proposition", toJson (← isProp decl.type))]
    return Json.mkObj [
      ("name", toJson name.toString),
      ("binders", toJson binders),
      ("conclusion", toJson (← ppExpr result).pretty)]

unsafe def main (args : List String) : IO Unit := do
  let [outPath] := args | throw <| IO.userError "Expected output JSON path"
  initSearchPath (← findSysroot)
  enableInitializersExecution
  let env ← importModules #[{ module := `FreeEntropy.Theorem1Complete },
    { module := `FreeEntropy.Theorem2Choi }] {} (leakEnv := true) (loadExts := true)
  let names := #[`FreeEntropy.theorem1_achievability, `FreeEntropy.theorem1_converse,
    `FreeEntropy.theorem1_converse_of_uniform,
    `FreeEntropy.ExteriorRepresentation.theorem2_cloning_accuracy_choi]
  let mut results : Array Json := #[]
  let options := ({} : Options).set `pp.width (120 : Nat)
    |>.set `pp.funBinderTypes true |>.set `pp.piBinderTypes true
  for name in names do
    let (result, _, _) ← (inspect name).toIO
      { fileName := "<statement-audit>", fileMap := default, options := options }
      { env := env }
    results := results.push result
  IO.FS.writeFile outPath (toJson results).pretty
  IO.println s!"Exported binder evidence for {results.size} endpoints."
