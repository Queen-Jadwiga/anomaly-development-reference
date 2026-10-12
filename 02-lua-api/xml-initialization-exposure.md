# Lua-facing XML initialization: verified boundary and open bindings (ADR v0.1.7)

> ADR document set: **v0.1.56**. Research revisions and source/build versions below describe their original scope.

**Engine source target:** X-Ray Monolith `2026.5.15` / `6a08e0905ce34748ee2904a5e0809f8afd141137`. **Runtime:** deferred.  
**Important:** This is a *registration investigation*, not an inventory of Lua-exposed `CUIXmlInit` methods.

## Source-confirmed native layer

`CUIXmlInit` is a native initialization facility; methods already documented in [native XML layouts](../03-ui-pda/xml-layouts.md) include `InitWindow`, `InitStatic`, `InitTextWnd`, `InitText`, and `InitScrollView`.

- [`UIXmlInit.h`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.h) — native declarations.
- [`UIXmlInit.cpp`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp) — implementation and its assertions.
- Native scroll initialization uses `CUIXmlInit::InitScrollView` and calls `CUIScrollView::InitScrollView` internally; this does **not** independently prove a direct Lua call to either initializer.

## Lua registration state

The inspected native `UIXmlInit.h` and `UIXmlInit.cpp` do not include an identifiable `script_register` definition for `CUIXmlInit`. **This is not proof that the class is absent from Lua.** A binding may be registered elsewhere or presented through a differently named helper / XML wrapper.

| Candidate interface | Native evidence | Lua exposure in pinned build | Runtime |
|---|---|---|---|
| `CUIXmlInit::InitStatic` | Confirmed native | **Not established** | Deferred |
| `CUIXmlInit::InitTextWnd` | Confirmed native | **Not established** | Deferred |
| `CUIXmlInit::InitScrollView` | Confirmed native | **Not established** | Deferred |
| Script-level `CUIXml` / `CUIXmlInit` constructor | Not determined in this pass | **Not established** | Deferred |
| DXML/other XML helper functions | Not investigated in matching registration sites | **Not established** | Deferred |

**Do not generate executable Lua examples invoking these methods** until the appropriate `class_`, `module`, or equivalent registration is located in the pinned source.

## Next source investigation

1. Search the entire pinned revision (not merely `ui/UIXmlInit.*`) for `CUIXmlInit`, `CUIXml`, `InitScrollView`, and Luabind `class_` registrations.
2. Inspect the exports' argument policy and object lifetime, if located.
3. Trace which script XML wrappers GAMMA actually deploys, separately from engine registrations.
4. Record one source-accurate call signature only after registration and overloads are matched.

**Evidence classification:** native methods source-confirmed; their Lua exposure **unverified**; all runtime behavior **untested**.
