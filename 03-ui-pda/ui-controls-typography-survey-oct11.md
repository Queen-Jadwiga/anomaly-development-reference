# October 11 UI survey — Lua controls, fonts, visual resources

> ADR document set: **v0.1.78**. Research revisions and source/build versions below describe their original scope.

**Scope:** index of confirmed export locations and targeted implications. NOT a complete enumeration of all UI exports.

## Verified

- `CUIWindow` Luabind exports `AttachChild` with `adopt<2>()`, `AttachChildKeepOwner` without it, `DetachChild`, `FindChild`, and `SetAutoDelete`; ownership implications addressed in C-01 to C-04. [src/xrGame/ui/UIWindow_script.cpp:202-213](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow_script.cpp#L202-L213).
- The same registration module publishes named getter functions such as `GetFontSmall`, `GetFontMedium`, `GetFontDI`, and other native font presets. This proves getters exist, not that they are safe at arbitrary startup phases. [src/xrGame/ui/UIWindow_script.cpp:188-197](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UIWindow_script.cpp#L188-L197).
- Lua bindings for `CUITabControl` provide programmatic creation and scrolling operations for tab controls; dynamic tabs have an engine-supported registry. [src/xrGame/ui/UITabControl_script.cpp:8-29](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/UITabControl_script.cpp#L8-L29).
- Font manager and scroll ownership have their own source records B-01/B-02 and C-01..C-04; those remain the ownership and lifetime authorities, not this survey.

## CtZ design implication

Use native font getters rather than allocating unverified new engine font objects; avoid relying on cached pointers across lifetime boundaries until stress-tested. Native FindChild is available, but returned pointers must follow the parent-lifetime restrictions already documented.

## Open

- UI-08 (SOURCE): enumerate ALL exported UI classes, methods, overloads, and dynamic-cast routes; verify XML widget styles, texture atlas selection, DPI/high-resolution logic, widget resize contracts.
- UI-09 (RUNTIME): test font resources, display scaling, XML textures, and reset/open-close behavior at player resolutions.
