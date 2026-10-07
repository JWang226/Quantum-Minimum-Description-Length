/-
Copyright (c) 2026 Free Entropy formalization contributors.
See LICENSE and NOTICE in the repository root for license and attribution.
-/
module
import Lean

/-! Kernel witnesses for explicitly reviewed, closed foundation-instance pairs.

This tool reconstructs the exact serialized constant/application expressions. It
does not elaborate the input terms, normalize them, or import project proofs.
For each pair it constructs `Eq.refl` on the left and submits the proposed
left/right equality as a theorem to `Environment.addDeclCore` with kernel checking
explicitly enabled. Success therefore requires kernel definitional equality.
The paired terms may contain only closed universe levels and constants from the
imported Mathlib/Lean foundation environment. No project expressions are accepted.
-/

open Lean

private def array (json : Json) : IO (Array Json) := IO.ofExcept json.getArr?

private def string (json : Json) : IO String := IO.ofExcept json.getStr?

private def nat (json : Json) : IO Nat := IO.ofExcept json.getNat?

private partial def decodeName (json : Json) : IO Name := do
  let fields ← array json
  match ← string fields[0]! with
  | "anonymous" =>
    unless fields.size == 1 do throw <| IO.userError "Malformed anonymous name"
    return .anonymous
  | "str" =>
    unless fields.size == 3 do throw <| IO.userError "Malformed string name"
    return .str (← decodeName fields[1]!) (← string fields[2]!)
  | "num" =>
    unless fields.size == 3 do throw <| IO.userError "Malformed numeric name"
    return .num (← decodeName fields[1]!) (← nat fields[2]!)
  | tag => throw <| IO.userError s!"Unknown name tag: {tag}"

private partial def decodeLevel (json : Json) : IO Level := do
  let fields ← array json
  match ← string fields[0]! with
  | "zero" =>
    unless fields.size == 1 do throw <| IO.userError "Malformed zero level"
    return .zero
  | "succ" =>
    unless fields.size == 2 do throw <| IO.userError "Malformed successor level"
    return .succ (← decodeLevel fields[1]!)
  | "max" =>
    unless fields.size == 3 do throw <| IO.userError "Malformed maximum level"
    return .max (← decodeLevel fields[1]!) (← decodeLevel fields[2]!)
  | "imax" =>
    unless fields.size == 3 do throw <| IO.userError "Malformed impredicative maximum level"
    return .imax (← decodeLevel fields[1]!) (← decodeLevel fields[2]!)
  | tag => throw <| IO.userError s!"Closed universe level required; received {tag}"

