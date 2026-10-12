"""Scoped source index; preprocess registrations, do not compile or install game code."""
from pathlib import Path
import re, csv, hashlib, subprocess, json, argparse
from binding_patterns import BINDING_PATTERN, binding_kind, valid_binding_origin
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-root',type=Path,default=Path('engine-source/xray-monolith-2026.10.11'))
parser.add_argument('--warfare-root',type=Path,default=Path('warfare-source/beta150'))
parser.add_argument('--repo-root',type=Path,default=Path(__file__).resolve().parents[1])
options=parser.parse_args()
ROOT=options.source_root.resolve()
OUT=options.repo_root.resolve()/'02-lua-api/alife'; OUT.mkdir(parents=True,exist_ok=True)
EVIDENCE=options.repo_root.resolve()/'evidence/alife'; EVIDENCE.mkdir(parents=True,exist_ok=True)
SERVER=ROOT/'src/xrServerEntities'
files=sorted(set(SERVER.glob('xrServer_Objects*script*.cpp')) | set(SERVER.glob('xrserver_objects*script*.cpp')))
files = sorted(set(files) | set((ROOT/'src/xrGame').glob('alife_*_script.cpp')) | {ROOT/'src/xrGame/game_graph_script.cpp'})
headers=[SERVER/'script_export_macroses.h',SERVER/'xrServer_script_macroses.h']
def trim_includes(s):
    return re.sub(r'^[ \t]*#[ \t]*include[^\n]*', lambda m: ' '*len(m.group(0)), s, flags=re.M)
def balanced(s,start,left='(',right=')'):
    depth=0; quote=None; escape=False
    for i in range(start,len(s)):
        ch=s[i]
        if quote:
            if escape: escape=False
            elif ch=='\\': escape=True
            elif ch==quote: quote=None
            continue
        if ch in '\"\'': quote=ch; continue
        if ch==left: depth+=1
        elif ch==right:
            depth-=1
            if depth==0:return i
    raise ValueError(('unbalanced',s[start:start+100]))
def split_args(s):
    result=[];start=0;stack=[];quote=None;escape=False
    for i,ch in enumerate(s):
        if quote:
            if escape:escape=False
            elif ch=='\\':escape=True
            elif ch==quote:quote=None
            continue
        if ch in '\"\'':quote=ch
        elif ch in '(<[':stack.append(ch)
        elif ch in ')>]':
            if stack:stack.pop()
        elif ch==',' and not stack:result.append(s[start:i].strip());start=i+1
    result.append(s[start:].strip());return result
def compact(s):return re.sub(r'\s+',' ',s).strip()
classes=[]; bindings=[]; evidence={}
def add_evidence(p,source='ENGINE1011',base=ROOT):
    data=p.read_bytes(); rel=str(p.relative_to(base))
    evidence[(source,rel)]=[source,rel,hashlib.sha256(data).hexdigest(),len(data.splitlines())]
