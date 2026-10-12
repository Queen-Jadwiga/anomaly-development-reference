# WORLD-01 — Existing world/navigation coverage and next scope

> ADR document set: **v0.1.76**. Research revisions and source/build versions below describe their original scope.

- ID: WORLD-01
- Subsystem: world interaction/navigation
- ADR revision: v0.1.70
- Record status: complete-within-scope (inventory only)
- Source status: scoped-source-audit of existing ADR documentation; original source confidence retained
- Runtime status: untested; deferred
- Baseline IDs and provenance: ADR v0.1.69 main `6ab1f93634f54ccc40dfe3fe33b716114a62157e`; existing ENGINE1011 and qualified supplied-package records via [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and scope

Which world interaction/navigation concerns already have a bounded ADR source trace, which are cataloged/adjacent only, and where should new work begin? Review A-Life lifecycle/state/callback/completion references, simulator/server/squad/class catalogs, ALIFE-05/06/07/08 and adjacent inventory/task/persistence references. Inventory scope closes after canonical links, preserved confidence, gaps and a bounded follow-on sequence are recorded. It does not close new native APIs or runtime.

## Evidence and method

[Fourteen-row coverage ledger](../../evidence/world/coverage-inventory-2026-10-12.csv) pins selected original ADR document hashes and section markers at the immutable ADR commit. Search/review terms included `lookup`, `object_by_id`, `position`, `vertex`, `graph`, `restrict`, `accessible`, `patrol`, `smart`, `teleport`, `level change` and `map marker`. Read the relevant reference sections, ledgers and original investigation scope/exclusions; classify coverage rather than count symbol mentions as closure. Existing evidence is reused through canonical links, with no schema migration or new artifact pin.

ENGINE1011 path search additionally locates candidate native files listed in the [inventory](../../04-game-systems/world/coverage-inventory.md). File presence and export occurrences are trace targets only. Exact installed executable/profile equivalence and effective file winners remain unknown. No new engine behavior conclusion is based on those candidate searches.

## Findings

W01–W08 retain selected server lookup/identity, lifetime, offline graph/group movement, completion and position/relocation limits. W09–W10 identify weaker restriction/patrol catalog coverage. W11 preserves effective smart/job gaps. W12 distinguishes already traced map position authority from still-needed marker lifecycle. W13 separates squad graph/level changes from actor travel. W14 recognizes inventory consumers without promoting them to a general use/touch routing audit. See the [coverage table](../../04-game-systems/world/coverage-inventory.md) for each canonical source and remaining edge.

Reuse the existing A-Life graph/offline/realization records. Extend live spatial queries/requests first, then interaction/actor transitions/marker lifecycle, then supplied consumers and consolidation/audit. Each new behavior claim still requires declaration/export/definition/caller evidence under the original baseline policy.

## Competing explanations and missing edges

An existing export catalog, selected position helper or text mention may look like complete navigation coverage. The original scopes do not justify that interpretation: restriction policy, live spatial helper semantics, marker lifecycle and actor travel need separate traces. Conversely, no reviewed closure does not imply missing upstream source, absent installed functionality or an installed bug. Active smart/jobs, wrappers/configuration and binder/storage/startup chains remain effective-source gaps.

## Checks and outcomes

Validate all inventory target documents, original hashes, section ranges/markers and step allocations against the v0.1.69 base. Preserve prior CSV/JSON/history/generated/tool/test bytes; dated investigations change only document-set banners. Run repository checks and existing documentation regressions, compare remote base and publish full path/blob maps. [Verification](../verification-2026-10-12-v0.1.70.md). No independent runtime or engine compilation.

## Disposition and next work

WORLD-01 inventory is complete within scope. World interaction/navigation remains partial under its [completion rule](../../04-game-systems/world/source-completion-status.md). **Next: WORLD-02 spatial queries, relocation and selected restriction/patrol contracts.** [Central guide](../../04-game-systems/world/development-reference.md), [roadmap](../../ROADMAP.md).
