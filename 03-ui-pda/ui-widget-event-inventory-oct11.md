# UI-06 — October 11 Lua widget and event binding inventory

> ADR document set: **v0.1.64**. Research revisions and source/build versions below describe their original scope.

**Status:** Source-catalogued, runtime validation deferred. This is a lexical inventory of the scoped UI registration sources, *not* proof that all names are callable in every context.

**Scope:** 16 C++ registration-related source files in `src/xrGame/ui`, plus `ui_export_script.cpp`, `ScriptXMLInit.cpp` and `UIGameCustom_script.cpp`. **Entries:** 425 extracted named `.def` occurrences.

The accompanying CSV preserves one row per binding occurrence and an exact source line. Bindings may be conditional, overloaded, registered under namespaces, or require a constructor/valid native pointer. Names in `[module / global candidate]` require surrounding `module(L)` inspection before using them.

## Source binding entry points

- `UIRegistrator::script_register`: [ui_export_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_export_script.cpp)
 - `CUIWindow::script_register`: [UIWindow_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow_script.cpp)
 - `CScriptXmlInit::script_register`: [ScriptXMLInit.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ScriptXMLInit.cpp)

## Class-level exported method names

### `CDialogHolder` — 2 named bindings

`AddDialogToRender`, `RemoveDialogToRender`

Source: [src/xrGame/ui/UIWindow_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow_script.cpp) (individual line references in CSV).

### `CMainMenu` — 10 named bindings

`CancelDownload`, `GetAccountMngr`, `GetCDKey`, `GetDemoInfo`, `GetGSVer`, `GetLoginMngr`, `GetPatchProgress`, `GetPlayerName`, `GetProfileStore`, `ValidateCDKey`

Source: [src/xrGame/ui_export_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_export_script.cpp) (individual line references in CSV).

### `CScriptXmlInit` — 37 named bindings

`GetNodesNum`, `Init3tButton`, `InitAnimStatic`, `InitCDkey`, `InitCheck`, `InitComboBox`, `InitEditBox`, `InitFrame`, `InitFrameLine`, `InitHint`, `InitKeyBinding`, `InitListBox`, `InitMMShniaga`, `InitMPPlayerName`, `InitMapInfo`, `InitMapList`, `InitProgressBar`, `InitScrollView`, `InitServerList`, `InitSleepStatic`, `InitSpinFlt`, `InitSpinNum`, `InitSpinText`, `InitStatic`, `InitTab`, `InitTextWnd`, `InitTrackBar`, `InitWindow`, `NavigateToNode`, `NavigateToNode_ByAttribute`, `NavigateToNode_ByPath`, `NavigateToRoot`, `NodeExist`, `ParseDirFile`, `ParseFile`, `ReadAttribute`, `ReadValue`

Source: [src/xrGame/ScriptXMLInit.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ScriptXMLInit.cpp) (individual line references in CSV).

### `CServerList` — 9 named bindings

`ConnectToSelected`, `NetRadioChanged`, `RefreshList`, `RefreshQuick`, `SetConnectionErrCb`, `SetFilters`, `SetPlayerName`, `SetSortFunc`, `ShowServerInfo`

Source: [src/xrGame/ui/UIListBox_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIListBox_script.cpp) (individual line references in CSV).

### `CUIActorMenu` — 9 named bindings

`HideDialog`, `IsShown`, `ShowDialog`, `ToBelt`, `ToSlot`, `get_drag_item`, `highlight_for_each_in_slot`, `highlight_section_in_slot`, `refresh_current_cell_item`

Source: [src/xrGame/ui/UIActorMenu_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIActorMenu_script.cpp) (individual line references in CSV).

### `CUICheckButton` — 3 named bindings

`GetCheck`, `SetCheck`, `SetDependControl`

Source: [src/xrGame/ui/UIButton_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIButton_script.cpp) (individual line references in CSV).

### `CUIComboBox` — 13 named bindings

