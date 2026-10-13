# Lua INI construction, reads, writes and DLTX metadata

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

- ID: CONFIG-02-API
- Subsystem: configuration/script integration
- C++ owner: `CScriptIniFile : CInifile`; Lua class: `ini_file`
- Interface kind: Lua exports and separately identified bundled script helpers
- Registered inheritance: `class_<CScriptIniFile>("ini_file")` does not register a separate Lua `CInifile` base
- Baseline: ENGINE1011 uploaded archive; [provenance](../../00-environment/source-baseline-2026-10-11.md)
- Source status: source-confirmed selected registrations/definitions/converters
- Runtime status: untested; deferred
- Build scope: extended methods guarded by `INI_FILE_EXTENDED_EXPORTS`; `game_ini` by `XRGAME_EXPORTS`; snapshot feature definition present, installed build unknown
- Evidence: [CONFIG-02 ledger](../../evidence/configuration/ltx-ini-dltx-2026-10-12.csv), A01–A20/S01–S02 and N01–N28
- Example status: none; call forms below are source signatures, not tested recipes
- Last reviewed: 2026-10-12

## Construction and ownership

Signatures omit an ordinary method's receiver. `LPCSTR` arguments use the selected string converter; C++ null guards/defaults do not create omitted Lua arguments or prove nil input acceptance. `BOOL` here is **int**, not C++ bool: the five-argument constructor's three flags use the integer converter, which matches number/nil and converts nil to 0, rather than matching Lua booleans. Bounds, finite values and arbitrary numeric casts are not certified. A01/A02/A10–A12/A14/A18, `script_ini_file.h:18–76`, `script_ini_file_script.cpp:165–235`, `_types.h:23–29`, Luabind `policy.hpp:285–323,553–556`.

| Lua form / exact registered parameters | Return and owner | Behavior and lifetime boundary |
| --- | --- | --- |
| `ini_file(LPCSTR filename)` | Owned `CScriptIniFile` userdata | Resolves through `$game_config$`; native defaults read-only/load/save-at-end=true |
| `ini_file(LPCSTR filename, BOOL readonly, BOOL load, BOOL save_at_end, LPCSTR path)` — extended | Owned userdata | **Five arguments**, no registered 2/3/4-argument filename constructors. When non-null, fifth `path` is selected as the **filename**, bypassing resolution of the first argument; it is not the reader constructor's include directory |
| `ini_file(IReader* reader, LPCSTR path)` — extended | Owned userdata | **Two arguments**; native reader mode read-only=true/save-at-end=false and path used for includes. Reader provenance/exposure is not a new recommended Lua recipe |
| `create_ini_file(LPCSTR text)` | Newly allocated `CInifile` cast to script interface, `adopt<result>()` owns result | Synchronous reader over supplied text, config directory for includes, empty stored filename; no automatic named-root mod discovery/cache |
| `system_ini()` | Borrowed `pSettings` cast to script interface; no adoption | Owner is engine settings lifecycle, not Lua GC |
| `game_ini()` — game build | Borrowed `pGameIni` | Separate root/lifetime from system settings |
| `reload_system_ini()` — extended | New borrowed system pointer | Deletes old system object, invalidates all named cache, constructs system.ltx; does not refresh all aliases/copied fields/game/auth roots |
| `ini:close()` | void | Deletes native `this`; no ownership removal, wrapper invalidation or global-root repair in this method |

A02/A05/A07/A10/A12–A15; native settings roots N01/N02. Default pointer conversion creates a non-owning userdata when there is no back-reference; adopted factory/constructor paths install owning deletion. Owned finalization invokes its destructor. Explicit `close` can therefore leave aliases and an owning userdata referencing deleted memory. Borrowed global deletion can also leave the engine's stored pointer stale. No universal safe manual-close protocol is established; lifecycle and Lua alias safety must be resolved before using deletion/reload. [Parser/lifetime reference](../../04-game-systems/configuration/ltx-ini-dltx.md).

## Selected reads and iteration

All class calls below have the receiver plus their listed parameters. Native section lookup can lowercase on `r_section`; `section_exist` is exact, and the wrappers' prechecks retain that difference. Existing empty values are not missing keys. Null strings become Lua nil, while copied non-null strings become Lua strings through the pinned converter/LuaJIT path. A03/A12/A17/A19/A20; N23.

| Registered name and parameters | Result / failure behavior |
| --- | --- |
| `section_exist(LPCSTR section)`, `line_exist(LPCSTR section,LPCSTR key)` | bool existence; no numeric/string coercion or null-input safety inferred beyond converter/implementation |
| `line_count(LPCSTR section)` | u32; wrapper asserts section exists |
| `r_string(LPCSTR section,LPCSTR key)` | string or nil for existing null value; wrapper asserts section/key existence; keeps quotes |
| `r_string_wq(LPCSTR section,LPCSTR key)` | Maps to `r_string_wb`; strips leading/trailing double quote independently; no wrapper missing-key precheck in that method, inherited read can fail |
| `r_u32`, `r_s32`, `r_float` with section/key | u32/int/float; existence assertions, then `atoi`/`atof`; no strict parse/range/finite validation established |
| `r_bool(LPCSTR section,LPCSTR key)` | bool via native string read, lowercase and true-token set; does not add the numeric wrappers' same explicit prechecks |
| `r_vector(LPCSTR section,LPCSTR key)` | Copied Fvector; existence assertions, zero-initialized components then unchecked-count sscanf |
| `r_vector4(LPCSTR section,LPCSTR key)` | Copied Fvector4; missing section/key returns zero vector with log; valid read uses native component parsing |
| `r_line(LPCSTR section,int index,internal_string& name,internal_string& value)` | **Four explicit inputs**, commonly two empty-string placeholders; returns bool plus converted name/value via `out_value<4>() + out_value<5>()` including receiver. Missing section/high index assert; negative index passes upper precheck but native returns false. Null value becomes empty output string |
| `section_count()` — extended | u32 number of sections |
| `section_for_each(functor<bool>(section_name))` — extended | void; snapshot initial names, skip names removed before visit, stop when listener returns true. No local listener pcall; new names not added to that snapshot; deleting/reloading the INI itself is not made safe |

