# Warfare subsystem

**Current revision: v0.1.35.**

**Current evidence:** Capture the Zone is intended to extend Anomaly/GAMMA Warfare, including PDA strategy display and tracking faction control.

## Topics and questions

- Faction identifiers, faction relation state, ownership of smart terrains.
- Squad lifecycle and offline/online transitions.
- Territory capture events and their available callbacks.
- Whether current state and history are serialized; save and load boundaries.
- Interaction with other Warfare/CtZ mods and MO2 override priority.

## Needed source material

Exact GAMMA Warfare scripts from the active profile, any Warfare-overriding mods, and relevant save/log examples. Do **not** treat generic Anomaly scripts on the web as authoritative for a heavily modded GAMMA profile.

## Initial deliverable

A call graph connecting faction state -> squad/smart-terrain logic -> event source -> CtZ UI update, each edge labeled with evidence and version.

## v0.1.31 — First source boundary established

- [Native A-Life identity and lifecycle](../alife/identity-lifecycle-oct11.md).
- [WAR-001: CtZ call sites and missing effective-profile dependencies](ctz-integration-boundary-oct11.md).

The October 11 archive includes `sim_squad_scripted.script` and selected native bindings, but does not provide the referenced board/smart/Warfare policy implementations. Faction capture and effective GAMMA override behavior remain open. In-game verification is deferred by user request.

## v0.1.33 — Supplied package policy traced

- [WAR-002a: two Warfare packages, pinned public GAMMA comparison and effective-profile source requirements](source-packages-effective-profile-oct11.md).
- [WAR-002b: target/arrival distinction, ownership policy, callbacks and offline combat](warfare-policy-offline-combat-oct11.md).
- [Source locations and hashes](source-evidence-war002-oct11.csv).
- [Archive script byte comparison](archive-script-comparison-oct11.csv).

Supplied package implementations are now inspected. Current MO2 winning files and runtime function overrides remain unverified; this supersedes the earlier missing-package status without changing its historical findings. Runtime tests remain deferred.

## v0.1.34 — Persistence boundary

[Native save/load and CtZ campaign reconstruction](../alife/save-load-identity-oct11.md) distinguishes saved campaign records, squad packet fields and late member-pointer repair. Effective storage wrappers and ownership synchronization remain open; runtime deferred.

## v0.1.35 — Movement versus combat update authority

[ALIFE-05](../alife/offline-scheduling-brains-oct11.md) traces the native scheduled task/movement flow and Lua squad task handoff. Native scheduling, Lua arrival policy and the supplied offline-combat coordinator are separate mechanisms; installed overrides and runtime remain deferred.
