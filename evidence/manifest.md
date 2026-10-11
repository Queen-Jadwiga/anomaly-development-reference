# Evidence manifest

## Runtime logs (user-provided in prior Anomaly project conversations)

| ID | File | Supported facts | Limitations |
|---|---|---|---|
| LOG-001 | `xray_erik(20261008-031926).log` | Startup version header | Full font crash trace not yet reproduced in ADR |
| LOG-002 | `xray_erik(20261009-005123).log` | Startup version header | Does not pin Git commit |
| LOG-003 | `xray_erik(20261009-100733).log` | Startup version header | Does not pin Git commit |

## Web sources

| ID | URL | Supports |
|---|---|---|
| WEB-001 | https://github.com/themrdemonized/xray-monolith | Current project lineage, MT-TEST explanation, dated upstream change history |
| WEB-002 | https://github.com/themrdemonized/xray-monolith/releases | Public release history (release-tag matching pending) |
| WEB-003 | https://github.com/bergemon/xray-monolith-anomaly | Alternative fork, not assumed identical |

All version-sensitive engine documentation must cite an exact revision once identified.
