# ITEM-01 — Native inventory ownership and pickup/drop

> ADR document set: **v0.1.82**. Research revisions and source/build versions below describe their original scope.

- ID: ITEM-01
- Subsystem: inventory
- ADR revision: v0.1.54
- Record status: complete-within-scope
- Source status: source-confirmed selected native/server/actor/box paths
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline: ENGINE1011; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-11

## Question and scope

How do server attachment, live parenting and inventory membership change through selected pickup/drop/transfer paths, and when do native callbacks observe them? Include server guards/routing, selected single-player graph helper callers, actor/base owner/box consumers, live parent hooks, focused Lua request/enumeration methods and registrations. Exclude full NPC variants, graph helper internals, slot/activation details, pricing, consumption, full destruction/save reconstruction and effective scripts/runtime.

## Evidence and method

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit/installed executable correspondence unknown. [I01–I20 ledger](../../evidence/inventory/ownership-lifecycle-2026-10-11.csv) records paths, original-byte hashes, counts and line/symbol ranges. Read native definitions, receiver routing, callers, actor overrides and Lua registrations/signatures; compare callback sites with following mutations rather than treating their names as completion signals.

## Findings

[Ownership reference](../../04-game-systems/inventory/ownership-lifecycle.md) and [Lua contracts](../../02-lua-api/inventory/ownership-api.md) carry nearby evidence IDs.

- Server ID containment, live parenting, inventory membership/placement and box ID storage are distinct representations. I01/I02/I07–I13.
- Server take performs guarded attach/broadcast; reject checks membership and invokes detach before clearing server parent. Parent mismatch logging does not abort that reject branch. I07–I10.
- Selected actor take parents before inventory insertion; callback occurs after placement but before later weight/UI work. Drop removes inventory membership then invokes callback while live parent/old placement still exist; parent detach follows. I01–I06/I11/I12.
- Box callback observes in-use removal, not certified destination receipt. Lua helpers send event sequences without transaction/completion result; SAFE_WRAP does not convert them into such an API. I13–I17/I20.
- Available-item enumeration is filtered and pointer-list based, not a lifetime-safe raw m_all snapshot. I18/I19.

## Competing explanations and missing edges

NPC/derived owners, online/offline graph handling and installed binders/addons can add guards or notifications. Direct event sequences require transport/consumer evidence before claims about synchronous completion. Callback reentrancy and pointer lifetime are not certified by source ordering alone. No runtime crash, ID inconsistency or transaction failure is diagnosed.

## Checks and outcomes

Verify source hashes/counts/ranges/symbols, API registrations and signatures, semantic phase order, prior evidence/history preservation, navigation/version and publication tree/readbacks. [Increment verification](../verification-2026-10-11-v0.1.54.md). No runtime, gameplay/source/save edits, engine build, redistributed source/assets or license.

## Disposition and next work

Selected ownership/request/observer foundation complete within scope; inventory subsystem partial. Next ITEM-02 placement/active-item transitions, then consumption/destruction, persistence and bounded consolidation. Broader general-modding ADR roadmap now separates these foundations from CtZ examples and optional depth. [Roadmap](../../ROADMAP.md).
