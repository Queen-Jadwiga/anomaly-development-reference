# Configuration/script integration source completion

> ADR document set: **v0.1.80**. Research revisions and source/build versions below describe their original scope.

- ID: CONFIG-STATUS
- Subsystem: configuration/script integration
- Research revision: v0.1.77
- Record status: planned available-source pass complete-within-scope; effective integration partial
- Source status: documentation inventory plus selected native/supplied contracts confirmed
- Runtime status: untested; deferred
- Baselines: CONFIG-01 ADR v0.1.73 pin; ENGINE1011/BETA150/ZIP142 via [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Completed selected scope

| Work | Canonical reference | Boundary |
| --- | --- | --- |
| CONFIG-01 inventory | [18 pinned documentation rows](coverage-inventory.md) | Original hashes/sections preserved; later five-event correction explicit |
| CONFIG-02 LTX/INI/DLTX | [Behavior](ltx-ini-dltx.md), [INI API](../../02-lua-api/configuration/ini-api.md) | Selected parser/export/converter/lifetime paths |
| CONFIG-03 loading/startup/callbacks | [Behavior](script-loading-startup-callbacks.md), [API](../../02-lua-api/configuration/script-callback-api.md) | Selected shared/helper/debug-global contracts; missing effective core routing retained |
| CONFIG-04 consumers | [Options/patches](supplied-options-patches.md), [API](../../02-lua-api/configuration/options-patch-api.md) | Selected menu/preset/cache/refresh/builder/wrapper/unlocalizer chains and variants |
| Consolidation/bounded audit | [Guide](development-reference.md), [v0.1.77 audit](../../08-research/verification-2026-10-12-v0.1.77.md) | 114 source rows/156 ranges, original inventory pins, comparison/scope/preservation/navigation |
| Effective integration | Partial | Winning inputs and executed wrapper/consumer/restore chain unknown |
| Independent runtime | Untested; deferred | No compatibility, timing, reload or recovery certification |

## Effective-source requirements

| Input needed | Closure required |
| --- | --- |
| Winning _G/global/core class/exec helpers, script.ltx and configured startup callback | Native initialization → actual globals/module handlers; final Register/Send/Unregister route |
| Winning UI definitions/current axr/localization/preset/include resources and optional selection | Exact path/type/current/default, include completeness, edit/apply/write/command/change and consumer behavior |
| Executable/build/debug/cache configuration, virtual-view conflict records and packed resources | Uploaded-source equivalence, actual native inputs and supplying-mod winners |
| Later modules, original captures, directives and binders | Effective wrapper layers, repeated-install guards, listener identity and object lifetime |
| Domain manager/storage/restore emitters and copied consumer state | Refresh/reconstruction across different owners; retain each subsystem's unresolved edges |

[WAR-002a virtual-view requirements](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md) remain authoritative. Current scopes positively identify engine extensions/axr_main and supplied ui_options. Requested-filename absence in an addon is not installed absence; partial preset include files require effective base/other resources. A mod list alone does not establish executed order.

## Completion and stopping rule

The planned available-source pass closes after selected implementation/export/caller, state/lifetime/error/reset/precedence contracts are linked and audited. Effective integration closes only when relevant winning chains/inputs are reconciled. Shared integration research does not implement absent manager/binder/storage behavior or certify compatibility by assembling alternative packages.

Runtime is a separate explicitly resumed phase with executable/profile provenance, repeatable observations/logs and actual outcomes; it remains deferred. Exhaustive option/VM/parser/addon combinations, full MCM and broad MO2 internals remain optional depth. [ARCH-01 practical inventory](../../05-mod-architecture/coverage-inventory.md) is complete within scope; next ARCH-02 module/state ownership and compatibility contracts. [Guide](development-reference.md), [roadmap](../../ROADMAP.md).
