# World interaction/navigation development reference

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

**Current cross-system status:** [ADR-01 whole-reference audit](../../08-research/reference-status.md) is complete within scope. Original research allocations/baselines below remain dated; selected foundations are consolidated, effective installed integration stays partial and runtime verification deferred.

- ID: WORLD-01-GUIDE
- Subsystem: world interaction/navigation
- Reference revision: v0.1.73 consolidation; detailed original scopes retained
- Source status: selected native/supplied contracts consolidated and bounded audit complete
- Runtime status: untested; deferred
- Baselines: ENGINE1011, BETA150 main and ZIP142; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

WORLD-01 coverage inventory, WORLD-02 spatial contracts, WORLD-03 interaction/travel/marker lifecycle and WORLD-04 supplied consumers/consolidation/audit complete the planned available-source pass **within selected scope**. Effective installed integration remains **partial**. [Completion status](source-completion-status.md), [audit](../../08-research/verification-2026-10-12-v0.1.73.md).

## Choose the state owner and operation

| Concern | Established distinction | Canonical evidence |
| --- | --- | --- |
| Lookup/location | Server identity, live client wrapper, level/game vertex and patrol index differ; geometric nearest is not route eligibility | [Spatial behavior](spatial-queries-relocation.md), [API](../../02-lua-api/world/spatial-api.md); [A-Life lifetime](../alife/lifecycle-state-reference.md) |
| Relocation/arrival | Simulator graph relocation, actor/NPC transform, member/cache writes and requested destination have separate effects | Spatial P11–P20; [supplied relocation](supplied-consumers.md), S01/S02/S05; existing A-Life movement/arrival |
| Restrictions | Per-client lists, defaults, server dynamic IDs and live restrictor-type updates are different owners | Spatial P21–P30; supplied C06–C10; [extension API](../../02-lua-api/world/consumer-extension-api.md) |
| Use/touch | Void use callbacks, forced-use bool, pickup veto, sampled zone membership and shape intersection differ | [Interaction behavior](interaction-transitions-markers.md), [API](../../02-lua-api/world/interaction-api.md), U-ledger; supplied C01–C05/S11 |
| Actor travel | Contact/dialog/send/accepted save/broadcast/restart versus loaded destination readiness | Interaction T-ledger; [persistence](../persistence/development-reference.md) and A-Life callbacks |
| Markers | Manager identity/entries, script icon bookkeeping, actual/drawn state, notifications and stored fields differ | Interaction M-ledger; supplied S03/S06/S07/S12/S13 |

Evidence IDs are local to their ledgers: [world evidence directory](../../evidence/world/README.md). The [coverage inventory](coverage-inventory.md) retains earlier document pins and reuse boundaries; A-Life graph/offline/realization findings remain canonical rather than copied into new claims.

## Development review questions

1. Identify the representation, campaign/lifecycle identity and coordinate namespace before lookup or mutation. Reacquire live references after spawn/load/teardown; an ID or path-existence test is not full receiver/point readiness.
2. Trace what a request actually writes: graph registry, transform/physics, destination, member bookmarks, restriction defaults or Lua cache. State changes can precede a later path update; no universal atomic relocation or arrival guarantee is established.
3. Locate the actual callback owner and caller return: use callback, forced-use/UI, pickup veto, native contact versus Lua zone-table predicate, manager-added versus queued removal notification. Repeated/missing/mutating callbacks need their own winning dispatcher evidence.
4. Keep actor travel separate from simulator teleport and squad graph notifications. Check silent versus dialog gate, destination producer, optional hook, save/restart and post-load readiness. An enabled flag or true acceptance result is insufficient arrival proof.
5. Track marker object/type, Lua icon fields and rendering policy separately. Compare numeric 0/1 explicitly. Duplicate append, first-match removal, XML defaults, loaded markers and deferred notice/deletion can disagree with script bookkeeping.
6. Find the serializer/restore caller for every field. Server restriction IDs, marker registry fields, native squad state, comments/local caches and current configuration do not autosave one another. Inspect reconstruction/rebinding before claiming UI state restoration.

These are source-derived review questions, not tested runtime recipes. The supplied source highlights cross-method bookkeeping and literal option-path mismatches; neither is diagnosed as an installed bug or modified as part of ADR work.

## Completion and next boundary

Collect the [effective inputs](source-completion-status.md) and reconcile winning binders/smart/jobs/zone/travel/marker/configuration/dispatcher/storage chains. Runtime resumes separately with identified executable/profile and observations. The next general ADR foundation is **configuration/script integration**, beginning by inventorying existing registration/loading/callback/option coverage. [Roadmap](../../ROADMAP.md).
