# Persistence

> ADR document set: **v0.1.78**. Research revisions and source/build versions below describe their original scope.

**Current revision: v0.1.78.** Available-source research/consolidation status: complete within selected scope. Full effective installed storage/schema behavior remains partial; runtime is unverified. Runtime verification is deferred until explicitly resumed by the user.

Start with the [development reference](development-reference.md) and [completion status](source-completion-status.md).

- [Native save/load pipeline](native-save-load-pipeline.md).
- [Native Lua extension contracts](../../02-lua-api/persistence/native-extension-contracts.md).
- [PER-01 investigation](../../08-research/investigations/2026-10-11-PER-01-native-save-load.md).
- [Source evidence](../../evidence/persistence/README.md).

Existing [ALIFE-04](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md), [A-Life callbacks](../alife/callback-phase-reference.md) and [FAC-02](../factions/relation-persistence.md) remain the detailed identity/member/relations foundations.

[Supplied Lua storage contracts/effective gaps](lua-storage-contracts.md), [focused codec/caller APIs](../../02-lua-api/persistence/lua-storage-api.md) and [PER-02](../../08-research/investigations/2026-10-11-PER-02-lua-storage.md) are complete within scope; core effective storage remains partial.

[CtZ campaign safety](ctz-campaign-safety.md) and [PER-03](../../08-research/investigations/2026-10-11-PER-03-ctz-campaign-safety.md) are complete within selected source scope. [Practical development reference](development-reference.md), [completion status](source-completion-status.md) and [PER-04 consolidation/audit](../../08-research/investigations/2026-10-11-PER-04-persistence-consolidation.md) complete the planned available-source work. Next: effective-source closure when winning files are available; another subsystem can proceed independently. See [roadmap](../../ROADMAP.md).
