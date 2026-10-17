#!/usr/bin/env python3
"""Check public corpus integrity. Data checks only; not a mathematical proof."""
from __future__ import annotations
import argparse, ast, collections, hashlib, json, re, subprocess, sys
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator
from public_links import markdown_targets
from run_theorem_certificates import entry_records, registered_certificates

def validate(root: Path, *, check_hashes=True):
    errors=[]
    def error(s):errors.append(s)
    state=yaml.safe_load((root/'docs/state/theorem-state.yaml').read_text())
    schema=json.loads((root/'docs/state/theorem-state.schema.json').read_text())
    for e in Draft202012Validator(schema).iter_errors(state):error('schema: '+e.message)
    rows=list(entry_records(state));ids={}
    buckets={'current_canonical_entries':'canonical','audited_working':'audited-working','regressions':'regression'}
    for target,bucket,c in rows:
        ident=c['id']
        if ident in ids:error('duplicate claim '+ident)
        ids[ident]=c
        if bucket in buckets and c['status']!=buckets[bucket]:error('claim lifecycle mismatch '+ident)
        if c['status']=='canonical' and not c.get('report'):error('canonical claim without proof '+ident)
        for k in ('report','audit'):
            if c.get(k) and not (root/c[k]).is_file():error(f'{ident}: missing {k}: {c[k]}')
        for p in c.get('certificates',[]):
            if not (root/p).is_file():error(f'{ident}: missing certificate: {p}')
    for _,_,c in rows:
        for p in c.get('depends_on',[]):
            # Edges may be structured records in future schemas; current schema is string IDs.
            if p not in ids:error(f'{c["id"]}: missing claim dependency {p}')
            elif c['status']=='canonical' and ids[p]['status'] not in ('canonical','regression'):
                error(f'{c["id"]}: noncanonical premise {p} ({ids[p]["status"]})')
    # Reject cycles in proof prerequisites, independently from the inherited checker.
    active=set();done=set()
    def visit(i):
        if i in active:error('proof dependency cycle '+i);return
        if i in done:return
        active.add(i)
        for j in ids[i].get('depends_on',[]):
            if j in ids:visit(j)
        active.remove(i);done.add(i)
    for i in ids:visit(i)
    from publication_migration import load_policy,reference_exclusions
    reference_links=0
    try:
        historical_payloads,imported_metadata=load_policy(root)
        excluded_references=reference_exclusions(root) if historical_payloads else set()
    except (ValueError,OSError,KeyError,subprocess.SubprocessError) as exc:
        error('migration archive policy: '+str(exc));historical_payloads=set();imported_metadata=set();excluded_references=set()
    tracked=[p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and '.venv' not in p.parts and '__pycache__' not in p.parts]
    for p in tracked:
        rel=p.relative_to(root).as_posix()
        if p.is_symlink():error('symlink forbidden in published corpus: '+rel);continue
        if rel in historical_payloads:continue
        if p.suffix=='.md':
            try:targets=markdown_targets(rel,p.read_text())
            except (ValueError,UnicodeError) as exc:error(f'{rel}: invalid navigation: {exc}');continue
            for q in targets:
                if not (root/q).exists():
                    if rel in imported_metadata and q in excluded_references:reference_links+=1
                    else:error(f'{rel}: missing link {q}')
        if p.suffix=='.py':
            try:nodes=ast.walk(ast.parse(p.read_text()))
            except SyntaxError as exc:error(f'{rel}: syntax {exc}');continue
            for n in nodes:
                names=[a.name for a in n.names] if isinstance(n,ast.Import) else [n.module] if isinstance(n,ast.ImportFrom) and n.module else []
                for name in names:
                    # Verifier conventions make absent local imports unambiguous.
                    if name.startswith(('verify_','target_')) and not (p.parent/(name+'.py')).is_file():error(f'{rel}: omitted helper {name}')
    cat=json.loads((root/'docs/research/agent-task-catalog.json').read_text())
    if not cat.get('tasks'):error('empty task catalogue')
    for t in cat['tasks']:
        for k in ('canonical_dependencies','previous_obstructions','audited_working_premises'):
            for r in t.get(k,[]):
                p=r['path']
                if not (root/p).is_file():error(f'{t["id"]}: unavailable prerequisite {p}')
                if p.startswith(('../','/')):error(f'{t["id"]}: private/outside prerequisite {p}')
        for k in ('question','assumptions','expected_evidence','falsification_strategy','stopping_condition','reproduction','remaining_if_successful','does_not_prove'):
            if not t.get(k):error(f'{t["id"]}: missing task field {k}')
    certs=registered_certificates(state)
    registry=json.loads((root/'research/certificates.json').read_text())
    if {r['path'] for r in registry['certificates']}!=set(certs):error('certificate registry disagrees with theorem manifest')
    inc=json.loads((root/'docs/publication/inclusion.json').read_text())
    for r in inc['entries']:
        p=root/r['public_path']
        if not p.is_file():error('omitted retained dependency: '+r['public_path'])
        elif check_hashes and hashlib.sha256(p.read_bytes()).hexdigest()!=r['public_sha256']:error('inclusion hash stale: '+r['public_path'])
        for dep in r.get('dependencies',[]):
            if not (root/dep).exists():error(f'{r["public_path"]}: omitted dependency {dep}')
    if inc.get('unresolved_dependencies'):error('publication dependency closure has unresolved edges')
    # The public graph must be independently regenerable from the retained manifest.
    from generate_theorem_state_views import expected_files
    for path,text in expected_files(root,state).items():
        if not (root/path).is_file() or (root/path).read_text()!=text:error('stale generated theorem view '+path)
    from build_artifact_index import build_records,check_state
    try:errors.extend(check_state(root,state,build_records(root,state)))
    except (ValueError,FileNotFoundError) as exc:error('artifact registry: '+str(exc))
    return errors,{'claims':len(ids),'edges':sum(len(c.get('depends_on',[])) for c in ids.values()),'certificates':len(certs),'tasks':len(cat['tasks']),'retained_source_files':len(inc['entries']),'nonredistributed_reference_links':reference_links}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--skip-hashes',action='store_true');a=ap.parse_args()
    errors,counts=validate(a.root.resolve(),check_hashes=not a.skip_hashes)
    for e in errors:print('ERROR',e)
    print(json.dumps({'integrity':'failed' if errors else 'passed','errors':len(errors),'counts':counts,'mathematical_proof':False},sort_keys=True))
    return bool(errors)
if __name__=='__main__':raise SystemExit(main())
