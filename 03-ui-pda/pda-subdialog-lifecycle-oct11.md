# UI-01 — Dynamic PDA tab and subdialog lifecycle (2026-10-11 source)

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

**Status:** Source-level findings established for stock October 11 engine + bundled registry. **Not a GAMMA runtime or multi-addon compatibility validation.**

## Verified native path

1. `CUIPdaWnd::RebuildExtraTabs()` retains `UITabControl->GetActiveId()`, removes dynamic tabs, calls Lua `pda_dynamic_tabs.build_extra_tabs`, then recalculates scrolling. If the previous id resolves to an existing non-dynamic button, the method ensures its visibility and returns. If the id no longer exists, it chooses the first button id (if any); otherwise it resets and sets the active tab when an id remains. **This routine does not universally invoke `SetActiveSubdialog` after a rebuild.**
   - [`src/xrGame/ui/UIPdaWnd.cpp:127–159`](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIPdaWnd.cpp#L127-L159)
2. Native `TAB_CHANGED` handling calls `SetActiveSubdialog` with the control's active id; `SetActiveSubdialog` detaches and hides the previous dialog, selects built-in dialog(s), then optionally calls Lua `pda.set_active_subdialog(section)`; if it gets a non-null `CUIDialogWndEx`-compatible window it attaches and shows it and updates `m_sActiveSection`, otherwise the section becomes empty.
   - [`src/xrGame/ui/UIPdaWnd.cpp:172–186`](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIPdaWnd.cpp#L172-L186)
   - [`src/xrGame/ui/UIPdaWnd.cpp:308–358`](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIPdaWnd.cpp#L308-L358)
3. `CUIPdaWnd::Show(true)` chooses Tasks if the stored active section is empty, otherwise reselects the stored section using `SetActiveSubdialog`. **This is not proof that a removed dynamic tab restores correctly, since the tab control's visual active ID and stored section are separately manipulated.**
   - [`src/xrGame/ui/UIPdaWnd.cpp:263–282`](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIPdaWnd.cpp#L263-L282)
4. Native Lua-facing PDA bindings expose `SetActiveSubdialog`, `GetActiveSection`, `SetPdaXml`, `GetPdaXml`, `GetTabControl`, `RebuildTabs`.
   - [`src/xrGame/ui/UIActorMenu_script.cpp:333–345`](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIActorMenu_script.cpp#L333-L345)
5. Bundled registry `pda_dynamic_tabs.script` stores entries, adds/removes tabs, rebuilds live tab strip if the game level and PDA UI exist, and **overwrites** `pda.set_active_subdialog` while chaining to the function it saw when loaded. Its UI getters run on selection; registry uses monotonically increasing generated IDs.
   - [`gamedata/scripts/pda_dynamic_tabs.script:46–104`](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/pda_dynamic_tabs.script#L46-L99)

## CtZ implementation implications (recommendations, not runtime claims)

- Prefer `pda_dynamic_tabs.register` and preserve its returned ID. Avoid competing global overrides of `pda.set_active_subdialog`; chaining order with other mods must be examined during integration.
- Do not rely on `RebuildTabs` alone to synchronize the displayed content and visual tab selection. Add an explicit, testable reconciliation path if needed, after verifying the appropriate API.
- Keep the returned dialog object stable across expected uses and respect native attachment/ownership findings from C-01–C-04.
- Design tests for: repeated registration/unregistration; currently active tab removal; previous tab preserved on reopen; two mods wrapping `pda.set_active_subdialog` in different load orders; switching XML/reskin; missing getter window.

## Open questions (remain open)

- **UI-01a (source):** trace `CUITabControl::RemoveDynamicTabs`, `ResetTab`, and active-state side effects to determine whether rebuild transitions can emit `TAB_CHANGED` in every path.
- **UI-01b (source):** analyze potential competing overwrites in GAMMA's installed PDA addons (not contained in the X-Ray source tree).
- **UI-02 (runtime):** tab selection/restore, reordering, reskins and multiple simultaneous PDA mods under the installed GAMMA mod stack.

**Conclusion:** Native PDA switching and bundled registry forwarding are source-backed; seamless cross-mod restoration is **not established**.

## External runtime amendment — 2026-10-12

The October scope above remains an inspected-source scope. Dynamic tabs existed by July 31; September exports support the registry. [Issue #2](https://github.com/Queen-Jadwiga/anomaly-development-reference/issues/2) reports startup/load registration crashing with MAC’s full strip while a later keypress worked. Do not accept the bundled “any time” comment or `level.present()` as complete UI readiness. Keep loading-only, strip-only and combined-interaction explanations open; no general eight-tab incompatibility was established.

A returned Lua window, native parent attachment, dialog-holder registration and HUD render registration are different lifetime edges. [Issue #1](https://github.com/Queen-Jadwiga/anomaly-development-reference/issues/1) concerns shown/HUD windows; it does not directly certify or reject a PDA-attached page. Audit teardown for the actual registration path. [Scoped findings and open investigations](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md).
