# Configuration and script integration development reference

> ADR document set: **v0.1.76**. Research revisions and source/build versions below describe their original scope.

- ID: CONFIG-01-GUIDE
- Subsystem: configuration/script integration
- Research revision: v0.1.76
- Record status: inventory and selected CONFIG-02/03 contracts complete within scope; subsystem partial
- Source status: existing documentation inventory plus selected source-confirmed ENGINE1011 contracts
- Runtime status: untested; deferred
- Baselines: CONFIG-01 pins ADR v0.1.73 main `6327645f473774753964454c79beabe4f4c2c716`; CONFIG-02/03 use ENGINE1011 via [manifest](../../evidence/manifest.md); linked records retain their original baselines
- Last reviewed: 2026-10-12

The [existing-coverage inventory](coverage-inventory.md) is complete within scope. CONFIG-02 [LTX/INI/DLTX contracts](ltx-ini-dltx.md) and [Lua INI API](../../02-lua-api/configuration/ini-api.md) are now complete within selected source scope. CONFIG-03 [script loading/startup/shared callback contracts](script-loading-startup-callbacks.md) are complete within selected source scope; effective integration remains partial; this guide connects established records and the next investigation boundaries. It is not a certified configuration recipe.

## Choose the layer before changing a value or hook

| Question | Start with | What still needs proof |
| --- | --- | --- |
| What value reaches a native A-Life consumer? | [Native controls](../alife/configuration-controls.md) | Winning settings root, section/value, read point and later setters |
| Does a Warfare menu change refresh policy? | [Policy controls](../warfare/policy-controls.md), [world option keys](../world/supplied-consumers.md) | Current/default/preset storage, change emission and every relevant cache |
| Which script body is effective? | [Package/profile boundary](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md), [interface map](../../02-lua-api/alife/script-interfaces.md) | Winning file, module evaluation, startup call and subsequent replacements |
| What does a callback establish? | [Callback phases/order](../alife/callback-phase-reference.md) | Effective wrapper/emitter, arguments/return consumption, object phase and listener mutation |
| Which XML text receives a patch? | [XML routes](../../03-ui-pda/xml-loading-paths-ui04a-oct11.md), [DXML errors/order](../../03-ui-pda/xml-dxml-callback-errors-ui04b-oct11.md) | Resolved filename, callback/cache lifetime and installed patch stack |
| Does a configured name execute once or persist? | [Task consumers](../tasks/supplied-task-dialogue-consumers.md), [storage contracts](../persistence/lua-storage-contracts.md) | Winning dispatcher/helper return, serialization/reset and failure path |

An integration trace needs the producer, selected input/file, parsing or lookup stage, state owner, read/refresh point, consumer and failure/lifetime boundary. This is a research checklist inferred from the linked records, not a runtime-tested workflow. Preserve literal identifiers and separate module evaluation, startup, event dispatch and load restoration.

## Apply the selected configuration contracts

Trace the resolved value through [parser stages](ltx-ini-dltx.md) before choosing a setting. Scalar collisions use depth/insertion filtering and override merge; list edits use a separate collected insertion order; parents and post-evaluation section deletion add further boundaries. Preserve an empty value separately from missing/deleted keys, and a helper default separately from native conversion failure.

The [Lua API](../../02-lua-api/configuration/ini-api.md) specifies constructor arity and BOOL flag conversion, existing-key writer checks and borrowed/owned pointer lifetime. A reload can invalidate handles without refreshing consumer fields. A save emits resolved plain data; metadata diagnostics do not reconstruct all source contributors. These are source-derived decisions, not a tested live-reload or tuning recipe. CONFIG-03 establishes selected loading/dispatcher definitions and conditional debug-global routing; CONFIG-04 still needs supplied option/preset/cache/change and patch-consumer tracing. Effective global helpers/emitters and later startup replacements remain open.

## Distinguish loading, registration and dispatch

[CONFIG-03](script-loading-startup-callbacks.md) separates module table existence from completed chunk execution, module evaluation from the startup-handler pass, and listener ordering from native lifecycle readiness. Registry constraints use exact identities; removal of a listener does not clear every retained closure or native alias. The supplied iterator snapshots keys while priorities remain live, and dispatch ignores returns without per-listener protection/reentry guards.

The debug-enabled native route can install a separate five-event global dispatcher before later core/module assignments. Establish the winning Register/Send/Unregister route together before relying on axr_main tiers. This is source-derived guidance; installed wrappers, configured startup body, restored state and actual timing remain open.

## Current stopping rule

CONFIG-01 closes the inventory only. CONFIG-02 now traces selected LTX/INI/DLTX; CONFIG-03 now connects selected native loading/startup/callbacks; next CONFIG-04 traces supplied options/patching and consolidates/audits. [Source status](source-completion-status.md), [evidence](../../evidence/configuration/README.md). No new API page or runnable recipe is introduced before its implementation/export/ownership chain is traced. Runtime remains deferred.
