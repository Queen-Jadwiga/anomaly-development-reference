# Supplied option and patch helper contracts

> ADR document set: **v0.1.80**. Research revisions and source/build versions below describe their original scope.

- ID: CONFIG-04-API
- Subsystem: configuration/script integration
- Owners: BETA150 main ui_options/warfare_options; ENGINE1011 option/INI/patch modules
- Interface kind: Lua script helpers, method replacements and configuration directives; not new native exports
- Baselines: ENGINE1011/BETA150; qualified ZIP142/optional comparisons via [manifest](../../evidence/manifest.md)
- Source status: source-confirmed selected definitions/callers; installed helper/class/winner chain partial
- Runtime status: untested; deferred
- Native/registered inheritance: inherited INI bindings retain [CONFIG-02](ini-api.md); UI methods retain their source class receiver
- Evidence: [CONFIG-04 ledger](../../evidence/configuration/supplied-options-patches-2026-10-12.csv), B01–B14/P01–P02/E01–E12/N01
- Example status: none; source signatures only
- Last reviewed: 2026-10-12

## BETA150 main option access

Dot-call functions below have no implicit receiver. UIOptions methods use colon-call self plus the listed arguments. Lua body optional/nil handling is distinct from native C++ defaults and bindings.

| Helper and parameters | Return and side effects | Boundary |
| --- | --- | --- |
| `ui_options.get(id)` | Value or nil; initialize empty tree, read persisted typed value first; otherwise console/default branch, with default writes/save | Not a pure getter; does not use v.curr, validate every path/content; no direct opt_temp or v.curr branch. Cached undeclared values can return before definition lookup |
| `ui_options.set(id,value)` | nil; write/save config | No local option-change event, command/functor application, pending-cache update, type/bounds guarantee or consumer refresh |
| `get_opt_table(id)` | Definition table; unknown indexed path can yield `{}` | It is not a nil-on-missing safe schema-validation contract |
| `UIOptions:GetCurrentValue(path,opt,v)` | Pending non-nil → curr functor → cmd console → persisted config | Effective exec/current/console functions and table type are dependencies |
| `UIOptions:GetDefaultValue(path,opt,v)` | Literal or executed default; may write missing current value and mark Save_AXR | Preparing/defaulting a control can mutate persistence owner before accept |
| `UIOptions:GetValue(path,opt,v,flags)` | Default/preset flag path, then current/default fallback, selected track clamp | Returned/displayed clamp is not validation of every staged/stored value |
| `UIOptions:CacheValue(path,opt,value,v)` | nil; backup comparison, pending table/color/count changes | Neither persistent commit nor general bound/content validation |
| `UIOptions:Callback_Preset()` | nil; validate selected name/section and option type/precondition; bool true only for literal "true", number via tonumber; stage edits | Not atomic apply; values/keys/include roots and helper semantics must match |
| `UIOptions:On_Accept()` | nil; pairs-based writes/functors/commands, config/keybind/cfg saves, gated event, cache clear then cancel | Distinct state owners; no local transaction/protected wrapper around all effects; unknown external exec/error behavior |
| `UIOptions:On_Cancel()` / `On_Discard()` | nil; cancel handles visibility/restart/flags; discard explicitly clears pending first | Cancel alone does not clear all tables; discard body does not explicitly clear backup |

B01–B10, `ui_options.script:36–89,688–776,1091–1170,1930–1997,2096–2191,2236–2266,2353–2477`. The accept emitter calls `SendScriptCallback("on_option_change")` with **no changed-value arguments**, after save stages and before clearing tables, only if level.present and Change_Done. Event routing and successful listener application require effective [CONFIG-03 shared wrappers](script-callback-api.md). False remains a legitimate value; nil fallback, default, pending/current/persisted and console state are not interchangeable.

## Refresh and patch installation

`warfare_options.update_settings()` refreshes fields and replaces its factions table; no success return or universal propagation to retained old-table references is established. The option-change listener is registered in warfare_options.on_game_start, while the separate warfare.on_game_start performs the initial refresh and other subscriptions. The module-level check_online_status replacement is distinct from the optional override_functions installer, for which no direct call was found in the supplied-package .script search. B11–B13; [canonical Warfare controls](../../04-game-systems/warfare/policy-controls.md).

| ENGINE1011 helper | Selected contract |
| --- | --- |
| `ui_options_modded_exes.on_xml_read()` | Installation handler replaces init_opt_base through mutable namespace slot ui_options_base, then initializes. Repeating in same module instance can capture its prior wrapper and cause self-reference; it is not a per-option-change or every-XML-text handler |
| `options_builder.check(args)` / `track(args)` | Mutate/return args, set type/value metadata; selected track console bounds delegated and reversed range swapped; not full persisted/current-value validation |
| `options_builder.page(args)` | Remove first header, attach remaining list/prepend slide; `head.sh or true` turns false into true; mutates input |
| `options_builder.import_into(dest)` | Requires existing metatable; builder-first __index replacement, then prior function/table fallback. Effective environment/later wrapper order matters |
| Existing `_G.ini_file_ex:r_value(s,k,type,default)` | One-time clear of instance cache, then underlying INI; bool-null false versus default for other types; definition affects existing class before later alias replacement |
| Existing `_G.ini_file_ex:w_value(s,k,value,comment)` | Delegate through self.ini:w_string with stringified value/comment; native arity/existing-key checks remain |
| `_G.SYS_GetParam(type,section,key,default)` | Dispatch selected type helper; bool branch does not forward default to ini_sys:r_bool_ex; missing type/section/key reports/callstack |
| `dynamic_items_by_level.on_game_start()` | Reassign local original slot and install wrapper; wrapper calls original slot before once-resolution guard. Same-instance repeat can self-reference; original returns not forwarded |

E01–E10/N01; [consumer reference](../../04-game-systems/configuration/supplied-options-patches.md). Lua argument tables and module fields are live references; no immutable schema or once-install/remove protocol follows. _g_patches cache disabling does not invalidate native filename cache or refresh every constructed INI/consumer. New class aliasing does not make an earlier instance a new class instance. Captured original functions can remain stale or accumulate wrapper layers; binder startup capture and trade module-evaluation capture have separate phases (E11/E12).

## Persistence, failure and checks

INI files, console config, menu pending/backup tables, copied Warfare fields, module closures and saved campaign tables have different owners. Available-source write/default intents do not prove successful new-key insertion through the native-derived writer or all installed effects. CONFIG-02 native ownership/cache/save and CONFIG-03 identity/error/reset contracts remain authoritative. No MCM ABI, all-option schema, reversible transaction or installed compatibility is introduced here.

Check pinned definitions/callers and raw hash/count/range/symbol integrity; reproduce package comparisons with explicit raw-file versus normalized-slice scope. Methods matching across optional variants do not make declarations/dependencies/winners identical. No runtime test ran. [Completion status](../../04-game-systems/configuration/source-completion-status.md), [audit](../../08-research/verification-2026-10-12-v0.1.77.md).
