# Engine architecture — first-pass map

> ADR document set: **v0.1.46**. Research revisions and source/build versions below describe their original scope.

**Status:** Architectural research outline; exact files and bindings pending source checkout at a pinned commit.

The Anomaly distribution uses the X-Ray engine with community Modded Exes. At a high level, distinguish the native C++ runtime, scripting bindings, Lua gameplay scripts, configuration and UI layout files, and packaged assets. Runtime behavior can depend on interactions across all layers.

```text
Installed game executable and native modules (C++)
    ↕ exposed native/Lua bindings + callbacks
Anomaly / GAMMA Lua scripts
    ↕ configuration, UI objects, state
LT(X), XML, textures, audio, saved data
```

This is a *conceptual* diagram, not an exhaustive list of dynamically loaded modules.

## Research targets

| Area | Need to establish | Evidence needed |
|---|---|---|
| Engine initialization | Subsystem order and log banner construction | Pinned source paths and actual log excerpts |
| Lua interfaces | Registration and binding declarations | C++ definitions in correct revision |
| UI framework | Creation, ownership, lifetime and callbacks | Native C++ and representative Lua usage |
| PDA | Where PDA pages / windows are constructed | Exact source path plus GAMMA override source |
| A-Life | Online/offline simulation and squad events | Native and script traces |
| Warfare | Faction/territory control, state transitions | GAMMA scripts, save schema and runtime tests |

**Do not equate `source-confirmed` with `available to Lua`:** native class existence is insufficient. Look for a binding/export and confirm supported constructor signatures.

## Integrated UI architecture (v0.1.10)

See [Lua → XML factory → native widget and font lifecycle](ui-lua-native-integration.md).
