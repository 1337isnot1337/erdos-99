#!/usr/bin/env python3
"""Read-only checks for Agent 1 migration assignment and payload ledgers."""
from __future__ import annotations
import hashlib, json, pathlib, math, re

EVIDENCE=pathlib.Path(__file__).resolve().parent
AGENT=EVIDENCE.parent
REPO=AGENT.parents[4]

def load_json(path):
    return json.loads(path.read_text(encoding='utf-8'))

def load_jsonl(path):
    return [json.loads(s) for s in path.read_text(encoding='utf-8').splitlines() if s]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def check_hash(path, expected):
    assert path.is_file(), f'missing file: {path}'
    assert sha(path.read_bytes())==expected, f'hash mismatch: {path}'

def check_sums(path):
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.strip():
            expected, relative=line.split('  ',1)
            check_hash(path.parent/relative,expected)

check_sums(EVIDENCE/'assignment-SHA256SUMS')
check_sums(EVIDENCE/'SHA256SUMS')
summary=load_json(EVIDENCE/'assignment-summary.json')
assignment=load_jsonl(EVIDENCE/'source-main-three-way-assignment.jsonl')
units=load_jsonl(EVIDENCE/'source-main-three-way-units.jsonl')
assert len(assignment)==summary['source_file_count']==4717
assert summary['source_main_sha']=='42f0296d1aca068c809f74cee5dcdb4ebdb27c73'
assert summary['destination_main_sha']=='c6e0394b3152d21075328bf4f26e6c070229bf13'
assert sum(r['status']=='already_preserved_frozen_report_813' for r in assignment)==813
assert sum(r['status']=='already_preserved_same_content' for r in assignment)==861
assert sum(r['backlog'] for r in assignment)==3043
unit_sources={}
for row in assignment:
    if not row['backlog']: continue
    path=pathlib.PurePosixPath(row['source_path']); suffix=path.suffix.lower()
    if row['cost_kind']=='third_party_exclusion_review':
        cost=1+row['conflict_cost_added']
    else:
        base,threshold=(3,10000) if row['cost_kind']=='markdown_research_proof' else (3,8000) if row['cost_kind']=='python_cpp_verifier' else (1,20000)
        cost=base+min(12,math.ceil(row['source_bytes']/threshold))+row['conflict_cost_added']
    assert cost==row['file_cost']
    stem=path.name[:-len(path.suffix)] if path.suffix else path.name
    is_note=suffix in {'.md','.markdown'}
    is_verifier=suffix in {'.py','.cpp'} and stem.startswith('verify_')
    if is_verifier: stem=stem[len('verify_'):]
    family=bool((is_note or is_verifier) and stem.startswith(('target_a_','target_b_','target_c_','global_')))
    expected=re.sub(r'(\d{4})[-_](\d{2})[-_](\d{2})',r'\1_\2_\3',stem) if family else row['source_path']
    assert row['unit_key']==expected
    unit_sources.setdefault(row['unit_key'],[]).append(row)
for unit in units:
    members=unit_sources[unit['unit_key']]
    assert unit['file_count']==len(members)
    assert unit['total_cost']==sum(r['file_cost'] for r in members)
    assert unit['source_paths']==sorted(r['source_path'] for r in members)
loads=summary['starting_workloads'][:]
previous=None
for unit in units:
    key=(-unit['total_cost'],unit['unit_key'])
    assert previous is None or key>=previous
    previous=key
    owner=min(range(3),key=lambda i:(loads[i],i))
    assert unit['agent']==owner+1 and unit['workload_before']==loads[owner]
    loads[owner]+=unit['total_cost']
    assert unit['workload_after']==loads[owner]
assert loads==summary['final_workloads']==[4269,4269,4268]
assert {str(i+1):sum(u['agent']==i+1 for u in units) for i in range(3)}==summary['assigned_unit_counts']
assert {str(i+1):sum(r.get('agent')==i+1 for r in assignment) for i in range(3)}==summary['assigned_file_counts']
assert summary['workload_spread_points']==1 and summary['workload_spread_percent_of_mean']<0.03

assigned={r['source_path']:r for r in assignment if r.get('agent')==1 and r['backlog']}
main=load_jsonl(AGENT/'source-main-reconciliation.jsonl')
assert len(main)==len(assigned)==1013 and {r['source_path'] for r in main}==set(assigned)
main_copies=0
for row in main:
    source=assigned[row['source_path']]
    assert row['source_sha256']==source['source_sha256']
    assert row['assignment_unit']==source['unit_key'] and row['file_cost']==source['file_cost']
    if row.get('destination_path'):
        check_hash(REPO/row['destination_path'],row['payload_sha256'])
        if not row.get('payload_transformations'): assert row['source_sha256']==row['payload_sha256']
        main_copies+=1
assert main_copies==951 and len(main)-main_copies==62

heads=load_jsonl(EVIDENCE/'source-branches/source-branch-heads.jsonl')
assert len(heads)==69
for row in heads:
    ref_hash=sha(row['source_ref'].encode())
    assert ref_hash==row['refname_sha256']
    remainder=int(ref_hash,16)%3
    if row['disposition']=='unique_non_pr_branch_work':
        assert remainder==row['hash_remainder_mod_3']
        assert remainder+1==row['assigned_agent']
    else:
        assert row['assigned_agent'] is None
