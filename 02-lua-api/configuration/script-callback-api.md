# Script lookup, prefetch and shared callback contracts

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

- ID: CONFIG-03-API
- Subsystem: configuration/script integration
- Owners: native CScriptEngine/CScriptStorage; Lua axr_main; separately assigned global wrappers
- Interface kind: one selected native Lua export, native-only lookup/loading methods, bundled Lua helpers
- Native versus registered inheritance: storage/engine internals are not a newly registered Lua engine class
- Baseline: ENGINE1011 uploaded archive via [manifest](../../evidence/manifest.md); upstream commit/executable correspondence unknown
- Source status: source-confirmed selected definitions/registration/callers; final installed global route partial
- Runtime status: untested; deferred
- Build/conditional scope: game/debugger/common-script guards, `lua_debug`, `-keep_lua` and `-_g` branches retained
- Evidence: [CONFIG-03 ledger](../../evidence/configuration/script-loading-callbacks-2026-10-12.csv), N01–N22/S01–S13
- Example status: none; signatures are source forms, not tested startup/dispatch recipes
- Last reviewed: 2026-10-12

## Native loading and lookup

| Interface | Signature / result | Contract |
| --- | --- | --- |
| Lua `prefetch` | `prefetch(LPCSTR module)` → void | One registered argument; appends .script through ordinary process_file; no success return, .lua fallback or Lua reload flag |
| Native-only process_file | `void process_file(LPCSTR)`; `void process_file(LPCSTR,bool reload)` | Namespace-table short-circuit unless reload; underlying load bool not propagated by these wrappers |
| Native-only process_file_if_exists | `(LPCSTR,bool warn_if_not_exist)` → void | Quiet path remembers one missing name; warning-enabled route bypasses that shortcut |
| Native-only namespace_loaded | `(LPCSTR,bool remove_from_stack)` → bool | Raw dotted-table existence, fatal non-table collision; not a module completion flag |
| Native-only function_object | `(LPCSTR qualified_name,luabind::object&,int type)` → bool | Empty name false; split last dot, request first root module for qualified namespace, check exact declared member type |
| Native-only functor template | `(LPCSTR,luabind::functor<Result>&)` → bool | Resolve function object then cast; call arguments/returns belong to its particular native caller, not this resolver |
| Native-only unload | `void unload()` | Stack-level restoration and last-miss clearing; not VM/namespace destruction |

N06–N12/N15/N16/N18, `script_engine.cpp:172–177,340–365,483–590,614–626`, `script_engine_inline.h:26–57`, `script_storage.cpp:681–787,1054–1177`, `script_engine_script.cpp:122–125,232–239`. Do not promote native signatures into additional Lua exports or constructor-style optional arguments. The existing [INI converter scope](ini-api.md) retains string-input limits; arbitrary module names, malformed dotted paths and all outer error handling remain qualified.

Named modules evaluate with the selected injected environment header; ordinary header falls back to _G, alternate -_g header only exposes explicit _G. Global autoload may execute a missing module during a table read. Existing namespace tables and partial top-level side effects can outlive a failed load; forcing reload can create new function identities without removing old registered closures. VM reconstruction invalidates old Lua-state objects rather than supplying a durable module handle. N01–N05/N08/N12–N15; [behavior and lifecycle](../../04-game-systems/configuration/script-loading-startup-callbacks.md).

## axr_main helpers

These are Lua module functions with dot-call parameters; they have no implicit module receiver. Optional parameters are implemented by Lua body logic, independently of native binding arity. They return nil on ordinary completion, including paths that log and return; no boolean registration receipt exists.

| Helper | Parameters | Selected behavior |
| --- | --- | --- |
| `callback_add` | `(name)` | Add event table plus metadata; existing name logs/callstack without replacement |
| `callback_set` | `(name,listener,before_funcs,after_funcs,priority)` | False/nil listener or absent event logs/returns. Dependencies default to empty; tier defaults NORMAL when false/nil. Invalid list/tier asserts; graph rejection restores recorded registration fields |
| `callback_unset` | `(name,listener)` | Remove exact identity and own metadata; scrub that target from others only for userdata; report missing event/reorder failure. No general uninstall or symmetric rollback transaction |
| `make_callback` | `(name,...)` | Function listener gets args; otherwise truthy `listener[name]` is invoked with self then args. Returns discarded, shared tables aliased, no per-listener protected call or reentry guard |
| `on_game_start` | `()` | Root nonempty *.script discovery with ignore list, autoload during collection, second-pass direct handlers; no local once-only/readiness guard |

