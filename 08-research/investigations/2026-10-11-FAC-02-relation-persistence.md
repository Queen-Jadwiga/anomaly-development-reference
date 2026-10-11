# FAC-02 — Native relation persistence, reset and ID cleanup

> ADR document set: **v0.1.50**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-02
- Subsystem: factions / relations
- ADR revision: v0.1.45
- Record status: complete-within-scope
- Source status: source-confirmed within selected paths; bounded negative serializer/cleanup findings
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline IDs and provenance: ENGINE1011; [October 11 source](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-11

## Question and scope

Which native relation state is serialized, which caches reset, and what does object-ID cleanup remove?

Include relation-data and A-Life registry ownership/serialization, selected load callback phases, wrapper/local fallback, level table reset, native monster unregister, object-registry/simulator destruction and module-detach cleanup. Exclude binary-format portability certification, effective diplomacy serializers/creature overrides, all engine teardown routes, faction-change propagation, action/fight updates and runtime tests. Completion is a bounded storage/lifetime reference, not complete faction persistence in installed GAMMA.

## Evidence and method

Archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; exact upstream commit/executable/profile correspondence unknown. [Ledger P01–P18](../../evidence/factions/relation-persistence-2026-10-11.csv) records 18 source files, hashes, ranges and symbols. P-labels are local to this ledger.

Read serializers, owner/container/wrapper definitions, load/save and unregister/destruction call sites. Search `src/` for `ClearRelations`, `clear_relation_registry`, `CHARACTER_COMMUNITY::Reset` and matrix references; interpret the selected implementations rather than treating search results as universal installed behavior. Review default map-loader clearing/acceptance and preserve ALIFE-04/07 lifecycle boundaries.

## Findings

The [practical reference](../../04-game-systems/factions/relation-persistence.md) supplies adjacent P-citations.

- Personal and community-to-character maps belong to the A-Life relation registry and are included in native save/load. Numeric person IDs/community indexes are saved, without a campaign fingerprint or name remapping in these records. P01–P05/P08/P17.
- Relation restoration precedes the selected final native `on_register` loop; early before-register and guarded storage load functor phases are earlier. Installed Lua load order remains unknown. P08/P10.
- The static community matrix/sympathy caches are reset by the selected level-before-load hook and lazily reload configuration. They are separate from saved relation records. An inspected matrix setter write is not made durable by the per-character serializer. Effective addon save/reapply logic remains open. P13–P15/P18.
- Native monster unregistration clears its own record maps after the inherited hook; the clear does not erase the outer record or sweep others' incoming personal references. Conditional ID-reuse implications are not runtime bug findings. P02/P09/P10/P17.
- Client teardown, creature death, native unregister and simulator teardown remain distinct. Unload deletes object registry/hook-bearing objects before the auxiliary relation owner; wrapper cleanup is separate. P06/P07/P11/P12 and ALIFE-07/WAR-002b.
- Module detach invokes wrapper/fight/map-spot cleanup; the scoped source search does not turn this into a per-level goodwill reset API. P02/P16.

## Competing explanations and missing edges

A diplomacy addon can save/reapply the faction matrix or sweep references outside these native paths. Effective creature overrides may omit inherited unregister. Querying a relation before native restoration or after a table reset can show different state without implying a serializer defect. Exact installed callbacks/configuration, all AI refresh behavior and runtime timing are unavailable.

## Checks and outcomes

Verified selected source order and ownership, field/key types, map serialization/default loader behavior, and cleanup reach within the cited functions. Checked full-file hashes, recorded counts, range bounds and symbols. [v0.1.45 verification](../verification-2026-10-11-v0.1.45.md) records repository checks and preservation. No engine build, source redistribution, gameplay changes or runtime verification.

## Disposition and next work

FAC-02 is complete within scope. The faction subsystem remains partial; character-community mutation is next, followed by action-driven goodwill and effective Warfare/diplomacy integration. Runtime remains deferred. [Roadmap](../../ROADMAP.md).
