# ADR index

> ADR document set: **v0.1.70**. Research revisions and source/build versions below describe their original scope.

Start with the [landing page](README.md), [current roadmap](ROADMAP.md), [API catalogs](02-lua-api/api-index.md), and [latest verification](08-research/verification-2026-10-12-v0.1.70.md).

Records retain their research revision and source baseline; those are distinct from the current ADR document-set version. Older source audits remain evidence, rather than current work lists.

## 00-environment

- [Installed engine baseline — ENV-001](00-environment/engine-version.md)
- [SRC-001 — Official May 15, 2026 source baseline](00-environment/source-baseline-2026-05-15.md)
- [SRC-002 — October 11, 2026 Modded Exes source and runtime candidate](00-environment/source-baseline-2026-10-11.md)
- [Source repositories — SRC-001](00-environment/source-repositories.md)

## 01-engine

- [Engine architecture — first-pass map](01-engine/architecture.md)
- [Native/XML-to-Lua registration and widget construction — Part A](01-engine/lua-xml-bridge-callflow.md)
- [Native `CGameFont` lifecycle — May 15, 2026 source](01-engine/native-font-object-lifecycle.md)
- [Source code map — work in progress](01-engine/source-map.md)
- [Historical source-tree audit — ADR v0.1.9](01-engine/source-tree-audit-v0.1.9.md)
- [UI initialization call-flow (source-confirmed subset)](01-engine/ui-initialization-callflow.md)
- [UI architecture: Lua ↔ native XML ↔ native widgets — Part D](01-engine/ui-lua-native-integration.md)

## 02-lua-api

- [Inventory ownership APIs](02-lua-api/inventory/ownership-api.md).

- [Supplied codec and Lua storage caller contracts](02-lua-api/persistence/lua-storage-api.md)

- [Native persistence extension contracts](02-lua-api/persistence/native-extension-contracts.md)

- [Rank/reputation and action-flag contracts](02-lua-api/factions/action-values-api.md)

- [Community mutation and live team APIs](02-lua-api/factions/community-mutation-api.md)

- [Focused faction and relation Lua contracts](02-lua-api/factions/relations-api.md)

- [A-Life / Warfare C++ and Lua interface catalog](02-lua-api/alife/README.md)
- [Native class and Lua name map](02-lua-api/alife/class-map.md)
- [Script interfaces and effective-source boundary](02-lua-api/alife/script-interfaces.md)
- [Server entity, squad and movement API](02-lua-api/alife/server-squad-api.md)
- [Simulator Lua API contracts](02-lua-api/alife/simulator-api.md)
- [Lua API catalogs](02-lua-api/api-index.md)
- [Part A — Luabind registration and XML initializer bridge (v0.1.10)](02-lua-api/registration-architecture-part-A.md)
- [Signature audit — v0.1.4](02-lua-api/signature-audit-v0.1.4.md)
- [ADR v0.1.5 — text/UI declaration audit](02-lua-api/signature-audit-v0.1.5.md)
- [API symbol](02-lua-api/templates/api-entry.md)
- [UI Lua API catalog](02-lua-api/ui/README.md)
- [CScriptXmlInit](02-lua-api/ui/classes/CScriptXmlInit.md)
- [CUILines — declaration audit (ADR v0.1.5)](02-lua-api/ui/classes/CUILines.md)
- [CUIProgressBar — declaration-backed signatures](02-lua-api/ui/classes/CUIProgressBar.md)
- [CUIScrollView — declaration-backed signatures](02-lua-api/ui/classes/CUIScrollView.md)
- [CUIStatic — declaration audit (ADR v0.1.5)](02-lua-api/ui/classes/CUIStatic.md)
- [CUITextWnd — declaration audit (ADR v0.1.5)](02-lua-api/ui/classes/CUITextWnd.md)
- [CUIWindow — declaration-backed signatures (ADR v0.1.4)](02-lua-api/ui/classes/CUIWindow.md)
- [Lua-facing XML initialization: verified boundary and open bindings (ADR v0.1.7)](02-lua-api/xml-initialization-exposure.md)
- [XML initializer Lua registration audit — v0.1.9](02-lua-api/xml-registration-audit-v0.1.9.md)
- [XML initializer Lua-registration search — v0.1.8](02-lua-api/xml-registration-search-v0.1.8.md)

## 03-ui-pda

