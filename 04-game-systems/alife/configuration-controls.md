# A-Life configuration and control reference

> ADR document set: **v0.1.68**. Research revisions and source/build versions below describe their original scope.

- ID: ALIFE-11
- Source status: source-confirmed within the selected ENGINE1011 paths
- Runtime status: untested; deferred until the user resumes verification
- Last reviewed: 2026-10-11

This maps control producers to consumers. It does not prescribe tuning values. ENGINE1011 is the uploaded October 11 archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; exact upstream commit and installed executable/configuration correspondence remain unknown. N01–N18 below refer only to the [native control ledger](../../evidence/alife/configuration-controls-2026-10-11.csv), with file paths, symbols, line ranges and full-file hashes.

Read with the [lifecycle/state map](lifecycle-state-reference.md), [callback phases](callback-phase-reference.md), [simulator API](../../02-lua-api/alife/simulator-api.md) and [Warfare policy controls](../warfare/policy-controls.md).

## Native settings and their consumers

| Setting/control | Producer/read point | Consumer/effect | Boundary |
| --- | --- | --- | --- |
| `schedule_min`, `schedule_max` | `CALifeUpdateManager` reads `pSettings` using its passed section; stores `shedule.t_min/t_max` | General engine scheduler computes the next manager interval; ALife `shedule_Scale()` returns 0.5 | Scheduler inputs, not guaranteed observed intervals or one brain update per interval. N01/N09/N10 |
| `objects_per_update` | Same settings section; reload applies stored value; Lua `set_objects_per_update(u32)` changes schedule-registry value | Schedule predicate stops after the configured entry count and guards each cycle | Count of registry entries, not all living NPCs. Zero permits none; eligibility/membership/activity are separate. N01/N04/N05/N15 |
| `process_time` | Same settings section; reload calls `set_process_time(int microseconds)`; Lua helper forwards an integer | Manager expression forwards a float budget to graph/current-level iterator | Named input units do not certify a microsecond cutoff; see the literal chain below. Schedule registry disables the inherited time limit. N01/N04/N06–N08/N15–N17 |
| `update_monster_factor` | Same settings section, float stored by update manager | Appears in the manager's process-time expression | Not a standalone monster speed/population multiplier or a proved scheduled-brain time allocation. N01 |
| `switch_distance`, `switch_factor` | Switch manager reads its passed settings section; setters recompute thresholds | Online/offline decision uses `D(1-F)` / `D(1+F)` | Setter does not clamp input; active values unknown. Lua binds distance getter/setter in scoped registration, not a factor setter there. N02/N03/N15 |
| `going_speed`, optional `current_level_going_speed` | Monster constructor reads its entity section; absent current-level speed falls back to going speed | Offline detail path chooses current-level or other-level speed and consumes elapsed game time | Distinct from online client locomotion and scheduler batch size. N11/N13 |
| `travel_speed(float)`, `current_level_travel_speed(float)` | Lua helpers write those entity-owned speed fields directly | Subsequent detail-path speed selection | Field setters do not independently create tasks, realize clients or establish smart arrival. N12/N13 |
| `smart_terrain_choose_interval` | Individual monster-brain constructor parses `hours:minutes:seconds` from object-name settings section and forms a time interval | Throttles individual smart task selection against game time when not already assigned and selection is enabled | Group brain uses virtual Lua `get_current_task`; this is not a universal group strategy timer. N14 and [ALIFE-05](../../08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md) |

These are actual read locations and fields, not a claim that a particular installed `alife.ltx` supplies the selected section or values. No native configuration file from the user's effective profile is asserted here.

## Time and count limits are different

The normal engine scheduler reads millisecond `Device.dwTimeGlobal`. In the selected path it computes `dwMin=max(30,t_min)`, `dwMax=(1000+t_max)/2`, derives an interval using `shedule_Scale`, clamps it and reschedules the manager. This is a transformed scheduler interval, not simply the midpoint of raw `schedule_min/max`. The manager can defer later updates to `Device.seqParallel` under `mtALife`; installed threading and observed cadence are unknown. N01/N09 (`xrSheduler.cpp:315–390`)/N10.

The inspected process-time chain must be quoted literally:

```text
graph budget = float(microseconds)
               - float(microseconds) * update_monster_factor() / 1000000.f
```

`CALifeGraphRegistry::set_process_time` forwards this value to the current-level registry; new level setup also applies the stored value. The inherited iterator setter stores it unchanged, and `time_over()` compares `GetElapsed_sec()` against it when time limiting is enabled and the first-update bypass is inactive. The level registry uses the default time-limit specialization; the scheduled registry explicitly uses `false`. N01 `144–151`; N06 `98–140`; N07/N08/N16/N17.

**Scoped clarification:** the method's parameter name and Lua helper establish the named integer input, but the inspected forwarding/comparison chain does not justify documenting it as a reliable microsecond wall-clock limit. Preserve the expression and units rather than silently rewriting the formula. This source observation is not a reproduced runtime bug or a recommendation to alter the engine. It qualifies the API's named input contract without changing earlier findings that scheduled updates use an entry count.

Offline movement independently uses game-time delta, converts milliseconds to seconds, divides by `normal_time_factor()` and multiplies by selected speed. First-timestamp handling, path failure and graph-edge consumption affect progress. `objects_per_update` affects when movement is processed; it does not multiply travel speed directly. N13 `104–117,200–287`; [scheduling investigation](../../08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md).

## Permission and update controls

| Control | Changes | Does not establish |
| --- | --- | --- |
| `set_switch_online/offline(id,bool)` | Effective object's permission bits via native setters | Immediate transition, client readiness, bypass of outer level/attachment/group checks. N01/N03/N15 |
| `forced_online_status` | Bundled script permission override: true blocks offline, false blocks online, nil leaves native result | An atomic status refresh/switch operation; active Warfare producer can replace the bundled one. N18 and [Warfare controls](../warfare/policy-controls.md#online-status-policy) |
| `set_interactive(id,bool)` | Interactive flag | Same meaning as switch permission, scheduled membership or alive status. N01 and [ALIFE-05](../../08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md) |
| `force_update()` | Calls `update_scheduled(true)` | Full manager switch pass, fresh client synchronization or completed strategic arrival. N15 |
| Brain `can_choose_alife_tasks(bool)` | Allows/prevents new individual smart task selection | Clearing an existing assignment or stopping processing of its existing task. N14 and [brain API](../../02-lua-api/alife/server-squad-api.md#task-and-movement-controls) |

Native thresholds use stored server 3D positions; Warfare's selected capture/combat ranges use squared X/Z distances. Do not substitute one range for another. The complete permission truth table, native object exceptions and group member gates remain in [ALIFE-08](../../08-research/investigations/2026-10-11-ALIFE-08-switching-eligibility.md).

## Development use and open inputs

For a later CtZ change, first identify whether the problem concerns scheduling, travel, permission, client realization or strategic policy. Record the effective producer, setter and consumer, the relevant clock/units, and the observation phase before selecting a control. This is design guidance, not a tested tuning recipe.

Still unknown: installed native settings, addon writes to these fields, actual executable/build flags and timing, and effective smart/board policy. Source consolidation is complete within this page's scope; [completion status](source-completion-status.md) keeps those missing chains and runtime work separate.