S01–S08/S13, `axr_main.script:14–53,205–222,241–664`. Intended listener identities are functions/userdata, but callback_set does not fully validate every truthy listener type or callable method. A successful key insertion is not proof that dispatch can invoke it safely. Invalid native object lifetime is not repaired by callback registration.

Before/after accept a function/userdata or table containing such values and are privately copied. Constraints identify **exact values**, not names or equivalent new closures. Forward function references can become active later. Re-registering preserves registration fallback position; unsetting and later registering can allocate a new position. Hard PRE/NORMAL/POST ordering precedes same-tier stable topological selection; contradictory cross-tier, self and cycle relations are rejected. Registration-state rollback does not undo consumer/game state. Other rules can retain unregistered function closures; userdata scrubbing has a different lifetime purpose. S02–S06.

## Global assignments and iterator limits

| Available wrapper definition | Mapping / return |
| --- | --- |
| `RegisterScriptCallback(name,listener,...)` in _g_patches | Calls callback_set with forwarded values; does not return its result |
| `RegisterScriptCallbackPre(name,listener,before,after,...)` | Inserts CALLBACKS_PRE=0 as fifth callback_set argument; further arguments have no parameter in that selected callee |
| `RegisterScriptCallbackPost(name,listener,before,after,...)` | Same, CALLBACKS_POST=2; CALLBACKS_NORMAL=1 |

S09, `_g_patches.script:426–439`. The selected global SendScriptCallback and UnregisterScriptCallback routes to axr_main still require missing effective core population; their names cannot be assumed aliases of make_callback/callback_unset. Startup/comment names and the small debug dispatcher do not supply that missing edge.

With the available _g_patches comparator/helper, make_callback uses a heap iterator that snapshots keys and reads live values/priorities. New outer-dispatch keys are excluded; removed nil keys are skipped; reprioritization does not certify a frozen or rebuilt total order for remaining listeners. Recursive dispatch builds another iterator from current state and can invoke the same listeners again. A different installed spairs can change these semantics. S07/S10, `_g_patches.script:413–415,769–793,814–887,1074–1081`.

## Separate debug-global functions

When enabled during storage reinit, LoadKernelScriptToGlobal loads dynamic_callbacks.lua without a namespace header. That file declares **five** events: save/load/update/save_state/load_state. Its global `RegisterScriptCallback(name,listener)` inserts a true-valued identity; Unregister removes it; Send iterates pairs, invokes function or named self-method and discards returns. Unknown event names are not inserted by registration. Its nil listener path calls external callstack and does not establish a safe registration guarantee. There are no priority/dependency parameters, stable order or per-listener protected-call/reentry contract in this file. N04/N17/N22/S11.

These debug definitions can be overwritten by later _G/modules. Setting the console lua_debug flag alone does not run the reinit body. Neither dispatcher can be generalized to every installed profile; September/October differences remain [separately pinned](../../04-game-systems/alife/callback-phase-reference.md#build-boundary--september-versus-october-dispatcher). Earlier six-event wording is amended by CONFIG-03, while historical ledgers stay byte-identical.

## State, checks and effective gaps

Registries/order/constraints and module environments are live Lua-state data; selected bodies do not serialize arbitrary listeners or certify restored handles. Native callback phases, shared table dispatch, global wrapper population and object-bound slots remain distinct. The evidence checks hash/count/range/symbol integrity and selected source branches; no API here is runtime-verified. Winning _G/script.ltx/binder/emitter/storage sources, later replacements, helper identity and debug/build settings remain open. [Completion rule](../../04-game-systems/configuration/source-completion-status.md), [investigation](../../08-research/investigations/2026-10-12-CONFIG-03-script-loading-startup-callbacks.md).