- [October 11 UI survey — DXML pipeline and patch scoping](03-ui-pda/dxml-pipeline-oct11.md)
- [October 11 UI survey — native dynamic PDA tabs](03-ui-pda/dynamic-pda-tabs-oct11.md)
- [Minimal UI patterns — reference only](03-ui-pda/examples/minimal-static-ui-patterns.md)
- [Native font initialization lifecycle — v0.1.8 evidence boundary](03-ui-pda/font-initialization-lifecycle-v0.1.8.md)
- [Font lifecycle — source audit v0.1.9](03-ui-pda/font-lifecycle-audit-v0.1.9.md)
- [Font manager and Lua-facing getters — interface boundary (ADR v0.1.7)](03-ui-pda/font-manager-and-lua-getters.md)
- [XML font resolution and text initialization (ADR v0.1.6)](03-ui-pda/fonts.md)
- [PDA architecture — investigation PDA-001](03-ui-pda/pda-architecture.md)
- [UI-01 — Dynamic PDA tab and subdialog lifecycle (2026-10-11 source)](03-ui-pda/pda-subdialog-lifecycle-oct11.md)
- [XML/UI Construction and ownership (Part C)](03-ui-pda/ui-construction-ownership.md)
- [October 11 UI survey — Lua controls, fonts, visual resources](03-ui-pda/ui-controls-typography-survey-oct11.md)
- [October 11 UI survey — input and event routes](03-ui-pda/ui-input-events-oct11.md)
- [UI rendering, aspect scaling, native font and texture paths — 2026-10-11 source](03-ui-pda/ui-rendering-scaling-fonts-textures-oct11.md)
- [UI-06 — October 11 Lua widget and event binding inventory](03-ui-pda/ui-widget-event-inventory-oct11.md)
- [UI-06 supplementary audit — registration, emitters, builds, modal routing](03-ui-pda/ui06-supplementary-registration-emission-build-modal-oct11.md)
- [UI-06a through UI-06d — Native UI export, dispatch, and focus audit](03-ui-pda/ui06a-d-registrations-events-focus-oct11.md)
- [UI widgets — source-backed starting index](03-ui-pda/widgets.md)
- [UI-04b — DXML callback failure and registration behavior (2026-10-11)](03-ui-pda/xml-dxml-callback-errors-ui04b-oct11.md)
- [UI-04 — Native XML interception and DXML lifecycle (2026.10.11)](03-ui-pda/xml-dxml-native-lifecycle-oct11.md)
- [Native XML UI initialization (ADR v0.1.6)](03-ui-pda/xml-layouts.md)
- [UI-04a — XML loading routes, naming and DXML interception boundaries](03-ui-pda/xml-loading-paths-ui04a-oct11.md)

## 04-game-systems

- [World interaction/navigation guide](04-game-systems/world/development-reference.md), [coverage inventory](04-game-systems/world/coverage-inventory.md), [completion status](04-game-systems/world/source-completion-status.md).
- [WORLD-01 investigation](08-research/investigations/2026-10-12-WORLD-01-existing-coverage.md), [coverage ledger](evidence/world/README.md), [v0.1.70 verification](08-research/verification-2026-10-12-v0.1.70.md).

- [Inventory/item lifecycle](04-game-systems/inventory/README.md).
- [Ownership and pickup/drop](04-game-systems/inventory/ownership-lifecycle.md).

- [Supplied Lua storage contracts and effective gaps](04-game-systems/persistence/lua-storage-contracts.md)

- [Native save/load pipeline](04-game-systems/persistence/native-save-load-pipeline.md)

- [Faction practical development reference](04-game-systems/factions/development-reference.md)
- [Faction source completion and remaining work](04-game-systems/factions/source-completion-status.md)

- [Supplied Warfare faction/relation consumers](04-game-systems/factions/warfare-relation-consumers.md)

- [Action-driven goodwill and rank/reputation](04-game-systems/factions/action-goodwill.md)

- [Character-community mutation and team/group effects](04-game-systems/factions/community-mutation.md)

- [Native relation persistence, reset and cleanup](04-game-systems/factions/relation-persistence.md)

- [Native faction identity and relations](04-game-systems/factions/native-relations.md)

- [Native configuration controls](04-game-systems/alife/configuration-controls.md)
- [Warfare policy controls](04-game-systems/warfare/policy-controls.md)
- [A-Life / Warfare completion status](04-game-systems/alife/source-completion-status.md)

- [A-Life lifecycle/state reference](04-game-systems/alife/lifecycle-state-reference.md)
- [A-Life callback phases](04-game-systems/alife/callback-phase-reference.md)

- [A-Life reference](04-game-systems/alife/README.md)
- [Factions](04-game-systems/factions/README.md)
- [Persistence](04-game-systems/persistence/README.md)
- [Warfare subsystem](04-game-systems/warfare/README.md)

