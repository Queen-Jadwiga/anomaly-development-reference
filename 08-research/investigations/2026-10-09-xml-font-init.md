# INV-006 — XML font and scrollview native initialization

**Date:** 2026-10-09  
**Source pin:** `6a08e0905ce34748ee2904a5e0809f8afd141137`  
**Status:** native source-confirmed; GAMMA runtime pending

## Direct observations

1. `CUIXmlInit::InitFont` resolves 11 explicit XML font aliases; unknown names assert. [https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L688-L750](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L688-L750)
2. `CUIXmlInit::InitText` asserts a valid font pointer for every present text node. [https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L277-L325](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L277-L325)
3. `CUIXmlInit::InitScrollView` invokes native `InitScrollView()` after setting XML-specified geometry and profile. [https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L1097-L1141](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L1097-L1141)
4. `InitAutoStaticGroup` gives created child statics native auto-delete ownership. [https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L619-L646](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L619-L646)

## Hypotheses (NOT conclusions)

- CtZ crash may be caused by an unsupported XML font token, absent font attribute on an active text node, or an invalid font pointer from another initialization path. Exact cause is **unknown**.
- Lua-created scrollviews may require construction via a supported XML pathway; installed binding surface and behavior remain to be tested.

## Next work

- Trace `CUIXmlInit` script bindings and UI font manager setup.
- Cross-check effective CtZ XML and earlier crash log assertions when available.
- Add static XML checks that validate documented font tokens, preserving a project-configurable exception list for custom overrides.
