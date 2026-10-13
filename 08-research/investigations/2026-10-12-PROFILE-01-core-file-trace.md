# PROFILE-01 — Reconstructed core startup, simulation and persistence

> ADR document set: **v0.1.83**. Research revisions and source/build versions below describe their original scope.

- ID: PROFILE-01
- Subsystem: effective-profile integration; configuration, A-Life, persistence and CtZ
- ADR revision: v0.1.83
- Record status: complete-within-scope for selected uploaded core chains; effective-profile closure partial
- Source status: source-confirmed for cited snapshot implementations; scoped negative searches
- Runtime status: supplied log observed; independent reproduction untested and now authorized
- Baseline IDs and provenance record: QJLOOSE1012, QJEXP1012, QJLOG1012, QJMODS1012 and ENGINE1011; [intake](../../00-environment/profile-source-2026-10-12.md)
- Last reviewed: 2026-10-12

## Question and scope

How do the supplied core files connect startup, listeners, actor lifetime, squad/smart ownership and campaign serialization? Trace the reconstructed inputs without substituting October bundled scripts for loose winners. Completion means these selected chains have pinned definitions, callers, ownership and error/restore limits. Excludes complete addon/DLTX precedence, every manager serialized by the actor, game modifications and certification of live winners/native binary equivalence.

## Evidence and method

[Core ledger](../../evidence/profile/core-trace-2026-10-12.csv) contains P01–P36, archive-relative paths, raw full-file SHA-256, line counts and selected ranges. [Overlay comparison](../../evidence/profile/overwritten-files-2026-10-12.csv) pins six corrected paths. Read bodies, distinguish block comments from executable code, and follow selected direct callers. Do not publish uploaded scripts/log/profile data. QJEXP1012 contains a mixture of unpacked and retained loose files; the intake defines exactly how first-ZIP copies were restored.

## Findings

### Startup and global wiring

Base `script.ltx` selects `_G`; base `alife.ltx` selects `_G.start_game_callback`. The supplied global function seeds RNG, reports version/marshal availability, calls `axr_main.on_game_start`, then gets the board and other helpers. `USE_MARSHAL` is derived from `marshal ~= nil`. Final LTX/DLTX values remain unknown; these are inspected inputs. [P01–P03]

The restored `axr_main.on_game_start` enumerates root `*.script` files, excludes its explicit ignore list, accesses each module through `_G[file_name]`, collects modules with `on_game_start`, then invokes those handlers directly in a second pass. There is no dependency sort or local per-handler `pcall`. The native module-loading error policy is a separate boundary. Module-load announcements and the enumeration order do not prove all declarations ran or dependencies were ready. Board construction also occurs lazily through callers, so the later global startup call is not its sole possible creation point. [P06, P23]

The global wrappers have two formal registration arguments and no success return: register delegates to `callback_set`, unregister to `callback_unset`, addition to `callback_add`. `SendScriptCallback` dispatches listeners and then calls an `axr_main[name]` helper if present. That helper can therefore execute after listeners, and a listener error can prevent reaching it. DXML captures the prior registration functions, keeps `on_xml_read` in a separate insertion-ordered list, and delegates other names through the captured two-argument wrapper without returning its result. XML dispatch calls handlers directly. [P04, P09]

### Actual supplied dispatcher contract

The original loose dispatcher owns a private `intercepts` table and per-event increasing ranks. `callback_add` creates an event/rank counter. Registration keys the table by exact function/userdata identity; registering that identity again replaces its rank and advances the counter. Unregister removes that exact key. Unknown events and nil listeners print a diagnostic/callstack; unknown registration does not throw or return a boolean receipt. No PRE/NORMAL/POST/dependency contract is present in this supplied implementation. [P05]

Dispatch uses `_g.spairs` with `_g_patches.sort_func_values_ascend`: keys are collected and sorted by current ranks before iteration. Functions receive the arguments; userdata receive `userdata[name](userdata, ...)`. Returns are discarded. There is no local protection/reentry guard. An addition during dispatch is outside that key snapshot; removal of an already captured key does not by itself remove the key from this invocation, whose body does not test the yielded value. These source semantics are not a reproduced runtime mutation test. Comparator/global installation must also hold at invocation. [P06–P08]

