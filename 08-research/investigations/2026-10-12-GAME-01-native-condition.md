# GAME-01 — Native condition fields and live hit phases

> ADR document set: **v0.1.72**. Research revisions and source/build versions below describe their original scope.

- ID: GAME-01
- Subsystem: actor/NPC gameplay state
- ADR revision: v0.1.63
- Record status: complete-within-scope
- Source status: source-confirmed selected native/base/live and supplied callback paths
- Runtime status: untested; deferred
- Baseline/provenance: ENGINE1011; [source record](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-12

## Question and scope

Identify live condition fields, direct setters versus pending changes, update/time/harm gates, selected hit mitigation/branch/callback stages and death request boundaries. Inventory prior faction/casualty/consumption coverage and link it. Exclude full actor survival/boosters, equipment formulas, every derived death override, complete server/client persistence and runtime/gameplay changes.

## Evidence and method

[Ledger G01–G21](../../evidence/gameplay/native-condition-2026-10-12.csv) pins archive-relative files, ranges/symbols and full-file hashes. Archive SHA-256 14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee; upstream/executable/profile correspondence unknown. Read state declarations, macros/registration, base condition routines and live caller/death-event chain, plus supplied callback relay. Preserve existing investigation and evidence bytes.

## Findings

[Reference](../../04-game-systems/gameplay/native-condition.md) maps current fields versus pending deltas, health/time/last-chance gates, branch-specific damage and mutable callback limits, immunity coefficient semantics, death request/event/cleanup and partial serializer boundaries. [API page](../../02-lua-api/gameplay/condition-api.md) preserves direct property versus delta behavior and base satiety no-ops. Existing faction/casualty/consumption records retain their scope.

## Competing explanations and missing edges

Derived actor/stalker/monster hits, before-death build activation, script relays/listeners, configuration and binders may change behavior. Base condition harm gates are not total invulnerability across all fields. Callback mutability does not restart branch selection, recompute attribution or supply a persistent hit object. Missing serialization in a base body does not establish whole-save loss. Offline combat need not traverse this live chain; health <= 0 is not confirmed strategic casualty cleanup.

## Checks and outcomes

Validate ledger paths/hashes/counts/ranges/cited symbols, source wrappers and caller semantics; run repository checker/existing regressions; preserve prior ledgers/history and dated investigation bodies except current banners. [Verification](../verification-2026-10-12-v0.1.63.md) records actual results. No independent game runtime.

## Disposition and next work

GAME-01 complete within selected scope; gameplay-state subsystem partial. Next actor-specific condition/survival/boosters/equipment, then derived death/condition restoration and supplied/effective consumers, followed by consolidation/audit. [Roadmap](../../ROADMAP.md).