for p in files+headers:add_evidence(p)
for p in files:
    rel=str(p.relative_to(ROOT))
    for game in (False,True):
        # Headers are only macro definitions/wrappers here. No include resolution or link claim.
        src='\n'.join(trim_includes(h.read_text()) for h in headers)
        src+='\n#line 1 "'+rel+'"\n'+trim_includes(p.read_text())
        args=['cpp','-E','-x','c++','-undef','-nostdinc']+(['-DXRGAME_EXPORTS'] if game else [])+['-']
        proc=subprocess.run(args,input=src,text=True,capture_output=True,check=True)
        text=''; locations=[];line=1;filename=''
        for raw in proc.stdout.splitlines(True):
            mark=re.match(r'# (\d+) "([^"]+)"',raw)
            if mark:line=int(mark[1]);filename=mark[2];continue
            if raw.lstrip().startswith('#'):line+=1;continue
            text+=raw;locations.extend([(filename,line)]*len(raw));line+=1
        for func in re.finditer(r'void\s+(\w+)::script_register\s*\([^)]*\)\s*\{',text):
            end=balanced(text,func.end()-1,'{','}'); body=text[func.end():end]; offset=func.end()
            events=[]
            for m in re.finditer(r'\bclass_\s*<',body):
                a=m.end()-1;b=balanced(body,a,'<','>');after=b+1
                while after<len(body) and body[after].isspace():after+=1
                if after>=len(body) or body[after]!='(':continue
                stop=balanced(body,after);arg=body[after+1:stop].strip()
                if not re.fullmatch(r'"[^"]+"',arg):continue
                params=split_args(body[a+1:b]);name=arg.strip('"')
                location=locations[offset+m.start()]
                classes.append([name,params[0],compact(body[a+1:b]),'XRGAME_EXPORTS' if game else '!XRGAME_EXPORTS',*location])
                events.append((m.start(),'class',name))
            for m in BINDING_PATTERN.finditer(body):
                start=body.index('(',m.start()); stop=balanced(body,start)
                vals=split_args(body[start+1:stop]);kind=m.group(1)
                if vals and re.fullmatch(r'"[^"]+"',vals[0]):
                    name=vals[0].strip('"'); expression=compact(', '.join(vals[1:]))
                    events.append((m.start(),'binding',(kind,name,expression)))
                elif kind=='.def' and vals[0].startswith('constructor<'):
                    events.append((m.start(),'binding',('constructor','<constructor>',compact(vals[0]))))
                else:raise ValueError(('unhandled binding',rel,vals))
            owner=None
            for pos,kind,value in sorted(events,key=lambda x:x[0]):
                if kind=='class':owner=value;continue
                form,name,expression=value
                actual_owner='<global>' if form=='def' else owner
                assert actual_owner,(rel,name)
                category=binding_kind(form,expression)
                file,line=locations[offset+pos]
                assert file==rel,(file,rel)
                bindings.append([actual_owner,name,category,expression,'XRGAME_EXPORTS' if game else '!XRGAME_EXPORTS',file,line])
def merge(rows,variant_index):
    groups={}
    for row in rows:
        key=tuple(row[:variant_index]+row[variant_index+1:]);groups.setdefault(key,set()).add(row[variant_index])
    out=[]
    for key,conditions in groups.items():
        row=list(key);row.insert(variant_index,'both evaluated branches' if len(conditions)==2 else next(iter(conditions)));out.append(row)
    return sorted(out,key=lambda r:(r[-2],int(r[-1]),r[0],r[1]))
classes=merge(classes,3);bindings=merge(bindings,4)
def write(name,columns,rows):
    with ((EVIDENCE if name=='interface-evidence-oct11.csv' else OUT)/name).open('w') as f:
        w=csv.writer(f,lineterminator='\n');w.writerow(columns);w.writerows(rows)
write('native-lua-classes-oct11.csv',['lua_class','cpp_class','registered_template_arguments','evaluated_branch','source_path','source_line'],classes)
write('native-lua-bindings-oct11.csv',['lua_owner','lua_name','binding_kind','expanded_binding_expression','evaluated_branch','source_path','source_line'],bindings)
# Function declarations are source-indexed helpers, not inferred Lua arities/default arguments.
declarations=[]
for p in files:
    s=p.read_text()
    for m in re.finditer(r'^([\w:<>&* \t]+?)\s+([\w:]+)\s*\(',s,re.M):
        if m.group(2) in ('if','for','while','switch'):continue
        try:b=balanced(s,m.end()-1)
        except ValueError:continue
        rest=s[b+1:].lstrip()
        if not rest.startswith('{'):continue
        declarations.append([m.group(2),compact(s[m.start():b+1]),str(p.relative_to(ROOT)),s[:m.start()].count('\n')+1])
