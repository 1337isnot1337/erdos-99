from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.localized_ci.packages import Invalid, path, strict_json
from tools.localized_ci.plan import Snapshot, git, make_plan, revision
from tools.localized_ci.replay import integrity, replay, execute, sandbox_prefix
from tools.local_ci import security

ROOT = Path(__file__).resolve().parents[1]


class Repository(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='e99-ci-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        self.root.mkdir()
        self.output = Path(self.temp.name) / 'output'
        self.run_git('init', '-q')
        self.run_git('config', 'user.name', 'CI Test')
        self.run_git('config', 'user.email', 'ci-test@example.invalid')
        self.write('README.md', 'fixture\n')
        self.write('helpers/deep.py', 'def value():\n    return 42\n')
        self.write('helpers/mid.py', 'from helpers.deep import value\n')
        self.write('helpers/__init__.py', '')
        self.write('data/all.txt', 'all-domain-input\n')
        self.anchor = self.commit()
        self.package('alpha')
        self.base = self.commit()

    def run_git(self, *args):
        return git(self.root, *args).decode().strip()

    def write(self, p, content):
        target = self.root / p
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)

    def read_json(self, p):
        return json.loads((self.root / p).read_text())

    def json(self, p, data):
        self.write(p, json.dumps(data, indent=2) + '\n')

    def commit(self):
        self.run_git('add', '-A')
        self.run_git('commit', '-qm', 'fixture', '--allow-empty')
        return self.run_git('rev-parse', 'HEAD')

    def package(self, name, extra=(), deps=(), code=None):
        d = f'research-packages/{name}'
        verifier = d + '/verify.py'
        self.write(verifier, code or 'for x in range(10):\n    assert x * x >= 0\nprint("passed exact 10-case fixture")\n')
        self.write(d + '/README.md', '# Scoped regression\nResult, limits and reproduction.\n')
        self.json(d + '/TASK.json', dict(version=1,id=name,scope=dict(statement='fixture only',domain='all integers 0..9',limitations='finite regression, no E99 claim'),result='finite fixture',remaining_questions=['global theorem remains open'],classification='regression'))
        inputs = [verifier, *extra]
        self.json(d + '/SOURCES.json', dict(version=1,baseline_commit=self.anchor,inputs=[dict(path=p,sha256=hashlib.sha256((self.root/p).read_bytes()).hexdigest(),identity=p,generated_from=[]) for p in inputs],packages=list(deps),unresolved=[]))
        self.json(d + '/VERIFY.json',dict(version=1,inputs=inputs,environment=dict(python='3.14',dependencies=[]),commands=[dict(argv=['{python}',verifier],timeout_seconds=5)],domain='all integers 0..9'))
        return d

    def repin(self, name='alpha'):
        p = f'research-packages/{name}/SOURCES.json'
        sources = self.read_json(p)
        for item in sources['inputs']:
            item['sha256'] = hashlib.sha256((self.root/item['path']).read_bytes()).hexdigest()
        self.json(p, sources)

    def plan(self):
        return make_plan(self.root, self.base)

    def full(self, plan=None):
        plan = plan or self.plan()
        self.assertEqual(plan['level'], 'full-verification-required', plan)
        self.assertFalse(plan['full_verified'])
        self.assertFalse(plan['replay_allowed'])
        return plan

    def test_documentation_fast_only(self):
        self.write('README.md','documentation\n'); self.commit()
        p = self.plan()
        self.assertEqual(p['level'], 'fast-only')
        self.assertFalse(p['full_verified']); self.assertFalse(p['replay_allowed'])

    def test_direct_package_change_replays_only_it(self):
        self.package('beta'); self.base = self.commit()
        self.write('research-packages/alpha/README.md', 'clarify result\n'); self.commit()
        p = self.plan()
        self.assertEqual(p['level'], 'targeted-replay', p)
        self.assertEqual(p['packages'], ['research-packages/alpha'])
        self.assertFalse(p['full_verified'])

    def test_new_package_needs_no_historical_retrofit(self):
        self.package('beta'); self.commit()
        self.assertEqual(self.plan()['packages'], ['research-packages/beta'])

    def test_declared_outside_input_and_transitive_helper(self):
        self.package('alpha', ('helpers/deep.py','helpers/mid.py','helpers/__init__.py'), code='from helpers.mid import value\nassert value() == 42\n')
        self.base = self.commit()
        self.write('helpers/deep.py','def value():\n    return 6 * 7\n')
        self.repin(); self.commit()
        p = self.plan()
        self.assertEqual(p['level'], 'targeted-replay', p)
        self.assertEqual(p['packages'], ['research-packages/alpha'])
        result = replay(self.root, p, self.output)
        self.assertEqual(result['status'], 'passed', result)
        self.assertFalse(result['full_verified'])

    def test_deleted_source(self):
        self.package('alpha', ('data/all.txt',)); self.base=self.commit()
        (self.root/'data/all.txt').unlink(); self.commit()
        p=self.full(); self.assertIn('research-packages/alpha', p['affected_packages'])

    def test_renamed_input_records_both_names(self):
        self.package('alpha', ('data/all.txt',)); self.base=self.commit()
        self.run_git('mv','data/all.txt','data/renamed.txt'); self.commit()
        p=self.full()
        self.assertEqual({c['path'] for c in p['changes']}, {'data/all.txt','data/renamed.txt'})

    def test_deleted_package_requires_review(self):
        self.run_git('rm','-r','research-packages/alpha'); self.commit(); self.full()

    def test_shared_certificate_utility(self):
        self.write('tools/certificate_utils.py','shared foundation\n'); self.commit()
        p=self.full(); self.assertEqual(p['packages'], ['research-packages/alpha'])

    def test_canonical_theorem_change(self):
        self.write('docs/targets/target-c/CURRENT.md','canonical\n'); self.commit(); self.full()

    def test_state_generated_index_change(self):
        self.write('docs/state/artifact-index.jsonl','{}\n'); self.commit(); self.full()

    def test_declared_generated_input_selects_package(self):
        self.package('alpha', ('data/all.txt','helpers/deep.py'))
        source='research-packages/alpha/SOURCES.json'
        s=self.read_json(source); s['inputs'][1]['generated_from']=['helpers/deep.py']; self.json(source,s)
        self.base=self.commit()
        self.write('data/all.txt','new generated bytes\n'); self.repin(); self.commit()
        self.assertEqual(self.plan()['level'],'targeted-replay')

    def test_generated_input_missing_generator(self):
        source='research-packages/alpha/SOURCES.json'
        s=self.read_json(source); s['inputs'][0]['generated_from']=['helpers/deep.py']; self.json(source,s)
        self.commit(); self.full()

    def test_unknown_file(self):
        self.write('unknown.txt','unknown dependency\n'); self.commit(); self.full()

    def test_malformed_manifest(self):
        self.write('research-packages/alpha/TASK.json','{'); self.commit(); self.full()

    def test_symlink(self):
        (self.root/'research-packages/alpha/verify.py').unlink()
        (self.root/'research-packages/alpha/verify.py').symlink_to('/etc/passwd')
        self.commit(); self.full()

    def test_duplicate_source(self):
        p='research-packages/alpha/SOURCES.json'; s=self.read_json(p)
        s['inputs'].append(s['inputs'][0]); self.json(p,s); self.commit(); self.full()

    def test_duplicate_identity(self):
        self.package('alpha', ('data/all.txt',))
        p='research-packages/alpha/SOURCES.json'; s=self.read_json(p)
        s['inputs'][1]['identity']=s['inputs'][0]['identity']; self.json(p,s); self.commit(); self.full()

    def test_removed_dependency_cannot_hide_changed_input(self):
        self.package('alpha', ('data/all.txt',)); self.base=self.commit()
        self.package('alpha'); self.write('data/all.txt','changed\n'); self.commit()
        p=self.full(); self.assertEqual(p['packages'], ['research-packages/alpha'])

    def test_package_edges_select_transitive_dependents(self):
        self.package('beta', deps=['research-packages/alpha']); self.base=self.commit()
        self.write('research-packages/alpha/README.md','change\n'); self.commit()
        p=self.plan(); self.assertEqual(p['level'],'targeted-replay',p)
        self.assertEqual(p['packages'],['research-packages/alpha','research-packages/beta'])

    def test_removing_package_edge_requires_review(self):
        self.package('beta',deps=['research-packages/alpha']); self.base=self.commit()
        self.package('beta'); self.commit(); self.full()

    def test_cyclic_package_edges(self):
        self.package('alpha',deps=['research-packages/beta']); self.package('beta',deps=['research-packages/alpha'])
        self.commit(); self.full()

    def test_workload_cap(self):
        self.package('beta'); self.package('gamma'); self.base=self.commit()
        for name in ('alpha','beta','gamma'): self.write(f'research-packages/{name}/README.md','changed\n')
        self.commit(); self.full()

    def test_dynamic_import(self):
        self.package('alpha',code='module = __import__("os")\n'); self.commit(); self.full()

    def test_undeclared_transitive_import(self):
        self.package('alpha',('helpers/mid.py',),code='from helpers.mid import value\nassert value()==42\n')
        self.commit(); self.full()

    def test_undeclared_package_initializer(self):
        self.package('alpha', ('helpers/deep.py',), code='from helpers.deep import value\nassert value()==42\n')
        self.commit(); self.full()

    def test_undeclared_package_shadowing_standard_library_requires_review(self):
        self.write('math/__init__.py', 'def sqrt(value):\n    return 99\n')
        self.package('alpha', code='import math\nassert math.sqrt(4) == 2\n')
        self.base = self.commit()
        self.write('research-packages/alpha/README.md', 'Unchanged finite claim\n')
        self.commit()
        p = self.full()
        self.assertTrue(any('unresolved import math' in r for r in p['reasons']))
        with self.assertRaises(Invalid):
            replay(self.root, p, self.output)

    def test_declared_package_shadowing_standard_library_is_replayed(self):
        self.write('math/__init__.py', 'def sqrt(value):\n    return 99\n')
        self.package('alpha', ('math/__init__.py',),
                     code='import math\nassert math.sqrt(4) == 99\n')
        self.base = self.commit()
        self.write('research-packages/alpha/README.md', 'Local package claim\n')
        self.commit()
        p = self.plan()
        self.assertEqual(p['level'], 'targeted-replay', p)
        result = replay(self.root, p, self.output)
        self.assertEqual(result['status'], 'passed', result)

    def test_legacy_shared_helper_cannot_be_claimed_exclusive(self):
        self.write('research/shared_helper.py', 'value = 42\n')
        self.package('alpha', ('research/shared_helper.py',)); self.base=self.commit()
        self.write('research/shared_helper.py', 'value = 6 * 7\n'); self.repin(); self.commit()
        p=self.full(); self.assertIn('research-packages/alpha',p['affected_packages'])

    def test_arbitrary_external_input_does_not_establish_legacy_closure(self):
        self.write('research/legacy.py','print("legacy certificate")\n')
        self.write('docs/state/theorem-state.yaml','targets:\n  fixture:\n    regressions:\n      - certificates: [research/legacy.py]\n')
        self.package('alpha', ('data/all.txt',)); self.base=self.commit()
        self.write('data/all.txt','changed\n'); self.repin(); self.commit()
        p=self.full()
        self.assertTrue(any('unmodeled legacy' in s for s in p['reasons']))

    def test_forged_plan_cannot_authorize_more_work(self):
        self.write('research-packages/alpha/README.md','changed\n'); self.commit()
        p=self.plan(); p['workload_seconds']=0
        with self.assertRaises(Invalid): replay(self.root,p,self.output)

    def test_actual_namespace_hides_credentials_network_and_undeclared_files(self):
        # This exercises the runtime boundary directly, using trusted test code that
        # is deliberately outside the restricted package language.
        visible=Path(self.temp.name)/'visible'; visible.mkdir()
        (visible/'allowed.txt').write_text('declared')
        hidden=Path(self.temp.name)/'host-secret'; hidden.write_text('fixture-secret')
        code = '''import os,socket,pathlib
assert 'GITHUB_TOKEN' not in os.environ
assert 'PYTHONOPTIMIZE' not in os.environ
assert not pathlib.Path(%r).exists()
assert not pathlib.Path('/work/undeclared.txt').exists()
assert not pathlib.Path('/work/.git').exists()
try:
    pathlib.Path('/work/allowed.txt').write_text('mutated')
except OSError:
    pass
else:
    raise AssertionError('input is writable')
try:
    socket.create_connection(('1.1.1.1',443),timeout=.1)
except OSError:
    pass
else:
    raise AssertionError('network is reachable')
print('isolated')
''' % str(hidden)
        argv=sandbox_prefix([(visible,'/work')])+['--chdir','/work','--','/usr/bin/python3','-I','-S','-c',code]
        with patch.dict(os.environ,{'GITHUB_TOKEN':'fixture-secret','PYTHONOPTIMIZE':'2'}):
            r=execute(argv,5,Path(self.temp.name)/'isolation.log')
        self.assertEqual(r['status'],'passed',(Path(self.temp.name)/'isolation.log').read_text())

    def test_undeclared_filesystem_input(self):
        self.package('alpha',code='with open("data/all.txt") as f:\n    assert f.read()\n')
        self.commit(); self.full()

    def test_dynamic_filesystem_input(self):
        self.package('alpha',('data/all.txt',),code='name="data/all.txt"\nwith open(name) as f:\n    assert f.read()\n')
        self.commit(); self.full()

    def test_declared_unresolved_input(self):
        p='research-packages/alpha/SOURCES.json'; s=self.read_json(p); s['unresolved']=['data-dependent dynamic import']; self.json(p,s)
        self.commit(); self.full()

    def test_missing_merge_base(self):
        self.full(make_plan(self.root,'f'*40))

    def test_ambiguous_merge_base(self):
        original=git
        def ambiguous(root,*args):
            if args[:2]==('merge-base','--all'): return (self.anchor+'\n'+self.base+'\n').encode()
            return original(root,*args)
        with patch('tools.localized_ci.plan.git',side_effect=ambiguous): self.full()

    def test_real_criss_cross_ancestry(self):
        tree=self.run_git('rev-parse','HEAD^{tree}')
        left=self.run_git('commit-tree',tree,'-p',self.anchor,'-m','left')
        right=self.run_git('commit-tree',tree,'-p',self.anchor,'-m','right')
        first=self.run_git('commit-tree',tree,'-p',left,'-p',right,'-m','merge one')
        second=self.run_git('commit-tree',tree,'-p',right,'-p',left,'-m','merge two')
        self.run_git('checkout','--detach',first)
        self.full(make_plan(self.root,second))

    def test_advanced_base_new_dependent_is_not_invisible(self):
        self.package('alpha', ('data/all.txt',)); self.base=self.commit()
        self.package('beta', ('data/all.txt',)); target=self.commit()
        self.run_git('checkout','--detach',self.base)
        self.write('data/all.txt','new PR bytes\n'); self.repin(); self.commit()
        p=self.full(make_plan(self.root,target))
        self.assertEqual(p['affected_packages'],['research-packages/alpha','research-packages/beta'])

    def test_advanced_base_unrelated_package_does_not_expand_replay(self):
        self.package('beta'); target=self.commit()
        self.run_git('checkout','--detach',self.base)
        self.write('research-packages/alpha/README.md','PR clarification\n'); self.commit()
        p=make_plan(self.root,target)
        self.assertEqual(p['level'],'targeted-replay',p)
        self.assertEqual(p['packages'],['research-packages/alpha'])

    def test_advanced_base_changed_package_contract_needs_rebase(self):
        self.package('alpha',('data/all.txt',)); target=self.commit()
        self.run_git('checkout','--detach',self.base)
        self.write('research-packages/alpha/README.md','PR clarification\n'); self.commit()
        p=self.full(make_plan(self.root,target))
        self.assertTrue(any('target base' in s for s in p['reasons']))

    def test_privileged_workflow_proposal_is_not_a_green_plan(self):
        self.write('.github/workflows/unsafe.yml','on: pull_request_target\njobs: {}\n')
        self.commit(); p=self.full()
        self.assertTrue(any('privileged PR trigger' in e for e in security(self.root,p)))

    def test_force_push_event(self):
        p=make_plan(self.root,event={'before':self.base,'after':self.base,'forced':True}); self.full(p)

    def test_stale_pr_head(self):
        self.write('README.md','new head\n'); self.commit()
        self.full(make_plan(self.root,event={'pull_request':{'base':{'sha':self.base},'head':{'sha':self.base}}}))

    def test_dirty_checkout(self):
        self.write('README.md','uncommitted\n'); self.full()

    def test_shallow_history(self):
        (self.root/'.git/shallow').write_text(self.base+'\n'); self.full()

    def test_new_domain_must_match_verify(self):
        p='research-packages/alpha/TASK.json'; t=self.read_json(p); t['scope']['domain']='only zero'; self.json(p,t)
        self.commit(); self.full()

    def test_coordinated_domain_reduction_requires_review(self):
        for name in ('TASK','VERIFY'):
            p=f'research-packages/alpha/{name}.json'; s=self.read_json(p)
            if name=='TASK': s['scope']['domain']='only zero'
            else: s['domain']='only zero'
            self.json(p,s)
        self.commit(); self.full()

    def test_code_only_domain_reduction_cannot_report_full_verification(self):
        self.write('research-packages/alpha/verify.py','for x in range(1):\n    assert x * x >= 0\nprint("passed exact 10-case fixture")\n')
        self.repin(); self.commit(); p=self.full()
        self.assertTrue(any('domain-sensitive' in s for s in p['reasons']))
        with self.assertRaises(Invalid): replay(self.root,p,self.output)

    def test_dependency_installation_is_not_silently_skipped(self):
        p='research-packages/alpha/VERIFY.json'; s=self.read_json(p)
        s['environment']['dependencies']=['missing==1.0']; self.json(p,s); self.commit(); self.full()

    def test_shell_and_interpreter_flags_rejected(self):
        for argv in (['sh','-c','true'],['{python}','-O','research-packages/alpha/verify.py']):
            p='research-packages/alpha/VERIFY.json'; s=self.read_json(p); s['commands'][0]['argv']=argv; self.json(p,s); self.commit(); self.full()

    def test_timeout_fails_and_is_not_fully_verified(self):
        self.package('beta',code='while True:\n    pass\n')
        p='research-packages/beta/VERIFY.json'; s=self.read_json(p); s['commands'][0]['timeout_seconds']=1; self.json(p,s)
        self.commit(); p=self.plan(); self.assertEqual(p['level'],'targeted-replay',p)
        result=replay(self.root,p,self.output)
        self.assertEqual(result['status'],'failed'); self.assertFalse(result['full_verified'])
        self.assertEqual(result['packages'][0]['commands'][0]['status'],'timeout')

    def test_no_sandbox_means_no_replay(self):
        self.write('research-packages/alpha/README.md','changed\n'); self.commit()
        with patch('tools.localized_ci.replay.shutil.which',return_value=None):
            with self.assertRaises(Invalid): replay(self.root,self.plan(),self.output)

    def test_malicious_privileged_import_is_rejected(self):
        self.package('alpha',code='import os\nprint(os.environ)\n'); self.commit(); self.full()

    def test_replay_does_not_inherit_optimization_or_secrets(self):
        self.package('beta',code='assert False, "negative control must fail"\n'); self.commit()
        with patch.dict(os.environ,{'PYTHONOPTIMIZE':'2','GITHUB_TOKEN':'fixture-secret'}):
            result=replay(self.root,self.plan(),self.output)
        self.assertEqual(result['status'],'failed'); self.assertFalse(result['full_verified'])

    def test_selected_tool_cache_runtime_is_bound_explicitly(self):
        with patch('tools.localized_ci.replay.sys.base_prefix','/opt/e99-trusted-python'), patch('tools.localized_ci.replay.sys.prefix','/opt/e99-trusted-python'):
            argv=sandbox_prefix([])
        self.assertIn('/opt/e99-trusted-python',argv)
        self.assertIn('/opt/e99-trusted-python/lib',argv)

    def test_security_and_whitespace(self):
        self.write('README.md','has trailing space \n'+'-----BEGIN '+'PRIVATE KEY-----\n'); self.commit()
        self.assertEqual(len(security(self.root,self.plan())),2)

    def test_scanner_fixture_is_not_a_private_key(self):
        self.write('README.md', 'A scanner fixture string: "-----BEGIN '+'PRIVATE KEY-----"\n')
        self.commit()
        self.assertEqual(security(self.root,self.plan()),[])

    def test_whitespace_diagnostics_do_not_echo_credentials(self):
        token='ghp_'+'a'*35
        self.write('README.md',token+' \n'); self.commit()
        errors=security(self.root,self.plan())
        self.assertEqual(len(errors),2)
        self.assertNotIn(token,str(errors))

    def test_pinned_source_commit_must_match_bytes(self):
        self.package('alpha',('data/all.txt',))
        p='research-packages/alpha/SOURCES.json'; s=self.read_json(p); s['inputs'][1]['commit']=self.anchor; self.json(p,s)
        self.base=self.commit(); self.write('data/all.txt','changed\n'); self.repin(); self.commit(); self.full()


