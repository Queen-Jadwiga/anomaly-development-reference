# A-01 — Complete October 11 registration chain

> ADR document set: **v0.1.77**. Research revisions and source/build versions below describe their original scope.

**Status:** SOURCE RESEARCH COMPLETE — runtime validation pending.  **Date:** 2026-10-11.

**Question:** How does engine initialization invoke `CScriptXmlInit::script_register(lua_State*)`?

## Verified direct code links (local October 11 source archive)

1. `src/xrServerEntities/script_engine.cpp:367` declares `extern void export_classes(lua_State* L);`; `:399` within `CScriptEngine::init()` calls `export_classes(lua())` after `::luabind::open(lua())` and `setup_callbacks()`.
2. `src/xrServerEntities/script_engine_export.cpp:26` defines `export_classes(lua_State* L)`; `:130` invokes `UIRegistrator::script_register(L)` in its conditional registration branch. The build preprocessor conditions must be respected.
3. `src/xrGame/ui_export_script.cpp:29` defines `UIRegistrator::script_register(lua_State* L)` and `:44` invokes `CScriptXmlInit::script_register(L)`.
4. `src/xrGame/ScriptXMLInit.cpp:363` defines `CScriptXmlInit::script_register(lua_State* L)`; `:365-405` uses `module(L)` and `class_<CScriptXmlInit>("CScriptXmlInit")` to register constructor and selected XML/UI methods.
5. `src/xrGame/ScriptXMLInit.h` declares the native class. `DECLARE_SCRIPT_REGISTER_FUNCTION` declares the static entry point; the explicit UI registrator is what invokes it.

The complete source-level call chain is therefore:

`CScriptEngine::init()` → `export_classes(lua())` → `UIRegistrator::script_register(L)` → `CScriptXmlInit::script_register(L)` → Luabind class registration.

## Source links (permalinks to locally named tag; remote availability not independently verified)

- https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrServerEntities/script_engine.cpp#L395-L401
- https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrServerEntities/script_engine_export.cpp#L125-L133
- https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_export_script.cpp#L29-L47
- https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ScriptXMLInit.cpp#L363-L405

**Evidence standard:** file paths and quoted line numbers verified directly in uploaded source archive. GitHub URLs are navigation candidates until independently confirmed accessible; do not call them verified remote links.

## What this closure does and does not prove
- **Proved for uploaded source:** the registration dispatcher and class-specific call chain exist.
- **Not yet proved:** that a particular user-installed compiled executable follows that source exactly or that arbitrary `CScriptXmlInit()`/`ParseFile()` usage is safe across all GAMMA UI contexts.
- **Runtime test when available:** initialize a known safe UI context, construct `CScriptXmlInit()`, parse a known XML document, check expected widgets, capture log and any crash. Do not use a test to infer unrelated lifetime guarantees.

A-01 now meets the agreed source research stopping threshold. Reopen only for contradictory source/binary evidence or a specific runtime failure; do not conflate this with A-02, separate `CUIXmlInit` Lua exposure.
