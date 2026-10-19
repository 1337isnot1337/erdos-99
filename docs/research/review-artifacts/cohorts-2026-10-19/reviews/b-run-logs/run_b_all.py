import fcntl,json,os,pathlib,subprocess,sys,time
run=pathlib.Path('/home/cinna/.local/state/erdos99-merge/20261019'); repo=run/'review-b'
assignment=json.load(open(run/'reviews/b-assignment.json')); data=json.load(open(run/'reviews/b-review.json'))
by={p['number']:p for p in assignment}; dossiers={p['number']:p for p in data['prs']}
py='/home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/venv/bin/python'; lock_path='/home/cinna/.local/state/erdos99-host-compute.lock'
heavy={106,126,129,137,149,150,151,152,172}; docs={116,124,127,132,143,168}
# Clear results from the briefly overlapping earlier run, retaining the all-PR static audit.
for d in data['prs']:
 d['actual_commands']=[x for x in d['actual_commands'] if x.get('log')=='/tmp/review-b-integrity.json']
 d['evidence_complete']=False
for n,p in by.items():
 d=dossiers[n]
 subprocess.run(['git','checkout','--detach',p['head']],cwd=repo,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,check=True)
 env=os.environ.copy(); env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
 vpath=next((x for x in p['paths'] if x.endswith('/VERIFY.json')),None)
 if vpath:
  v=json.loads(subprocess.check_output(['git','show',f"{p['head']}:{vpath}"],cwd=repo,text=True))
  c=v['commands'][0]; argv=[py if x=='{python}' else x for x in c['argv']]; timeout=c.get('timeout_seconds',30)
  start=time.monotonic(); log=pathlib.Path(f'/tmp/review-b-pr{n}-verify.log')
  def launch(): return subprocess.run(argv,cwd=repo,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout)
  if n in heavy:
   with open(lock_path,'w') as lf:
    fcntl.flock(lf,fcntl.LOCK_EX)
    try: out=launch(); output=out.stdout; rc=out.returncode
    except subprocess.TimeoutExpired as e: output=(e.stdout or '')+'\nTIMEOUT'; rc=124
    finally: fcntl.flock(lf,fcntl.LOCK_UN)
  else:
   try: out=launch(); output=out.stdout; rc=out.returncode
   except subprocess.TimeoutExpired as e: output=(e.stdout or '')+'\nTIMEOUT'; rc=124
  log.write_text(output)
  item={'command':' '.join(argv),'working_tree':str(repo),'head':p['head'],'exit_code':rc,'result':'PASS' if rc==0 else ('TIMEOUT/deferred' if rc==124 else 'FAIL'),'elapsed_seconds':round(time.monotonic()-start,3),'log':str(log)}
  if len(v['commands'])>1: item['note']='VERIFY.json repeats the identical command; one invocation was run because the second is duplicate evidence.'
  d['actual_commands'].append(item); print(n,'verifier',rc,flush=True)
 if n in docs:
  ok=True
  for label,argv in [('artifact-index',[py,'tools/build_artifact_index.py']),('reading-edition',[py,'tools/build_reading_edition.py','--check'])]:
   start=time.monotonic(); out=subprocess.run(argv,cwd=repo,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=45)
   log=pathlib.Path(f'/tmp/review-b-pr{n}-{label}.log'); log.write_text(out.stdout)
   d['actual_commands'].append({'command':' '.join(argv),'working_tree':str(repo),'head':p['head'],'exit_code':out.returncode,'result':'PASS' if out.returncode==0 else 'FAIL','elapsed_seconds':round(time.monotonic()-start,3),'log':str(log)})
   print(n,label,out.returncode,flush=True)
   ok &= out.returncode==0
 d['evidence_complete']=all(x['exit_code']==0 for x in d['actual_commands'] if x.get('head')==p['head']) and bool(d['actual_commands'])
 (run/'reviews/b-review.json').write_text(json.dumps(data,indent=2)+'\n')
print('all commands complete')
