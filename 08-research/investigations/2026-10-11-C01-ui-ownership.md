# C-01 — Native UI creation and parent-child ownership contract

> ADR document set: **v0.1.56**. Research revisions and source/build versions below describe their original scope.

**Source:** user-provided `xray-monolith-2026.10.11.zip`. **Status:** source research complete; no runtime claims. **Question:** Which ownership and attachment behaviors are actually implemented when native UI controls are constructed by `CScriptXmlInit`, and which are exposed to Lua?

## Verified native paths

1. **Factory helper:** `_attach_child(child,parent)` returns immediately when `parent` is null; otherwise it sets `child->SetAutoDelete(true)` and uses `CUIScrollView::AddWindow(child,true)` for scroll parents or `CUIWindow::AttachChild(child)` for other parents. [`ScriptXMLInit.cpp:28–38`](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ScriptXMLInit.cpp#L28-L38).
2. **Creation examples:** `CScriptXmlInit::InitStatic`, `InitTextWnd`, `InitScrollView`, `InitListBox` allocate controls with `xr_new`, perform type-specific `CUIXmlInit::Init*` initialization, call `_attach_child`, and return pointers. [`ScriptXMLInit.cpp:180–224`](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ScriptXMLInit.cpp#L180-L224). This statement covers the inspected examples, not every factory method.
3. **Parent list:** `CUIWindow::AttachChild` verifies child, checks direct duplicate attachments and logs/returns if already attached, calls `SetParent(this)`, and appends to `m_ChildWndList`. It does **not** itself set `AutoDelete`. [`UIWindow.cpp:285–298`](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow.cpp#L285-L298).
4. **Removal/destruction:** `DetachChild` removes the child from the list, clears its parent and deletes it only if `IsAutoDelete()` is true. `DetachAll` repeats on all children; `CUIWindow::~CUIWindow` invokes `DetachAll`. A child destructor also detaches itself when it has a parent but is *not* autodelete. [`UIWindow.cpp:183–198`](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow.cpp#L183-L198), [`UIWindow.cpp:300–325`](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow.cpp#L300-L325).
5. **Lua bindings:** `CUIWindow` exports a constructor, `AttachChild` **with `luabind::adopt<2>()`**, `AttachChildKeepOwner` without that policy, `DetachChild`, `SetAutoDelete`, and `IsAutoDelete`. [`UIWindow_script.cpp:202–209`](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow_script.cpp#L202-L209). Distinguish Luabind *userdata ownership policy* from native `m_bAutoDelete`: these are separate mechanisms.

## Implications, with strict limits

- For the inspected `CScriptXmlInit` factory methods, a **non-null parent** leads to native auto-delete marking and attachment (special handling for scroll view); **null parent** leaves the newly constructed control without this helper's ownership transfer. The code alone does not prove who will later delete an unattached object.
- Native parent deletion deletes **auto-delete children** during `DetachAll`; attached **non-auto-delete** children are detached but not deleted by that path. Explicitly retaining references in Lua is **not** evidence of lifetime safety after native deletion.
- `AttachChild` (Lua) includes `adopt<2>()`, unlike `AttachChildKeepOwner`; invoking these interchangeably can change ownership behavior on the Lua side. Do **not** infer how garbage collection interacts with deletion solely from the method names; investigate Luabind runtime semantics separately if needed.
- Neither this record nor the source code establishes that all widget types can safely be reparented, detached, or retained after closing PDA tabs. XML factory behavior for all controls, scroll ownership details, and Lua GC lifetime are **separate questions**.

## CtZ application and deferred validation

Avoid duplicate attachments, preserve a single consistent lifetime owner, and do not retain Lua references after native UI destruction. Before changing existing PDA window assembly, test parented vs unparented controls, scrollview additions, tab closure/reopening, and Lua references surviving window destruction in an isolated runtime build. Those are **pending runtime tests**, not verified outcomes.

**Disposition:** C-01 source research complete. Next follow-up can narrow to C-02 (scroll-view ownership or userdata lifetime), without reopening the parent-child contract established here.
