# INV-014 — A-01/A-02 registration bootstrap audit (ADR v0.1.11)

> ADR document set: **v0.1.46**. Research revisions and source/build versions below describe their original scope.

**Research date:** 2026-10-09  
**Baseline:** X-Ray Monolith `2026.5.15` / `6a08e0905ce34748ee2904a5e0809f8afd141137`.  
**Verification:** historical targeted source inspection; **no comprehensive checkout or runtime checks**.  
**Result:** both A-01 and A-02 remain **OPEN**. This is an evidence/closure-method increment, not a claimed resolution.

## What is established

- [`CScriptXmlInit::script_register(lua_State*)`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L337-L384) defines a Luabind registration expression with `class_<CScriptXmlInit>("CScriptXmlInit")`, a default constructor, and XML parsing/widget initialization methods. This is a *definition of an export*, not proof that the function is called during startup.
- [`CScriptXmlInit::InitScrollView`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L199-L205) constructs and initializes a native widget through `CUIXmlInit`; the wrapper is distinct from direct registration of `CUIXmlInit`.
- The historical `ScriptXMLInit.cpp` source contains the registration definition and native wrapper code. It does not supply the call chain into `script_register` in the inspected region.

## A-01 — Trace bootstrap invocation (OPEN)

**Required chain:** engine startup → Lua state construction → registration aggregator/type list → `CScriptXmlInit::script_register(L)` → Lua-visible `CScriptXmlInit`.

**Unknown:** the registration aggregator's actual C++ symbol, file, and call order. Prior hypotheses about `script_type_list`/`add_to_type_list` remain search terms, **not confirmed mechanisms** for this build.

**Proof needed:** caller location at pinned commit, source-linked chain to Lua VM initialization, and any guards/conditional registration.

## A-02 — Is `CUIXmlInit` separately exposed? (OPEN)

`CUIXmlInit` appears as a native dependency of `CScriptXmlInit`; this does **not** show that the native class is itself registered to Luabind. Earlier audits inspected targeted files only. Searches for `class_<CUIXmlInit>`, quoted Lua class names, registration macros, typedef aliases, and binding wrappers must cover the entire pinned source tree. Negative conclusions are valid only with documented coverage, and dynamic registration could require further analysis.

**Proof needed:** direct registration path if present; otherwise full-tree search report (commit, scope, command, matched paths) and a carefully scoped statement that no registration was found *in the audited sources*.

## Retrieval limitations encountered

- The accessible source viewer returned the historical `ScriptXMLInit.cpp` successfully.
- A complete local historical repository checkout was **not** available during this audit. Container-side direct GitHub download failed due to network/DNS restrictions; browser access to a Git tree/archive index was also unsuccessful.
- Failed lookups of guessed file names were not treated as evidence of absence.

## Reproducible audit

From a complete checkout of the exact commit, run `python tools/audit_xml_lua_registrations.py PATH_TO_CHECKOUT`; save its generated Markdown result in `evidence/` and resolve the referenced invocation and alias cases manually.

Alternatively, on a Git-enabled machine:

```bash
git clone https://github.com/themrdemonized/xray-monolith.git
cd xray-monolith
git checkout 6a08e0905ce34748ee2904a5e0809f8afd141137
git rev-parse HEAD
git grep -n -F 'CScriptXmlInit::script_register' -- src
git grep -n -E 'class_<[[:space:]]*CUIXmlInit|CUIXmlInit::script_register|"CUIXmlInit"' -- src
git grep -n -E 'script_register|script_type_list|add_to_type_list|lua_State|luabind::module' -- src/xrGame
```

The last command is a **lead generator**, not proof of startup order. Follow caller references to the Lua state constructor and startup sites.

## Impact

Do not modify the `02-lua-api` documentation to claim direct native `CUIXmlInit` Lua support; the confirmed scripting path remains `CScriptXmlInit` only. Do not promote speculative bootstrap symbols to API facts. Runtime verification remains deferred.
