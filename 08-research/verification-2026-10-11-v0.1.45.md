# FAC-02 source and repository verification — v0.1.45

> ADR document set: **v0.1.76**. Research revisions and source/build versions below describe their original scope.

- Date: 2026-10-11
- Scope: native relation persistence/reset/ID cleanup and navigation
- Source status: source-confirmed within selected paths; negative serializer/cleanup conclusions remain bounded
- Runtime status: untested; deferred until explicitly resumed by the user
- Publication base: v0.1.44, commit `3a5b88dd1628a027fe2e839af637d153c2a74c9a`

## Source and semantic checks

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee` pins the source snapshot. Exact upstream commit/executable and installed scripts/configuration remain unknown.

The [FAC-02 ledger](../evidence/factions/relation-persistence-2026-10-11.csv) records 18 files and 26 range groups. Read record/container/wrapper serializers and ownership; native save/load and callback gating; monster unregister and object-registry destruction; simulator unload/reload; character table reset/lazy reload and module detach. Scoped `src/` searches for reset/clear/matrix symbols support the selected trace, not an installed-wide negative assertion.

Reviewed these distinctions against the implementation:

- Saved per-character personal/community contributions versus static community matrix/sympathy caches.
- Final native registration loop after auxiliary registry restoration versus earlier hooks and unknown effective Lua dispatch.
- Clearing one record's maps versus erasing the outer record or sweeping incoming personal references.
- Ordinary client teardown/death versus server unregister and simulator owner disposal.
- Current A-Life registry routing versus no-A-Life local fallback; wrapper deletion versus simulator data deletion.

The [reference](../04-game-systems/factions/relation-persistence.md) identifies conditional ID-reuse risk without claiming a runtime defect, and leaves addon diplomacy save/reapply, all overrides and callback order open. No native matrix durability is inferred from a different serializer.

## Repository and preservation checks

- Compared every base snapshot blob with the published v0.1.44 tree. No repository files deleted.
- Preserved all 24 existing CSV datasets byte for byte, all 36 prior investigation bodies except current document-set banners, and all three historical snapshots byte for byte.
- Verified 346 hash-bearing evidence rows against retained source snapshots: full-file SHA-256, recorded line counts, 443 range groups and symbols where present. Datasets without compatible path/hash fields are outside this hash pass; existing comparison datasets remain preserved.
- New ledger symbols were also checked within their cited range groups, not only somewhere in the file. Structural validity is not a substitute for semantic review.
- Six ALIFE-09 catalog outputs remain unchanged and match the outputs reproduced in v0.1.43; no extractor/input change requires a new extraction.
- Repository checker passed: 138 Markdown files, 768 local targets, 14 anchors and zero errors. It validates local Markdown targets/anchors, C-03/C-04/CtZ navigation, current VERSION/banners, nonempty files, CSV widths and absence of forwarding pages. Seven existing validator tests pass.
- Publication uses the inspected base tree and expected-head lease. Compare full remote path/blob identities, read back the increment and VERSION, and verify main points to the intended commit.

## Disposition and limits

FAC-02 completes its bounded native persistence/reset/cleanup question; factions/relations remains partial. Next is community mutation, then action-driven goodwill and effective Warfare/diplomacy integration. Previous findings remain preserved; current references link this follow-up without rewriting dated research conclusions. No engine compilation, gameplay edits, third-party source redistribution, license addition or in-game tests. Runtime verification remains deferred. [Current roadmap](../ROADMAP.md).
