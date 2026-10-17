#!/usr/bin/env python3
"""Check public corpus integrity. Data checks only; not a mathematical proof."""
from __future__ import annotations
import argparse, ast, json
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator
from public_links import markdown_targets, safe_path
from run_theorem_certificates import entry_records, registered_certificates

def check_files(root: Path, records):
    """Check current navigation and Python helpers without historical inventories.

    Archived documents retain source-relative references and are data, not live
    navigation or executable modules. The release scanner still scans them.
    Older unreviewed report headers are a metadata format, not a byte pin.
    """
    from build_artifact_index import legacy_unreviewed_header
    record_by_path = {record['path']: record for record in records}
    errors, reference_links = [], 0
    for path in root.rglob('*'):
        rel = path.relative_to(root).as_posix()
        if any(part in {'.git', '.venv', '__pycache__'} for part in path.relative_to(root).parts):
            continue
        if path.is_symlink():
            errors.append('symlink forbidden in published corpus: ' + rel)
            continue
        if not path.is_file() or rel.startswith(('docs/archive/', 'docs/research/migration/')):
            continue
        if path.suffix == '.md':
            try:
                text = path.read_text(encoding='utf-8')
                targets = markdown_targets(rel, text)
            except (ValueError, UnicodeError, OSError) as exc:
                errors.append(f'{rel}: invalid navigation: {exc}')
                continue
            record = record_by_path.get(rel)
            first = text.splitlines()[0] if text else ''
            legacy = record is not None and legacy_unreviewed_header(first, record)
            for target in targets:
                if (root / target).exists():
                    continue
                literature = target.startswith('extracted/') or (
                    target.startswith('papers/') and Path(target).suffix not in {'.md', '.bib', '.json'})
                if legacy and literature:
                    reference_links += 1
                else:
                    errors.append(f'{rel}: missing link {target}')
        if path.suffix == '.py':
            try:
                nodes = ast.walk(ast.parse(path.read_text(encoding='utf-8')))
            except (SyntaxError, UnicodeError, OSError) as exc:
                errors.append(f'{rel}: syntax {exc}')
                continue
            for node in nodes:
                names = ([alias.name for alias in node.names] if isinstance(node, ast.Import)
                         else [node.module] if isinstance(node, ast.ImportFrom) and node.module else [])
                for name in names:
                    if name.startswith(('verify_', 'target_')) and not (path.parent / (name + '.py')).is_file():
                        errors.append(f'{rel}: omitted helper {name}')
    return errors, reference_links


def check_declared_files(root: Path, dependencies):
    """Require the files named by current proof and evidence declarations."""
    paths = set(dependencies)
    for required in dependencies.values():
        paths.update(required)
    errors = []
    for path in sorted(paths):
        try:
            safe_path(path)
        except ValueError:
            errors.append('unsafe current dependency: ' + path)
            continue
        if not (root / path).is_file():
            errors.append('missing current dependency: ' + path)
    return errors


def validate(root: Path):
    errors=[]
    def error(s):errors.append(s)
    state=yaml.safe_load((root/'docs/state/theorem-state.yaml').read_text(encoding='utf-8'))
    schema=json.loads((root/'docs/state/theorem-state.schema.json').read_text(encoding='utf-8'))
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
    from build_artifact_index import build_records,check_state
    records=[]
    try:
        records=build_records(root,state)
        errors.extend(check_state(root,state,records))
    except (ValueError,OSError) as exc:error('artifact registry: '+str(exc))
    file_errors,reference_links=check_files(root,records)
    errors.extend(file_errors)
    cat=json.loads((root/'docs/research/agent-task-catalog.json').read_text(encoding='utf-8'))
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
    registry=json.loads((root/'research/certificates.json').read_text(encoding='utf-8'))
    if {r['path'] for r in registry['certificates']}!=set(certs):error('certificate registry disagrees with theorem manifest')
    # The public graph follows current theorem and certificate declarations.
    from generate_theorem_state_views import current_file_dependencies, expected_files
    errors.extend(check_declared_files(root,current_file_dependencies(root,state)))
    for path,text in expected_files(root,state).items():
        if not (root/path).is_file() or (root/path).read_text(encoding='utf-8')!=text:error('stale generated theorem view '+path)
    from build_reading_edition import check as check_reading
    try:errors.extend(check_reading(root))
    except (ValueError,OSError) as exc:error('reading edition: '+str(exc))
    return errors,{'claims':len(ids),'edges':sum(len(c.get('depends_on',[])) for c in ids.values()),'certificates':len(certs),'tasks':len(cat['tasks']),'artifacts':len(records),'nonredistributed_reference_links':reference_links}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=ap.parse_args()
    errors,counts=validate(a.root.resolve())
    for e in errors:print('ERROR',e)
    print(json.dumps({'integrity':'failed' if errors else 'passed','errors':len(errors),'counts':counts,'mathematical_proof':False},sort_keys=True))
    return bool(errors)
if __name__=='__main__':raise SystemExit(main())
