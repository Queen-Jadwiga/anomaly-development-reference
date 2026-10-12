# FAC-06 — Faction reference consolidation and final available-source audit

> ADR document set: **v0.1.78**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-06
- Subsystem: factions / relations
- ADR revision: v0.1.49
- Record status: complete-within-scope
- Source status: consolidation of source-confirmed selected paths; bounded consistency audit
- Runtime status: untested; deferred until explicitly resumed by the user
- Baselines and provenance: ENGINE1011 and BETA150 main; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-11

## Question and scope

Can FAC-01–05 form a consistent practical CtZ development reference without conflating faction identities, relation queries, mutation, persistence, rewards and strategic ownership?

Include practical selection/phase/storage guidance, cross-reference review of the completed investigations and focused APIs, source spot checks of high-impact boundaries, evidence/navigation/version integrity and a current completion rule. Exclude new engine mechanics, effective installation closure, exhaustive API/variant/quest coverage and runtime verification. This completes the final consolidation/audit action authorized after FAC-05.

## Evidence and method

Existing five [faction ledgers](../../evidence/factions/README.md) retain their bytes, schemas and labels: F (identity), P (persistence), M (mutation), A (actions), R (BETA150 consumers). They contain 95 entries across 62 distinct source files and 148 range groups. No replacement or duplicate synthesis ledger is needed: the [development reference](../../04-game-systems/factions/development-reference.md) qualifies each label by its original ledger.

ENGINE1011 archive hash `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee` and BETA150 hash `9f71999bb44cb6d3e41c431feaf5be4714159522df1fa8d71599ac039946315d` pin snapshots. Upstream engine commit/executable/profile correspondence and installed winners remain unknown.

Review selected claim boundaries across FAC-01–05, their APIs and the adjacent A-Life/Warfare references. Re-read high-impact native/helper bodies, verify all faction-ledger hashes/counts/ranges/symbols within ranges, preserve earlier findings and explicitly retain missing effective edges. The [audit report](../verification-2026-10-11-v0.1.49.md) records scope/results, not exhaustive proof of every sentence or build.

## Findings and consolidation

[Practical guide](../../04-game-systems/factions/development-reference.md) connects:

- Configured community identity, script faction mapping and strategic ownership as separate models.
- Directed matrix, target-owned community goodwill, personal contribution, three-/five-term aggregates and virtual live relation as separate query contracts.
- Contribution setters, native community bridge, live hierarchy migration and script strategic mutation with their own preconditions/phase limits.
- Saved goodwill, static matrix reset and supplied script save/reapply as separate persistence domains.
- Native online awards, dynamic adapters, offline outcome and actor support with independent eligibility and observation boundaries.

The audited selected boundaries are consistent with their pinned sources. No substantive research conclusion is silently rewritten. Current navigation/status now reflects completion of the available-source work while dated records preserve the sequence and former next steps.

## Missing edges and limits

Effective identity/diplomacy, startup/storage, death/reward, strategic reassignment and CtZ synchronization still require winning sources/dependencies and configuration. Archive labels and source spot checks cannot certify installed behavior. Exhaustive unrelated types, converters/builds and quest consumers are optional expansions.

## Checks and disposition

Source integrity, preservation, navigation/version tests and publication checks are in [v0.1.49 verification](../verification-2026-10-11-v0.1.49.md). Runtime remains untested; no gameplay edits, script fixes, engine build, license addition or third-party source distribution.

FAC-06 closes planned available-source consolidation/audit. Full effective integration remains partial under [completion status](../../04-game-systems/factions/source-completion-status.md). Another subsystem can proceed independently; missing installed-source contracts remain tracked in the [roadmap](../../ROADMAP.md).
