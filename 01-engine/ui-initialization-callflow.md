# UI initialization call-flow (source-confirmed subset)

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

```mermaid
flowchart TD
 A[Native UI construction] --> B[CUIXmlInit::InitStatic / InitTextWnd]
 B --> C[CUIXmlInit::InitWindow]
 B --> D[CUIXmlInit::InitText]
 D --> E[CUIXmlInit::InitFont]
 E --> F[UI().Font() font getter]
 F --> G[CGameFont pointer]
 G --> H[CUILines::SetFont]
```

**Scope:** this diagram is the confirmed XML text-initialization slice, **not** an engine startup sequence and **not** proof these methods are Lua-callable.

[Source: pinned `UIXmlInit.cpp`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp). Runtime tests deferred.
