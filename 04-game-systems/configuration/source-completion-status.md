# Configuration/script integration source completion

> ADR document set: **v0.1.74**. Research revisions and source/build versions below describe their original scope.

- ID: CONFIG-STATUS
- Subsystem: configuration/script integration
- Research revision: v0.1.74
- Record status: partial
- Source status: scoped-source-audit of existing ADR documentation
- Runtime status: untested; deferred
- Baseline: ADR v0.1.73 main `6327645f473774753964454c79beabe4f4c2c716`; linked records retain their original baselines
- Last reviewed: 2026-10-12

## Current scope

| Work | Status | Boundary |
| --- | --- | --- |
| CONFIG-01 existing coverage | Complete within scope | 18 selected pinned documentation rows; inherited confidence, no new native closure |
| CONFIG-02 LTX/INI and selected DLTX | Open | Parsing/patch order, reads/defaults/errors, settings lifetime, Lua exports/ownership |
| CONFIG-03 native script loading/startup/callbacks | Open | Namespace lookup, execution/cache/reset, global bridges, registration/removal/dispatch contracts |
| CONFIG-04 supplied options/replacements and audit | Open | Selected current/default/preset/cache/change consumers, installation phases, practical synthesis and bounded audit |
| Effective installed integration | Partial | Winning inputs/profile, wrappers, later patches, build flags and core dependencies |
| Independent game runtime | Untested; deferred | No engine/game test or installed compatibility result in this increment |

## Required effective inputs

Collect relevant winning scripts including global wrappers, dispatch/startup, options/preset loaders and later differently named patches; relevant LTX/include/DLTX and XML resources; conflict/supplying-mod records from the active virtual view; packed-core dependencies and executable/build identity. Existing [WAR-002a provenance requirements](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md) remain authoritative. Prior package inventories identify scoped absences only; ENGINE1011 axr_main and supplied ui_options are available and must not be called absent wholesale.

## Completion and stopping rule

The available-source foundation closes after CONFIG-02–04's selected implementation/export/caller, ownership/failure/reset and precedence boundaries are traced, linked and audited. Effective integration closes only when relevant winning source chains and inputs are reconciled; collecting a mod list alone does not close execution order. Preserve missing core manager/binder/storage edges in their owning subsystems rather than pretending shared startup research implements them.

Independent runtime remains a separate explicitly resumed phase with executable/profile provenance, repeatable observations and logs. Exhaustive parser/VM/filesystem/addon combinations and every option are optional later depth. [Inventory](coverage-inventory.md), [guide](development-reference.md), [roadmap](../../ROADMAP.md).
