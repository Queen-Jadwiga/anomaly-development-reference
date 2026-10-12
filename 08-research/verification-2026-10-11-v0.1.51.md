# PER-02 increment verification — v0.1.51

> ADR document set: **v0.1.71**. Research revisions and source/build versions below describe their original scope.

- Date: 2026-10-11
- Scope: supplied Lua codec/caller contracts and bounded effective-profile gaps
- Source status: source-confirmed selected implementations/callers; scoped missing-definition scan
- Runtime status: untested; deferred until explicitly resumed by the user
- Publication base: v0.1.50, commit `81c969547f6a80677d2ba4e9b7e8c50f827f4a3f`

## Source review and pins

ENGINE1011 and BETA150 archive pins are recorded in [PER-02](investigations/2026-10-11-PER-02-lua-storage.md). CTZ005J pins commit `eba6660db09353dcc42a195ae6e7e706f4762277`; campaign-script local blob `25638cc5ae5ed81ceddacf6c16f39f53a5f4d791` matches that commit's retrieved Git tree entry. Actual engine executable, installed winners/settings and native injected symbols remain unknown.

[New ledger](../evidence/persistence/lua-storage-2026-10-11.csv): 13 entries across ten files, 21 range groups. Read Marshal API/type/reference/custom restore/error paths and extension startup; shared argument forwarding; selected binder mode/fields/cleanup; main pstor scalar/CTime format; active versus commented squad serialization; Warfare namespace assignment/restore-clear, diplomacy helper calls and minimal CtZ table attachment/registration.

Compared codec capability with storage policy, plain references with deep-copy claims, callback consumers with missing emitter/encode timing, scalar tags with unsupported-type branches, and native/binder/shared storage phases. No full decoder robustness/portability certification or runtime experiment was performed.

Scoped search covered 110 script files in ENGINE1011 gamedata, complete BETA150 and CtZ gamedata. No core manager/global files or selected named function/assignment definitions were found under the declared search rules. Alias resolution, native injected symbols, ZIP142 and installed files are outside that negative finding. Exact requested winning definitions/closure questions remain in the [reference](../04-game-systems/persistence/lua-storage-contracts.md).

## Preservation and repository checks

- Compared every local base blob with the published v0.1.50 tree; no files deleted.
- Preserved all 29 previous CSV datasets byte for byte, all 42 dated investigation bodies except current document-set banners, and all three historical snapshots byte for byte. CtZ repository/source files were read only.
- Verified 442 hash-bearing evidence rows against retained snapshots: full-file SHA-256, recorded counts, 587 range groups and symbols where present. Datasets without compatible path/hash fields remain outside this hash pass; original comparisons remain preserved.
- New ledger symbols occur within their cited ranges. Source bytes are preserved; ASCII symbol checks use replacement decoding where source text is not UTF-8.
- Six unchanged ALIFE-09 catalog files match earlier reproduced outputs; extractor/input scope unchanged.
- Repository checker passed: 162 Markdown files, 1,059 local targets, 14 anchors and zero errors. Checks cover Markdown targets/anchors, required C-03/C-04/CtZ routes, VERSION/banners, nonempty files, CSV widths and absence of forwarding pages. Seven existing validator tests pass.
- Publish using inspected base tree/expected-head lease; compare full remote path/blob map, read back increment/VERSION and verify main head.

## Disposition and limits

PER-02 closes this bounded codec/caller/gap investigation. Complete effective Lua storage remains partial: core manager/global implementations, schemas/type/default/ownership policy, hook→dispatcher→encoder/file chain, cleanup and companion coordination require actual winning sources. Next is PER-03 CtZ campaign identity/schema/restoration/reconciliation; eventual consolidation/audit remains open. Runtime is deferred; no engine build, gameplay/save edits, source/assets distribution or license addition. [Roadmap](../ROADMAP.md).
