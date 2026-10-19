import json
from pathlib import Path
base=Path('/home/cinna/.local/state/erdos99-merge/20261019/reviews')
p=base/'b-review.json'
d=json.loads(p.read_text())
row=next(x for x in d['prs'] if x['number']==124)
row['coverage']=(
    'Independent destination review of PR #124 positive-leaf anchor sharpening: assuming PR #139 near-diameter '
    'localization at s=0 and s=2, the full-source KKT cone and an inner-ball contraction imply '
    'dist(a, partial K_D)=O(D^(-2/3)). This is conditional; PR #139 localization is a separate unreviewed '
    'candidate. No endpoint-tail/moment or full diameter-edge transfer, vacancy, packet, source motion, or '
    'theorem promotion is included.'
)
row['source_bindings']={
  'report': {
    'path':'docs/audits/target_c_positive_leaf_anchor_destination_review_2026-10-18.md',
    'revision':row['head'],
    'sha256':'492b87c9276752cae74f1218b48b07a4200ea0f91f38092b505f55c69a4c9dcf',
    'git_blob':'c319d0c9ca4d983e9b3e768f8c0cd26dbf7ee61c',
    'artifact_id':'ART-7B6F9C6B4A70',
    'canonical':False,'status':'unreviewed'
  },
  'reviewed_inputs':[
    {'candidate':'TARGET-C-POSITIVE-LEAF-ANCHOR-D23-PR947','source_pr':947,'head':'1afb7e64d47c5619d872d32759b0e01f1526fd5a','status':'unreviewed strengthening candidate'},
    {'candidate':'TARGET-C-NEAR-DIAMETER-PAIR-MIDPOINT-BOUND-PR947','audit_pr':139,'audit_report':'docs/audits/target_c_near_diameter_pair_midpoint_destination_audit_2026-10-19.md','audit_revision':'8bc3d8f10ecf7204078f8db66005dfc0551263c6','audit_git_blob':'4ac98647466f92d6a5ba4ea00bc7b21dfb8c19d7','status':'candidate unreviewed; localization component audit PASS'},
    {'canonical_claim':'C-FS-GEOM','role':'full-source circumradius bound R<=D/2+3^(1/4)*sqrt(D)'},
    {'canonical_claim':'C-FS-DIAMETER-MIDPOINT-D2-3','role':'endpoint tangent estimate and actual diameter normal estimate at s=0'}
  ]
}
row['dependencies_and_evidence_reuse']=(
    'Reconstructed the conditional geometry from PR #124 exact-head prose and canonical interfaces. The near-diameter '
    'estimates for the same source at s=0 and s=2 are a separate PR #139 result and are used only as premises; '
    'PR #139 independently reviews the localization component for all s>=0, but its candidate lifecycle remains '
    'unreviewed and its companion endpoint-tail/moment/full-diameter transfer claims are excluded. No full historical '
    'proof-chain reconstruction was performed.'
)
row['scope_limitations']=[
    'Conditional on the PR #139 endpoint-tangent bounds at s=0 and s=2; this audit does not re-prove the near-diameter candidate.',
    'Only the positive-leaf cone-to-boundary-contraction implication is covered; no count, vacancy, packet, source-realized move, or global result.',
    'The exact PR head contains a second theorem-state marker with ART-PLACEHOLDER. The generator validates only the first-line marker; integration cleanup is tracked separately.',
    'No full historical canonical proof chain was reconstructed.'
]
row['open_obligations']=[
    'Keep both candidate lifecycles unreviewed/noncanonical; independently establish the complete near-diameter candidate before relying on its premise for adoption.',
    'Connect boundary localization to a source-realized move with every label and pair constraint.'
]
row['necessary_repairs']=[
    'The PR #124 report contains a duplicate theorem-state comment at line 4 with ART-PLACEHOLDER. Root reports removing it at integration commit ee8f9df94a8a1043098482386bbbc6a893214330; independently verify that exact correction and regenerated views before snapshot.'
]
# repair the malformed recorded hash in PR143 source binding
r143=next(x for x in d['prs'] if x['number']==143)
for x in r143['source_bindings'].get('reviewed_inputs',[]):
    if x.get('path','').endswith('/TASK.json'):
        x['sha256']='36656f1a9651485438874376ee7dac47996deee6b51db16096463a7a09f2173e'
