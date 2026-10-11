# Warfare configuration and policy controls

> ADR document set: **v0.1.47**. Research revisions and source/build versions below describe their original scope.

- ID: WAR-003
- Source status: source-confirmed for the selected supplied-package paths; scoped negative searches
- Runtime status: untested; deferred until the user resumes verification
- Last reviewed: 2026-10-11

Baseline: BETA150 archive SHA-256 `9f71999bb44cb6d3e41c431feaf5be4714159522df1fa8d71599ac039946315d`. Main scripts and the optional GAMMA patch are distinct variants, not an assumed combined installation. W01–W18 below refer only to the [Warfare control ledger](../../evidence/warfare/configuration-controls-2026-10-11.csv). The exact MO2 winners, preset selection, saved UI values and later replacements remain unknown. [Package provenance](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md).

## Producers, aliases and refresh boundaries

`warfare_options.update_settings()` reads UI values into general and faction tables. Main Warfare `on_game_start` calls it; the options module registers it for `on_option_change`. Some fields are aliases: UI `general/auto_capture` becomes `options.enable_auto_capture`, and faction `flag_priority` becomes `faction_flag_priority`. The faction path is constructed dynamically from its faction name. W01 `23–200,302–304`; W02 `917–940`.

The offline-combat script independently reads its mode at coordinator execution, while its Warfare combat radius is squared into a **local at module initialization**. `update_settings` does not update that local. A full-file scoped search finds only its definition and later coordinator assignment to `opt_dist`, with no local recomputation path. An external reload/replacement remains possible; an option change cannot be assumed to refresh every consumer immediately. W03/W04.

## Control-to-consumer map

Paths below are relative to UI `alife/`, unless marked as fields/constants. Main script evidence is BETA150 main; UI declaration samples are separately the optional GAMMA patch.

| UI path / field | Producer and consumer | Effect / contract | Evidence |
| --- | --- | --- | --- |
| `general/offline_combat` | Direct live `ui_options.get` in coordinator | `full` subscribes to squad updates; `on_smarts_only` subscribes to smart updates; other values remove the previous subscription | W04 |
| `warfare/general/offline_combat_distance` | Local squared snapshot at module load → coordinator's `opt_dist` → enemy validation | Combat test uses squared X/Z distance with strict `<`; not native online radius | W03–W05 |
| `warfare/general/enable_mutant_offline_combat` | `options` refreshed by settings reader → coordinator copies policy | Mutant eligibility policy in Warfare; not a native spawn limit or universal creature combat disable | W01/W04/W05 |
| `warfare/<faction>/offline_power_multiplier` | Faction table → coordinator copies multiplier → NPC power → squad power cache | Multiplies rank/class-based abstraction; existing cached power is not universally recalculated by an option change | W01/W04/W06 |
| `warfare/general/auto_capture` | Alias `enable_auto_capture` → selected capture method's gates | Enables staged squad-spawn/target policy, not direct owner assignment; newer method also has a manual-request branch | W01/W08 |
| `warfare/general/use_old_auto_capture` | Settings table → early method selection | Chooses old/new capture routes with different conditions and spawn locations | W01/W08 |
| `warfare/general/auto_capture_max_distance` | Settings table → squared X/Z comparisons | Bounds selected capture proximity/reset tests; not actor-centered 3D native switching | W01/W08 |
| `warfare/general/auto_capture_wait_time` | Settings table → elapsed game-time checks | New route compares rounded seconds to value×60; old route rounds seconds/60 then compares to value. Both use game-minute scale, with distinct rounding/stages | W08 |
| `warfare/<faction>/min_faction_respawn`, `max_faction_respawn`, `base_count_modifier` | Faction settings → selected `spawn_defense` interpolation and timer | `lerp(min,max,clamp((base_count+modifier)/warfare.base_count,0,1))`; timer checked in game seconds against value×60, with additional Monolith/near-actor gates | W01/W02/W10 |
| `warfare/<faction>/expansion_aggression`, `min/max_smart_targets_per_base` | Faction table → selected target/invasion random and count gates | Influences strategic choices; not a travel-speed or guaranteed expansion-rate setting | W01/W09 |
| `warfare/<faction>/linked_level_targeting` | Faction table → target candidate construction | Selected non-overflow route limits candidates to current/linked levels; alternative includes active levels | W01/W13 |
| `warfare/<faction>/base_priority`, `resource_priority`, `territory_priority`, `flag_priority` | Faction table → selected additive target-scoring terms | Weights terrain properties, alongside further conditions; score is not arrival/capture | W01/W13 |
| `warfare/<faction>/keep_last_base` | Faction table → owner retention branch | Can retain prior ownership under nested conditions; not a universal strongest-faction selection rule | W01/W12 |
| `warfare/general/monster_min/max_faction_respawn`, `monster_max_squads_per_level`; `general/alife_mutant_pop` | Options/UI population → selected mutant respawn/capacity code | Separate spawn/timer/capacity controls; not the native scheduled batch limit | W01/W11 |

