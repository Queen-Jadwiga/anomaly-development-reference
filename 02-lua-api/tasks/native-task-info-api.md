# Native task and info Lua contracts

> ADR document set: **v0.1.70**. Research revisions and source/build versions below describe their original scope.

- ID: TASK-01-API
- Subsystem: tasks/dialogue/info state
- C++/Lua owner: CScriptGameObject / game_object; CGameTask
- Interface kind: selected native methods/class exports
- Baseline/provenance: ENGINE1011; [manifest](../../evidence/manifest.md)
- Source status: source-confirmed selected declarations/registration/bodies
- Runtime status: untested; deferred
- Converter/lifetime policy: u32/bool/string/task pointer conversions not exhaustively audited; task adoption and registry lifetime matter
- Example status: none; no tested reward/task recipe
- Last reviewed: 2026-10-12

[Ledger T05–T08](../../evidence/tasks/native-task-dialogue-info-2026-10-12.csv), [reference](../../04-game-systems/tasks/native-task-dialogue-info.md).

| Lua method | Native signature excluding receiver | Return / mutation |
| --- | --- | --- |
| give_task | void GiveTaskToActor(CGameTask*, u32 dt, bool bCheckExisting, u32 timer) | Global actor-task manager; registered adopt<2> for task argument; manager return discarded |
| set_task_state | void SetGameTaskState(ETaskState, LPCSTR task_id) | Global manager ID path, in-progress lookup; no receiver-specific task registry |
| get_task | CGameTask* GetTask(LPCSTR id, bool only_inprocess) | Manager lookup; null when not found, no new task ownership |
| give_info_portion | bool GiveInfoPortion(LPCSTR) | Failed inventory-owner cast false; otherwise transfer event plus local mutation, return true even duplicate |
| disable_info_portion | bool DisableInfoPortion(LPCSTR) | Failed cast false; otherwise forwards and true even absent ID |
| has_info / dont_has_info | bool query(LPCSTR) | Failed owner cast false/true respectively; valid owner requires nonempty ID |

The grant manager dereferences the supplied task without a local null guard; a valid initialized task is required. No Lua default-argument contract is inferred from C++ declarations. Task wrappers do not promise safe caller ownership/reuse after adoption or duplicate grant rejection. Task ID/type/title/priority/map setters and info/function list adders are separately registered on CGameTask; helper functor names are committed by grant/load, not automatically a retained prior closure. See T01–T05/T18 and the reference for active/read state, repeated terminal effects and save-list omissions.

Dialogue helper interfaces have one/two-speaker and DIALOG_UPGRADE variants. Their caller-specific argument order and actor-global info policy are documented in the reference; no universal precondition/action signature or script reward return convention is supplied here.
