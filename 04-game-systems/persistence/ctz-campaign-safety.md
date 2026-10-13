# CtZ campaign identity, schema and reconciliation

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

**Research revision: v0.1.52.** PER-03 is complete within its selected source scope. Runtime verification remains deferred. This describes CTZ005J Alpha 0.0.5j at commit `eba6660db09353dcc42a195ae6e7e706f4762277`; it does not certify save compatibility or change CtZ gameplay.

Evidence references C01–C13 are local to the [PER-03 ledger](../../evidence/persistence/ctz-campaign-safety-2026-10-11.csv). [Investigation](../../08-research/investigations/2026-10-11-PER-03-ctz-campaign-safety.md), [manifest](../../evidence/manifest.md), [native pipeline](native-save-load-pipeline.md) and [supplied Lua storage contracts](lua-storage-contracts.md) establish provenance and the surrounding boundaries.

## Keep four kinds of version and identity separate

| Item | Selected source value/meaning | Limit |
| --- | --- | --- |
| Package baseline | Alpha 0.0.5j, pinned CTZ005J commit | Package identity does not update every internal literal |
| Campaign `VERSION` | `0.0.3b`; stamped into state | Internal literal differs from package label; preserve it as evidence |
| `SAVE_VERSION` | `9`; saved in `state.save_version` and `m_data.ctz_save_version` | `load_state` does not read either saved version to dispatch or reject schemas |
| `scenario_id` | `rostok_army_warehouses_prototype`; `created_sec` is game time | Initial metadata is not a checked campaign fingerprint in this load/rebind chain |
| Detachment/native IDs | Strategic string key plus numeric `squad_id` and `spawn_member_ids` | Numeric resolution alone does not prove campaign/generation identity |

C01/C02/C04/C05. The selected load handler replaces version fields after its repairs. This establishes labeling and field-presence backfills, not a versioned compatibility gate. There is no scenario/fingerprint comparison in that handler or the cited numeric rebind paths. This is a bounded source finding, not an assertion that an installed manager cannot supply additional identity checks.

## Save and deserialize contract

`save_state(m_data)` stamps an existing state, writes the top-level schema label and attaches the live state table as `ctz_state`. `load_state(m_data)` assigns that table directly; only absent/false state creates an initial state. It does not deep-copy, consume-clear `m_data.ctz_state`, validate the entire table shape, or wrap its full body in a local protected call. Caller/encoder ownership and error policy remain missing effective contracts. C02; [PER-02](lua-storage-contracts.md).

The handler defaults events, battle sequence and detachments; backfills native siege origin for old assault-locked movement records; ensures economy; supplies missing forts and named fort anchors; converts false contest values to nil; recounts ownership totals; clears selected mobile route/recovery transient fields; and gives old field engagements native mode. Repairs are conditional by field/role, rather than a saved-version migration sequence. Unknown fields are not removed by a general whitelist. C02/C10.

Economy repair creates missing accounts/stock, converts legacy resources to roubles, clamps/coerces selected balances and flags a newly created economy/account for later clock anchoring. The first economy tick then anchors to current game time and returns without retroactive income; a clock rewind also resets the anchor. This targeted mechanism does not validate all campaign fields. C03.

## Restoration phases and side effects

| Entry/phase | Selected operations | Boundary |
| --- | --- | --- |
| `load_state` | Restore strategic table and targeted repairs | Does not perform the later member setup |
| `on_game_load` | Reset readiness timestamp, start 8,000 ms transition grace, quarantine targets | Comment describes realization timing; effective emitter timing remains unverified |
| Quarantine | Resolve saved squad IDs; stamp ownership; clear movement transient targets, retain numeric assigned target; garrison sanitization is narrower | Numeric type check does not establish target validity; strategic `target_fort` retained |
| First actor update | Install task guards; skip fake_start; for initialized state require readiness and elapsed transition grace, then restore and validate | Does not initialize absent campaigns here |
| Actor update | Guard installation; campaign enable check; marker update; separately gated battle maintenance; interval gate; readiness/grace; create absent state; restore; initialize or validate | The readiness/grace gates do not encompass every operation in the callback |

