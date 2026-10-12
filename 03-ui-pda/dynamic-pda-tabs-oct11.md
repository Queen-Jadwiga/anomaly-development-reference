# October 11 UI survey — native dynamic PDA tabs

> ADR document set: **v0.1.76**. Research revisions and source/build versions below describe their original scope.

**Inspected baseline:** supplied `2026.10.11` source snapshot; the October label is not the feature’s introduction/minimum supported version. **Evidence:** native/bundled source plus separately scoped external runtime observations; no independent ADR game test.

## Feature history and load-time hazard

Dynamic PDA support was introduced upstream on July 19 and shipped in [2026.7.31](https://github.com/themrdemonized/xray-monolith/releases/tag/2026.7.31). September source already has the registry and native interfaces. Version/availability and safe initialization phase are separate questions; inspect the actual installed bindings and script winner. [History and pinned September comparison](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md#feature-history-and-build-scope).

**Reported runtime hazard:** [issue #2](https://github.com/Queen-Jadwiga/anomaly-development-reference/issues/2) records an access violation when `register` ran from `on_game_start` during loading, with GAMMA/MAC’s full eight-tab strip. Later keypress registration worked. The registry’s “any time” comment is not an established safe-load contract: `level.present()` and a non-null menu pointer do not prove readiness to rebuild it. Defer live registration/rebuild to a deliberately verified post-load phase; no fixed delay or named universal callback is certified here. Full-strip versus loading interaction remains open.

## Verified source path

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
