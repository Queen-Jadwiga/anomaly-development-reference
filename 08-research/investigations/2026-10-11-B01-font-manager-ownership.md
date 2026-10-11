# B-01 — ownership of UI font manager and named font pointers

> ADR document set: **v0.1.42**. Research revisions and source/build versions below describe their original scope.

**Baseline:** X-Ray Monolith `2026.10.11`, source archive supplied by user. **Status:** source research complete; runtime deferred. **Scope:** ownership, not entire engine initialization chronology (B-02).

## Verified ownership chain

1. `UI()` returns `*GamePersistent().m_pUI_core` in [`ui_base.cpp`, lines 6–7](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_base.cpp#L6-L7). This identifies the UI core accessed by game code.
2. The `ui_core` type has a `CFontManager* m_pFontManager` member, and `Font()` returns `*m_pFontManager`, in [`ui_base.h`, lines 52–75](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_base.h#L52-L75).
3. `ui_core` constructs that manager with `xr_new<CFontManager>()` for the **non-dedicated-server** branch, otherwise sets the pointer to `NULL`, in [`ui_base.cpp`, lines 213–224](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_base.cpp#L213-L224). `ui_core::~ui_core()` deletes it using `xr_delete` in [lines 234–238](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_base.cpp#L234-L238).
4. `CFontManager` declares named `CGameFont*` fields and a vector of **addresses of those pointer fields** (`xr_vector<CGameFont**>`) in [`ui_base.h`, lines 20–49](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_base.h#L20-L49). The vector itself does not contain font objects.
5. Its constructor stores addresses of the named pointers, initializes them to `NULL`, and calls `InitializeFonts()` in [`HUDManager.cpp`, lines 31–53](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/HUDManager.cpp#L31-L53). `InitializeFont` allocates `xr_new<CGameFont>` if absent or reinitializes the existing object otherwise in [lines 73–85](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/HUDManager.cpp#L73-L85).
6. `CFontManager::~CFontManager()` unregisters the reset listener and `xr_delete`s each font through its stored pointer address, in [`HUDManager.cpp`, lines 88–95](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/HUDManager.cpp#L88-L95).

**Conclusion:** In the normal client UI path, `ui_core` owns its `CFontManager`, which owns the named `CGameFont` instances. `UI().Font().pFont…` accesses manager-owned pointers; it does **not** transfer ownership to widgets or Lua.

## Limits / next work

- This B-01 conclusion is limited to the named manager fonts. Other fonts exist (e.g. engine application or console fonts) with separate owners; do not generalize this manager to **all** `CGameFont` objects.
- No runtime test was performed. Do not infer what exactly caused the previous CtZ font crash.
- **B-02** remains open: trace creation and destruction of `ui_core` itself, initialization ordering and device-reset behavior across the wider engine.
- The dedicated server branch has a null font manager; `Font()` directly dereferences the manager pointer, so do not assume it is safe there.
