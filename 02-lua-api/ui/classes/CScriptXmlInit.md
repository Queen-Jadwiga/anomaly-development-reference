# CScriptXmlInit

> ADR document set: **v0.1.59**. Research revisions and source/build versions below describe their original scope.

**Evidence:** Source-confirmed registration declaration; runtime deferred. **Engine:** `2026.5.15`.

**Registration:** [`ScriptXMLInit.cpp#L337-L384`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L337-L384).

**Native method declarations:** [`ScriptXMLInit.h#L30-L78`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.h#L30-L78).

| Method | Native signature (selected) | Notes |
|---|---|---|
| `ParseFile` | `void ParseFile(LPCSTR xml_file)` | Loads UI XML |
| `InitWindow` | `void InitWindow(LPCSTR path, int index, CUIWindow* pWnd)` | Initializes a provided window |
| `InitStatic` | `CUIStatic* InitStatic(LPCSTR path, CUIWindow* parent)` | Allocates and attaches |
| `InitTextWnd` | `CUITextWnd* InitTextWnd(LPCSTR path, CUIWindow* parent)` | Allocates and attaches |
| `InitScrollView` | `CUIScrollView* InitScrollView(LPCSTR path, CUIWindow* parent)` | Native XML initializer called before attachment |
| `InitProgressBar` | `CUIProgressBar* InitProgressBar(LPCSTR path, CUIWindow* parent)` | Same construction pattern |

For other registered names see `../registration-architecture-part-A.md`. No example code is included pending validation of Lua call sites and object lifetime.


## v0.1.12 registration-path update (October 11)

Source registration entry chain has been verified locally: `script_engine.cpp:399` → `script_engine_export.cpp:130` → `ui_export_script.cpp:44` → `ScriptXMLInit.cpp:363-405`. See [A-01 closure](../../../08-research/investigations/2026-10-11-A01-source-registration-closure.md). This supersedes the historical A-01 dispatcher uncertainty for the October 11 source only; behavior still requires runtime validation.
