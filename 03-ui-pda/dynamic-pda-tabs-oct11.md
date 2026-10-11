# October 11 UI survey — native dynamic PDA tabs

> ADR document set: **v0.1.53**. Research revisions and source/build versions below describe their original scope.

**Version:** xray-monolith source tag `2026.10.11` only. **Evidence:** native exports and bundled Lua implementation, **not runtime-tested**.

## Verified

- The bundled `gamedata/scripts/pda_dynamic_tabs.script` documents `register(caption_key, ui_getter, after)` and `unregister(id)`; tab IDs are generated as `ept_dynamic_<n>`. It provides the integration contract and notes limitations: width and art derive from tab strip, long labels may clip, icon textures are optional. [gamedata/scripts/pda_dynamic_tabs.script:1-36](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/pda_dynamic_tabs.script#L1-L36)
- The registry's `apply` asks `ActorMenu.get_pda_menu():RebuildTabs()` when `level.present()` and PDA menu exists; `build_extra_tabs` calls `tab_control:AddTab` and optional `SetTabIcon`. [gamedata/scripts/pda_dynamic_tabs.script:38-99](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/pda_dynamic_tabs.script#L38-L99)
- `CUIPdaWnd::Init` calls `RebuildExtraTabs`; the rebuild removes dynamic tabs, invokes `pda_dynamic_tabs.build_extra_tabs`, recalculates scrolling and restores/selects available tabs subject to implementation checks. [src/xrGame/ui/UIPdaWnd.cpp:112-159](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIPdaWnd.cpp#L112-L159)
- `CUIPdaWnd` exposes `SetActiveSubdialog`, `GetActiveSection`, `GetTabControl`, `RebuildTabs`, `SetPdaXml`, etc. [src/xrGame/ui/UIActorMenu_script.cpp:333-345](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIActorMenu_script.cpp#L333-L345)
- `CUITabControl` exposes `AddTab`, `SetTabIcon`, `RecalcScroll`, `SetActiveTab`, `GetButtonById`, etc. [src/xrGame/ui/UITabControl_script.cpp:8-29](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UITabControl_script.cpp#L8-L29)

## CtZ design implication

Prefer **registry-based new War tab** to taking over vanilla Archive/Tutorials, assuming compatibility tests pass. Keep tab content UI separate from registry; supply a stable translated caption and optional icon. The registry's `pda.set_active_subdialog` wrapping is a shared hook and could conflict with other mods implementing their own wrapper. Do not assert compatibility until tested with GAMMA PDA stack.

## Open (source or runtime)

- UI-01 (SOURCE): audit all current tab-switch pathways / stack behavior for last-active-tab restoration and duplicate registry wrappers.
- UI-02 (RUNTIME): validate add/remove/rebuild with other installed PDA addons, localization, long captions, scrollbar and repeated session entry.
- UI-03 (SOURCE): compare actual bundled XML/static default tab setup and game-resolution placement; document differences across PDA skins.
