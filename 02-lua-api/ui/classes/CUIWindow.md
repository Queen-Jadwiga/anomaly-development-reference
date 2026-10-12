# CUIWindow — declaration-backed signatures (ADR v0.1.4)

> ADR document set: **v0.1.67**. Research revisions and source/build versions below describe their original scope.

**Target:** 2026.5.15 source commit `6a08e09`; **status:** C++ declarations + Lua registration confirmed, GAMMA runtime untested.

**Evidence:** [binding registration](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIWindow_script.cpp#L129-L193), [class declarations](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIWindow.h#L104-L230), [attach/detach implementation](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIWindow.cpp#L221-L260).

| Lua call | C++ parameter(s) / result | Notes |
|---|---|---|
| `CUIWindow()` | no arguments → window object | Luabind constructor registered |
| `window:AttachChild(child)` | `CUIWindow*` → `void` | `adopt<2>()` binding policy; ownership transfers from Lua |
| `window:DetachChild(child)` | `CUIWindow*` → `void` | Native detach deletes child **if** auto-delete is set |
| `window:SetAutoDelete(enabled)` | `bool` → `void` | Interacts with detach/destruction; avoid casual toggles |
| `window:IsAutoDelete()` | none → `bool` | State inspection |
| `window:SetWndRect(rect)` | `Frect` by value → `void` | Lua wrapper `SetWndRect_script` |
| `window:SetWndPos(pos)` | `Fvector2` by value → `void` | Lua wrapper `SetWndPos_script` |
| `window:SetWndSize(size)` | `Fvector2` by value → `void` | Lua wrapper `SetWndSize_script` |
| `window:GetWndPos()` | none → `const Fvector2*` | Binding helper returns address of native position; reference lifetime matters |
| `window:GetWidth()` | none → numeric | Width from native base class; precise typedef resolved in that base separately |
| `window:GetHeight()` | none → numeric | Same caveat |
| `window:Enable(enabled)` | `bool` → `void` | Enable window |
| `window:IsEnabled()` | none → `bool` | State inspection |
| `window:Show(visible)` | `bool` → `void` | Also invokes `Enable(visible)` in native implementation |
| `window:IsShown()` | none → `bool` | Visibility |
| `window:SetWindowName(name)` | `LPCSTR` → `void` | String name |
| `window:WindowName()` | none → `LPCSTR` | Lua wrapper rather than native shared_str |
| `window:IsCursorOverWindow()` | none → `bool` | Maps to `CursorOverWindow` |
| `window:FocusReceiveTime()` | none → `u32` | Native time value |
| `window:GetAbsoluteRect(rect)` | `Frect&` output → `void` | **Not** zero-argument value-returning function; caller-supplied rect needed |
| `window:SetPPMode()` / `ResetPPMode()` | no arguments → `void` | Registers or unregisters post-process draw |

**Ownership warning:** `AttachChild` uses Luabind adoption, but native child destruction is also controlled by auto-delete. The precise safe lifecycle for an individual UI pattern still needs a GAMMA test. `DetachChild` must not be assumed to leave a usable Lua reference after an auto-delete child is removed.

**Do not generalize** unregistered native methods like `GetParent()` or `FindChild()` as Lua-accessible from the class declaration alone.