The expanded ZIP's overwritten base dispatcher instead stores `true` and iterates `pairs`; neither that copy nor ENGINE1011's richer dispatcher should silently replace the first loose baseline. The restored line positions align with the provided callstacks, but winner origin/hash verification remains open. [Overlay comparison; QJLOG1012 intake]

### Actor lifetime and readiness

The actual filename is `bind_stalker.script`, selected by `configs/creatures/actor.ltx:script_binding = bind_stalker.actor_init`; the earlier collection request for `bind_actor.script` was incorrect. `actor_init` binds `actor_binder`; successful net spawn sets the first-update flag and adds the actor to `db`. Reinit installs available native callback slots and, with marshal enabled, registers the binder userdata itself for `save_state`. Teardown unregisters that same listener identity, calls the extension destroy path, removes the actor/native slots, then calls the base destructor. [P12–P14]

The extension emits `on_game_load` from net spawn and `actor_on_net_destroy` from teardown. The first alive update clears the flag before emitting `actor_on_first_update`; later ordinary updates emit through the extension. This is a lifecycle phase, not proof every simulation object/manager is ready. The supplied extension's `actor_on_net_spawn()` has no `binder` parameter even though its emission refers to `binder`; do not promise a valid binder argument from that body. Runtime/global behavior of that free name is not established. [P13–P15]

### Board, smart and squad authority

`get_sim_board` lazily creates `_G.SIMBOARD`. The board owns smart ID/name indexes, squad bookkeeping and pending assignments. Smart `on_before_register` registers the object with the board; its later `on_register` adds `db`/simulation-target registration, loads jobs, applies queued squads and realizes deferred NPC jobs. Unregister removes those registries and the sidecar object entry. `simulation_objects.object_registry`/`available_by_id` are separate structures; its unregister removes the registry element without locally clearing availability. Do not equate all these maps or certify every stale-ID lifecycle. [P23, P27, P29]

The supplied squad `on_register` stores `true` in `SIMBOARD.squads[id]`, not the squad object. Resolve by ID rather than dereferencing that value. Squad unregister emits `server_entity_on_unregister`, removes board membership and clears assignment. This event differs from generic `server_object_on_register` in the Modded Exes producer; similarly named events are not interchangeable. [P10, P26]

Board assignment queues missing smart IDs. Otherwise it saves the previous smart ID, clears old board membership/population, calls `squad:assign_smart(new_smart, old_id)`, updates new bookkeeping and emits enter/leave notifications. Squad assignment uses that old ID to unregister members before registering at the new smart. Direct field assignment alone is not this protocol; board assignment/member registration and actual arrival are separate outcomes. [P24–P25]

CtZ garrison anchoring calls assignment with the old smart, updates board assignment, clears persisted `scripted_target`/instance `get_script_target` and stores diagnostic/target fields. Movement orders clear the old roster, write `scripted_target` and route intent, and return a provider label. The supplied squad target/update path consumes that scripted target. A successful order return/log is not movement completion; `pcall` around assignment also does not prove the assignment succeeded. [P25, P31]

### Persistence and restoration phases

`alife_storage_manager` owns local `m_data`; `get_state()` returns the table itself. With marshal available, before-save sets game version, dispatches `save_state`, captures selected pstor, encodes and writes `.scoc`. There is no local atomic pairing protocol with the native save or confirmed write-completion receipt from callback registration. Missing/unreadable/empty load input returns before replacing the root; successful read decodes, replaces `m_data`, runs pre-load migration and dispatches `load_state`. The actual behavior on missing/corrupt data across sessions remains untested. [P18–P20]

The October native source calls the Lua before-save hook before native packet serialization and calls the Lua load hook before native header/spawn/object restoration, under `ENGINE_LUA_ALIFE_STORAGE_MANAGER_CALLBACKS`. This explains the inspected staged design; it is not proof the reported binary is compiled from those bytes. [P35–P36]

