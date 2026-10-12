# Debugging workflow

> ADR document set: **v0.1.79**. Research revisions and source/build versions below describe their original scope.

1. Keep original log and timestamp privately.
2. Extract startup banner and environment facts.
3. Preserve full error + traceback + affected mod revision.
4. Identify the smallest reproduction and record expected/observed result.
5. Label hypotheses separately from confirmed causes.
6. Test minimal fix, then regression test the full mod.
7. Add findings to relevant API notes with evidence IDs.

Never publish personal machine paths or unredacted logs by default.

## Current coverage and next work

[ARCH-01 inventory](../05-mod-architecture/coverage-inventory.md) is complete within scope. The workflow above remains an intake outline; selected XML/script/external-report diagnostics are linked there, while general native logger/stack/assertion/error/flush contracts remain DEBUG-01 work. Existing documentation/source tests are separate from deferred game/profile reproduction. [Inventory verification](../08-research/verification-2026-10-12-v0.1.78.md), [roadmap](../ROADMAP.md).

Current architecture step: [ARCH-02 ownership](../05-mod-architecture/module-state-contracts.md) and [compatibility](../05-mod-architecture/compatibility-package-contracts.md) are complete within selected synthesis scope. **Next DEBUG-01**: selected native/Lua logging, stack, assertion, error and flush routes with provenance-aware triage. The outline and existing diagnostic references remain qualified; no new logger trace is claimed by ARCH-02. [Roadmap](../ROADMAP.md).
