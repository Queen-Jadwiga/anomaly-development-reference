# INV-010 — Lua XML registration (Part A)

**Status:** Partial resolution. **Date:** 2026-10-09. **Runtime testing:** deferred.

## Finding

Identified the previously missing bridge: [`CScriptXmlInit::script_register`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L337-L384) registers `CScriptXmlInit` with Luabind. Its implementations delegate UI initialization to native `CUIXmlInit`. This **resolves whether a script-facing XML initialization route exists in the pinned source**; it does **not** settle whether native `CUIXmlInit` itself has another export.

## Remaining questions (deliberately retained)

1. Which bootstrap or registration aggregator invokes `CScriptXmlInit::script_register`? Trace full startup route.
2. Is the separate `CUIXmlInit` class registered anywhere else? Requires repository-wide search before negative claim.
3. What is the failure/ownership behavior if a widget initializer receives an absent XML node or null parent? Study implementation and creation contracts.
4. Is `_G.COnXmlRead` called for every requested XML file or only specific parser entry points? Identify call sites.
5. Does the user's installed MT-TEST binary exactly match the release? Runtime/binary verification deferred.
6. Does any later or GAMMA-specific patch change the registration? Unverified.

## Reproduction

Search historical files `src/xrGame/ScriptXMLInit.cpp` and `.h` at pinned commit, then run the `git grep` procedures in `02-lua-api/registration-architecture-part-A.md` on a full checkout.
