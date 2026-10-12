# Inventory consolidation and bounded audit — v0.1.58

> ADR document set: **v0.1.59**. Research revisions and source/build versions below describe their original scope.

- Date: 2026-10-11
- Investigation: ITEM-05
- Scope: selected ITEM-01–04 references, focused APIs and cross-system consistency
- Runtime: untested; deferred until explicitly resumed
- Publication base: v0.1.57, commit `20f709bf8bd79213e8a8a9ae721cb067f3ecf97e`

## Baseline and audit boundary

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit, installed build/profile and winning scripts unknown. Reuse [inventory ledgers](../evidence/inventory/README.md), 72 rows. Semantic review reread selected risk-bearing implementations/callers; all row metadata received mechanical integrity checks. These are distinct checks; this is not a fresh exhaustive engine-wide trace or effective-script audit.

## Bounded semantic review

| Reviewed boundary | Evidence checked against source | Outcome |
| --- | --- | --- |
| Server containment versus live parenting/membership | I01/I02/I08/I09/I11 | Distinct owners and mutation stages retained; no atomic transfer claim |
| Actor/base-owner take/drop phases | I01/I02/I04/I05; R14 | Take precedes final weight/UI; drop callback precedes parent detach; pending slot request follows take callback |
| Slot/belt/ruck metadata and attachment | P01/P02/P06 | Unequal callback snapshots retained |
| Ordinary predicates versus strict restoration | P01–P03; R12/R13 | Clarify current ITEM-04 wording: strict Take bypasses ordinary predicates; fallback is not eligibility/migration proof |
| Current/next slot and readiness | P04/P05/P17/P18 | Server/HUD/hidden/block gates and forced-assignment distinction retained |
| Lua transfer/placement request contracts | I14/I18/I19; P07/P10/P11 | Void requests, split payloads, commented preflight and filtered iteration retained |
| Consumption effects/return/parent assumptions | D01–D03/D05/D13 | Post-effect false and direct wrapper/event-gate distinction retained; clarify required non-null parent invariant |
| Destruction and owner teardown | D06/D07/D10–D12 | Request/server/live stages and Clear versus per-item mutation retained; no robust malformed-relationship claim |
| Saved fields and derived initialization | R01–R10/R15 | Server STATE/UPDATE/client bytes kept distinct; later initialization and single-player base update limit retained |
| Restore callback/activation phases | R11–R14 | Spawn callback before parent take; pending saved-slot activation is not final readiness |
| Cross-system dependencies | Existing A-Life/persistence completion records | Effective death/release, ID/schema and NPC policy remain open; trade names do not establish payment |

No contradiction requiring reversal of selected ITEM-01–04 conclusions found within this scope. Two qualifications above improve current reference precision; dated investigations retain their original bodies. No runtime fault or successful gameplay recipe asserted.

## Preservation and structural/source checks

- Compare all base local blobs with the inspected published v0.1.57 tree before edits; preserve every prior path.
- Preserve all prior CSV datasets and three marked history snapshots byte for byte; preserve prior dated investigation bodies except current version banners.
- Verify all hash-bearing evidence rows against retained engine/package/CtZ inputs, recorded line counts, range bounds and symbols; inventory rows also receive symbol-in-cited-range review where the ledger identifies the symbol.
- Compare six unchanged generated A-Life catalog files with retained reproduced outputs; no generator/input change.
- Repository checker passes local targets/anchors, required routes, VERSION/current banners, CSV widths, nonempty files and forwarding-page checks. Seven existing validator tests pass.
- Publish using expected-head lease; compare complete remote path/blob map, read back VERSION/new reference/status and verify main head.

Actual checks: 527 hash-bearing evidence rows and 705 range groups validated across all ledgers; all 72 inventory entries across 36 source files passed hash/count/range/symbol checks including symbol occurrence within cited ranges. Preserved 35 prior CSV datasets, three history snapshots and 49 prior dated investigation bodies (banner changes only). Repository checker inspected 190 Markdown files, 1,367 local targets and 15 anchors; seven validator tests passed. Structural validity, correct hashes or source-name occurrence alone do not establish semantic coverage, effective delivery, binary compatibility or runtime success.

## Disposition

Selected available-source inventory first-edition foundation, practical consolidation and bounded audit complete within scope. [Effective installed integration](../04-game-systems/inventory/source-completion-status.md) partial; runtime deferred. Next general foundations: trade/economy. [Reference](../04-game-systems/inventory/development-reference.md), [investigation](investigations/2026-10-11-ITEM-05-inventory-consolidation.md), [roadmap](../ROADMAP.md). No game/save/source edits, engine build, third-party source/assets redistribution or license addition.
