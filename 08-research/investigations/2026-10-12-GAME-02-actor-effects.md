# GAME-02 — Actor survival effects and equipment mitigation

> ADR document set: **v0.1.74**. Research revisions and source/build versions below describe their original scope.

- ID: GAME-02
- Subsystem: actor/NPC gameplay state
- ADR revision: v0.1.64
- Record status: complete-within-scope
- Source status: source-confirmed selected actor/effect/equipment paths; scoped-source-audit medicine update gap
- Runtime status: untested; deferred
- Baseline/provenance: ENGINE1011; [source record](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-12

## Question and scope

Trace actor update gates, sleep/satiety/stamina, medicine/booster application/replacement/expiration, selected Lua exports and outfit/helmet/artefact mitigation. Link prior condition/consumption findings. Exclude full derived creature behavior, all effectors/upgrades/bone-table internals, complete save reconstruction, installed configuration and runtime.

## Evidence and method

[A01–A21 ledger](../../evidence/gameplay/actor-effects-2026-10-12.csv), original paths/hashes/ranges/symbols. Archive SHA-256 14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee; upstream/build/profile match unknown. Read update, effects, serializer and bindings together; compare actual actor Hit stages with base GAME-01. Search all src/xrGame C++ and bundled gamedata scripts for medicine record/current-time readers/writes; preserve snapshot-only scope.

## Findings

[Reference](../../04-game-systems/gameplay/actor-effects-equipment.md) maps survival, typed booster replacement and success-return limits, optional armor formulas, artefact query/damage differences and callback phases. [API subset](../../02-lua-api/gameplay/actor-effects-api.md) records raw modifiers and by-value map/reference mismatch.

## Competing explanations and missing edges

No timed medicine advance/apply consumer was found in the selected native/bundled-script search scope; installed external scripts or another compiled revision may differ. Non-const reference binding to a by-value booster accessor raises a build/ownership mismatch, not a tested runtime bug. Optional armor parameter presence does not validate divisors. Whole restore initialization, effective callbacks/item configs/upgrades/owner skeletons and NPC policy remain required.

## Checks and outcomes

Ledger hashes/counts/ranges/symbols and existing repository/tests checked; prior evidence/history/generated datasets unchanged. Source interpretations reviewed with state/return/lifetime boundaries. [Verification](../verification-2026-10-12-v0.1.64.md). No independent engine/game execution or source patch.

## Disposition and next work

GAME-02 complete within selected scope; gameplay-state integration partial. Next derived death and server/client condition restoration with supplied/effective consumers, then consolidation/audit. Carry timed-medicine and booster-accessor questions forward. [Roadmap](../../ROADMAP.md).
