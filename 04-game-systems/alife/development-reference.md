# A-Life development reference

> ADR document set: **v0.1.79**. Research revisions and source/build versions below describe their original scope.

- ID: STRUCT-01-ALIFE
- Subsystem: A-Life
- Reference revision: v0.1.67 navigation synthesis; original research revisions retained
- Source status: synthesis of linked source-confirmed selected native/bundled contracts
- Runtime status: untested; deferred
- Baseline/provenance: ENGINE1011 and qualified supplied packages; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

Start here for practical A-Life development. The existing [lifecycle/state reference](lifecycle-state-reference.md) and [callback-phase reference](callback-phase-reference.md) remain the detailed central syntheses; this page gives them the same entry point used by newer subsystems. Available-source work is complete within its selected scope; effective integration remains partial under the [shared A-Life/Warfare completion rule](source-completion-status.md).

## Choose the representation and observation point

Persistent server identity, live client objects, native member/group state and Lua board/bookmarks are separate representations. Client absence does not establish permanent removal; native membership does not establish smart assignment or arrival. Use [lifecycle/state](lifecycle-state-reference.md#representations-and-authorities) before choosing an API, and [callback phases](callback-phase-reference.md) before treating registration, load or destroy notifications as final readiness.

| Development question | Detailed reference | Supporting API or research |
| --- | --- | --- |
| Object identity, creation, registration and release | [Lifecycle/state](lifecycle-state-reference.md) | [Simulator API](../../02-lua-api/alife/simulator-api.md), ALIFE-01/02 |
| Squad members, scheduling and movement | [Lifecycle/state](lifecycle-state-reference.md) | [Server/squad/task API](../../02-lua-api/alife/server-squad-api.md), ALIFE-03/05 |
| Graph location, realization and offline teardown | [Lifecycle/state](lifecycle-state-reference.md) | ALIFE-06/07/08 linked there |
| Observation/readiness and Lua ownership | [Callback phases](callback-phase-reference.md) | [Class map](../../02-lua-api/alife/class-map.md), ALIFE-10 |
| Permissions, thresholds, clocks and configuration | [Native controls](configuration-controls.md) | [Control APIs](../../02-lua-api/alife/README.md), ALIFE-11 |
| Strategic targeting, ownership and combat | [Warfare development reference](../warfare/development-reference.md) | Supplied policy differs from native simulation |

[API catalog](../../02-lua-api/alife/README.md), [source ledgers](../../evidence/alife/README.md), [ALIFE-10 consolidation](../../08-research/investigations/2026-10-11-ALIFE-10-lifecycle-callback-consolidation.md), [bounded final source audit](../../08-research/verification-2026-10-11-v0.1.43.md). Existing evidence IDs and source ranges are retained in those canonical pages.

For mod design, choose the authority needed by the operation, retain durable IDs with campaign/lifecycle safeguards, and distinguish requested switching from completed realization. [Persistence](../persistence/development-reference.md) and [gameplay-state restoration](../gameplay/development-reference.md) supply cross-system limits. Missing effective board/smart, death/release, startup and storage chains remain in completion status; no new runtime or engine API certification is introduced here.