write('binding-helper-declarations-oct11.csv',['cpp_symbol','cpp_definition_signature','source_path','source_line'],declarations)
# Lua declaration inventory. Preserve source variants; do not infer execution/startup order.
scripts=[('ENGINE1011',ROOT,p) for p in sorted((ROOT/'gamedata/scripts').glob('*.script')) if p.name in {'sim_squad_scripted.script','bind_monster.script','callbacks_gameobject.script','aaaa_script_fixes_mp.script'}]
war=options.warfare_root.resolve()
scripts += [('BETA150',war,p) for p in sorted(war.rglob('*.script'))]
lua=[]
for source,base,p in scripts:
    add_evidence(p,source,base)
    s=p.read_bytes().decode('utf-8', errors='replace');s=re.sub(r'--\[(=*)\[.*?\]\1\]',lambda m:'\n'*m.group(0).count('\n'),s,flags=re.S)
    for i,line in enumerate(s.splitlines(),1):
        m=re.match(r'^\s*(?:local\s+)?function\s+([\w.:]+)\s*\(([^)]*)\)',line)
        if not m:continue
        symbol=m.group(1);params=m.group(2)
        lua.append([source,str(p.relative_to(base)),i,symbol,params,'implicit self' if ':' in symbol else 'explicit parameters','source declaration; effective installation unverified'])
write('script-interfaces-oct11.csv',['source_id','source_path','source_line','lua_symbol','parameters','receiver_form','status'],lua)
for p in [ROOT/'src/xrGame/alife_simulator.h',ROOT/'src/xrServerEntities/xrServer_Object_Base.h',ROOT/'src/xrServerEntities/xrServer_Objects_ALife.h',ROOT/'src/xrServerEntities/xrServer_Objects_ALife_Monsters.h',ROOT/'src/xrGame/alife_online_offline_group.cpp',ROOT/'src/xrGame/alife_update_manager.h',ROOT/'src/xrGame/alife_simulator_base.h',ROOT/'src/xrGame/alife_simulator_base.cpp',ROOT/'src/xrGame/alife_combat_manager.h',ROOT/'src/xrGame/alife_smart_terrain_task.h',ROOT/'src/xrServerEntities/alife_monster_brain.h',ROOT/'src/xrGame/alife_monster_movement_manager.h',ROOT/'src/xrGame/alife_monster_detail_path_manager.h',ROOT/'src/xrGame/alife_monster_patrol_path_manager.h']:
    add_evidence(p)
write('interface-evidence-oct11.csv',['source_id','archive_relative_path','sha256','line_count'],sorted(evidence.values()))
assert any(r[0]=='cse_alife_online_offline_group' and r[1]=='get_current_task' and r[4]=='XRGAME_EXPORTS' for r in bindings)
assert any(r[0]=='cse_alife_online_offline_group' and r[1]=='can_switch_online' and r[2]=='virtual_method' for r in bindings)
assert not any(r[1]=='force_change_game_vertex_id' for r in bindings)
assert not any(r[1]=='objects_iter' for r in bindings)
assert len([r for r in bindings if r[0]=='alife_simulator' and r[1]=='create'])==4
# Verify every row's source origin against the unpreprocessed archive.
for row in classes:
    line=(ROOT/row[-2]).read_text().splitlines()[int(row[-1])-1]
    assert 'class_' in line,(row,line)
for row in bindings:
    line=(ROOT/row[-2]).read_text().splitlines()[int(row[-1])-1]
    assert valid_binding_origin(line),(row,line)
for source,path,line,symbol,*_ in lua:
    base=ROOT if source=='ENGINE1011' else war
    actual=(base/path).read_bytes().decode('utf-8',errors='replace').splitlines()[int(line)-1]
    assert re.search(r'function\s+'+re.escape(symbol)+r'\s*\(',actual),(path,line,symbol)
stats={'registrar_files':len(files),'class_rows':len(classes),'binding_rows':len(bindings),'helper_declarations':len(declarations),'script_declarations':len(lua),'source_files':len(evidence)}
(OUT/'catalog-statistics.json').write_text(json.dumps(stats,indent=2)+'\n');print(json.dumps(stats))
