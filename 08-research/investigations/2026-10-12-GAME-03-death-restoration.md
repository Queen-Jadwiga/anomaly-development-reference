# GAME-03 — Derived death and condition reconstruction

> ADR document set: **v0.1.69**. Research revisions and source/build versions below describe their original scope.

- ID: GAME-03
- Subsystem: actor/NPC gameplay state
- ADR revision: v0.1.65
- Record status: complete-within-scope
- Source status: source-confirmed selected native/server/supplied paths
- Runtime status: untested; deferred
- Baselines/provenance: ENGINE1011/BETA150; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and scope

Trace selected actor/stalker/base-monster derived death order and server/live/client-data health restoration. Link existing base hit/casualty/storage findings, expose callback observation limits, and carry medicine/booster questions forward. Exclude all species overrides, whole installed handlers, complete packet/converter inventory, malformed-save robustness and runtime/gameplay changes.

## Evidence and method

[Ledger R01–R19](../../evidence/gameplay/death-restoration-2026-10-12.csv) pins archive-relative paths, hashes and cited ranges/symbols. Archive SHA-256 pins remain in the manifest; installed/executable correspondence unknown. Read derived call chains, factory/virtual save-load dispatch, Entity versus CustomMonster spawn writes, server STATE/UPDATE and registry load order, plus selected supplied offline disposition.

## Findings

[Reference](../../04-game-systems/gameplay/death-restoration.md) records eDeath inside derived cleanup; separate server on_death/kill; health STATE/UPDATE versus custom conditions; pre-binder Entity health and post-binder CustomMonster overwrite; actor serializer/factory dispatch and repeated-load limits. Supplied offline bookkeeping does not prove live callback traversal.

## Competing explanations and missing edges

Effective binders and server script classes can override native handlers; built executable/configuration and startup order remain unknown. A getter or serializer is not a common authoritative snapshot across offline/server/live objects. Actor boost reset/reapply, health-to-membership convergence, medicine updater and helper/compiler mismatch remain open. Safe revival or casualty reconciliation cannot be inferred from health writes.

## Checks and outcomes

Check hashes/counts/ranges/cited symbols, existing repository regressions, base-tree correspondence and prior evidence/history preservation. Review inheritance/spawn/virtual dispatch source order rather than deriving it from names. [Verification](../verification-2026-10-12-v0.1.65.md). No engine/game runtime.

## Disposition and next work

Selected GAME-03 available-source boundary complete; effective integration partial. Next gameplay-state practical consolidation and bounded audit; carry effective-source and runtime gaps explicitly. [Roadmap](../../ROADMAP.md).
