# ITEM-03 — Consumption, destruction and owner cleanup

> ADR document set: **v0.1.63**. Research revisions and source/build versions below describe their original scope.

- ID: ITEM-03
- Subsystem: inventory
- ADR revision: v0.1.56
- Record status: complete-within-scope
- Source status: source-confirmed selected native/actor/eatable paths
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline: ENGINE1011; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-11

## Question and scope

What separates use effects, exhaustion/drop, destruction requests, server/client removal and owner cleanup? Include Eat/ClientEat, selected eatable config/UseBy/hooks, actor named gate, manual-drop producer, server destroy packing/child recursion, live destroy/queue/teardown, owner clear/selective removal and focused Lua wrappers/accessors. Exclude every derived item/death policy, effect internals, full release graph, persistence and runtime.

## Evidence and method

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit/binary/profile unknown. [D01–D18 ledger](../../evidence/inventory/consumption-destruction-2026-10-11.csv) pins original paths/bytes/counts/ranges. Read definitions/callers/registration and active-versus-commented gates; compare u8 declaration with literal infinite-use comment and effect/return order. Interpretation does not substitute for runtime.

## Findings

[Reference](../../04-game-systems/inventory/consumption-destruction.md) and [API](../../02-lua-api/inventory/consumption-api.md) cite each boundary.

- Eat effects/callback can precede false for an exhausted retained item; ClientEat only sends and actor request has its own named gate. D01/D05/D13/D18.
- Exhaustion can mark deferred drop; eatable independent hooks request local/server destruction separately. Literal u8/-1 comparison does not support the 255-infinite comment under ordinary promotion. D02–D04.
- Request, server child/reject/removal, client destroy flag, reference-release/net_Destroy and wrapper deletion are distinct. D06–D09.
- Owner Clear resets containers/owner rather than per-item drop/destruction. Selective sell_useless_items requests destruction with exclusions, not demonstrated payment. D10–D12.

## Competing explanations and missing edges

Effective gates can reject empty use, derived classes/config can alter counters/effects and NPC/death policy can choose other paths. Server recursion/queue assumptions are not complete malformed-graph robustness guarantees. No runtime defect or verified NPC consumption recipe is asserted; new findings qualify this source rather than modifying it.

## Checks and outcomes

Ledger hash/count/range/symbol, semantic order/declaration/registration, preservation/navigation/version/tests and publication checks: [increment verification](../verification-2026-10-11-v0.1.56.md). No runtime, source/gameplay/save edits, build, redistribution or license.

## Disposition and next work

ITEM-03 selected consumption/removal foundation complete within scope; inventory partial. Next item persistence/reconstruction, then consolidation/audit; runtime deferred. [Roadmap](../../ROADMAP.md).
