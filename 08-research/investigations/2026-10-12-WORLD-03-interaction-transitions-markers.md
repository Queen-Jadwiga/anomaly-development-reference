# WORLD-03 — Use touch actor transitions and marker lifecycle

> ADR document set: **v0.1.81**. Research revisions and source/build versions below describe their original scope.

- ID: WORLD-03
- Subsystem: world interaction/navigation
- ADR revision: v0.1.72
- Record status: complete-within-scope
- Source status: source-confirmed selected native definitions/registrations/callers and bundled marker relay
- Runtime status: untested; deferred
- Baseline IDs/provenance: ENGINE1011 October 11 uploaded archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and scope

Trace selected actor-use/forced-use callback and UI handoffs, script-zone sampled contacts versus movement restrictors, level-changer trigger/dialog/packet/server save/reconnect and local/server state, plus ordinary object-marker add/query/remove/update/serialization/restoration. Exclude every interactable/door/vehicle implementation, anomaly damage, full renderer/relation-marker visibility, every installed Lua consumer and executable testing. Reuse WORLD-02 relocation and existing A-Life/inventory/tasks/persistence foundations.

## Evidence and method

[Ledger U01–U16, T01–T13, M01–M19](../../evidence/world/interaction-transition-markers-2026-10-12.csv) records exact raw file hashes, line counts, symbols and ranges. Follow selected registrations into implementations and callers, compare void/bool results, contact membership order, actual save writes and queue phases. No invented upstream commit or installed build/profile correspondence. Two native control paths are not assumed equivalent because their names resemble one another.

## Findings

The [behavior reference](../../04-game-systems/world/interaction-transitions-markers.md) holds the detailed source citations; [API tables](../../02-lua-api/world/interaction-api.md) record actual call shapes/returns. Use callback returns, Lua forced-use booleans and void UI calls have different meanings. Script-zone geometry/list membership/release notifications differ. Silent level-changer contact bypasses the enabled flag checked in dialog presentation; acceptance saves destination state, restores current server state and broadcasts a restart request. Marker append/query/remove/visibility/storage and notification phases are separate; numeric 0/1 query return and duplicate handling matter for Lua consumers. Stored XML-derived TTL/cache/subclass behavior is not fully encoded by the selected marker save format.

## Competing explanations and missing edges

A use callback can be mistaken for completed inventory/dialogue action; selected callers ignore or reinterpret the return. Disabled client flags can be mistaken for universal travel gates; silent/direct callers differ. A marker entry can be mistaken for a rendered, lifetime-safe or persisted marker; XML, owner/cache, visibility and queue state have separate rules. Effective UI/map/destination XML, dispatcher/listener/binder/state replacements and all installed consumers remain required for installed closure. Callback reentrancy/thread safety and save error rollback are not inferred from queue code or successful structural checks.

## Checks and outcomes

Verify all ledger raw hashes/counts/ranges/symbols, selected registration/definition/caller orders and serialization omissions; preserve prior evidence/history/tools; run repository checks and existing regressions; verify remote base and published path/blob maps. [Verification](../verification-2026-10-12-v0.1.72.md). No engine compile, independent runtime or CtZ gameplay change.

## Disposition and next work

WORLD-03 selected available-source trace is complete within scope. World interaction/navigation remains partial. Next WORLD-04 supplied consumers/variants, cross-system practical consolidation and bounded audit; preserve missing effective/runtime edges under the [completion rule](../../04-game-systems/world/source-completion-status.md). [Guide](../../04-game-systems/world/development-reference.md), [roadmap](../../ROADMAP.md).
