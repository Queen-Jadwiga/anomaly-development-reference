# Verification — 2026-10-12 — ADR v0.1.60

> ADR document set: **v0.1.67**. Research revisions and source/build versions below describe their original scope.

- Target ADR revision: v0.1.60, based on main `b72967058951166f33ad46eaac6fc9f92562f4de`
- Changed scope: REV-01 external feedback intake; scoped property extraction; build/history and UI/callback/persistence guidance
- Source baseline IDs: ENGINE1011 uploaded archive; immutable UPSTREAM0912 source; ENV-RT01 external reported build
- Last reviewed: 2026-10-12

## Checks performed

The catalog was regenerated from its original engine/Warfare input roots, and a second isolated generation is compared byte-for-byte. The change adds one `cse_alife_inventory_item.condition` property row, preserving all 1,150 earlier binding rows and the other generated inventories/input ledger. Regression checks cover property recognition, property-only origin validation and unchanged prior binding categories.

Repository links/anchors/CSV widths and current revision banners are checked by the repository validator and its tests. New source ledger paths, ranges and hashes are checked against the declared inputs; immutable September files are compared with the retrieved tag files. Original historical evidence ledgers and history snapshots remain unchanged.

## Results and corrections

The repository checker passes: **199 Markdown files, 1,453 local targets, 23 anchors, zero errors**. All **10 unit tests** pass (seven repository-validator regressions and three binding-pattern regressions). Isolated catalog regeneration is byte-identical. Six new source file hashes/ranges pass, and the four September source files match their immutable commit retrieval. Every earlier evidence CSV and history snapshot remains byte-identical. Source/catalog corrections are separate from externally reported observations and inferred mechanisms. The report preserves issue URLs, reporter/setup/timestamps/body hashes and missing artifacts; no independent game test ran.

## Publication verification

Publish only after checks pass. Verify the resulting main head and complete path/blob map, then close #3/#4 as completed catalog/documentation intake; leave #1/#2 open. The published commit identifies this record; no final SHA is fabricated in advance.

## Remaining limitations

UI crash causes, load-readiness gates, effective installed callbacks/wrappers/PDA XML, exact executable/profile correspondence and raw log/probe/save artifacts remain unresolved. LuaJIT iteration, header/version observations and a reported workaround do not certify universal engine or CtZ behavior. Independent runtime testing stays deferred. No CtZ code, engine assets/source or license changes are included.
