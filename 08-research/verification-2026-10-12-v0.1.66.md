# Verification — 2026-10-12 — ADR v0.1.66

> ADR document set: **v0.1.75**. Research revisions and source/build versions below describe their original scope.

- Target revision: v0.1.66, based on main 7996f62bdcb3f4542b65ce67e3db93eb1f517498
- Scope: GAME-04 gameplay-state consolidation and bounded audit
- Baselines: ENGINE1011/BETA150
- Last reviewed: 2026-10-12

## Semantic audit

| Group | Reconciled contracts | Evidence/outcome |
| --- | --- | --- |
| Fields, changes and authority | Direct live health, pending deltas, server harm gate, first-time reset and commit clamps | G01–G03/G07/G13/G16–G18; no automatic safe healing/revival |
| Damage and callbacks | Branch mitigation, mutable temporary hit, actor pre-hit/eHit versus base after-calcs stage | G04–G11/G19/G20; A18/A19; distinct producer phases retained |
| Actor survival and effects | Actor gates, rates, hysteresis, medicine record, keyed replacement/countdown and raw modifiers | A01–A12/A20/A21; actor/NPC difference, medicine/helper/compiler gaps retained |
| Gear calculations | Armor/AP, durability versus protection, stamina factor, artefact query versus damage/passive rates | G14/G15; A13–A19; conditional/configuration bounds retained |
| Death and casualty policy | Native request/event, derived cleanup around eDeath, server kill/on_death and supplied offline bookkeeping | G09–G12; R04–R07/R13/R19; no universal final-casualty barrier |
| Restoration | Server STATE then UPDATE, virtual condition data, pre/post-binder health writes and booster reuse | R01–R03/R08–R18; health/membership/boost reconstruction gaps retained |

## Integrity and results

Repository checker passes: **224 Markdown files, 1,688 local targets, 25 anchors, zero errors**. All **10 existing regression tests** pass. All **61 gameplay ledger entries and 75 cited range groups** pass full-file hash, line-count, range and cited-symbol checks. Local base files match published v0.1.65; prior-artifact preservation checks pass. Unchanged generated inventories were compared byte-for-byte rather than regenerated; no generator/input changed. No independent game runtime or engine compilation ran.

Prior CSVs/history/generated inventories and tool/test implementations remain byte-identical; dated investigation bodies change only current banners. No generator/input/schema or source baseline changed. Current navigation now identifies consolidation/completion status rather than older intermediate next steps. Editorial repair in GAME-03 splits the health-channel sentence without changing its claim. No source patches, CtZ behavior, license or third-party source/assets publication.

## Publication verification

Use expected main head and compare complete staged/published path/blob map and final head. No future commit hash is invented in this report.

## Remaining limits

Effective condition/medicine/death/restore configs/scripts, callback/build identity, NPC-specific policy, modifier reset and runtime observations remain open. This is a bounded available-source audit, not executable verification. Next tasks/dialogue/info state.
