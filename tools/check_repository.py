"""Check local Markdown targets/anchors and the required ADR entry points.

Run from any working directory: python tools/check_repository.py [--root PATH]
This is a structural check, not source interpretation or game verification.
"""
import argparse,json,re,sys,unicodedata
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
    landing=texts.get(root/'README.md','')
    for token in ['2026-10-11-C03-luabind-adoption-autodelete.md','2026-10-11-C04-xml-factory-return-ownership.md','https://github.com/Queen-Jadwiga/capture-the-zone']:
        if token not in landing:errors.append('landing page missing navigation: '+token)
    return {'markdown_files':len(files),'local_targets_checked':links,'anchors_checked':anchors,'errors':errors}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);args=parser.parse_args()
    result=check(args.root);print(json.dumps(result,indent=2));return 1 if result['errors'] else 0

if __name__=='__main__':sys.exit(main())
