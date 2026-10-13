# ARCH-02 — Module/state ownership and compatibility contracts

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

- ID: ARCH-02
- Subsystem: practical architecture
- ADR revision: v0.1.79
- Record status: complete-within-scope for selected synthesis; effective integration partial
- Source status: scoped documentation synthesis of existing source-confirmed selected contracts; design inference identified
- Runtime status: untested; deferred
- Baseline IDs and provenance record: ADR v0.1.78 `b187f8707ae4276c442284a25359baa8b3cf538f`; inherited ENGINE1011/BETA150/ZIP142/CTZ005J and qualified historical/external pins through the [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and scope

How should a mod divide module interfaces, state ownership and compatibility responsibilities without assuming a shared lifetime, transaction or installed dependency chain the source does not establish?

Included: native/export/script/config/UI/persistence ownership boundaries; durable/transient state; evaluation, installation, subscription, teardown and reload; request/result/retry limits; schema/campaign identity; winning-file/dependency evidence; package/upgrade/removal contracts. Completion requires a usable ownership/interface/lifecycle synthesis and a qualified dependency/package support record linked to existing evidence.

Excluded: runnable framework, new engine exports, universal compatibility or MO2 internals, every addon integration, gameplay edits, actual save migration or native cleanup, and runtime execution. Diagnostic internals and qualified patterns/test guidance remain DEBUG-01/ARCH-03.

## Evidence and method

The [26-row documentation ledger](../../evidence/architecture/module-state-contracts-2026-10-12.csv) pins sections in nine canonical documents at immutable v0.1.78. Each row records raw full-document SHA-256, inclusive one-based range, heading marker, inherited evidence labels, boundary and derived design contract. This is a synthesis schema, not newly traced native source evidence. Reproduction requires the pinned revision because current banners change.

Read the selected source-qualified reference sections and retain their original ledger-local IDs, baselines, execution conditions and missing edges. Group their boundaries into ownership/interface/lifecycle and compatibility/package decisions. Explicitly label proposed interfaces, operation states, wrapper restoration, schema rules and package fields as design inference. No missing interface had to be invented or newly traced to close this synthesis; missing effective manager/global/binder/startup/profile routes remain open. Archive source pins do not identify installed executable equivalence.

## Findings

1. **State authority is specific to a fact and lifetime.** Persistent server state, client representations, native membership, Lua assignments, cached configuration, subscriptions and UI registrations have distinct owners. Proposed domain/adapters/storage/reconciliation/UI boundaries keep those distinctions visible. S01–S12/U01–U02/M05; [ownership reference](../../05-mod-architecture/module-state-contracts.md#assign-one-authority-per-fact).
2. **Loading and notification are not completed services.** Module-table presence can follow partial execution; startup can repeat; dispatch shares mutable arguments and discards returns. Exact listener identity and effective routing are required. Suggested explicit result/readiness and request/result contracts do not add a success receipt to existing APIs. M01–M07.
3. **Installation/removal is a separate resource contract.** Capture phase and shared slots determine wrapper repetition. Reload leaves prior closures/aliases; UI/INI cleanup follows ownership. Suggested conditional slot restoration cannot revoke wrappers captured elsewhere. S03/S06/S07/U01; design inference explicitly qualified.
4. **Requests, retries and persistence require actual authority.** Native requests/callbacks do not establish common accounting or atomic delivery; table attachment does not establish encoding. Suggested operation records and reconciliation need a real implementation, serializer, identity and repeat policy. S09–S13.
5. **Compatibility has multiple axes.** Native source, executable, package/interface, schema and campaign identity require separate evidence. Profile winners, differently named patches, debug routes, directives/resources and load/apply phases cannot be reduced to version labels or filename order. C01–C04/M04/M07/S01–S07/S10–S12; [companion](../../05-mod-architecture/compatibility-package-contracts.md).
6. **Package support includes stale files and retained effects.** Suggested manifests record intentional overwrites, dependencies, namespace/schema support, integration and upgrade/disable limits. Clean replacement, restart or new campaign remains a support decision requiring relevant evidence. This is design guidance rather than a verified installation/removal path.

## Competing explanations and missing edges

An observed stale value could arise from a consumer copy, replaced table, script cache, native filename cache or unapplied option; it cannot be attributed to one solely from a stored value. A duplicated effect could arise from repeated installation, different listener closures, partial execution or retry after an unresolved native effect. A missing callback could involve a distinct dispatcher, absent installer or missing producer. These are source-derived alternatives, not diagnosed runtime incidents.

The winning global/core class/config/exec/storage/binder inputs, native build/debug flags, actual startup/patch callers, snapshot/encoder timing, companion coordination, UI registration teardown and campaign pairing remain profile-qualified missing edges. September/October callback differences and external UI/clock reports retain their own scope. No all-version compatibility, minimum feature release or universal readiness event is inferred.

## Checks and outcomes

[Verification](../verification-2026-10-12-v0.1.79.md) records the 26 new pins, preserved ARCH-01 inventory and prior evidence/investigation bodies, repository validation, existing source-tool regression tests and full publication blob checks. Pin/link tests establish integrity; semantic review checks source versus design and partial versus complete distinctions. No engine compiled, game ran, saves changed or runtime compatibility was tested.

## Disposition and next work

ARCH-02 is complete within the selected cross-system synthesis scope. [Architecture entry](../../05-mod-architecture/README.md) now leads to practical ownership and compatibility contracts, with ARCH-01 retained as the dated inventory. Next **DEBUG-01 — selected native/Lua logging, stack, assertion, error and flush routes with provenance-aware diagnosis**. ARCH-03 then qualifies patterns/test guidance and consolidates/audits. Practical foundation remains partial until those bounded passes; runtime deferred. No CtZ gameplay or third-party source/assets changes. [Roadmap](../../ROADMAP.md).
