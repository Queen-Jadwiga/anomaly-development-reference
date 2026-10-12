# PER-04 — Persistence consolidation and final available-source audit

> ADR document set: **v0.1.70**. Research revisions and source/build versions below describe their original scope.

- ID: PER-04
- Subsystem: persistence
- ADR revision: v0.1.53
- Record status: complete-within-scope
- Source status: source-confirmed selected contracts; scoped-source-audit for consolidation
- Runtime status: untested; deferred until explicitly resumed by the user
- Baselines: ENGINE1011, BETA150 main, CTZ005J; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-11

## Question and scope

Do PER-01–03 form a consistent practical persistence reference, and what prevents full effective-source closure? Include ownership/serialization, phase ordering, type/schema/identity distinctions, failure/cleanup/reconciliation boundaries and source/navigation/preservation audit. Exclude new gameplay fixes, runtime, complete codec robustness certification, every engine save entry and installed scripts not supplied.

## Evidence and method

Reuse the original [S01–S24](../../evidence/persistence/native-pipeline-2026-10-11.csv), [L01–L13](../../evidence/persistence/lua-storage-2026-10-11.csv) and [C01–C13](../../evidence/persistence/ctz-campaign-safety-2026-10-11.csv) ledgers without duplicating IDs or normalizing their bytes. Archive/commit pins remain in original records and manifest; installed executable/profile correspondence remains unknown.

Compare the three references and focused APIs with ALIFE-04, A-Life callbacks and FAC-02. Re-read selected native storage/validity/binder, shared callback forwarding/cleanup and CtZ load/actor gates directly. Check all persistence ledger hashes/counts/ranges and selected symbols; compare prior repository blobs/history/datasets. The audit is bounded and does not reread every earlier source line or invent missing core implementation.

## Findings

[Development reference](../../04-game-systems/persistence/development-reference.md) consolidates guidance with ledger-qualified nearby citations; [completion status](../../04-game-systems/persistence/source-completion-status.md) retains explicit missing effective chains.

- Save request, native file write, early load hook, final native registration, late group repair and client binder load are separate stages. Shared dispatch cannot be placed between them from callback names alone. PER-01 S01/S13–S20/S24; PER-02 L06.
- Explicit native/custom bytes, codec values, shared namespaces and CtZ strategic state have different owners and type/identity/schema limits. No single universal persistence API follows from their coexistence. PER-01 S09/S15/S21; PER-02 L01–L13; PER-03 C01–C13.
- Version acceptance, targeted backfills, numeric resolution, readiness delays and protected calls each establish narrower contracts than compatibility, identity or complete restore success. PER-01 S04/S16; PER-03 C02/C04/C06/C08/C09/C13.
- CtZ reconciliation is world mutation/accounting after strategic restore. Selected missing/lost/time policies do not close installed campaign/reset and ID safety. PER-03 C03/C10–C13.
- Correct current roadmap FAC-06 audit target to its original v0.1.49 report; remove stale forwarding-page wording from investigation navigation. These are navigation corrections; dated conclusions remain preserved.

## Competing explanations and missing edges

Installed manager/dispatch/binder/addon sources can establish additional identity/schema/order rules or replace selected paths. Source packages cannot be combined into a proven active profile. PER-02's missing-definition scan remains limited to its original roots/patterns; this synthesis does not expand that negative claim. No new runtime finding or contradiction requiring a research conclusion revision was established in this bounded review.

## Checks and outcomes

[Final audit report](../verification-2026-10-11-v0.1.53.md) records actual preservation, source/range checks, validator/tests and publication verification. Structural checks do not certify interpretation, installed execution or save robustness.

## Disposition and next work

Planned available-source persistence research and consolidation/audit are complete within scope. Effective installed persistence remains partial; runtime remains deferred. Another subsystem can proceed independently; effective-source collection resumes when winning files/profile are available. [Roadmap](../../ROADMAP.md).
