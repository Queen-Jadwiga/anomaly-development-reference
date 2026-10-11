# WAR-002a — Warfare source packages and effective-profile boundary

> ADR document set: **v0.1.54**. Research revisions and source/build versions below describe their original scope.

**ADR v0.1.33 · 11 October 2026 · package-source inspection; installed-profile reconciliation pending; runtime deferred.**

## Available sources

The Library search located two previously supplied archives. Both were extracted for this pass. No archive was installed into the game, and no source package was designated as the active profile merely from its name.

| Source ID | Artifact | SHA-256 | Meaning |
| --- | --- | --- | --- |
| ZIP142 | `warfare a-life overhaul gamma.zip` | `566739c68b4597ab417e98ee9e3ce11858f3d42ed29a39d7e3c39ed2d76443a8` | Root folder contains a GAMMA-labelled package; meta.ini and installation notes identify 1.4.2 |
| BETA150 | `WarfareALifeOverhaul_1_5_0_beta3_1.7z` | `9f71999bb44cb6d3e41c431feaf5be4714159522df1fa8d71599ac039946315d` | Installation notes identify 1.5.0; main files and separately selectable GAMMA patch are distinct folders |
| ENGINE1011 | `xray-monolith-2026.10.11.zip` | `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee` | Native engine source; exact upstream commit and executable equivalence remain unverified |
| GAMMA-UPSTREAM | `Grokitach/Stalker_GAMMA` commit `ab0f743af42a3b3b0b0ee853b3676f5189f7f0d0` | Git commit pinned below | Public repository reference; not the user's active MO2 installation |

The [16-file evidence ledger](../../evidence/warfare/source-evidence-war002-oct11.csv) records exact archive-relative paths, hashes and line windows. The [17-script byte-comparison ledger](../../evidence/warfare/archive-script-comparison-oct11.csv) compares ZIP142 against the BETA150 main folder and records BETA150 GAMMA-patch variants. It inventories main-folder scripts, not every resource or optional patch.

## Why version labels are insufficient

ZIP142 and BETA150 have byte-identical main versions of `sim_offline_combat.script`, `sim_squad_warfare.script`, `sim_squad_scripted.script`, and `warfare_options.script`. Their `smart_terrain_warfare.script`, `warfare.script`, `faction_expansions.script`, and `xr_logic.script` differ. All 17 comparisons are in the ledger.

The smart-terrain differences are substantive: BETA150's update routes distinguish base and pure-resource processing; its newer autocapture initiation checks base/territory properties, while ZIP142's examined initiation checks base/resource/territory properties. BETA150 also contains newer night/resource handling. This is not a claim that all policies changed or that BETA150 is the installed winner. [W07:368–456,502–741; W16:290–379,387–442]

In BETA150, the GAMMA-patch squad script differs from the main squad script at the help-target condition: the patch reads two survival-mode configuration modules and their seek-distance setting; the main uses `IsSurvivalMode()` and a fixed 250-distance test. The package's installer offers main and GAMMA patch as separate choices and describes the GAMMA patch as a separate installation intended to win conflicts. That describes author intent, not observed user load order. [W04:6–42; W10/W11:265–274]

## Public GAMMA comparison

Pinned primary references:

- [Public Warfare-patch squad script](https://github.com/Grokitach/Stalker_GAMMA/blob/ab0f743af42a3b3b0b0ee853b3676f5189f7f0d0/G.A.M.M.A/modpack_addons/Warfare%20Patch/gamedata/scripts/sim_squad_scripted.script).
- [Public default mod list](https://github.com/Grokitach/Stalker_GAMMA/blob/ab0f743af42a3b3b0b0ee853b3676f5189f7f0d0/G.A.M.M.A/modpack_data/modlist.txt).

Comparing decoded text, the public Warfare-patch squad script uses the main archive's survival condition rather than BETA150's GAMMA-patch condition. It also has a trailing-blank-line difference in the materialized comparison. This is a scoped text comparison; archive byte hashes are recorded separately, and no SHA-256 of normalized public text is represented as a raw Git blob hash.

The public default list contains disabled entries for Warfare Patch and the numbered Warfare A Life overhaul. Default availability/status does not establish the user's enabled state, installation content or selected game mode.

## Historical user-profile evidence

The supplied `modlist.txt`, uploaded 5 October 2026, is a CSV-style export with priority, status, name and installation metadata. The relevant inspected rows list Useful Idiots, GAMMA A-Life fixes, AlifePlus, AlifeGuard and an earlier CtZ package as enabled. Its final CtZ row refers to Alpha 0.0.1m, not the published 0.0.5j. No conclusion about today's Warfare enablement can be drawn from absent rows in this export.

This evidence identifies additional source candidates; it does not prove which script files they overwrite, which functions they replace, or today's callback order. Personal filesystem paths and the full profile export are deliberately not republished. Source locations for this bounded observation: export lines 324, 423, 588–589 and 613.

## Missing pieces required for effective-profile closure

The inspected engine and Warfare archives do not supply the exact core filenames `sim_board.script`, `smart_terrain.script`, `simulation_objects.script`, `se_stalker.script`, `se_monster.script`, `safe_release_manager.script`, or the global callback wrapper `_g.script` / `_G.script`. Some other missing module references, such as faction/level helpers, also require effective source before exhaustive policy tracing.

A useful next source submission is a ZIP copied from the **game's virtual filesystem under the active MO2 profile**, rather than a single mod directory:

1. `gamedata/scripts`, including nested Lua folders. This captures both winning files and differently named scripts that monkey-patch them at load/startup.
2. Relevant effective configurations: `gamedata/configs/misc/offline_combat_simulator.ltx`, `simulation_objects_props.ltx`, `simulation.ltx`, `gamedata/configs/alife.ltx`, and the selected Warfare preset/options configuration where available.
3. Current MO2 profile mod list and the supplying-mod/conflict information for the core squad/board/smart/Warfare files.

A file-copy/archive tool launched through MO2 can read the virtual view without running the game. A ZIP of the physical Anomaly `gamedata` directory may omit loose files supplied virtually by MO2 or packed base-game scripts. If packed core scripts remain absent, extract those separately and identify their origin. Profile names, version labels and an enabled-mod list alone do not establish function replacements by scripts.

## Disposition

The earlier [WAR-001 missing-source statement](2026-10-11-WAR-001-ctz-integration-boundary.md) remains a historical description of v0.1.31. Two package sources are now available and inspected; **effective-profile sources remain unresolved**. See [WAR-002b policy trace](2026-10-11-WAR-002b-policy-offline-combat.md) for conclusions that can already be supported without runtime testing.

ALIFE-03 and WAR-002 remain partially open. Their remaining work is winning-file verification, board/smart arrival and job registration, creature death overrides, safe-release scheduling, and startup/monkey-patch ordering. No compatibility result or gameplay change is implied.
