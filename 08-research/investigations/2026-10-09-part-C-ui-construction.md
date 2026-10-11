# INV-012 — Part C: XML/UI object construction, attachment and deletion

> ADR document set: **v0.1.45**. Research revisions and source/build versions below describe their original scope.

**Baseline:** X-Ray Monolith `2026.5.15` (`6a08e0905ce34748ee2904a5e0809f8afd141137`).  **Evidence:** historical source, not runtime tested. **Date:** 2026-10-09.

## Confirmed creation pipeline

`CScriptXmlInit::InitStatic`, `InitTextWnd`, `InitScrollView`, and `InitProgressBar` allocate native widgets with `xr_new`, call the corresponding `CUIXmlInit` initializer, and pass the result to `_attach_child` before returning the widget pointer. See [ScriptXMLInit.cpp lines 26–36, 169–204](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L26-L36), [widget constructors](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L169-L204), [progress bar](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L313-L319).

`_attach_child(child,parent)` does **nothing** when the parent is null. If non-null it sets `SetAutoDelete(true)` on the child. If the parent is a scroll view it invokes `AddWindow(child,true)`; otherwise it invokes `AttachChild(child)`. See [attachment helper](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L26-L36). The helper's explicit null-parent path means a returned widget can be left unattached; **its final Lua/C++ ownership is not established by this alone.**

## Native parent-child ownership

- `CUIWindow` constructor initializes `m_bAutoDelete(false)`; [UIWindow.cpp lines 100–115](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIWindow.cpp#L100-L115).
- `AttachChild` sets the child's parent and adds it to `m_ChildWndList`, with a check for duplicate attachment; [UIWindow.cpp lines 221–233](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIWindow.cpp#L221-L233).
- `DetachChild` removes the child, nulls its parent, and calls `xr_delete` if its `AutoDelete` flag is true; [UIWindow.cpp lines 235–252](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIWindow.cpp#L235-L252).
- `DetachAll` iterates through `DetachChild`; [UIWindow.cpp lines 254–260](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIWindow.cpp#L254-L260).
- `~CUIWindow` verifies an auto-deleting child isn't still parented, detaches from its parent when needed, and calls `DetachAll` on its own children; [UIWindow.cpp lines 125–139](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIWindow.cpp#L125-L139).

**Practical implication:** a Lua reference to a native child may become invalid after the parent detaches or deletes it. This is a native-source-based risk, not a demonstrated Lua use-after-free in the target game.

## Scroll-view initialization is structurally necessary

`CUIScrollView`'s default constructor initializes `m_pad` and `m_VScrollBar` to null. `InitScrollView()` allocates/attaches the internal pad and scrollbar. `AddWindow` immediately dereferences `m_pad` to attach an item. `Clear` calls `m_pad->DetachAll()`. See [UIScrollView.cpp lines 8–20, 55–112](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIScrollView.cpp#L8-L112).

**Source-derived warning:** calling `AddWindow`/`Clear` on a never-initialized default scroll view risks null-pointer dereference. The `CScriptXmlInit::InitScrollView` path explicitly invokes `CUIXmlInit::InitScrollView` before attachment. Lua `CUIScrollView()` is registered, but the native `InitScrollView()` is not among its inspected Lua registrations. See [UIWindow_script.cpp lines 235–247](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIWindow_script.cpp#L235-L247).

## Lua ownership interface must be separated from native AutoDelete

The Luabind wrapper registers `CUIWindow::AttachChild` with an `adopt<2>()` ownership policy. This is distinct from the native `SetAutoDelete` flag. Both must be audited together when deciding whether Lua or C++ remains responsible for an object's lifetime. [UIWindow_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIWindow_script.cpp).

Do **not** infer that the XML factory's returned pointer has the same policy as a manually constructed child passed to Lua `AttachChild` without checking the registration return policy.

## Open questions carried to Part D and later full-source audit

1. Does `CScriptXmlInit` register return-value ownership policies or only default pointer handling? Review full binding context and Luabind policy.
2. How does an absent/malformed XML node interact with `xr_new` widget creation and assertions? Audit each relevant `CUIXmlInit` call and error handling.
3. What is the exact native behavior for `CUIScrollView::RemoveWindow` versus `Clear`, including whether a retained Lua reference stays safe?
4. Can arbitrary UI children be reparented or used after a parent deletes them? Avoid making such claims without runtime/lifetime analysis.
5. Are parentless factory-created native widgets owned/deleted by Lua, another window, or leaked? Examine pointer converter and registration return-policy semantics.
6. Does the exact GAMMA executable change any of these implementations? Deferred per user request.

## Part D consolidation checkpoint

After Part D, **review every unresolved item from Parts A, B, and C**, deduplicate the register and prioritize tests/source searches. Do not drop partially investigated items.
