# Whole-reference audit evidence

> ADR document set: **v0.1.83**. Research revisions and source/build versions below describe their original scope.

ADR-01 audits baseline v0.1.81 commit `dc826c78041971cac96710b329b6ce85905e8e13`. The scope is every baseline file/dataset structure and current provenance/navigation/completion contracts, not every native interpretation or installed profile. [Status](../../08-research/reference-status.md), [provenance](../../00-environment/provenance-register.md), [investigation](../../08-research/investigations/2026-10-12-ADR-01-whole-reference-audit.md).

| Dataset | Schema and meaning |
| --- | --- |
| [Base file inventory](base-file-inventory-2026-10-12.csv) | 378 original paths, category/role, bytes/raw SHA-256 and immutable ADR base commit; includes 304 Markdown pages, not semantic certification of each |
| [Ledger integrity/classification](ledger-integrity-2026-10-12.csv) | All 59 baseline CSV datasets: raw hash, rows, purpose, checked/unchecked rows, checked range groups, outcome and explicit limits; original schemas remain unchanged |
| [Entry contracts](entry-contracts-2026-10-12.csv) | Eleven behavior entries: original README/guide/status paths and 33 raw hashes, scoped audit, effective/runtime disposition, shared Warfare rule and review boundary |
| [Corrections](corrections-2026-10-12.csv) | 19 current navigation/provenance/test-maintenance boundaries, original path/raw hash, basis/disposition and scope; grouped guide annotations are described explicitly |
| [Audit summary](audit-summary-2026-10-12.json) | Baseline counts, classification totals, integrity check scope and exceptions; independent runtime deferred |

Source/file integrity passes for **938 rows**, **1,322 cited range groups**, **334 distinct available artifact-relative source paths**. This includes repeated claims and file-only ledgers; it is not 938 distinct native APIs. Existing ENGINE1011/BETA150/ZIP142/CTZ005J roots and legacy aliases are mapped for these checks only. Source paths/hash/range integrity does not certify every symbol, converter, branch or interpretation anew.

All **102 earlier reference rows** pass at their original immutable revisions: WORLD-01 v0.1.69, CONFIG-01 v0.1.73, ARCH-01 v0.1.77, ARCH-02 v0.1.78, DEBUG-01 v0.1.79 and ARCH-03 v0.1.80. Current banner-updated pages intentionally have different bytes. Four UPSTREAM0912 source rows retain their immutable remote commit/hash pins; local September source is unavailable, so no local rehash result is claimed.

Eight generated API CSVs, three comparison CSVs, the external observation ledger, historical migration ledger and empty source template are inventoried under their own purpose. Full API regeneration, historical May source revalidation, comparison re-execution and independent external-report reproduction are not claimed. Seven baseline JSON datasets parse; their original specialized scope records remain authoritative. No original evidence dataset is normalized or replaced.

Reproduce file/reference checks against each declared original ADR revision; source checks require the original artifacts recorded in the [manifest](../manifest.md). Audit CSV/JSON bytes reproduce from those inputs; semantic review is manual and bounded to current roles/qualification/status/navigation. A complete file index is not an engine coverage inventory. [Verification](../../08-research/verification-2026-10-12-v0.1.82.md). No third-party source/assets/logs/dumps or CtZ gameplay changes.
