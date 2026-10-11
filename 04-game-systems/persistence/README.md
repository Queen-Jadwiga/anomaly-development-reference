# Persistence

> ADR document set: **v0.1.51**. Research revisions and source/build versions below describe their original scope.

**Current revision: v0.1.51.** Subsystem status: partial. The selected native A-Life pipeline and Lua extension boundaries are documented; installed storage/schema behavior and runtime remain unverified. Runtime verification is deferred until explicitly resumed by the user.

- [Native save/load pipeline](native-save-load-pipeline.md).
- [Native Lua extension contracts](../../02-lua-api/persistence/native-extension-contracts.md).
- [PER-01 investigation](../../08-research/investigations/2026-10-11-PER-01-native-save-load.md).
- [Source evidence](../../evidence/persistence/README.md).

Existing [ALIFE-04](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md), [A-Life callbacks](../alife/callback-phase-reference.md) and [FAC-02](../factions/relation-persistence.md) remain the detailed identity/member/relations foundations.

[Supplied Lua storage contracts/effective gaps](lua-storage-contracts.md), [focused codec/caller APIs](../../02-lua-api/persistence/lua-storage-api.md) and [PER-02](../../08-research/investigations/2026-10-11-PER-02-lua-storage.md) are complete within scope; core effective storage remains partial.

Next: CtZ campaign safety and restoration/reconciliation; practical persistence consolidation and final available-source audit. See [roadmap](../../ROADMAP.md).
