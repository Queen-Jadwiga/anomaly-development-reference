# Rank, reputation and action-flag Lua contracts

> ADR document set: **v0.1.49**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-04-API
- Subsystem: factions / relations
- C++ owner: `CScriptGameObject`, forwarding to inventory-owner mutation or stalker flags
- Lua owner: `game_object`
- Interface kind: selected Lua exports; native `RELATION_REGISTRY::Action` is not established as a Lua action API here
- Baseline: ENGINE1011; [provenance](../../00-environment/source-baseline-2026-10-11.md)
- Source status: source-confirmed within selected declarations/registrations/bodies
- Runtime status: untested; deferred until explicitly resumed by the user
- Build/conditional scope: inspected registration bodies; no exhaustive build projection
- Native versus registered Lua inheritance: receiver casts below, not an exhaustive inheritance map
- Example status: none
- Last reviewed: 2026-10-11

A-labels refer to the [FAC-04 ledger](../../evidence/factions/action-goodwill-2026-10-11.csv). The [action reference](../../04-game-systems/factions/action-goodwill.md) separates native outcomes, clocks, contributions and online/offline policy.

## Numerical values

| Lua method | Exact selected native signature / result | Receiver and mutation/read contract | Evidence |
| --- | --- | --- | --- |
| `obj:character_rank()` | `int CharacterRank()` | Base-monster receiver has a special rank getter; otherwise inventory-owner getter. Unsupported type logs/returns 0; zero is not a success indicator | A08 `940–956`; A09/A10 |
| `obj:set_character_rank(value)` | `void SetCharacterRank(int)` | Inventory-owner receiver required; forwards absolute value to `SetRank`, with server lookup/trader gates | A07/A08/A09/A10 |
| `obj:change_character_rank(delta)` | `void ChangeCharacterRank(int)` | Inventory-owner receiver required; add delta to current rank then use setter. Does not call action/reward policy | A07/A08/A09/A10 |
| `obj:character_reputation()` | `int CharacterReputation()` | Inventory-owner receiver; unsupported receiver logs/returns 0 | A08/A09/A10 |
| `obj:set_character_reputation(value)` | `void SetCharacterReputation(int)` | Inventory-owner receiver; forwards absolute value to server-backed setter | A07/A08/A09/A10 |
| `obj:change_character_reputation(delta)` | `void ChangeCharacterReputation(int)` | Inventory-owner receiver; add delta then use setter. Not a synthetic kill/help event | A07/A08/A09/A10 |

The getter's monster special case does not make the inventory-owner mutation wrappers a universal monster-rank API. Mutation receiver failure logs/returns; deeper setters assert alive-entity casts and require a matching server trader before writing both client and server values. Return type is void, not a reliable success result. No numeric clamp occurs in the selected rank/reputation setters; goodwill clamp rules are different. A07/A08.

These are scalar value operations on borrowed live objects. No ownership transfer, object creation or campaign identity validation is established. Converter behavior, optional arguments, arbitrary values and all derived mutation overrides remain unaudited. Object lifetime must follow the [A-Life reference](../../04-game-systems/alife/lifecycle-state-reference.md).

## Relation flags

| Lua method | Exact selected signature | Contract |
| --- | --- | --- |
| `obj:get_actor_relation_flags()` | `Flags32 get_actor_relation_flags() const` | Stalker receiver required via `THROW`; returns its flag value |
| `obj:set_actor_relation_flags(flags)` | `void set_actor_relation_flags(Flags32)` | Same stalker requirement; directly replaces flags without running action policy |

A09/A10/A14. The exact Flags32 converter/userdata surface is outside this pass. Construction zeroes the flags. Registered enum labels include `relation_attack`, `relation_fight_help_human`, `relation_fight_help_monster`, and `relation_kill`; literal native values are 1, 2, 4 and 0 respectively. The selected action code calls mask `set(action,TRUE)`, whose zero mask does not add a kill bit. These flags are not an event count or reliable award receipt. A03/A09/A15/A18/A20.

For stalker targets the flag attempt precedes the actor attack throttle and outcome gates. A flag write does not certify that reputation, rank or community goodwill changed. A03/A04.

## Native actions and callback observation

Selected hit entry registers a fight before invoking ATTACK; the actor branch assumes a fight pointer and has no local null check before using it. Direct arbitrary action calls are not documented as safe. KILL in selected live Die occurs before inherited death and the object-bound death callback, but the installed death/cleanup chains and script listeners may add policy. No shared “award complete” callback is established here. A01–A04.

Rank/reputation setters invoke actor Discord display helpers when applicable; those helpers read script producers. They do not establish PDA refresh, Warfare bookkeeping or CtZ casualty persistence. A07/A13.

## Checks and open work

Compared signatures, argument/receiver mapping, selected registrations, scalar mutation gates, flag masks and callback phase. Verified pinned hashes, counts, ranges and symbols. No runtime tests or gameplay edits. Effective settings, additional native/derived award paths, online/offline script policy and numeric converter behavior remain unverified. [Investigation](../../08-research/investigations/2026-10-11-FAC-04-action-goodwill.md), [verification](../../08-research/verification-2026-10-11-v0.1.47.md).
