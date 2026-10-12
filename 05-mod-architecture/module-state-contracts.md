# Module and state ownership contracts

> ADR document set: **v0.1.82**. Research revisions and source/build versions below describe their original scope.

- ID: ARCH-02-OWNERSHIP
- Subsystem: practical mod architecture
- Research revision: v0.1.79
- Record status: complete-within-scope for selected cross-system synthesis; effective integration partial
- Source status: scoped documentation synthesis of existing source-confirmed contracts; proposed design contracts explicitly distinguished
- Runtime status: untested; deferred
- Baseline: ADR v0.1.78 `b187f8707ae4276c442284a25359baa8b3cf538f`; inherited ENGINE1011/BETA150/ZIP142/CTZ005J and qualified historical/external evidence
- Last reviewed: 2026-10-12

Use this page to decide who owns a value, resource or operation before connecting modules. The [compatibility/package companion](compatibility-package-contracts.md) covers dependencies, upgrades and support claims. Evidence IDs below refer to the [ARCH-02 documentation ledger](../evidence/architecture/module-state-contracts-2026-10-12.csv), whose section pins lead to the original native/export/script ledgers. This increment synthesizes those contracts; it does not introduce an engine API, runnable framework or tested installation recipe. [Investigation](../08-research/investigations/2026-10-12-ARCH-02-module-state-compatibility.md).

## Assign one authority per fact

“One authority” is a proposed mod design rule: identify which owner may change a fact and how other representations refresh. The engine already has several distinct owners; a mod cannot collapse them by keeping all references in one table.

| State/resource | Existing boundary | Mod-owned contract to specify |
| --- | --- | --- |
| Campaign records, orders, faction accounts | Lua assignments alone are not serialization; separate native/binder/shared-table paths | Authoritative namespace, actual serializer, root reset, schema and campaign identity |
| Server object ID and native state | Persistent server objects differ from clients; IDs can be reused | Identity validation, removal policy and phase-specific reacquisition |
| Client object, binder, cached pointer | Realization/teardown differs from permanent server release | Short-lived lease, invalidation event and missing-client meaning |
| Native group membership, Lua strategic assignment | Different representations and authorities | Which fact is authoritative; reconciliation when the views disagree |
| INI data, named cache, script memoization, consumer fields | Cache invalidation and object mutation do not refresh all other owners | Refresh producer, copy/alias policy and dependent invalidation |
| Pending option, stored value, applied consumer state | Menu staging, saving, commands and gated notifications are separate | Validation, apply result and handling of external writes during editing |
| Listener closure/userdata, dependency rules | Registration/removal uses exact identity; referenced functions can remain retained | Subscription owner, event name, retained token and removal scope |
| Wrapper and captured original | Capture at evaluation/startup or shared mutable slot yields different repeat behavior | Installation identity, capture lifetime, return forwarding and restoration policy |
| Widget/window, parent and display registration | Allocation, attachment, AutoDelete, Luabind ownership and native registrations differ | Matching creation/registration and teardown route; separate content model |

Inherited boundaries: S01–S12, U01–U02, M05. Detailed authority remains in [A-Life lifecycle](../04-game-systems/alife/lifecycle-state-reference.md), [persistence](../04-game-systems/persistence/development-reference.md), [INI lifetime](../04-game-systems/configuration/ltx-ini-dltx.md) and [UI ownership](../03-ui-pda/ui-construction-ownership.md). Unknown effective storage/dispatcher/binder routes remain unknown.

Treat an aliased table as shared until a documented copy is made. Replacing a producer's table does not retarget old holders: the selected Warfare settings refresh demonstrates that boundary. Clearing script memoization does not clear the native filename cache. Borrowed system INI pointers require the owner's lifecycle; generic close/reload is not a certified cleanup procedure. These are inherited source contracts, rather than implementation details of the proposed module split. S01/S03/S05.

## Divide modules by responsibility

The following split is **recommended architecture**, not an implemented native service or mandatory filename scheme. Small mods can combine responsibilities while keeping the contracts explicit. Use a distinctive project prefix for public module names, option IDs and saved namespaces, and document every intentional shared name.

| Responsibility | Owns | Boundary to expose |
| --- | --- | --- |
| Bootstrap/integration | Exact subscriptions, wrapper installation records, selected dependency adapters | Explicit install status and repeat/cleanup policy; no campaign mutation merely from discovery |
| Domain model | Durable mod facts and validated state transitions | Requests and readable snapshots; no durable client/window handles |
| Engine adapter | Selected lookups, native mutations/requests and phase observations | Baseline-qualified arguments, effects, return/error meaning and identity checks |
| Storage/schema | Mod namespace encoding/decoding, supported versions and reset policy | Snapshot timing, migration result and validation; no assumed world readiness |
| Reconciliation/scheduling | Pending work, completion observations and retry decisions | Operation identity, clock domain, missing-target policy and bounded repeat behavior |
| UI/presentation | Transient controls and display registrations | Read model and validated commands; content state outlives a window only through its actual state owner |

M01–M07/S08–S13/U01 support the boundaries that motivate this split. They do not prove these suggested modules exist. Keep dependencies directed through named interfaces; document any required cycle and its installation/readiness protocol. A filename sort is insufficient to break a cycle because module lookup can autoload dependencies during discovery. M02/M04.

## Declare an interface before connecting consumers

For each public adapter or service, fill this review record. Fields describe the mod's promises and the evidence supporting them; absent evidence should be marked unknown rather than supplied by a convenient callback name.

