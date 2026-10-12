# PER-02 — Supplied Lua storage contracts and effective-profile gaps

> ADR document set: **v0.1.58**. Research revisions and source/build versions below describe their original scope.

- ID: PER-02
- Subsystem: persistence
- ADR revision: v0.1.51
- Record status: complete-within-scope
- Source status: source-confirmed codec/callers; scoped-source-audit for missing definitions
- Runtime status: untested; deferred until explicitly resumed by the user
- Baselines: ENGINE1011, BETA150 main, CTZ005J; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-11

## Question and scope

What storage contracts can be established from the supplied codec, binders and consumers, and which installed core implementations remain absent?

Include native Marshal value/reference/type/error/registration mechanics, shared callback forwarding, selected engine generic binder, main Warfare/xr_logic/squad/diplomacy consumers, minimal CtZ callback attachment/registration and bounded missing-definition scan. Exclude full codec robustness/portability certification, every custom userdata hook, installed core storage/file formats/dispatch, full CtZ identity/migration/reconciliation, gameplay edits and runtime. Completion is a codec/caller/gap map, not the complete effective Lua storage system.

## Provenance and method

ENGINE1011 archive hash `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; BETA150 archive hash `9f71999bb44cb6d3e41c431feaf5be4714159522df1fa8d71599ac039946315d`. CTZ005J is Alpha 0.0.5j at commit `eba6660db09353dcc42a195ae6e7e706f4762277`; local campaign-script blob matches committed `25638cc5ae5ed81ceddacf6c16f39f53a5f4d791`. Engine executable/winning profile correspondence remains unknown.

[Ledger L01–L13](../../evidence/persistence/lua-storage-2026-10-11.csv) records 13 entries across ten source files. Read codec encode/decode/types/refs, extension startup, callback forwarding, binder branches, pstor tagged fields, selected namespace aliasing/consume-clear and helper calls.

Scoped missing-definition scan covers 110 `.script`/`.lua` files under ENGINE1011 gamedata, complete BETA150 and CtZ gamedata. Look for alife_storage_manager.script/_g.script basenames and named function/assignment definitions of save_var, load_var, get_game_object_state, get_se_obj_state and the three named CALifeStorageManager hooks. None found. This does not resolve aliases/native injected symbols or claim installation absence; ZIP142 and unrelated sources are outside this scan.

## Findings

[Reference](../../04-game-systems/persistence/lua-storage-contracts.md) and [API contracts](../../02-lua-api/persistence/lua-storage-api.md) carry nearby L-citations.

- Marshal serializes binary values/references; functions/custom persist paths have executable reconstruction behavior. Module availability does not establish file/schema/campaign storage policy. L01–L05.
- Shared callbacks forward arguments without a local snapshot/pcall; consumers can attach live table references and mutate load input. Emitter/encode/order contracts remain missing. L06/L10/L13.
- Selected generic binder chooses Marshal versus explicit packet paths, consumes manager object-state fields and performs ID cleanup. The manager's creation/return/ownership contract remains inferred only from call shape. L07/L08.
- Non-Marshal pstor supports selected scalar tags plus separate game-time entries; Marshal mode sends callbacks. Unsupported type logging is not a safe skip/round-trip policy. L09.
- Main squad shared methods are commented; active packet state remains explicit. Dynamic diplomacy calls global named-variable storage/reapplication, whose core definition is absent. L11/L12.
- CtZ attaches/reads a state table and attempts guarded callback registration; full campaign safety is the next investigation, not completed here. L13.

## Missing edges and alternatives

Installed managers can choose different codec, files, state ownership/reset, global emitters and type conversions. Later addons can replace callbacks or restore userdata. Matching consumer names and codec magic do not certify durability, companion-file coordination, schema compatibility or live object/campaign identity. Required winning sources and closure questions are enumerated in the reference.

## Checks and disposition

Verify ledger hashes/counts/ranges/symbols and CtZ pinned blob; compare active/comments, aliases, scalar format and missing-definition scope. Repository preservation/navigation/version and publication checks are in [increment verification](../verification-2026-10-11-v0.1.51.md). No execution/engine/gameplay/save tests, license addition or third-party source redistribution.

PER-02 closes this bounded supplied codec/caller/gap pass. Effective Lua storage remains partial. Next PER-03: CtZ campaign identity/schema/restoration/reconciliation from pinned source; effective core contracts and runtime remain open. [Roadmap](../../ROADMAP.md).
