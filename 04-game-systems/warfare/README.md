# Warfare subsystem — research WAR-001

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
