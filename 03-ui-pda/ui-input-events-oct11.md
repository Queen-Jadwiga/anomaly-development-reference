# October 11 UI survey — input and event routes

> ADR document set: **v0.1.47**. Research revisions and source/build versions below describe their original scope.

**Scope:** source-identified routes; not a comprehensive guarantee about interception priority in every input mode.

## Verified

- `CLevel::IR_OnKeyboardPress` checks UI input paths and gameplay input; the PDA has special-case handling in level input. [src/xrGame/Level_input.cpp:160-295](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/Level_input.cpp#L160-L295).
- `CUIPdaWnd::SendMessage` reacts to `TAB_CHANGED` by switching the active subdialog; it forwards other messages to the active dialog when appropriate. [src/xrGame/ui/UIPdaWnd.cpp:174-200](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIPdaWnd.cpp#L174-L200).
- `CUIPdaWnd` has native mouse and keyboard action implementations. [src/xrGame/ui/UIPdaWnd.cpp:203-230](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIPdaWnd.cpp#L203-L230); [src/xrGame/ui/UIPdaWnd.cpp:511-535](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIPdaWnd.cpp#L511-L535).
- `CUITabControl::SendMessage` processes scroll arrows and tab-change notifications; handling depends on its accelerator mode. [src/xrGame/ui/UITabControl.cpp:151-194](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UITabControl.cpp#L151-L194).

## CtZ design implication

Do not bind generic movement/navigation keys (A/D etc.) without accounting for text fields and focused controls. Route tab interactions through supported UI callbacks where possible; retain explicit state for search field focus and previous PDA subdialog. C-01 to C-04 lifetime findings remain applicable to event targets.

## Open

- UI-06 (SOURCE): exact Lua-facing widget callbacks and message routing for search/edit/scroll focus, with binding signatures.
- UI-07 (RUNTIME): search text capture versus gameplay keybinds, UI focus reentry, PDA close/reopen/scroll restoration.
