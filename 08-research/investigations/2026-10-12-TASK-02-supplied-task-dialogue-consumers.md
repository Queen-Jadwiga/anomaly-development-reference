# TASK-02 — Supplied task dialogue reward and restoration consumers

> ADR document set: **v0.1.75**. Research revisions and source/build versions below describe their original scope.

- ID: TASK-02
- ADR/research revision: v0.1.69
- Record status: complete-within-scope
- Source status: selected supplied consumers confirmed; effective installation partial
- Runtime status: untested; deferred
- Baselines: BETA150 main and ZIP142; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and method

Trace available offer/description/setup/grant/stage/turn-in/cancel and reward/restoration callers against TASK-01. Read relevant bodies and task configuration, compare two supplied snapshots, search selected main package for expected core files/definitions, and follow explicit call boundaries. No online claims, effective installation assumptions or runtime execution.

## Findings and evidence

[L01–L16](../../evidence/tasks/supplied-consumers-2026-10-12.csv) pins raw-file hashes/counts and cited ranges/symbols. [Reference](../../04-game-systems/tasks/supplied-task-dialogue-consumers.md) records description side effects, stage-versus-terminal distinctions, sequential reward wrappers, missing reward/manager/storage definitions, saved selection versus local cache/tsk state, offline listener restoration and BETA150's return-dependent double invocation versus ZIP142's single invocation.

Four relevant source/config files are byte-identical across these snapshots; xr_logic has the isolated dispatch change. The 89-section task file contains no active smart_control reference. Smart-control cache-index and boolean-ID discrepancies remain source candidates with use/runtime unproven. Non-UTF8 dialog bytes were read using cp1251 for inspection; hashes use unchanged raw bytes, and no third-party code is copied into the ADR.

## Limits and disposition

Missing core/winning managers, helpers, binders, dispatcher, XML/info/task include roots and installation/build correspondence prevent reward atomicity/deduplication, whole restoration or consumer activity certification. Available caller tracing is complete within scope; no guessed reward behavior fills these gaps. Proceed to TASK-03 practical consolidation/audit. [Completion status](../../04-game-systems/tasks/source-completion-status.md). Runtime stays deferred.
