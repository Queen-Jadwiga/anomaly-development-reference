# Persistence development reference

> ADR document set: **v0.1.54**. Research revisions and source/build versions below describe their original scope.

**Research revision: v0.1.53.** Selected native, supplied Lua and CtZ persistence research is consolidated for development use within its source boundaries. Effective installed persistence remains partial; runtime is untested and deferred until explicitly resumed by the user. [Completion rule](source-completion-status.md), [PER-04 record](../../08-research/investigations/2026-10-11-PER-04-persistence-consolidation.md), [audit](../../08-research/verification-2026-10-11-v0.1.53.md).

## Start with the data owner

Choose the layer that explicitly serializes the field before choosing a callback. A table assignment, a save request or an available codec alone does not establish durable storage. The following is guidance derived from the selected implementations, not a new universal storage API.

| Data or question | Established source contract | Start here |
| --- | --- | --- |
| Native server object state | Filtered spawn/update packets, root/child selection, explicit registries | [Native pipeline](native-save-load-pipeline.md); PER-01 S09–S14/S21 |
| Client binder custom bytes | Save relevance, native then binder output, retained client_data, load during client realization | [Native extension APIs](../../02-lua-api/persistence/native-extension-contracts.md); PER-01 S07/S08/S15–S19 |
| Shared addon tables | Selected consumers attach namespaces; emitter, encode timing, manager/root lifetime remain missing | [Lua storage contracts](lua-storage-contracts.md); PER-02 L06–L08/L10/L13 |
| Scalar pstor | Selected non-Marshal tags and separate CTime stream; Marshal branch forwards callbacks | [Lua API contracts](../../02-lua-api/persistence/lua-storage-api.md); PER-02 L09 |
| Marshal values | Binary codec/reference and custom restore mechanics, separate from file/schema policy | PER-02 L01–L05; [codec reference](lua-storage-contracts.md) |
| Native goodwill versus dynamic diplomacy | Native auxiliary registry and script save/reapply are separate domains | [Faction persistence](../factions/relation-persistence.md); PER-01 S10, PER-02 L11 |
| CtZ strategic campaign | Shared state attachment, targeted load repairs, later numeric rebinding and reconciliation | [CtZ campaign reference](ctz-campaign-safety.md); PER-03 C01–C13 |

Evidence IDs are ledger-local: [PER-01 S-ledger](../../evidence/persistence/native-pipeline-2026-10-11.csv), [PER-02 L-ledger](../../evidence/persistence/lua-storage-2026-10-11.csv), [PER-03 C-ledger](../../evidence/persistence/ctz-campaign-safety-2026-10-11.csv). ENGINE1011, BETA150 and CTZ005J are pinned artifacts in the [manifest](../../evidence/manifest.md), not proven installed winners. Do not compose their branches into one verified active profile.

## Save and load phase contracts

| Phase | What source establishes | What it does not establish |
| --- | --- | --- |
| Packet save preparation | ClientSend then ClientSave before filename save | Direct filename calls have the same preparation; universal transport acknowledgement |
| Native save hooks | Conditional before-save functor before memory serialization; save functor after native writer closes | Shared callback listener/encoder timing or companion atomicity |
| File validity predicate | Length >= 8, sentinel, outer version >= native constant | Whole-save integrity, addon compatibility or arbitrary forward schema support |
| Early native load hook | Runs before reading native chunks in buffer reconstruction | Restored native objects/registries or client readiness |
| Native registration | Objects reserved/inserted, auxiliary registry load, enabled final on_register | Late group/member repair already complete |
| Late native repair | Filename loader invokes group on_after_game_load after buffer function | All client spawn/binder or addon reconciliation complete |
| Binder load | During selected base client spawn, from retained custom bytes | Whole-world readiness |
| CtZ load callback | Shared state assignment and presence/role-based repairs | Saved-version dispatch, full shape validation or identity certification |
| CtZ actor restore/validation | Readiness/grace guards, ownership/member setup, role-dependent routing and accounting | Guaranteed registration completion, transaction success or universal idempotence |

PER-01 S01–S04/S07/S13–S20/S24; PER-03 C02/C06–C13. The native load request only prepares options; it is not disk reconstruction. A callback named load or on_game_load needs its producer traced before placing it on this timeline. The connection between named native hooks, effective shared-table dispatch, encoding/files and CtZ callbacks remains unresolved. See [A-Life callback phases](../alife/callback-phase-reference.md).

## Practical design and diagnosis questions

Use these questions when reviewing a persistent field or investigating a load discrepancy; they are source-derived review guidance, not a certified save-repair recipe.

1. **Ownership:** which explicit serializer writes it, and does that path actually run under the winning binder/mode? Native object filtering/relevance and commented squad methods matter. PER-01 S09/S15–S19; PER-02 L07/L09/L12.
2. **Snapshot:** is the stored value copied or aliased, and when does the effective encoder run? Warfare/CtZ namespace assignments can retain live table references; later listeners can mutate shared input. PER-02 L06/L10/L13.
3. **Schema and versions:** distinguish ADR revision, engine ALIFE_VERSION, package release, internal campaign VERSION and SAVE_VERSION. CtZ's selected load stamps schema 9 without reading a saved version for rejection/dispatch; targeted repairs are not arbitrary compatibility. PER-01 S02–S04; PER-03 C01/C02.
4. **Identity:** a save filename, scenario string or numeric object ID is not an independently demonstrated campaign/generation fingerprint. Identify campaign pairing/reset and ID cleanup before rebinding references. CtZ selected lookups/reclamation do not perform an independent identity comparison. PER-02 L07/L08; PER-03 C04/C05/C08/C09; [ALIFE-04](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md).
5. **Dependencies:** distinguish deserialize, native registry restoration, late member repair, client realization and addon world mutation. Cross-object work needs an established phase, not just a callback name or delay. PER-01 S01/S13–S15; PER-03 C06–C08/C13.
6. **Failures and repeats:** binder exceptions clear the binder, unsupported scalar pstor values are not safely skipped by a proven format policy, and protected CtZ setup/transfer calls can hide partial effects. Require evidence for rollback/retry/deduplication rather than assuming successful native continuation means successful addon persistence. PER-01 S16; PER-02 L09; PER-03 C08/C09.
7. **Accounting and time:** CtZ ignores MISSING for immediate core loss reconciliation, then applies timed/engagement-specific classification. Its economy migration anchors later; persisted missing timers and game-clock rewinds have separate effects. Keep death observations separate from casualty authority. PER-03 C01/C03/C10–C13.

For a future runtime report, record executable/build, winning files/settings, campaign/save identity, reproduction, logs and outcomes. Runtime work is still deferred; this list does not authorize engine execution or save modification.

## Required effective-source closure

Obtain the actual winning manager/global/dispatcher definitions, binders and addon replacements with their dependencies and configuration provenance. Trace root construction/reset, native hook to emitter/listeners to encoding/file write, type/default/schema/version contracts, errors, companion coordination, cleanup and restore order. Then reconcile those findings with the native and CtZ references. [Source completion requirements](source-completion-status.md), [profile collection requirements](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md).

PER-01–04 finish the planned available-source persistence work. Missing effective sources and runtime remain separate open work. Another subsystem can proceed independently without promoting these boundaries to verified installed behavior. [Roadmap](../../ROADMAP.md).
