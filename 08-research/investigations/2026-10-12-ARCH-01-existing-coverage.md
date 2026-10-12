# ARCH-01 — Existing practical architecture/debugging coverage

> ADR document set: **v0.1.78**. Research revisions and source/build versions below describe their original scope.

- ID: ARCH-01
- Subsystem: practical architecture/debugging (cross-system foundation)
- ADR revision: v0.1.78
- Record status: complete-within-scope (inventory only); practical foundation partial
- Source status: scoped-source-audit of selected existing ADR documentation
- Runtime status: untested; deferred
- Baseline: ADR v0.1.77 main `fd6904d872af9a55f6abc7c219132824ffad558c`; original source/build/external-report confidence retained
- Last reviewed: 2026-10-12

## Question and scope

Which architecture, compatibility/state-ownership, diagnosis/logging and example/test concerns already have bounded ADR coverage, and what practical foundation remains? Review selected environment/profile/architecture/UI/A-Life/configuration/persistence/economy/error/external-report/policy/test/example references. Completion requires canonical pins, retained confidence, concrete gaps and a bounded follow-on sequence. No new native/API/runtime closure is part of this inventory.

## Evidence and method

The [22-row ledger](../../evidence/architecture/coverage-inventory-2026-10-12.csv) pins raw document hashes and inclusive selected section ranges/markers at the declared immutable v0.1.77 commit. Search terms included architecture, compatibility, ownership, identity, reload, callback, save/schema, logging, assert, error, pcall, traceback, diagnostic, clock, example, test and reproducibility. Read selected sections and existing test bodies to distinguish implemented source-tool checks from planned game tests. Original source ledgers and external-report confidence stay authoritative; no native re-audit is implied by document hashing.

Native diagnostic filename searches in the available ENGINE1011 tree locate the eight candidate paths listed in the [inventory](../../05-mod-architecture/coverage-inventory.md). Presence alone does not establish exports, error propagation, build activity or installed logger behavior. No new source artifact/binary equivalence is introduced.

## Findings

A01/A02 expose starter outlines, while A03/A04 retain build/profile provenance. A05–A11 reuse selected configuration/install/lifetime/identity/callback/persistence/request contracts instead of inventing general architecture guarantees. D01/D02 identify the outline versus missing shared logging/error-chain reference; D03–D07 retain selected XML/script failure, externally observed UI mechanisms, evidence and clock boundaries. T01–T04 distinguish existing documentation/catalog tests, example qualification, non-runnable sketches and source/publication checks.

The practical gap is synthesis of module/state/dependency interfaces, selected diagnostic contracts and qualified example/test guidance. ARCH-02 handles architecture/compatibility; DEBUG-01 handles bounded logging/crash diagnosis; ARCH-03 handles selected examples/test guidance and consolidation/audit. This does not close the separate final cross-system ADR audit or effective installed/runtime backlogs.

## Competing explanations and missing edges

Many subsystem guides already contain architectural advice; their existence does not make the old architecture/debugging outlines complete practical guides. A log/traceback intake list is not an implemented logger/error-recovery contract. Passing documentation tests or selected external observations is not independent game verification. Missing reviewed closure is not missing upstream functionality, and a source filename or pcall does not certify universal recovery. Profiles/winning sources and current executable identity remain unresolved where prior records say so.

## Checks and outcomes

Validate all 22 original raw document hashes, section markers/ranges and step allocations against v0.1.77, preserve prior evidence/history/generated/tool/test bytes and dated bodies except current banners, and run repository validation/10 existing regressions. Repair a tests-entry economy audit link to its actual v0.1.62 report and label starter architecture maps as historical orientation; these are current-navigation corrections, not new source findings. [Verification](../verification-2026-10-12-v0.1.78.md). Compare complete remote base/staged/published path/blob maps with expected-head update. No game/runtime or engine compilation.

## Disposition and next work

ARCH-01 inventory is complete within scope; practical architecture/debugging foundation remains partial. **Next ARCH-02 — module/state ownership and compatibility contracts.** [Inventory/plan](../../05-mod-architecture/coverage-inventory.md), [roadmap](../../ROADMAP.md). Runtime remains deferred; no CtZ gameplay or third-party source/assets changes.
