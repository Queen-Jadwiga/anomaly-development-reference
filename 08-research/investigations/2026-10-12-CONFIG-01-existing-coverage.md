# CONFIG-01 — Existing configuration/script integration coverage

> ADR document set: **v0.1.74**. Research revisions and source/build versions below describe their original scope.

- ID: CONFIG-01
- Subsystem: configuration/script integration
- ADR revision: v0.1.74
- Record status: complete-within-scope (inventory only); subsystem partial
- Source status: scoped-source-audit of existing ADR documentation
- Runtime status: untested; deferred
- Baseline: ADR v0.1.73 main `6327645f473774753964454c79beabe4f4c2c716`; linked records retain their original baselines
- Last reviewed: 2026-10-12

## Question and scope

Which configuration/script integration mechanisms already have bounded ADR coverage, which are adjacent/catalog/plan-only, and what shared contracts need investigation next? Inventory selected A-Life/Warfare controls, UI XML/DXML, script interfaces/callback phases, task/dialogue/effect dispatch, persistence, economy/world callers and package/profile requirements. Completion requires canonical links, pinned reviewed sections, retained confidence and a bounded next sequence. It does not require new API certification or runtime.

## Evidence and method

The [18-row documentation ledger](../../evidence/configuration/coverage-inventory-2026-10-12.csv) pins raw file hashes and inclusive section ranges/markers at the declared immutable ADR v0.1.73 commit. Search terms included ini_file, system_ini, pSettings, include, configuration, DLTX, MCM, on_game_start, callback, load/script, override and winner. Read selected sections and relevant original scope/ledgers; classify established contracts rather than count name occurrences. No earlier ledger/schema is migrated or native source conclusion recertified.

ENGINE1011 candidate path searches locate parser, Lua INI exports, native script-engine/storage and bundled startup/options/dispatcher files listed in the [inventory](../../04-game-systems/configuration/coverage-inventory.md). Presence/search targets do not certify exports, execution or precedence. Linked records retain ENGINE1011/BETA150/ZIP142 and separately pinned upstream/external-report provenance; exact uploaded-source upstream commit and installed executable/profile equivalence remain unknown.

## Findings

K01–K06 show selected native setting consumers, package provenance and supplied option/preset paths, while the general LTX/INI/DLTX pipeline remains outside reviewed closure. K07–K11 distinguish native module loading, selected root startup callers, shared listener ordering, global bridges and replacement declarations. K12–K13 retain established XML-specific routing/error/cache contracts. K14–K18 reuse task effect variants, native named dialogue calls, persistence gaps, baseline-specific dispatch differences and economy replacement/option consumers. See each canonical section and retained boundary in the [inventory table](../../04-game-systems/configuration/coverage-inventory.md).

Preserve domain policy in existing subsystems. Trace shared settings parsing first (CONFIG-02), native script loading/startup/callback contracts second (CONFIG-03), then supplied options/patch-installation consumers and consolidation/audit (CONFIG-04). Split the later passes if source volume requires it. No new runnable recipe is justified by this inventory.

## Competing explanations and missing edges

Existing named settings, an INI export occurrence, a priority algorithm or an on_game_start declaration may look like full integration coverage. These records do not establish general parser defaults/errors, namespace loading, registration/reset/removal, complete option refresh or final installed replacement order. Conversely, a missing closure in selected documents is not missing upstream functionality. The mod architecture page is an outline; DLTX and MO2 precedence cannot be promoted from that plan. XML include/hook rules cannot be transferred to LTX.

ENGINE1011 axr_main and supplied ui_options are already available; missing effective wrappers/storage/managers/configuration remain scoped dependencies, not a claim that every core source is absent. External observations and September/October dispatcher differences retain their separate confidence axes. Registration/lookup/readiness and native lifecycle/listener order remain distinct.

## Checks and outcomes

Validate all 18 raw document hashes and cited section markers/ranges against the v0.1.73 base, review classifications/step allocations, preserve prior evidence/history/generated/tool/test bytes and dated investigation bodies except current banners, and run repository checks plus existing regressions. Compare complete remote base/staged/published path/blob maps. [Verification](../verification-2026-10-12-v0.1.74.md). No engine compilation, independent game test, source/assets redistribution or CtZ gameplay changes.

## Disposition and next work

CONFIG-01 is complete within the documentation-inventory scope; the subsystem remains partial. **Next: CONFIG-02 — LTX/INI and selected DLTX contracts.** [Guide](../../04-game-systems/configuration/development-reference.md), [completion rule](../../04-game-systems/configuration/source-completion-status.md), [roadmap](../../ROADMAP.md).
