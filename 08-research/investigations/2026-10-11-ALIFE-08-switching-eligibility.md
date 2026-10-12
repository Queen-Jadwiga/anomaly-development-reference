# ALIFE-08 — Switching eligibility, hysteresis and forced states

> ADR document set: **v0.1.60**. Research revisions and source/build versions below describe their original scope.

**ADR v0.1.38 · 11 October 2026 · bounded source pass complete; effective profile and runtime pending.**

Native switching uses two virtual permissions and two distance thresholds. Permission to enter a state is not a command to enter it immediately. Squads add member checks and Lua policy; attachment, registry membership and location synchronization bound the path before those checks.

## Baseline

Native and bundled Lua evidence uses the supplied `xray-monolith-2026.10.11` archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`. Exact upstream commit and installed executable correspondence are unverified. The Warfare comparison uses BETA150 main from archive SHA-256 `9f71999bb44cb6d3e41c431feaf5be4714159522df1fa8d71599ac039946315d`, not an assumed installed winner. See [WAR-002a](2026-10-11-WAR-002a-source-packages-effective-profile.md).

[Evidence ledger](../../evidence/alife/switching-eligibility-evidence-oct11.csv): E01–E18 identify engine-archive files; W01 identifies the Warfare main file. Paths below are archive-relative; all line numbers are one-based. Full-file hashes identify the inspected bytes.

## 1. Which objects reach the test

The update manager runs the current-level registry's switch pass before scheduled updates. Its switch predicate uses `m_switch_counter` to avoid revisiting the same object in a cycle. The level registry rejects additions whose game-graph level differs from its level. Thus a force-online policy in this path is not a command to realize entities on another level. **E01:** `src/xrGame/alife_update_manager.cpp:34–57,92–118`; **E02:** `src/xrGame/alife_level_registry_inline.h:23–50`.

`switch_object` first releases redundant objects, then calls location synchronization, then dispatches by `m_bOnline`; it checks redundancy again afterward. An empty online/offline group is redundant. The synchronization manager bypasses location work for objects not using AI locations, attached objects and offline objects with invalid node IDs; otherwise a false synchronization result prevents the switch attempt. A bypass returning true is not itself a veto on switching. **E03:** `alife_switch_manager.cpp:127–247`; **E06:** `alife_online_offline_group.cpp:319–322`.

Both manager try-switch methods return for an attached object (`ID_Parent != 0xffff`). Its representation therefore does not independently follow an actor-radius test here. Group registration also removes member objects from separate registry processing and can align a new member/group online state directly, outside the normal distance test. **E03:** same file:160–227; **E06:** `alife_online_offline_group.cpp:102–148`; **E04:** `alife_graph_registry.cpp:49–84,157–178`. See [ALIFE-02](2026-10-11-ALIFE-02-creation-registration-release.md) and [ALIFE-06](2026-10-11-ALIFE-06-graph-online-realization.md) for realization details.

## 2. Two thresholds and exact boundaries

The switch manager reads `switch_distance` and `switch_factor` from its settings section. Setting either recalculates both thresholds. **E05:** `alife_switch_manager_inline.h:11–45`.

Let `D = switch_distance`, `F = switch_factor`, and `d` be the three-dimensional Euclidean distance between the actor's stored server `o_Position` and the tested object's stored `o_Position`:

| Threshold | Formula | Ordinary individual transition when both permissions are true |
| --- | --- | --- |
| Online | `D × (1 − F)` | Offline → online when `d <= online_distance` |
| Offline | `D × (1 + F)` | Online → offline when `d > offline_distance` |

For positive `D` and `0 < F < 1`, the interval between these thresholds preserves the object's existing state: hysteresis. Equality at the online threshold permits realization; equality at the offline threshold retains online state. This is a conditional mathematical interpretation, not a claim about active configuration values. The inspected setter does not clamp its inputs; negative/reversed thresholds must not be silently normalized in documentation. Effective settings and Lua changes to distance remain unknown. **E07:** `alife_dynamic_object.cpp:133–187`; **E05** as above.

Distances here use imported server positions, not a guaranteed current rendered client position. See [ALIFE-07](2026-10-11-ALIFE-07-client-server-offline-teardown.md). No exact polling interval or transition delay is asserted.

## 3. Permissions and forced behavior

For the base A-Life implementation, `can_switch_online()` is `match_configuration() && flSwitchOnline`; `can_switch_offline()` is `!match_configuration() || flSwitchOffline`. Boolean setters modify those bits. Configuration matching is virtual, so the raw bit alone does not determine the effective result. **E08:** `xrServer_Objects_ALife.cpp:574–610`; **E09:** `xrServer_Object_Base.h:155`; **E10:** `xrServer_Objects_ALife_Monsters.cpp:1041–1047` includes the DEBUG creature designer-mode override.

The individual dynamic object's decision order is:

| Effective online permission | Effective offline permission | Currently offline | Currently online |
| --- | --- | --- | --- |
| true | true | Apply online distance test | Apply offline distance test |
| true | false | Switch online without distance test | Stay online |
| false | true | Stay offline / failed-switch hook | Switch offline without distance test |
| false | false | Stay offline / failed-switch hook | Stay online |

**E07:** `alife_dynamic_object.cpp:133–187`. The two false permissions preserve the current state; they do not select a preferred state. Other outer gates still apply. The offline individual path also reconciles scheduled membership before checking online permission, and its failed-online hook clears eligible client data. **E07:** same file:133–146,294–307; see ALIFE-05/07.

`alife():set_switch_online(id, value)` and `set_switch_offline` resolve the server object and call its permission setters. They do not call `switch_online`/`switch_offline` in their bodies. Simulator Lua exports also provide `switch_distance()` and `set_switch_distance()`; no switch-factor export is present in the inspected registration window. **E01:** `alife_update_manager.cpp:333–345`; **E11:** `alife_simulator_script.cpp:664–665,689–691`; **E12:** `xrServer_Objects_ALife_script.cpp:53–54`. This is a scoped registration statement, not a claim about every possible Lua interface.

## 4. Online/offline groups add another gate

This section concerns `CSE_ALifeOnlineOfflineGroup`, the native base of the supplied scripted simulation squad. It does not substitute the separately implemented `CSE_ALifeGroupAbstract` algorithm. **E13:** `alife_group_abstract.cpp:116–215`.

For a nonempty group:

- **Coming online:** reject if group online permission is false. If offline permission is false, delegate directly to the inherited dynamic-object attempt. Otherwise iterate members, verify alive/switch-permission invariants, and look for a member at or inside the online threshold. Finding one delegates to the inherited attempt, which still tests the **group's** position when both permissions remain true. If no member qualifies, run the failed-online hook.
- **Going offline:** reject if group offline permission is false. If online permission is false, switch directly. Otherwise verify member invariants and keep the group online if **any** member is at or inside the offline threshold; only after all members are outside does it switch.

**E06:** `alife_online_offline_group.cpp:201–268`. The member `VERIFY3` statements are invariant checks, not ordinary skip/filter branches. Their build behavior should not be turned into a universal runtime recovery guarantee.

For ordinary online realization, a nearby member is therefore necessary but not always sufficient: inherited group-position eligibility remains. Normal offline updates copy group position to members, but other mutation paths mean we should preserve the two checks in the contract. Before online-to-offline testing, group location synchronization mirrors its first member's stored position/node/graph/distance; the offline branch of that method does not do this copy. **E06:** same file:55–99,183–198; see ALIFE-05/06.

## 5. Creature and object exceptions

Native creature offline permission additionally requires `get_health() > 0`. A dead creature's blocked offline permission can consequently bypass distance when coming online if its online permission is true. This describes that individual native path, not permission for dead members to remain in a living squad: group methods verify alive members. Ammo offline permission requires nonzero `a_elapsed`; space restrictors, breakables and climbables return false from their examined offline-permission overrides. **E10:** `xrServer_Objects_ALife_Monsters.cpp:1182–1195`; **E14:** `xrServer_Objects_ALife_Items.cpp:893–901`; **E08:** `xrServer_Objects_ALife.cpp:847–850,2063–2066,2140–2143`. These are selected exceptions, not an exhaustive entity-class audit.

## 6. Lua forced status and the Warfare boundary

The group registration uses a wrapper with virtual permission exports. The wrapper calls the Lua member and supplies an inherited static fallback for explicit base calls; its catch-all returns zero on exceptions. The effective permission can therefore be narrower than the native flag result. **E15:** `xrserver_objects_alife_monsters_script3.cpp:85–111`; **E16:** `xrServer_script_macroses.h:57–63,278–284,363–366,469–471`; **E17:** `script_export_macroses.h:41–42,61–77`.

The bundled `sim_squad_scripted` permission overrides check the native base first. `forced_online_status == true` blocks switching offline; `false` blocks switching online; nil leaves native permissions unchanged. Thus this status affects a later permission test rather than directly invoking realization. **E18:** `gamedata/scripts/sim_squad_scripted.script:1104–1138`.

The bundled status producer and supplied Warfare replacement differ. The bundled producer gives story squads no enforced status, then checks task force-online, `__lock`, survival, companions and other policies; its underground branch does not force a status. The BETA150 Warfare replacement prioritizes survival, force-online, companions, then forces online on levels outside `level_weathers.valid_levels`; later branches handle monster hours or offline non-story proximity exclusion. Its definition replaces the method at module scope, but active loading and later replacements remain unverified. Numeric time tests also differ between implementations. **E18:** same file:1035–1102; **W01:** BETA150 main `gamedata/scripts/warfare_options.script:255–304`.

The squad's update computes this status in `check_online_status`; the native manager consumes virtual permissions in its own switch pass. These inspected functions do not establish an atomic status-refresh/switch transaction. Do not infer exact cross-layer scheduling or universal Warfare behavior from the field name or archive comment. See [WAR-002b](2026-10-11-WAR-002b-policy-offline-combat.md) for prior override/callback findings.

## Disposition

The bounded native switching investigation is complete. No game tests or gameplay modifications were performed; no installed distance values are asserted.

The agreed remaining scope is: close effective smart/board/job and arrival chains, creature-death/safe-release chains, startup/override order and persistence integration when winning sources become available; then consolidate the CtZ-relevant APIs, state/callback maps and evidence audit. Runtime validation stays deferred. Exhaustive unrelated creature AI and entity-class coverage remain optional expansion rather than prerequisites.
