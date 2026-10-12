# ALIFE-11 — Native configuration and control contracts

> ADR document set: **v0.1.74**. Research revisions and source/build versions below describe their original scope.

- ID: ALIFE-11
- Subsystem: A-Life
- ADR revision: v0.1.43
- Record status: complete-within-scope
- Source status: source-confirmed within selected definitions/consumers
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline IDs and provenance record: ENGINE1011; [October 11 baseline](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-11

## Question and scope

Which native settings and Lua controls affect scheduling, switching, offline movement and task selection, and what do their consumers establish about units and update behavior?

Include manager constructor/reload/setters, switching formulas, schedule count/time specialization, graph-budget forwarding, scheduler clock/interval, entity speed initialization/Lua helpers, detail movement and individual task-choice interval. Exclude installed settings, every configuration consumer, online AI/tactics, tuning changes and runtime tests. Completion is a producer/consumer reference with pinned definitions and qualified units.

## Evidence and method

Archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; exact upstream commit and executable correspondence unknown. [Ledger N01–N18](../../evidence/alife/configuration-controls-2026-10-11.csv) follows the current claim-ledger schema and records 18 source files, symbols, ranges and hashes.

Read the selected functions and corresponding bindings, continuing the ALIFE-05/08/09 traces. For schedule cadence, trace the millisecond device clock and `CSheduler::ProcessStep`; for process budget, trace manager → graph → current-level registry → inherited iterator comparison. Check full-file hashes, line counts, range bounds and symbols against the extracted snapshot.

## Findings

The [configuration/control reference](../../04-game-systems/alife/configuration-controls.md) provides the mappings and nearby N-citations.

- Native schedule inputs are transformed by the general scheduler; the manager can defer work under `mtALife`. They do not define a guaranteed observed brain cadence. N01/N09/N10.
- Schedule entries are count-limited; that registry disables the inherited time cutoff. A configured batch does not mean all living NPCs update. N04/N05.
- Switch distance/factor compute the two thresholds; effective permissions and outer gates still bound transition. Lua distance changes are separate from immediate realization. N02/N03/N15/N18.
- Entity-section speeds and Lua speed setters feed offline detail movement, whose elapsed game time and normal-time factor remain separate from manager cadence. N11–N13.
- Individual smart task-selection interval and selection permission do not specify group Lua strategy or clear existing assignment. N14.

### Process-time qualification

The public helper/native method use a named microsecond integer input. The native expression is `float(microseconds) - float(microseconds) * update_monster_factor() / 1000000.f`. Graph/current-level forwarding passes that float into an unchanged iterator budget, whose time test uses `GetElapsed_sec()`. N01/N06–N08/N16/N17.

This adds a narrower source qualification to the API's named input; it does not rewrite the original source findings, normalize the expression, or establish a runtime bug. A literal method/argument name is insufficient to certify actual wall-clock units or scheduled-brain time limits.

## Competing explanations and missing edges

Installed settings/addon setters, executable changes, active threading flags, timer observations and effective task/board policy are unavailable. An observed delay could involve manager cadence, count-limited membership, task/path failure, accumulated game-time movement or client realization. This source-only reference does not choose a runtime diagnosis.

## Checks and outcomes

Selected hash/range/symbol verification and source-order review are recorded in the [v0.1.43 audit](../verification-2026-10-11-v0.1.43.md). Navigation/version checks and previous catalog/evidence preservation apply. No tuning, gameplay changes, engine compilation or in-game tests were performed.

## Disposition and next work

ALIFE-11 completes the native control-reference part of available-source consolidation. See [completion status](../../04-game-systems/alife/source-completion-status.md) for still-missing effective chains and deferred runtime work. Collect installed values and actual setter/override order when source access returns; do not substitute archive defaults.
