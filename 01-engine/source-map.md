# Source code map — work in progress

> ADR document set: **v0.1.48**. Research revisions and source/build versions below describe their original scope.

**Important:** No exact 2026-05-15 source commit has yet been pinned. The paths below are navigation targets, not verified file-location assertions.

| Topic | Search identifiers | Next action |
|---|---|---|
| UI widgets | `CUIWindow`, `CUIStatic`, `CUIScrollView`, `CUIXmlInit` | Locate definitions and Lua exports |
| Fonts | `CGameFont`, `GetFont`, `font`, `CUIStatic` | Trace registry and invalid-font behavior |
| PDA windows | `UIPda`, `Pda`, `CUIPdaWnd` | Find interfaces and native scripting surface |
| Lua binding | `luabind`, `script_export` | Locate registration and ownership rules |
| Callbacks | `callback`, callback IDs | Compare C++ exports and GAMMA Lua |
| Warfare | `warfare`, `smart_terrain`, `squad` | Locate actual GAMMA scripts supplied by user |

Before citing any of these as supported APIs, capture a permalinking source line from the compatible commit.
