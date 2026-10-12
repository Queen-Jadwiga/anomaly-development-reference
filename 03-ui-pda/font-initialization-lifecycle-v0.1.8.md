# Native font initialization lifecycle — v0.1.8 evidence boundary

> ADR document set: **v0.1.58**. Research revisions and source/build versions below describe their original scope.

**Baseline:** May 15, 2026 source at `6a08e0905ce34748ee2904a5e0809f8afd141137`. **Runtime:** deferred.

## Confirmed: font access during XML parsing

1. `CUIXmlInit::CUIXmlInit()` invokes `InitColorDefs()`; this is color-definition setup, **not proof** of font-manager initialization. [Implementation](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L40-L56).
2. `CUIXmlInit::InitStatic` delegates to `InitWindow`, `InitText`, and texture initialization. [`UIXmlInit.cpp`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L138-L149).
3. `CUIXmlInit::InitTextWnd` delegates to `InitWindow` and `InitText` on its text item. [`UIXmlInit.cpp`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L186-L211).
4. `InitFont` resolves recognized XML token strings to native `UI().Font()` pointers. The exact token table and assertions are already documented in [fonts.md](fonts.md). [`UIXmlInit.cpp`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L688-L750).
5. The previously documented `InitText` path asserts that the resolved `CGameFont*` is non-null before applying it. [`UIXmlInit.cpp`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L277-L325).

## Not yet established: lifecycle order

The above provides a **call-site path**, not a complete manager lifecycle. We have **not located and audited** the pinned definitions for UI core creation/destruction, font-object allocation, `InitializeFonts` or equivalents, or renderer/device restart sequencing. As a result we **cannot currently claim** which engine-startup callback first makes any font getter safe, or whether a cached font pointer survives graphics resets.

## Preliminary event graph (scope-limited)

`XML widget initialization` → `InitText` → `InitFont` → `UI().Font().pFont*` → `SetFont(CGameFont*)`

Only this direct XML text initialization chain is supported; no broader startup lifecycle ordering is implied.

## Required follow-on source trace

Clone pinned revision, find `GetFontSmall`/`GetFontDI` registrations, `UI().Font()` implementation and `pFontStat` creation/destruction, and trace each back to engine startup and shutdown entry points. Record exact file/line anchors. Keep runtime verification pending as requested.

## Relevance to Capture the Zone

An invalid XML font token, missing font on an active text node, or null font pointer can follow different failure paths. None has yet been demonstrated as the cause of the user's crash. Do not treat a named XML token as a Lua `CGameFont*` or assume a newly constructed UI element is initialized.
