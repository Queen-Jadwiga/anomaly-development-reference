# UI-06 supplementary audit — registration, emitters, builds, modal routing

> ADR document set: **v0.1.78**. Research revisions and source/build versions below describe their original scope.

**Baseline:** uploaded source `xray-monolith-2026.10.11.zip`. **Version:** ADR 0.1.28. **Status:** four bounded source findings; global completeness remains unproven. **Runtime:** not tested.

## UI-06a-EXH — Registration inventory

- Generated `02-lua-api/ui06-followup-scoped-def-occurrences.csv` by scanning all top-level `src/xrGame/ui/*script*.cpp` files plus `src/xrGame/ui_export_script.cpp` for registration-expression lines. This is reproducible **occurrence-level** coverage of this explicit file set, not an exhaustive mapping of every Lua export in xrGame, signature, overload, global `module`, registration helpers, or preprocessor-reachable code.
- The native dispatcher invokes multiple registrators; composed classes include helpers in distinct translation units. See [ui_export_script.cpp:29–58](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_export_script.cpp#L29-L58), [ui/UIScriptWnd_script.cpp:21–48](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIScriptWnd_script.cpp#L21-L48) and [ui/uiscriptwnd_script2.cpp:18–31](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/uiscriptwnd_script2.cpp#L18-L31).
- **Open:** For truly exhaustive UI globals/overloads, enumerate every `module(L)`/registered free function across the full source tree and resolve each conditional signature manually. Do not describe this CSV as all runtime API methods.

## UI-06b-EMIT — Source-supported event emitters

- Button: `CUIButton` sends `BUTTON_DOWN` on its down path and `BUTTON_CLICKED` via click handling. [ui/UIButton.cpp:45–99](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIButton.cpp#L45-L99).
- List: `CUIListBox` forwards `LIST_ITEM_SELECT` and `LIST_ITEM_CLICKED` from its child-message handling. [ui/UIListBox.cpp:99–118](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIListBox.cpp#L99-L118).
- Combo: `CUIComboBox` forwards `LIST_ITEM_SELECT`. [ui/UIComboBox.cpp:90–106](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIComboBox.cpp#L90-L106).
- Tab: `CUITabControl::OnTabChange` forwards `TAB_CHANGED`. [ui/UITabControl.cpp:218–231](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UITabControl.cpp#L218-L231).
- Edit: `CUICustomEdit` emits `EDIT_TEXT_COMMIT`, `EDIT_TEXT_CANCEL`, and keyboard-capture-lost messages on distinct paths. [ui/UICustomEdit.cpp:103–112](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UICustomEdit.cpp#L103-L112) and [ui/UICustomEdit.cpp:290–334](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UICustomEdit.cpp#L290-L334).
- Generated `02-lua-api/ui06-followup-message-emitters.csv` lists exact **direct SendMessage callsites** for these five implementations. Inherited/indirect emitters, other widgets, and conditions require additional tracing. This is not a claim that every event always occurs.

## UI-06c-BUILD — Translation-unit inclusion

- Both `src/xrGame/xrGame.vcxproj` and `src/xrGame/vs2022/xrGame.vcxproj` include `ui_export_script.cpp`, `ui/UIWindow_script.cpp`, `ui/UIScriptWnd_script.cpp`, and `ui/uiscriptwnd_script2.cpp` as `ClCompile` items (verified from uploaded project XML). This establishes **listed compilation inputs for those two project variants**, not successful compilation, linkage under every configuration, or dynamic reachability in a distributed binary.
- **Open:** a complete per-configuration preprocessor/MSBuild property-sheet/link audit, and any alternate build systems not covered by these two projects.

## UI-06d-MODAL — Native dialog holder and input

- `CDialogHolder::SetMainInputReceiver` maintains `m_input_receivers` as a stack-like list; adding a receiver pushes it and removal can erase an existing entry. [UIDialogHolder.cpp:185–227](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/UIDialogHolder.cpp#L185-L227).
- `IR_UIOnKeyboardPress` chooses `TopInputReceiver()`, respects `IR_process()`, offers mouse/keyboard events to the active dialog, and contains an additional input forwarding path to the current entity under specific conditions. [UIDialogHolder.cpp:280–318](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/UIDialogHolder.cpp#L280-L318).
- Release and hold paths are implemented independently: [UIDialogHolder.cpp:319–377](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/UIDialogHolder.cpp#L319-L377). Dialog capture inside a window is handled separately by [ui/UIWindow.cpp:577–645](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow.cpp#L577-L645).
- **CtZ concern:** UI focus is not a universal suppression contract for independent addon hotkeys. Audit the specific PDA input hooks and GAMMA overrides when those scripts are available.
- **Open:** exhaustive global input handling across all game modes, external addon script callbacks, and runtime behavior under nested dialogs.

## Evidence boundary / handoff

This closes the **targeted supplementary source pass** for the identified UI-06 questions without claiming an exhaustive engine-wide audit. Record remaining subquestions as **source-open** (not runtime-only); runtime validation stays deferred. Next UI topic: typography, rendering, resolution and texture contracts.
