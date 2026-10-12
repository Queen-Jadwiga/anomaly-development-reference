# XML font resolution and text initialization (ADR v0.1.6)

> ADR document set: **v0.1.59**. Research revisions and source/build versions below describe their original scope.

**Target:** X-Ray Monolith tag `2026.5.15`, commit `6a08e0905ce34748ee2904a5e0809f8afd141137`. **Source-confirmed only; installed executable remains untested.**

## Accepted XML `font` attributes

`CUIXmlInit::InitFont` maps the following exact, case-sensitive XML strings to native `UI().Font()` pointers. These are **XML tokens**, not interchangeable Lua arguments or `.ttf` filenames.

| XML `font` | Native font pointer |
| --- | --- |
| `graffiti19` | `pFontGraffiti19Russian` |
| `graffiti22` | `pFontGraffiti22Russian` |
| `graffiti32` | `pFontGraffiti32Russian` |
| `graffiti50` | `pFontGraffiti50Russian` |
| `arial_14` | `pFontArial14` |
| `medium` | `pFontMedium` |
| `small` | `pFontStat` |
| `letterica16` | `pFontLetterica16Russian` |
| `letterica18` | `pFontLetterica18Russian` |
| `letterica25` | `pFontLetterica25` |
| `di` | `pFontDI` |

Source: [`UIXmlInit.cpp` lines 26–38](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L26-L38) and [font resolver lines 688–750](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L688-L750).

## Error behavior

- The parser retrieves `font` with `ReadAttrib(path,index,"font",NULL)`.
- If attribute is absent, `InitFont` sets its output pointer to null and returns `false`.
- If the attribute is present but unrecognized, it triggers `R_ASSERT3(0, "unknown font", font_name)`.
- When `InitText` is invoked for a present text node, it calls `InitFont` and asserts `R_ASSERT(pTmpFont)` before `SetFont`. Consequently **missing font on a present text node is also an assertion path**.
- A completely absent text node exits `InitText` without this sequence.

Evidence: [font resolver](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L688-L750), [text initialization](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L277-L325).

## Distinguish XML and Lua font paths

`CUITextWnd::SetFont` and `CUILines::SetFont` accept a native `CGameFont*`; XML `font="small"` is **not** equivalent to passing `"small"` in Lua. The previously catalogued global getters (e.g. `GetFontSmall`) are candidate pointer sources, subject to engine initialization timing and registration confirmation.

## CtZ implications

The historical implementation gives a **plausible** explanation for a font assertion during XML text initialization but does not establish the actual crash path. Before attributing the CtZ failure, compare the logged assertion/stack and effective XML after mod overrides against the exact parsing paths above.

**Unresolved:** Trace how each `UI().Font()` pointer is initialized, ascertain whether post-May patches are present, and runtime-test on the user's executable after return.

## Font lifecycle cross-reference

[Native `CGameFont` object](../01-engine/native-font-object-lifecycle.md) · [Integrated UI/Lua/native flow](../01-engine/ui-lua-native-integration.md) · [Open questions](../08-research/open-questions-v0.1.10.md).