C06/C07/C13. Readiness requires actor plus a nonempty, non-fake_start level and 3,000 ms elapsed from its candidate timestamp. The strategic interval defaults to 10 seconds. Battle maintenance has its own 2,000 ms interval. These delays are guards in source, not proof of object registration completion. Guarded `safe_register` attempts callback installation with `pcall`; the effective callback emitters and ordering relative to native hooks remain open.

`restore_loaded_squads` only acts on initialized state. A successful numeric lookup stamps CtZ ownership, supplies missing expected/requested counts and compares sorted member IDs to the squad's `ctz_setup_sig`. Changed signatures trigger member setup; individual setup attempts are protected, and the signature is stored afterward even though that protection can swallow an error. This is conditional retry avoidance, not transactional restoration success. C08.

## Numeric identity and initialization

`get_squad(id)` returns `alife():object(id)` when available; it has no section/class/faction/generation check. Spawn records retain the squad ID, original member IDs, expected/requested counts and initial casualty baseline. Initialization retries reuse any object resolved from an existing record's squad ID; otherwise they replace that record with a new definition and attempt spawn, stopping on failure. Only after the loop is the campaign marked initialized. C04/C05.

Member reclamation is separately gated by configuration, core role and a table of original IDs. Missing current members are looked up by original numeric ID; apparently alive objects may be unregistered from an old group and registered into the core squad. No original section/faction/campaign token comparison appears in this path. Protected calls can leave partial effects; there is no rollback around transfer. C09.

**Inference:** if a persisted ID resolves to a different generation/object, these selected paths provide no independent proof that it is the intended CtZ entity before ownership stamping or member transfer. The investigation does not establish that ID reuse actually occurs under a particular save/profile. Native save/load member repair and ID lifecycle remain in [ALIFE-04](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md); effective storage reset and campaign pairing remain prerequisites.

## Reconciliation is more than deserialization

Validation first absorbs eligible ambient squads, suppresses selected unrelated human squads and ensures base markers. It then looks up each detachment, reclaims core members, applies role/engagement/order-dependent routing, takes a fresh snapshot, reconciles losses and updates markers/diagnostics. These are world mutations, not just a read-only restoration pass. C12/C09.

Snapshots distinguish absent squad (`MISSING`, zero alive) from resolved squad with zero alive (`LOST`). Core casualty reconciliation ignores `MISSING`; an absent baseline is initialized to the snapshot count, and later decreases reduce strategic faction strength, clamped at zero. Increasing counts update the baseline without refunding strength. The NPC death callback logs observation and avoids a second strategic decrement. C10/C11/C13.

For missing core squads, validation normally waits 120 game seconds using the persisted `missing_since_sec`; a resolved squad clears that timer. An active movement engagement with a surviving opposing movement record can immediately classify a missing squad as lost. The timer is not universally reset by load; a game-clock rewind can postpone confirmation. This exception and timer are source policies, not independently proven combat truth. C01/C12.

After snapshots, destruction bookkeeping runs, followed by field engagements, fort battles, regrouping, operational status and economy. Destruction preserves `destroyed_squad_id`, marks destroyed/time and clears relevant battle/marker state. See the cited branches for role distinctions; this pass does not claim to document every strategic battle algorithm. C11/C12.

## Open safety contracts and next work

The available source establishes targeted repairs, delayed setup and casualty policies. It does not certify arbitrary old/new schema acceptance, malformed payload handling, campaign/new-game pairing, native/companion atomicity, generation-safe rebinding, every retry's idempotence, or installed callback success/order. Obtain winning core storage/dispatcher sources and profile settings before claiming those contracts closed. Runtime remains deferred; no save files or CtZ source were edited.

Next: practical persistence consolidation and final bounded available-source audit, bringing PER-01–03 together while keeping effective-source and runtime gaps explicit. [Roadmap](../../ROADMAP.md).
