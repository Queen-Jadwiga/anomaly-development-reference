# Evidence manifest

> ADR document set: **v0.1.57**. Research revisions and source/build versions below describe their original scope.

## Current source baselines and ledgers

| Source ID | Artifact / immutable identity | Role |
| --- | --- | --- |
| ENGINE1011 | `xray-monolith-2026.10.11.zip`, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee` | Current native/bundled source snapshot; upstream commit/executable match unknown |
| BETA150 | `WarfareALifeOverhaul_1_5_0_beta3_1.7z`, SHA-256 `9f71999bb44cb6d3e41c431feaf5be4714159522df1fa8d71599ac039946315d` | Supplied Warfare main/optional patch sources; installation unknown |
| ZIP142 | `warfare a-life overhaul gamma.zip`, SHA-256 `566739c68b4597ab417e98ee9e3ce11858f3d42ed29a39d7e3c39ed2d76443a8` | Earlier supplied package comparison |

- [October 11 baseline record](../00-environment/source-baseline-2026-10-11.md).
- [ALIFE-10 lifecycle/callback synthesis ledger](alife/lifecycle-callbacks-2026-10-11.csv): ENGINE1011; 47 entries, 39 source files; original ledger provenance retained.
- [Native configuration/control ledger](alife/configuration-controls-2026-10-11.csv): N01–N18, 18 ENGINE1011 files.
- [Warfare configuration/control ledger](warfare/configuration-controls-2026-10-11.csv): W01–W18, nine BETA150 files with main/optional patch paths distinguished.
- [Faction relation ledger](factions/native-relations-2026-10-11.csv): F01–F18, 18 ENGINE1011 files.
- [Relation persistence ledger](factions/relation-persistence-2026-10-11.csv): P01–P18, 18 ENGINE1011 files.
- [Community mutation ledger](factions/community-mutation-2026-10-11.csv): M01–M19, 19 ENGINE1011 files.
- [Action-goodwill ledger](factions/action-goodwill-2026-10-11.csv): A01–A20, 20 entries across 19 ENGINE1011 files.
- [Warfare faction-consumer ledger](factions/warfare-consumers-2026-10-11.csv): R01–R20, 20 entries across nine BETA150 main files.
- [Native persistence pipeline ledger](persistence/native-pipeline-2026-10-11.csv): S01–S24, ENGINE1011 selected request/storage/binder/packet paths.
- [Lua storage contract ledger](persistence/lua-storage-2026-10-11.csv): L01–L13, ENGINE1011 codec/binder, BETA150 main consumers and CTZ005J callbacks. CTZ005J pins Alpha 0.0.5j commit `eba6660db09353dcc42a195ae6e7e706f4762277`; source blob correspondence checked, installed copy unknown.
- [A-Life ledgers](alife/README.md).
- [Warfare ledgers and package comparisons](warfare/README.md).
- [New claim-ledger schema](templates/source-evidence.csv).
- [Current evidence policy](../08-research/evidence-policy.md).

The archive hashes pin the supplied bytes, not the active game profile. Existing dataset schemas/IDs remain preserved. File-level inventory ledgers and claim-oriented ledgers serve different purposes; exact citations live in their linked records. UI evidence includes historical commit/tag citations and scoped CSVs in [the UI catalog](../02-lua-api/ui/README.md).

## Historical starter manifest — preserved

### Original manifest

## Runtime logs (user-provided in prior Anomaly project conversations)

| ID | File | Supported facts | Limitations |
|---|---|---|---|
| LOG-001 | `xray_erik(20261008-031926).log` | Startup version header | Full font crash trace not yet reproduced in ADR |
| LOG-002 | `xray_erik(20261009-005123).log` | Startup version header | Does not pin Git commit |
| LOG-003 | `xray_erik(20261009-100733).log` | Startup version header | Does not pin Git commit |

## Web sources

| ID | URL | Supports |
|---|---|---|
| WEB-001 | https://github.com/themrdemonized/xray-monolith | Current project lineage, MT-TEST explanation, dated upstream change history |
| WEB-002 | https://github.com/themrdemonized/xray-monolith/releases | Public release history (release-tag matching pending) |
| WEB-003 | https://github.com/bergemon/xray-monolith-anomaly | Alternative fork, not assumed identical |

All version-sensitive engine documentation must cite an exact revision once identified.

- [Inventory ownership evidence](inventory/README.md): ENGINE1011; no new baseline introduced.

[Inventory persistence/reconstruction ledger](inventory/persistence-reconstruction-2026-10-11.csv): ENGINE1011, R01–R15; selected item/owner serialization and reconstruction.
