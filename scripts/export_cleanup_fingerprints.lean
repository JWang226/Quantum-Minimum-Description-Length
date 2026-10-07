/-
Copyright (c) 2026 Free Entropy formalization contributors.
See LICENSE and NOTICE in the repository root for license and attribution.
-/
module
import Lean

/-! Read-only structural evidence for a cleanup review.

Import the compiled project and serialize its actual expression trees as a DAG.
The serialization retains constructor tags, hierarchical names, universe levels,
binder names and annotations, and let flags. Kernel-irrelevant expression metadata
and internal cached hash fields are omitted. No proof is added or checked here.
The accompanying Python comparer checks structural identity, not definitional
equality or agreement with the manuscript. Theorem/proposition proof values are
deliberately omitted; non-proposition definition and opaque values are retained.
-/

open Lean

private def kind : ConstantInfo → String
  | .axiomInfo _ => "axiom"
  | .defnInfo _ => "definition"
  | .thmInfo _ => "theorem"
  | .opaqueInfo _ => "opaque"
  | .quotInfo _ => "quotient"
  | .inductInfo _ => "inductive"
  | .ctorInfo _ => "constructor"
  | .recInfo _ => "recursor"

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

private def binderKind : BinderInfo → String
  | .default => "explicit"
  | .implicit => "implicit"
  | .strictImplicit => "strict_implicit"
  | .instImplicit => "instance"

private structure Dag where
  nodes : Array Json := #[]
  -- Ordinary BEq Expr ignores binder annotations. ExprStructEq retains them.
  cache : ExprStructMap Nat := {}

private partial def expressionNode (expr : Expr) : StateT Dag IO Nat := do
  if let some id := (← get).cache.get? ⟨expr⟩ then return id
  if let .mdata _ body := expr then
    let id ← expressionNode body
    modify fun state => { state with cache := state.cache.insert ⟨expr⟩ id }
    return id
  let node ← match expr with
    | .bvar index => pure <| Json.arr #[toJson "bvar", toJson index]
    | .fvar _ => throw <| IO.userError "Unexpected free variable in a compiled declaration"
    | .mvar _ => throw <| IO.userError "Unexpected metavariable in a compiled declaration"
    | .sort level => pure <| Json.arr #[toJson "sort", levelTree level]
    | .const name levels =>
      pure <| Json.arr #[toJson "const", nameTree name, toJson (levels.map levelTree)]
    | .app fn arg => do
      let fn ← expressionNode fn
      let arg ← expressionNode arg
      pure <| Json.arr #[toJson "app", toJson fn, toJson arg]
    | .lam name type body info => do
      let type ← expressionNode type
      let body ← expressionNode body
      pure <| Json.arr #[toJson "lam", nameTree name, toJson type, toJson body,
        toJson (binderKind info)]
    | .forallE name type body info => do
      let type ← expressionNode type
      let body ← expressionNode body
      pure <| Json.arr #[toJson "forall", nameTree name, toJson type, toJson body,
        toJson (binderKind info)]
    | .letE name type value body nondep => do
      let type ← expressionNode type
      let value ← expressionNode value
      let body ← expressionNode body
      pure <| Json.arr #[toJson "let", nameTree name, toJson type, toJson value,
        toJson body, toJson nondep]
    | .lit (.natVal value) => pure <| Json.arr #[toJson "nat_literal", toJson value]
    | .lit (.strVal value) => pure <| Json.arr #[toJson "string_literal", toJson value]
    | .proj type index struct => do
      let struct ← expressionNode struct
      pure <| Json.arr #[toJson "proj", nameTree type, toJson index, toJson struct]
    | .mdata _ _ => throw <| IO.userError "Unreachable metadata branch"
  let id := (← get).nodes.size
  modify fun state => { nodes := state.nodes.push node, cache := state.cache.insert ⟨expr⟩ id }
  return id

private def isProposition (env : Environment) (type : Expr) : IO Bool := do
  let (result, _, _) ← (Meta.isProp type).toIO
    { fileName := "<cleanup-fingerprint>", fileMap := default } { env := env }
  return result

public unsafe def main (args : List String) : IO Unit := do
  let [seedPath, outPath] := args
    | throw <| IO.userError "Expected seed JSON path and output JSON path"
  let seedText ← IO.FS.readFile seedPath
  let seedJson ← IO.ofExcept <| Json.parse seedText
  let seedNames ← IO.ofExcept <| seedJson.getObjValAs? (Array String) "public_declarations"
  let mut seeds : NameSet := {}
  for name in seedNames do
    let name := name.toName
    if seeds.contains name then throw <| IO.userError s!"Duplicate seed: {name}"
    seeds := seeds.insert name
  initSearchPath (← findSysroot)
  enableInitializersExecution
  let env ← importModules #[{ module := `FreeEntropy }] {}
    (leakEnv := true) (loadExts := true)
  let mut seen : NameSet := {}
  let mut declarations : Array Json := #[]
  let mut dag : Dag := {}
  for idx in [:env.header.moduleData.size] do
    let moduleName := env.allImportedModuleNames[idx]!
    unless (`FreeEntropy).isPrefixOf moduleName do continue
    for item in env.header.moduleData[idx]!.constants do
      if seen.contains item.name then continue
      seen := seen.insert item.name
      let some ci := env.checked.get.find? item.name
        | throw <| IO.userError s!"Missing compiled declaration: {item.name}"
      let some origin := env.getModuleIdxFor? ci.name
        | throw <| IO.userError s!"Missing defining module: {ci.name}"
      let (typeRoot, nextDag) ← (expressionNode ci.type).run dag
      dag := nextDag
      let mut valueRoot : Json := Json.null
      let mut valueClass := "absent"
      if let some value := ci.value? (allowOpaque := true) then
        if ← isProposition env ci.type then
          valueClass := "proof_omitted"
        else
          let (root, nextDag) ← (expressionNode value).run dag
          dag := nextDag
          valueRoot := toJson root
          valueClass := "data"
      declarations := declarations.push <| Json.mkObj [
        ("name", toJson ci.name.toString), ("name_tree", nameTree ci.name),
        ("kind", toJson (kind ci)),
        ("module", toJson env.allImportedModuleNames[origin.toNat]!.toString),
        ("public_audit_seed", toJson (seeds.contains ci.name)),
        ("level_parameters", toJson (ci.levelParams.map nameTree)),
        ("type_root", toJson typeRoot), ("value_root", valueRoot),
        ("value_class", toJson valueClass), ("is_unsafe", toJson ci.isUnsafe),
        ("is_partial", toJson ci.isPartial)]
  for name in seeds do
    unless seen.contains name do throw <| IO.userError s!"Public audit seed missing: {name}"
  let result := Json.mkObj [
    ("schema_version", toJson "qmdl-cleanup-fingerprints-v1"),
    ("seed_provenance", seedJson),
    ("serialization_policy", toJson "Exact Expr constructor trees modulo Expr.mdata; all hierarchical names, levels, binder annotations and let flags retained; cached internal fields omitted; proof values omitted; no normalization or unfolding."),
    ("nodes", toJson dag.nodes), ("declarations", toJson declarations)]
  IO.FS.writeFile outPath result.compress
  IO.println s!"Exported {declarations.size} declarations, {seedNames.size} public seeds and {dag.nodes.size} expression nodes."
