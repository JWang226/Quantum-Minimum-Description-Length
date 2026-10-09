/-
Copyright (c) 2026 Free Entropy formalization contributors.
See LICENSE and NOTICE in the repository root for license and attribution.
-/
import Lean

/-!
Check the actual compiled dependency closure of the independent physical
Theorem 2 statements. Start at theorem TYPES, excluding the deliberate challenge
proof holes, then follow every referenced declaration's type, body (including
opaque bodies), and inductive/constructor/recursor metadata. This checks the
specification boundary; it does not prove correspondence with the manuscript.

Usage from lean/:
  lake env lean --run ../scripts/check_physical_spec.lean OUTPUT.json
Optional MODULE ROOT... arguments support isolated negative-control fixtures.
No root proof body is traversed or executed. A root referenced by another
statement is rejected rather than silently exempted from dependency traversal.
-/
open Lean

private def defaultModule : Name := `ComparatorChallenges.Theorem2Physical

private def defaultRoots : Array Name := #[
  `FreeEntropy.ExteriorRepresentation.theorem2_cloning_accuracy_physical,
  `FreeEntropy.ExteriorRepresentation.theorem2_physical_realizations_exist]

private def forbiddenNames : Array Name := #[
  `sorryAx,
  `FreeEntropy.ExteriorRepresentation.canonicalOrbitState,
  `FreeEntropy.SchurWeyl.canonicalWeightTensorState,
  `FreeEntropy.SchurWeyl.canonicalTensorState,
  `FreeEntropy.SchurWeyl.canonicalTensorSource,
  `FreeEntropy.ExteriorRepresentation.canonicalChoiProjector,
  `FreeEntropy.ExteriorRepresentation.canonicalChoiEmbedding,
  `FreeEntropy.ExteriorRepresentation.canonicalReverseChoiProjector,
  `FreeEntropy.ExteriorRepresentation.canonicalReverseChoiEmbedding,
  `FreeEntropy.ExteriorRepresentation.prvForward,
  `FreeEntropy.ExteriorRepresentation.prvReverse,
  `FreeEntropy.SchurWeyl.canonicalWeightTensorState_eq_orbit,
  `FreeEntropy.SchurWeyl.physicalIsometricState_eq_orbit,
  `FreeEntropy.SchurWeyl.physicalIsometricState_eq_weightTensorState]

private def forbiddenModules : Array Name := #[
  `FreeEntropy.CanonicalChoi,
  `FreeEntropy.CanonicalReverseChoi,
  `FreeEntropy.ForwardChoiUniqueness,
  `FreeEntropy.PhysicalStateUniqueness,
  `FreeEntropy.PhysicalOrbitChannels,
  `FreeEntropy.PhysicalCanonicalSector,
  `FreeEntropy.CanonicalPhysicalOrbit,
  `FreeEntropy.Theorem2Canonical,
  `FreeEntropy.Theorem2Choi,
  `FreeEntropy.Theorem2Physical]

private def kind (ci : ConstantInfo) : String :=
  match ci with
  | .axiomInfo _ => "axiom"
  | .defnInfo _ => "definition"
  | .thmInfo _ => "theorem"
  | .opaqueInfo _ => "opaque"
  | .quotInfo _ => "quotient"
  | .inductInfo _ => "inductive"
  | .ctorInfo _ => "constructor"
  | .recInfo _ => "recursor"

private def structuralRefs (ci : ConstantInfo) : Array Name :=
  match ci with
  | .inductInfo i => i.ctors.toArray ++ i.all.toArray
  | .ctorInfo i => #[i.induct]
  | .recInfo i => i.all.toArray ++ i.rules.toArray.flatMap
      (fun r => #[r.ctor] ++ r.rhs.getUsedConstants)
  | _ => #[]

private def references (ci : ConstantInfo) : Array Name :=
  ci.type.getUsedConstants ++
    ((ci.value? (allowOpaque := true)).map Expr.getUsedConstants |>.getD #[]) ++
    structuralRefs ci

private def strings (ns : Array Name) : Json := toJson (ns.map Name.toString)

private def moduleOf (env : Environment) (name : Name) : Option Name := do
  let idx ← env.getModuleIdxFor? name
  env.allImportedModuleNames[idx.toNat]?

unsafe def main (args : List String) : IO Unit := do
  let (outPath, moduleName, roots) ← match args with
    | [outPath] => pure (outPath, defaultModule, defaultRoots)
    | outPath :: moduleName :: first :: rest =>
      pure (outPath, moduleName.toName, (first :: rest).toArray.map String.toName)
    | _ => throw <| IO.userError "Expected OUTPUT.json [MODULE ROOT...]"
  if roots.isEmpty || roots.size != (roots.foldl (fun s n => s.insert n) ({} : NameSet)).size then
    throw <| IO.userError "Theorem roots must be nonempty and unique"
  initSearchPath (← findSysroot)
  enableInitializersExecution
  let env ← importModules #[{ module := moduleName }] {} (leakEnv := true) (loadExts := true)
  let mut todo : Array Name := #[]
  let mut rootRecords : Array Json := #[]
  for root in roots do
    let some ci := env.checked.get.find? root
      | throw <| IO.userError s!"Missing expected theorem: {root}"
    unless match ci with | .thmInfo _ => true | _ => false do
      throw <| IO.userError s!"Expected root is not a theorem: {root}"
    let refs := ci.type.getUsedConstants
    todo := todo ++ refs
    rootRecords := rootRecords.push <| Json.mkObj [
      ("name", toJson root.toString), ("type_references", strings refs),
      ("root_proof_body_traversed", toJson false)]
  let mut seen : NameSet := {}
  let mut projectRecords : Array (Name × Json) := #[]
  let mut specificationRecords : Array (Name × Json) := #[]
  let mut axioms : Array Name := #[]
  while !todo.isEmpty do
    let name := todo.back!
    todo := todo.pop
    if seen.contains name then continue
    if roots.contains name then
      throw <| IO.userError s!"Challenge proof root referenced in expected type closure: {name}"
    if forbiddenNames.contains name then
      throw <| IO.userError s!"Forbidden constructed state/projector/proof dependency: {name}"
    let some ci := env.checked.get.find? name
      | throw <| IO.userError s!"Missing compiled dependency: {name}"
    let origin := moduleOf env name
    if let some mod := origin then
      if forbiddenModules.contains mod then
        throw <| IO.userError s!"Forbidden proof/construction module in expected type closure: {mod} ({name})"
    seen := seen.insert name
    todo := todo ++ references ci
    match ci with
    | .axiomInfo _ => axioms := axioms.push name
    | _ => pure ()
    if let some mod := origin then
      let entry := Json.mkObj [
        ("name", toJson name.toString), ("module", toJson mod.toString),
        ("kind", toJson (kind ci))]
      if (`FreeEntropy).isPrefixOf mod then
        projectRecords := projectRecords.push (name, entry)
      else if moduleName == mod then
        specificationRecords := specificationRecords.push (name, entry)
  let byName := fun (a b : Name × Json) => decide (a.1.toString < b.1.toString)
  projectRecords := projectRecords.qsort byName
  specificationRecords := specificationRecords.qsort byName
  let report := Json.mkObj [
    ("schema_version", toJson "qmdl-physical-spec-boundary-v1"),
    ("status", toJson "passed"), ("module", toJson moduleName.toString),
    ("roots", toJson rootRecords), ("dependency_count", toJson seen.size),
    ("shared_project_dependencies", toJson (projectRecords.map (·.2))),
    ("independently_redeclared_dependencies", toJson (specificationRecords.map (·.2))),
    ("referenced_axioms", strings (axioms.qsort (fun a b => decide (a.toString < b.toString)))),
    ("forbidden_names", strings forbiddenNames), ("forbidden_modules", strings forbiddenModules),
    ("policy", toJson "Compiled theorem types plus full transitive declaration references; target proof bodies excluded. This guard does not establish independent human or manuscript correspondence review.")]
  IO.FS.writeFile outPath (report.pretty ++ "\n")
  IO.println s!"PHYSICAL SPECIFICATION BOUNDARY PASSED: {roots.size} theorem types; {seen.size} dependencies; {projectRecords.size} shared project declarations."
