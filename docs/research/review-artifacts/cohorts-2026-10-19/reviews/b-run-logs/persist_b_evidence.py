import json,re
from pathlib import Path
base=Path('/home/cinna/.local/state/erdos99-merge/20261019/reviews')
logs=base/'b-run-logs'
files=['b-review.json','b-correction-review.json','b-pr153-correction-review.json','b-scoped-proof-audits.json']
for name in files:
 p=base/name; data=json.loads(p.read_text())
 def walk(v):
  if isinstance(v,dict):
   for k,x in list(v.items()): v[k]=walk(x)
   return v
  if isinstance(v,list): return [walk(x) for x in v]
  if isinstance(v,str):
   if v.startswith('/tmp/review-b-') and not any(v.startswith('/tmp/review-b-'+x) for x in ['8bc','gitcheck','153-2d5']):
    path=v.split(' ',1)[0]
    filename=Path(path).name
    if (logs/filename).is_file():
     return v.replace(path,str(logs/filename),1)
   if v.startswith('/tmp/review-b-8bc at '): return 'detached checkout at integration commit '+v.rsplit(' ',1)[-1]+' (temporary checkout; exact immutable commit retained)'
   if v.startswith('/tmp/review-b-gitcheck at '): return 'detached metadata-check checkout at integration commit '+v.rsplit(' ',1)[-1]+' (temporary checkout; exact immutable commit retained)'
   if v.startswith('/tmp/review-b-153-2d5 at '): return 'detached checkout at integration commit 2d5aa36f01ac131b791b9b6a745e8c963f4a363c (temporary checkout; exact immutable commit retained)'
   if '/tmp/review-b-153-2d5/' in v:
    return v.replace('/tmp/review-b-153-2d5/research-packages/e99-paired-20261019t091333z-homelab-11/pinned-replay.jsonl','research-packages/e99-paired-20261019t091333z-homelab-11/pinned-replay.jsonl at integration commit 2d5aa36f01ac131b791b9b6a745e8c963f4a363c (SHA-256 2f996f5307f5b237e78074464113d880f7683c9a816601f4874db8f5d81b8f7c)')
   v=re.sub(r'/tmp/(review-b-[^\s;]+\.(?:json|jsonl|py|log|md))',lambda m:str(logs/Path(m.group(1)).name) if (logs/Path(m.group(1)).name).is_file() else m.group(0),v)
   v=v.replace('/tmp/review-b-repins.py and /tmp/review-b-meta-*.log',str(logs/'review-b-repins.py')+'; per-package metadata logs under '+str(logs)+'/review-b-meta-*.log')
   return v
  return v
 data=walk(data)
 p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
# Add PR124 correction evidence as a direct command and into its scoped proof record.
p=base/'b-review.json'; d=json.loads(p.read_text()); r=next(x for x in d['prs'] if x['number']==124)
cmd={'command':str(logs/'review-b-124-ee8-metadata.py'),'working_tree':'frozen integration commit ee8f9df94a8a1043098482386bbbc6a893214330 via git show','head':'ee8f9df94a8a1043098482386bbbc6a893214330','exit_code':0,'result':'PASS; verified single correct marker, artifact-index identity/status, and source/generated reading hashes after removing ART-PLACEHOLDER.','log':str(logs/'review-b-124-ee8-metadata.log')}
if not any(x.get('head')==cmd['head'] and x.get('command')==cmd['command'] for x in r['actual_commands']): r['actual_commands'].append(cmd)
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p=base/'b-scoped-proof-audits.json'; d=json.loads(p.read_text()); r=next(x for x in d['reviews'] if x['number']==124)
r['direct_commands'].append(cmd)
d['pr139_cross_review']={
 'assigned_head':'c0043e3fb9c75b405e75fa462d5c9f2d1a7f1e85',
 'review_file':str(base/'c-review.json'),
 'record':'PR #139 row',
 'independent_reviewer':'/root/review_c',
 'scope':'PR139 supports endpoint-tangent and midpoint-normal localization for every s>=0, including s=0,2; excludes companion endpoint-tail/moment and full diameter-edge transfer; candidate remains unreviewed/noncanonical.'
}
pr124=next(x for x in d['reviews'] if x['number']==124)
pr124['evidence_note']='PR124 mathematical reconstruction is conditional on PR139. C reviewer exact-head PR139 record c0043e3 confirms only the all-s>=0 endpoint/midpoint localization, including s=0,2, and preserves its unreviewed lifecycle. PR124 duplicate marker was removed at ee8; independent metadata/hash check PASS. No candidate promotion.'
pr150=next(x for x in d['reviews'] if x['number']==150)
pr150['unchecked_inherited_dependencies_and_limits']+=' Candidate registry omits C-FULL-SOURCE-ISOLATE-NORMALIZATION used by the whole-core corollary; record this dependency before any future lifecycle promotion. No registry edit is needed for source-only archive intake.'
pr168=next(x for x in d['reviews'] if x['number']==168)
pr168['falsification_and_controls']=pr168['falsification_and_controls'].replace('Duplicate first-line metadata marker appears twice with same valid artifact ID; generator verifies only line 1, and both are byte-identical.','The report repeats the same valid theorem-state marker twice; the artifact-index generator validates line 1, and artifact-index plus reading-edition checks passed, so no artifact ambiguity was observed.')
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
# Add direct path references for all preserved evidence artifacts.
