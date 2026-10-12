# Native `CGameFont` lifecycle — May 15, 2026 source

> ADR document set: **v0.1.82**. Research revisions and source/build versions below describe their original scope.

**Research scope:** ADR v0.1.10 Part B. **Engine target:** X-Ray Monolith tag `2026.5.15`, pinned commit `6a08e0905ce34748ee2904a5e0809f8afd141137`. **Runtime:** deferred.

## Source-confirmed object-level sequence

1. Two native constructors are defined: `CGameFont(LPCSTR section, u32 flags)` and `CGameFont(LPCSTR shader, LPCSTR texture, u32 flags)`. Both obtain a font-renderer object through `RenderFactory->CreateFontRender()` and invoke `Initialize`.
2. The section-based constructor selects a texture key by the rendering resolution, reads a shader and font sizing/spacing configuration from `pSettings`, then initializes the renderer and glyph data. This does **not** mean Lua can invoke either constructor.
3. `CGameFont::Initialize(cShader, cTextureName)` resolves an optional language-specific texture suffix, asserts that a glyph-metrics `.ini` exists under `$game_textures$`, reads a supported metrics layout (`mb_symbol_coords`, `symbol_coords`, `char widths`, or `font_size`), and calls `pFontRender->Initialize(cShader, cTexture)`.
4. `CGameFont::~CGameFont()` releases the character metrics table (`TCMap`) and delegates renderer destruction to `RenderFactory->DestroyFontRender(pFontRender)`.
5. `CGameFont::OnRender()` calls `pFontRender->OnRender(*this)` and clears the queued strings without releasing capacity.

**Exact historical source:** [https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrEngine/GameFont.cpp](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrEngine/GameFont.cpp) (constructor near lines 1047–1137; initialization lines 1139–1344; destructor lines 1346–1358; OnRender near 1388–1395 in GitHub's page rendering).

## Important boundary

These findings describe **the lifetime of one native font object**, not the higher-level UI font manager's startup, registration of named getter pointers, or global shutdown sequence. `x_ray.cpp` was checked as a candidate location but did not yield `pFontSystem` / `_InitializeFont` in this revision; do not copy old-engine lifecycle assumptions into the Monolith record.

## Failure implications (hypotheses, not diagnoses)

- Missing metrics `.ini` can trip an initialization assertion.
- A mismatched texture/shader/metrics set can break font construction or rendering.
- A null or invalid `CGameFont*` remains a separate UI binding issue.

Nothing here proves which failure occurred in the Capture the Zone crash.
