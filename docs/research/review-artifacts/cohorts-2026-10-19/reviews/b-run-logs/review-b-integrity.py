import ast,hashlib,json,pathlib,subprocess,sys
repo='/home/cinna/.local/state/erdos99-merge/20261019/review-b'
run=pathlib.Path('/home/cinna/.local/state/erdos99-merge/20261019')
rows=json.load(open(run/'reviews/b-assignment.json'))
def git(*args): return subprocess.check_output(['git','-C',repo,*args])
def blob(commit,path): return git('show',f'{commit}:{path}')
results=[]
for row in rows:
 n=row['number']; head=row['head']; base=row['base']; api=json.load(open(run/f'prs/{n}.json'))
 actualhead=git('rev-parse',f'origin/pr/{n}').decode().strip()
 paths=sorted(f['filename'] for f in api['files'])
 diff=sorted(x for x in git('diff','--name-only',base,head).decode().splitlines() if x)
 mb=git('merge-base',head,base).decode().strip()
 modes=[]; parse_errors=[]; pin_errors=[]; pins_checked=0
 for p in diff:
  tree=git('ls-tree',head,'--',p).decode().split()
  modes.append({'path':p,'mode':tree[0] if tree else 'missing','type':tree[1] if len(tree)>1 else 'missing'})
  try: data=blob(head,p)
  except subprocess.CalledProcessError:
   parse_errors.append(f'missing head blob: {p}'); continue
  if p.endswith('.json'):
   try: json.loads(data)
   except Exception as e: parse_errors.append(f'{p}: {e}')
  elif p.endswith('.jsonl'):
   for i,line in enumerate(data.splitlines(),1):
    try: json.loads(line)
    except Exception as e: parse_errors.append(f'{p}:{i}: {e}')
  elif p.endswith('.py'):
   try: ast.parse(data.decode())
   except Exception as e: parse_errors.append(f'{p}: {e}')
  if p.endswith('/SOURCES.json'):
   src=json.loads(data)
   for item in src.get('inputs',[]):
    path=item.get('path'); expected=item.get('sha256'); commit=item.get('commit') or head
    if not path or not expected: continue
    pins_checked+=1
    try: actual=hashlib.sha256(blob(commit,path)).hexdigest()
    except subprocess.CalledProcessError: pin_errors.append(f'{path}: unavailable at {commit}'); continue
    if actual!=expected: pin_errors.append(f'{path}: {actual} != {expected} at {commit}')
 ok=actualhead==head and mb==base and len(paths)==api['pull']['changed_files']==row['changed_files']==len(diff) and paths==diff and all(m['mode'] in ('100644','100755') for m in modes) and not parse_errors and not pin_errors
 results.append({'number':n,'head':head,'head_ref_match':actualhead==head,'base':base,'merge_base':mb,'changed_files_api':api['pull']['changed_files'],'assignment_count':row['changed_files'],'github_inventory_count':len(paths),'git_inventory_count':len(diff),'inventory_match':paths==diff,'modes':modes,'json_jsonl_python_parse_errors':parse_errors,'source_pin_count':pins_checked,'source_pin_errors':pin_errors,'static_integrity_pass':ok})
print(json.dumps({'reviewer':'review_b','scope':'assigned 26 PR immutable-head static integrity','results':results,'all_pass':all(x['static_integrity_pass'] for x in results)},indent=2))
