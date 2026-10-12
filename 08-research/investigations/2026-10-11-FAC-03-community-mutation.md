# FAC-03 — Character-community mutation and team/group effects

> ADR document set: **v0.1.57**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-03
- Subsystem: factions / relations
- ADR revision: v0.1.46
- Record status: complete-within-scope
- Source status: source-confirmed within selected setters, virtual paths and packet consumers
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline and provenance: ENGINE1011; [October 11 source](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-11

## Question and scope

How does the client Lua community setter update character/server identity and live team/squad/group state, and what downstream effects are established?

Include declarations/registrations, client inventory-owner bridge, character index/sympathy, entity hierarchy migration, group shared memory/agent ownership, selected stalker/base-monster hooks, separate team-only wrapper, server community getter/state, selected tuple packets/receipt and spawn hydration, actor display side effect. Exclude effective disguise/faction-switch scripts, every derived entity override, exhaustive hierarchy bounds/converters, AI decision convergence, strategic board/squad reassignment, all save/packet timing and runtime tests. Completion is a source-pinned native chain and focused API contracts, not complete installed faction switching.

## Evidence and method

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit/executable/effective configuration remain unknown. [Ledger M01–M19](../../evidence/factions/community-mutation-2026-10-11.csv) records 19 files with hashes, symbols and ranges.

Read setter/wrapper bodies in source order, follow virtual `ChangeTeam` and group register/unregister helpers, compare server community/creature fields and tuple packet bodies/receipt, then inspect reconstruction and the actor display function. Preserve previously traced A-Life lifetime/persistence and relation-storage boundaries. No generic installed policy substituted for missing effective scripts.

## Findings

The [native reference](../../04-game-systems/factions/community-mutation.md) and [API contracts](../../02-lua-api/factions/community-mutation-api.md) carry nearby M-citations.

- Lua community setter calls inventory-owner mutation, then tuple migration with supplied squad/group. Inventory-owner alive phase uses current squad/group first; two actual migrations are possible. Same-tuple calls are no-ops. M01/M02/M04.
- Character mutation resets sympathy; server trader community is written after live mutation and alive-only migration. Missing lookup/trader or assertion failures can leave earlier phases without later completion; no rollback/success contract. M01–M03/M15.
- Tuple change migrates local hierarchy membership, agent manager and shared senses; selected stalker hooks preserve combat registration and base monsters migrate their extra squad system. This is separate from A-Life/Warfare strategic squad identity. M04–M07 and A-Life reference.
- Team-only Lua helper does not invoke community mutation. Native signature/receiver requirements differ from the community setter. M08–M10/M16/M18.
- Trader identity is a direct server field write; creature tuple follows the selected update-receipt path and separate state/update serialization. Spawn hydration reads server community/tuple separately. No atomic packet/save guarantee. M02/M03/M04/M06/M11/M17/M19.
- Actor's selected faction RPC function updates Discord display via a script true-community getter; it does not establish game diplomacy/ownership/UI refresh. M13.

## Missing edges and competing explanations

A later script may reconcile faction identity, strategic membership, goodwill and disguise/true-community values, or override the selected behavior. Packet receipt, partial setter phases, specific-character/species hydration and separate strategic caches can produce divergent observed fields. These are source-grounded possibilities, not reproduced defects. Installed scripts/builds/configuration and actual AI/UI timing remain unavailable.

## Checks and outcomes

Compared exact signatures/registrations, receiver casts, early returns, mutation order, hook ownership, selected packet fields and source-level build/version conditions. Verified ledger full-file hashes, line counts, range bounds and symbols within cited ranges. Repository navigation, version and preservation checks are in [v0.1.46 verification](../verification-2026-10-11-v0.1.46.md). No engine compilation, gameplay changes, source redistribution or runtime tests.

## Disposition and next work

FAC-03 completes the bounded native community/team mutation chain. Factions remains partial. Next: action-driven goodwill (attack/kill/help), rank/reputation contributions, then supplied Warfare/effective diplomacy consumers. Runtime stays deferred. [Roadmap](../../ROADMAP.md).
