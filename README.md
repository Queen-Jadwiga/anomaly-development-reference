# Anomaly Development Reference (ADR)

> ADR document set: **v0.1.63**. Research revisions and source/build versions below describe their original scope.

**Source-backed modding research for S.T.A.L.K.E.R. Anomaly / X-Ray Monolith / Modded Exes**

> **Work in progress — independent research, not official engine documentation.**
> Current ADR revision: **v0.1.63** (12 October 2026). Primary research source: the
> **2026.10.11** X-Ray Monolith source archive. Independent target-installation testing remains pending; selected **external runtime observations** are documented with build limits.

## Current runtime feedback

[REV-01](08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md) incorporates colleague reports without equating them to universal engine verification. UI quickload teardown and live-tab registration during loading remain open hazards. The confirmed property-catalog omission and build-history/dispatcher clarifications are corrected.

## What is this?

A version-aware development reference produced while researching the **Capture the Zone (CtZ)**
mod. Its purpose is to make native engine and Lua behavior traceable to source code,
document ownership and lifecycle rules, and keep unknowns visible rather than guessing.

It is **not** the game mod itself, nor a replacement for the X-Ray source or official documentation.

## Capture the Zone mod

The [Capture the Zone (CtZ) repository](https://github.com/Queen-Jadwiga/capture-the-zone)
contains the mod files for **Alpha 0.0.5j — Revised Fixed Bars / Advantage Marker**,
with its original build documentation and assets.

## Recommended quick review

If you only have a few minutes, start here:

| Topic | Why read it? |
| --- | --- |
| [C-03 — Luabind and native UI ownership](08-research/investigations/2026-10-11-C03-luabind-adoption-autodelete.md) | `adopt<2>()` versus native `AutoDelete` — see research index for the exact C-03 record |
| [C-04 — XML factory return ownership](08-research/investigations/2026-10-11-C04-xml-factory-return-ownership.md) | How XML-created control pointers are owned and returned |
| [UI construction & ownership](03-ui-pda/ui-construction-ownership.md) | Practical consequences for XML-created controls and native parent ownership |
| [Dynamic PDA tabs](03-ui-pda/dynamic-pda-tabs-oct11.md) | New native-backed PDA tab registration and Lua integration |
| [A-Life lifecycle/state reference](04-game-systems/alife/lifecycle-state-reference.md) | Persistent server, group and temporary client representations |
| [A-Life callback phases](04-game-systems/alife/callback-phase-reference.md) | What each observation point establishes and what remains pending |
| [PDA subdialog lifecycle](03-ui-pda/pda-subdialog-lifecycle-oct11.md) | Rebuild, selection, and content synchronization |
| [A-Life / Warfare completion status](04-game-systems/alife/source-completion-status.md) | Completed source scope and missing effective chains |
| [Native configuration controls](04-game-systems/alife/configuration-controls.md) / [Warfare policy controls](04-game-systems/warfare/policy-controls.md) | Producers, consumers, clocks and refresh boundaries |
| [Native faction identity and relations](04-game-systems/factions/native-relations.md) | Community identity, goodwill direction and final attitude |
| [Faction development reference](04-game-systems/factions/development-reference.md) | Practical query, mutation, storage and event boundaries |
| [Native save/load pipeline](04-game-systems/persistence/native-save-load-pipeline.md) | File framing, reconstruction and Lua extension phases |
| [Current verification report](08-research/verification-2026-10-12-v0.1.63.md) | What was checked and what was not |
| [Full research index](INDEX.md) | Every investigated area and historic records |

## Research status

- **UI/PDA:** development-reference ready at source level; native ownership, XML/DXML,
  widget exports, input, fonts, scaling, rendering, and dynamic tabs investigated.
- **A-Life / Warfare:** [identity/lifecycle](08-research/investigations/2026-10-11-ALIFE-01-identity-lifecycle.md) and [creation/release/callback ordering](08-research/investigations/2026-10-11-ALIFE-02-creation-registration-release.md) documented; [supplied Warfare policy and offline combat](08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md) traced. [Save/load and CtZ identity reconstruction](08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md) traced. [Native offline scheduling and brains](08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md) traced. [Graph location and online realization](08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md) traced. [Client-to-server position synchronization and offline teardown](08-research/investigations/2026-10-11-ALIFE-07-client-server-offline-teardown.md) traced. [Native switching eligibility and forced states](08-research/investigations/2026-10-11-ALIFE-08-switching-eligibility.md) traced. [C++/Lua class and interface catalog](02-lua-api/alife/README.md) added. [Lifecycle/state](04-game-systems/alife/lifecycle-state-reference.md) and [callback-phase](04-game-systems/alife/callback-phase-reference.md) references consolidate the native/bundled-source paths. Active GAMMA profile reconciliation remains open.
- **Factions / relations:** [native query foundations](04-game-systems/factions/native-relations.md) and [focused Lua contracts](02-lua-api/factions/relations-api.md) documented; [native persistence/reset/cleanup](04-game-systems/factions/relation-persistence.md) traced; [community mutation and local team/group effects](04-game-systems/factions/community-mutation.md) traced; [native action-driven goodwill/rank/reputation](04-game-systems/factions/action-goodwill.md) traced; [selected supplied Warfare relation consumers](04-game-systems/factions/warfare-relation-consumers.md) traced; [practical consolidation](04-game-systems/factions/development-reference.md) and bounded final audit complete within available-source scope; [effective integration remains partial](04-game-systems/factions/source-completion-status.md).
- **Persistence:** [native save/load pipeline](04-game-systems/persistence/native-save-load-pipeline.md) and [Lua extension boundaries](02-lua-api/persistence/native-extension-contracts.md) documented; [supplied Lua codec/caller contracts](04-game-systems/persistence/lua-storage-contracts.md) and missing core implementations mapped; [CtZ campaign identity/schema/reconciliation](04-game-systems/persistence/ctz-campaign-safety.md) documented; [practical consolidation and bounded audit](04-game-systems/persistence/development-reference.md) complete within scope; effective installed storage remains partial.
- **Inventory/item lifecycle:** selected ownership, placement/activation, consumption/removal and persistence foundations consolidated in the [development reference](04-game-systems/inventory/development-reference.md); [bounded audit](08-research/verification-2026-10-12-v0.1.63.md) complete. [Effective integration](04-game-systems/inventory/source-completion-status.md) remains partial.
- **October 11 executable in GAMMA:** candidate target; runtime compatibility and behavior
  are unverified.
- **Source-level limits:** some exhaustive export, indirect event, configuration, and
  cross-addon questions remain open; see [ROADMAP.md](ROADMAP.md).

## Research workflow

Follow the [standard workflow](08-research/workflow.md), [folder conventions](08-research/repository-layout.md) and [contributing guide](CONTRIBUTING.md). Current APIs are organized in the [central catalog index](02-lua-api/api-index.md); research records and source ledgers have separate canonical homes.

## Evidence conventions

- **Source-verified:** supported by a specified source path and implementation.
- **Scoped source audit:** supported within an explicitly bounded search; not an engine-wide proof.
- **Hypothesis / open:** further evidence required.
- **Runtime pending:** source research sufficient for now; actual in-game behavior not yet tested.

Claims should not be promoted to runtime-verified without testing.

## Repository navigation

- [Full index](INDEX.md)
- [Research roadmap and open work](ROADMAP.md)
- [Environment and source baselines](00-environment)
- [Engine architecture](01-engine)
- [Lua API reference](02-lua-api)
- [UI / PDA reference](03-ui-pda)
- [Game systems](04-game-systems)
- [Research and verification](08-research)
- [Changelog](CHANGELOG.md)
- [Historical README snapshot](08-research/history/readme-through-v0.1.40.md)

## Publishing

See [publishing instructions](PUBLISHING.md) for GitHub Desktop or Git CLI.

## Feedback welcome

For an engine developer reviewing this guide, the most helpful feedback would be:

1. Are the Luabind/UI ownership conclusions correct, particularly the distinctions between
   Lua userdata ownership and native `AutoDelete`?
2. Have we overlooked supported engine interfaces or intended usage patterns, especially for
   dynamic PDA tabs?
3. Are there sections likely to mislead modders despite being source-referenced?

Please reference the specific Markdown file and line or open a GitHub Issue.

## Attribution and scope

X-Ray Monolith / Modded Exes and Anomaly are third-party projects. This repository contains
independent research and source references; it does **not** redistribute the engine sources
or the compiled executables. No upstream endorsement is implied.

Selected inventory/item lifecycle foundations are complete within scope: [ownership, containment and pickup/drop](04-game-systems/inventory/ownership-lifecycle.md), with focused Lua contracts. See the [broader first-edition scope](ROADMAP.md#general-modding-foundations) for remaining general modding foundations.

[Item placement and active-slot transitions](04-game-systems/inventory/placement-activation.md) now distinguish placement, requested/current selection and readiness boundaries; effective NPC equipment delivery remains open.

[Item persistence and reconstruction](04-game-systems/inventory/persistence-reconstruction.md) now traces saved server/client fields, live placement and pending active-slot restoration; [practical consolidation and bounded audit](04-game-systems/inventory/development-reference.md) are complete. [Effective integration](04-game-systems/inventory/source-completion-status.md) remains partial; trade/economy is next.

Trade/economy available-source work is consolidated and audited: [practical reference](04-game-systems/economy/development-reference.md) and [source completion](04-game-systems/economy/source-completion-status.md). Selected native/supplied contracts are complete within scope; installed managers/configs and runtime remain open. Next actor/NPC gameplay state.

Actor/NPC gameplay-state research has started: [native condition/hit phases](04-game-systems/gameplay/native-condition.md) separates live fields, pending changes and death requests. Next actor survival/boosters/equipment; runtime deferred.
