# Debugging reference

> ADR document set: **v0.1.80**. Research revisions and source/build versions below describe their original scope.

Start with [selected native/Lua diagnostic routes](diagnostic-routes.md), then [provenance-aware triage](triage.md). **DEBUG-01 is complete within selected source scope**; effective executable/profile chains remain partial. Runtime verification stays deferred.

- [Four Lua diagnostic exports](../02-lua-api/debugging/diagnostic-api.md): exact signatures, guards, result and failure limits. Native helpers, console commands and unresolved installed aliases remain separate.
- [Investigation](../08-research/investigations/2026-10-12-DEBUG-01-diagnostic-routes-triage.md), [41-row source evidence and six documentation pins](../evidence/debugging/README.md), [verification](../08-research/verification-2026-10-12-v0.1.80.md).
- Reuse [configuration/loading/callbacks](../04-game-systems/configuration/development-reference.md), [UI ownership](../03-ui-pda/development-reference.md), [external reports](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md), [architecture](../05-mod-architecture/README.md) and [source-tool tests](../tests/README.md).

Preserve full private logs/dumps and executable/profile/save identity before narrowing the symptom. Distinguish emitter, failure boundary and cause; qualify missing frames/output and partial effects. Proposed probes and recovery questions are guidance, not tested fixes. No generic pcall/catch, hot-reload or dump-completion guarantee.

[ARCH-01 inventory](../05-mod-architecture/coverage-inventory.md) retains the original allocation. Next ARCH-03: qualified patterns/test guidance and practical consolidation/bounded audit. The later whole-ADR audit remains separate. [Roadmap](../ROADMAP.md).
