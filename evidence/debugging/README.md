# Selected debugging evidence

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

DEBUG-01 uses ENGINE1011 archive SHA-256 `withheld-upload-fingerprint`. Source paths are relative to its `xray-monolith-2026.10.11/` tree. Unknown upstream commit, exact executable equivalence and active profile remain explicit. [Environment](../../00-environment/source-baseline-2026-10-11.md), [manifest](../manifest.md).

- [diagnostic-routes-2026-10-12.csv](diagnostic-routes-2026-10-12.csv): **41 source rows, 67 inclusive range groups, 21 distinct files**, standard source-evidence schema. IDs L01–L07/B01–B06/N01–N06/A01–A04/S01–S15/P01–P02/I01 are ledger-local. Rows connect selected logger/writer/lifecycle, project/header guards, native handlers/stack/dump, four Lua exports/default converter, loader/storage/Luabind/binder/panic and supplied helper/rejection boundaries.
- [diagnostic-scope-2026-10-12.json](diagnostic-scope-2026-10-12.json): artifact pin, file hashes/line counts, method and exclusions. Selected definitions/registrations/callers/conditionals; not exhaustive native diagnostics or whole-tree search.
- [triage-references-2026-10-12.csv](triage-references-2026-10-12.csv): **six documentation pins** at immutable ADR v0.1.79 `2db0cc343662140d3670eec16ea247e75b00279b`. Purpose-specific schema records ledger-local D01–D06, commit/path/raw full-document SHA-256, inclusive full-document range, heading marker and reused boundary. Reproduce at that commit, not a later banner-updated page. Original source/build/external-report confidence remains authoritative.

Check raw bytes/hashes, decoded line counts and each semicolon-separated inclusive source range against the declared archive. Review branch conditions and registered signatures separately; range/hash integrity alone does not establish behavior. No third-party source, logs, dumps or assets are republished. Recommended probes and triage are design guidance; runtime untested/deferred.

[Routes](../../06-debugging/diagnostic-routes.md), [triage](../../06-debugging/triage.md), [API](../../02-lua-api/debugging/diagnostic-api.md), [investigation](../../08-research/investigations/2026-10-12-DEBUG-01-diagnostic-routes-triage.md), [verification](../../08-research/verification-2026-10-12-v0.1.80.md).

[ARCH-03 practical audit](../architecture/bounded-audit-2026-10-12.json) rechecks these 41 source rows/67 ranges/21 files and six original reference pins without changing their bytes or widening diagnostic scope. [Practical consolidation](../../05-mod-architecture/development-reference.md), [verification](../../08-research/verification-2026-10-12-v0.1.81.md). Runtime remains deferred.
