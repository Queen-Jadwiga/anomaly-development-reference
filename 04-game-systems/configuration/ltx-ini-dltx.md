# LTX/INI loading and selected DLTX contracts

> ADR document set: **v0.1.79**. Research revisions and source/build versions below describe their original scope.

- ID: CONFIG-02
- Subsystem: configuration/script integration
- Research revision: v0.1.75
- Record status: complete-within-scope for selected native/parser/Lua contracts; effective integration partial
- Source status: source-confirmed within selected ENGINE1011 paths
- Runtime status: untested; deferred
- Baseline: ENGINE1011 uploaded archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit/executable equivalence unknown
- Last reviewed: 2026-10-12

[50-row ledger](../../evidence/configuration/ltx-ini-dltx-2026-10-12.csv) N01–N28/A01–A20/S01–S02 pins paths, raw hashes and inclusive ranges. IDs below belong only to that ledger. [Lua contracts](../../02-lua-api/configuration/ini-api.md), [investigation](../../08-research/investigations/2026-10-12-CONFIG-02-ltx-ini-dltx.md), [verification](../../08-research/verification-2026-10-12-v0.1.75.md).

## Settings roots, file construction and cache

`InitSettings` resolves `$game_config$/system.ltx` into read-only `pSettings`, constructs a separate `pSettingsAuth` using an include predicate, and resolves `game.ltx` into read-only `pGameIni`. The system/game roots must have nonzero section counts there; the time-factor global is separately initialized from system settings. Engine settings teardown deletes all three. This is their selected construction/lifetime chain, not the installed effective files or an automatic consumer-refresh contract. N01, `src/xrEngine/x_ray.cpp:198–231,287–294`.

A filename constructor stores its filename/flags, optionally checks the named-file cache, then opens/parses when a reader exists. Failure to open leaves empty data in this body; it does not itself establish the startup root's nonempty check or safe typed-read defaults. A reader constructor has an empty filename, read-only=true, save-at-end=false and override-names=false. The filename constructor's native defaults are read-only/load/save-at-end=true; its zeroed override flag remains false. Destruction saves only when writable and save-at-end is set. N02/N03, `Xr_ini.cpp:148–245`, `xr_ini.h:101–121`.

The enabled-by-default cache keys the **lowercased stored filename**, copies resolved section/item vectors into new instances, and skips parsing on a hit. Eligibility tests only a nonempty filename. The key does not include read-only mode, include predicate, input content or mod-list identity; a hit therefore does not reapply an include filter. This is a cache-key limitation, not an assessment of installed authentication. Reader/string-created objects have no filename for automatic root mod discovery or named cache participation. Cache invalidation erases one lowercased filename or all entries; the selected cache-disable console path invalidates all. Saving successfully opens a writer before invalidating the object's current filename. Mutation alone does not invalidate this cache or reread other existing objects. N02–N04/N20/N22/N27, `Xr_ini.cpp:109–245,1294–1417,1501–1561`; `xr_ini.h:171–174`; `console_commands.cpp:2475–2492,3273–3276`.

## Parse and include boundaries

The selected parser trims lines, detects `;` and an initial `//` candidate with its local quote test, and removes value whitespace outside double quotes through `_parse`. Quoted values keep quotes/inside whitespace; an unmatched quote enters a multiline accumulation loop with size assertions. This is the inspected implementation, not a general escaped-string grammar or guaranteed recovery for arbitrary malformed input. A key without `=` or with an empty right-hand side stores a null value; existence and a non-null string value differ. N05/N13/N16, `Xr_ini.cpp:38–68,618–716,811–880`.

Includes resolve against the current parse directory and call `loadFile` with **depth+1**. The `*.ltx` branch enumerates a file set; a permitted include must open or assert. Non-editor builds can veto a load through `allow_include_func`. The selected include recursion has no local include-cycle guard; inheritance cycle detection later is a separate mechanism. Root/mod automatic discovery belongs to a named outer load, not every recursively included file. XML resource remapping and DXML interception retain their separate [UI rules](../../03-ui-pda/xml-loading-paths-ui04a-oct11.md). N06/N09/N13, `Xr_ini.cpp:327–360,523–615,618–716`.

## Root mods, section forms and scalar precedence

