# Evidence manifest

> ADR document set: **v0.1.83**. Research revisions and source/build versions below describe their original scope.

## Current source baselines and ledgers

[Profile evidence](profile/README.md) adds 36 selected core claim rows and six loose/unpacked overlay comparisons; [intake](../00-environment/profile-source-2026-10-12.md) pins uploaded snapshots and private log observations. This supplements package/native baselines without claiming full installed compatibility.

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

## Additional current ledgers and audits

- [Inventory ownership evidence](inventory/README.md): ENGINE1011; no new baseline introduced.

[Inventory persistence/reconstruction ledger](inventory/persistence-reconstruction-2026-10-11.csv): ENGINE1011, R01–R15; selected item/owner serialization and reconstruction.

[Native trade/economy ledger](economy/native-trade-2026-10-11.csv): ENGINE1011, E01–E23; money/pricing/selected UI accounting and Lua contracts.

## External runtime review — REV-01

- [Source comparison ledger](runtime/issue-review-source-2026-10-12.csv): ENGINE1011 property/LuaJIT checks and immutable UPSTREAM0912 registry/dispatcher/native-binding files.
- [Reported observations](runtime/reported-observations-2026-10-12.csv): ten external observations with issue/reporter/timestamp/body-hash provenance, reported setup and limits.
- [Environment record](../00-environment/reported-gamma-runtime-2026-10-12.md) and [review/disposition](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md). No raw third-party source, logs or private profile assets are redistributed.

[Trader configuration/supply ledger](economy/trader-configuration-2026-10-12.csv): T01–T21, ENGINE1011/BETA150; [supplied source scope](economy/supplied-source-scope-2026-10-12.json) records missing core definitions across ENGINE1011 gamedata/BETA150/ZIP142.

[Gameplay condition ledger](gameplay/native-condition-2026-10-12.csv): G01–G21, ENGINE1011; selected base condition/live hit, Lua properties and supplied mutable callback relay.

[Actor effects/equipment ledger](gameplay/actor-effects-2026-10-12.csv): A01–A21, ENGINE1011; actor survival, medicine/boosters, Lua helpers and selected armor/artefact formulas.

[Death/condition restoration ledger](gameplay/death-restoration-2026-10-12.csv): R01–R19, ENGINE1011/BETA150; selected derived death and server/live/custom-data reconstruction.

[Native tasks/dialogue/info ledger](tasks/native-task-dialogue-info-2026-10-12.csv): T01–T18, ENGINE1011; selected lifecycle, info storage and phrase helper/caller paths.

[Task/dialogue supplied-consumer ledger](tasks/supplied-consumers-2026-10-12.csv): L01–L16, BETA150 main and ZIP142; offer/setup/stage/turn-in/reward/restoration callers and alternative dispatcher comparison. No new source artifact or installed-winner claim.

[World coverage inventory](world/README.md): 14 document-reference rows pinned to immutable ADR v0.1.69; coverage classification and next-step allocation, not a new native claim ledger or engine baseline.

[World spatial/contracts source ledger](world/spatial-contracts-2026-10-12.csv): P01–P40, ENGINE1011; selected native exports/definitions/callers, input-output policy and two bundled callers. [World evidence](world/README.md).

[World interaction/transition/marker ledger](world/interaction-transition-markers-2026-10-12.csv): U01–U16, T01–T13, M01–M19, ENGINE1011; selected use/touch/travel/ordinary-marker lifecycle and one bundled relay, not full installed consumers.

[World supplied-consumer ledger and scope/comparison records](world/README.md): WORLD-04, ENGINE1011/BETA150 main/ZIP142; selected callers, configuration requests, focused native restriction extensions and bounded inventory/comparison. No new source artifact or installed winner is introduced.

[Configuration/script-integration coverage ledger](configuration/README.md): CONFIG-01, 18 existing-documentation rows at ADR v0.1.73 immutable main commit. Inherited source/runtime confidence; no new native contract or source artifact.

[CONFIG-02 LTX/INI/DLTX source ledger](configuration/ltx-ini-dltx-2026-10-12.csv): 50 ENGINE1011 rows across 21 files/72 cited range groups; selected settings/parser/merge/cache/read/write/Lua/policy/helper contracts. Archive pin retained, upstream commit/executable correspondence unknown.

[CONFIG-03 loading/startup/callback ledger](configuration/script-loading-callbacks-2026-10-12.csv): 35 ENGINE1011 rows, 14 files/47 range groups; [scoped availability](configuration/script-source-scope-2026-10-12.json). Explicit WORLD-04 C12/CONFIG-01 K08 five-event correction preserves original CSV bytes; no installed/global winner inferred.

[CONFIG-04 supplied consumer ledger](configuration/supplied-options-patches-2026-10-12.csv): 29 ENGINE1011/BETA150 main/explicit optional variant rows, 15 files/37 ranges; [seven raw/slice comparisons](configuration/package-comparison-2026-10-12.csv) and [scoped inputs](configuration/supplied-source-scope-2026-10-12.json). Full CONFIG-02–04 bounded audit covers 114 source rows/156 ranges; no installed winner or runtime certification.

[Practical architecture/debugging inventory](architecture/README.md): ARCH-01, 22 existing-documentation rows pinned at ADR v0.1.77 immutable main commit. Original source/build/external confidence retained; no new native/logger/API/runtime contract or source artifact.

[ARCH-02 ownership/compatibility synthesis](architecture/README.md): 26 section pins in nine documents at immutable ADR v0.1.78. Documentation synthesis and explicitly proposed design contracts; inherited source/build/external scopes retained. No new engine/API/runtime guarantee or third-party source artifact.

[DEBUG-01 diagnostic evidence](debugging/README.md): ENGINE1011 selected native/Lua logger, writer, build, stack, assertion/error, Luabind/binder/panic and Windows filter/dump routes; 41 rows/67 ranges/21 files plus six immutable ADR v0.1.79 documentation pins. Four Lua exports/converter qualified; triage is recommended guidance. Unknown binary/profile correspondence, missing installed aliases and deferred runtime retained. No third-party source/assets.

[ARCH-03 qualified patterns/practical audit](architecture/README.md): 16 immutable ADR v0.1.80 reference/test-source rows; recheck 54 earlier reference rows and 41 DEBUG-01 source rows/67 ranges/21 files. Four proposed protocols and two linked non-runnable UI sketches, implemented ADR test inventory and consolidated guidance. No new engine API, runnable framework/fixture, runtime result or whole-ADR audit.

## Whole-reference audit and provenance

[ADR-01 inventory/integrity/corrections](reference/README.md) covers every baseline file and dataset schema, rechecks available source/reference pins and records exceptions. [Provenance register](../00-environment/provenance-register.md) also distinguishes CTZ005J, UPSTREAM0912, the historical May UI pin, binary candidate and runtime/report identities. Original ledger schemas/IDs remain unchanged.

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

