# Native/XML-to-Lua registration and widget construction — Part A

> ADR document set: **v0.1.44**. Research revisions and source/build versions below describe their original scope.

```mermaid
flowchart TD
  A[Lua code] --> B[Luabind: CScriptXmlInit]
  B --> C[CScriptXmlInit::InitScrollView / InitTextWnd / InitStatic]
  C --> D[Native CUIXmlInit::Init...]
  D --> E[Native UI widget configuration]
  C --> F[_attach_child]
  F --> G{ScrollView parent?}
  G -->|Yes| H[CUIScrollView::AddWindow]
  G -->|No| I[CUIWindow::AttachChild]
```

**Source:** pinned `src/xrGame/ScriptXMLInit.cpp`, lines 26–36, 136–205, 337–384. Source-backed conceptual call flow. Actual Lua invocation and binary behavior not yet tested. The origin of bootstrap registration is not shown; no global startup sequence is implied by this diagram.
