# TASK-01 — Native tasks dialogue and info state

> ADR document set: **v0.1.80**. Research revisions and source/build versions below describe their original scope.

- ID: TASK-01
- Subsystem: tasks/dialogue/info state
- ADR revision: v0.1.68
- Record status: complete-within-scope
- Source status: source-confirmed selected native/Lua/persistence paths
- Runtime status: untested; deferred
- Baseline/provenance: ENGINE1011; [source record](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-12

## Question and scope

Trace selected task grant/state/predicate/action and save-load, actor/owner info transfer/query/storage, and dialogue helper/caller conditions/actions. Inventory prior UI/persistence/CtZ coverage first. Exclude full supplied/effective reward/restore scripts, conversation UI/session internals, every branch/build/converter and runtime/game changes.

## Evidence and method

[T01–T18 ledger](../../evidence/tasks/native-task-dialogue-info-2026-10-12.csv) pins files/ranges/symbols/full-file hashes. Archive SHA-256 14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee; installed/build correspondence unknown. Read bodies/declarations/registration and caller order; distinguish active CInfoPortion from commented legacy and task saved fields from live vectors.

## Findings

[Reference](../../04-game-systems/tasks/native-task-dialogue-info.md) maps task duplicate/time/fail-first predicates, terminal side effects before callbacks, actor-global helper info checks, overload-dependent dialogue action order, local-plus-event info transfer, and native task reconstruction limits. [API page](../../02-lua-api/tasks/native-task-info-api.md) retains task adoption/void return and info boolean meanings. [Central guide](../../04-game-systems/tasks/development-reference.md) remains explicitly in-progress.

## Competing explanations and missing edges

Winning scripts may reconstruct omitted info lists or implement rewards/mission state separately. Native task action bool results are ignored; dialogue invocation catch does not roll back transferred info. Missing functors and map reconstruction have their own guards. Runtime, actor/UI readiness and effective Lua dispatcher/conditional configuration remain unresolved. No unused CtZ dynamic text is assumed implemented because native support exists.

## Checks and outcomes

Hash/count/range/cited-symbol and declaration/registration/order comparison; repository/existing regression checks; preserve prior evidence/history/generated outputs and dated records. [Verification](../verification-2026-10-12-v0.1.68.md). No independent game/engine runtime.

## Disposition and next work

Selected TASK-01 native foundation complete within scope; subsystem partial. Next supplied-consumer/effective-gap pass and reward/restoration chains, then consolidation/audit. [Roadmap](../../ROADMAP.md).