At named-root EOF, `LTXLoad` enumerates `<root-basename>_*.ltx` ambiguity candidates and `mod_<root-basename>_*.ltx` mods in the root directory. A regex check excludes mods matching an alternative ambiguous root name. Enumeration uses an ordered `FS_FileSet` comparing names; loaded mod depths start at **−200**, then decrease by **200** per loaded mod. Includes increment that assigned depth. The call requests `FS_ListFiles` without `FS_RootOnly`; do not silently describe it as a root-only listing. This establishes native indexed-file enumeration and parse ordering, not MO2 supplying-mod priority or a same-filename conflict winner. N09–N13, `Xr_ini.cpp:523–716`, `LocatorAPI.cpp:997–1068`, `LocatorAPI_defs.h:6–13,56–78`, `_stl_extensions.h:332–337,404–405`.

| Form or collision | Selected contract | Limit |
| --- | --- | --- |
| `[section]` | Ordinary base section, name lowercased | Another ordinary definition of the same section is fatal, even in a different included/mod file |
| `![section]` | Accumulate override data for that name | A standalone unresolved override does not ordinarily create a final section; warnings depend on the warning flag |
| `@[section]` | Override plus mark absent base for empty-section creation | This is conditional creation in this parser, not a runtime object/default-schema guarantee |
| `!![section]` | Mark section for removal after evaluation | Does not retroactively undo values already inherited by another evaluated section |
| `!key` / `!key = ...` | Store the internal deletion marker for that key | Deletion behavior depends on the merge stage; not equivalent to assigning an empty value |
| Repeated ordinary scalar key within base or override data | Sort by key, **lower depth first**, then **higher insertion index first**; keep first per key | Includes and file order both matter; “last textual line always wins” is too broad |

N07–N08/N14/N16/N17/N20, `Xr_ini.cpp:362–453,718–903,905–998,1294–1417`. Depth resolves collisions within each base/override collection; the subsequent merge explicitly favors override data over base data. Filename metadata is a lowercased trimmed basename attached to items, not a full supplying-mod provenance chain.

## Inheritance and list edits

The `]:` parser records parent lists and checks read-only mode with `VERIFY2`. `MergeParentSet` removes the opposite parent marker; an override `!parent` removes a prior unmarked parent, while ordinary parent additions are appended. Parsed section names are lowercased; this selected parent-token path does not explicitly lowercase all referenced parent names. The recursive evaluator tracks a resolved cache and recursion stack; inheritance cycles go to `Debug.fatal`. Missing parents create empty fallback base entries, including an override-only parent compatibility case, with conditional warnings. Consequently a parent need not be defined earlier textually, but case/availability mistakes are not certified as safe intended inheritance. N14/N15/N18, `Xr_ini.cpp:297–325,718–809,1001–1101`.

Parents merge in listed order, so later parent values replace earlier collisions. Local base data and its scalar overrides are merged next; the resulting local values replace parent values. In a base/mod merge a deletion records a removed key; in a parent/local merge a deletion marker collision keeps the parent item. Thus a bare `!key` in ordinary child data must not be documented as universally deleting inherited values. A section deletion is applied to the resolved map after inheritance; copied descendant values can remain. These conclusions follow the active branches, not only parser comments. N17/N18/N20.

`>key = ...` and `<key = ...` are routed to list modifications. After parent/local/scalar resolution, edits sort by unprefixed key and ascending collected insertion index, **without the scalar depth comparator**. Splitting uses literal commas, trims token edges and drops empty tokens; it does not protect commas inside quoted list items. Insert appends tokens without deduplication; removal removes all exact matching tokens. Edits can create a previously absent key unless it was blocked by the base/mod deletion set; null edit values are skipped. If edits empty the list, the result entry is omitted. The resulting item's filename tracks the applied edit, not a history of every contributor. N19, `Xr_ini.cpp:1103–1292`; routing and collected insertion indices in N28, `Xr_ini.cpp:232–253`.

## Reads, writes and save output