`AddItem`, `ClearList`, `CurrentID`, `GetCurrentIdx`, `GetText`, `GetTextOf`, `SetCurrentIdx`, `SetCurrentOptValue`, `SetListLength`, `SetText`, `SetVertScroll`, `disable_id`, `enable_id`

Source: [src/xrGame/ui/UIComboBox_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIComboBox_script.cpp) (individual line references in CSV).

### `CUICustomEdit` — 4 named bindings

`CaptureFocus`, `GetText`, `SetNextFocusCapturer`, `SetText`

Source: [src/xrGame/ui/UIEditBox_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIEditBox_script.cpp) (individual line references in CSV).

### `CUICustomSpin` — 1 named bindings

`GetText`

Source: [src/xrGame/ui/UIButton_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIButton_script.cpp) (individual line references in CSV).

### `CUIDialogWnd` — 7 named bindings

`AllowCenterCursor`, `AllowCursor`, `AllowMovement`, `AllowWorkInPause`, `GetHolder`, `HideDialog`, `ShowDialog`

Source: [src/xrGame/ui/UIWindow_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow_script.cpp) (individual line references in CSV).

### `CUIEditBox` — 1 named bindings

`InitTexture`

Source: [src/xrGame/ui/UIEditBox_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIEditBox_script.cpp) (individual line references in CSV).

### `CUIFrameLineWnd` — 3 named bindings

`SetColor`, `SetHeight`, `SetWidth`

Source: [src/xrGame/ui/UIWindow_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow_script.cpp) (individual line references in CSV).

### `CUIFrameWindow` — 3 named bindings

`SetColor`, `SetHeight`, `SetWidth`

Source: [src/xrGame/ui/UIWindow_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow_script.cpp) (individual line references in CSV).

### `CUIGameCustom` — 14 named bindings

`AddCustomStatic`, `AddDialogToRender`, `CurrentItemAtCell`, `GetCustomStatic`, `GetWindow`, `HideActorMenu`, `HidePdaMenu`, `RemoveCustomStatic`, `RemoveDialogToRender`, `UpdateActorMenu`, `enable_fake_indicators`, `hide_messages`, `show_messages`, `update_fake_indicators`

Source: [src/xrGame/UIGameCustom_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/UIGameCustom_script.cpp) (individual line references in CSV).

### `CUILines` — 6 named bindings

`GetText`, `SetElipsis`, `SetFont`, `SetText`, `SetTextColor`, `SetTextST`

Source: [src/xrGame/ui/UIStatic_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIStatic_script.cpp) (individual line references in CSV).

### `CUIListBox` — 13 named bindings

`AddExistingItem`, `AddTextItem`, `GetItem`, `GetItemByIndex`, `GetItemHeight`, `GetSelectedIndex`, `GetSelectedItem`, `GetSize`, `RemoveAll`, `RemoveItem`, `SetItemHeight`, `SetSelectedIndex`, `ShowSelectedItem`

Source: [src/xrGame/ui/UIListBox_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIListBox_script.cpp) (individual line references in CSV).

### `CUIListBoxItem` — 6 named bindings

`AddIconField`, `AddTextField`, `GetTAG`, `GetTextItem`, `SetTAG`, `SetTextColor`

Source: [src/xrGame/ui/UIListBox_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIListBox_script.cpp) (individual line references in CSV).

### `CUIMMShniaga` — 3 named bindings

`SetPage`, `SetVisibleMagnifier`, `ShowPage`

Source: [src/xrGame/ui/UIWindow_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow_script.cpp) (individual line references in CSV).

### `CUIMainIngameWnd` — 1 named bindings

`GetQuickSlotIcons`

Source: [src/xrGame/ui/UIActorMenu_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIActorMenu_script.cpp) (individual line references in CSV).

### `CUIMapInfo` — 2 named bindings

`Init`, `InitMap`

Source: [src/xrGame/ui/UIMapInfo_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIMapInfo_script.cpp) (individual line references in CSV).

