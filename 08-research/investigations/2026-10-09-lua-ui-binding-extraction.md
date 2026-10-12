# Investigation: UI Lua binding extraction

> ADR document set: **v0.1.60**. Research revisions and source/build versions below describe their original scope.

## Source and scope
- Pin: `6a08e0905ce34748ee2904a5e0809f8afd141137`.
- [`UIWindow_script.cpp`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIWindow_script.cpp) — `CUIWindow`, `CUIScrollView`, font globals, UI events.
- [`UIStatic_script.cpp`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIStatic_script.cpp) — `CUIStatic`, `CUITextWnd`, `CUILines`.
- [`UIProgressBar_script.cpp`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIProgressBar_script.cpp) — `CUIProgressBar`.
- [`lua_help_ex.script`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/gamedata/scripts/lua_help_ex.script) — developer-facing supplemental API descriptions.
- [May 15 PR #532](https://github.com/themrdemonized/xray-monolith/pull/532/files) — change evidence for ProgressBar exports and physics shell methods.

## Findings
1. Registration via `module(L)` and Luabind `class_`/`.def` provides identifiable script-visible export names.
2. CUIWindow attaches child with `adopt<2>()`; ownership issues require special caution.
3. Global font getter functions are explicitly bound, not arbitrary font identifiers.
4. Progress bar bindings include 2026.05.15 additions `GetSnapNoDelay`, `SetSnapNoDelay`, `SnapProgressPos`.
5. **Potential source bug:** `SetMiddleColor` and `SetMaxColor` bind to `SetMinColor` (rather than same-name methods). Report as source observation only.
6. `PHShell` May 15 documented additions: `set_linear_vel(vector)`, `set_angular_vel(vector)`; not inventoried within UI CSV.

## Limits
- This is an exported-name inventory. Full C++ parameter and return type verification remains to do.
- Did not run against installed executable.
- No claim of full engine Lua API coverage.
