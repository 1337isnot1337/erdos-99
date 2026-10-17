"""Adversarial omissions in a real public corpus, not success-shaped fixtures."""
import contextlib,json,shutil,sys,tempfile,unittest
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from check_public import validate

class CorpusAttacks(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.temp=tempfile.TemporaryDirectory(prefix='e99-corpus-attacks-')
  cls.root=Path(cls.temp.name)/'repo'
  shutil.copytree(ROOT,cls.root,ignore=shutil.ignore_patterns('.git','__pycache__','.venv'))
 @classmethod
 def tearDownClass(cls):cls.temp.cleanup()
 @contextlib.contextmanager
 def omit(self,path):
  p=self.root/path;raw=p.read_bytes();p.unlink()
  try:yield
  finally:p.write_bytes(raw)
 @contextlib.contextmanager
 def alter(self,path,func):
  p=self.root/path;raw=p.read_bytes();p.write_text(func(raw.decode('utf-8')),encoding='utf-8',newline='\n')
  try:yield
  finally:p.write_bytes(raw)
 def errors(self):return validate(self.root)[0]
 def test_omitted_canonical_audit_is_rejected(self):
  s=yaml.safe_load((self.root/'docs/state/theorem-state.yaml').read_text(encoding='utf-8'))
  p=next(c['audit'] for c in s['targets']['target-c']['current_canonical_entries'] if c.get('audit'))
  with self.omit(p):self.assertTrue(any(p in e for e in self.errors()))
 def test_omitted_import_helper_is_rejected(self):
  p='research/verify_target_c_one_corner_vacancy_packet_2026_10_06.py'
  # This is an actual imported helper in the retained verifier network.
  import ast
  tree=ast.parse((self.root/p).read_text(encoding='utf-8'))
  names=[n.module for n in ast.walk(tree) if isinstance(n,ast.ImportFrom) and n.module]
  names += [a.name for n in ast.walk(tree) if isinstance(n,ast.Import) for a in n.names]
  q=next('research/'+n+'.py' for n in names if (self.root/('research/'+n+'.py')).is_file())
  with self.omit(q):self.assertTrue(any(q in e or Path(q).stem in e for e in self.errors()))
 def test_old_corrected_grid_proof_is_still_required(self):
  p='docs/reports/target_b_dual_tree_dense_grid_extraction_correction_2026-09-05.md'
  with self.omit(p):self.assertTrue(any(p in e for e in self.errors()))
 def test_private_task_prerequisite_is_rejected(self):
  def mutate(text):
   d=json.loads(text);d['tasks'][0]['canonical_dependencies'][0]['path']='../private/theorem.md';return json.dumps(d)
  with self.alter('docs/research/agent-task-catalog.json',mutate):self.assertTrue(any('private/theorem' in e for e in self.errors()))
 def test_removed_artifact_in_generated_graph_is_rejected(self):
  with self.alter('docs/state/THEOREM_GRAPH.generated.md',lambda t:t+'\n[proof](../missing-proof.md)\n'):
   self.assertTrue(any('stale generated' in e or 'missing-proof' in e for e in self.errors()))
 def test_conditional_premise_cannot_be_canonical(self):
  def mutate(text):
   s=yaml.safe_load(text);s['targets']['target-c']['current_canonical_entries'][0]['status']='conditional';return yaml.safe_dump(s,sort_keys=False)
  with self.alter('docs/state/theorem-state.yaml',mutate):self.assertTrue(any('lifecycle mismatch' in e or 'noncanonical premise' in e for e in self.errors()))
 def test_recovered_frozen_report_is_load_bearing(self):
  p='docs/reports/target_c_multishear_traffic_domination_2026-10-05.md'
  with self.omit(p):self.assertTrue(any(p in e for e in self.errors()))
 def test_cross_route_shared_theory_is_required(self):
  p='docs/theory/04-ambient-force-and-cap-transport.md'
  with self.omit(p):self.assertTrue(any(p in e for e in self.errors()))

if __name__=='__main__':unittest.main()
