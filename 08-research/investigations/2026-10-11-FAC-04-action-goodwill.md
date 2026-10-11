# FAC-04 — Action-driven goodwill and rank/reputation contributions

> ADR document set: **v0.1.47**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-04
- Subsystem: factions / relations
- ADR revision: v0.1.47
- Record status: complete-within-scope
- Source status: source-confirmed within selected native actions/callers/registrations
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline and provenance: ENGINE1011; [October 11 source](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-11

## Question and scope

Which selected online hit/death actions change goodwill, reputation or rank, and how do eligibility, fight memory, victim relation, configuration and callback phases affect them?

Include native Hit/Die entry gates, fight registry/throttle/help inference, action outcomes, rank/reputation bands and attitude tables, live/server numerical setters, Lua value/flag contracts and actor display effects. Exclude every reward path, installed action-point/rank tables, effective game-relations/diplomacy scripts, all derived Hit/Die overrides, offline convergence, executable timing and runtime tests. Completion requires a bounded source reference and focused contracts, not a universal award algorithm for GAMMA.

## Evidence and method

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit/executable/profile correspondence unknown. [Ledger A01–A20](../../evidence/factions/action-goodwill-2026-10-11.csv): 20 entries across 19 files, with selected symbols/ranges and full-file hashes.

Read native entry/caller and outcome bodies, fight first-match/expiry logic, settings read points, rank/reputation loaders/tables, setters, declarations/registrations, flag implementation and object-bound death phase. Compare conditions against comments, distinguishing directed target-to-source relation from symmetric/strategic state. Follow previously pinned Warfare offline boundaries without importing installed script behavior.

## Findings

The [action reference](../../04-game-systems/factions/action-goodwill.md) and [Lua contracts](../../02-lua-api/factions/action-values-api.md) provide nearby A-citations.

- Selected Hit registers attack only with surviving living victim/attacker, different IDs and single-player; selected Die attempts KILL before inherited death/object callback. Not every lethal hit/offline casualty shares that path. A01.
- Common Action gate is inventory-owner source excluding base monsters, not simply actor-only. Stalker target flags/relation resolution precede branch gates. A03.
- Actor throttle uses the first matching fight record and device milliseconds. Inferred help is recursive fight-memory policy; both help enums share a branch, while declared SOS_HELP has no case in this switch. A02–A04/A18/A19.
- Attack excludes stalker-to-stalker goodwill; kill excludes same-community stalker goodwill. Group-to-source personal and community-to-source changes are distinct. Community changes are nested inside nonzero personal delta; reputation and kill rank use separate gates. A04/A12.
- Kill uses current relation because historical fight-relation use is commented out. Rank award uses victim stalker band; no universal monster reward is asserted. A04/A05.
- Rank/reputation bands use strict thresholds and feed directed attitude tables. Their numerical setter path has different limits from goodwill and writes client/server values after server-trader checks. A05–A12.
- Flags are not counted events or award receipts: KILL is zero and the mask implementation sets no new bit for it; flag attempts can occur before suppressed outcomes. Actor RPC helpers update Discord display, not a universal award-completion signal. A03/A09/A13–A15/A18/A20.

## Missing edges and alternatives

Effective scripts can award additional deltas, replace callbacks, reconcile offline events or implement other ranking models. Different fight-record selection, elapsed-time gates, configuration signs/limits, victim relation or independent rank/reputation effects can explain observations; this pass makes no runtime diagnosis. Installed action tables and death/cleanup/diplomacy dispatch remain unknown.

## Checks and outcomes

Reviewed source order, gate nesting, active versus commented code, thresholds, flags, signatures and callbacks. Verified full-file hashes, counts, ranges and symbols within cited ranges. Preservation/navigation/version tests are recorded in [v0.1.47 verification](../verification-2026-10-11-v0.1.47.md). No engine build, gameplay changes, source redistribution or runtime tests.

## Disposition and next work

FAC-04 closes this bounded native pass; factions remains partial. Next: supplied Warfare faction/relation consumers and effective-script boundaries, then practical consolidation and final available-source audit. Installed diplomacy/true-community/reward policy and runtime remain open. [Roadmap](../../ROADMAP.md).
