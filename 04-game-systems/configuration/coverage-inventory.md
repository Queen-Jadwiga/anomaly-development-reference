# Configuration/script integration coverage inventory

> ADR document set: **v0.1.83**. Research revisions and source/build versions below describe their original scope.

- ID: CONFIG-01
- Subsystem: configuration/script integration
- Research revision: v0.1.74
- Record status: complete-within-scope (inventory only); subsystem partial
- Source status: scoped-source-audit of existing ADR documentation
- Runtime status: untested; deferred
- Baseline: ADR v0.1.73 main `6327645f473774753964454c79beabe4f4c2c716`; linked records retain their original baselines
- Last reviewed: 2026-10-12

This inventory classifies selected existing records before new native tracing. It does not revalidate every source claim, certify an INI API or establish installed behavior. [Pinned 18-row documentation ledger](../../evidence/configuration/coverage-inventory-2026-10-12.csv), [investigation](../../08-research/investigations/2026-10-12-CONFIG-01-existing-coverage.md), [verification](../../08-research/verification-2026-10-12-v0.1.74.md).

## Existing coverage and missing edges

| Area | Existing coverage | Canonical reference | Missing edge / next trace |
| --- | --- | --- | --- |
| K01 — Native settings producers and consumers | selected-contract | [configuration-controls](../../04-game-systems/alife/configuration-controls.md) | Trace general pSettings construction and lifetime; do not repeat selected A-Life algorithms. |
| K02 — General LTX/INI load and read semantics | outside-reviewed-closure | [configuration-controls](../../04-game-systems/alife/configuration-controls.md) | Trace includes/inheritance, duplicates, missing sections/keys, typed reads, mutation/save and Lua ownership/export contracts. |
| K03 — DLTX and compatibility packaging | plan-only | [README](../../05-mod-architecture/README.md) | Trace available native patch discovery/application and interactions with ordinary includes/inheritance; keep MO2 winner separate. |
| K04 — Package variants and effective file precedence | selected-provenance | [2026-10-11-WAR-002a-source-packages-effective-profile](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md) | Trace only relevant available filesystem resolution; retain missing winning-file/conflict records and packed-core dependencies. |
| K05 — Options aliases and change listeners | selected-consumer | [policy-controls](../../04-game-systems/warfare/policy-controls.md) | Trace option definition/current/default storage and change emission; distinguish reads from refreshing all consumers. |
| K06 — Presets and exact option keys | selected-consumer | [supplied-consumers](../../04-game-systems/world/supplied-consumers.md) | Trace preset include/load/current/default order and cache commit; no invented alias or installed setting. |
| K07 — Native script loading and namespace resolution | outside-reviewed-closure | [script-interfaces](../../02-lua-api/alife/script-interfaces.md) | Trace script-engine initialization, autoload, .script/.lua selection, namespace/function lookup, caching/reload and failures. |
| K08 — Root script startup loop and standalone Lua namespace | selected-caller | [supplied-consumers](../../04-game-systems/world/supplied-consumers.md) | Connect native initialization to global wrappers and axr_main startup; trace discovery, execution/reentry and readiness gates. |
| K09 — Listener ordering and dispatch | selected-contract | [callback-phase-reference](../../04-game-systems/alife/callback-phase-reference.md) | Extend registration/removal validation, mutation/reentry/error and return/argument contracts where not already traced. |
| K10 — Global callback wrappers and DXML registration | selected-bridge | [xml-dxml-callback-errors-ui04b-oct11](../../03-ui-pda/xml-dxml-callback-errors-ui04b-oct11.md) | Establish selected global population/caller route and forced registration interactions; installed wrappers remain unknown. |
| K11 — Module assignments and monkey patches | catalog-plus-selected-behavior | [script-interfaces](../../02-lua-api/alife/script-interfaces.md) | Trace selected top-level versus startup patches, captured originals, unlocalizers and later replacements. |
| K12 — XML includes, resource selection and interception | selected-contract | [xml-loading-paths-ui04a-oct11](../../03-ui-pda/xml-loading-paths-ui04a-oct11.md) | Link UI as canonical; compare LTX/DLTX routing without transferring XML rules to INI. |
| K13 — DXML errors and cache lifetime | selected-contract | [xml-dxml-callback-errors-ui04b-oct11](../../03-ui-pda/xml-dxml-callback-errors-ui04b-oct11.md) | Trace only missing shared-dispatch/cache reset dependencies; exhaustive XML/error propagation remains optional. |
| K14 — Condition-list effects and variant returns | selected-consumer | [supplied-task-dialogue-consumers](../../04-game-systems/tasks/supplied-task-dialogue-consumers.md) | Link existing task evidence; trace winning parser/helper/namespace startup boundaries without recertifying reward delivery. |
| K15 — Named script callbacks in configured dialogue | selected-contract | [native-task-dialogue-info](../../04-game-systems/tasks/native-task-dialogue-info.md) | Connect general functor resolution to existing task/dialogue contracts; avoid repeating their state/lifecycle trace. |
| K16 — Shared persistence callbacks and binder storage | selected-caller-plus-effective-gap | [lua-storage-contracts](../../04-game-systems/persistence/lua-storage-contracts.md) | Reuse persistence evidence; identify shared startup/dispatcher dependencies without claiming missing encoding/storage implementation. |
| K17 — Build differences and external observations | qualified-comparison | [2026-10-12-REV-01-external-runtime-issues](../../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md) | Preserve baseline-specific arity/order and external-observation confidence; no new runtime conclusion. |
| K18 — Economy options and captured replacement | selected-consumer | [trader-configuration](../../04-game-systems/economy/trader-configuration.md) | Compare selected option producers/caches and replacement installation phases; preserve economy accounting/refresh scope. |