The actor binder's marshal branch restores its own state directly during binder load because it is not ready at the earlier `load_state` broadcast. Its fields live under `m_data.game_object[id].actor_binder`; save state also calls derived manager serializers outside this bounded trace. The helper stores object name on first creation but does not compare it when reusing an existing ID entry; its comment is not an implemented name-validation guarantee. The unregister helper clears sidecar entries after listeners through the global dispatch path. [P16–P22]

Squad and smart `save_state/load_state` examples are enclosed in block comments. Active `STATE_Write/STATE_Read` paths retain packet serialization even with marshal available. Squad packets store target/respawn/smart/scripted-target fields and invoke load initialization; smart packets retain arriving NPC/job/respawn/alarm data and defer job realization. A marshal-enabled actor therefore does not imply a wholly sidecar-serialized simulation. [P26, P28]

CtZ `save_state` assigns the campaign table directly to `m_data.ctz_state`; this is an alias until encoding, not a copied snapshot. Load obtains that table or initial state and repairs selected fields. The supplied version constants are internal 0.0.3b/schema 9 despite Alpha 0.0.5j packaging. `on_game_load` quarantines targets; first update excludes `fake_start`; ordinary update gates real-world readiness and transition grace before restoration/initialization. `restore_loaded_squads` resolves saved IDs and reattaches transient ownership/member setup, rather than serializing every instance field. These are source gates, not a passed roundtrip test. [P30, P32–P33]

CtZ's `safe_register` wraps registration in `pcall`; its optional `axr_main.callbacks` check does not inspect the supplied private registry, and no such exposed field is defined in this supplied dispatcher. Since unknown-event registration logs without throwing, protected-call success cannot certify listener installation. [P05, P34]

### Observed diagnostic mismatch

QJLOG1012 contains ten script-load error records (five names twice) and twelve missing-callback records (six names twice). Supplied `callbacks_gameobject.script` declares both `server_object_on_register` and `on_luabind_fatal_error` at module scope and installs native-facing global emitters. The log announces that module's load but later rejects those names. The cleanup listener in `aaaa_script_fixes_mp` is requested on first update and rejected at the logged request. The evidence does not explain why the declarations were unavailable or establish every cleanup route failed. [P10–P11; intake log table]

## Competing explanations and missing edges

Potential explanations include a different effective producer/global file, failed or partial module execution, later registry/global replacement, or a reconstructed snapshot that omits relevant addon behavior. These remain hypotheses. The static declaration/announcement mismatch does not justify patching callback names, replacing the dispatcher or claiming the executable incompatible.

Final MO2 origins/winners, all relevant loose addons and final config/DLTX merges are not established. Five failing addon modules/providers are absent from the collection. Native hook/comparator installation and complete registration order need observation. This record closes selected core source tracing, not all ADR subsystem effective closure.

## Checks and outcomes

Raw archive/source hashes, six overlay corrections, campaign byte equality, cited range bounds and source-path ownership checked. Repository navigation/banner checks and unchanged historical evidence are checked in [v0.1.83 verification](../verification-2026-10-12-v0.1.83.md). The supplied log is observed evidence; no new game run, native compilation, save edit or CtZ gameplay change was performed.

## Disposition and next work

Core trace complete within this scope. Runtime is **authorized and untested**, superseding the earlier current deferral while preserving dated conclusions.

Next bounded test should record the same profile/reported executable, MO2 origin and raw hashes of `_g`, `axr_main`, `_g_patches`, `dxml_core`, `callbacks_gameobject`, actor binder/extension and simulation overrides. Observe registration/emission order for the two declared-but-rejected names without changing event tables. Then test a disposable campaign save/load and a level transition, recording CtZ state/schema, squad/member IDs, smart assignments and target reattachment before/after; preserve both native save and `.scoc`. A registration receipt must observe invocation or registry state, not merely `pcall` success. Collect the five failed modules/providers separately for addon triage. No runtime probe is claimed implemented here. [Current roadmap](../../ROADMAP.md).

This installed-snapshot supplement qualifies earlier generic source references rather than replacing them: [configuration guide](../../04-game-systems/configuration/development-reference.md), [A-Life guide](../../04-game-systems/alife/development-reference.md), [persistence guide](../../04-game-systems/persistence/development-reference.md), [architecture guide](../../05-mod-architecture/development-reference.md).
