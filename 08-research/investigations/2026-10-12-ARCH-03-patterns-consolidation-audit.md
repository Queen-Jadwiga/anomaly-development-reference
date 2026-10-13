# ARCH-03 — Qualified patterns, test guidance and bounded practical audit

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

- ID: ARCH-03
- Subsystem: practical architecture/debugging/examples
- ADR revision: v0.1.81
- Record status: complete-within-scope for selected patterns/test guidance/consolidation/audit; effective integration partial
- Source status: scoped-source-audit and pinned reference/test-source synthesis; proposed patterns distinguished
- Runtime status: untested; deferred
- Baseline IDs and provenance record: ADR v0.1.80 `a9248aea46442c3cd520b7e33974827dbd810a95`; original ARCH-01/02 and DEBUG-01 pins plus ENGINE1011 archive `withheld-upload-fingerprint` through [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and scope

Which selected practical patterns and checks can be documented from the established ownership/compatibility/diagnostic contracts, and is the bounded practical foundation consistent in qualification, evidence and navigation?

Included: four proposed non-runnable protocols for subscription identity, wrapper capture/restoration, staged restoration/request reconciliation and bounded probes; qualification of two existing UI call sketches; implemented ADR tests versus proposed fixtures/source/build/profile checks; central practical decision guide; selected reference/source integrity and semantic/navigation audit.

Completion requires dependency/precondition/state/failure/reentry/cleanup/persistence/test status for each selected pattern, usable test-evidence guidance and bounded consolidated status. Excluded: a drop-in framework, new runnable mod or fixture implementation, new native/API tracing, actual migrations/cleanup, every addon/build, engine/game execution and the separate final whole-ADR audit. Code adds no value without the missing effective interfaces; protocols remain design guidance rather than executable examples.

## Evidence and method

[16-row reference ledger](../../evidence/architecture/qualified-patterns-2026-10-12.csv) Q01–Q16 pins eight Markdown references and two test-source files at immutable v0.1.80. Raw file hashes, inclusive sections/full-file ranges, markers, retained boundary and use are recorded. Original native/script/external evidence remains authoritative; test-source pins establish the implemented ADR fixtures, not a game harness.

[Bounded audit record](../../evidence/architecture/bounded-audit-2026-10-12.json) rechecks **54 earlier reference rows** at original revisions, the **16 new rows**, and **41 DEBUG-01 source rows/67 ranges/21 files** plus scope-map agreement. Review current guides for implemented/design, source/runtime/external, ownership/alias, request/result/retry, build/winner, filtered-stack/output and lifetime distinctions. Audit scope is explicitly narrower than all subsystems and all source dependencies.

No original evidence schema is converted and no earlier CSV/JSON/tool/test body is rewritten. Current hubs gain consolidated status; dated investigations change only banners. Proposed fixtures are plans, not executed results. Full catalog generation is unchanged and is preserved rather than rerun to imply an unrelated engine audit.

## Findings

1. **Selected protocols can be useful without pretending to be native services.** Exact listener identity, per-install capture/conditional restoration, staged schema/identity/reconciliation and bounded diagnostic decisions are made concrete with assumptions/failure/cleanup. Existing engine receipts/readiness/removal are not invented. Q01–Q10; [patterns](../../07-code-library/qualified-patterns.md).
2. **UI sketches need their actual initialized-object owner.** The two existing bar/scroll sketches remain non-runnable; bare constructor safety and generic PDA teardown are not inferred. Explicit dependencies/lifetime/failure/cleanup qualification links the current UI guide. Q11/Q15.
3. **Different checks answer different claims.** Existing tests implement seven repository checks and three binding-pattern fixtures. Proposed mocks can test a mod model while native producers, side effects, formatting and termination remain source/profile-qualified. No new fixture or engine test is supplied. Q12–Q14/Q16; [test guidance](../../05-mod-architecture/test-guidance.md).
4. **The selected foundation is consolidated.** A central 05 guide links canonical ownership/compatibility, 06 routes/triage, 07 patterns and test guidance. ARCH-01–03/DEBUG-01 planned source/design work now closes within selected scope. Effective integration, binary/profile identity and runtime remain partial/deferred. [Central reference](../../05-mod-architecture/development-reference.md).
5. **Integrity checks retain bounded confidence.** Original pins/source hashes/ranges/scope records match. Semantic review retains implemented/design and source/runtime distinctions; current next-step/navigation is updated without silently rewriting dated findings. No whole-ADR consistency or exhaustive native semantic guarantee follows from those checks.

## Competing explanations and missing edges

A fixture may pass because its fake dependency supplies a success result or synchronous completion that the real route does not. A wrapper may appear removed while another closure retains it; a decoded model may be valid while campaign pairing or world readiness is unresolved; missing log output may be a gate/file-stage issue rather than no execution. Each pattern/test plan preserves these alternatives.

Winning globals/dispatcher aliases, installers/emitters, native build/executable, serializer/root/snapshot/encoder, campaign identity, UI registrations/teardown and addon interaction remain effective-source gaps. No proposed interface/pattern is promoted to installed compatibility or runtime-safe behavior. Prior externally reported UI/clock observations retain their own provenance.

## Checks and outcomes

[Verification](../verification-2026-10-12-v0.1.81.md) records the selected source/reference checks, exact audit/ledger reproduction, old evidence/history/tool/test preservation, dated-body banner-only changes, repository validation, ten existing regression tests and remote full-blob verification. No generator scope, gameplay files, saves or engine binaries change. No game ran.

## Disposition and next work

ARCH-03 is complete within the selected practical foundation scope. Use the [central guide](../../05-mod-architecture/development-reference.md), [qualified patterns](../../07-code-library/qualified-patterns.md) and [test guidance](../../05-mod-architecture/test-guidance.md). ARCH-01 retains the inventory/allocation; ARCH-02/DEBUG-01 retain original source/research boundaries with current completion links.

Next: **separate cross-system final ADR consolidation/provenance/navigation/consistency audit**. It is not performed by this increment and must preserve subsystem evidence scopes and effective/runtime limits. Broader native/addon depth and runtime resumption remain separate. No CtZ gameplay or third-party source/assets changes. [Roadmap](../../ROADMAP.md).