### `CUIMapList` — 13 named bindings

`ClearList`, `GetCommandLine`, `GetCurGameType`, `IsEmpty`, `LoadMapList`, `OnModeChange`, `SaveMapList`, `SetMapInfo`, `SetMapPic`, `SetModeSelector`, `SetServerParams`, `SetWeatherSelector`, `StartDedicatedServer`

Source: [src/xrGame/ui/UIListBox_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIListBox_script.cpp) (individual line references in CSV).

### `CUIMessageBox` — 4 named bindings

`GetHost`, `GetPassword`, `InitMessageBox`, `SetText`

Source: [src/xrGame/ui/UIMessageBox_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIMessageBox_script.cpp) (individual line references in CSV).

### `CUIMessageBoxEx` — 4 named bindings

`GetHost`, `GetPassword`, `InitMessageBox`, `SetText`

Source: [src/xrGame/ui/UIMessageBox_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIMessageBox_script.cpp) (individual line references in CSV).

### `CUIMiniMapWidget` — 34 named bindings

`clear_pointer_target`, `clear_pointer_texture`, `clear_pointer_types`, `clear_spot_textures`, `clear_spot_type_filter`, `has_map`, `init`, `local_of`, `map_texture`, `pointer_count`, `set_active_point`, `set_global_texture`, `set_global_visible`, `set_heading`, `set_map_texture`, `set_pointer_scale`, `set_pointer_target`, `set_pointer_texture`, `set_pointer_type`, `set_pointers_visible`, `set_rotate`, `set_spot_color`, `set_spot_height_textures`, `set_spot_scale`, `set_spot_shader`, `set_spot_texture`, `set_spot_type_visible`, `set_texture_color`, `set_update_interval`, `set_zoom_span`, `spot_at`, `spot_count`

Source: [src/xrGame/ui/UIActorMenu_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIActorMenu_script.cpp) (individual line references in CSV).

### `CUIPdaWnd` — 11 named bindings

`GetActiveDialog`, `GetActiveSection`, `GetPdaXml`, `GetTabControl`, `HideDialog`, `IsShown`, `RebuildTabs`, `SetActiveDialog`, `SetActiveSubdialog`, `SetPdaXml`, `ShowDialog`

Source: [src/xrGame/ui/UIActorMenu_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIActorMenu_script.cpp) (individual line references in CSV).

### `CUIProgressBar` — 15 named bindings

`GetProgressPos`, `GetProgressStatic`, `GetRange_max`, `GetRange_min`, `GetSnapNoDelay`, `SetColor`, `SetMaxColor`, `SetMiddleColor`, `SetMinColor`, `SetProgressPos`, `SetRange`, `SetSnapNoDelay`, `ShowBackground`, `SnapProgressPos`, `UseColor`

Source: [src/xrGame/ui/UIProgressBar_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIProgressBar_script.cpp) (individual line references in CSV).

### `CUIPropertiesBox` — 13 named bindings

`AddHeader`, `AddItem`, `AddSubmenu`, `AutoUpdateSize`, `GetSelectedItem`, `Hide`, `InitPropertiesBox`, `RemoveAll`, `RemoveItem`, `Show`, `ShowAt`

Source: [src/xrGame/ui/UIPropertiesBox_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIPropertiesBox_script.cpp) (individual line references in CSV).

### `CUIScrollView` — 10 named bindings

`AddWindow`, `Clear`, `GetCurrentScrollPos`, `GetMaxScrollPos`, `GetMinScrollPos`, `RemoveWindow`, `ScrollToBegin`, `ScrollToEnd`, `SetFixedScrollBar`, `SetScrollPos`

Source: [src/xrGame/ui/UIWindow_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow_script.cpp) (individual line references in CSV).

### `CUIStatic` — 24 named bindings

