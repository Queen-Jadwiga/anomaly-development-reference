# FAC-05 — Supplied Warfare faction/relation consumers

> ADR document set: **v0.1.75**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-05
- Subsystem: factions / Warfare integration
- ADR revision: v0.1.48
- Record status: complete-within-scope
- Source status: source-confirmed within selected BETA150 main-package definitions/call sites
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline and provenance: BETA150; [package record](2026-10-11-WAR-002a-source-packages-effective-profile.md)
- Last reviewed: 2026-10-11

## Question and scope

Which faction/relation values do the supplied Warfare consumers use, and where do helper semantics, identities, mutations and online/offline adapters differ?

Include BETA150 main `game_relations` helpers and selected save/reapply/death adapters; squad/actor faction producers; squad arrival, visibility, tooltip, ignored-member conversion and actor support; smart ownership/target penalties; offline enemy/outcome; faction boosts/resurgence and PDA matrix display. Exclude every quest/dialog/menu call, full dynamic-diplomacy mathematical certification, installed winners/configuration/helpers, exhaustive optional-patch/ZIP142 equivalence, gameplay changes and runtime. Completion is this consumer investigation only; consolidation/final available-source audit are expressly separate later actions.

## Evidence and method

BETA150 archive SHA-256 `9f71999bb44cb6d3e41c431feaf5be4714159522df1fa8d71599ac039946315d`. [Ledger R01–R20](../../evidence/factions/warfare-consumers-2026-10-11.csv): 20 claim entries across nine main-package files, with paths, symbols, ranges and hashes. Optional variants are not silently combined with main.

Search main scripts for `game_relations`, `relation_registry`, community getters and selected identity/mutation producers; read helper implementations and surrounding call gates. Follow selected dynamic save/reapply, death and contested-target paths. Distinguish active code from comments, local captured aliases from exported helper names, native attitude from matrix cells and strategic state. No installed script order or effective configuration inferred.

## Findings

The [consumer reference](../../04-game-systems/factions/warfare-relation-consumers.md) provides adjacent ledger citations and tables.

- Native community, script `player_id` mapping, cached actor true faction and smart ownership differ. Script faction lists are not native numeric community-index order. R01/R07–R09/R19.
- Predicates classify directed matrix values at script ±1000 boundaries. A misleadingly named change helper instead alters community-to-character goodwill. Script save helper supplies symmetry and actor storage intent. R01–R03.
- Visibility/arrival/statistics/combat gates use matrix predicates; tooltip can average loaded members' full attitude, with a different fallback. Opposite query directions and captured local helpers require explicit handling. R11/R12/R15/R16/R18/R19.
- Dynamic mutation writes ordinary and actor-prefixed pairs, applies bounds/random resets and sends threshold news. Marshal-gated restore is a script layer, not proof of native matrix durability or installed callback order. Literal reset/counter caveats remain unrepaired. R03/R04/R06/R08/R09.
- Contested target penalties are strategic diplomacy inputs under options/pair gates. Online/offline death adapters differ; offline outcome and actor support add separate script awards. No native/offline convergence or deduplication is established. R04/R05/R13/R14/R17/R20.
- Active ignored-member conversion differs from its commented trader rewrite and can mark a one-shot flag before members are available. Native setter effects remain FAC-03's selected contract. R10.

## Missing edges and alternatives

Winning scripts can replace predicates/identities, change thresholds, reapply matrix state, alter rank/reward bookkeeping or strategic membership. `save_var/load_var`, global startup/shared dispatch, true-community helpers, reward helpers and active configuration require effective-source review. Captured aliases and cached faction fields can outlive export replacements. Missing/unloaded members can change a display's selected branch. These possibilities do not diagnose runtime behavior.

## Checks and outcomes

Reviewed selected helper/caller semantics, direction, gates, active/commented code and storage intent. Verified source hashes/counts/ranges/symbols and normal repository navigation/version/preservation checks, recorded in [increment verification](../verification-2026-10-11-v0.1.48.md). These checks validate the increment; they do not perform or close the deferred faction consolidation/final audit. No runtime, gameplay edits or script corrections.

## Disposition and next work

FAC-05 completes this scoped supplied-main-package consumer research. Factions remains partial. Consolidation and final available-source audit are later separate actions; installed diplomacy/effective integration and runtime remain open. [Roadmap](../../ROADMAP.md).