## 05-mod-architecture

- [Mod architecture and GAMMA compatibility](05-mod-architecture/README.md)

## 06-debugging

- [Debugging workflow](06-debugging/README.md)

## 07-code-library

- [Reusable code library](07-code-library/README.md)

## 08-research

- [PER-02 Lua storage investigation](08-research/investigations/2026-10-11-PER-02-lua-storage.md)
- [Current verification — v0.1.56](08-research/verification-2026-10-12-v0.1.69.md)

- [PER-01 native save/load investigation](08-research/investigations/2026-10-11-PER-01-native-save-load.md)
- [PER-01 verification — v0.1.50](08-research/verification-2026-10-11-v0.1.50.md)

- [FAC-06 consolidation and final source audit](08-research/investigations/2026-10-11-FAC-06-faction-consolidation.md)
- [Final faction verification — v0.1.49](08-research/verification-2026-10-11-v0.1.49.md)

- [FAC-05 Warfare consumer investigation](08-research/investigations/2026-10-11-FAC-05-warfare-consumers.md)
- [FAC-05 increment verification — v0.1.48](08-research/verification-2026-10-11-v0.1.48.md)

- [FAC-04 action-goodwill investigation](08-research/investigations/2026-10-11-FAC-04-action-goodwill.md)
- [FAC-04 verification — v0.1.47](08-research/verification-2026-10-11-v0.1.47.md)

- [FAC-03 community mutation investigation](08-research/investigations/2026-10-11-FAC-03-community-mutation.md)
- [FAC-03 verification — v0.1.46](08-research/verification-2026-10-11-v0.1.46.md)

- [FAC-02 relation persistence investigation](08-research/investigations/2026-10-11-FAC-02-relation-persistence.md)
- [FAC-02 verification — v0.1.45](08-research/verification-2026-10-11-v0.1.45.md)

- [FAC-01 native faction/relation queries](08-research/investigations/2026-10-11-FAC-01-native-relations.md)
- [FAC-01 verification — v0.1.44](08-research/verification-2026-10-11-v0.1.44.md)

- [ALIFE-11 configuration investigation](08-research/investigations/2026-10-11-ALIFE-11-configuration-controls.md)
- [WAR-003 policy-control investigation](08-research/investigations/2026-10-11-WAR-003-configuration-policy-controls.md)
- [Available-source audit — v0.1.43](08-research/verification-2026-10-11-v0.1.43.md)

- [ALIFE-10 synthesis record](08-research/investigations/2026-10-11-ALIFE-10-lifecycle-callback-consolidation.md)
- [ALIFE-10 verification — v0.1.42](08-research/verification-2026-10-11-v0.1.42.md)

- [Canonical-tree cleanup verification — v0.1.41](08-research/verification-2026-10-11-v0.1.41.md)

