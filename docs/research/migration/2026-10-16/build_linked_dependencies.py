#!/usr/bin/env python3
"""Import and reconcile first-party Markdown-linked dependencies of Target C work.

Only frozen source-main bytes and caller-pinned source commits are read. Third-party
papers and extracted text are logged as blocked dependencies and are never copied.
"""
from __future__ import annotations
import argparse, hashlib, json, posixpath, re, subprocess
from collections import deque
from pathlib import Path
import sys
from urllib.parse import urlsplit
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from tools.public_links import local_target, markdown_destinations

BASE=Path(__file__).resolve().parent
PIN=json.loads((BASE/'baseline'/'baseline.json').read_text())
SM=PIN['source']['main_sha']; DM=PIN['destination']['main_sha']
ARCHIVE='docs/archive/source-e99-main-42f0296d'
THIRD_PARTY=('papers/','extracted/')

def git(repo:Path,*args:str)->bytes:
    return subprocess.check_output(['git','-C',str(repo),*args])
def tree(repo:Path,commit:str)->dict[str,dict[str,str]]:
    out={}
    for item in git(repo,'ls-tree','-r','-z','--full-tree',commit).split(b'\0'):
        if item:
            meta,path=item.split(b'\t',1); mode,typ,oid=meta.decode().split()
            out[path.decode('utf-8','surrogateescape')]={'mode':mode,'type':typ,'blob':oid}
    return out
def blob(repo:Path,oid:str)->bytes:return git(repo,'cat-file','blob',oid)
def sha(data:bytes)->str:return hashlib.sha256(data).hexdigest()
def archive(path:str)->str:return f'{ARCHIVE}/{path}'+('.source' if path.endswith('.md') else '')
def safe_bytes(data:bytes)->tuple[bytes,list[str]]:
    out=re.sub(rb'(?<![A-Za-z0-9_.-])/home/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*',b'[local filesystem path omitted]',data)
    tx=['removed absolute owner-local filesystem path'] if out!=data else []
    if b'homelab' in out.lower():out=re.sub(rb'(?i)homelab',b'local service environment',out);tx.append('neutralized private-environment reference')
    return out,tx
def source_archive_notice(data:bytes,path:str,commit:str)->tuple[bytes,list[str]]:
    tx=[];lines=data.splitlines(keepends=True)
    if lines and lines[0].startswith(b'<!-- theorem-state:'):lines=lines[1:];tx.append('removed source theorem-state header')
    return f'> **Historical source dependency, not current theorem authority.** Frozen at `{commit}` from `{path}`.\n\n'.encode()+b''.join(lines),tx+['added historical source notice']
