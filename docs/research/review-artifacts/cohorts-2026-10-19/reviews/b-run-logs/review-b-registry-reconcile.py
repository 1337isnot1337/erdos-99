import json,subprocess,hashlib
repo='/home/cinna/.local/state/erdos99-merge/20261019/review-b'
commits=['8bc3d8f10ecf7204078f8db66005dfc0551263c6','2d5aa36f01ac131b791b9b6a745e8c963f4a363c','e185b58bfffa27be92d4ec91d919f1aa4f939725','ee8f9df94a8a1043098482386bbbc6a893214330']
def show(c,p): return subprocess.check_output(['git','show',f'{c}:{p}'],cwd=repo)
checks=[]
for c in commits:
 d=json.loads(show(c,'docs/targets/target-c/candidate-registry.json'))
 by={x['candidate_id']:x for x in d['entries']}
 pos=by['TARGET-C-POSITIVE-LEAF-ANCHOR-D23-PR947']
 near=by['TARGET-C-NEAR-DIAMETER-PAIR-MIDPOINT-BOUND-PR947']
 checks.append({
  'commit':c,
  'positive_leaf_status_kept_unreviewed_strengthening':pos['status']=='unreviewed strengthening candidate; destination keeps the weaker canonical bound',
  'positive_leaf_validation_conditional_on_pr139':('PR #139' in pos['validation']['scope'] and 's=0' in pos['validation']['scope'] and 's=2' in pos['validation']['scope']),
  'near_diameter_status_unreviewed':near['status']=='unreviewed',
  'near_diameter_scope_all_s_including_endpoints':('all s>=0' in near['validation']['scope'] and 's=0' in near['validation']['scope'] and 's=2' in near['validation']['scope']),
  'no_promotion_or_state_change':('candidate lifecycle remains unreviewed' in pos['validation']['status'] and 'candidate lifecycle remains unreviewed' in near['validation']['status'])
 })
# Confirm assigned exact PR139 report scope.
pr139='c0043e3fb9c75b405e75fa462d5c9f2d1a7f1e85'
r=show(pr139,'docs/audits/target_c_near_diameter_pair_midpoint_destination_audit_2026-10-19.md').decode()
checks.append({'pr139_head':pr139,'report_says_all_s_ge_0':('every `s >= 0`' in r),'report_explicit_s0_s2':'s=0' in r and 's=2' in r,'report_excludes_companion_claims':'does not audit the companion endpoint-tail/moment or full diameter-edge transfer' in r,'candidate_not_promoted':'candidate remains `unreviewed`' in r})
# Confirm the PR124 integration marker repair and generated hashes at ee8.
c='ee8f9df94a8a1043098482386bbbc6a893214330'; path='docs/audits/target_c_positive_leaf_anchor_destination_review_2026-10-18.md'
s=show(c,path); read=show(c,'reading/'+path); index=json.loads(next(x for x in show(c,'docs/state/artifact-index.jsonl').decode().splitlines() if path in x)); manifest=json.loads(show(c,'reading/manifest.json')); item=next(x for x in manifest['documents'] if x['source']==path)
checks.append({'pr124_marker_repair_at_ee8':sum(1 for x in s.decode().splitlines() if '<!-- theorem-state:' in x)==1,'artifact_unreviewed_noncanonical_at_ee8':index['status']=='unreviewed' and index['canonical'] is False,'reading_source_hash_matches':hashlib.sha256(s).hexdigest()==item['source_sha256'],'reading_generated_hash_matches':hashlib.sha256(read).hexdigest()==item['reading_sha256']})
assert all(all(v for k,v in x.items() if k not in ('commit','pr139_head')) for x in checks), checks
print(json.dumps({'result':'PASS','checks':checks},indent=2))