- [Update scope — v0.1.12](08-research/2026-10-11-update-scope.md)
- [Evidence and verification policy](08-research/evidence-policy.md)
- [INV-014 — A-01/A-02 registration bootstrap audit (ADR v0.1.11)](08-research/investigations/2026-10-09-A01-A02-registration-bootstrap.md)
- [Investigation: UI Lua binding extraction](08-research/investigations/2026-10-09-lua-ui-binding-extraction.md)
- [INV-010 — Lua XML registration (Part A)](08-research/investigations/2026-10-09-part-A-registration-audit.md)
- [Part B — Font manager investigation (2026-10-09)](08-research/investigations/2026-10-09-part-B-native-font-manager.md)
- [INV-012 — Part C: XML/UI object construction, attachment and deletion](08-research/investigations/2026-10-09-part-C-ui-construction.md)
- [INV-013 — Part D integration and post-audit review](08-research/investigations/2026-10-09-part-D-integration.md)
- [INV-001: Establish upstream source baseline](08-research/investigations/2026-10-09-source-baseline.md)
- [INV-009 — Source-tree audit and XML/font lifecycle](08-research/investigations/2026-10-09-source-tree-audit-v0.1.9.md)
- [INV-003 — Map installed executable to historical source tag](08-research/investigations/2026-10-09-tag-reconstruction.md)
- [INV-002: Capture the Zone font crash](08-research/investigations/2026-10-09-ui-fonts.md)
- [INV-006 — XML font and scrollview native initialization](08-research/investigations/2026-10-09-xml-font-init.md)
- [INV-007 — XML/Lua boundary and font getters](08-research/investigations/2026-10-09-xml-lua-bridge.md)
- [INV-008 — XML registration and font-manager lifecycle](08-research/investigations/2026-10-09-xml-lua-search-and-font-lifecycle.md)
- [A-01 — Complete October 11 registration chain](08-research/investigations/2026-10-11-A01-source-registration-closure.md)
- [A-02 — Separate native CUIXmlInit Lua exposure (2026-10-11)](08-research/investigations/2026-10-11-A02-native-xml-lua-exposure.md)
- [ALIFE-01 — Server identity, squad membership and online/offline lifecycle](08-research/investigations/2026-10-11-ALIFE-01-identity-lifecycle.md)
- [ALIFE-02 — Native creation, registration, release and callback ordering](08-research/investigations/2026-10-11-ALIFE-02-creation-registration-release.md)
- [ALIFE-04 — Native persistence and CtZ identity reconstruction](08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md)
- [ALIFE-05 — Native scheduling, brains and offline movement](08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md)
- [ALIFE-06 — Graph location, online realization and spawn callbacks](08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md)
- [ALIFE-07 — Client-to-server position synchronization and offline teardown](08-research/investigations/2026-10-11-ALIFE-07-client-server-offline-teardown.md)
- [ALIFE-08 — Switching eligibility, hysteresis and forced states](08-research/investigations/2026-10-11-ALIFE-08-switching-eligibility.md)
- [B-01 — ownership of UI font manager and named font pointers](08-research/investigations/2026-10-11-B01-font-manager-ownership.md)
- [B-02 — client UI font manager lifecycle and device-reset handling](08-research/investigations/2026-10-11-B02-font-manager-lifecycle.md)
- [C-01 — Native UI creation and parent-child ownership contract](08-research/investigations/2026-10-11-C01-ui-ownership.md)
- [C-02 — CUIScrollView internal pad and child ownership](08-research/investigations/2026-10-11-C02-scrollview-ownership.md)
- [C-03 — Luabind ownership transfer versus native UI AutoDelete](08-research/investigations/2026-10-11-C03-luabind-adoption-autodelete.md)
- [C-04 — Lua return ownership of CScriptXmlInit-created UI controls](08-research/investigations/2026-10-11-C04-xml-factory-return-ownership.md)
- [UI-01a — Native tab selection, reset, and event propagation](08-research/investigations/2026-10-11-UI-01a-tab-state-transitions.md)
- [WAR-001 — CtZ integration boundary and source prerequisites](08-research/investigations/2026-10-11-WAR-001-ctz-integration-boundary.md)
- [WAR-002a — Warfare source packages and effective-profile boundary](08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md)
- [WAR-002b — Targeting, ownership and offline combat in the supplied Warfare source](08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md)
- [Research investigations](08-research/investigations/README.md)
- [Open questions — consolidated review after Parts A–D](08-research/open-questions-v0.1.10.md)
- [Repository file and folder conventions](08-research/repository-layout.md)
- [ID — Investigation title](08-research/templates/investigation.md)
- [Verification — YYYY-MM-DD — ADR revision](08-research/templates/verification.md)
- [ADR source verification — v0.1.30 (11 October 2026)](08-research/verification-2026-10-11-v0.1.30.md)
- [Workflow and structure verification — ADR v0.1.40](08-research/verification-2026-10-11-v0.1.40.md)
- [Standard ADR research workflow](08-research/workflow.md)

## 09-projects

- [Capture the Zone integration](09-projects/capture-the-zone/README.md)

## evidence

- [Persistence evidence](evidence/persistence/README.md)

- [Faction and relation evidence](evidence/factions/README.md)

- [A-Life source evidence](evidence/alife/README.md)
- [Evidence manifest](evidence/manifest.md)
- [Warfare source evidence](evidence/warfare/README.md)

## tests

- [Verification and tests](tests/README.md)

## tools

- [Research and documentation tools](tools/README.md)
- [Reproducible pinned checkout and audit](tools/source-audit-commands.md)

## History and maintenance

- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Maintenance rules](AGENTS.md)
- [Publishing](PUBLISHING.md)
- [Historical navigation](08-research/history/index-through-v0.1.40.md)
- [Historical roadmap](08-research/history/roadmap-through-v0.1.40.md)
- [Historical README](08-research/history/readme-through-v0.1.40.md)

- [CtZ campaign identity/schema/reconciliation](04-game-systems/persistence/ctz-campaign-safety.md).
- [PER-03 investigation](08-research/investigations/2026-10-11-PER-03-ctz-campaign-safety.md).

