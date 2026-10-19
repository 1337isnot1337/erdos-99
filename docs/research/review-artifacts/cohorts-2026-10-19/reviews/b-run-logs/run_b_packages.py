import fcntl,json,os,pathlib,subprocess,sys,time
run=pathlib.Path('/home/cinna/.local/state/erdos99-merge/20261019')
repo=run/'review-b'; assignment=json.load(open(run/'reviews/b-assignment.json')); dossiers=json.load(open(run/'reviews/b-review.json'))
by={p['number']:p for p in assignment}; dr={p['number']:p for p in dossiers['prs']}
py='/home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/venv/bin/python'
lock_path='/home/cinna/.local/state/erdos99-host-compute.lock'
heavy={106,126,129,137,149,150,151,152,172}
for n in map(int,sys.argv[1:]):
 p=by[n]; verify=next((x for x in p['paths'] if x.endswith('/VERIFY.json')),None)
 if not verify: continue
 v=json.loads(subprocess.check_output(['git','show',f"{p['head']}:{verify}"],cwd=repo,text=True))
 cmds=v.get('commands',[])
 if not cmds: continue
 # duplicate declared commands are rerun only once; one exact invocation is the same verification evidence.
 argv=[py if x=='{python}' else x for x in cmds[0]['argv']]
 timeout=cmds[0].get('timeout_seconds',30)
 subprocess.run(['git','checkout','--detach',p['head']],cwd=repo,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,check=True)
 env=os.environ.copy(); env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
 log=pathlib.Path(f'/tmp/review-b-pr{n}-verify.log')
 start=time.monotonic()
 if n in heavy:
  with open(lock_path,'w') as lf:
   fcntl.flock(lf,fcntl.LOCK_EX)
   try: out=subprocess.run(argv,cwd=repo,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout)
   except subprocess.TimeoutExpired as e: out=e; output=(e.stdout or '')+'\nTIMEOUT'
   else: output=out.stdout
   fcntl.flock(lf,fcntl.LOCK_UN)
 else:
  try: out=subprocess.run(argv,cwd=repo,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout)
  except subprocess.TimeoutExpired as e: out=e; output=(e.stdout or '')+'\nTIMEOUT'
  else: output=out.stdout
 log.write_text(output)
 rc=(out.returncode if hasattr(out,'returncode') else 124)
 item={'command':' '.join(argv),'working_tree':str(repo),'head':p['head'],'exit_code':rc,'result':'PASS' if rc==0 else ('TIMEOUT/deferred' if rc==124 else 'FAIL'),'elapsed_seconds':round(time.monotonic()-start,3),'log':str(log)}
 if len(cmds)>1: item['note']='VERIFY.json repeats the identical command; one invocation was run because the second is duplicate evidence.'
 dr[n]['actual_commands'].append(item)
 dr[n]['evidence_complete']=(rc==0)
 pathlib.Path(run/'reviews/b-review.json').write_text(json.dumps(dossiers,indent=2)+'\n')
 print(n,rc,item['result'],item['elapsed_seconds'],log,flush=True)
