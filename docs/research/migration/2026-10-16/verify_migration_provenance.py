#!/usr/bin/env python3
"""Verify frozen source identities and retained destination hashes for the migration ledger."""
from __future__ import annotations
import argparse, hashlib, json, subprocess, sys
from collections import Counter
from pathlib import Path

BASE=Path(__file__).resolve().parent

def git(repo:Path,*args:str)->bytes:
    return subprocess.check_output(['git','-C',str(repo),*args])
def sha(data:bytes)->str:return hashlib.sha256(data).hexdigest()
def jsonl(path:Path)->list[dict]:
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]
def check_blob(source:Path,commit:str,path:str,expected:str)->bool:
    try:return git(source,'rev-parse',f'{commit}:{path}').decode().strip()==expected
    except subprocess.CalledProcessError:return False

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('--source-repo',type=Path,required=True);ap.add_argument('--destination',type=Path,required=True);a=ap.parse_args()
    src=a.source_repo.resolve();dst=a.destination.resolve();pin=json.loads((BASE/'baseline'/'baseline.json').read_text())
    main_sha=pin['source']['main_sha'];dest_sha=pin['destination']['main_sha']
    errors=[];counts=Counter()
    artifacts=jsonl(BASE/'ledger'/'source-main-artifacts.jsonl')
    files=jsonl(BASE/'ledger'/'source-main-files.jsonl')
    deps=jsonl(BASE/'ledger'/'source-main-dependencies.jsonl')
    edges=jsonl(BASE/'ledger'/'source-main-dependency-edges.jsonl')
    for row in artifacts:
        path=row['original_path'];commit=row['source_commit'];oid=row['source_git_blob_sha']
        counts['source_artifact_records']+=1
        if not check_blob(src,commit,path,oid):errors.append(f'source artifact tree/blob mismatch: {path}@{commit[:12]}');continue
        data=git(src,'cat-file','blob',oid)
        if sha(data)!=row['source_sha256']:errors.append(f'source artifact SHA-256 mismatch: {path}')
        if row['source_target']=='target-c':counts['target_c_artifacts']+=1
        public_path=row.get('public_path')
        expected=row.get('public_sha256')
        if public_path and expected:
            out=dst/public_path
            if not out.is_file():errors.append(f'missing retained artifact: {public_path}')
            elif sha(out.read_bytes())!=expected:errors.append(f'destination artifact hash mismatch: {public_path}')
            else:counts['public_artifact_hashes_checked']+=1
        disposition=row.get('disposition','')
        if disposition.startswith(('integrate','preserve')) and not (public_path and expected):
            errors.append(f'integrated artifact lacks destination hash receipt: {path}')
    for row in files:
        path=row['original_path'];commit=row['source_commit'];oid=row['source_git_blob_sha']
        counts['source_file_records']+=1
        if not check_blob(src,commit,path,oid):errors.append(f'source file tree/blob mismatch: {path}@{commit[:12]}');continue
        if sha(git(src,'cat-file','blob',oid))!=row['source_sha256']:errors.append(f'source file SHA-256 mismatch: {path}')
        public_path=row.get('public_path');expected=row.get('public_sha256')
        if public_path and expected:
            out=dst/public_path
            if not out.is_file():errors.append(f'missing retained source file: {public_path}')
            elif sha(out.read_bytes())!=expected:errors.append(f'destination source-file hash mismatch: {public_path}')
            else:counts['public_source_hashes_checked']+=1
        if row.get('integration_batch') and not (public_path and expected):errors.append(f'integrated source file lacks destination hash: {path}')
    commits={main_sha,*[x['source_commit'] for x in deps]}
    for row in deps:
        path=row['original_path'];commit=row['source_commit'];oid=row['source_git_blob_sha']
        counts['linked_dependency_records']+=1
        if not check_blob(src,commit,path,oid):errors.append(f'dependency source tree/blob mismatch: {path}@{commit[:12]}');continue
        if sha(git(src,'cat-file','blob',oid))!=row['source_sha256']:errors.append(f'dependency source SHA-256 mismatch: {path}')
        public_path=row.get('destination_path');expected=row.get('public_sha256')
        is_integrated=bool(row.get('integration_batch'))
        is_exact_existing=row.get('destination_relation')=='identical_same_path'
        if public_path and expected and (is_integrated or is_exact_existing):
            out=dst/public_path
            if not out.is_file():errors.append(f'missing linked dependency: {public_path}')
            elif sha(out.read_bytes())!=expected:errors.append(f'linked dependency public hash mismatch: {public_path}')
            else:counts['linked_dependency_hashes_checked']+=1
    for row in edges:
        counts['dependency_edges']+=1
        for key in ('from_source_commit','to_source_commit'):
            commit=row.get(key)
            if commit and commit not in commits and commit not in pin.get('source_history_commits',[]):
                # Exact path/blob verification above is the authority; this catches unpinned graph nodes.
                if commit not in {x.get('commit') for x in pin.get('source_history_commits',[])} and commit!=main_sha:
                    errors.append(f'unpinned dependency-edge commit: {commit}')
        destpath=row.get('to_destination_path')
        if row.get('integration_status')=='integrated_with_audit_batch' and destpath and not (dst/destpath).exists():
            errors.append(f'dependency edge destination absent: {destpath}')
    unresolved=jsonl(BASE/'ledger'/'unresolved-source-dependencies.jsonl')
    counts['unresolved_or_rights_blocked_dependencies']=len(unresolved)
    if unresolved:errors.append(f'{len(unresolved)} unresolved or rights-blocked source dependencies require disposition')
    current_state=sha((dst/'docs/state/theorem-state.yaml').read_bytes())
    frozen_state=sha(git(dst,'show',f'{dest_sha}:docs/state/theorem-state.yaml'))
    if current_state!=frozen_state:errors.append('destination theorem-state changed from frozen authoritative manifest')
    current=(dst/'docs/targets/target-c/CURRENT.md').read_text()
    if 'q=O(D^(4/5))' not in current or 'withdrawn' not in current.lower():errors.append('destination inverse-phase correction warning is absent')
    out={'status':'PASS' if not errors else 'FAIL','source_main':main_sha,'destination_baseline':dest_sha,
         'counts':dict(counts),'errors':errors,'claim':'source identity and retained-byte provenance only; no theorem correctness inferred'}
    print(json.dumps(out,indent=2))
    return 0 if not errors else 1
if __name__=='__main__':raise SystemExit(main())
