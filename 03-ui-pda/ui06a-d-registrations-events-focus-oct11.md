# UI-06a through UI-06d — Native UI export, dispatch, and focus audit

> ADR document set: **v0.1.42**. Research revisions and source/build versions below describe their original scope.

**Source baseline:** provided `xray-monolith-2026.10.11.zip` extracted source. **Status:** targeted source findings verified; enumerated wider exhaustiveness questions remain open. No runtime verification.

## UI-06a — Export contexts, signatures, and enumeration boundaries

- The native `UIRegistrator::script_register(lua_State*)` calls registrations for `CUIWindow`, `CUIStatic`, `CUIButton`, `CUIProgressBar`, `CUIComboBox`, `CUIEditBox`, `CUITabControl`, `CUIMessageBox`, `CUIListBox`, `CUIDialogWndEx`, `CUIPropertiesBox`, `CUIOptionsManagerScript`, `CUIMapInfo`, `CScriptXmlInit`, `CUIGameCustom`, and `CUIActorMenu`. Evidence: [ui_export_script.cpp:29-46](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_export_script.cpp#L29-L46).
- Registrations can involve composed helper functions and not just single-file `.def` lists. `CUIDialogWndEx::script_register` constructs the `CUIScriptWnd` Luabind class and composes `script_register_ui_window1` and `script_register_ui_window2`. Evidence: [ui/UIScriptWnd_script.cpp:21-48](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIScriptWnd_script.cpp#L21-L48) and [ui/uiscriptwnd_script2.cpp:18-31](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/uiscriptwnd_script2.cpp#L18-L31).
- Exact selected signature: `CUIScriptWnd:Register(CUIWindow*, LPCSTR)`; the native single-argument overload is **not registered through this binding**. `AddCallback` binds `(LPCSTR, s16, functor<void>, luabind::object)`. Evidence: [ui/UIScriptWnd_script.cpp:35-48](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIScriptWnd_script.cpp#L35-L48).
- The `CGameFont` enum `EAligment` with `alLeft`, `alRight`, and `alCenter` is registered through `module(L)` in `ui_export_script.cpp`; enum registrations must not be mistaken for callable methods. Evidence: [ui_export_script.cpp:48-58](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_export_script.cpp#L48-L58).
- Previous 425-name CSV remains a **scoped occurrence index**, not a compiled complete method-signature map. Exact overloads should be read per registration expression. **Open UI-06a-EXH:** inventory every global/module registration and validate all overloaded signatures beyond the scoped index; do not claim exhaustive coverage.

## UI-06b — Event selection, emissions and Lua overrides

- `event_comparer` tests event ID then compares **control pointer if specified**, otherwise sender `WindowName()` against registered `m_control_name`. Evidence: [ui/UIWndCallback.cpp:7-16](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWndCallback.cpp#L7-L16).
- `CUIDialogWndEx::AddCallback` replaces a callback for a duplicate `(name,event)` registration; `SendMessage` picks the **first** match and invokes its stored no-argument functor, otherwise falls back to inherited `SendMessage`. `pData` is not passed to that functor. Evidence: [ui/UIScriptWnd.cpp:27-40](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIScriptWnd.cpp#L27-L40) and [ui/UIScriptWnd.cpp:52-69](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIScriptWnd.cpp#L52-L69).
- The script wrapper forwards virtual `OnKeyboardAction`, `OnMouseAction`, `OnMouseMoveRelative`, `Update`, `Dispatch` to Lua member methods named `OnKeyboard`, `OnMouse`, `OnMouseMoveRelative`, `Update`, `Dispatch`; registered fallback methods invoke corresponding inherited native methods. Evidence: [ui/uiscriptwnd_script.h:5-62](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/uiscriptwnd_script.h#L5-L62) and [ui/uiscriptwnd_script2.cpp:20-30](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/uiscriptwnd_script2.cpp#L20-L30).
- **Open UI-06b-EMIT:** an exhaustive per-widget matrix of which widgets emit which `EUIMessages` has not been proven here. Calling `AddCallback` alone does not guarantee emission.

## UI-06c — Registration reachability and conditionality

- `UIRegistrator::script_register` establishes the **direct UI dispatcher list** in the inspected revision; entry into the engine-wide exporter was established in A-01. `CUIScriptWnd` demonstrates multi-file composed registrations. Evidence: [ui_export_script.cpp:29-46](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_export_script.cpp#L29-L46), [ui/UIScriptWnd_script.cpp:21-48](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIScriptWnd_script.cpp#L21-L48).
- The examined dispatcher list contains no visible preprocessor branch around its individual `script_register` calls. This is **not** proof that all methods are present in every binary, nor proof that no other UI-like exports exist elsewhere (compile options, linked object sets, and separate module registrators still matter).
- **Open UI-06c-BUILD:** verify the actual build target's compile/link inclusion of each registration translation unit and any conditional definitions. This is a static build-system follow-up, not inherently a runtime-only issue.

## UI-06d — Keyboard focus, edit fields, dialog gating

- `CUIWindow::OnKeyboardAction` first offers the action to `m_pKeyboardCapturer`, then visits enabled child windows in reverse order and stops on a handler returning true; `OnKeyboardHold` uses the analogous pattern. Evidence: [ui/UIWindow.cpp:577-627](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow.cpp#L577-L627).
- `SetKeyboardCapture` propagates the capture chain upward, sends `WINDOW_KEYBOARD_CAPTURE_LOST` to an existing capturer, and replaces or clears the capturer pointer. Evidence: [ui/UIWindow.cpp:630-645](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow.cpp#L630-L645).
- `CUICustomEdit` captures keyboard focus on left click/double click, accepts pressed/released keys while focused and emits `EDIT_TEXT_COMMIT` on capture loss or explicit commit. Its escape, tab and focus methods have separate native logic. Evidence: [ui/UICustomEdit.cpp:105-162](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UICustomEdit.cpp#L105-L162) and [ui/UICustomEdit.cpp:300-343](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UICustomEdit.cpp#L300-L342).
- `CUIDialogWnd::OnKeyboardAction` refuses input when `IR_process()` is false; `IR_process()` gates on enabled state, dialog holder pause policy and `Device.Paused()`/`WorkInPause`. Evidence: [ui/UIDialogWnd.cpp:27-53](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIDialogWnd.cpp#L27-L53).
- **CtZ implication:** native edit focus can consume keystrokes, but PDA tab shortcuts and other independent script/global handlers still need inspection; do not promise universal suppression of A/D or other hotkeys by merely focusing a text box.
- **Open UI-06d-MODAL:** a comprehensive modal-dialog stack and input interception audit remains outside these cited focus paths. Runtime tests deferred.

## Evidence discipline and disposition

The four investigation labels have **targeted source conclusions**, but broader exhaustive sub-questions remain explicitly open. This is not a blanket completion certificate for every native UI export or event. Relevant tests for CtZ input handling, callback interoperability, and runtime ownership are deferred until the user can test.
