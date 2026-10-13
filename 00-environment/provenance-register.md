# ADR provenance register

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

- ID: ADR-01-PROVENANCE
- Research revision: v0.1.82
- Source status: audit of existing artifact/commit/report distinctions; no new binary equivalence claim
- Runtime status: earlier audit deferred; October 12 user log observed, independent tests now authorized and untested
- Baseline: ADR v0.1.81 `dc826c78041971cac96710b329b6ce85905e8e13`
- Last reviewed: 2026-10-12

Use this register to distinguish inspected source, runtime candidates and observations. It consolidates the existing records; it does not replace their file/line/guard evidence or establish that an addon wins in the installed profile. [Whole-reference status](../08-research/reference-status.md), [audit evidence](../evidence/reference/README.md).


| Identity | Existing pin/evidence | Role and limit |
| --- | --- | --- |
| ENGINE1011 | Uploaded source archive SHA-256 `withheld-upload-fingerprint` | Preferred selected native/bundled source; upstream commit and exact executable correspondence unknown |
| BETA150 | Uploaded archive SHA-256 `withheld-upload-fingerprint` | Main and explicitly identified optional Warfare variants; no installed winner inferred |
| ZIP142 | Uploaded archive SHA-256 `withheld-upload-fingerprint` | Alternative supplied Warfare package; equal files/slices do not certify profile equivalence |
| CTZ005J | Commit `eba6660db09353dcc42a195ae6e7e706f4762277`, Alpha 0.0.5j | Selected campaign source pin; internal VERSION/SAVE_VERSION are separate; not a claim about current mod HEAD |
| Historical May UI source | Commit `6a08e0905ce34748ee2904a5e0809f8afd141137`, tag 2026.5.15 | Existing scoped UI extraction/declaration research; original short-pin intake record is historical, binary match unknown |
| UPSTREAM0912 | Commit `9b491ffbfe5d529e817ceffed70214d0f03f62c5`, tag 2026.9.12 | Four selected September comparison files; retained remote hashes, no local September rehash in ADR-01 |
| October binary archive | SHA-256 `withheld-upload-fingerprint` | Uploaded runtime adoption candidate; archive identity does not prove installed executable identity/testing |
| ENV-001 user logs | Historical May 15 MT-TEST/xrCore 9959 startup observations | User's recorded installation at that time; no executable hash or proof of later adoption |
| ENV-RT01 external reports | Issue/reporter/timestamp/body hashes and reported September setup | External UI/clock/string/header observations; neither the user's installation nor independent ADR reproduction |
| ADR reference pins | Immutable repository revisions in documentation inventories | Pin documentation/test-source bytes; not engine builds, feature-introduction versions or game schemas |

Authority: [manifest](../evidence/manifest.md), [October baseline](source-baseline-2026-10-11.md), [historical installed record](engine-version.md), [May source intake](source-baseline-2026-05-15.md), [historical UI extraction](../02-lua-api/ui/README.md), [reported runtime](reported-gamma-runtime-2026-10-12.md), [persistence evidence](../evidence/persistence/README.md) and [REV-01](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md). No dates/tags are promoted to invented commits or binary hashes.

Legacy ledger labels such as a full engine archive name, “October 11 uploaded engine archive”, BETA150-main or a CtZ commit description retain their original schema. The audit maps those existing labels only for integrity checks; it does not rewrite them. BETA150-main remains distinguished from optional patches while sharing BETA150's artifact. [Ledger classification](../evidence/reference/ledger-integrity-2026-10-12.csv).

Source-file hashes/ranges are rechecked where the original uploaded/pinned source is available. Generated inventories, historical May extraction, package comparisons and external reports retain their original projection/qualification; full regeneration or new runtime observations are not claimed. Feature availability remains version-specific: October labels identify inspected scope rather than a universal introduction/minimum version. [Evidence policy](../08-research/evidence-policy.md), [effective-profile requirements](../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md).