The table documents selected paths, not every Warfare option or every consumer. It does not establish that the installed variant executes them. [Assignment, ownership and combat investigation](../../08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md) supplies the surrounding reach/death/effective-script boundaries.

## Clocks and local constants

| Input | Selected source meaning | Limitation |
| --- | --- | --- |
| `UPDATE_TIME=30`, initial coordinator event delay `2` | Coordinator resets a real-time event; load callback schedules startup | Source constant/event request, not every battle's interval or a verified installed timer implementation. W03/W04/W07 |
| Capture wait | Elapsed game time; both routes scale to minutes differently | Staging, rounding, prerequisites and update invocation prevent an exact delay guarantee. W08 |
| Selected faction defense respawn | Game-time minutes after interpolation and gates | Not all creature respawn paths, and not a native update setting. W10 |
| `HIT_BASE=0.4`, `HIT_FACTOR=0.2` | Damage uses cached attacker power times `0.4 + random()*0.2`, then rounded in the battle code | A casualty abstraction, not live weapon/armor simulation. W03/W06 |

The `offline_health` section exists in both supplied main and optional patch configuration files. The examined `init_settings` reads `story_communities`, `ignore_list` and `stationary_squads`; the selected rank/class damage calculation does not establish consumption of the `offline_health` table. This is a bounded consumer finding, not a claim that no other addon uses the section. W06/W07/W17/W18.

## Defaults, presets and installed values

| Declaration sample | Optional GAMMA-patch UI `def` | What is actually established |
| --- | --- | --- |
| `general/offline_combat` | `"full"` | Declaration in that patch's UI table, not current user selection |
| `general/excl_dist` | `75` | Declared list includes 0/25/50/75/100; runtime value still unknown |
| Warfare capture toggle / old-method toggle | Both `false` | UI declaration defaults only |
| Capture distance / wait | `50` / `1` | Declared defaults; selected consumers supply the units/contracts above |
| Offline combat radius / mutant combat | `50` / `true` | Declaration does not change the module-load snapshot's refresh behavior |
| Faction offline multiplier / keep-last-base | `1` / `false` | Shared faction UI declaration; applied preset/faction/user values can differ |

W14 `ui_options.script:428–442,466–510,543–575`. The main preset has separate values and legacy paths, including `warfare/general/disable_offline_combat`. Main `warfare_options` readers for `disable_offline_combat` and `simulate_offline_combat_at_smarts` are commented out; active mode selection is the direct `general/offline_combat` read described above. A preset entry or inclusion listing alone does not prove its application or an active consumer. W01/W04/W15/W16. Do not replace source distinctions with “GAMMA defaults.”

## Online-status policy

BETA150 main assigns a replacement `sim_squad_scripted.check_online_status` at module scope. In source order it prioritizes survival, task force-online, companions and levels outside `level_weathers.valid_levels`, then selected monster hours or an offline, non-story proximity exclusion using `general/excl_dist` when the actor is not sleeping. It writes `forced_online_status`; the native-first permission overrides consume that field later. W01 `255–299`; [native controls](../alife/configuration-controls.md#permission-and-update-controls).

The producer's literal hour comparisons, precedence and differences from the bundled engine script are preserved in [ALIFE-08](../../08-research/investigations/2026-10-11-ALIFE-08-switching-eligibility.md). This is not a direct online/offline command or an atomic refresh/switch transaction. The separate `override_functions` body has no caller found in the supplied package's prior scoped search; its definition alone does not install all replacements. No installed winner is inferred.

## Development use and disposition

Before diagnosing a later CtZ behavior, distinguish native switching from Warfare routing, arrived smart state, ownership and offline casualty accounting. Record the option's source variant, alias, read/refresh point, clock and consumer. Changes to one options table can leave module-local snapshots or caches unchanged; this is a reason to inspect the consumer, not a tested reload prescription.

WAR-003's selected package-control reference is complete within scope. Full effective script order, board/smart reach/jobs, creature death/safe release and strategic persistence remain open in the [shared completion status](../alife/source-completion-status.md). Runtime verification remains deferred.
