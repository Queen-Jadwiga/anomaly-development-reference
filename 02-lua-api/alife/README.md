# A-Life / Warfare C++ and Lua interface catalog

> ADR document set: **v0.1.54**. Research revisions and source/build versions below describe their original scope.

**ADR v0.1.39 · ALIFE-09 · 11 October 2026 · source inventory and focused contracts; runtime deferred.**

This catalog maps native classes to Lua registration names, exported methods/fields, virtual override points and supplied script declarations. It complements the lifecycle investigations; it does not establish the active GAMMA implementation merely from an export or function definition.

## Start here

- [C++ classes, Lua names and ownership map](class-map.md).
- [Simulator API: lookup, creation, release, switching and iteration](simulator-api.md).
- [Server entities, squads, tasks and brains](server-squad-api.md).
- [Script modules and unresolved effective interfaces](script-interfaces.md).

## Searchable source inventories

| Artifact | Contents |
| --- | --- |
| [Native/Lua classes CSV](native-lua-classes-oct11.csv) | 84 registration rows with native template arguments, Lua names, evaluated branch and origin line |
| [Bindings CSV](native-lua-bindings-oct11.csv) | 1,150 registration rows: methods, virtual methods, fields, constructors and global functions; overloads preserved |
| [Binding helper declarations CSV](binding-helper-declarations-oct11.csv) | 174 source definition signatures, including the C++ receiver parameter where present |
| [Script interfaces CSV](script-interfaces-oct11.csv) | 1,372 function declarations from selected bundled scripts and the BETA150 main/patch sources; variants retained |
| [Evidence ledger](../../evidence/alife/interface-evidence-oct11.csv) | SHA-256 and line count for 73 input files |
| [Rebuild script](../../tools/build_alife_catalog.py) | Reproduces the scoped extraction from locally extracted archives |

Counts are **rows**, not unique callable methods or promises that every row exists in one executable. Repeated virtual registrations across classes and mutually exclusive branch results are retained. Inherited availability is obtained from the registered bases; the CSV does not duplicate every inherited method on every descendant.

## Method and limits

The inventory processes 21 registration translation units: the seven `alife_*_script.cpp` files and `game_graph_script.cpp` under `src/xrGame`, plus 13 server-object registration files matching `xrServer_Objects*script*.cpp` / `xrserver_objects*script*.cpp` under `src/xrServerEntities`. Shared `xrServer_script_macroses.h` and `script_export_macroses.h` are expanded with the C preprocessor.

Two source projections are evaluated: `XRGAME_EXPORTS` defined and undefined, with other macros undefined. Includes are suppressed while preserving original line positions. This is a preprocessing audit, **not compilation, linkage or exhaustive build-configuration verification**. `DEBUG`, other optional macros and registrations elsewhere can change coverage. Commented-out registrations are excluded. Macro-expanded rows cite the registration invocation line; their binding expression comes from the shared macro definitions. These headers are separately hashed.

The class CSV records the literal expanded template arguments, including wrappers and bases. This is the **registered Lua inheritance**, which can omit native C++ bases. The bindings CSV preserves exact binding expressions, explicit casts and policies. A raw method pointer without a cast is not automatically an exact Lua signature: resolve its declaration and converter policy before using it. The focused pages supply selected checked contracts; the helper CSV is a source declaration index, not a fully resolved overload/conversion catalog for all 1,150 rows. C++ default arguments do not automatically establish optional Lua arguments.

Lua rows inventory named `function` declarations, including colon receivers and dotted monkey-patch assignments. Anonymous assigned functions, generated callbacks, local closures and arbitrary writable script fields are outside that extraction. Long block comments are excluded. Script bytes are hashed unchanged; non-UTF-8 prose is decoded with replacement for declaration scanning, whose symbols are ASCII. Declaration presence does not prove module loading or replacement order.

Rebuild with Python 3 and `cpp` from a directory containing `engine-source/xray-monolith-2026.10.11/` and `warfare-source/beta150/`; run `python tools/build_alife_catalog.py --source-root /path/to/xray-monolith-2026.10.11 --warfare-root /path/to/beta150`. API output goes to `02-lua-api/alife/` and the file ledger to `evidence/alife/`. Use `--repo-root` for isolated output. Sources are not redistributed with this catalog.

## Baselines and disposition

ENGINE1011 archive SHA-256: `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`. BETA150 archive SHA-256: `9f71999bb44cb6d3e41c431feaf5be4714159522df1fa8d71599ac039946315d`. Exact upstream engine commit, executable correspondence and installed script winners remain unverified. [Package provenance](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md).

This closes the scoped interface-mapping pass. Effective smart/board, death/safe-release and persistence chains remain open. See [current roadmap](../../ROADMAP.md). Runtime verification remains deferred; no gameplay change or license is introduced.

## Lifecycle context

Read the [lifecycle/state reference](../../04-game-systems/alife/lifecycle-state-reference.md) and [callback phases](../../04-game-systems/alife/callback-phase-reference.md) before applying these contracts across spawn, switching, load or teardown. Runtime verification remains deferred.

For producer/consumer, clock and refresh boundaries, use the [native configuration controls](../../04-game-systems/alife/configuration-controls.md) and [Warfare policy controls](../../04-game-systems/warfare/policy-controls.md).
