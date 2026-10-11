# CUIScrollView — declaration-backed signatures

> ADR document set: **v0.1.48**. Research revisions and source/build versions below describe their original scope.

**Source-confirmed, runtime-untested:** [registration in UIWindow_script.cpp](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIWindow_script.cpp#L235-L246), [declarations](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIScrollView.h#L43-L79).

| Lua method | Native declaration | Note |
|---|---|---|
| `CUIScrollView()` | `CUIScrollView()` | Registered default constructor |
| `AddWindow(child,auto_delete)` | `void(CUIWindow*, bool)` | Be explicit about deletion policy |
| `RemoveWindow(child)` | `void(CUIWindow*)` | Check native handling before reusing child |
| `Clear()` | `void()` | Clears the view; child lifetime testing pending |
| `ScrollToBegin()` | `void()` | Scroll navigation |
| `ScrollToEnd()` | `void()` | Scroll navigation |
| `GetMinScrollPos()` | `int()` | Minimum scroll position |
| `GetMaxScrollPos()` | `int()` | Maximum scroll position |
| `GetCurrentScrollPos()` | `int()` | Current scroll position |
| `SetScrollPos(position)` | `void(int)` | Set scroll position |
| `SetFixedScrollBar(value)` | `void(bool)` | Toggle fixed scroll bar |

**Important:** `InitScrollView()` appears in the native header but is **not registered as a Lua method** in this class. Creation from Lua alone is not evidence that the object is fully initialized or safe for UI operations. We must examine XML initialization and runtime behavior before constructing standalone scroll views.
