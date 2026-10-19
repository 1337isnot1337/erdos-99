import json,os,pathlib,subprocess,sys,time
run=pathlib.Path('/home/cinna/.local/state/erdos99-merge/20261019'); repo=run/'review-b'; data=json.load(open(run/'reviews/b-review.json'))
py='/home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/venv/bin/python'
for n in map(int,sys.argv[1:]):
 d=next(x for x in data['prs'] if x['number']==n); h=d['head']
 subprocess.run(['git','checkout','--detach',h],cwd=repo,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,check=True)
 env=os.environ.copy(); env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
 for name,argv in [('artifact-index',[py,'tools/build_artifact_index.py']),('reading-edition',[py,'tools/build_reading_edition.py','--check'])]:
  start=time.monotonic(); p=subprocess.run(argv,cwd=repo,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=45)
  log=pathlib.Path(f'/tmp/review-b-pr{n}-{name}.log'); log.write_text(p.stdout)
  d['actual_commands'].append({'command':' '.join(argv),'working_tree':str(repo),'head':h,'exit_code':p.returncode,'result':'PASS' if p.returncode==0 else 'FAIL','elapsed_seconds':round(time.monotonic()-start,3),'log':str(log)})
  print(n,name,p.returncode,round(time.monotonic()-start,3),flush=True)
 d['evidence_complete']=all(x['exit_code']==0 for x in d['actual_commands'] if x['head']==h)
 (run/'reviews/b-review.json').write_text(json.dumps(data,indent=2)+'\n')
