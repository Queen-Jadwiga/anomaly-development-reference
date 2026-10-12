# Available-source consolidation audit — ADR v0.1.43

> ADR document set: **v0.1.63**. Research revisions and source/build versions below describe their original scope.

- Date: 2026-10-11
- Scope: ALIFE-11 / WAR-003 controls, bounded A-Life/Warfare consistency review and repository integrity
- Source status: source-confirmed within selected paths; scoped negative searches remain bounded
- Runtime status: untested; deferred until explicitly resumed by the user
- Publication base: v0.1.42, commit `34e4aea345e5c8506e94ad300c8b32e0241d6c9b`

## Baselines and completion boundary

ENGINE1011 and BETA150 are pinned by archive hashes in the [manifest](../evidence/manifest.md). Exact engine upstream commit/executable correspondence, installed winning scripts, applied presets and active settings remain unknown. ZIP142 and the supplied CtZ sources retain their earlier evidence roles. No installed profile is inferred from archive names or public defaults.

The planned available-source consolidation is complete within scope. The overall effective A-Life/Warfare section remains partial. [Completion status](../04-game-systems/alife/source-completion-status.md) lists four required effective-source chains: board/smart assignment, Warfare startup/policy, death/safe release and persistence integration. This report does not certify every sentence, export, configuration, variant or runtime behavior.

## Bounded consistency review

Review compared the practical lifecycle/callback references, focused APIs, preceding investigations and selected native/package control definitions. Newly traced settings consumers supplement the previous investigations; historical conclusions remain preserved.

| Boundary reviewed | Consistent interpretation / qualification | Research basis |
| --- | --- | --- |
| Creation versus registration | Immediate creation, registry insertion and deferred/bulk callbacks have different phases; a registration callback is not universal readiness | [ALIFE-02](investigations/2026-10-11-ALIFE-02-creation-registration-release.md), [callback reference](../04-game-systems/alife/callback-phase-reference.md) |
| Native unregister versus release | Unregister hook precedes registry removal; release and online event paths are separate contracts | ALIFE-02; native `alife_simulator_base2.cpp`, `alife_simulator_base.cpp` |
| Load and identity | Server identity can survive client teardown; numeric IDs can be reused; load registration precedes late member-pointer repair | [ALIFE-04](investigations/2026-10-11-ALIFE-04-save-load-identity.md), lifecycle/callback ledgers |
| Scheduling and brains | Count-limited registry processing differs from wall-clock budget and group Lua task policy; `force_update` invokes scheduled work | [ALIFE-05](investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md), [ALIFE-11](investigations/2026-10-11-ALIFE-11-configuration-controls.md) |
| Graph/group/client realization | Group container and realized members are different representations; graph movement and Lua arrival are separate | [ALIFE-06](investigations/2026-10-11-ALIFE-06-graph-online-realization.md), lifecycle reference |
| Spawn callbacks | Early lookup/binder callbacks, queued post-full-spawn delivery, immediate add-time delivery and guarded after-spawn callback differ | ALIFE-06 / [ALIFE-10](investigations/2026-10-11-ALIFE-10-lifecycle-callback-consolidation.md); `Level_network_spawn.cpp` |
| Position and teardown | Client, stored server, graph and display state differ; selected offline route does not establish a final snapshot barrier | [ALIFE-07](investigations/2026-10-11-ALIFE-07-client-server-offline-teardown.md) |
| Permission versus command | Hysteresis/permission and outer group/attachment gates remain; a forced-status producer is not an atomic transition | [ALIFE-08](investigations/2026-10-11-ALIFE-08-switching-eligibility.md), ALIFE-11 / WAR-003 |
| Strategic state | Target selection, board assignment, reach/arrival and owner policy are distinct; missing board/smart internals remain open | [WAR-002b](investigations/2026-10-11-WAR-002b-policy-offline-combat.md), [WAR-003](investigations/2026-10-11-WAR-003-configuration-policy-controls.md) |
| Death and persistence | Direct creature death does not prove native group notification/safe release; explicit strategic saves do not prove arbitrary Lua serialization or global dispatch order | WAR-002b / ALIFE-04; completion status |
| Control clocks and refresh | Native scheduler, game-time travel/capture and event requests differ; options tables, locals/caches and optional UI declarations have distinct refresh/provenance | ALIFE-11 / WAR-003 |

**Explicit qualification added:** the earlier API table described `set_process_time(int)` as a microsecond input. Its integer parameter is named `microseconds`, but the literal native expression and unchanged forwarding reach an elapsed-seconds comparison. The current API links to [the full qualification](../04-game-systems/alife/configuration-controls.md#time-and-count-limits-are-different). This is a bounded source correction to the unit promise, not a runtime defect finding or a rewrite of earlier count-limited scheduling conclusions.

WAR-003's full-file negative searches establish only that the inspected main offline-combat module has no recomputation assignment for its module-local Warfare radius and no demonstrated `offline_health` consumption. External reloads, later replacements and other addons remain possible.

## Verification results

- Verified every original blob in the local v0.1.42 snapshot against the published base tree before comparison.
- Preserved all 21 previous CSV blobs byte for byte, all 33 previous investigation bodies apart from their current document-set banners, and all three historical snapshots byte for byte. No repository file was deleted.
- Resolved 310 hash-bearing evidence rows against the retained source snapshots; verified full-file SHA-256, recorded line counts, 385 range groups and recorded symbols where present. Datasets without a compatible path/hash field are outside this hash check; the supplied archive-comparison dataset remains preserved.
- Added two 18-entry control ledgers: N01–N18 across 18 native files and W01–W18 across nine main/optional-patch files. IDs are ledger-local; no third-party source files are distributed.
- Rebuilt six ALIFE-09 catalog outputs from the same engine and Warfare inputs and compared their bytes with the repository: exact matches. Extraction reported 84 class rows, 1,150 bindings, 174 helper declarations and 1,372 script declarations; this is extraction scope, not exhaustive API certification.
- Repository checker passed: 130 Markdown files, 693 local targets and 14 anchors, with zero errors. Checks cover Markdown targets/anchors, required C-03/C-04/CtZ navigation, current version/banner consistency, absence of obsolete forwarding pages, nonempty files and CSV row widths.
- Ran all seven existing checker tests, covering meaningful failure cases. No engine compilation, gameplay changes or in-game tests were performed.
- Publication uses the inspected base tree and expected-head lease. The full remote path/blob map and published head are compared with the intended tree, followed by readback of the new references/evidence and version.

## Disposition

The available-source reference and bounded audit are complete. Effective source closure requires the missing installed chains; runtime verification remains deferred. The [roadmap](../ROADMAP.md) uses that distinction. Existing evidence, research history and source limitations remain visible as the ADR grows.
