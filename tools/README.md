# Research and documentation tools

| Tool | Purpose | Requirements / scope |
| --- | --- | --- |
| [check_repository.py](check_repository.py) | Check local Markdown targets/anchors, root containment and required entry navigation | Python 3; no network or engine execution |
| [build_alife_catalog.py](build_alife_catalog.py) | Rebuild scoped native/Lua classes, bindings, helper/script declarations and source ledger | Python 3 + `cpp`; explicit source roots; two XRGAME_EXPORTS projections, not compilation |
| [audit_xml_lua_registrations.py](audit_xml_lua_registrations.py) | Historical read-only XML/Lua registration audit | See tool and [source audit commands](source-audit-commands.md); bounded search |

Run `python tools/check_repository.py` from the repository root (or any working directory with the tool path). Rebuild the A-Life catalog with `python tools/build_alife_catalog.py --source-root /path/to/xray-monolith-2026.10.11 --warfare-root /path/to/beta150`; output defaults to this repository. Use `--repo-root` for an isolated output directory.

Record actual checks in the increment's verification record. Generated output belongs in canonical API/evidence folders. Inputs are not redistributed. Lua/XML/asset/log validators beyond these tools remain future work; no general engine compiler or gameplay harness is provided.
