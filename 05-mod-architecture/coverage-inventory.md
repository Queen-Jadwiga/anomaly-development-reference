# Practical architecture/debugging coverage inventory

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

- ID: ARCH-01
- Subsystem: practical architecture/debugging (cross-system foundation)
- Research revision: v0.1.78
- Record status: complete-within-scope (inventory only); practical foundation partial
- Source status: scoped-source-audit of selected existing ADR documentation
- Runtime status: untested; deferred
- Baseline: ADR v0.1.77 main `fd6904d872af9a55f6abc7c219132824ffad558c`; original source/build/external-report confidence retained
- Last reviewed: 2026-10-12

This inventories selected established ADR records before practical architecture/debugging work. It does not revalidate every native claim, certify new logging APIs, create runtime-tested examples or close installed compatibility. [22-row documentation ledger](../evidence/architecture/coverage-inventory-2026-10-12.csv), [investigation](../08-research/investigations/2026-10-12-ARCH-01-existing-coverage.md), [verification](../08-research/verification-2026-10-12-v0.1.78.md).

## Existing coverage and remaining work

| Area | Existing coverage | Canonical section | Remaining practical work |
| --- | --- | --- | --- |
| A01 — Cross-layer engine architecture | conceptual-outline | [architecture](../01-engine/architecture.md) | Synthesize module boundaries/dependencies from completed source references; keep native-only versus exported contracts explicit. |
| A02 — Compatibility, file layout and packaging | plan-only | [README](../05-mod-architecture/README.md) | Define practical layout, dependency/winner/build matrix and upgrade/package boundaries using existing provenance and source contracts. |
| A03 — Source, executable and feature version identity | qualified-provenance | [source-baseline-2026-10-11](../00-environment/source-baseline-2026-10-11.md) | Connect release/schema/feature/build qualification to architecture decisions; do not silently infer an installed target. |
| A04 — Effective virtual-view and supplying-mod inputs | selected-provenance | [2026-10-11-WAR-002a-source-packages-effective-profile](../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md) | Create a practical dependency/conflict evidence matrix without claiming full MO2 internals or actual installed winners. |
| A05 — Configuration ownership and precedence | selected-synthesis | [development-reference](../04-game-systems/configuration/development-reference.md) | Translate these into mod-owned state/config interfaces and dependency assumptions, without retracing CONFIG-02. |
| A06 — Module and patch installation phases | selected-contract | [supplied-options-patches](../04-game-systems/configuration/supplied-options-patches.md) | Define initialization, subscription/install/remove/reload responsibilities and failure states; do not certify repeat safety by convention. |
| A07 — UI ownership and native alias lifetime | selected-contract-plus-qualified-reports | [development-reference](../03-ui-pda/development-reference.md) | Build practical object-lifetime boundaries and cleanup obligations through existing UI evidence; defer runtime-safe recipe claims. |
| A08 — Server/client identity and authority | selected-synthesis | [development-reference](../04-game-systems/alife/development-reference.md) | Map durable identity and reacquisition boundaries across modules without promoting lookup to campaign/generation proof. |
| A09 — Callback identity, timing and state sharing | selected-contract | [script-loading-startup-callbacks](../04-game-systems/configuration/script-loading-startup-callbacks.md) | Define adapters/subscription ownership and observation records, using effective emitter/argument/return contracts. |
| A10 — Persistent schema and reconciliation | selected-design-guidance | [development-reference](../04-game-systems/persistence/development-reference.md) | Synthesize mod data/version/reset/rebind rules and missing receipts; keep source-defined policy distinct from runtime validation. |
| A11 — Mutation, requests and partial failure | selected-contract-plus-design-guidance | [development-reference](../04-game-systems/economy/development-reference.md) | Define operation/result/uncertainty and retry boundaries for mod interfaces without inventing atomic engine services. |
| D01 — General crash intake workflow | workflow-outline | [README](../06-debugging/README.md) | Turn the outline into source-qualified intake/triage with exact executable/profile/save/mod/callback phase evidence. |
| D02 — Native logging, assertions and stack/error handling | outside-reviewed-closure | [README](../06-debugging/README.md) | Trace selected native/Lua log/error/callstack routes, guards/format/return/flush limits and local-versus-outer error boundaries. |
| D03 — XML/DXML failure boundaries | selected-contract | [xml-dxml-callback-errors-ui04b-oct11](../03-ui-pda/xml-dxml-callback-errors-ui04b-oct11.md) | Link these as diagnosis cases instead of reopening complete XML/UI traces; inspect outer handlers only for selected diagnostic routes. |
| D04 — Script compile versus partial execution failure | selected-contract | [script-loading-startup-callbacks](../04-game-systems/configuration/script-loading-startup-callbacks.md) | Build syntax/load/lookup/registration/dispatch failure triage with actual guards and emitted evidence. |
| D05 — External runtime evidence and competing mechanisms | qualified-external-observations | [2026-10-12-REV-01-external-runtime-issues](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md) | Define how to preserve hypotheses and discriminating observations without reclassifying external reports or promising fixes. |
| D06 — Evidence pins and confidence axes | established-reference-policy | [evidence-policy](../08-research/evidence-policy.md) | Apply policy to diagnostic records and minimal probes; retain private artifacts and scope negative searches. |
| D07 — Clocks, timing and performance diagnosis | selected-contract | [configuration-controls](../04-game-systems/alife/configuration-controls.md) | Define clock/unit/phase/bounded logging questions; profiling results and safe logger overhead remain deferred. |
| T01 — Documentation and extractor regression checks | implemented-source-tool-tests | [README](../tests/README.md) | Define when source/tool checks, fixtures and eventual engine/profile tests answer different questions. |
| T02 — Reusable example promotion policy | policy-only | [README](../07-code-library/README.md) | Produce only selected qualified patterns with preconditions/ownership/failure/cleanup/review and deferred runtime status. |
| T03 — Existing UI call sketches | illustrative-non-runnable | [minimal-static-ui-patterns](../03-ui-pda/examples/minimal-static-ui-patterns.md) | Reuse their qualification and link APIs; do not promote sketches to tested generic widgets or add unnecessary examples. |
| T04 — Reproducibility, audit and publication workflow | established-reference-policy | [workflow](../08-research/workflow.md) | Consolidate architecture/debugging/example guidance and audit selected references/dependencies/navigation without exhaustive whole-ADR revalidation. |