`section_exist` searches the supplied section name exactly; `r_section` lowercases its lookup. Keys remain exact comparator lookups. Lua wrappers that first call `section_exist` can therefore reject a casing that a native `r_section` would accept. Missing sections/keys take assertion/fatal paths in selected reads, while an existing empty entry can return a null native string. Native `atoi`/`atof` readers do not establish strict numeric syntax/range/finite-value validation; vector readers start with zero components and do not check `sscanf`'s parsed-component count. Boolean reads lowercase and use only `on/yes/true/1` as true, after a length VERIFY; token lookup is case-insensitive and returns 0 when unmatched, which is not a unique missing-token sentinel. N23–N25, `Xr_ini.cpp:1563–1828`, `xr_ini.h:86–90`; [Lua wrapper differences](../../02-lua-api/configuration/ini-api.md).

Native `w_string` requires writable mode, normalizes/creates a section, parses key/value whitespace and asserts duplicate replacement is allowed by `eOverrideNames`. Both insert and replacement use a newly constructed item's empty filename metadata. Native removal requires writable mode. Lua writer wrappers impose additional **existing section and key** checks; setting writable/override flags does not bypass those checks. `set_override_names` controls native runtime duplicate writes; it does not change the parser's DLTX selection rules. N26/A04/A05, `Xr_ini.cpp:1833–1885,2019–2050`, `script_ini_file.cpp:121–224,235–288`.

`save_as` writes the **resolved DATA** as plain sorted sections/key/value lines, with decorated commas. It does not reproduce includes, inheritance declarations, deletion/list-edit commands or original source structure. A nonempty supplied filename changes the object's stored filename **before** opening; open failure returns false after that change. Success is local writer completion, not an atomic profile transaction, filesystem durability proof, game-save persistence or refresh of consumer fields. Automatic destructor saving uses the same native mechanism under its two flags. N02/N22, `Xr_ini.cpp:148–245,1501–1561`.

## Lifetime and diagnostics

`system_ini()` and `game_ini()` expose borrowed settings pointers. `reload_system_ini()` destroys the old system object, clears the whole named cache, constructs `system.ltx` again, and returns the new borrowed pointer. No selected body revokes every Lua alias, recreates game/auth settings, reruns startup or refreshes all fields/caches copied by consumers. Reacquisition and dependent state reconciliation require the actual owning lifecycle; a convenient function name does not guarantee a safe live reload. A07/A10/A12 and N01.

Lua constructors and adopted `create_ini_file(text)` results instead have owned userdata finalizers. `close()` directly calls native deletion without clearing that ownership or all aliases. The combination presents stale-alias and later owned-finalizer deletion hazards in source; no safe “close then collect” recipe is certified. Do not close borrowed engine settings. This is a source-derived lifetime warning, not a reproduced runtime crash. A05/A07/A10/A12–A15; [API ownership table](../../02-lua-api/configuration/ini-api.md).

DLTX diagnostics inspect **final surviving item metadata**: `dltx_get_filename_of_line` can return nil for absence, `dltx_is_override` tests whether that filename starts with `mod_`, and `dltx_get_section` returns a new Lua table keyed by item name with name/value/filename fields. A filename heuristic can disagree with literal override syntax, included filenames or runtime writes. Removed values, replaced contributors and complete MO2 provenance are not recovered. Empty native values can omit a table's value field through nil conversion. N21/A06/A10/A12/A17/A19/A20, `Xr_ini.cpp:1420–1499`, `script_ini_file.cpp:290–314`.

## Remaining integration and next work

Selected bundled `r_*_ex` defaults and `ini_file_ex` replacement differ from raw native readers; their definition-level contracts are in the API page. Actual global installation/order and later replacements remain CONFIG-03/04 work. Reuse domain option/preset, task, economy and persistence evidence instead of claiming all those consumers reload together. Exact effective include/mod files, filesystem winners, cache settings, build flags and consumer copies remain unknown. Exhaustive malformed-input/security/VM/error propagation and every parser/option remain optional depth. CONFIG-02 closes this selected source scope; **next CONFIG-03 — native script loading, startup and shared callbacks**. [Completion status](source-completion-status.md), [guide](development-reference.md), [roadmap](../../ROADMAP.md).

## Subsequent available-source completion

CONFIG-04 supplied consumers, [practical consolidation](development-reference.md) and [bounded audit](../../08-research/verification-2026-10-12-v0.1.77.md) are now complete within selected available-source scope. The dated findings/next allocation above retain their original research revision; [current completion](source-completion-status.md) keeps effective integration partial and runtime deferred.
