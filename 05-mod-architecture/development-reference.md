# Practical architecture and debugging development reference

> ADR document set: **v0.1.81**. Research revisions and source/build versions below describe their original scope.

- ID: ARCH-03-GUIDE
- Subsystem: cross-system practical architecture/debugging
- Research revision: v0.1.81
- Record status: ARCH-01–03 and DEBUG-01 complete within selected foundation scope; effective integration partial
- Source status: scoped-source-audit and pinned reference synthesis; proposed design patterns explicitly distinguished
- Runtime status: untested; deferred; qualified external observations retain their own provenance
- Baselines: original ARCH-01 v0.1.77, ARCH-02 v0.1.78, DEBUG-01 ENGINE1011/v0.1.79 and ARCH-03 v0.1.80 pins in [architecture](../evidence/architecture/README.md) and [debugging](../evidence/debugging/README.md) evidence
- Last reviewed: 2026-10-12

This is the central decision guide for the practical foundation. Detailed ownership, compatibility, diagnostics and patterns stay in their canonical 05/06/07 pages. The [bounded audit](../08-research/verification-2026-10-12-v0.1.81.md) checks selected evidence, qualifications and navigation; it does not recertify every ADR subsystem, create a mod framework or close installed dependencies.

## Choose the question and its authority

| Development question | Canonical starting point | Decision to make |
| --- | --- | --- |
| What owns this value/resource? | [Module/state contracts](module-state-contracts.md) | Authority, alias/copy, durable/transient lifetime and invalidation |
| What does this interface promise? | [Interface record](module-state-contracts.md#declare-an-interface-before-connecting-consumers) and the relevant [API catalog](../02-lua-api/api-index.md) | Exact arguments/results, effects, phase, errors and qualified implementation |
| How is installation/removal repeated? | [Lifetime contracts](module-state-contracts.md#make-lifetime-transitions-explicit), [P01/P02 patterns](../07-code-library/qualified-patterns.md) | Exact identities, capture/return policy, partial install and restoration limits |
| What is actually compatible? | [Dependency/package contracts](compatibility-package-contracts.md) | Winning files/replacements, build/interface/schema/campaign axes and support boundary |
| When may restored state affect the world? | [Persistence phases](../04-game-systems/persistence/development-reference.md), [P03](../07-code-library/qualified-patterns.md#p03--stage-restoration-and-reconcile-owned-operations) | Decode/validate, identity rebinding, observation/reconciliation and repeat authority |
| What does this diagnostic prove? | [Native/Lua routes](../06-debugging/diagnostic-routes.md), [four exports](../02-lua-api/debugging/diagnostic-api.md) | Emitter, guards, buffer/file stage, filtered stack and failure boundary |
| How can the alternatives be distinguished? | [Triage](../06-debugging/triage.md), [P04](../07-code-library/qualified-patterns.md#p04--use-a-bounded-probe-to-discriminate-one-hypothesis) | Minimal hypothesis/phase/value record and qualified observation plan |
| What check supports the claim? | [Test guidance](test-guidance.md), [implemented ADR tests](../tests/README.md) | Integrity/fixture/model/source/build/profile evidence level and actual result |
| Can a UI call sketch be reused? | [UI sketch qualification](../07-code-library/qualified-patterns.md#reuse-the-two-ui-sketches-with-their-lifetime-limits), [UI guide](../03-ui-pda/development-reference.md) | Valid initialized object, parent/native registrations, lifespan and deferred runtime |

ARCH-03 Q01–Q16 in the [reference ledger](../evidence/architecture/qualified-patterns-2026-10-12.csv) identify reused boundaries. The architecture tables/pattern protocols are recommended design, not additional native APIs. Domain behavior still belongs to [subsystem guides](../08-research/subsystem-map.md); exact source/executable/profile provenance belongs to [environment records](../00-environment/source-baseline-2026-10-11.md).

## Connect contracts without collapsing their lifetimes

A feature can declare a public request, validate/update owned domain state, use an adapter in an established phase, observe a native result and later reconcile/persist it. Each step needs its own effect/result/identity contract. A notification return is not automatically a receipt; a table assignment is not encoding; encoding is not an atomic combined save; a callback is not universal readiness. These retained boundaries motivate the selected patterns. [ARCH-02 request authority](module-state-contracts.md#separate-requests-observations-and-retry-authority), [DEBUG-01 error boundaries](../06-debugging/diagnostic-routes.md#error-handling-is-not-one-recovery-protocol).

Keep campaign content separate from transient clients/UI, exact subscription tokens separate from saved domain facts, producer tables separate from old aliases, and native/script caches separate from applied consumer fields. On failure, preserve the last established outcome and unresolved effects rather than assuming retry/refund/cleanup is safe. The proposed modules and protocols have no universal installation, hot-reload, migration or recovery implementation. [Ownership](module-state-contracts.md), [patterns](../07-code-library/qualified-patterns.md).

## Selected completion and what the audit establishes

| Step | Completed selected allocation | Retained limit |
| --- | --- | --- |
| ARCH-01 | 22 pinned existing-coverage rows, bounded plan and canonical reuse | Inventory does not establish a new engine/logger contract |
| ARCH-02 | 26 pinned sections, state/interface/lifecycle and dependency/package/schema support guidance | Designs unimplemented; effective state/storage/startup/winner chains partial |
| DEBUG-01 | 41 source rows/67 ranges/21 files, six reference pins, four exports and diagnostic/triage boundaries | Actual binary/aliases/profile, symbols/dump outcomes and independent reproduction unresolved |
| ARCH-03 | Four non-runnable protocol patterns, two linked UI sketches with qualification, test guidance and bounded consolidation/audit; 16 reference rows | No new fixture/mod implementation, runtime-safe pattern or whole-ADR audit |

The audit rechecks **54 earlier reference rows**, **16 new reference rows**, and the **41 DEBUG-01 source rows** under their original pins. It preserves historical bodies/evidence and reviews selected distinctions: implemented versus proposed, source versus runtime/external, return versus completion, durable versus transient, current versus fault stack, and entry navigation versus dated plans. Exact counts/results are in [verification](../08-research/verification-2026-10-12-v0.1.81.md). Hash/link success establishes integrity; semantic review is bounded to these claims.

## Effective-source and runtime closure remain separate

Before claiming an installed integration, establish executable/build conditions, virtual winning files and differently named patches, actual global/dispatcher aliases, installer/emitter/order, storage root/snapshot/encoder, binders, identity/campaign pairing, resources/config and teardown. Domain-specific missing edges remain in their existing completion records. [Compatibility requirements](compatibility-package-contracts.md), [profile collection](../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md).

Runtime remains deferred. Existing externally observed UI/clock failures retain their recorded provenance and hypotheses. Ten ADR regression tests exercise documentation and registration tools; they do not execute the four proposed patterns or test the game. [Test guidance](test-guidance.md), [REV-01](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md).

The practical ARCH-01–03/DEBUG-01 foundation is complete within selected available-source/design scope. Next is the **separate cross-system final ADR consolidation/provenance/navigation/consistency audit**. It must retain subsystem audit scopes and effective/runtime gaps; this increment does not perform it. Broader renderer/VM/profiler/security, every addon/build and unrelated gameplay depth remain optional unless a concrete question requires them. [Roadmap](../ROADMAP.md), [ARCH-03 investigation](../08-research/investigations/2026-10-12-ARCH-03-patterns-consolidation-audit.md).
