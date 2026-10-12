# UI-04b — DXML callback failure and registration behavior (2026-10-11)

> ADR document set: **v0.1.55**. Research revisions and source/build versions below describe their original scope.

**Status:** Source research complete for inspected October 11 source; runtime validation deferred. **Scope:** native XML callback boundary, DXML Lua parser wrapper, module registration and callback ordering. This document does not assert that installed GAMMA uses the same effective scripts.

## Native boundary and errors

1. [`src/xrXMLParser/xrXMLParser.cpp`, lines 118–145](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrXMLParser/xrXMLParser.cpp#L118-L145): `CXml::Load` parses expanded XML, calls `R_ASSERT2` on parse error, then calls `XMLLuaCallback`. No locally visible exception handler protects the callback invocation.
2. [`src/xrGame/ScriptXMLInit.cpp`, lines 55–65](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ScriptXMLInit.cpp#L55-L65): native `XMLLuaCallback` returns early on null/empty input; obtains `_G.COnXmlRead` via script-engine `functor`; invokes it if present and passes its result to `m_xml.LoadFromString`. No explicit `try/catch`, fallback on Lua exception, or null-result guard is present **within this function**. Behavior of errors crossing Luabind and outer engine error handlers is NOT established by these local snippets.
3. [`src/xrXMLParser/xrXMLParser.cpp`, lines 147–159](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrXMLParser/xrXMLParser.cpp#L147-L159): `LoadFromString` asserts on malformed transformed XML. A callback producing invalid output therefore enters a native parse failure route; we do not assert a recoverable fallback.

## Lua pipeline, parse failures and callbacks

4. [`gamedata/scripts/_g_patches.script`, lines 222–230](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/_g_patches.script#L222-L230): `try(func, ...)` uses `pcall`, logs an error and returns `false` on exception. In [`dxml_core.script`, lines 964–1014](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L964-L1014), `parser.simple_dom` and `xml_object` construction run through `try`; failures return original XML.
5. The same DXML function calls `SendScriptCallback("on_xml_read", ...)` and later serializes via `parser:simple_xml(xml_table)` **without local `try` wrappers**. Therefore its protected parse/construction stages should not be generalized to arbitrary mod callback or serializer exceptions. Later native error propagation is an open behavior, not proven to be safe.
6. The cache checks exact `xml_file_name` keys before parsing; callback-set `flags.cache` stores transformed XML. A cached hit suppresses subsequent callback dispatch for that name in the current cache lifetime. Neither invalidation nor full external patch interaction is demonstrated.

## Registration and order

7. [`dxml_core.script`, lines 119–163](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L119-L163): discovers nonempty root `modxml_*.script` files, retrieves modules, sorts their names, and invokes module `on_xml_read()` *registration functions* in sorted order. A separately specified forced-load list follows. This proves sorting of **registration calls**, not arbitrary code loading order or guarantees against third-party wrappers.
8. [`_g_patches.script`, lines 427–440](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/_g_patches.script#L427-L440) delegates `RegisterScriptCallback` to `axr_main.callback_set`. [`axr_main.script`, lines 509–580](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/axr_main.script#L509-L580) recognizes before/after constraints, priority tiers, and reorder logic, with validation and rollback on failed reordering. Order is not purely lexical when priority/constraints intervene. This audit does not assert precedence for any specific external addon.
9. [`dxml_core.script`, lines 1033–1052](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L1033-L1050) exposes `openXMLFile` with separate protected parse/construct stages and callback dispatch. Its failure semantics should not be conflated with native `CXml::Load`.

## CtZ recommendations and boundary

- Avoid throwing errors inside `on_xml_read` hooks; check target nodes, log narrowly, and preserve original structures when unable to patch.
- Keep patches deterministic/idempotent; do not assume alphabetical filenames control final callback execution priority.
- Do not depend on DXML callback failure being automatically caught by native code.
- Runtime-deferred: actual GAMMA mod load order, external wrappers, error propagation in executable, malformed patch repro, cache conflicts.

**Source-level remaining questions:** a truly exhaustive error-propagation study through Luabind and global script exception handlers would be separate; it is not necessary to represent local callback behavior above accurately. This record deliberately makes no blanket claim that all Lua exceptions terminate the game.
