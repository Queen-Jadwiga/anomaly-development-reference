# Supplied world/navigation consumers and effective boundaries

> ADR document set: **v0.1.80**. Research revisions and source/build versions below describe their original scope.

- ID: WORLD-04-CONSUMERS
- Research revision: v0.1.73
- Source status: selected supplied callers source-confirmed; scoped package comparison; effective installed closure partial
- Runtime status: untested; deferred
- Last reviewed: 2026-10-12

[Ledger C01–C13/S01–S13/Z01](../../evidence/world/supplied-consumers-2026-10-12.csv), [package comparisons](../../evidence/world/package-comparison-2026-10-12.csv), [scope/file hashes](../../evidence/world/supplied-scope-2026-10-12.json). Source IDs use the [manifest](../../evidence/manifest.md): ENGINE1011 bundled gamedata/native extensions, BETA150 **main only**, ZIP142 alternative upload. No actual winning profile is inferred; source/assets are not redistributed.

## Relocation, patrol and restore callers

Supplied set_squad_position forces container relocation only when offline, computes per-member offline bookmark vertices, then resets animation and requests live NPC relocation or writes only the server member position. This body does not atomically synchronize every graph/node/member/client/cache representation or validate every vertex result. Spawn selection separately tries explicit spawn_vid, selected spawn_point patrol point 0, smart patrol point 0, then smart location. Constructing patrol before testing the returned object does not turn its THROW precondition into safe existence handling; numeric IDs/vector truthiness are not sufficient validity checks. BETA150 S01/S02, `sim_squad_scripted.script:638–687,835–857`; [WORLD-02](spatial-queries-relocation.md).

ENGINE1011 monster spawn favors offline bookmark over spawned-vertex cache, clears the selected cache, then requests set_npc_position. Destroy clears callbacks, emits monster notification and later stores location/section. The bundled startup patch calls original motivator/monster destroy before clearing recognized squad bookmarks. Existing [A-Life realization](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md) retains the mechanism; missing xr_motivator and winning startup/replacement order remain effective gaps. C03/C04. The live binder patrol extrapolation caller explicitly tests path existence before constructing patrol/reading current flags, unlike the selected squad spawn caller; it still depends on a valid current patrol point. C02.

Base squad constructor/packet STATE writes do not add explicit durable current_spot_id/spot_section/warfare_spot fields. Alternate save_state/load_state bodies and their constructor registration are commented in the selected file. Native parent serialization and custom marker registry are different owners; no inference of autosaving all Lua fields is made. Load calls init_squad_on_load and delegates smart assignment. Task handoff reads effective target npc_info.job/alife_task or target fallback; squad am_i_reached is its own empty/same-ID test. These are references to existing [A-Life job/arrival gaps](../alife/source-completion-status.md), not new installed arrival guarantees. S04/S05.

## Base versus Warfare marker policy

| Supplied consumer | Native marker identity used | Script-side authority and limit |
| --- | --- | --- |
| Base squad refresh/show/hide | commander ID + selected type | current_spot_id/spot_section; commander change hides then updates/recurses; special markers can latch show_disabled; PDA/faction/level checks select icon |
| Warfare replacement show/hide | squad container self.id + selected type | warfare_spot for registered Warfare; spot_section in nonregistered branch; fog/distance/relationships/PDA determine add/hint/remove requests |
| Smart-terrain show/hide | smart self.id, plus target smart IDs | warfare_spot, target_spots and other.actor_target tables coordinate normal/target spots; ownership/fog/options update icons |
| Task target functors | squad.id + red_location | > 2,500 squared position distance adds; nearer removes; numeric native existence comparisons used |

BETA150 S03/S06/S07/S12/S13: base squad `1163–1264`, replacement squad `365–540`, selected smart `3644–4000`, assault `211–249`, smart-control `173–215`. These supplied callers compare map_has_object_spot with 0/1 or ~=0, avoiding Lua-zero truthiness. State fields and add/hint/remove calls remain separate from actual manager entries and visible/drawn state. Native callbacks may precede updates to those fields; external removal/loaded marker state can disagree with cached script intent. No installed duplication, loss or recovery defect is asserted. [WORLD-03 marker contracts](interaction-transitions-markers.md).

Warfare show/hide methods replace the base class methods through namespace assignment. In the nonregistered show branch, spot_section can be used while replacement hide only checks warfare_spot; base commander bookkeeping is not a universal authority after replacement. This is a selected cross-method mismatch to inspect under the winning implementation/startup/state, not a runtime-confirmed bug. Smart-control's source presence does not establish configured use; [TASK-02](../tasks/supplied-task-dialogue-consumers.md) retains its cache/readiness and absent active task-reference qualifications.

## Configuration and zone conditions

