# Font manager and Lua-facing getters — interface boundary (ADR v0.1.7)

> ADR document set: **v0.1.77**. Research revisions and source/build versions below describe their original scope.

**Baseline:** `6a08e0905ce34748ee2904a5e0809f8afd141137`. Runtime verification is deferred.

## Three distinct concepts

1. **XML font tokens.** The native parser maps XML attributes such as `font="small"` to `UI().Font()` pointers. The supported token table and assertion paths are documented in [fonts.md](fonts.md), traced to [`UIXmlInit.cpp`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp).
2. **Native font objects.** `CUITextWnd::SetFont` takes a `CGameFont*`; it does not take a string token. This is supported by the earlier declaration audit.
3. **Lua getter globals.** The earlier v0.1.3 registration survey identified the global font getters below as source-registered names. Their return objects' non-nullness at any particular initialization phase has **not** been tested.

| Lua global getter | XML token mapping (if known) | Confidence |
|---|---|---|
| `GetFontSmall()` | `small` | Getter name previously extracted; runtime untested |
| `GetFontMedium()` | `medium` | Same |
| `GetFontDI()` | `di` | Same |
| `GetFontGraffiti19Russian()` | `graffiti19` | Same |
| `GetFontGraffiti22Russian()` | `graffiti22` | Same |
| `GetFontGraffiti32Russian()` | `graffiti32` | Same |
| `GetFontGraffiti50Russian()` | `graffiti50` | Same |
| `GetFontLetterica16Russian()` | `letterica16` | Same |
| `GetFontLetterica18Russian()` | `letterica18` | Same |
| `GetFontLetterica25()` | `letterica25` | Same |

The XML parser also supports `arial_14`; this audit **does not assert** that a corresponding Lua getter is exposed in the installed build.

## API safety rules

- Never pass an XML token string directly to `CUITextWnd:SetFont` or `CUILines:SetFont`.
- Do not assume a getter is usable before UI font manager initialization, or after shutdown.
- Check the actual script binding and runtime object before relying on it; do not infer a custom font getter from the XML list.
- For CtZ crashes, inspect the effective XML and stack before assigning blame to a missing or unknown font.

## Remaining source work

Trace the font manager's initialization order, `CGameFont*` lifetime and the *exact pinned global Lua export registration sites*. This pass cross-linked the existing source findings; it did not independently finish this complete registration search.

## Part B update

Native `CGameFont` constructor/destructor/renderer lifecycle now mapped in [engine object lifecycle](../01-engine/native-font-object-lifecycle.md). Higher-level manager ownership and startup remain unresolved; see [Part B investigation](../08-research/investigations/2026-10-09-part-B-native-font-manager.md).
