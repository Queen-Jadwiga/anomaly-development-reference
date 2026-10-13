#!/usr/bin/env python3
"""Bounded public-content guard; never prints matched private values."""
from pathlib import Path
import json,re

RULES={
    'personal-game-log-name':re.compile(r'\bxray_[a-z0-9_-]+\([^)]*\)\.log\b',re.I),
    'local-windows-user-or-game-path':re.compile(r'\b[a-z]:[\\/](?:users|games)[\\/]',re.I),
    'local-home-or-scratch-path':re.compile(r'/(?:home|Users|workspace|mnt/data)/'),
    'published-private-intake-fingerprint':re.compile(r'\|\s*PRIVATE-(?:SOURCE|LOG|PROFILE)\s*\|\s*`[a-f0-9]{64}`',re.I),
    'published-personal-binary-fingerprint':re.compile(r'Reported executable SHA-256:\s*`[a-f0-9]{64}`',re.I),
}
def violations(text):
    return [name for name,pattern in RULES.items() if pattern.search(text)]
def check(root):
    errors=[];checked=0
    for path in sorted(root.rglob('*')):
        if not path.is_file() or '.git' in path.parts or '__pycache__' in path.parts or path.suffix not in {'.md','.csv','.json','.txt','.xml','.ini','.py'}:continue
        checked+=1
        for rule in violations(path.read_text()):errors.append({'path':path.relative_to(root).as_posix(),'rule':rule})
    return {'files_checked':checked,'errors':errors,'limits':'Pattern guard only; manual review remains required.'}
if __name__=='__main__':
    result=check(Path(__file__).resolve().parents[1]);print(json.dumps(result,indent=2));raise SystemExit(bool(result['errors']))
