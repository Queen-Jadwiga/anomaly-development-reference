#!/usr/bin/env python3
"""Read-only source inventory for ADR A-01/A-02. Produces leads, not proof of absence."""
import argparse
import pathlib
import re
import subprocess

PATTERNS = {
    "CScriptXmlInit registration or reference": re.compile(r"CScriptXmlInit\s*::\s*script_register|\bCScriptXmlInit\b"),
    "Native class registration candidate": re.compile(r"class_\s*<\s*(?:[\w:]+::)?CUIXmlInit\s*>|\bCUIXmlInit\s*::\s*script_register|[\"']CUIXmlInit[\"']"),
    "Registration aggregators / imports": re.compile(r"script_register|script_type_list|add_to_type_list|lua_State|luabind::module"),
}
EXTENSIONS={".cpp",".cc",".cxx",".h",".hpp",".inl",".inc",".lua",".script"}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("checkout",type=pathlib.Path)
    p.add_argument("--max-matches",type=int,default=1000)
    a=p.parse_args(); root=a.checkout.resolve()
    if not (root/".git").exists(): p.error("Expected a Git checkout with .git; a standalone source directory is not enough to verify commit provenance")
    commit=subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"],text=True).strip()
    files=[f for f in (root/"src").rglob("*") if f.is_file() and f.suffix.lower() in EXTENSIONS]
    print(f"# Lua registration audit — commit `{commit}`")
    print(f"Files scanned: {len(files)}; scope: src/**/* with extensions {sorted(EXTENSIONS)}")
    print("Search is lexical, case-sensitive, and cannot prove absence of indirect/dynamic registrations.\n")
    for label, pattern in PATTERNS.items():
        print(f"## {label}")
        n=0
        for file in files:
            try: lines=file.read_text(encoding="utf-8",errors="replace").splitlines()
            except OSError: continue
            for lineno, line in enumerate(lines,1):
                if pattern.search(line):
                    if n<a.max_matches: print(f"- `{file.relative_to(root)}:{lineno}`: `{line.strip()[:200]}`")
                    n+=1
        print(f"Total matching lines: {n}\n")

if __name__=="__main__":main()