| Field | Required content |
| --- | --- |
| Owner and identity | Public namespace/interface version; sole writer; campaign/module/session lifetime |
| Inputs | Exact arity, type, missing/empty/false distinctions, range checks and identity requirements |
| Output | Return/result meaning, immediate versus later completion, copied versus borrowed value |
| Effects | Native requests, table mutations, subscriptions, file writes and possible partial progress |
| Phase/dependencies | Caller/emitter, required restored state, installed winner and adapter/build limits |
| Failure/reentry | Error boundary, shared mutable input policy, nested invocation and partial effects |
| Repeat/cleanup | Exact listener/resource identity, deduplication evidence, invalidation and teardown owner |
| Persistence | Actual serializer, snapshot/encode point, schema, reset/migration and campaign pairing |
| Qualification | Source pins, implementation status, runtime status and unresolved edges |

Exact export arity/converters remain in the [INI API](../02-lua-api/configuration/ini-api.md), [callback API](../02-lua-api/configuration/script-callback-api.md) and domain catalogs. C++ defaults, a truthy namespace or successful listener registration do not provide a complete Lua service contract. M02/M05/S02/S03.

An **illustrative, unimplemented** order interface could promise a validated request record with an owned order ID and return an acceptance status. Its adapter would separately observe delivery; its storage component would serialize the record; its reconciler would decide whether retry is allowed. This describes responsibilities only. Existing trade/inventory requests and callbacks do not supply an atomic delivery/payment receipt or an automatic safe refund. S13, [economy design guidance](../04-game-systems/economy/development-reference.md#applying-the-contracts-to-a-mod).

## Make lifetime transitions explicit

| Transition | Inherited source limit | Required mod design decision |
| --- | --- | --- |
| Module evaluation | Autoload can run dependency code during discovery; runtime failure can leave a namespace | Define declaration-time effects and explicit initialization result; table presence is insufficient |
| Installation/startup | Handlers can repeat; wrappers capture different originals; registration is identity-based | Decide repeat/no-op/replacement policy per installation and retain exact installed identities |
| Deserialization | Native/shared/binder phases differ; early load precedes reconstruction | Decode/validate owned records without assuming reconstructed clients, UI or linked objects |
| Rebinding/reconciliation | Native registration can precede late member repair; IDs can be reused | Validate campaign/object identity and prerequisites before applying world effects |
| Option/config refresh | Stored, pending, cached and applied values differ | Define refresh completion and update copied/aliased consumers explicitly |
| Level/client/UI teardown | Client loss is not permanent server removal; UI registrations have distinct owners | Invalidate the matching transient resources without deleting unrelated durable facts |
| Module reload/VM reinit | Reload does not revoke old closures; VM reinit differs from stack unload | Establish which lifecycle actually occurred; do not promise universal hot reload |
| Package removal | Installed winners, retained data and native effects are profile-specific | State disable/uninstall limits and preserve an upgrade/recovery route |

M01/M03–M05/S04–S12/U01–U02. These rows are review obligations, not a universal event timeline. A fixed delay, `level.present()`, lookup success or a callback's name cannot certify all prerequisites. Use the actual [A-Life phases](../04-game-systems/alife/callback-phase-reference.md) and [save/load phases](../04-game-systems/persistence/development-reference.md#save-and-load-phase-contracts).

A proposed wrapper owner should retain the original captured for that installation, the exact installed wrapper and any subscription tokens. Define whether original returns are forwarded and whether failures leave installation partial. For reversible restoration, a proposed guard is to restore a slot only if it still contains that owner's wrapper; another addon may have replaced or wrapped it. If another wrapper captured this one, changing the public slot alone cannot remove that embedded reference. This is **design inference**, not an implemented removal protocol. M03/S06/S07. Native registration cleanup still follows its own owner and route.

## Separate requests, observations and retry authority

Recommended operation states are **requested**, **observed complete**, **reconciled**, **failed**, and **unresolved**. Define what each means for the selected operation rather than assuming these names exist in the engine. For example, acceptance into a local queue is requested; the expected identity/resource observation may establish observed completion; updating the owned campaign ledger establishes reconciled. An exception after a native effect can leave the operation unresolved even when the caller reports failure.

Record an operation ID, intended effect, target identity, relevant snapshot and last established outcome when retries could duplicate effects. A retry needs evidence that replay is safe or that the previous effect did not occur. An ID in a mod record alone does not deduplicate a native request; the actual adapter/reconciler must enforce the rule. Completion callbacks may be early, returns may be discarded, and protected calls do not roll back external effects. M03/M06/S11/S13.

For mutable notifications, document who may mutate arguments and what later listeners receive. A caller-owned snapshot or validation after dispatch can be a deliberate mod contract; the supplied dispatcher itself shares tables, ignores listener returns and has no local per-listener protection/reentry guard. Notification dispatch is therefore not a request/response protocol merely because a listener returns a value. M06.

## Completion boundary

ARCH-02 ownership synthesis closes within this selected scope. No new source trace was needed to invent a missing interface: effective manager/global/binder/startup/winner edges remain explicitly open. The [compatibility companion](compatibility-package-contracts.md) completes the dependency/package/upgrade side. DEBUG-01 next traces selected diagnostics; ARCH-03 later qualifies patterns/tests and audits the combined foundation. Runtime remains deferred. [Roadmap](../ROADMAP.md), [verification](../08-research/verification-2026-10-12-v0.1.79.md).

## Subsequent practical foundation consolidation

ARCH-03 [central guide](development-reference.md), [qualified patterns](../07-code-library/qualified-patterns.md), [test guidance](test-guidance.md) and [bounded audit](../08-research/verification-2026-10-12-v0.1.81.md) now complete the selected practical foundation. The original ARCH-02 allocation/limits above retain their research revision. Effective integration partial and runtime deferred; next separate whole-ADR audit.
