# INV-007 — XML/Lua boundary and font getters

> ADR document set: **v0.1.67**. Research revisions and source/build versions below describe their original scope.

- Version: ADR v0.1.7
- Target: `6a08e0905ce34748ee2904a5e0809f8afd141137`
- Source status: **partial source-confirmed** (native XML and previously extracted font globals); Lua XML wrapper registration **unverified**
- Runtime: **deferred** per project agreement

## Questions addressed
- Does native XML initialization automatically imply Lua availability? **No.** Need an explicit registration path or script wrapper.
- Is `font="small"` the same input as `SetFont("small")`? **No.** Native `SetFont` expects `CGameFont*`.
- Does absence of `script_register` in `UIXmlInit.cpp`/`.h` rule out exposure elsewhere? **No.** Registry-wide source search remains open.

## Sources
- [Native XML implementation](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp)
- [Native declarations](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.h)
- [Prior ADR font names and assertion record](../../03-ui-pda/fonts.md)
- [Prior ADR UI export inventory](../../02-lua-api/api-index.md)

## Deferred tests
- On user's MT-TEST `2026.05.15`: determine available XML helper names via safe reflection/introspection; test valid font getter references in an initialized UI; compare CtZ font crash stack with native assertions.

## Open issue
No verified script-registration location for the XML initializer has yet been established, so do not label any such initializer call as Lua API-confirmed.
