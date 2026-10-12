# CONFIG-03 — Native script loading, startup and shared callbacks

> ADR document set: **v0.1.76**. Research revisions and source/build versions below describe their original scope.

- ID: CONFIG-03
- Subsystem: configuration/script integration
- ADR revision: v0.1.76
- Record status: complete-within-scope; effective installed integration partial
- Source status: source-confirmed selected ENGINE1011 native/bundled contracts; scoped-source-audit for filename availability
- Runtime status: untested; deferred
- Baseline IDs and provenance: ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; [baseline](../../00-environment/source-baseline-2026-10-11.md), [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and scope

How do native initialization, ordinary .script autoload, namespace/function lookup, compile/execute/reset, root module startup and selected shared callback registration/removal/order/mutation/return contracts connect? Trace native callers, loader/environment, prefetch registration, axr_main and _g_patches iterator/global assignments, DXML's adjacent registration pass and debug-global loader. Reuse ALIFE-10 and build-comparison evidence. Closure requires definitions/callers/registrations and failure/lifetime limits; it does not require the absent effective startup/storage/binder configuration or runtime tests.

## Evidence and method

[35-row source ledger](../../evidence/configuration/script-loading-callbacks-2026-10-12.csv) N01–N22/S01–S13 pins 14 files/47 inclusive range groups. Read initialization/reset callers, normal/debug loaders, environment headers, namespace/functor checks, local compile/execute failures, registry/order/removal/dispatch bodies and selected spairs heap implementation. Inspect filename enumeration definitions/backing set and scoped missing global/configuration inputs. [Scope JSON](../../evidence/configuration/script-source-scope-2026-10-12.json) inventories exact requested filenames within 161 ENGINE1011 gamedata files; it is not a negative installed-functionality claim.

The uploaded archive's exact upstream commit/executable/profile equivalence remains unknown. Existing September/October dispatcher comparison and externally observed startup/loading issues retain independent provenance and confidence; no fresh web/version assertion or runtime observation is made. Earlier evidence ledgers and inventory pins remain immutable.

## Findings

The [behavior reference](../../04-game-systems/configuration/script-loading-startup-callbacks.md) separates VM reconstruction, quiet missing-name cache, existing-table namespace predicate, ordinary .script autoload, injected environment, configured registrators/common initializer and simulator start callback before load. A failed chunk can leave partial effects and a namespace table; process_file/prefetch do not propagate a success receipt. Root startup discovers/evaluates modules first and calls handlers in a second direct pass. Dependency loading can alter evaluation order independently of enumeration. N01–N21/S08/S12/S13.

The [API page](../../02-lua-api/configuration/script-callback-api.md) preserves native-only versus exported prefetch, exact namespace/function resolution, listener identity, private dependency copies, hard tiers/topological fallback, re-registration rollback, userdata-specific scrubbing, ignored returns and no local protected-call/reentry guard. Actual spairs in the available patch snapshots keys while retaining live value/priority reads; this qualifies dispatch mutation beyond the previously scoped make_callback body. S01–S10.

Storage reinit has an explicit lua_debug-enabled global loading route for dynamic_callbacks.lua, separate from .script autoload and before later _G/module assignments. That file contains **five** event names and uses pairs without axr_main tiers. N04/N17/N22/S11. Prior WORLD-04 C12 and CONFIG-01 K08 six-name wording was incorrect; current references are amended and old CSV bytes retained. The newly traced conditional route strengthens file-presence-only knowledge without establishing the final installed global aliases.

## Competing explanations and missing edges

Namespace existence is weaker than completed module execution; registration priority is weaker than native readiness; handler discovery is not whole-profile execution order. Comments about pruning unused events during on_game_load lack an active implementation in the inspected axr_main body. A key snapshot is not a frozen listener/order snapshot, and graph-registration rollback is not gameplay rollback. Debug-only global wrapper installation does not make the small dispatcher equivalent to axr_main or supply all generic events.

Available ENGINE1011 gamedata lacks exact _g.script/script.ltx/bind_actor.script filenames, while axr_main/_g_patches/global.lua/dynamic_callbacks.lua are present. The configured start callback body, core global Send/Unregister route to axr_main, post-load/storage emitter, actual helper winner and later patch order remain effective gaps. Unlocalizer directive/consumer depth belongs to CONFIG-04; exhaustive VM/error/security/addon behavior remains optional. No comment or source filename certifies installed compatibility.

## Checks and outcomes

Validate raw hashes/counts and 47 cited ranges/symbols for all 35 rows; reproduce scoped filename hashes/event-name extraction and original CONFIG-01 documentation pins. Review native/script-layer mapping and correction scope. Preserve earlier evidence/history/generated/tool/test bytes and dated investigation bodies except synchronized banners; run repository validation and the 10 existing regression tests. [Verification](../verification-2026-10-12-v0.1.76.md). Compare complete remote base/staged/published path/blob maps with expected-head update. No engine compilation or independent game tests.

## Disposition and next work

CONFIG-03 closes the selected source pass. Configuration/script integration remains partial. **Next CONFIG-04 — supplied options/patch consumers, consolidation and bounded audit.** [Guide](../../04-game-systems/configuration/development-reference.md), [completion status](../../04-game-systems/configuration/source-completion-status.md), [roadmap](../../ROADMAP.md). Runtime remains deferred; no CtZ gameplay or third-party source/assets changes.
