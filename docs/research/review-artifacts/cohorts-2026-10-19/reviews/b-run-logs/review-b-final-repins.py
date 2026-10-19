import hashlib,json,subprocess,pathlib
repo='/home/cinna/.local/state/erdos99-merge/20261019/review-b'; run='/home/cinna/.local/state/erdos99-merge/20261019'
A=json.load(open(run+'/reviews/b-assignment.json')); pkgs={x.split('/README.md')[0] for p in A for x in p['paths'] if x.startswith('research-packages/') and x.endswith('/README.md')}
rows=json.load(open(run+'/final-metadata-repins.json')); final='e185b58bfffa27be92d4ec91d919f1aa4f939725'; checks=[]
for row in rows:
 if row['package'] not in pkgs: continue
 old=subprocess.check_output(['git','show',f"{row['old_commit']}:{row['path']}"],cwd=repo)
 new=subprocess.check_output(['git','show',f"{row['new_commit']}:{row['path']}"],cwd=repo)
 sources=json.loads(subprocess.check_output(['git','show',f"{final}:{row['package']}/SOURCES.json"],cwd=repo,text=True))
 pin=next((x for x in sources['inputs'] if x.get('path')==row['path']),None)
 checks.append({'package':row['package'],'path':row['path'],'old_commit':row['old_commit'],'new_commit':row['new_commit'],'old_sha_matches':hashlib.sha256(old).hexdigest()==row['old_sha256'],'new_sha_matches':hashlib.sha256(new).hexdigest()==row['new_sha256'],'final_sources_pin_matches':pin is not None and pin['sha256']==row['new_sha256'] and pin.get('commit')==row['new_commit']})
print(json.dumps({'rows_checked':len(checks),'checks':checks,'all_pass':bool(checks) and all(x['old_sha_matches'] and x['new_sha_matches'] and x['final_sources_pin_matches'] for x in checks)},indent=2))
