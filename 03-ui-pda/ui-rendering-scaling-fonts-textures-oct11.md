# UI rendering, aspect scaling, native font and texture paths — 2026-10-11 source

> ADR document set: **v0.1.79**. Research revisions and source/build versions below describe their original scope.

**Status:** CtZ-relevant source pass complete; no runtime verification. **Scope:** XML initialization, named fonts, aspect-related filename selection, and `CUIStatic` texture initialization. This is **not** an exhaustive renderer or device backend audit.

## Verified implementation links (October 11 source)

Source root: `xray-monolith-2026.10.11/src/xrGame/`; official source location: https://github.com/themrdemonized/xray-monolith/tree/2026.10.11/src/xrGame (uploaded ZIP is the inspected evidence; remote tag contents have not been independently checked here).

1. **XML font resolution is finite and asserts for unknown font names.** `ui/UIXmlInit.cpp:747–811`, `CUIXmlInit::InitFont`, matches XML `font` attributes against 11 native names, obtains pointers from `UI().Font()`, and uses `R_ASSERT3(0, "unknown font", font_name)` for unknown names. `ui/UIXmlInit.cpp:313–325`, `InitText`, asserts that the resolved font pointer is non-null before `SetFont`. Therefore CtZ must use known configured font identifiers or a separately verified font provisioning path. A C++ token being accepted is not proof its configured texture/shader resources exist in any particular GAMMA install.
2. **Named font initialization and reset reuse.** `HUDManager.cpp:55–108`, `CFontManager::InitializeFonts`, `InitializeFont`, `OnDeviceReset`, and destructor. Font creation consults `GetFontTextureName(section)` and `pSettings->r_string(section, "shader")`, constructs `CGameFont` if absent, and otherwise reinitializes the existing pointer. Device-reset handling calls `InitializeFonts`. This corroborates B-01/B-02; it does not establish arbitrary Lua-held font-reference safety.
3. **Resolution variants and aspect scaling are separate concerns.** `ui_base.cpp:270–339`, `ui_core::is_widescreen`, `screenmode`, `get_current_kx`, `get_xml_name`. The `screenmode` tests select normal, `_16`, or `_21` XML candidates with file-existence fallback. `get_current_kx` computes a screen-ratio coefficient, except in aspect-neutral/world-pass conditions where it returns `1.0f`. This is **not** evidence that every UI widget scales identically: downstream coordinate and rendering consumers require separate inspection when CtZ needs them.
4. **XML texture nodes delegate to native texture owner.** `ui/UIXmlInit.cpp:1013–1048`, `CUIXmlInit::InitTexture`, reads `<texture>` text and optional `shader`, calls `InitTextureEx` or `InitTexture`, reads atlas `x/y/width/height`, root `stretch`, and texture `color`, and sets the texture rectangle only if both dimensions are nonzero. `ui/UIStatic.cpp:60–74` shows `CUIStatic::InitTexture[Ex]` delegates to `CUITextureMaster::InitTexture`, with a default `hud\default` shader when unspecified. The presence of a texture name in XML does not prove the referenced atlas/asset exists in the user's installed gamedata.
5. **Static text and texture are distinct paths.** `ui/UIStatic.h:46–55, 163–171` exposes texture attributes and text/font controls on `CUIStatic`, but header declarations by themselves do not prove Lua exposure. Consult the existing `02-lua-api/ui-binding-inventory-oct11.csv` and exact registration records for a Lua call.

## CtZ decisions supported now

- Prefer supplied, configured native font names; validate XML font identifiers and required resources before packaging.
- Use `CUIXmlInit` XML conventions for texture/shader/atlas rectangle; validate assets and possible `_16`/`_21` filenames.
- Keep War PDA layout in native UI coordinates and check actual resolution/layout in deferred runtime tests; avoid claiming universal aspect-ratio correctness from `get_current_kx` alone.
- Avoid allocating or deleting `CGameFont` objects in Lua unless a separate verified ownership design exists.

## Deliberately open / deferred

- **UI-08a (source, only if implementation requires):** exact renderer backend/UI coordinates and pixel-snap/font rasterization behavior across DX8–DX11; not an ADR blocking issue for CtZ.
- **UI-08b (source, if asset failures arise):** `CUITextureMaster` lookup/atlas resource error behavior and path normalization.
- **UI-08c (runtime):** real font readability, texture existence, clipping, tab resizing and `_16`/`_21` fallback at CtZ target resolutions.
- Previous UI-06 exhaustive export/build/global-input questions remain indexed; not promoted to runtime-verified nor claimed resolved.

**Subsystem disposition:** UI is **development-reference ready, runtime pending** for the functions CtZ currently plans to use. Full engine-wide UI exhaustiveness is expressly out of scope. Next research focus: A-Life/Warfare squad and smart-terrain lifecycle, ownership, and offline transitions.
