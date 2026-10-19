import hashlib,json,subprocess
repo='/home/cinna/.local/state/erdos99-merge/20261019/review-b'
base='7d0a450fe66991036541023f95c44c064a04b6a8'; amended='2d5aa36f01ac131b791b9b6a745e8c963f4a363c'
pkg='research-packages/e99-paired-20261019t091333z-homelab-11'
def show(rev,path): return subprocess.check_output(['git','show',f'{rev}:{path}'],cwd=repo)
src=json.loads(show(amended,pkg+'/SOURCES.json'))
rows=[]
for x in src['inputs']:
 rev=x.get('commit',amended); raw=show(rev,x['path'])
 rows.append({'path':x['path'],'commit':rev,'sha_matches':hashlib.sha256(raw).hexdigest()==x['sha256'],'sha256':hashlib.sha256(raw).hexdigest(),'pin':x['sha256']})
# Check the imported candidate registry's source report/verifier/certificate bindings.
r=json.loads(show(amended,'docs/targets/target-c/candidate-registry.json'))
e=next(e for e in r['entries'] if e['candidate_id']=='TARGET-C-PR952-UNEQUAL-HEIGHT-ISOLATE-TRANSPORT')
art=[]
for a in e['artifacts']:
 path=a['path']; raw=show(base,path)
 art.append({'path':path,'baseline_sha_matches':hashlib.sha256(raw).hexdigest()==a['source_sha256'],'sha256':hashlib.sha256(raw).hexdigest(),'baseline_blob':subprocess.check_output(['git','rev-parse',f'{base}:{path}'],cwd=repo,text=True).strip(),'claimed_blob':a.get('source_git_blob_sha')})
print(json.dumps({'package_source_pins':rows,'candidate_artifact_pins':art,'all_pass':all(x['sha_matches'] for x in rows) and all(x['baseline_sha_matches'] and x['baseline_blob']==x['claimed_blob'] for x in art)},indent=2))
