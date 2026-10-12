# Configuration and script integration development reference

> ADR document set: **v0.1.82**. Research revisions and source/build versions below describe their original scope.

**Current cross-system status:** [ADR-01 whole-reference audit](../../08-research/reference-status.md) is complete within scope. Original research allocations/baselines below remain dated; selected foundations are consolidated, effective installed integration stays partial and runtime verification deferred.

- ID: CONFIG-01-GUIDE (stable central-guide identity)
- Subsystem: configuration/script integration
- Research revision: v0.1.77
- Record status: planned available-source CONFIG-01–04 complete within selected scope; effective integration partial
- Source status: scoped documentation inventory plus selected source-confirmed native/supplied contracts
- Runtime status: untested; deferred
- Baselines: CONFIG-01 ADR v0.1.73 documentation pin; CONFIG-02/03 ENGINE1011; CONFIG-04 ENGINE1011/BETA150/ZIP142 via [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

This guide consolidates [LTX/INI/DLTX](ltx-ini-dltx.md), [loading/startup/callbacks](script-loading-startup-callbacks.md) and [supplied options/patch consumers](supplied-options-patches.md). The [bounded audit](../../08-research/verification-2026-10-12-v0.1.77.md) checks 114 source rows/156 cited ranges, the original 18 documentation pins and new qualified package comparisons. It is not installed compatibility or runtime certification. [Completion status](source-completion-status.md), [evidence](../../evidence/configuration/README.md).

## Choose the state owner and operation

| Need | Start with | Keep separate |
| --- | --- | --- |
| Explain a final LTX value | CONFIG-02 parser stages and final item metadata | Native file enumeration, DLTX resolution and MO2 supplying-mod winner |
| Read/write an INI | [INI API](../../02-lua-api/configuration/ini-api.md) | Existing/empty/missing key, helper default, copied consumer field and game-save state |
| Load/call a module | CONFIG-03 environment/autoload/lookup | Namespace existence, chunk completion, startup handler and native readiness |
| Install/remove a callback | [Callback API](../../02-lua-api/configuration/script-callback-api.md) | Exact identity, one-event ordering, lifecycle emission and object lifetime |
| Apply a menu option | [Option API](../../02-lua-api/configuration/options-patch-api.md) | Persistent input, pending/backup, current/default, console and consumer copies |
| Install a wrapper | CONFIG-04 captured-original trace | Evaluation, handler installation, repetition, later replacement and restoration |
| Reconstruct durable state | [Persistence](../persistence/development-reference.md) | INI/cfg output, module tables/closures, native packets and campaign storage |

Identify the actual producer/input, implementation, state owner, read/apply point, failure result and later consumer. This is source-derived guidance, not a tested live-reload, patch or tuning recipe. Domain controls remain canonical in [A-Life](../alife/configuration-controls.md), [Warfare](../warfare/policy-controls.md), [economy](../economy/trader-configuration.md), [tasks](../tasks/supplied-task-dialogue-consumers.md) and [world](../world/supplied-consumers.md). XML/DXML retains its [UI rules](../../03-ui-pda/xml-loading-paths-ui04a-oct11.md).

## Configuration values and handles

Includes increment depth; named roots discover selected mod files at EOF. Scalar collisions use lower depth/later insertion within base/override data, then override merge. Parent resolution, list edits and post-evaluation section deletion have separate order. Empty, missing and deleted values differ. Lists append without deduplication and remove exact matches; filename metadata is not complete contributor history. CONFIG-02 N06–N22/N28.

Native filename cache, instance DATA, script memoization and consumer copies are different owners. Mutation does not automatically invalidate the native cache; invalidation does not reload objects or refresh all consumers. Saving emits resolved plain data rather than preserving include/inheritance/DLTX structure. CONFIG-02 N02–N04/N22/N26; CONFIG-04 E05–E09.

Use exact registered arities/converters: C++ defaults/null branches do not add Lua overloads; preserve BOOL integer flags and r_line in-out placeholders. Native loose numeric reads differ from Lua defaults; helper empty-bool/default forwarding differences remain explicit. Higher-level default writes do not bypass the native-derived writer's existing-key checks. Borrowed settings pointers and owned factory/constructor userdata differ; reload destroys old system state, while close does not clear owned-finalizer aliases. Neither is a certified generic cleanup/reload protocol. CONFIG-02 A01–A20/S01/S02; CONFIG-04 B03/E05/E06.

## Evaluation, startup, dispatch and readiness

Ordinary autoload uses .script and can skip a table left by partial execution. Prefetch has no success receipt/reload flag. VM reconstruction, module reload and stack unload are separate operations. The configured native startup callback precedes the selected simulator load; missing core/global/configuration inputs keep its effective handler route open. Root discovery can evaluate dependencies before the later startup-handler pass. DXML registration is another route. Filename order does not establish final replacements or readiness. CONFIG-03 N01–N21/S08/S12/S13.

Establish effective Register/Send/Unregister together: the conditional five-event debug-global dispatcher is separate from axr_main. Exact listener identity, tier/dependency ordering, registration rejection and userdata-specific unsetting have separate contracts. Dispatch ignores returns, shares mutable arguments and has no local per-listener protection/reentry guard. The supplied iterator snapshots keys while values/priorities remain live; mutation is not frozen-order dispatch. Priority cannot move an event past native work that follows its emitter. CONFIG-03 S01–S11/N04/N17/N22; [A-Life phases](../alife/callback-phase-reference.md).

## Options and patch installation

Direct get can persist defaults and prioritizes stored config; UI current lookup has a distinct pending/curr/console/config chain. Presets stage values with exact conversion, while CacheValue does not commit or universally validate. Accept applies sequential writes/functors/commands/saves and a gated event; direct set does not emit that event. Cancel and discard have different cache behavior. Warfare refresh replaces its faction table rather than retargeting old references. Matching optional menu methods does not equate declarations, defaults or installed winners. CONFIG-04 B01–B14/P01/P02.

Trace original capture per installation versus shared module slots. Trade evaluation capture, binder startup layers, option registration slots and dynamic-item startup slots have different repetition behavior. The two mutable-slot examples can self-reference when installed again in the same module instance; a resolution guard after the original call does not prevent it. These conditional source hazards are not observed profile failures. Builders mutate input/metatable state; unlocalizers preprocess selected declarations before execution. CONFIG-04 E01–E12/N01.

## Stopping rule and next foundation

CONFIG-01–04 planned available-source inventory/contracts/consumers/consolidation/audit are complete within scope. Winning configuration/global/class/exec/storage/binder inputs, startup/patch caller order, native/cache/debug identity and effective consumer refresh/restoration remain partial under the [completion rule](source-completion-status.md). Runtime remains deferred.

Next: **practical architecture/debugging, beginning with existing-coverage inventory**. All-option tuning, every VM/parser/filesystem/addon/control combination, full MCM and broad MO2 internals remain optional depth unless a concrete question requires them. [Roadmap](../../ROADMAP.md).

Current navigation: [ARCH-02 ownership](../../05-mod-architecture/module-state-contracts.md) and [compatibility/package contracts](../../05-mod-architecture/compatibility-package-contracts.md) are complete within selected synthesis scope. [DEBUG-01 diagnostic routes/triage](../../06-debugging/README.md) are now complete within selected source scope. ARCH-03 [practical consolidation](../../05-mod-architecture/development-reference.md), [patterns](../../07-code-library/qualified-patterns.md) and [bounded audit](../../08-research/verification-2026-10-12-v0.1.81.md) now complete the selected foundation. Next separate whole-ADR audit; effective integration partial and runtime deferred. The stopping-rule paragraph above retains the CONFIG-04 research allocation.
