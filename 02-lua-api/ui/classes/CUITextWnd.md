# CUITextWnd — declaration audit (ADR v0.1.5)

> ADR document set: **v0.1.50**. Research revisions and source/build versions below describe their original scope.

**Evidence level:** Source-confirmed native declarations and previously extracted Lua registrations at pinned commit; **GAMMA runtime untested.** Only methods already listed in the previous Lua registration inventory are treated as exported. Other native methods are not automatically Lua-accessible.

Sources: [declarations in UIStatic.h](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIStatic.h#L132-L160), [Lua registration](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIStatic_script.cpp), [CUILines.h](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UILines.h).

| Lua-visible method | Native declaration / result | Notes |
|---|---|---|
| `CUITextWnd()` | constructor | UI ownership still applies |
| `SetText(txt)` | `LPCSTR` → `void` | Literal text |
| `SetTextST(txt)` | `LPCSTR` → `void` | Localized/string-table path; semantics require runtime confirmation |
| `GetText()` | none → `LPCSTR` | Native-managed text buffer; copy if needed |
| `SetFont(font)` | `CGameFont*` → `void` | **Font object pointer, not a font name string** |
| `GetFont()` | none → `CGameFont*` | Borrowed native pointer |
| `SetTextColor(color)` | `u32` → `void` | Packed engine color |
| `GetTextColor()` | none → `u32` | |
| `SetTextComplexMode(mode)` | `bool` → `void` | C++ declaration default `true`; explicitly pass an argument in Lua |
| `SetTextAlignment(align)` | `ETextAlignment` → `void` | Exact Lua constants pending |
| `SetVTextAlignment(align)` | `EVTextAlignment` → `void` | Exact Lua constants pending |
| `SetEllipsis(enabled)` | `bool` → `void` | |
| `SetTextOffset(x,y)` | `float,float` → `void` | |
| `AdjustHeightToText()` / `AdjustWidthToText()` | none → `void` | |

**Safety implication:** `SetFont` requires a valid engine-managed `CGameFont*`. Supplying arbitrary font identifiers or names is not equivalent. Verify available font getters and initialization sequence before constructing a CtZ window.

**Not asserted exported:** `SetCutWordsMode` exists in the native class but was not in our listed Lua registration inventory. Native declarations alone do not establish access.
