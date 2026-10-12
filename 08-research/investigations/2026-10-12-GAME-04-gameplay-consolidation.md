# GAME-04 — Gameplay state consolidation and bounded audit

> ADR document set: **v0.1.66**. Research revisions and source/build versions below describe their original scope.

- ID: GAME-04
- Subsystem: actor/NPC gameplay state
- ADR revision: v0.1.66
- Record status: complete-within-scope
- Source status: scoped-source-audit synthesis of selected source-confirmed contracts
- Runtime status: untested; deferred
- Baselines/provenance: ENGINE1011/BETA150; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and scope

Consolidate GAME-01–03 into practical guidance and a source-completion rule. Audit current/pending/server/custom state, hit/effect/return/cleanup phases, inheritance and persistence boundaries against selected evidence. Exclude every species/variant, effective profile closure and runtime/gameplay changes.

## Evidence and method

Reuse [GAME-01 G01–G21](../../evidence/gameplay/native-condition-2026-10-12.csv), [GAME-02 A01–A21](../../evidence/gameplay/actor-effects-2026-10-12.csv) and [GAME-03 R01–R19](../../evidence/gameplay/death-restoration-2026-10-12.csv). Validate all 61 rows and their cited ranges; preserve original ledger bytes/schema. Re-read selected update/booster/death/spawn/serializer bodies and declarations; compare existing references/API pages with literal order/returns. No new baseline introduced.

## Findings

[Development reference](../../04-game-systems/gameplay/development-reference.md) reconciles state owners, actor versus NPC mechanics, mutation versus observation and snapshot versus final restoration. [Completion status](../../04-game-systems/gameplay/source-completion-status.md) closes available-source first-edition scope without closing effective integration. Carry medicine updater, booster accessor/compiler and repeated restoration questions forward. Source integrity and prior semantic distinctions are retained; no new runtime bug or tested recipe is asserted.

## Competing explanations and missing edges

Installed scripts/builds can replace or mask selected behavior. Accepted booster/use calls and callbacks do not establish effects/settlement/cleanup. Optional formulas and raw setters do not validate arbitrary numeric input. Base custom serializer omissions do not establish whole-save loss; online/offline death paths remain separate. Effective source and runtime gaps are explicit rather than expanded into assumed behaviors.

## Checks and outcomes

[Verification](../verification-2026-10-12-v0.1.66.md) records bounded semantic audit, ledger checks, preservation, links/banners and existing regressions. No runtime or engine compilation ran.

## Disposition and next work

GAME-04 complete within scope; effective gameplay-state integration partial, runtime deferred. Next tasks/dialogue/info state, inventorying existing coverage before new research. [Roadmap](../../ROADMAP.md).
