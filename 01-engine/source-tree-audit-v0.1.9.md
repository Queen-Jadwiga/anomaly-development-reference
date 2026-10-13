# Historical source-tree audit — ADR v0.1.9

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

**Revision:** `2026.5.15`; recorded full commit `6a08e0905ce34748ee2904a5e0809f8afd141137` (confirm locally against `git rev-parse`).
**Coverage:** partial; NOT a repository-wide inventory.
**Reason:** a complete Git checkout/archive could not be retrieved from this environment. Raw individual source paths were inspected using GitHub's hosted files. Do not describe this as a complete repository analysis.

## Confirmed historical files

| Path | Role | Evidence |
|---|---|---|
| `src/xrGame/ui/UIXmlInit.h` | Native declarations for `CUIXmlInit` | [Pinned header](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.h) |
| `src/xrGame/ui/UIXmlInit.cpp` | Native XML initialization and font resolution | [Pinned implementation](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp) |

## Native call flow verified from implementation

- `CUIXmlInit::InitStatic` calls `InitWindow`, then `InitText` for the nested `:text` path; it also configures texture and effects.
- `CUIXmlInit::InitTextWnd` calls `InitWindow`, then `InitText` with `TextItemControl()`.
- `CUIXmlInit::InitText(CUILines*)` first checks for the XML node, calls `InitFont`, checks for a valid returned `CGameFont*`, and passes it to `CUILines::SetFont`.
- `CUIXmlInit` constructor calls `InitColorDefs`; this is **not** font manager initialization.

Source: [UIXmlInit.cpp lines 47–50, 138–192, 277–296](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L277-L296).

## Export boundary

`CUIXmlInit.h` declares a native C++ class. No conclusion about an exposed Lua `CUIXmlInit` class follows from these declarations alone. **Lua registration remains unverified** until every relevant binding translation unit is searched.

## Pending source-tree inventory

Record: full directory listing, registration units, `CUIXmlInit` references, font getters, `CGameFont` creation/deletion, engine init order, and linkage; do not fill guessed paths.
