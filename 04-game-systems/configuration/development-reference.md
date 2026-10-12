# Configuration and script integration development reference

> ADR document set: **v0.1.74**. Research revisions and source/build versions below describe their original scope.

- ID: CONFIG-01-GUIDE
- Subsystem: configuration/script integration
- Research revision: v0.1.74
- Record status: complete-within-scope (inventory only); subsystem partial
- Source status: scoped-source-audit of existing ADR documentation
- Runtime status: untested; deferred
- Baseline: ADR v0.1.73 main `6327645f473774753964454c79beabe4f4c2c716`; linked records retain their original baselines
- Last reviewed: 2026-10-12

The [existing-coverage inventory](coverage-inventory.md) is complete within scope. Shared native configuration/script contracts remain partial; this guide currently connects established records and the next investigation boundaries. It is not a certified configuration recipe.

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

## Current stopping rule

CONFIG-01 closes the inventory only. Next CONFIG-02 traces LTX/INI and selected DLTX contracts; CONFIG-03 then connects native loading/startup/callbacks; CONFIG-04 traces selected supplied options/patching and consolidates/audits. [Source status](source-completion-status.md), [evidence](../../evidence/configuration/README.md). No new API page or runnable recipe is introduced before its implementation/export/ownership chain is traced. Runtime remains deferred.