# Attach independent exact finite PR143 check.
r143['actual_commands'].append({
 'command':'/home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/venv/bin/python /tmp/review-b-143-independent.py',
 'working_tree':'standalone Fraction reconstruction from PR #143 exact report coordinates; no repository source edits',
 'head':r143['head'],'exit_code':0,
 'result':'PASS; reconstructed 51 labels and all 1,275 pairs; minimum squared distance 1; maximum 84 attained only by retained wall pair ((0,7),(7,0)); all 1,170 pairs involving moved labels are strictly above 1; all pairs <= original D^2=112.',
 'log':'/tmp/review-b-143-independent.log'
})
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')

p=base/'b-correction-review.json'; c=json.loads(p.read_text())
c['candidate_registry_reconciliation_at_8bc']={
 'path':'docs/targets/target-c/candidate-registry.json',
 'commits_checked':['8bc3d8f10ecf7204078f8db66005dfc0551263c6','2d5aa36f01ac131b791b9b6a745e8c963f4a363c','e185b58bfffa27be92d4ec91d919f1aa4f939725'],
 'pr124_candidate':{
   'candidate_id':'TARGET-C-POSITIVE-LEAF-ANCHOR-D23-PR947',
   'status':'unreviewed strengthening candidate; destination keeps the weaker canonical bound',
   'lifecycle':'Source proposes sharpening the canonical O(D^(-1/2)) positive-leaf anchor statement to O(D^(-2/3)); adoption not performed.',
   'accepted_component_scope':'PR #124 report proves only the cone-to-boundary-contraction implication conditional on PR #139 near-diameter localization at s=0 and s=2. The stronger exponent is not promoted.',
   'open_obligations':['Independently establish the full near-diameter premise before any adoption.','Connect boundary localization to a full-source movement with all labels and pair constraints.']
 },
 'pr139_candidate':{
   'candidate_id':'TARGET-C-NEAR-DIAMETER-PAIR-MIDPOINT-BOUND-PR947',
   'status':'unreviewed',
   'lifecycle':'Source PR proposes canonical all-source localization; destination has not adopted it.',
   'accepted_component_scope':'PR #139 destination audit passes endpoint-tangent and midpoint-normal localization only for all s>=0, explicitly including s=0 and s=2. It excludes companion endpoint-tail/moment and full diameter-edge transfer claims.',
   'open_obligation':'Source-level counting or replacement argument must use localization without assuming an unproved global atlas.'
 },
 'verdict':'Exact registry reconciliation is correctly attributed: PR #124 is the conditional positive-leaf implication; PR #139 is the near-diameter localization premise. Both candidates remain unreviewed/noncanonical, and the weaker canonical O(D^(-1/2)) bound remains authoritative; no theorem-state change or exponent promotion.'
}
p.write_text(json.dumps(c,indent=2,ensure_ascii=False)+'\n')

p=base/'b-pr153-correction-review.json'; s=json.loads(p.read_text())
for cmd in s['actual_commands']:
    if 'PENDING shared compute lock' in cmd.get('result',''):
       cmd.update({
         'exit_code':0,
         'result':'PASS; independently reran the original source verifier at exact amended integration commit under the host compute lock, single-threaded with a 120s timeout. It emitted H=30,31,100 and symbolic-limit rows; all 225,680 enumerated support pairs and the 13 critical-pair/5,858 strict-limit checks passed, every row reported global_minimizer=false, and stdout matched pinned-replay.jsonl byte for byte.',
         'log':'/tmp/review-b-153-source-verifier.log',
         'timeout_seconds':120,
         'stdout_comparison':'PASS cmp -s against /tmp/review-b-153-2d5/research-packages/e99-paired-20261019t091333z-homelab-11/pinned-replay.jsonl'
       })
s['evidence_complete']=True
p.write_text(json.dumps(s,indent=2,ensure_ascii=False)+'\n')
