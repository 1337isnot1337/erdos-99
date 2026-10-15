#!/usr/bin/env python3
"""List full task prerequisites and reachable registered certificate commands."""
from pathlib import Path
import argparse,json,yaml
from run_theorem_certificates import entries
ROOT=Path(__file__).resolve().parents[1]
def context(task_id):
 cat=json.loads((ROOT/'docs/research/agent-task-catalog.json').read_text())
 task=next(t for t in cat['tasks'] if t['id']==task_id)
 inc=json.loads((ROOT/'docs/publication/inclusion.json').read_text())
 graph={r['public_path']:set(r.get('dependencies',[])) for r in inc['entries']}
 seen={r['path'] for k in ('canonical_dependencies','previous_obstructions') for r in task[k]};todo=list(seen)
 while todo:
  p=todo.pop()
  for q in graph.get(p,[]):
   if q not in seen:seen.add(q);todo.append(q)
 state=yaml.safe_load((ROOT/'docs/state/theorem-state.yaml').read_text());certs=set()
 for c in entries(state):
  if {c.get('report'),c.get('audit')} & seen:
   certs.update(c.get('certificates',[]))
 print(json.dumps({'task':task_id,'question':task['question'],'read_first':[r['path'] for r in task['canonical_dependencies']],
  'transitive_file_prerequisites':sorted(seen),'certificate_commands':['python '+p for p in sorted(certs)],
  'note':'Read complete statements and inline section references too; file reachability is not mathematical proof. A proof-only task may have no registered certificate.'},indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('task_id');context(p.parse_args().task_id)
