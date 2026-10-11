# UI-01a — Native tab selection, reset, and event propagation

> ADR document set: **v0.1.41**. Research revisions and source/build versions below describe their original scope.

Status: **source research complete for tab-control state transitions**; runtime checks deferred. Source baseline: uploaded `xray-monolith-2026.10.11.zip` (not the installed executable). Line numbers refer to this archive. This record is limited to `CUITabControl` state transitions, dynamic-tab rebuild interaction, and PDA routing. It does not certify addon compatibility.

## Verified source behavior

1. `src/xrGame/ui/UITabControl.cpp:292–300`: `ResetTab()` normalizes button states and sets both `m_sPushedId` and `m_sPrevPushedId` to empty; **it does not call** `OnTabChange` or send `TAB_CHANGED`.
2. `src/xrGame/ui/UITabControl.cpp:232–242`: `SetActiveTab(sNewTab)` returns without action when new ID equals `m_sPushedId`; otherwise assigns it, calls `OnTabChange`, updates previous ID, and calls `EnsureVisible`. This method does not independently confirm that the requested ID identifies an existing tab.
3. `src/xrGame/ui/UITabControl.cpp:219–230`: `OnTabChange` looks up new and previous tab buttons, notifies the previous button if present, and unconditionally dereferences the **new** button to send `TAB_CHANGED`. It forwards `TAB_CHANGED` to the message target only when accelerator mode is enabled. Therefore an invalid ID is a source-visible risk; callers should validate via `GetButtonById` first.
4. `src/xrGame/ui/UITabControl.cpp:151–205`: `SendMessage` accepts button-originated `TAB_CHANGED` only if accelerator mode is enabled; when the pressed ID differs from the previous ID it dispatches `OnTabChange`. Scroll-arrow BUTTON_CLICKED events are handled before that accelerator gate, and thus still scroll with accelerators off.
5. `src/xrGame/ui/UITabControl.cpp:244–258`: keyboard accelerators select tabs only for `WINDOW_KEY_PRESSED` while accelerator mode is enabled. No basis here to claim a generic mouse-input disable.
6. `src/xrGame/ui/UITabControl_scroll.cpp:103–114`: `RemoveDynamicTabs` detaches dynamic buttons and compacts the array of static buttons; it does not issue a tab-change event or itself clear the stored active ID. `src/xrGame/ui/UIPdaWnd.cpp:127–159`: `RebuildExtraTabs` remembers the active ID, removes/rebuilds extras, recalculates scroll, and either keeps the static selection visible or resets and selects an available ID. When no selected ID remains, it falls back to the first tab, if present.
7. `src/xrGame/ui/UIPdaWnd.cpp:174–183` routes forwarded `TAB_CHANGED` from `UITabControl` to `SetActiveSubdialog(GetActiveId())`; `UIPdaWnd.cpp:308–358` detaches/hides the prior dialog and then attaches/shows the resolved dialog. In particular, a rebuild that simply returns for an already-active **static** tab does not itself call `SetActiveSubdialog`.
8. `src/xrGame/ui/UITabControl_script.cpp:8–29` exports `AddTab`, `RecalcScroll`, `GetActiveId`, `SetActiveTab`, `GetButtonById`, `GetEnabled`, and `SetEnabled`, among others. `ResetTab` and `RemoveDynamicTabs` are not registered in this specific class binding; they are invoked natively in the inspected PDA rebuild path. These findings do not rule out another wrapper elsewhere.

## CtZ guidance from this source

- Validate dynamic tab IDs before selection; never rely on `SetActiveTab` to reject an invalid ID.
- Do not assume `ResetTab()` or `RemoveDynamicTabs()` automatically synchronizes the selected PDA subdialog or emits notifications.
- Preserve distinction between **tab-button selection** and **actual active content**. If rebuilding an interface, explicitly reason through both state machines.
- Avoid using accelerator mode as a blanket 'input disabled' mechanism; scroll arrows bypass the gate.

## Open / deliberately excluded

- Runtime: selection, focus, and PDA restoration in the user's actual GAMMA configuration, including third-party PDA wrappers.
- Source follow-up: full provenance of native `SetActiveTab_script` overload/guards and any higher-level Lua wrapper behavior, if relevant to a future implementation.
- Source follow-up: DXML interception boundaries and complete UI export inventory belong to separate UI pass records.

## Source pointers

- `https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UITabControl.cpp`
- `https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UITabControl_scroll.cpp`
- `https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIPdaWnd.cpp`
- `https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UITabControl_script.cpp`

These links are constructed from the uploaded archive tag/path. The exact contents and line references above were inspected **in the uploaded archive**; remote link resolution has not been separately verified here.