`AdjustHeightToText`, `AdjustWidthToText`, `EnableHeading`, `GetConstHeading`, `GetCoverTexture`, `GetHeading`, `GetStretchTexture`, `GetTextureColor`, `GetTextureRect`, `InitTexture`, `InitTextureEx`, `RemoveColorAnimation`, `ResetColorAnimation`, `ResetHeadingPivot`, `SetColorAnimation`, `SetConstHeading`, `SetCoverTexture`, `SetHeading`, `SetHeadingPivot`, `SetLineTo`, `SetStretchTexture`, `SetTextureColor`, `SetTextureRect`, `TextControl`

Source: [src/xrGame/ui/UIStatic_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIStatic_script.cpp) (individual line references in CSV).

### `CUITabControl` — 12 named bindings

`AddItem`, `AddTab`, `GetActiveId`, `GetButtonById`, `GetEnabled`, `GetTabsCount`, `RecalcScroll`, `RemoveAll`, `SetActiveTab`, `SetEnabled`, `SetTabIcon`

Source: [src/xrGame/ui/UITabControl_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UITabControl_script.cpp) (individual line references in CSV).

### `CUITextWnd` — 14 named bindings

`AdjustHeightToText`, `AdjustWidthToText`, `GetFont`, `GetText`, `GetTextColor`, `SetEllipsis`, `SetFont`, `SetText`, `SetTextAlignment`, `SetTextColor`, `SetTextComplexMode`, `SetTextOffset`, `SetTextST`, `SetVTextAlignment`

Source: [src/xrGame/ui/UIStatic_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIStatic_script.cpp) (individual line references in CSV).

### `CUITrackBar` — 12 named bindings

`GetCheck`, `GetFValue`, `GetIValue`, `GetInvert`, `SetCheck`, `SetCurrentValue`, `SetFValue`, `SetIValue`, `SetInvert`, `SetOptFBounds`, `SetOptIBounds`, `SetStep`

Source: [src/xrGame/ui/UIButton_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIButton_script.cpp) (individual line references in CSV).

### `CUIWindow` — 70 named bindings

`AttachChild`, `AttachChildKeepOwner`, `DetachChild`, `Enable`, `EnableClip`, `FindChild`, `FocusReceiveTime`, `GetAbsoluteRect`, `GetHeight`, `GetHideLock`, `GetWidth`, `GetWndPos`, `IsAutoDelete`, `IsClipEnabled`, `IsCursorOverWindow`, `IsEnabled`, `IsMouseCapturer`, `IsShown`, `ResetClipRect`, `ResetPPMode`, `SetAutoDelete`, `SetClipRect`, `SetHideLock`, `SetMouseCapture`, `SetPPMode`, `SetWindowName`, `SetWndPos`, `SetWndRect`, `SetWndSize`, `Show`, `WindowName`, `cast_3tButton`, `cast_ActorMenu`, `cast_Button`, `cast_CheckButton`, `cast_ComboBox`, `cast_CustomEdit`, `cast_CustomSpin`, `cast_DialogWnd`, `cast_EditBox`, `cast_FrameLineWnd`, `cast_FrameWindow`, `cast_Hint`, `cast_HudStatesWnd`, `cast_ListBox`, `cast_ListBoxItem`, `cast_ListBoxItemMsgChain`, `cast_MMShniaga`, `cast_MainIngameWnd`, `cast_MapInfo`, `cast_MapList`, `cast_MessageBox`, `cast_MessageBoxEx`, `cast_MessagesWindow`, `cast_MotionIcon`, `cast_PdaWnd`, `cast_ProgressBar`, `cast_PropertiesBox`, `cast_ScriptWnd`, `cast_ScrollView`, `cast_ServerList`, `cast_SleepStatic`, `cast_SpinFlt`, `cast_SpinNum`, `cast_SpinText`, `cast_Static`, `cast_TabButton`, `cast_TabControl`, `cast_TextWnd`, `cast_TrackBar`

Source: [src/xrGame/ui/UIWindow_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow_script.cpp) (individual line references in CSV).

