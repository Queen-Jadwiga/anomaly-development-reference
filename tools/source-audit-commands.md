# Reproducible pinned checkout and audit

> ADR document set: **v0.1.65**. Research revisions and source/build versions below describe their original scope.

```bash
git clone https://github.com/themrdemonized/xray-monolith.git
cd xray-monolith
git checkout 2026.5.15
git rev-parse HEAD
git ls-tree -r --name-only HEAD > source-files.txt
git grep -n -E 'CUIXmlInit|script_register|GetFontSmall|CGameFont' -- src > initial-symbol-hits.txt
```

Do not interpret zero hits unless the checkout is complete and the searched paths exist. Check tag-to-SHA correspondence; avoid current `main` when building the May 2026 API catalog. Save the search results separately from licensed source code.