- [Persistence development reference](04-game-systems/persistence/development-reference.md).
- [Persistence source completion](04-game-systems/persistence/source-completion-status.md).
- [PER-04 consolidation/audit](08-research/investigations/2026-10-11-PER-04-persistence-consolidation.md).

- [ITEM-01 investigation](08-research/investigations/2026-10-11-ITEM-01-ownership-lifecycle.md).
- [Inventory evidence](evidence/inventory/README.md).

- [Item placement/activation](04-game-systems/inventory/placement-activation.md).
- [Placement Lua APIs](02-lua-api/inventory/placement-api.md).
- [ITEM-02 investigation](08-research/investigations/2026-10-11-ITEM-02-placement-activation.md).

- [Item consumption/destruction](04-game-systems/inventory/consumption-destruction.md).
- [Consumption APIs](02-lua-api/inventory/consumption-api.md).
- [ITEM-03 investigation](08-research/investigations/2026-10-11-ITEM-03-consumption-destruction.md).

- [Item persistence/reconstruction](04-game-systems/inventory/persistence-reconstruction.md), [ITEM-04](08-research/investigations/2026-10-11-ITEM-04-persistence-reconstruction.md), [ledger](evidence/inventory/persistence-reconstruction-2026-10-11.csv).

- [Inventory development reference](04-game-systems/inventory/development-reference.md), [completion status](04-game-systems/inventory/source-completion-status.md), [ITEM-05](08-research/investigations/2026-10-11-ITEM-05-inventory-consolidation.md).

- [Trade/economy](04-game-systems/economy/README.md), [native trade](04-game-systems/economy/native-trade.md), [money/cost APIs](02-lua-api/economy/money-cost-api.md), [ECO-01](08-research/investigations/2026-10-11-ECO-01-native-trade.md).

## 2026-10-12 external runtime review

- [ENV-RT01 reported GAMMA baseline](00-environment/reported-gamma-runtime-2026-10-12.md).
- [REV-01 confidence/disposition review](08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md).
- [Source comparison](evidence/runtime/issue-review-source-2026-10-12.csv) and [external observations](evidence/runtime/reported-observations-2026-10-12.csv).
- [v0.1.60 verification](08-research/verification-2026-10-12-v0.1.69.md).

- [Trader configuration and supply consumers](04-game-systems/economy/trader-configuration.md), [policy/supply APIs](02-lua-api/economy/trader-policy-api.md), [ECO-02](08-research/investigations/2026-10-12-ECO-02-trader-configuration.md).

- [Economy development reference](04-game-systems/economy/development-reference.md), [completion status](04-game-systems/economy/source-completion-status.md), [ECO-03](08-research/investigations/2026-10-12-ECO-03-economy-consolidation.md).

- [Actor/NPC gameplay state](04-game-systems/gameplay/README.md), [native condition](04-game-systems/gameplay/native-condition.md), [condition APIs](02-lua-api/gameplay/condition-api.md), [GAME-01](08-research/investigations/2026-10-12-GAME-01-native-condition.md).

- [Actor survival/boosters/equipment](04-game-systems/gameplay/actor-effects-equipment.md), [effect APIs](02-lua-api/gameplay/actor-effects-api.md), [GAME-02](08-research/investigations/2026-10-12-GAME-02-actor-effects.md).

- [Derived death/condition restoration](04-game-systems/gameplay/death-restoration.md), [GAME-03](08-research/investigations/2026-10-12-GAME-03-death-restoration.md).

- [Gameplay-state development reference](04-game-systems/gameplay/development-reference.md), [completion status](04-game-systems/gameplay/source-completion-status.md), [GAME-04](08-research/investigations/2026-10-12-GAME-04-gameplay-consolidation.md).

## Standard subsystem entry points

[Subsystem entry map](08-research/subsystem-map.md), [UI/PDA hub](03-ui-pda/README.md), [game-system hub](04-game-systems/README.md). Each researched behavior subsystem has a README, development reference and completion status; legacy detailed files retain their identity.

- [Tasks/dialogue/info state](04-game-systems/tasks/README.md), [native foundation](04-game-systems/tasks/native-task-dialogue-info.md), [APIs](02-lua-api/tasks/native-task-info-api.md), [TASK-01](08-research/investigations/2026-10-12-TASK-01-native-task-dialogue-info.md).

- [Supplied task/dialogue/reward/restoration consumers](04-game-systems/tasks/supplied-task-dialogue-consumers.md), [TASK-02](08-research/investigations/2026-10-12-TASK-02-supplied-task-dialogue-consumers.md), [TASK-03 consolidation](08-research/investigations/2026-10-12-TASK-03-task-state-consolidation.md).
