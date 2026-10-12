# Native persistence extension contracts

> ADR document set: **v0.1.76**. Research revisions and source/build versions below describe their original scope.

- ID: PER-01-API
- Subsystem: persistence
- Owners: native `CALifeStorageManager`, `CScriptBinder` and `CScriptBinderObjectWrapper`; named Lua `alife_storage_manager` functors / `object_binder` virtual methods
- Interface kind: native-to-Lua hooks and virtual binder overrides; not an exhaustive persistence API
- Baseline: ENGINE1011; [provenance](../../00-environment/source-baseline-2026-10-11.md)
- Source status: source-confirmed within selected bodies/registrations
- Runtime status: untested; deferred until explicitly resumed by the user
- Build/conditional scope: named hooks under `ENGINE_LUA_ALIFE_STORAGE_MANAGER_CALLBACKS`, enabled in supplied define file; actual executable unknown
- Native versus registered Lua inheritance: selected `object_binder` virtual forwarding only; no exhaustive converter/inheritance projection
- Example status: none
- Last reviewed: 2026-10-11

S-labels refer to the [PER-01 ledger](../../evidence/persistence/native-pipeline-2026-10-11.csv). [Pipeline reference](../../04-game-systems/persistence/native-save-load-pipeline.md) provides ownership, framing and phase context.

## Named storage hooks

| Named Lua functor | Native lookup/call contract | Phase / argument |
| --- | --- | --- |
| `alife_storage_manager.CALifeStorageManager_before_save` | Optional `luabind::functor<void>`; called if lookup succeeds | Before native serializers; receives current `m_save_name`, including selected `.scop` extension |
| `alife_storage_manager.CALifeStorageManager_save` | Same optional void functor | After native writer closes; receives same selected save name |
| `alife_storage_manager.CALifeStorageManager_load` | Same optional void functor | Before buffer reconstruction; receives resolved `file_name` from filename-load path |

S01/S20. These are engine emissions with one string argument, not a shared-script callback ordering contract. A module/function name matching a missing installed script does not prove a listener is loaded. Save versus load arguments are not automatically the same bare-name/path convention. Hook return type is not a success acknowledgement or atomic companion-file commit. Installed functor errors/converters and effective dispatch remain unaudited.

## Binder persistence methods

| Lua virtual name | Exact native wrapper signature | Selected forwarding/default |
| --- | --- | --- |
| `save` | `void save(NET_Packet* output_packet)` | `call_member<void>(this,"save",output_packet)`; base default empty |
| `load` | `void load(IReader* input_packet)` | `call_member<void>(this,"load",input_packet)`; base default empty |
| `net_save_relevant` | `bool net_SaveRelevant()` | `call_member<bool>(this,"net_save_relevant")`; base default false |

Registered through `object_binder` with static base fallbacks. S17–S19. The actual packet/reader conversion and every inherited entity relevance override are outside this pass. The selected client save enumeration filters non-destroying game objects and queries virtual relevance; there is no universal promise that every binder is enumerated. S07/S15/S16.

Packet/reader pointers refer to the currently executing serialization operation. No ownership transfer, durable pointer lifetime, automatic arbitrary-table serialization or safe retention outside the call is established. The writer/reader positions and field/schema order must agree with the effective implementation; this reference does not invent a Lua storage format.

`CScriptBinder` invokes bound methods only when a binder exists and catches exceptions by clearing it; relevance fallback is false. These bodies can leave native processing continuing without proving that an addon completed its schema. S16. Object save writes native then binder data; object load consumes native then binder data during base spawn after reload/reinit and when retained custom bytes are nonempty. Later virtual/outer spawn work and other objects can still be pending. S15; [callback phases](../../04-game-systems/alife/callback-phase-reference.md).

## Missing effective contracts and checks

Installed `alife_storage_manager`, storage/save_var/load_var wrappers, binders, schemas, companion files, marshal policy and shared load/save listener order require the next source investigation. Native hooks are not a substitute for those implementations. CtZ campaign identity/migration and object-ID reconciliation are separate follow-ups.

Compared hook lookup/call arguments, wrapper signatures/registrations, default methods, relevance and exception phase. Verified pinned hashes, counts, ranges and symbols. No gameplay examples, runtime verification, engine build or save mutation. [PER-01](../../08-research/investigations/2026-10-11-PER-01-native-save-load.md), [verification](../../08-research/verification-2026-10-11-v0.1.50.md).