private partial def decodeExpr (env : Environment) (json : Json) : IO Expr := do
  let fields ← array json
  match ← string fields[0]! with
  | "const" =>
    unless fields.size == 3 do throw <| IO.userError "Malformed constant expression"
    let name ← decodeName fields[1]!
    let some origin := env.getModuleIdxFor? name
      | throw <| IO.userError s!"Unknown foundation constant: {name}"
    if (`FreeEntropy).isPrefixOf env.allImportedModuleNames[origin.toNat]! then
      throw <| IO.userError s!"Project constant is disallowed: {name}"
    let levels ← (← array fields[2]!).mapM decodeLevel
    return .const name levels.toList
  | "app" =>
    unless fields.size == 3 do throw <| IO.userError "Malformed application expression"
    return .app (← decodeExpr env fields[1]!) (← decodeExpr env fields[2]!)
  | tag => throw <| IO.userError s!"Only closed constant/application expressions accepted: {tag}"

private def nameTree : Name → Json
  | .anonymous => Json.arr #[toJson "anonymous"]
  | .str parentName value => Json.arr #[toJson "str", nameTree parentName, toJson value]
  | .num parentName value => Json.arr #[toJson "num", nameTree parentName, toJson value]

private def levelTree : Level → Json
  | .zero => Json.arr #[toJson "zero"]
  | .succ u => Json.arr #[toJson "succ", levelTree u]
  | .max u v => Json.arr #[toJson "max", levelTree u, levelTree v]
  | .imax u v => Json.arr #[toJson "imax", levelTree u, levelTree v]
  | .param name => Json.arr #[toJson "param", nameTree name]
  | .mvar id => Json.arr #[toJson "level_mvar", nameTree id.name]

private partial def groundTree : Expr → IO Json
  | .const name levels =>
    pure <| Json.arr #[toJson "const", nameTree name, toJson (levels.map levelTree)]
  | .app fn arg => do
    pure <| Json.arr #[toJson "app", ← groundTree fn, ← groundTree arg]
  | expr => throw <| IO.userError s!"Unexpected non-ground certificate expression: {reprStr expr}"

public unsafe def main (args : List String) : IO Unit := do
  let [inputPath, outputPath] := args
    | throw <| IO.userError "Expected exact instance-pair input and witness-output paths"
  let input ← IO.ofExcept <| Json.parse (← IO.FS.readFile inputPath)
  unless (← IO.ofExcept <| input.getObjValAs? String "schema_version") ==
      "qmdl-cleanup-instance-pairs-v1" do
    throw <| IO.userError "Unsupported instance-pair input schema"
  initSearchPath (← findSysroot)
  enableInitializersExecution
  let modules : Array Import := #[
    { module := `Mathlib.Data.Int.ConditionallyCompleteOrder },
    { module := `Mathlib.Analysis.RCLike.Basic }]
  let mut env ← importModules modules {} (leakEnv := true) (loadExts := true)
  for name in env.allImportedModuleNames do
    if (`FreeEntropy).isPrefixOf name then
      throw <| IO.userError "Foundation environment unexpectedly imports FreeEntropy"
  let pairs ← IO.ofExcept <| input.getObjValAs? (Array Json) "pairs"
  unless pairs.size > 0 do throw <| IO.userError "No instance pairs supplied"
  let mut records : Array Json := #[]
  for pair in pairs do
    let id ← IO.ofExcept <| pair.getObjValAs? String "id"
    let before ← decodeExpr env (← IO.ofExcept <| pair.getObjVal? "before_expr")
    let after ← decodeExpr env (← IO.ofExcept <| pair.getObjVal? "after_expr")
    let expectedType ← decodeExpr env (← IO.ofExcept <| pair.getObjVal? "type_expr")
    let action : MetaM (Expr × Expr × Expr) := do
      return (← Meta.inferType expectedType, ← Meta.inferType before, ← Meta.inferType after)
    let ((sort, beforeType, afterType), _, _) ← action.toIO
      { fileName := "<cleanup-instance-pair>", fileMap := default } { env := env }
    let .sort universeLevel := sort
      | throw <| IO.userError s!"Expected instance type is not a sort: {id}"
    -- Do not use the Meta.isDefEq decision as evidence. The kernel must accept
    -- the literal reflexivity proof at this explicitly specified equality type.
    let type := mkApp3 (.const `Eq [universeLevel]) expectedType before after
    let value := mkApp2 (.const `Eq.refl [universeLevel]) expectedType before
    let theoremName := (`QMDLCleanupFoundationWitness).str id
    let decl := Declaration.thmDecl {
      name := theoremName, levelParams := [], type := type, value := value }
    match env.addDeclCore 0 decl none (doCheck := true) with
    | .error error =>
      throw <| IO.userError s!"Kernel rejected instance pair {id}: {← (error.toMessageData {}).toString}"
    | .ok checked => env := checked
    let (axioms, _) ← (collectAxioms theoremName : CoreM (Array Name)).toIO
      { fileName := "<cleanup-instance-axioms>", fileMap := default } { env := env }
    for axiomName in axioms do
      unless axiomName == `propext || axiomName == `Classical.choice || axiomName == `Quot.sound do
        throw <| IO.userError s!"Unexpected witness axiom for {id}: {axiomName}"
    IO.println s!"Kernel-checked exact foundation pair {id}; axioms: {axioms.map fun name => name.toString}"
    records := records.push <| Json.mkObj [
      ("id", toJson id), ("before_expr", ← groundTree before),
      ("after_expr", ← groundTree after), ("type_expr", ← groundTree expectedType),
      ("inferred_before_type_expr", ← groundTree beforeType),
      ("inferred_after_type_expr", ← groundTree afterType),
      ("equality_type_expr", ← groundTree type), ("eq_refl_proof_expr", ← groundTree value),
      ("kernel_eq_refl_checked", toJson true),
      ("axioms", toJson (axioms.map fun name => name.toString)),
      ("axiom_policy_passed", toJson true),
      ("theorem_name", toJson theoremName.toString),
      ("witness", toJson "Eq.refl on the before expression checked against Eq before after")]
  let result := Json.mkObj [
    ("schema_version", toJson "qmdl-cleanup-instance-witnesses-v1"),
    ("status", toJson "passed"), ("kernel_check_explicitly_enabled", toJson true),
    ("allowed_axioms", toJson #["propext", "Classical.choice", "Quot.sound"]),
    ("project_modules_imported", toJson false),
    ("foundation_imports", toJson (modules.map fun item => item.module.toString)),
    ("instance_pair_input", input), ("pairs", toJson records),
    ("method", toJson "Exact closed Expr reconstruction; Environment.addDeclCore with doCheck=true; no Meta.isDefEq verdict and no skip-kernel option; no project import, normalization or custom axioms.")]
  IO.FS.writeFile outputPath result.compress
  IO.println s!"Kernel-checked {records.size} exact foundation instance pairs."