### `CUIZoneMap` — 2 named bindings

`Background`, `MapFrame`

Source: [src/xrGame/ui/UIActorMenu_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIActorMenu_script.cpp) (individual line references in CSV).

### `Patch_Dawnload_Progress` — 4 named bindings

`GetFlieName`, `GetInProgress`, `GetProgress`, `GetStatus`

Source: [src/xrGame/ui_export_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_export_script.cpp) (individual line references in CSV).

### `StaticDrawableWrapper` — 1 named bindings

`wnd`

Source: [src/xrGame/UIGameCustom_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/UIGameCustom_script.cpp) (individual line references in CSV).

### `UIHint` — 4 named bindings

`GetHintText`, `SetHeight`, `SetHintText`, `SetWidth`

Source: [src/xrGame/ui/UIWindow_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow_script.cpp) (individual line references in CSV).

### `connect_error_cb` — 2 named bindings

`bind`, `clear`

Source: [src/xrGame/ui/UIListBox_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIListBox_script.cpp) (individual line references in CSV).

## Modules, callbacks, and events: interpretation

A `.def` export is a callable method binding, **not** proof that a matching UI message is delivered to every window. UI message identifiers, event forwarding, and Lua override hooks require reading `UIScriptWnd`, `UIScriptWnd_script`, `uiscriptwnd_script2`, and `UIWindow` native dispatch paths.

For `CUIWindow::AttachChild`, `adopt<2>()` remains distinct from native AutoDelete (C-03). `CUIScrollView::AddWindow` lacks that explicit adopt policy; see C-02/C-03.

## Verified Lua dialog callback dispatch (targeted source trace)

- `CUIDialogWndEx::Register(child, name)` sets the child window name and message target (`UIScriptWnd.cpp:15–24`). The one-argument native overload exists but is **not** among the `CUIScriptWnd` Lua bindings in `UIScriptWnd_script.cpp:35–47`.
- `CUIDialogWndEx::AddCallback(control_id, evt, functor, object)` replaces an existing callback for the same control name and event ID, otherwise appends a callback (`UIScriptWnd.cpp:52–69`). This *four-argument form* is the one explicitly registered as `AddCallback` in `UIScriptWnd_script.cpp:45–47`.
- `SendMessage(sender, msg, data)` finds the **first matching** callback and invokes its Lua functor without forwarding `data`; if none matches, it delegates to the inherited message handler (`UIScriptWnd.cpp:27–40`). The precise matching semantics are in `event_comparer` and deserve a targeted follow-up.
- The registered `CUIScriptWnd` wrapper exposes `OnKeyboard`, `OnMouse`, `OnMouseMoveRelative`, `Update`, and `Dispatch` through `uiscriptwnd_script2.cpp:22–30`, with wrapper/static fallbacks. Their actual override semantics must be read alongside `uiscriptwnd_script.h` before promising behavior.
- This establishes a callback path, **not** a guarantee that every widget automatically emits all event codes or that every focus state forwards keyboard events.

## Open source questions

- UI-06a: Parse registration contexts precisely (especially top-level `module(L)` exports and enum/event constants), overload signatures, and registration coverage outside `_script.cpp` files.
- UI-06b: Partly established (register, callback replacement, dispatch). Still trace `event_comparer`, source of `EUIMessages` emissions, and wrapper override semantics.
- UI-06c: Check whether binding classes are conditionally compiled and whether all classes in the list are invoked by `UIRegistrator`, versus separately registered.
- UI-06d: Source-audit keyboard capture, editable text focus, and modal dialogs before prescribing War PDA behavior.
- UI-07: Verify widget focus, callbacks and interactions in actual GAMMA runtime (deferred).

## CtZ usage constraint

Use the class table to locate candidate native functionality; verify method signature, instance construction, ownership, and routing in the source before adopting it in production. This inventory is an index for follow-up, not a blanket compatibility guarantee.
