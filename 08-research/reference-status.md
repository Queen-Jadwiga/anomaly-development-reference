# Whole-reference status and effective closure

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

- ID: ADR-01-STATUS
- Research revision: v0.1.82
- Record status: whole-reference consolidation/provenance/navigation/consistency audit complete within declared scope
- Source status: repository-wide structural/provenance inventory and integrity checks; semantic review of current entry/status contracts
- Baseline: ADR v0.1.81 `dc826c78041971cac96710b329b6ce85905e8e13`
- Last reviewed: 2026-10-12


## Current coverage and authoritative gaps

| Area | Central reference | Completion/audit authority | Retained boundary |
| --- | --- | --- | --- |
| UI/PDA | [Guide](../03-ui-pda/development-reference.md) | [Status/per-page scope](../03-ui-pda/source-completion-status.md) | Mixed historical/October source scopes; owned registration/readiness and external crash questions open |
| A-Life | [Guide](../04-game-systems/alife/development-reference.md) | [Shared status](../04-game-systems/alife/source-completion-status.md), [v0.1.43](verification-2026-10-11-v0.1.43.md) | Board/smart/arrival, death/release, startup and strategic restoration |
| Warfare | [Guide](../04-game-systems/warfare/development-reference.md) | [Status](../04-game-systems/warfare/source-completion-status.md), shared A-Life rule | Package/preset/control evidence separate from installed policy and replacements |
| Factions | [Guide](../04-game-systems/factions/development-reference.md) | [Status](../04-game-systems/factions/source-completion-status.md), [v0.1.49](verification-2026-10-11-v0.1.49.md) | True community/diplomacy, awards, reassignment and save/reapply |
| Persistence | [Guide](../04-game-systems/persistence/development-reference.md) | [Status](../04-game-systems/persistence/source-completion-status.md), [v0.1.53](verification-2026-10-11-v0.1.53.md) | Actual storage root/encoder/snapshot, schema/campaign pairing and restore phases |
| Inventory | [Guide](../04-game-systems/inventory/development-reference.md) | [Status](../04-game-systems/inventory/source-completion-status.md), [v0.1.58](verification-2026-10-11-v0.1.58.md) | Actual ownership/placement/cleanup, callbacks and derived persistence |
| Economy | [Guide](../04-game-systems/economy/development-reference.md) | [Status](../04-game-systems/economy/source-completion-status.md), [v0.1.62](verification-2026-10-12-v0.1.62.md) | Winning prices/stock/helpers and request/accounting/retry outcomes |
| Gameplay state | [Guide](../04-game-systems/gameplay/development-reference.md) | [Status](../04-game-systems/gameplay/source-completion-status.md), [v0.1.66](verification-2026-10-12-v0.1.66.md) | Medicine/hit/death/restore, configured values and casualty authority |
| Tasks/dialogue/info | [Guide](../04-game-systems/tasks/development-reference.md) | [Status](../04-game-systems/tasks/source-completion-status.md), [v0.1.69](verification-2026-10-12-v0.1.69.md) | Actual task/reward/functor/info definitions, stage history and reconstruction |
| World/navigation | [Guide](../04-game-systems/world/development-reference.md) | [Status](../04-game-systems/world/source-completion-status.md), [v0.1.73](verification-2026-10-12-v0.1.73.md) | Winning use/travel/zone/restriction/marker consumers and request completion |
| Configuration/script | [Guide](../04-game-systems/configuration/development-reference.md) | [Status](../04-game-systems/configuration/source-completion-status.md), [v0.1.77](verification-2026-10-12-v0.1.77.md) | Globals/dispatch/installers/cache/option application and effective startup/restore |
| Practical architecture/debugging | [Guide](../05-mod-architecture/development-reference.md) | [v0.1.81 bounded audit](verification-2026-10-12-v0.1.81.md) | Proposed patterns unimplemented; effective dependencies/lifetimes and runtime unresolved |

The eleven behavior entries keep their README/guide/status roles; Warfare shares its combined closure rule with A-Life. Environment, architecture, diagnostics, examples, tools/tests and CtZ project records keep their own categories. [Subsystem map](subsystem-map.md), [full index](../INDEX.md), [entry contracts](../evidence/reference/entry-contracts-2026-10-12.csv).

## What this audit checked and corrected

The base inventory covers all **378 files**, including **304 Markdown pages**, **59 CSV datasets** and **seven JSON datasets**. Rechecks pass for **938 source/file rows across 334 available artifact-relative source paths**, **1,322 source range groups**, and **102 earlier reference rows**. Four UPSTREAM0912 rows retain immutable remote pins; local September source is unavailable. Generated API inventories, historical May source, comparisons and external observations are classified with their original limits rather than newly regenerated/tested. [Audit summary](../evidence/reference/audit-summary-2026-10-12.json), [provenance register](../00-environment/provenance-register.md).

Corrected current navigation includes a complete Markdown index, current-versus-historical API/evidence grouping, missing configuration hub entry, verification-label/target mismatches, obsolete follow-on allocations and a pinned CtZ baseline rather than an unverified current mod-version claim. A focused validator rule and regression fixtures now reject explicit local verification-revision labels that disagree with the report filename; source-version labels on other targets are not treated as report labels. [Corrections](../evidence/reference/corrections-2026-10-12.csv), [verification](verification-2026-10-12-v0.1.82.md).

Review retains source versus executable/profile, source versus external/runtime, implementation versus proposed patterns, durable versus transient/aliased state, callback/return/request versus completion, parser/save versions versus campaign schemas, and original research revisions versus current banners. Original dated investigations and historical snapshots remain preserved. Structural/hash success is not an exhaustive semantic or runtime guarantee.

## Remaining work has three different purposes

1. **Effective-source closure:** collect relevant virtual winning files, packed inputs, configuration, globals/dispatchers, installers/emitters, binders/storage, campaign identity and resource/teardown chains; trace them for a concrete integration question. The status pages above remain authoritative. A mod list, same filename or source date alone cannot close those edges.
2. **Targeted source depth:** investigate a specific missing contract when a modding/debugging question needs it. Full renderer/VM/security/profiler/animation/physics, every AI/item/build/addon and unrelated multiplayer remain optional depth rather than silently included completion criteria.
3. **Runtime verification:** explicitly resumed by the user on October 12; authorized and independently untested. It requires executable/profile/save identity, reproduction and actual observations/results. Existing ADR tests exercise documentation/source tools; proposed model fixtures and non-runnable sketches do not test the game.

No CtZ gameplay changes, save edits, native compilation or third-party source/assets are part of this audit. The selected reference foundation and whole-reference audit are complete within scope; installation/runtime closure stays open. [Roadmap](../ROADMAP.md), [investigation](investigations/2026-10-12-ADR-01-whole-reference-audit.md).