warfare_options reads ui_options paths and registers an option-change listener. Selected defaults/preset values are declarations, not the user's active values. The canonical menu reader/declaration uses hide_underground_smarts, while the selected preset has hide_undegraund_smarts and hide_undergraund_smarts. The member spelling options.hide_undegraund_smarts is distinct from the requested path. ui_options get reads exact configured IDs or defaults; selected preset application checks a matching option table/type before caching values. No canonical preset value or installed alias fix is inferred from the misspelled rows. Winning preset includes, current axr_options values and replacement option readers remain needed. S08–S10, `warfare_options.script:24–55,83,302–304`, preset `1–33`, `ui_options.script:475–482,1091–1169,1940–1995`.

xr_logic configured on_actor_in_zone/not_in_zone reads db.actor_inside_zones; on_npc_in_zone/outside resolves a live object and delegates utils_obj.npc_in_zone with db.zone_by_name. Actor-inside/outside also delegates that helper. Native contact lists, geometry and Lua zone tables cannot be equated without the missing producers/helper. Parsing numbered condition keys and dispatch still use [TASK-02's BETA150/ZIP142 return-dependent effect difference](../tasks/supplied-task-dialogue-consumers.md). S11. No base zone/teleport binder or map_spots.xml is present by the requested filenames in these three selected gamedata roots; this is a scoped file-presence result, not absence from the actual installation.

## Use and dynamic restriction consumers

ENGINE1011 monster update installs/clears native use callbacks based on dead/looted/knife state; its use callback relays monster_on_actor_use_callback. Knife/looted producers and the actual listener are missing selected dependencies. The living small-creature kick callback applies a hit rather than proving generic use success. Patrol and use callback slots are reconstructed/cleared by binder lifecycle, not certified durable listeners. C01–C03; [WORLD-03](interaction-transitions-markers.md). The before-item-pickup wrapper returns mutable flags.ret_value after SendScriptCallback, which is a separate native bool veto from void use callbacks. C05.

Bundled anomaly policy collects selected anomaly shapes and online monster references, polls a camera/distance-gated subset, switches live restrictor type between enum 2 (default-in) and 3 (none), then invalidates affected monsters. It registers the active actor-update loop after loading-screen dismissal; alternative entity-loop registrations shown are commented. This is selected runtime policy source, not guaranteed one-second updates, continuous contact, universal safe reference retention or verified AI avoidance. C06. Native force_set_restrictor_type requires a space restrictor, checks enum/same-type, unregisters/registers the live manager; invalidate_restrictions requires CCustomMonster and sets actual(false). Holder/default callbacks retain their own preconditions. These live methods do not write a matching server restrictor field in the inspected body. C07–C10. Other enum values, full anomaly damage/pathfinding and physics remain outside selected consumer closure.

dynamic_items_by_level wraps game_setup.init_settings, reads external dynamic_item_spawn.ltx and accesses named producer upvalues. Its geometric nearest graph helper sets config gm_id or drops entries when level resolution fails; a resolved guard is set before resolve, making it one-time per selected module lifecycle even when resolve returns early for missing upvalues. Missing producer/config/runtime and later wrapping order remain open. C11; [WORLD-02 nearest query](spatial-queries-relocation.md).

ENGINE1011 has an axr_main .script module-start loop and a separate dynamic_callbacks.lua namespace with five storage/update names (count corrected by CONFIG-03). The latter file's presence does not establish global aliasing or generic marker/use callback delivery. The former selected loop searches root *.script on_game_start methods; it does not prove every .lua namespace executes. Full effective aliases/startup/priority/order are retained for the next configuration/script-integration subsystem and [prior REV-01](../../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md). C12/C13.

## Package comparison and remaining inputs

Nine full-file BETA150/ZIP142 comparisons plus one normalized smart show/hide slice and the ENGINE1011/BETA150 squad comparison are recorded. Read the comparison_scope: normalized slice equality is not full-file equality. The smart file differs overall but selected show/hide blocks are equal; engine-bundled and main squad full files differ. Relevant core files, option includes, marker XML, actor/restrictor/teleport binders, smart/jobs, save wrappers and namespace startup must come from the actual winning profile. Source findings do not select a preferred variant or prescribe a patch. [Completion rule](source-completion-status.md), [central guide](development-reference.md), [bounded audit](../../08-research/verification-2026-10-12-v0.1.73.md).

## CONFIG-03 amendment — 2026-10-12

[CONFIG-03](../configuration/script-loading-startup-callbacks.md) corrects C12's six-name description to **five** (save/load/update/save_state/load_state) and establishes the selected lua_debug-enabled native global loader for this .lua file. Later _G/module assignments and actual debug/profile settings still decide the effective global route; axr_main and this dispatcher remain distinct. The original C12 CSV subject/hash is preserved as dated evidence, with this explicit correction. Generic marker/use delivery is still not proved by that small dispatcher.