assert sum(r['assigned_agent']==1 and r['disposition']=='unique_non_pr_branch_work' for r in heads)==19
head_owner={r['source_ref']:r['assigned_agent'] for r in heads}
artifacts=load_jsonl(EVIDENCE/'source-branches/source-branch-artifacts.jsonl')
assert all(head_owner.get(r['source_ref'])==1 for r in artifacts)
assert {r['source_ref'] for r in artifacts} <= {ref for ref,owner in head_owner.items() if owner==1}
branch_payloads=[r for r in artifacts if r.get('destination_path')]
assert len(branch_payloads)==156
for row in branch_payloads:
    check_hash(REPO/row['destination_path'],row['payload_sha256'])
    if not row.get('payload_transformations'): assert row['source_sha256']==row['payload_sha256']

worktrees=load_jsonl(EVIDENCE/'source-dirty-worktrees/source-dirty-worktree-assignments.jsonl')
assert len(worktrees)==32
for row in worktrees:
    if row.get('source_path'):
        path_hash=sha(row['source_path'].encode())
        assert path_hash==row['path_sha256']
        assert int(path_hash,16)%3+1==row['assigned_agent']
    elif row.get('branch_hash_owner_if_known'):
        branch_hash=sha(row['source_ref'].encode())
        assert int(branch_hash,16)%3+1==row['branch_hash_owner_if_known']
    if row.get('destination_path'):
        assert row['actual_sha256']==row['frozen_snapshot_sha256']
        check_hash(REPO/row['destination_path'],row['payload_sha256'])
assert sum(r.get('assigned_agent')==1 and r.get('status')=='recoverable_agent1_snapshot' for r in worktrees)==10

pr=load_jsonl(EVIDENCE/'pr737/pr737-file-reconciliation.jsonl')
assert len(pr)==46
pr_payloads=[r for r in pr if r.get('destination_path')]
assert len(pr_payloads)==45
for row in pr_payloads:
    check_hash(REPO/row['destination_path'],row['payload_sha256'])
    if not row.get('payload_transformations'): assert row['source_sha256']==row['payload_sha256']
assert sum(r.get('source_lifecycle')=='unreviewed' for r in pr)==14
assert sum(r['destination_relation']=='same_path_different_content' for r in pr)==5
assert len(load_jsonl(EVIDENCE/'pr737/pr737-source-artifact-index-records.jsonl'))==13
edges=load_jsonl(EVIDENCE/'pr737/pr737-dependency-edges.jsonl')
assert len(edges)==86 and len({r['dependency_path'] for r in edges})==43
assert sum(r['disposition']=='third_party_literature_or_extraction_excluded_by_user_instruction' for r in edges)==2
assert sum(r['disposition']=='Agent1_source_main_dependency_preserved_in_own_shard' for r in edges)==1

payload=AGENT/'payload'
files=[p for p in payload.rglob('*') if p.is_file()]
assert not any(p.suffix.lower() in {'.pdf','.djvu','.ps','.epub'} for p in files)
assert not any('/extracted/images/' in p.as_posix() or '/extracted/text/' in p.as_posix() for p in files)
assert {p.relative_to(payload).parts[0] for p in files}=={'source-main','source-branches','source-dirty-worktrees','source-pr-737'}
assert not any(p.relative_to(payload).parts[0]=='source-main' and p.relative_to(payload).parts[1:3] in {('docs','state'),('docs','publication')} for p in files)
for path in files:
    data=path.read_bytes()
    assert b'/home/cinna/' not in data, f'owner path remains: {path}'
    assert not any(token in data for token in (b'ghp_',b'github_pat_',b'AKIA',b'-----BEGIN PRIVATE KEY-----')), f'credential-like marker: {path}'

guard_pattern=re.compile(rb'(?:global[\s_-]+lipschitz|inverse[\s_-]+phase)',re.I)
guarded=0
for ledger_path in (AGENT/'source-main-reconciliation.jsonl',EVIDENCE/'source-branches/source-branch-artifacts.jsonl'):
    for row in load_jsonl(ledger_path):
        dest=row.get('destination_path')
        if dest and guard_pattern.search((REPO/dest).read_bytes()):
            assert row.get('agent1_claim_restore_guard_note')
            guarded+=1
assert guarded==20

runs=load_json(AGENT/'verification/pr737-dependency-verification-results.json')
assert len(runs['results'])==15 and all(x['outcome']=='PASS' and x['exit_code']==0 for x in runs['results'])
comparisons=load_json(AGENT/'verification/pr737-certificate-comparisons.json')
assert len(comparisons)==7 and all(x['parsed_json_equal'] for x in comparisons)

print(json.dumps({'result':'PASS','source_files':len(assignment),'frozen_reports_not_copied':813,
                  'other_exact_matches_not_copied':861,'agent1_backlog_files':len(main),
                  'agent1_source_main_payloads':main_copies,'agent1_explicit_exclusions':len(main)-main_copies,
                  'final_workloads':loads,'workload_spread_points':max(loads)-min(loads),
                  'agent1_branch_heads':19,'agent1_branch_payloads':len(branch_payloads),
                  'agent1_dirty_snapshots':10,'pr737_paths':len(pr),
                  'pr737_archived_payloads':len(pr_payloads),'verifier_executions':len(runs['results']),
                  'certificate_comparisons':len(comparisons),'payload_file_count':len(files)},
                 indent=2,sort_keys=True))
