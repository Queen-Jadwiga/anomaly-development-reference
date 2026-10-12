# Persistence source completion and remaining work

> ADR document set: **v0.1.65**. Research revisions and source/build versions below describe their original scope.

**As of 11 October 2026:** planned selected native, supplied Lua and CtZ persistence research, practical consolidation and bounded final available-source audit are complete within scope. The [development reference](development-reference.md) is usable within those documented source boundaries. Full effective GAMMA/CtZ persistence is **partial**; runtime is **untested** and deferred until the user explicitly resumes it.

## Completed available-source work

| Area | Record/reference | Disposition |
| --- | --- | --- |
| Selected native pipeline and Lua extension phases | [PER-01](../../08-research/investigations/2026-10-11-PER-01-native-save-load.md), [pipeline](native-save-load-pipeline.md) | Requests, serializers, framing, reconstruction and extension boundaries mapped |
| Supplied codec/caller contracts and missing core definitions | [PER-02](../../08-research/investigations/2026-10-11-PER-02-lua-storage.md), [Lua contracts](lua-storage-contracts.md) | Selected formats/aliasing/cleanup mapped; scoped missing-definition scan preserved |
| Pinned CtZ identity/schema/restoration/reconciliation | [PER-03](../../08-research/investigations/2026-10-11-PER-03-ctz-campaign-safety.md), [campaign reference](ctz-campaign-safety.md) | Targeted repairs, numeric rebind/gates and casualty policies mapped |
| Practical consolidation and bounded consistency audit | [PER-04](../../08-research/investigations/2026-10-11-PER-04-persistence-consolidation.md), [audit](../../08-research/verification-2026-10-11-v0.1.53.md) | Planned available-source final step complete |

## Effective contracts still open

| Contract | Required evidence |
| --- | --- |
| Manager/root and campaign pairing | Winning alife_storage_manager/global helpers; root creation/reset, campaign/new-game separation, filename/companion mapping and ID-generation policy |
| Dispatch and phase order | Native hook definitions through effective emitter/listeners, replacement/startup order, encode/write timing and restore/readiness dependencies |
| Types, schema and failures | Winning USE_MARSHAL producer, codecs/CTime persist hooks, binder/pstor implementations, defaults/version migration/rejection, error/retry and transaction policy |
| Cleanup and reconciliation | Effective teardown/server-unregister paths, ID-keyed state removal, CtZ/Warfare reference repair, online/offline and casualty deduplication authority |
| Native/profile correspondence | Actual executable/build/configuration and winning external spawn/config/source dependencies |

Consumer names, binary magic, version comparisons, elapsed delays and successful protected-call attempts do not close those contracts. Existing [A-Life/Warfare](../alife/source-completion-status.md) and [faction](../factions/source-completion-status.md) requirements overlap this backlog; [profile provenance requirements](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md) remain applicable.

## Stopping rule

Close the effective chains and reconcile their evidence before marking complete installed persistence **development-reference ready at source level / runtime pending**. Runtime requires separate explicit user resumption, identified build/profile, repeatable save/load/new-game/level-change/cleanup observations and results. Arbitrary file robustness, every codec type/metatable, all engine save entry points and unrelated API expansion are optional separate investigations, not silently included in this completion claim.

No research conclusions, baseline datasets or historical snapshots are removed. No gameplay/save edits, engine builds, source/assets redistribution or license addition. [Roadmap](../../ROADMAP.md).
