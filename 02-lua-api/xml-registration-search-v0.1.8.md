# XML initializer Lua-registration search — v0.1.8

> ADR document set: **v0.1.66**. Research revisions and source/build versions below describe their original scope.

**Baseline:** `6a08e0905ce34748ee2904a5e0809f8afd141137` / MT-TEST 2026.05.15 candidate. **Runtime:** deferred.

## Confirmed native surface

The pinned [`UIXmlInit.h`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.h#L31-L92) declares `CUIXmlInit` with a public constructor and static methods including `InitWindow`, `InitStatic`, `InitTextWnd`, `InitFont`, and `InitScrollView`. These are **C++ signatures**, not evidence of Lua exposure. The corresponding [`UIXmlInit.cpp`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L47-L91) implements constructor → `InitColorDefs()` and native `InitWindow` layout work.

## Registration investigation status

- Neither of the inspected `UIXmlInit.h` and `UIXmlInit.cpp` contains an identified `CUIXmlInit::script_register` implementation or Luabind registration for the class.
- Guessed separate paths `ui/UIXmlInit_script.cpp`, `ui/UIXmlInit_script.h` and `ui/xrUIXmlParser_script.cpp` returned HTTP 404; that **does not** prove there is no binding elsewhere.
- Web-indexed searches did not produce a verifiable historical `class_<CUIXmlInit>` declaration or corresponding Lua wrapper. **No positive or negative whole-repository registration conclusion is warranted.**

| Lua candidate | Conclusion | Evidence level |
|---|---|---|
| `CUIXmlInit()` | No historical registration found in inspected files | Unresolved |
| `CUIXmlInit.InitStatic(...)` | Native method exists; no Lua registration identified | Unresolved |
| `CUIXmlInit.InitScrollView(...)` | Native method exists; no Lua registration identified | Unresolved |
| Alternate Lua XML helper class | Could exist in a separate script binding or Lua wrapper | Unresolved |

## How to close this investigation

When a clone of the pinned repository is available, run a **complete** tree search:

```bash
git checkout 6a08e0905ce34748ee2904a5e0809f8afd141137
git grep -n -E 'CUIXmlInit|class_<.*CUIXml|script_register|InitScrollView' -- src
```

Inspect matches around `module(...)`, `class_(...)`, and bound `.def(...)`; then identify the actual exported Lua name and ownership policy. A full-tree search was not performed during v0.1.8 because the source archive was not available to this runtime.

**Coding restriction:** Do not introduce Lua code calling native initializer methods until their bindings are confirmed.