class ProtocolSyntax(unittest.TestCase):
    def test_traversal_aliases_and_special_paths(self):
        for value in ('../secret','a/../b','/etc/passwd','a//b','./a','a/./b','a\\b','-x','a\nb','a b'):
            with self.subTest(value=value), self.assertRaises(Invalid): path(value)

    def test_duplicate_json_keys(self):
        with self.assertRaises(Invalid): strict_json('{"version":1,"version":2}')

    def test_workflow_permissions_and_gates(self):
        import yaml
        workflow=yaml.safe_load((ROOT/'.github/workflows/theorem-state.yml').read_text())
        self.assertEqual(set(workflow.get('on',workflow.get(True))),{'pull_request'})
        self.assertEqual(workflow['permissions'],{'contents':'read'})
        self.assertIn('draft == false',workflow['jobs']['plan']['if'])
        self.assertIn('E99_PUBLIC_PACKAGE_REPLAY',workflow['jobs']['replay']['if'])
        self.assertNotIn('strategy',workflow['jobs']['replay'])
        for job in workflow['jobs'].values():
            self.assertLessEqual(job['timeout-minutes'],6)
            for step in job['steps']:
                if 'uses' in step:
                    self.assertRegex(step['uses'],r'@[0-9a-f]{40}$')
                if step.get('uses','').startswith('actions/checkout@'):
                    self.assertFalse(step['with']['persist-credentials'])
        text=(ROOT/'.github/workflows/theorem-state.yml').read_text()
        self.assertNotIn('pull_request_target',text)
        self.assertNotIn('secrets.',text)
        self.assertNotIn('run_theorem_certificates.py',text)

if __name__=='__main__':
    unittest.main()

