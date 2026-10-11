# Supplied Lua storage contracts and effective-profile gaps

> ADR document set: **v0.1.51**. Research revisions and source/build versions below describe their original scope.

- ID: PER-02
- Source status: source-confirmed for selected codec/callers; scoped-source-audit for missing implementations
- Runtime status: untested; deferred until explicitly resumed by the user
- Last reviewed: 2026-10-11

L01–L13 refer to the [Lua storage ledger](../../evidence/persistence/lua-storage-2026-10-11.csv). Inputs are ENGINE1011 (archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`), BETA150 main (archive SHA-256 `9f71999bb44cb6d3e41c431feaf5be4714159522df1fa8d71599ac039946315d`) and CTZ005J (CtZ Alpha 0.0.5j, commit `eba6660db09353dcc42a195ae6e7e706f4762277`). These are supplied-source pins, not an installed profile. No third-party source is distributed.

Read with [native save/load phases](native-save-load-pipeline.md), [focused codec/caller contracts](../../02-lua-api/persistence/lua-storage-api.md), [FAC-02 storage boundaries](../factions/relation-persistence.md) and [ALIFE-04 CtZ reconstruction](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md).

## What the sources actually provide

| Layer | Available evidence | Contract boundary |
| --- | --- | --- |
| Marshal codec | Native extension registration and encode/decode implementation | Converts values to/from binary strings; not a file writer or campaign manager |
| Shared storage callbacks | `axr_main` declares save_state/load_state tables and forwards arguments to listeners | Does not identify the missing storage emitter, serialization timing or installed callback order |
| Binder consumers | Selected engine binder calls get_game_object_state and chooses Marshal/packet branches | Supplies selected fields and cleanup behavior; manager return/creation/schema contract unknown |
| Scalar pstor | BETA150 main xr_logic defines explicit non-Marshal tags/read/write | Limited packet field types; Marshal branch delegates through callbacks |
| Warfare/diplomacy consumers | Shared-table namespace and save_var/load_var call sites | Express storage intent, not implementation of file ownership or atomicity |
| CtZ consumer | Attaches campaign state and version fields to supplied table; reads it back | No proven deep-copy, encoded bytes, campaign fingerprint or dispatch order from this call alone |

L01–L13. A scoped scan of 110 `.script`/`.lua` files under engine `gamedata`, the complete BETA150 package and CtZ `gamedata` found no `alife_storage_manager.script` or `_g.script`, and no selected function/assignment definitions for the missing storage helpers or named native save/load functors. This is bounded to those supplied roots and definition patterns; it is not a claim that the installation lacks them. [Investigation](../../08-research/investigations/2026-10-11-PER-02-lua-storage.md).

## Codec behavior and limits

The inspected extension initializer registers `marshal.encode`, `decode` and `clone`; script-storage initialization calls that initializer. Availability in this source does not prove the user's executable or storage manager chooses it. L01/L04/L05.

The codec emits a magic byte `0x8e`, type/tag data and native binary values. Strings carry lengths, numbers use the selected eight-byte write, and ordinary tables recursively serialize keys/values through `lua_next`. Normal-table encode records a reference before recursion, and decode registers the new table before reading entries: this is the selected mechanism for shared/cyclic table references, not a tested guarantee for every custom persist hook. Table iteration is not a canonical sorted representation. L01–L03.

Lua functions use dumped bytecode and serialized upvalues; a C function not supplied as a preseeded reference is rejected. Userdata requires a `__persist` hook returning a function. Table/userdata custom restoration decodes that function and calls it. Thus decode can load bytecode and execute restoration callbacks; it is not just inert field assignment. Threads/lightuserdata are not ordinary supported encode values in this switch. Native objects do not become durable game identities merely because an extension can serialize some userdata. L02/L03.

Optional second arguments seed corresponding permanent references on encode/decode. Correct identity mapping depends on supplying the matching reference table. The inspected magic/bounds/error paths do not supply an application schema version, campaign identity, checksummed file transaction, all malformed-data safety or cross-build/VM portability certification. Custom metatables, CTime persistence hooks, numeric limits and installed wrapper policy need separate evidence. L01–L03; [API](../../02-lua-api/persistence/lua-storage-api.md).

## Shared callback table and aliasing

`axr_main.make_callback` forwards arguments to ordered functions or userdata methods. It has no local listener pcall or table snapshot in this selected body. The save_state/load_state registry comments describe a table argument, but the missing effective native-hook/global storage dispatcher must establish who constructs it, when encoding occurs and which listeners run. L06; existing [callback ordering reference](../alife/callback-phase-reference.md).

BETA150 Warfare save writes a `m_data.warfare` namespace, copies selected ID→target/owner entries and directly assigns several live tables to fields. Its load restores selected tables, performs a legacy patrol conversion, restores squad/owner caches and sets `m_data.warfare=nil`. Assignments do not deep-copy tables in Lua; callers can share referenced tables, and the load input is consumed/modified. This is not an immutable snapshot API. Exact serialization relative to subsequent listeners is unknown. L10.

CtZ's selected save callback similarly assigns `m_data.ctz_state=state` and version fields; load reassigns state from that field or creates initial state. Its safe registration checks callback presence and uses pcall. That proves guarded registration attempts, not successful emission/storage or a copied snapshot. Detailed campaign migration/identity/reconciliation is reserved for PER-03. L13.

## Binder storage versus non-Marshal pstor

The supplied engine generic binder registers for save_state under `USE_MARSHAL`; its native packet save/load methods use markers/base callbacks and then choose mode. Marshal load calls its own `load_state`, which requests manager object state; non-Marshal calls xr_logic packet helpers. Its shared save callback writes selected `xr_logic` fields, including a time-relative activation value; load restores selected fields and transfers/clears pstor tables when present. The helper's true argument suggests a creation request at this call site, but the absent implementation prevents asserting exact allocation/ownership/default guarantees. L07.

BETA150 non-Marshal `pstor_save_all` writes entry count, key, tag and value: number=0/float, string=1/stringZ, boolean=2/bool. A separate count/key/CTime sequence handles `pstor_ctime`. Loader performs matching reads and early elapsed-byte exits. This is not a nested-table or arbitrary userdata format. Unsupported types are counted and their keys written before the logging-only branch emits no recognized value/tag; that is not a demonstrated safe skip/round-trip contract. No runtime corruption is diagnosed. L09.

In its Marshal mode, pstor helpers initialize tables, send `on_pstor_save_all`/`on_pstor_load_all` callbacks and return. The sender call alone does not identify the listeners or the codec/storage format used. Also do not combine the engine binder and BETA150 xr_logic as proven installed winners. L07/L09.

BETA150 squad shared save/load methods are inside a commented block; its active state packet methods still write/read explicit string fields and markers, with the Marshal early-return commented out. Merely finding shared-method names is not proof those methods serialize squads through the shared table. L12; ALIFE-04 retains detailed squad field evidence.

## Caller-only manager contracts and cleanup

| Missing implementation | Selected call shape | What remains unknown |
| --- | --- | --- |
| `alife_storage_manager.get_state()` | Shared state lookup used by unregister cleanup and package consumers | Root lifetime, reset timing, ownership and allocation |
| `get_game_object_state(obj[,true])` | Binder selected-object state read/write | ID mapping, creation flag semantics, default subfields, encoded storage |
| `get_se_obj_state(se_obj,true)` | Existing offline outcome bookkeeping from FAC-05 | Server-object schema/cleanup and campaign safety |
| `save_var(actor,key,value)` / `load_var(actor,key,nil)` | Dynamic diplomacy stores/reads named directional relation keys | Owning namespace, default/type rules, codec/file location, durability |
| Named native manager hooks | PER-01 emits before-save/after-save/early-load functors | Connection to shared callbacks, filenames/companions, ordering and failures |

L07/L08/L11; FAC-05 R17 and [PER-01 extensions](../../02-lua-api/persistence/native-extension-contracts.md). These are observed consumer signatures, not invented implemented APIs.

Selected binder teardown removes its ID from `m_data.game_object`; selected generic server-unregister helper removes both `se_object[id]` and `game_object[id]`. Those are separate lifetime stages, and their effective dispatch must reach them. Neither sweeps arbitrary CtZ/Warfare references or establishes complete ID-reuse safety. L07/L08; [A-Life lifecycle](../alife/lifecycle-state-reference.md).

## Required effective evidence and next work

Collect winning manager/global/storage definitions, callback dispatcher and binders, `USE_MARSHAL` producer, active pstor/CTime hooks and relevant addon replacements. Trace root construction/reset, native hook→script emitter→listener order→encoding/file write, filenames/schema/type/default limits, error behavior, companion-file coordination and restore/cleanup phases. Existing provenance requirements are in [WAR-002a](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md).

PER-02 completes this codec/caller/gap pass within scope; the complete effective Lua storage system remains partial. Next: CtZ campaign identity/schema/restoration/reconciliation from its pinned source, then consolidation/audit. Runtime stays deferred, and no gameplay/save files are changed.
