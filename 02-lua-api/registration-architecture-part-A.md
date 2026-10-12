# Part A — Luabind registration and XML initializer bridge (v0.1.10)

> ADR document set: **v0.1.70**. Research revisions and source/build versions below describe their original scope.

**Baseline:** X-Ray Monolith tag `2026.5.15`, commit `6a08e0905ce34748ee2904a5e0809f8afd141137` (matching reported build date; binary identity not proven). **Method:** targeted inspection of historical files, *not* full-repository search. **Runtime:** deferred.

## Confirmed registration site

[`src/xrGame/ScriptXMLInit.cpp`, lines 337–384](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L337-L384) defines `void CScriptXmlInit::script_register(lua_State* L)` and uses `luabind::module(L)[class_<CScriptXmlInit>("CScriptXmlInit").def(constructor<>()) ...]`.

This confirms that **`CScriptXmlInit`** (not the same C++ class as **`CUIXmlInit`**) has an explicit Luabind registration expression in this source revision. Whether and when the registration function is invoked during startup still requires tracing the engine's registration aggregator.

## Confirmed native bridge

- [`ScriptXMLInit.cpp`, lines 136–139](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L136-L139): `CScriptXmlInit::InitWindow` forwards to `CUIXmlInit::InitWindow`.
- [Lines 169–181](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L169-L181): `InitStatic` and `InitTextWnd` allocate their native widgets, initialize through `CUIXmlInit`, and attach them via `_attach_child`.
- [Lines 199–205](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L199-L205): `InitScrollView` allocates a `CUIScrollView`, calls `CUIXmlInit::InitScrollView` and attaches it.
- [Lines 313–319](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L313-L319): `InitProgressBar` follows the same pattern.
- [Lines 26–36](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L26-L36): `_attach_child` sets the auto-delete flag; scroll-view parents use `AddWindow(child, true)`, others use `AttachChild`.
- [`ScriptXMLInit.h`, lines 30–60](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.h#L30-L60): native type signatures for constructor-independent methods.

## Registered Lua names observed

The registration block includes: `ParseFile`, `ParseDirFile`, `NodeExist`, `GetNodesNum`, `NavigateToNode`, `NavigateToNode_ByAttribute`, `NavigateToNode_ByPath`, `NavigateToRoot`, `ReadValue`, `ReadAttribute`, `InitWindow`, `InitHint`, `InitFrame`, `InitFrameLine`, `InitEditBox`, `InitStatic`, `InitTextWnd`, `InitAnimStatic`, `InitSleepStatic`, `Init3tButton`, `InitCheck`, `InitSpinNum`, `InitSpinFlt`, `InitSpinText`, `InitComboBox`, `InitTab`, `InitServerList`, `InitMapList`, `InitMapInfo`, `InitTrackBar`, `InitCDkey`, `InitMPPlayerName`, `InitKeyBinding`, `InitMMShniaga`, `InitScrollView`, `InitListBox`, `InitProgressBar`.

These are source-observed registration *names*, not a runtime guarantee; signatures must be checked against the declaration, and object lifetime must be considered.

## Additional script integration hook

[`ScriptXMLInit.cpp`, lines 49–62](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L49-L62) defines `XMLLuaCallback`, which looks up `_G.COnXmlRead` and, when available, obtains a replacement XML string. **Open:** establish precisely which XML-loading paths invoke this callback, its error behavior, and its interaction with other mods.

## Boundary and conclusions

- **Confirmed:** `CScriptXmlInit` has a native Luabind export definition; its methods delegate to `CUIXmlInit`.
- **Not established:** direct registration of the separate native class `CUIXmlInit`. Do not infer absence from targeted searches.
- **Not established:** complete Lua script registration aggregator/startup order or exact correspondence to the user's executable binaries.
- **No runtime claims:** no scripts executed on the user's engine.

## Next source queries (full checkout when available)

```bash
git grep -n 'CScriptXmlInit::script_register' -- src
git grep -n -E 'CUIXmlInit::script_register|class_<CUIXmlInit>|"CUIXmlInit"' -- src
git grep -n -E 'script_register\(|script_type_list|add_to_type_list' -- src/xrGame src/xrServerEntities
```

Log the complete set of files searched, and preserve negative findings only with clearly scoped search coverage.

## Cross-layer integration

See [Part D integrated call-flow](../01-engine/ui-lua-native-integration.md) and [post-audit open questions](../08-research/open-questions-v0.1.10.md).
