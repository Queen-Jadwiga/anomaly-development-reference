# WAR-003 — Supplied Warfare configuration and policy controls

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

- ID: WAR-003
- Subsystem: Warfare / A-Life integration
- ADR revision: v0.1.43
- Record status: complete-within-scope
- Source status: source-confirmed for selected consumers; scoped-source-audit for negative searches
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline IDs and provenance record: BETA150; [package provenance](2026-10-11-WAR-002a-source-packages-effective-profile.md)
- Last reviewed: 2026-10-11

## Question and scope

Which supplied package controls feed selected targeting, capture, ownership, offline combat and online-status policy, and how do options, local snapshots, clocks and optional declaration defaults differ?

Include BETA150 main options/Warfare/smart/offline-combat consumers, selected main preset/include/configuration sections, and separately labeled optional GAMMA-patch UI/configuration declarations. Exclude full preset loader/option-storage implementation, every option/consumer, installed winners/values, creature/board/safe-release internals, gameplay changes and runtime tests. Completion requires a scoped control map and explicit unresolved refresh/order boundaries.

## Evidence and method

Archive SHA-256 `withheld-upload-fingerprint`. [Ledger W01–W18](../../evidence/warfare/configuration-controls-2026-10-11.csv) names each main or optional-patch path; 18 entries over nine files use the current evidence schema. Labels are local and do not refer to WAR-002's older W-ledger.

Read settings producer, startup/option subscription, coordinator, distance/power consumers, capture methods, selected defense timers, target scoring, owner policy and optional UI/default/preset declarations. Search the complete main `sim_offline_combat.script` for `COMBAT_DISTANCE_WARFARE` and `offline_health`; trace active `init_settings` sections and retain the prior scoped `override_functions` caller limitation. Verify paths/hashes/ranges/symbols against the supplied package.

## Findings

The [Warfare policy-control reference](../../04-game-systems/warfare/policy-controls.md) provides consumer mappings and qualified defaults.

- `update_settings` populates general/faction tables and aliases. Warfare startup calls it; options startup subscribes it to `on_option_change`. These producer hooks do not establish installed relative listener order. W01/W02.
- Offline mode is a direct coordinator read of `alife/general/offline_combat`; older similarly named Warfare option reads are commented out. The Warfare radius local is computed once at module initialization and reused later; a full-file search finds no recomputation assignment in that file. W01/W03/W04.
- Coordinator copies faction multipliers and selects event subscriptions; NPC/squad power calculation is an abstraction and can use cached squad power. These are distinct refresh points. W04/W06.
- Old/new capture routes both use game-minute scale but differ in rounding, stages and spawn location. A newly targeted squad is not automatic owner transfer or independently proved physical arrival. W08 and WAR-002b.
- Selected defense respawn interpolates faction settings and applies game-minute timers/gates; targeting scores/count/random gates and owner retention remain separate mechanisms. W09–W13.
- Optional patch UI `def`, preset text and inclusion lists are declarations, not installed values or proof of an active consumer. In this file's inspected loader, OCS configuration consumption covers story/ignore/stationary sections; a health-table header alone does not demonstrate use by its rank/class calculation. W07/W14–W18.
- Module-level online-status replacement writes a permission input consumed later; the separate defined replacement function is not proof of invocation. W01 and ALIFE-08/WAR-002b.

## Competing explanations and missing edges

External reloads or later monkey patches can change the local/cache behavior. Saved user settings or another preset can override UI declaration defaults. Another addon may consume a configuration section absent from the selected module. Missing global dispatch, winning files and storage prevent asserting exact option-refresh, strategy or casualty timing.

## Checks and outcomes

New evidence and targeted consumer/clock review pass within their scope; the [v0.1.43 audit](../verification-2026-10-11-v0.1.43.md) records the actual checks. Prior research/evidence and catalog inputs remain preserved. No source code was redistributed or modified; no runtime tests were performed.

## Disposition and next work

WAR-003 completes the selected supplied-package control reference. ALIFE-03/effective Warfare/death/persistence integration remain open. The [completion status](../../04-game-systems/alife/source-completion-status.md) records the stopping point for available-source consolidation and the requirements for later closure.
