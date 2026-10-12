"""Check local Markdown targets/anchors and the required ADR entry points.

Run from any working directory: python tools/check_repository.py [--root PATH]
This is a structural check, not source interpretation or game verification.
"""
import argparse,csv,json,re,sys,unicodedata
from pathlib import Path
from urllib.parse import unquote,urlsplit

def prose(text):
    lines=[]; fence=None
    for line in text.splitlines():
        m=re.match(r'^\s*(`{3,}|~{3,})',line)
        if m:
            marker=m.group(1)[0]
            if fence is None:fence=marker
            elif fence==marker:fence=None
            continue
        if fence is None:lines.append(line)
    return '\n'.join(lines)

def headings(text):
    result=set();counts={}
    for m in re.finditer(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$',prose(text),re.M):
        value=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',m.group(1)).lower()
        value=''.join(c for c in value if c in '_- ' or unicodedata.category(c)[0] in 'LN')
        value=value.replace(' ','-')
        count=counts.get(value,0);counts[value]=count+1
        result.add(value+('-'+str(count) if count else ''))
    result.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']',text))
    return result

def check(root):
    root=root.resolve();errors=[];links=0;anchors=0
    files=sorted(p for p in root.rglob('*.md') if not any(x.startswith('.') for x in p.relative_to(root).parts))
    texts={p:p.read_text(encoding='utf-8') for p in files}
    ids={p:headings(t) for p,t in texts.items()}
    for path,text in texts.items():
        clean=prose(text)
        # A valid target can still have a misleading explicit verification revision label.
        for label,raw in re.findall(r'\[([^\]\n]+)\]\(([^\s)]+)(?:\s+"[^"]*")?\)',clean):
            url=urlsplit(raw.strip('<>'))
            if url.scheme or url.netloc:continue
            report=re.fullmatch(r'verification-\d{4}-\d{2}-\d{2}-v(\d+\.\d+\.\d+)\.md',Path(unquote(url.path)).name)
            versions=set(re.findall(r'\bv(\d+\.\d+\.\d+)\b',label))
            if report and len(versions)==1 and report.group(1) not in versions:
                errors.append(f'{path.relative_to(root)}: verification revision label mismatch: {label} -> {raw}')
        targets=re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)',clean)
        targets+=re.findall(r'^\s*\[[^]]+\]:\s*(\S+)',clean,re.M)
        for raw in targets:
            raw=raw.strip('<>');url=urlsplit(raw)
            if url.scheme or url.netloc:continue
            if not url.path and not url.fragment:continue
            target=(path.parent/unquote(url.path)).resolve() if url.path else path
            try:target.relative_to(root)
            except ValueError:errors.append(f'{path.relative_to(root)}: target escapes repository: {raw}');continue
            links+=1
            if not target.exists():errors.append(f'{path.relative_to(root)}: missing target: {raw}');continue
            if url.fragment and target.suffix=='.md' and target in ids:
                anchors+=1
                if unquote(url.fragment) not in ids[target]:errors.append(f'{path.relative_to(root)}: missing anchor: {raw}')
    required=['README.md','INDEX.md','ROADMAP.md','CHANGELOG.md','CONTRIBUTING.md','AGENTS.md','08-research/workflow.md','08-research/repository-layout.md','08-research/evidence-policy.md','02-lua-api/api-index.md','02-lua-api/ui/README.md','02-lua-api/alife/README.md','08-research/templates/investigation.md','02-lua-api/templates/api-entry.md']
    for rel in required:
        if not (root/rel).is_file():errors.append('missing required entry: '+rel)
    version_path=root/'VERSION'
    version=version_path.read_text().strip() if version_path.is_file() else ''
    if not re.fullmatch(r'0\.1\.\d+',version):errors.append('missing or invalid VERSION')
    for path,text in texts.items():
        rel=path.relative_to(root).as_posix()
        if text.startswith('# Moved:'):errors.append('obsolete forwarding page: '+rel)
        if '/history/' not in rel:
            expected=f'> ADR document set: **v{version}**.'
            if text.count(expected)!=1:errors.append('missing/inconsistent document-set version: '+rel)
            for value in re.findall(r'Current (?:ADR )?revision:\s*\*{0,2}(v\d+\.\d+\.\d+)',text):
                if value!='v'+version:errors.append('stale current revision: '+rel+': '+value)
    for path in root.rglob('*'):
        if not path.is_file() or any(x.startswith('.') for x in path.relative_to(root).parts):continue
        if path.stat().st_size==0:errors.append('empty repository file: '+path.relative_to(root).as_posix())
        if path.suffix=='.csv':
            with path.open(encoding='utf-8',newline='') as stream:
                rows=list(csv.reader(stream))
            if not rows:errors.append('empty CSV: '+path.relative_to(root).as_posix())
            elif any(len(row)!=len(rows[0]) for row in rows[1:]):errors.append('CSV row width mismatch: '+path.relative_to(root).as_posix())
    landing=texts.get(root/'README.md','')
    for token in ['2026-10-11-C03-luabind-adoption-autodelete.md','2026-10-11-C04-xml-factory-return-ownership.md','https://github.com/Queen-Jadwiga/capture-the-zone']:
        if token not in landing:errors.append('landing page missing navigation: '+token)
    return {'version':version,'markdown_files':len(files),'local_targets_checked':links,'anchors_checked':anchors,'errors':errors}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);args=parser.parse_args()
    result=check(args.root);print(json.dumps(result,indent=2));return 1 if result['errors'] else 0

if __name__=='__main__':sys.exit(main())
