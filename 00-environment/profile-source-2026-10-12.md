# GAMMA profile source intake — 12 October 2026

> ADR document set: **v0.1.83**. Research revisions and source/build versions below describe their original scope.

- ID: ENV-PROFILE01
- Research revision: v0.1.83
- Source status: uploaded snapshot hashes confirmed; selected reconstructed source chains traced
- Runtime status: supplied log observed; independent reproduction untested
- Last reviewed: 2026-10-12

The user reports profile **G. A. M. M. A**, Demonized MT-TEST executable dated October 11, and CtZ Alpha 0.0.5j. Runtime work was explicitly resumed on October 12; authorization does not establish that any new test passed. Raw profile/log/source archives remain private and are not published in ADR.

| Source ID | SHA-256 | Scope |
| --- | --- | --- |
| QJLOOSE1012 | `58229b570b5b32d8fac17b8952d1110a92efab5477d0dfcc0e102abcf97a509c` | First ZIP: 70 files, 653,054 uncompressed bytes; loose collection supplied through prior MO2 collection instructions |
| QJEXP1012 | `73a03ade693590c4f6430b633aeeda519d9727500d1394b9c567560ee64939c1` | Expanded ZIP: 4,303 files, 41,012,615 uncompressed bytes; unpacked files merged into the previous collection and separate CtZ folder |
| QJLOG1012 | `7c4be14d226df18c1a0f3afcfd5090776f9c1c3db1934a239674b3a13d6da09d` | Supplied game log: 20,754 lines; private filename/path omitted; line citations below refer to this exact artifact |
| QJMODS1012 | `21566fcb72e0271ac97927df0418d8ec0f8edfa68e2b66aa19e478c3db30e30f` | CSV-format profile export: 620 enabled rows, including 28 separators; priority gaps and enabled-only rows prevent reconstruction of the complete profile |

Reported executable SHA-256: `c9c7147e50f540799234548c1a00d1f4c34c7b358d7df8db9f89c4eb4068643c`. Executable bytes were not supplied with this intake; this is user-reported identity, not an independently rehashed binary or a match to ENGINE1011.

## Reconstruction and limits

The user confirmed unpacked files replaced copies in the collection, not a change to the live game. Preserve both ZIPs. Overlay the first loose `scripts`/`configs` over the expanded root `scripts`/`configs`, then include the separate `Capture the Zone - Alpha 0.0.5j/gamedata/scripts` and `configs`. This yields **4,290 research script/config files**: 4,209 from the expanded root, 70 from the first loose collection and 11 from the separate CtZ folder. Textures/assets and editor metadata are not research claims or ADR deliverables. Counts include the originally collected files but do not certify every file as a game input.

Six differing paths are restored from QJLOOSE1012: `scripts/axr_main.script`, `scripts/bind_monster.script`, `scripts/item_weapon.script`, `scripts/sim_squad_scripted.script`, `scripts/xr_combat_ignore.script`, and `configs/axr_options.ltx`. The other 64 original paths are byte-identical in both ZIPs. [Raw-hash comparison](../evidence/profile/overwritten-files-2026-10-12.csv).

Archive-relative ledger paths include `mo2 files for chatgpt/`. This is the supplied collection prefix, not a claim about the original installed filesystem. Expanded-root files include both unpacked material and retained loose copies; origin/mod winner names are not independently established. This composition is a reproducible research candidate, **not a complete verified MO2 effective profile**.

The separately supplied campaign script SHA-256 is `4f2b0703f438034ac126437f88ba8a0d82463fc14c05b45e814b75cde85e1540`, byte-identical to CTZ005J commit `eba6660db09353dcc42a195ae6e7e706f4762277`. Internal `VERSION = "0.0.3b"` and `SAVE_VERSION = 9` therefore do not contradict the Alpha 0.0.5j package label. This verifies the supplied installed-copy bytes, not absence of other runtime overrides. [P30](../evidence/profile/core-trace-2026-10-12.csv).

## Log observations

QJLOG1012 lines 8–15 report 73 archives, xrCore build 10108 dated October 11, MT-TEST 2026.10.11 and X-Ray Monolith 1.5.3; line 12 records session start October 12 at 19:54:11.727. The log's executable path is deliberately omitted here. Lines 5188 and the later startup pass report marshal availability. Observations do not prove native source/binary equivalence.

| Observation | Exact log lines | Limit |
| --- | --- | --- |
| Five script-load failures, each twice | 5209/13223; 6232/14244; 6904/14913; 6935/14944; 6946/14955 | Failed modules: `a_faction_prices`, `mags_patches`, `zz_ui_inventory_better_stats_bars`, `zzz_mspizza_godis_zoomcalc`, `zzz_player_injuries`; the zoom module reports syntax error, others nil globals |
| Six callback names rejected, each twice | 7002/15011; 7013/15022; 7039/15048; 7054/15063; 7067/15076; 8223/16122 | `on_fddar_consumable_anim_start/end`, `npc_on_enemy_selected`, `dotmarks_on_manual_interact_release`, `on_luabind_fatal_error`, `server_object_on_register`; rejection at these requests, not proof no later addition succeeds |
| Producer module load announcement | 5804/13816 | `callbacks_gameobject.script` announcement alone does not prove the supplied file's declarations completed or remained installed |
| CtZ load and campaign start | 7267; 16000; 16726 | Load at `fake_start`, later `l07_military`, then campaign initialized; no independent save/load or transition test certified |
| Dispatcher callstack | Rejection stacks adjacent to the above lines | `callback_set:267`, `make_callback:284`, `on_game_start:333` align with QJLOOSE1012; line alignment is supporting evidence, not whole-file runtime hash proof |

No `FATAL ERROR` blocks or lines beginning `[error]` occur in this log. Its terminal logger-close line is 20754. These scoped searches do not certify stability or rule out faults outside the captured session.

The five failed addon modules and their relevant nil-global providers are absent from both ZIPs. Do not treat this absence as evidence they are absent in the live profile: the log records attempted loads. Their source/origins and any other relevant loose overrides remain collection gaps. [Core trace and next tests](../08-research/investigations/2026-10-12-PROFILE-01-core-file-trace.md).