A03/A08–A10/A16; N23–N25. Final sections and scalar items are name-sorted, so an ordinal is not source-line insertion order. `r_line` is an in-out policy, not a pure-output registration with two explicit inputs. Native-only unexported read widths or C++ defaults must not be added as Lua APIs. `r_clsid(section,key)` and `r_token(section,key,CScriptTokenList const&)` are additionally registered; mapping requires the class factory/token-list contract, and unmatched native token return 0 is not unambiguous absence. Arbitrary empty token-list safety is outside this selected pass.

## Mutation and output

Extended writes are registered with **four explicit inputs** `(section,key,value,comment)`; the declaration comments `/* = 0 */` are not Lua default/overload registrations. Selected `w_string`, `w_float`, `w_bool` and analogous width/vector/color wrappers assert existing section/key, then invoke inherited writes. The extended set includes w_color/w_fcolor/w_fvector2/3/4/w_s8/16/32/64/w_u8/16/32/64; registration does not add unregistered native methods. The C++ value type governs its converter; exhaustive large-number/vector/color conversion remains outside this focused scalar/ownership audit. A01/A04/A10.

| Method | Selected contract |
| --- | --- |
| `set_readonly(bool)`, `set_override_names(bool)`, `save_at_end(bool)` | void flag setters. Existing duplicate write needs writable and override-enabled state; flags do not remove wrapper existence checks or reparse DLTX |
| `remove_line(section,key)` | void; wrapper asserts existence, inherited writable check; missing-line no-op from native-only method is not this Lua wrapper's contract |
| `remove_section(section)` | bool; empty name/read-only logs false, inherited parses/lowercases name and removes if present |
| `save_as(LPCSTR filename)` | bool; **one explicit string argument**, wrapper rejects null; empty string requests use of existing filename in native body, which still must be nonempty. Open failure can leave changed stored filename; successful write serializes resolved plain DATA and invalidates that named cache |
| `get_filename()` | stored filename string, potentially empty for reader-created objects; does not identify every include/mod contributor |

A04/A05/A10 and N03/N22/N26. Mutating INI data is separate from game save state and fields already copied by consumers. `save_as` is not a source-preserving DLTX/include serializer or a certified atomic write. Destructor autosave requires writable plus save-at-end flags; GC timing is not a controlled persistence phase.

## DLTX inspection and bundled defaults

`dltx_print(section,line)` has two explicit string parameters in the registration; native null guards do not establish no-argument or nil-input Lua overloads. `dltx_get_filename_of_line(section,line)` returns surviving item's basename or nil; `dltx_is_override(section,line)` returns whether that basename starts with `mod_`. `dltx_get_section(section)` returns a copied name-keyed table whose entries contain name/value/filename; missing section returns an empty table, null values can omit value. These are final-state diagnostics with metadata limits, not a complete override or MO2 provenance history. N21/A06/A10/A12/A17/A19/A20.

The available `_g_patches.script` assigns definition-level helpers:

| Helper | Default/type behavior from the selected body |
| --- | --- |
| `r_string_ex(section,key,default)` | Existence/read via Lua and/or; null value falls back to default |
| `r_float_ex(section,key,default)` | Missing/null or failed tonumber returns default; not raw atof behavior |
| `r_bool_ex(section,key,default)` | Missing/null returns default; existing string compares exact lowercase true tokens, without native lowercasing |
| `r_sec_ex(section,key,default)` | Reads result then validates against external ini_sys, returns nil if invalid |
| `r_line_ex(section,index)` | Calls native in-out r_line with two empty-string placeholders |
| Replacement `ini_file_ex` advanced mode | One-argument base constructor then writable/override=true/save-at-end=false; `save()` explicitly calls save_as on constructed config path |
| Replacement `r_value(section,key,type,default)` | Missing returns default; null for bool type 1 returns false, other types default. Type 2 uses tonumber; type 1 exact true tokens |
| Replacement `w_value(section,key,value,comment)` | Converts values/comment to strings and calls four-input w_string; does not bypass existing-key requirement |

S01/S02, `_g_patches.script:459–491,575–623,671`. In particular inherited `ini_file.r_bool_ex` and replacement `ini_file_ex:r_bool_ex` have different empty-value behavior. Assignment existence does not certify actual startup/global installation or final winning helper. CONFIG-03/04 trace those phases and further option/preset/cache consumers.

## Checks and open boundaries

Definitions, registrations, feature guards, string/integer/pointer/adopt/in-out converters and finalizer paths are read and pinned; ledger integrity checks reproduce their raw hashes/ranges/symbols. Preserve every receiver and registered overload. Selected scalar return/case/default behavior and ownership are established only for these source paths; assertion/exception behavior across all outer handlers, arbitrary malformed configs, reader lifetime, installed aliases/winners and executable flags remain qualified. Runtime remains deferred. [Completion rule](../../04-game-systems/configuration/source-completion-status.md), [investigation](../../08-research/investigations/2026-10-12-CONFIG-02-ltx-ini-dltx.md).