def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('--source-repo',type=Path,required=True);ap.add_argument('--destination',type=Path,required=True);ap.add_argument('--extra-commit',action='append',default=[]);ap.add_argument('--import-files',action='store_true')
    a=ap.parse_args();src=a.source_repo.resolve();dst=a.destination.resolve()
    trees={SM:tree(src,SM),**{c:tree(src,c) for c in a.extra_commit}};dt=tree(dst,DM)
    idx={x['path']:x for x in (json.loads(l) for l in git(src,'show',f'{SM}:docs/state/artifact-index.jsonl').decode().splitlines())}
    arts=[json.loads(l) for l in (BASE/'ledger/source-main-artifacts.jsonl').read_text().splitlines()]
    fpath=BASE/'ledger/source-main-files.jsonl'; files=[json.loads(l) for l in fpath.read_text().splitlines()] if fpath.exists() else []
    path_map={x['original_path']:x['proposed_destination'] for x in arts if x['source_target']=='target-c'}
    for x in files:path_map.setdefault(x['original_path'],x['proposed_destination'])
    dest_hashes={}
    for p,e in dt.items():
        if e['type']=='blob':dest_hashes.setdefault(sha(blob(dst,e['blob'])),[]).append(p)
    queue=deque((SM,x['original_path'],x['proposed_destination']) for x in arts if x['source_target']=='target-c' and x['destination_relation'] in ('missing','modified_same_path') and x['original_path'].endswith('.md') and not x['proposed_destination'].endswith('.source'))
    visited=set();planned={};dep_rows={};blocked=[];unresolved=[];linkmap=dict(path_map);edges=[]
    source_target_c_paths={x['original_path'] for x in arts if x['source_target']=='target-c'}
    for row in arts: row['linked_source_files']=[]
    while queue:
        commit,parent,parent_dest=queue.popleft();key=(commit,parent)
        if key in visited:continue
        visited.add(key);ent=trees.get(commit,{}).get(parent)
        if not ent or ent['type']!='blob':continue
        data=blob(src,ent['blob']);text=data.decode('utf-8','replace')
        for _,_,raw in markdown_destinations(text):
            try:target=local_target(parent,raw)
            except ValueError as e:unresolved.append({'from':parent,'target':raw,'reason':str(e)});continue
            if target is None:continue
            if any(target.startswith(x) for x in THIRD_PARTY):
                blocked.append({'from':parent,'target':target,'source_commit':commit,'reason':'third-party paper or extracted text; no file redistributed; citation retained'})
                continue
            target_commit=SM;target_tree=trees[SM];te=target_tree.get(target)
            if not te or te['type']!='blob':
                found=next(((c,t,t[target]) for c,t in trees.items() if c!=SM and target in t and t[target]['type']=='blob'),None)
                if found:target_commit,target_tree,te=found
            if not te or te['type']!='blob':
                if not (dst/target).is_file():unresolved.append({'from':parent,'target':target,'reason':'absent from frozen source main, pinned extra commits, and destination main'})
                linkmap.setdefault(target,target)
                continue
            target_data=blob(src,te['blob']);target_sha=sha(target_data)
            existing_map=linkmap.get(target)
            if existing_map:
                mapped=existing_map
            else:
                de=dt.get(target);dsha=sha(blob(dst,de['blob'])) if de and de['type']=='blob' else None
                if dsha==target_sha:mapped=target
                elif target_sha in dest_hashes:mapped=dest_hashes[target_sha][0]
                elif not de:mapped=target
                else:mapped=archive(target)
                linkmap[target]=mapped
            edges.append({'from_source_commit':commit,'from_source_path':parent,'to_source_commit':target_commit,
                          'to_source_path':target,'to_destination_path':mapped,'edge_kind':'markdown-local-link'})
            if target not in source_target_c_paths:
                de=dt.get(target);dsha=sha(blob(dst,de['blob'])) if de and de['type']=='blob' else None
                relation='identical_same_path' if dsha==target_sha else ('identical_at_different_path' if target_sha in dest_hashes else ('missing' if not de else 'modified_same_path'))
                dep_rows.setdefault(target,{'record_type':'linked-source-dependency','original_path':target,'source_commit':target_commit,'source_git_blob_sha':te['blob'],'source_sha256':target_sha,'source_bytes':len(target_data),'mathematical_scope':idx.get(target,{}).get('target','linked cross-target or supporting dependency'),'source_lifecycle':idx.get(target,{}).get('status','unindexed at frozen source main'),'linked_from':[],'destination_path':mapped,'destination_relation':relation,'transformation':['none'],'disposition':'integrated as linked noncanonical dependency' if mapped==target else 'preserved in historical source archive; destination bytes retained'})
                dep_rows[target]['linked_from'].append(parent)
            # Materialize only first-party dependencies not already in this branch.
            if not (dst/mapped).is_file() and mapped not in planned:
                safe,trans=safe_bytes(target_data)
                if mapped.startswith(ARCHIVE+'/'):
                    safe,notices=source_archive_notice(safe,target,target_commit);trans+=notices
                planned[mapped]={'original_path':target,'source_commit':target_commit,'source_git_blob_sha':te['blob'],'source_sha256':target_sha,'bytes':safe,'transformations':trans}
                dep_rows.setdefault(target,{'record_type':'linked-source-dependency','original_path':target,'source_commit':target_commit,'source_git_blob_sha':te['blob'],'source_sha256':target_sha,'source_bytes':len(target_data),'mathematical_scope':idx.get(target,{}).get('target','cross-target dependency linked by a Target C source artifact'),'source_lifecycle':idx.get(target,{}).get('status','unindexed at frozen source main'),'linked_from':[],'destination_path':mapped,'destination_relation':'missing' if not dt.get(target) else 'modified_same_path','transformation':trans or ['none'],'disposition':'integrated as linked noncanonical dependency' if mapped==target else 'preserved in historical source archive; destination bytes retained'})
            # Recursively resolve markdown links, including the external-head Target B lemma.
            if target.endswith('.md') and target_commit in trees:
                qdest=mapped
                if qdest.endswith('.source'):continue
                queue.append((target_commit,target,qdest))
    # Rebuild imported Markdown copies from the pinned source body and apply
    # destination-relative link rewrites idempotently. Preserve the destination
    # theorem-state header already generated for the current path.
    rewrites=[]
    candidates=[]
    for row in arts:
        if row['source_target']=='target-c' and row['destination_relation'] in ('missing','modified_same_path'):
            candidates.append((SM,row['original_path'],row['proposed_destination']))
    for row in dep_rows.values():
        if row['destination_relation'] in ('missing','modified_same_path'):
            candidates.append((row['source_commit'],row['original_path'],row['destination_path']))
    seen_candidates=set()
    for parent_commit,parent_source,parent_dest in candidates:
        if (parent_commit,parent_source) in seen_candidates or parent_dest.endswith('.source'):continue
        seen_candidates.add((parent_commit,parent_source))
        source_ent=trees.get(parent_commit,{}).get(parent_source);current_file=dst/parent_dest
        if not source_ent or not current_file.is_file():continue
        source_data,privacy_tx=safe_bytes(blob(src,source_ent['blob']))
        source_lines=source_data.splitlines(keepends=True)
        if source_lines and source_lines[0].startswith(b'<!-- theorem-state:'):source_lines=source_lines[1:]
        source_body=b''.join(source_lines).decode('utf-8','replace')
        body=source_body
        original_spans=list(markdown_destinations(source_body))
        replacements=[]
        for start,end,raw in original_spans:
            try:target=local_target(parent_source,raw)
            except ValueError:continue
            if target is None:continue
            mapped=linkmap.get(target,target)
            if mapped==target:continue
            parsed=urlsplit(raw.strip('<>'));new=posixpath.relpath(mapped,posixpath.dirname(parent_dest) or '.')
            if parsed.fragment:new+='#'+parsed.fragment
            if raw.startswith('<') and raw.endswith('>'):new='<'+new+'>'
            replacements.append((start,end,raw,new,target,mapped))
        for start,end,raw,new,target,mapped in reversed(replacements):body=body[:start]+new+body[end:]
        current_file_text=current_file.read_text(encoding='utf-8')
        header=current_file_text.splitlines()[0] if current_file_text.startswith('<!-- theorem-state:') else None
        rebuilt=(header+'\n' if header else '')+body
        if rebuilt!=current_file_text:current_file.write_text(rebuilt,encoding='utf-8')
        for _,_,raw,new,target,mapped in replacements:
            rewrites.append({'parent_source':parent_source,'parent_destination':parent_dest,'source_commit':parent_commit,
                'source_target':target,'retained_target':mapped,'old_link':raw,'new_link':new,
                'application':'applied' if current_file_text!=rebuilt else 'verified_in_reconstructed_copy',
                'transformation':'rebuilt from pinned source body; rewrote link to exact retained destination path'})
    if a.import_files:
        for destpath,r in sorted(planned.items()):
            f=dst/destpath
            if f.exists():
                if f.read_bytes()==r['bytes']:continue
                raise SystemExit('refusing dependency overwrite: '+destpath)
            f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(r['bytes']);dep_rows[r['original_path']]['public_sha256']=sha(r['bytes'])
    for r in dep_rows.values():
        r['linked_from']=sorted(set(r['linked_from']))
        public=dst/r['destination_path']
        if public.is_file():r['public_sha256']=sha(public.read_bytes())
    for row in arts:
        row['linked_source_files']=sorted({(x['from'],x['destination_path']) for x in row.get('linked_source_files',[])})
        row['linked_source_files']=[{'from':x[0],'destination_path':x[1]} for x in row['linked_source_files']]
        public=dst/row['proposed_destination'] if row.get('proposed_destination') else None
        if public and public.is_file():
            row['public_path']=row['proposed_destination'];row['public_sha256']=sha(public.read_bytes())
        if row['source_target']=='target-c' and row['destination_relation'] in ('missing','modified_same_path') and public and public.is_file():
            row['integration_batch']='source-main-target-c-artifact-batch-1'
            if any(x['parent_source']==row['original_path'] for x in rewrites):
                row['release_transformations']=sorted(set(row.get('release_transformations',[])+['destination-relative source links reconciled']))
        if row['source_target']=='shared' and row['original_path'] in dep_rows:
            row['linked_dependency_record']=True;row['linked_from']=dep_rows[row['original_path']]['linked_from']
            row['disposition']='integrated_as_linked_noncanonical_dependency' if row['destination_relation'] in ('missing','modified_same_path') else 'exact_duplicate_verified_by_sha256'
            row['scope_reason']='Direct dependency of frozen Target C research; full source and destination identity is in the linked dependency ledger.'
            if public and public.is_file() and row['destination_relation'] in ('missing','modified_same_path'):
                row['integration_batch']='source-main-linked-dependencies-batch-1'
    for row in files:
        row['linked_from']=sorted({x['from_source_path'] for x in edges if x['to_source_path']==row['original_path']})
        public=dst/row['proposed_destination'] if row.get('proposed_destination') else None
        if public and public.is_file():
            row['public_path']=row['proposed_destination'];row['public_sha256']=sha(public.read_bytes())
        if row.get('destination_relation') in ('missing','modified_same_path') and public and public.is_file():
            row['integration_batch']='source-main-target-c-artifact-batch-1-linked-dependency'
            row['disposition']='integrated_as_linked_dependency; later full-corpus import will deduplicate by source path and blob'
    out=BASE/'ledger';out.mkdir(parents=True,exist_ok=True)
    (out/'source-main-dependencies.jsonl').write_text(''.join(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n' for x in dep_rows.values()))
    (out/'source-main-link-rewrites.jsonl').write_text(''.join(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n' for x in rewrites))
    (out/'source-main-dependency-edges.jsonl').write_text(''.join(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n' for x in edges))
    for row in arts:
        row['linked_source_files']=sorted(row.get('linked_source_files',[]),key=lambda x:(x['from'],x['destination_path']))
    (out/'source-main-artifacts.jsonl').write_text(''.join(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n' for x in arts))
    (out/'source-main-files.jsonl').write_text(''.join(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n' for x in files))
    (out/'unresolved-source-dependencies.jsonl').write_text(''.join(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n' for x in blocked+unresolved))
    print(json.dumps({'linked_source_dependencies':len(dep_rows),'planned_files':len(planned),'rewritten_links':len(rewrites),'blocked_third_party_links':len(blocked),'unresolved':len(unresolved),'commits':sorted({x['source_commit'] for x in dep_rows.values()}),'imported':a.import_files},indent=2))
    return 0
if __name__=='__main__':raise SystemExit(main())
