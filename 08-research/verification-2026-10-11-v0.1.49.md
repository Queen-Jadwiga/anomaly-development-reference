# Faction consolidation and final available-source audit — v0.1.49

> ADR document set: **v0.1.77**. Research revisions and source/build versions below describe their original scope.

- Date: 2026-10-11
- Scope: FAC-01–05 practical consolidation, bounded semantic consistency and repository integrity
- Source status: selected source-confirmed findings; audit is bounded, not exhaustive
- Runtime status: untested; deferred until explicitly resumed by the user
- Publication base: v0.1.48, commit `fa06e2753d1800c7b1fb6b9eda870faeb3b1c4a8`

## Completion and provenance

FAC-06 completes the planned available-source faction consolidation and final bounded audit, now authorized after FAC-05. [Practical reference](../04-game-systems/factions/development-reference.md) and [completion status](../04-game-systems/factions/source-completion-status.md) keep effective GAMMA/CtZ integration partial.

ENGINE1011 archive hash `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee` and BETA150 archive hash `9f71999bb44cb6d3e41c431feaf5be4714159522df1fa8d71599ac039946315d` pin the native/supplied inputs. Engine upstream commit/executable and installed winners/settings remain unknown. BETA150 findings select main-package paths, not an assumed optional-patch combination.

## Bounded source-consistency review

Compared the five investigation/reference scopes, three focused API pages, original ledgers and adjacent A-Life/Warfare boundaries. Re-read high-impact native/helpers during this pass. The table identifies audited interpretations, not a certificate for every sentence, converter, build, variant or runtime behavior.

| Boundary | Audited consistent interpretation | Basis |
| --- | --- | --- |
| Identity versus ownership | Configured community, live tuple, script mapping and strategic owner remain distinct | FAC-01 F01–F04; FAC-03 M01–M04; FAC-05 R07–R09/R15 |
| Direction/storage | Matrix is directed; community goodwill is community → target, stored with target | FAC-01 F01/F06/F09; FAC-05 R02 |
| Aggregate getters | Object general-goodwill has five terms; server-ID helper has three | FAC-01 F05/F09/F10; re-read registry/template and level helper |
| Relation classification | Native virtual/full-attitude path differs from BETA150 matrix predicates/display averages | FAC-01 F13–F17; FAC-05 R01/R02/R11/R12/R18 |
| Relation setters | Enum preset does not compensate full attitude; force-set subtracts only community terms | FAC-01 F05/F06; re-read SetRelationType/ForceSetGoodwill |
| Saved state versus caches | Native records serialize; matrix cache resets; supplied script explicitly saves/reapplies separately | FAC-02 P01–P08/P13–P18; FAC-05 R03/R06 |
| Restore phases | Final native registration follows relation load; installed Lua restore order remains open | FAC-02 P08/P10; re-read load and script callback registration |
| Clear versus ID purge | One record's maps clear; no inbound sweep or outer erase in that function | FAC-02 P02/P09/P17; re-read ClearRelations |
| Community versus tuple mutation | Two-stage live migration/partial phases; direct server community write differs from tuple packet receipt | FAC-03 M01/M02/M04/M06/M11/M17/M19 |
| Actions and independent outcomes | Goodwill nesting/exclusions differ from reputation and kill-rank gates | FAC-04 A01–A07/A12; re-read kill outcome gate nesting |
| Flags/observation | Zero kill mask is not an independent event bit; flags/callbacks do not certify all awards or cleanup | FAC-04 A01/A03/A09/A14/A18/A20; re-read flags implementation |
| Native/script integration | Offline outcome, dynamic diplomacy and actor support differ; no total convergence/deduplication asserted | FAC-04 and FAC-05 R04/R05/R13/R17/R20; WAR-002b |

Ledger labels are local to their respective [five original datasets](../evidence/factions/README.md). Findings remain consistent at these selected boundaries. No new substantive source correction was required. Current references/roadmap did contain earlier next-step wording, which is updated to completed follow-ups and the current effective-source backlog; dated investigations retain their historical dispositions.

## Integrity, preservation and checks

- Compared every local base blob against the published v0.1.48 tree before constructing the increment. No files deleted.
- Preserved all 28 prior CSV datasets byte for byte, all 40 dated investigation bodies except current document-set banners, and all three historical snapshots byte for byte.
- Verified all five faction ledgers: 95 entries, 62 distinct pinned source files, 148 range groups; SHA-256/count/range checks pass and recorded symbols occur inside cited ranges. No duplicate synthesis ledger replaces their provenance.
- Repository-wide compatible ledger check resolved 405 hash-bearing rows against retained snapshots, verified recorded line counts and 533 range groups, and checked symbols where recorded. Datasets without compatible path/hash fields remain outside this hash pass; comparison datasets are preserved.
- Six ALIFE-09 catalog outputs remain unchanged and match earlier reproduced files; no extractor/input change.
- Repository checker passed: 153 Markdown files, 965 local targets, 14 anchors and zero errors. Checks cover Markdown targets/anchors, C-03/C-04/CtZ required routes, current VERSION/banners, nonempty files, CSV widths and absence of obsolete forwarding pages. Seven existing validator tests pass.
- Publish from inspected base tree with expected-head lease; verify the full remote path/blob map, read back new references/record/report and VERSION, and verify the published main head.

## Remaining limits and disposition

Available-source research/consolidation/audit is complete within the planned scope. Effective identity/diplomacy, storage/dispatch, rewards/death and strategic/CtZ contracts remain required; [completion rule](../04-game-systems/factions/source-completion-status.md) lists sources/closure boundaries. All in-game verification remains deferred. No engine build, gameplay edits, script fixes, third-party source/assets redistribution or license addition. [Roadmap](../ROADMAP.md).
