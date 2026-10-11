# Script interfaces and effective-source boundary

[Catalog conventions](README.md). [Function declaration CSV](script-interfaces-oct11.csv) retains source IDs, paths, lines, parameters and colon/explicit receiver forms. It includes the four selected engine scripts (`sim_squad_scripted`, `bind_monster`, `callbacks_gameobject`, `aaaa_script_fixes_mp`) and all `.script` files found in the supplied BETA150 main/patch folders. It does not silently merge implementations from those variants.

## Core interface map

| Script class/module | Representative methods | Implementation status |
| --- | --- | --- |
| `sim_squad_scripted` | `update`, `specific_update`, `generic_update`, `assign_smart`, `assign_squad_member_to_smart`, `add_squad_member`, `remove_npc`, `on_npc_death`, `STATE_Read/Write`, `check_online_status`, `get_current_task` | Bundled and Warfare variants available; active winner/replacements unknown |
| `sim_squad_warfare` | `set_target`, squad update/registration and removal helpers | Supplied Warfare implementation traced; installation unknown |
| `smart_terrain_warfare` | Smart update, owner selection, autocapture and spawning helpers | Supplied package source available; base smart methods unresolved |
| `warfare` | Startup, strategic tables, save/load and callback listeners | Supplied source available; full effective callback order unresolved |
| `sim_offline_combat` | Coordinator, target validation, battle/death bookkeeping | Supplied source traced; creature overrides/release completion unresolved |
| `warfare_options` | Status replacement, settings update, optional override installation function | Declaration/assignment does not prove module/startup caller order |
| `bind_monster` / generic binder | `net_spawn`, `net_destroy`, save/load and scheme integration | Supplied binder available; effective winning binder unknown |
| `callbacks_gameobject` | Generic spawn/destroy forwarding and registry listeners | Supplied wrapper available; other listeners/replacements unknown |
| `aaaa_script_fixes_mp` | Startup patch installation and teardown/bookmark wrapper helpers | Supplied patch available; execution and later replacements unknown |

The bundled squad declaration derives `sim_squad_scripted` from `cse_alife_online_offline_group` (`gamedata/scripts/sim_squad_scripted.script:33–34`). A script method with the same name as an exported native virtual can participate in native dispatch; arbitrary Lua helper methods do not become C++ callbacks just because they exist on the same object.

## Missing implementations and known call boundaries

| Missing effective module | Calls/state requiring closure |
| --- | --- |
| `sim_board` | Squad assignment/unassignment, smart squad registry and member setup |
| `smart_terrain` | Registration/jobs, `on_reach_target`, `am_i_reached`, task selection and after-reach behavior |
| `simulation_objects` | Target identity/availability, registration and same-level policy |
| `se_stalker`, `se_monster` | Script creature death overrides and path into squad casualty notification |
| `safe_release_manager` | Queued release timing, cancellation and cleanup |
| `_g` / `_G`, storage and other startup wrappers | Effective callback dispatch, serialization and monkey-patch order |

These names come from calls/references in the inspected sources and earlier investigations. They are not invented class declarations or inferred signatures. Missing implementations are deliberately absent from the definition CSV. Supplied calls can still be mapped; the complete contracts require winning source files and relevant configurations.

## Selected script contracts already established

- `assign_smart(smart, old_smart_id)` and native `register_member(id)` operate at different layers: smart/job bookkeeping versus squad membership.
- Warfare `set_target` can invoke the smart's reach hook during targeting; that call alone does not prove arrival.
- `on_npc_death(se_npc, se_killer)` sends the supplied squad death callback before member removal. The offline-combat call into the missing creature override is still an unresolved edge.
- `check_online_status` populates policy state consumed through permission overrides. Supplied module-level replacements can change that producer.
- Native `STATE_*` hooks, script `save_state/load_state`, Warfare callback persistence and CtZ campaign records are different mechanisms; arbitrary fields are not automatically persistent.

Evidence and exact behavioral boundaries: [WAR-002b](../../warfare/warfare-policy-offline-combat-oct11.md), [ALIFE-04](../save-load-identity-oct11.md), [ALIFE-07](../client-server-offline-teardown-oct11.md), [ALIFE-08](../switching-eligibility-oct11.md).

This declaration catalog does not establish every function's side effects, event subscriptions or current winning implementation. Next consolidation can connect these interfaces into lifecycle/state and callback-phase maps, leaving the missing edges explicit until effective sources are available.
