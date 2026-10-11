# INV-008 — XML registration and font-manager lifecycle

> ADR document set: **v0.1.41**. Research revisions and source/build versions below describe their original scope.

Status: **Open / partially documented**. Target commit `6a08e0905ce34748ee2904a5e0809f8afd141137`. Runtime deferred.

## Source-supported findings

- `CUIXmlInit` header declares native static initializer methods and its constructor.
- Its source constructor calls `InitColorDefs`, not a demonstrated font setup call.
- `InitText`/`InitFont` provide the XML-to-font-pointer resolution path.

## Search limits

No successful historical whole-repository Luabind registration search or font-manager startup/shutdown trace was completed. Guessed script-binding filenames were absent (404) and do not establish the absence of a feature.

## Research queue

1. Obtain pinned source checkout and grep all class registrations and `GetFont*` global exports.
2. Trace UI core font creation and resource teardown, with exact line citations.
3. Reconcile registered Lua XML wrappers with GAMMA's Lua libraries.
4. Revisit CtZ crash and perform runtime checks only when user has access to PC.

No executable Lua examples added.
