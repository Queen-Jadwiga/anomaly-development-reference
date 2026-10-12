# Research and documentation tools

> ADR document set: **v0.1.62**. Research revisions and source/build versions below describe their original scope.

| Tool | Purpose | Requirements / scope |
| --- | --- | --- |
| [check_repository.py](check_repository.py) | Check local Markdown targets/anchors, root containment and required entry navigation | Python 3; no network or engine execution |
| [build_alife_catalog.py](build_alife_catalog.py) | Rebuild scoped native/Lua classes, bindings, helper/script declarations and source ledger | Python 3 + `cpp`; explicit source roots; two XRGAME_EXPORTS projections, not compilation |
| [audit_xml_lua_registrations.py](audit_xml_lua_registrations.py) | Historical read-only XML/Lua registration audit | See tool and [source audit commands](source-audit-commands.md); bounded search |

Run `python tools/check_repository.py` from the repository root (or any working directory with the tool path). Rebuild the A-Life catalog with `python tools/build_alife_catalog.py --source-root /path/to/xray-monolith-2026.10.11 --warfare-root /path/to/beta150`; output defaults to this repository. Use `--repo-root` for an isolated output directory.

Record actual checks in the increment's verification record. Generated output belongs in canonical API/evidence folders. Inputs are not redistributed. Lua/XML/asset/log validators beyond these tools remain future work; no general engine compiler or gameplay harness is provided.

The repository checker also validates `VERSION` against current Markdown banners, rejects forwarding pages and empty files, and checks CSV row widths. The A-Life generator writes LF line endings to reproduce the published catalogs byte for byte.

[binding_patterns.py](binding_patterns.py) contains shared registration-form/category/origin recognition used by the catalog builder and its property regression tests. The catalog now indexes `.property` with preserved accessor expressions; it does not infer a method signature or generalized setter policy.
