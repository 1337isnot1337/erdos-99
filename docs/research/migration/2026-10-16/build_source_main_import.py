#!/usr/bin/env python3
"""Recreate the frozen e-99 main Target C inventory and safe corpus import.

Run with --source-repo PATH --destination PATH --import-files to materialize
eligible first-party files. All source bytes are read from the pinned commit in
baseline.json; the source checkout's working branch is never consulted.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, subprocess
from pathlib import Path, PurePosixPath
import posixpath

BASE = Path(__file__).resolve().parent
PIN = json.loads((BASE / 'baseline' / 'baseline.json').read_text())
SOURCE_COMMIT = PIN['source']['main_sha']
DEST_COMMIT = PIN['destination']['main_sha']
ARCHIVE = 'docs/archive/source-e99-main-42f0296d'
TARGET_RE = re.compile(r'target[-_]c', re.I)
PRIVATE_HOME = re.compile(rb'(?<![A-Za-z0-9_.-])/home/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*')


def git(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(['git', '-C', str(repo), *args])


def tree(repo: Path, commit: str) -> dict[str, dict[str, str]]:
    raw = git(repo, 'ls-tree', '-r', '-z', '--full-tree', commit)
    out = {}
    for item in raw.split(b'\0'):
        if not item: continue
        meta, path = item.split(b'\t', 1)
        mode, typ, oid = meta.decode('ascii').split()
        out[path.decode('utf-8', 'surrogateescape')] = {'mode': mode, 'type': typ, 'blob': oid}
    return out


def blob(repo: Path, oid: str) -> bytes:
    return git(repo, 'cat-file', 'blob', oid)


def read_path(repo: Path, commit: str, path: str, source_tree: dict) -> bytes:
    return blob(repo, source_tree[path]['blob'])


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(x, sort_keys=True, separators=(',', ':'))+'\n' for x in rows))


def safe_bytes(data: bytes) -> tuple[bytes, list[str]]:
    out = PRIVATE_HOME.sub(b'[local filesystem path omitted]', data)
    changes = []
    if out != data: changes.append('removed absolute owner-local filesystem path')
    # The one generic infrastructure mention occurred in a research note and
    # is not mathematical content; neutralize it without exposing machine details.
    low = out.lower()
    if b'homelab' in low:
        out = re.sub(rb'(?i)homelab', b'local service environment', out)
        changes.append('neutralized private-environment reference')
    return out, changes


def historic_snapshot(data: bytes, original_path: str, destination_path: str) -> tuple[bytes, list[str]]:
    """Make archived snapshots visibly historical without altering their proof text."""
    if not (destination_path.endswith('.md') or destination_path.endswith('.md.source')):
        return data, []
    changes=[]
    lines=data.splitlines(keepends=True)
    if lines and lines[0].startswith(b'<!-- theorem-state:'):
        lines=lines[1:]
        changes.append('removed source theorem-state header; retained source lifecycle in migration ledger')
    current = original_path if original_path.startswith(('docs/reports/','docs/audits/','docs/targets/target-c/')) else 'docs/targets/target-c/CURRENT.md'
    rel=posixpath.relpath(current, posixpath.dirname(destination_path))
    banner=(f'> **Historical source snapshot, not current theorem authority.** This file preserves '
            f'`{original_path}` from e-99 main commit `{SOURCE_COMMIT}`. Source status labels are historical; '
            f'the destination theorem-state controls accepted claims. See the [current destination record]({rel}).\n\n').encode()
    if original_path.endswith('target_c_global_inverse_phase_face_tail_exclusion_independent_audit_2026-10-09.md'):
        banner+=(b'> **Withdrawn inference warning:** this source version asserts a global `K\'/D`-Lipschitz chart and '
                 b'`q=O(D^(4/5))`. The destination correction rejects those inferences; do not use them as premises.\n\n')
    changes.append('added historical-snapshot and destination-authority warning')
    return banner+b''.join(lines), changes


def archive_path(path: str) -> str:
    suffix='.source' if path.endswith('.md') else ''
    return f'{ARCHIVE}/{path}{suffix}'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--source-repo', type=Path, required=True)
    ap.add_argument('--destination', type=Path, required=True)
    ap.add_argument('--import-files', action='store_true')
    args = ap.parse_args()
    src, dst = args.source_repo.resolve(), args.destination.resolve()
    stree = tree(src, SOURCE_COMMIT)
    dtree = tree(dst, DEST_COMMIT)
    previous_payload_path=BASE/'ledger'/'main-import-payloads.json'
    previous_payload={}
    old_artifact_rows=[];old_file_rows=[]
    if (BASE/'ledger'/'source-main-artifacts.jsonl').exists():old_artifact_rows=[json.loads(x) for x in (BASE/'ledger'/'source-main-artifacts.jsonl').read_text().splitlines()]
    if (BASE/'ledger'/'source-main-files.jsonl').exists():old_file_rows=[json.loads(x) for x in (BASE/'ledger'/'source-main-files.jsonl').read_text().splitlines()]
    if previous_payload_path.exists():
        try: previous_payload={x['destination_path']:x for x in json.loads(previous_payload_path.read_text())}
        except (ValueError,KeyError,TypeError): previous_payload={}
    dest_hashes = {}
    for p, ent in dtree.items():
        if ent['type'] == 'blob': dest_hashes.setdefault(sha(blob(dst, ent['blob'])), []).append(p)
    idx = [json.loads(line) for line in git(src, 'show', f'{SOURCE_COMMIT}:docs/state/artifact-index.jsonl').decode().splitlines()]
    dest_index_bytes = git(dst, 'show', f'{DEST_COMMIT}:docs/state/artifact-index.jsonl')
    dest_idx = {json.loads(line)['path']: json.loads(line) for line in dest_index_bytes.decode().splitlines()}
    source_rows = []
    import_plan: dict[str, tuple[str, bytes, dict]] = {}
    for row in idx:
        path = row['path']
        if path not in stree or stree[path]['type'] != 'blob':
            content = b''; source_blob = None; source_sha = None
        else:
            source_blob = stree[path]['blob']; content = blob(src, source_blob); source_sha = sha(content)
        dst_row = dest_idx.get(path)
        d_ent = dtree.get(path)
        dest_blob = d_ent['blob'] if d_ent and d_ent['type']=='blob' else None
        dest_sha = sha(blob(dst, dest_blob)) if dest_blob else None
        if dest_sha == source_sha:
            relation = 'identical_same_path'
            treatment = 'exact_duplicate_verified_by_sha256'
        elif source_sha in dest_hashes:
            relation = 'identical_at_different_path'
            treatment = 'exact_duplicate_verified_by_sha256'
        elif not d_ent:
            relation = 'missing'
            treatment = 'integrate_as_noncanonical_research' if row['target'] == 'target-c' else 'review_for_cross_target_relevance'
        else:
            relation = 'modified_same_path'
            treatment = 'preserve_source_version_in_historical_archive; retain_destination_bytes'
        topic = 'target-c' if row['target']=='target-c' else ('cross-target-shared' if row['target']=='shared' else row['target'])
        rec = {
            'record_type':'artifact-index-entry', 'original_path':path,
            'source_commit':SOURCE_COMMIT, 'source_git_blob_sha':source_blob,
            'source_sha256':source_sha, 'source_bytes':len(content),
            'source_target':row['target'], 'source_lifecycle':row['status'],
            'source_canonical_flag':row['canonical'], 'source_claim_ids':row['claim_ids'],
            'source_claim_statuses':row['claim_statuses'], 'source_dependencies':row['depends_on'],
            'source_invalidates':row['invalidates'], 'source_supersedes':row['supersedes'],
            'destination_same_path_blob_sha':dest_blob, 'destination_same_path_sha256':dest_sha,
            'destination_relation':relation, 'proposed_destination':path if relation=='missing' else (archive_path(path) if relation=='modified_same_path' else (dest_hashes.get(source_sha,[None])[0] if source_sha else None)),
            'mathematical_scope':topic, 'contribution_kind':'research artifact; inspect source text and linked evidence',
            'disposition':treatment,
            'release_transformations':(['historical snapshot warning; remove source theorem-state label'] if relation=='modified_same_path' else (['apply destination-generated theorem-state metadata if needed'] if relation=='missing' else [])),
            'authority_note':'Source lifecycle is provenance only; destination theorem-state remains authoritative and no claim is promoted by import.'
        }
        source_rows.append(rec)
        if source_blob and row['target']=='target-c' and relation in ('missing','modified_same_path'):
            target = path if relation=='missing' else archive_path(path)
            data, transforms = safe_bytes(content)
            import_plan[target] = (path, data, {'source_blob':source_blob,'source_sha256':source_sha,'transforms':transforms,'kind':'artifact-index-entry'})
    write_jsonl(BASE/'ledger'/'source-main-artifacts.jsonl', source_rows)

    # Preserve the complete C-oriented research code/report tree. A path
    # collision is archived instead of overwriting destination work.
    file_rows = []
    research_paths = [p for p in stree if p.startswith('research/') and TARGET_RE.search(p)]
    for path in research_paths:
        ent=stree[path]
        if ent['type']!='blob': continue
        data=blob(src,ent['blob']); source_sha=sha(data)
        dest_ent=dtree.get(path); dest_sha=sha(blob(dst,dest_ent['blob'])) if dest_ent and dest_ent['type']=='blob' else None
        if dest_sha==source_sha: relation='identical_same_path'; target=path; disposition='exact_duplicate_verified_by_sha256'
        elif source_sha in dest_hashes: relation='identical_at_different_path'; target=dest_hashes[source_sha][0]; disposition='exact_duplicate_verified_by_sha256'
        elif not dest_ent: relation='missing'; target=path; disposition='integrated_as_noncanonical_research'
        else: relation='modified_same_path'; target=archive_path(path); disposition='preserved_source_version_in_historical_archive; destination version retained'
        transforms=[]
        safe, transforms=safe_bytes(data)
        rec={'record_type':'source-file','collection':'research-target-c','original_path':path,
             'source_commit':SOURCE_COMMIT,'source_git_blob_sha':ent['blob'],'source_sha256':source_sha,
             'source_bytes':len(data),'target':'target-c','source_lifecycle':'noncanonical research; see source claim/status references',
             'destination_same_path_sha256':dest_sha,'destination_relation':relation,'proposed_destination':target,
             'transformation':transforms or ['none'],'disposition':disposition,
             'dependencies':'Preserve adjacent files and report-declared dependencies; see source tree.'}
        file_rows.append(rec)
        if relation in ('missing','modified_same_path'):
            import_plan[target]=(path,safe,{'source_blob':ent['blob'],'source_sha256':source_sha,'transforms':transforms,'kind':'research-target-c'})

    # Keep prior route documentation as dated historical source snapshots; the
    # destination's CURRENT.md and theorem-state are never replaced.
    for path in stree:
        if not (path.startswith('docs/targets/target-c/') or path.startswith('prompts/') or path.startswith('docs/canonical/')): continue
        ent=stree[path]
        if ent['type']!='blob': continue
        data=blob(src,ent['blob']); source_sha=sha(data)
        dest_ent=dtree.get(path); dest_sha=sha(blob(dst,dest_ent['blob'])) if dest_ent and dest_ent['type']=='blob' else None
        if dest_sha==source_sha:
            relation='identical_same_path'; target=path; disposition='exact_duplicate_verified_by_sha256'
        elif source_sha in dest_hashes:
            relation='identical_at_different_path'; target=dest_hashes[source_sha][0]; disposition='exact_duplicate_verified_by_sha256'
        else:
            relation='missing' if not dest_ent else 'modified_same_path'
            target=archive_path(path); disposition='historical_source_route_snapshot; destination navigation remains current'
        transforms=[]; safe,transforms=safe_bytes(data)
        file_rows.append({'record_type':'source-file','collection':'route-prompt-canonical-history','original_path':path,
            'source_commit':SOURCE_COMMIT,'source_git_blob_sha':ent['blob'],'source_sha256':source_sha,
            'source_bytes':len(data),'target':'target-c','source_lifecycle':'historical source route; not destination authority',
            'destination_same_path_sha256':dest_sha,'destination_relation':relation,'proposed_destination':target,
            'transformation':transforms or ['none'],'disposition':disposition,
            'authority_note':'Historical snapshot only. Current route and theorem-state are governed by destination main.'})
        if disposition.startswith('historical'):
            import_plan[target]=(path,safe,{'source_blob':ent['blob'],'source_sha256':source_sha,'transforms':transforms,'kind':'route-history'})

    # Shared-index artifacts receive an explicit relevance decision, even when
    # they are outside this Target C migration's mathematical scope.
    for row in idx:
        if row['target']!='shared': continue
        path=row['path']; content=blob(src,stree[path]['blob']) if path in stree and stree[path]['type']=='blob' else b''
        if not content: continue
        c_relevant=bool(TARGET_RE.search(path) or re.search(rb'(?i)target\s*[- ]?c|c-ii|target_c|Target C',content))
        if c_relevant:
            sh=sha(content); ent=stree[path]; de=dtree.get(path); dh=sha(blob(dst,de['blob'])) if de and de['type']=='blob' else None
            relation='identical_same_path' if dh==sh else ('missing' if not de else 'modified_same_path')
            dest=path if relation=='missing' else (path if relation=='identical_same_path' else archive_path(path))
            frows={'record_type':'source-file','collection':'shared-cross-target','original_path':path,'source_commit':SOURCE_COMMIT,
              'source_git_blob_sha':ent['blob'],'source_sha256':sh,'source_bytes':len(content),'target':'shared; Target C relevance identified in text/path',
              'source_lifecycle':row['status'],'destination_same_path_sha256':dh,'destination_relation':relation,'proposed_destination':dest,
              'transformation':['none'],'disposition':'integrated_cross_target_foundation' if relation=='missing' else ('exact_duplicate_verified_by_sha256' if relation=='identical_same_path' else 'preserved_conflicting_source_version_in_archive'),
              'authority_note':'Cross-target source material is noncanonical unless independently present in destination theorem-state.'}
            file_rows.append(frows)
            if relation in ('missing','modified_same_path'):
                safe,transforms=safe_bytes(content); frows['transformation']=transforms or ['none']
                import_plan[dest]=(path,safe,{'source_blob':ent['blob'],'source_sha256':sh,'transforms':transforms,'kind':'shared-cross-target'})

    # Include source-only records for Target C-specific source docs not in the
    # generated artifact index; these are files whose paths advertise target c.
    artifact_paths={r['original_path'] for r in source_rows}
    for path in stree:
        if not path.endswith('.md') or path in artifact_paths: continue
        if not path.startswith(('docs/reports/','docs/audits/','docs/archive/')): continue
        if not TARGET_RE.search(path): continue
        ent=stree[path]; content=blob(src,ent['blob']); sh=sha(content); de=dtree.get(path); dh=sha(blob(dst,de['blob'])) if de and de['type']=='blob' else None
        relation='identical_same_path' if dh==sh else ('identical_at_different_path' if sh in dest_hashes else ('missing' if not de else 'modified_same_path'))
        target=path if relation=='missing' else (path if relation=='identical_same_path' else (dest_hashes[sh][0] if relation=='identical_at_different_path' else archive_path(path)))
        file_rows.append({'record_type':'source-file','collection':'unindexed-target-c-markdown','original_path':path,'source_commit':SOURCE_COMMIT,
          'source_git_blob_sha':ent['blob'],'source_sha256':sh,'source_bytes':len(content),'target':'target-c','source_lifecycle':'not present in frozen artifact index; noncanonical by default',
          'destination_same_path_sha256':dh,'destination_relation':relation,'proposed_destination':target,
          'transformation':['none'],'disposition':'integrated_unindexed_noncanonical_research' if relation=='missing' else ('exact_duplicate_verified_by_sha256' if relation.startswith('identical') else 'preserved_conflicting_source_version_in_archive')})
        if relation in ('missing','modified_same_path'):
            safe,transforms=safe_bytes(content); import_plan[target]=(path,safe,{'source_blob':ent['blob'],'source_sha256':sh,'transforms':transforms,'kind':'unindexed-markdown'})

    for target,(orig,data,meta) in list(import_plan.items()):
        if target.startswith(ARCHIVE+'/'):
            archived, changes=historic_snapshot(data,orig,target)
            meta['transforms'].extend(changes)
            import_plan[target]=(orig,archived,meta)

    plan_by_path={path:(orig,data,meta) for path,(orig,data,meta) in import_plan.items()}
    for row in source_rows:
        plan=plan_by_path.get(row['proposed_destination'])
        if plan:
            _,data,meta=plan
            row['release_transformations']=meta['transforms'] or ['none']
            row['planned_public_sha256_before_generated_artifact_header']=sha(data)
    for row in file_rows:
        plan=plan_by_path.get(row['proposed_destination'])
        if plan:
            _,data,meta=plan
            row['transformation']=meta['transforms'] or ['none']
            row['planned_public_sha256']=sha(data)

    if args.import_files:
        for target,(orig,data,meta) in sorted(import_plan.items()):
            out=dst/target
            if out.exists():
                current=out.read_bytes()
                if current == data: continue
                current_sha=sha(current)
                prior=next((r for r in old_artifact_rows+old_file_rows if r.get('proposed_destination')==target and r.get('source_git_blob_sha')==meta['source_blob'] and r.get('public_sha256')==current_sha),None)
                old=previous_payload.get(target)
                if prior or (old and current_sha==old.get('public_sha256')):
                    continue
                raise SystemExit(f'refusing to replace content not verified by the prior migration ledger: {target}')
            else:
                out.parent.mkdir(parents=True,exist_ok=True); out.write_bytes(data)
            meta['public_sha256']=sha(data); meta['public_path']=target; meta['original_path']=orig
            # The complete path-level provenance record is reconstructed below.
        # Archive-level notice keeps imported historical material's status clear.
        archive=dst/ARCHIVE
        archive.mkdir(parents=True,exist_ok=True)
        (archive/'README.md').write_text(
            '# Frozen e-99 source-main snapshots\n\n'
            'These files preserve source commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73` as a research-history snapshot. '
            'Their original source path, Git blob, SHA-256, destination mapping, and any release-safety transformation are recorded in '
            '[source-main artifact ledger](../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl).\n\n'
            'Source lifecycle labels are historical provenance only. The current destination theorem-state, Target C frontier, and current research navigation remain authoritative. '
            'In particular, old inverse-phase claims do not supersede the destination correction.\n')
    def preserve_prior(rows:list[dict],old_rows:list[dict])->None:
        old={(x.get('original_path'),x.get('source_git_blob_sha'),x.get('source_commit')):x for x in old_rows}
        for row in rows:
            prior=old.get((row.get('original_path'),row.get('source_git_blob_sha'),row.get('source_commit')))
            if not prior:continue
            for key in ('integration_batch','public_path','public_sha256','linked_source_files','linked_from','linked_dependency_record'):
                if key in prior:row[key]=prior[key]
            if prior.get('integration_batch') and prior.get('disposition','').startswith('integrated'):
                row['disposition']=prior['disposition']
    preserve_prior(file_rows,old_file_rows)
    preserve_prior(source_rows,old_artifact_rows)
    write_jsonl(BASE/'ledger'/'source-main-files.jsonl',file_rows)
    write_jsonl(BASE/'ledger'/'source-main-artifacts.jsonl',source_rows)
    (BASE/'ledger'/'main-import-payloads.json').write_text(json.dumps([
        {'source_path':orig,'destination_path':path,'source_git_blob_sha':meta['source_blob'],
         'source_sha256':meta['source_sha256'],'public_sha256':sha(data),'transformations':meta['transforms'] or ['none'],
         'kind':meta['kind']} for path,(orig,data,meta) in sorted(import_plan.items())],indent=2)+'\n')
    print(json.dumps({'source_artifact_rows':len(source_rows),'target_c_artifacts':sum(x['source_target']=='target-c' for x in source_rows),
      'research_target_c_files':len(research_paths),'file_inventory_rows':len(file_rows),'planned_imports':len(import_plan) if args.import_files else 0,
      'source_commit':SOURCE_COMMIT,'destination_commit':DEST_COMMIT},indent=2))
    return 0

if __name__=='__main__': raise SystemExit(main())