Labels classify the pinned records, not all upstream code. `outside-reviewed-closure` means the selected records do not establish the general chain; `plan-only` is an unfulfilled outline. A selected caller or catalog cannot certify its missing callee. Repeated canonical documents cover separate boundaries rather than distinct source implementations. Every row retains its original source/runtime confidence.

## Reuse and completion boundary

Keep domain policy in A-Life/Warfare, economy, tasks, persistence and world; keep XML/DXML routing and UI resource rules in UI/PDA. New configuration work owns shared parsing, loading, lookup, registration, option and patch-installation contracts, linking these domain consumers. Do not duplicate ledgers or convert earlier schemas. Presets/defaults are not effective values; filenames/declarations are not execution; registration success is not entity readiness; a listener order is not native lifecycle order.

## Bounded follow-on sequence

1. **CONFIG-02 — LTX/INI and selected DLTX contracts:** settings roots/lifetime, include and inheritance processing, patch discovery/application and precedence, section/key/read/default/error rules, selected writes/save, Lua registrations/converters/ownership. Reuse XML/DXML and existing domain consumers; do not infer MO2 precedence from native parsing.
2. **CONFIG-03 — script loading, startup and shared callbacks:** native initialization/autoload and namespace/function lookup, root startup discovery, global wrapper population, registration/removal, priorities/dependencies, arguments/returns, dispatch mutation/reentry/error and cache/reload boundaries. Reuse ALIFE-10 and preserve September/October differences.
3. **CONFIG-04 — supplied options/patch consumers, consolidation and bounded audit:** selected defaults/current/preset/cache/change chains; top-level/startup replacements and captured originals; relevant unlocalizers and available file-resolution boundaries. Consolidate practical guidance and audit the new contracts with reused records. Keep absent effective storage/managers/binders and installed winners open. Split if tracing volume warrants it.

ENGINE1011 path-presence searches locate `src/xrCore/Xr_ini.cpp`, `xr_ini.h`, `LocatorAPI.cpp`, `src/xrServerEntities/script_ini_file.cpp`, `script_ini_file_script.cpp`, `script_ini_file_inline.h`, `script_engine.cpp`, `script_engine_inline.h`, `script_storage.cpp`, and bundled `axr_main.script`, `_g_patches.script`, `dxml_core.script`, `dynamic_callbacks.lua`, `options_builder.script` and `ui_options_modded_exes.script`. WORLD-04 already pins selected BETA150/ZIP142 `ui_options`/preset callers. These are trace candidates, not newly certified contracts. Locate DLTX implementation through parser dependencies rather than assuming a standalone filename. Exact upstream commit/executable equivalence and installed overrides remain unknown.

All-option tuning advice, full MO2 internals, every filesystem consumer, arbitrary addon stacks, exhaustive Lua VM/Luabind error propagation and unrelated multiplayer remain optional depth unless a concrete integration question requires them. [Central guide](development-reference.md), [completion rule](source-completion-status.md), [roadmap](../../ROADMAP.md).

## CONFIG-03 amendment — 2026-10-12

CONFIG-03 now traces selected loading/startup/dispatch contracts and corrects K08's inherited six-name wording to five. The [original pinned ledger](../../evidence/configuration/coverage-inventory-2026-10-12.csv) remains unchanged; the new [source reference](script-loading-startup-callbacks.md) establishes the conditional debug-global loader and retains effective alias uncertainty. The bounded plan above records CONFIG-01's original allocation; current progress is in [completion status](source-completion-status.md).
