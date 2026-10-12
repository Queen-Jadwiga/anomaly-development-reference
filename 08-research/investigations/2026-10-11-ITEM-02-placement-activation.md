# ITEM-02 — Placement and active-item transitions

> ADR document set: **v0.1.64**. Research revisions and source/build versions below describe their original scope.

- ID: ITEM-02
- Subsystem: inventory
- ADR revision: v0.1.55
- Record status: complete-within-scope
- Source status: source-confirmed selected native/actor paths
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline: ENGINE1011; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-11

## Question and scope

How do slot/belt/ruck eligibility and movement differ from ownership and activation, and what do callbacks/Lua requests establish for equipment work? Include selected placement predicates/mutators, owner/stalker predicate boundary, callback guards/phases, server-only activation/Update and minimal HUD state producers, Lua declarations/registrations, server routing and actor consumers. Exclude exhaustive NPC consumer/AI selection, weapon/animation mechanics, blocking restoration internals, persistence/consumption and runtime.

## Evidence and method

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit/binary/profile correspondence unknown. [P01–P19 ledger](../../evidence/inventory/placement-activation-2026-10-11.csv) records original-file hashes/counts/ranges/symbols. Read methods, declarations/defaults, predicates, callback sites/compile guards, event payload producers/actor consumers and current/next Update transitions. NPC applicability remains an explicit gap rather than inferred from game_object export names.

## Findings

[Reference](../../04-game-systems/inventory/placement-activation.md) and [API contracts](../../02-lua-api/inventory/placement-api.md) carry nearby P-citations.

- Normal eligibility, strict placement and ownership are separate; base/stalker owner predicates differ. P01–P03/P14–P16.
- Slot/ruck callbacks precede placement metadata update, belt callback follows it; conditional enum producers do not give a uniform settled snapshot. P01/P02/P06/P12/P13.
- Server activation distinguishes next/current slot and hidden/HUD/block gates. Changed-slot functor is in selected Update, not every forced path, and not inherently a weapon-readiness event. P04/P05/P17–P19.
- Lua void methods send sequences; slot producer preflight is commented, third doNotActivate argument explicit, actor consumer checks/rejects independently. Effective NPC operation remains unverified. P07–P11/P14.

## Competing explanations and missing edges

Installed NPC/loadout scripts can use different native/AI policies rather than these player-event helpers. Derived items may change activation behavior. Delays, successful request sends or slot callbacks cannot substitute for established actor/NPC consumer/readiness evidence. No runtime failure or working NPC recipe is claimed.

## Checks and outcomes

Verify hashes/counts/ranges/symbols, argument/default/registration/payload alignment, callback/state ordering, prior evidence/history preservation, navigation/version/tests and publication tree/readbacks. [Increment verification](../verification-2026-10-11-v0.1.55.md). No runtime/gameplay/save/source edits, engine build, redistributed source/assets or license.

## Disposition and next work

ITEM-02 focused equipment foundation complete within scope; inventory remains partial. Relevant to CtZ loadout reasoning, but NPC AI/readiness is not certified. Next consumption/destruction/owner cleanup, then item persistence and consolidation; runtime deferred. [Roadmap](../../ROADMAP.md).
