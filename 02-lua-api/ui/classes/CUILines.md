# CUILines — declaration audit (ADR v0.1.5)

> ADR document set: **v0.1.74**. Research revisions and source/build versions below describe their original scope.

**Evidence level:** Source-confirmed native declarations and previously extracted Lua registrations at pinned commit; **GAMMA runtime untested.** Only methods already listed in the previous Lua registration inventory are treated as exported. Other native methods are not automatically Lua-accessible.

Sources: [UILines.h](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UILines.h#L17-L70) and [Lua registration](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIStatic_script.cpp).

| Lua-visible method | Native declaration / result | Notes |
|---|---|---|
| `SetFont(font)` | `CGameFont*` → `void` | Native font pointer |
| `SetText(text)` | `LPCSTR` → `void` | Literal text |
| `SetTextST(text)` | `LPCSTR` → `void` | String-table path; confirm semantics |
| `GetText()` | none → `LPCSTR` | Native-managed text buffer |
| `SetTextColor(color)` | `u32` → `void` | Packed color |
| `SetElipsis(mode)` | native `SetEllipsis(bool)` → `void` | **Lua registration spelling is `SetElipsis`**, per previous extraction; verify exact spelling before runtime tests |

The C++ declaration also includes text alignment, word-wrap, complex mode and other methods, but their presence in native code does **not** mean that the `CUILines` Lua registration exports them. `CUILines` is generally obtained through another window's text control; its own constructor is not in the recorded Lua bindings.
