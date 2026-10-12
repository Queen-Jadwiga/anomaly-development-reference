# CUIStatic — declaration audit (ADR v0.1.5)

> ADR document set: **v0.1.67**. Research revisions and source/build versions below describe their original scope.

**Evidence level:** Source-confirmed native declarations and previously extracted Lua registrations at pinned commit; **GAMMA runtime untested.** Only methods already listed in the previous Lua registration inventory are treated as exported. Other native methods are not automatically Lua-accessible.

Sources: [CUIStatic / CUITextWnd declarations](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIStatic.h#L51-L160) and [Lua registration](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIStatic_script.cpp).

| Lua-visible method | Native declaration / result | Caveat |
|---|---|---|
| `CUIStatic()` | Constructor | Instantiation and parenting require lifetime review |
| `SetTextureColor(color)` | `u32` → `void` | Packed engine color, not a CSS/string color |
| `GetTextureColor()` | none → `u32` | |
| `SetTextureRect(rect)` | `Frect*` through `SetTextureRect_script` → `void` | Verify Lua userdata passing syntax before use |
| `GetTextureRect()` | none → `const Frect*` through script wrapper | Native-owned reference; avoid retaining past owner lifetime |
| `InitTexture(name)` | `LPCSTR` → `void` | Texture must exist; not a font registration call |
| `InitTextureEx(name, shader)` | `LPCSTR, LPCSTR` → `void` | Native default shader `hud\default` must not be assumed preserved by every Lua binding |
| `SetStretchTexture(stretch)` | `bool` → `void` | |
| `GetStretchTexture()` | none → `bool` | |
| `AdjustHeightToText()` / `AdjustWidthToText()` | none → `void` | Text must already be properly initialized |
| `EnableHeading(enabled)` | `bool` → `void` | |
| `SetHeading(angle)` / `GetHeading()` | `float` → `void` / none → `float` | Unit conventions still need verification |
| `SetConstHeading(enabled)` / `GetConstHeading()` | `bool` → `void` / none → `bool` | |

## Outstanding bindings
`TextControl`, `SetColorAnimation`, `ResetColorAnimation`, and `RemoveColorAnimation` remain **signature pending** because their actual binding wrappers/overloads need individual examination. Do not infer arguments from names.

## Ownership
`CUIStatic` subclasses `CUIWindow`. Its text control is a native-managed member/pointer; treat it as borrowed unless ownership is explicitly proven otherwise. The parent-child ownership guidance from `CUIWindow` remains applicable.
