# Persistence source evidence

> ADR document set: **v0.1.66**. Research revisions and source/build versions below describe their original scope.

- [PER-01 native pipeline ledger](native-pipeline-2026-10-11.csv): S01–S24, ENGINE1011 source paths/hashes/ranges; IDs are ledger-local.
- [Reference](../../04-game-systems/persistence/native-save-load-pipeline.md), [extension contracts](../../02-lua-api/persistence/native-extension-contracts.md), [investigation](../../08-research/investigations/2026-10-11-PER-01-native-save-load.md).

[ALIFE-04 evidence](../alife/save-load-evidence-oct11.csv) and [FAC-02 evidence](../factions/relation-persistence-2026-10-11.csv) remain preserved in their original subsystem ledgers. Snapshot pins do not certify installed executables or Lua storage/schema behavior. [Evidence policy](../../08-research/evidence-policy.md).

- [PER-02 Lua storage ledger](lua-storage-2026-10-11.csv): L01–L13, 13 entries across ten ENGINE1011/BETA150/CTZ005J files; [reference](../../04-game-systems/persistence/lua-storage-contracts.md).

- [PER-03 campaign ledger](ctz-campaign-safety-2026-10-11.csv): C01–C13, one pinned CTZ005J file; [reference](../../04-game-systems/persistence/ctz-campaign-safety.md).

[PER-04 synthesis](../../08-research/investigations/2026-10-11-PER-04-persistence-consolidation.md) reuses these three original ledgers; no duplicate evidence IDs/dataset. [Development reference](../../04-game-systems/persistence/development-reference.md), [completion rule](../../04-game-systems/persistence/source-completion-status.md).
