# PDA architecture — investigation PDA-001

> ADR document set: **v0.1.41**. Research revisions and source/build versions below describe their original scope.

**Current state:** Source research is underway. No assertion yet that a new PDA tab can be registered using only the May 2026 Lua API.

## Questions to resolve

1. Which C++ objects own the PDA screen and its tabs/pages?
2. What Lua APIs expose PDA windows and UI event routing?
3. How do existing GAMMA scripts decorate or override PDA windows?
4. Which keyboard/mouse handlers require careful event propagation?
5. How are UI elements destroyed and how does Lua GC affect native ownership?

## Research trail

- Engine source: https://github.com/themrdemonized/xray-monolith
- Public changelog describes PDA-oriented enhancements, but every entry must be dated against 2026-05-15 before adoption.

**Capture the Zone implication:** Prefer known native widget construction and existing PDA extension points. Avoid engine modifications unless verified stock hooks cannot support the design.
