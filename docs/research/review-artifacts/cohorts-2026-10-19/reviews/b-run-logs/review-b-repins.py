import hashlib,json,pathlib,subprocess
repo='/home/cinna/.local/state/erdos99-merge/20261019/review-b'
root=pathlib.Path('/home/cinna/.local/state/erdos99-merge/20261019')
assign=json.load(open(root/'reviews/b-assignment.json'))
packages=set()
for row in assign:
 for p in row['paths']:
  if p.startswith('research-packages/') and p.count('/')>1:
   packages.add('/'.join(p.split('/')[:2]))
entries=json.load(open(root/'integration-metadata-repins.json'))
relevant=[e for e in entries if e['package'] in packages]
def blob(commit,path):
 b=subprocess.check_output(['git','-C',repo,'show',f'{commit}:{path}'])
 return hashlib.sha256(b).hexdigest()
errors=[]; details=[]
for e in relevant:
 p=e['path'];old=blob(e['old_commit'],p);new=blob(e['new_commit'],p)
 src=json.loads(subprocess.check_output(['git','-C',repo,'show',f"173b3dd14fa784f65f80bb9485b0f72ed1a36916:{e['package']}/SOURCES.json"]))
 cand=[i for i in src.get('inputs',[]) if i.get('path')==p]
 ok=old==e['old_sha256'] and new==e['new_sha256'] and len(cand)==1 and cand[0].get('commit')==e['new_commit'] and cand[0].get('sha256')==e['new_sha256']
 if not ok: errors.append(e)
 details.append({'package':e['package'],'path':p,'old_hash_verified':old==e['old_sha256'],'new_hash_verified':new==e['new_sha256'],'source_pin_matches_repin':len(cand)==1 and cand[0].get('commit')==e['new_commit'] and cand[0].get('sha256')==e['new_sha256']})
# Ensure only metadata changed within these packages from 8bc to 173.
for package in packages:
 for name in ('README.md','TASK.json','VERIFY.json','verify.py'):
  path=f'{package}/{name}'
  a=subprocess.run(['git','-C',repo,'rev-parse',f'8bc3d8f10ecf7204078f8db66005dfc0551263c6:{path}'],capture_output=True,text=True)
  b=subprocess.run(['git','-C',repo,'rev-parse',f'173b3dd14fa784f65f80bb9485b0f72ed1a36916:{path}'],capture_output=True,text=True)
  if a.returncode==0 and b.returncode==0 and a.stdout!=b.stdout: errors.append({'unexpected_changed_nonmetadata':path})
print(json.dumps({'assigned_packages_with_repins':sorted({e['package'] for e in relevant}),'verified_repin_rows':len(relevant),'details':details,'unexpected_errors':errors},indent=2))
if errors: raise SystemExit(1)