Coverage labels describe these pinned documents, not every source/mod. Outline/policy-only entries establish plans or qualification rules rather than implemented behavior. `outside-reviewed-closure` means the reviewed records do not establish the diagnostic chain; it does not mean the engine lacks it. Multiple rows reuse different boundaries of a canonical record. Source status, runtime observation and investigation completion remain independent.

## Reuse boundary and practical gaps

Native object/UI ownership, server/client identity, callback phase/order, configuration/loading/patch rules, persistence/reconciliation and request-versus-transaction limits already have selected source coverage. Keep their detailed references/ledgers canonical. Practical architecture should connect interfaces and state owners rather than recertify or duplicate entire subsystems. The architecture/source-map/mod-architecture starter outlines are historical orientation, not present completeness assertions.

The debugging outline, external issue review and local XML/script error traces do not yet supply one general native logger/flush/stack/assertion/recovery reference. Existing tests exercise documentation/catalog tools; their success does not run the game or prove every interpretation. The reusable code-library policy and two UI sketches do not constitute a tested drop-in library. Packaging, migration and repeat-install/recovery guidance need effective dependencies and qualified contracts.

## Bounded follow-on sequence

1. **ARCH-02 — module/state ownership and compatibility contracts:** synthesize practical boundaries from the existing native/export/script/config/UI/persistence references; map durable versus transient state, initialization/subscription/teardown/reload, requests/results/retries, schema/campaign identity, dependencies/winning-file evidence and package/upgrade limits. Trace only missing selected interfaces needed by this synthesis. No universal compatibility recipe, full MO2 implementation or CtZ gameplay changes.
2. **DEBUG-01 — bounded logging/crash-diagnosis contracts:** trace selected native/Lua log/stack/assertion/error routes and build/runtime flags, file/flush/return/format/lifetime limits and local-versus-outer failure handling. Combine existing XML/script/ownership/clock cases with provenance-aware intake, hypotheses and discriminating observation plans. Keep actual engine/profile reproduction and measured logger/profiler overhead deferred; do not promise pcall catches every native failure.
3. **ARCH-03 — qualified examples, test guidance and consolidation/audit:** use a few justified source-qualified patterns with dependencies/preconditions/state ownership/failure/cleanup and explicit untested status, or linked sketches when code adds no value. Distinguish documentation/generator/fixture/source checks from eventual engine/profile tests; consolidate the architecture/debugging guides and audit their selected evidence/links/limits. Keep the later cross-system final ADR audit separate.

ENGINE1011 path-presence searches locate `src/xrCore/log.cpp`, `xrDebug.cpp`, `xrDebugNew.cpp`, `xrDebug.h`, `xrDebug_macros.h`, `src/xrServerEntities/script_engine.cpp`, `script_storage.cpp` and `src/xrGame/script_binder.cpp`. These are diagnostic trace candidates, not newly certified behavior/exports. Unknown exact upstream commit/executable/profile correspondence remains explicit. File presence and old function names do not establish active build branches, logging guarantees or safe error recovery.

Cross-system architecture/debugging/example categories retain their existing 05/06/07 homes; the canonical inventory is here with links from their entry pages. They are not forced into the three-file behavior-subsystem pattern. Renderer/VM/security/profiler internals, every mod manager/addon combination, all native crash causes and unrelated multiplayer remain optional depth unless a concrete diagnostic/design question requires them. Runtime remains deferred. [Architecture entry](README.md), [debugging entry](../06-debugging/README.md), [examples](../07-code-library/README.md), [roadmap](../ROADMAP.md).

## ARCH-02 disposition — 2026-10-12

[Module/state ownership](module-state-contracts.md) and [compatibility/package contracts](compatibility-package-contracts.md) now close the selected ARCH-02 synthesis allocation. The pinned ARCH-01 rows and original bounded plan above remain unchanged. The new 26-row documentation ledger preserves existing source/build/external confidence and labels proposed designs; effective dependencies and runtime remain open. Next DEBUG-01, then ARCH-03. [Verification](../08-research/verification-2026-10-12-v0.1.79.md).

## DEBUG-01 disposition — 2026-10-12

[Selected diagnostic routes](../06-debugging/diagnostic-routes.md) and [triage](../06-debugging/triage.md) now close the bounded DEBUG-01 allocation: 41 source rows/67 ranges/21 files and six documentation pins. The original inventory/plan remains preserved; effective installed aliases/build/profile and runtime stay open. Next ARCH-03 patterns/test guidance and practical consolidation/audit. [Verification](../08-research/verification-2026-10-12-v0.1.80.md).

## ARCH-03 practical foundation closure — 2026-10-12

[Central practical reference](development-reference.md), [qualified patterns](../07-code-library/qualified-patterns.md) and [test guidance](test-guidance.md) now close the selected ARCH-01–03/DEBUG-01 foundation allocation. The dated inventory/plan above and original pins remain preserved. The [bounded audit](../08-research/verification-2026-10-12-v0.1.81.md) covers selected references/diagnostic source and qualifications; effective integration stays partial and runtime deferred. Next separate whole-ADR consolidation/provenance/navigation/consistency audit, not performed by this closure.
