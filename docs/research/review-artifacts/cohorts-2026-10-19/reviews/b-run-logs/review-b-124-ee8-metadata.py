import subprocess,hashlib,json
c='ee8f9df94a8a1043098482386bbbc6a893214330'; w='/home/cinna/.local/state/erdos99-merge/20261019/review-b'
def show(p): return subprocess.run(['git','-C',w,'show',f'{c}:{p}'],capture_output=True,check=True).stdout
src='docs/audits/target_c_positive_leaf_anchor_destination_review_2026-10-18.md'; read='reading/docs/audits/target_c_positive_leaf_anchor_destination_review_2026-10-18.md'
index=json.loads(next(x for x in show('docs/state/artifact-index.jsonl').decode().splitlines() if src in x)); manifest=json.loads(show('reading/manifest.json'))
item=next(x for x in manifest['documents'] if x.get('source')==src); s=show(src); rd=show(read)
expected={'artifact_id':index['artifact_id'],'canonical':index['canonical'],'claim_ids':index['claim_ids'],'claim_statuses':index['claim_statuses'],'index':'docs/state/artifact-index.jsonl','status':index['status'],'target':index['target']}
expected_line='<!-- theorem-state: '+json.dumps(expected,sort_keys=True,separators=(',',':'))+' -->'
checks={'exactly_one_theorem_state_marker':sum(1 for x in s.decode().splitlines() if '<!-- theorem-state:' in x)==1,'first_marker_matches_artifact_index':s.decode().splitlines()[0]==expected_line,'artifact_still_unreviewed_noncanonical':index['status']=='unreviewed' and index['canonical'] is False,'reading_manifest_source_hash_matches':hashlib.sha256(s).hexdigest()==item['source_sha256'],'reading_manifest_reading_hash_matches':hashlib.sha256(rd).hexdigest()==item['reading_sha256'],'artifact_index_path_and_id_match':index['artifact_id']=='ART-7B6F9C6B4A70' and index['path']==src}
print(json.dumps({'commit':c,'checks':checks,'result':'PASS' if all(checks.values()) else 'FAIL'},indent=2))
if not all(checks.values()): raise SystemExit(1)
