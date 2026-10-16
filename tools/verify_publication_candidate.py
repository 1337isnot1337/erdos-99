#!/usr/bin/env python3
"""Replay a clean, immutable publication candidate and write a detached receipt.

This executes trusted candidate code locally. It is not a fork CI entrypoint.
The receipt separates executable failures from rights/history clearance findings.
No private source repository, credentials, or hosted runner is required.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import importlib.metadata
import json
from pathlib import Path
import subprocess
import sys
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, required=True, help='New directory OUTSIDE the checkout')
    parser.add_argument('--gitleaks', type=Path, help='Optional installed Gitleaks executable')
    parser.add_argument('--actionlint', type=Path, help='Optional installed actionlint executable')
    args = parser.parse_args()
    root, output = args.root.resolve(), args.output.resolve()
    if output.is_relative_to(root) or output.exists():
        parser.error('output must be a new directory outside the checkout')

    def git(*argv):
        return subprocess.check_output(['git', '--no-replace-objects', '-C', str(root), *argv], text=True).strip()

    if git('status', '--porcelain', '--untracked-files=normal'):
        parser.error('candidate checkout must be clean')
    candidate, tree = git('rev-parse', 'HEAD'), git('rev-parse', 'HEAD^{tree}')
    output.mkdir(parents=True)
    versions = {d.metadata['Name']: d.version for d in importlib.metadata.distributions()}
    receipt = {'candidate_commit': candidate, 'candidate_tree': tree,
               'started_utc': datetime.now(timezone.utc).isoformat(),
               'python': sys.version, 'packages': dict(sorted(versions.items())),
               'commands': [], 'mathematical_proof': False, 'release_cleared': False}

    def run(name, argv, *, clearance=False):
        started = time.monotonic()
        with (output / (name + '.log')).open('wb') as log:
            proc = subprocess.run(argv, cwd=root, stdout=log, stderr=subprocess.STDOUT,
                                  stdin=subprocess.DEVNULL)
        record = {'name': name, 'argv': argv, 'exit_code': proc.returncode,
                  'seconds': round(time.monotonic() - started, 3),
                  'log': name + '.log', 'clearance_gate': clearance}
        receipt['commands'].append(record)
        (output / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
        print(f'{name}: exit={proc.returncode}, seconds={record["seconds"]}', flush=True)

    python = sys.executable
    run('public-integrity', [python, 'tools/check_public.py'])
    run('theorem-state', [python, 'tools/check_theorem_state.py'])
    run('tool-tests', [python, '-m', 'unittest', 'discover', '-s', 'tools', '-p', 'test_*.py', '-v'])
    run('corpus-tests', [python, '-m', 'unittest', 'discover', '-s', 'tests', '-v'])
    run('certificates', [python, 'tools/run_theorem_certificates.py'])
    run('release-audit', [python, 'tools/audit_public_release.py', '--output', str(output / 'release-audit.json')], clearance=True)
    if args.gitleaks:
        executable = str(args.gitleaks.resolve())
        run('gitleaks-version', [executable, 'version'])
        run('gitleaks-tree', [executable, 'dir', '--no-banner', '--redact', '--report-format', 'json',
                              '--report-path', str(output / 'gitleaks-tree.json'), '.'])
        run('gitleaks-history', [executable, 'git', '--no-banner', '--redact', '--report-format', 'json',
                                 '--report-path', str(output / 'gitleaks-history.json'), '--log-opts=--all', '.'])
    if args.actionlint:
        run('actionlint', [str(args.actionlint.resolve())])
    run('whitespace', ['git', 'diff', '--check'])
    receipt['finished_utc'] = datetime.now(timezone.utc).isoformat()
    receipt['candidate_unchanged'] = (git('rev-parse', 'HEAD') == candidate and
                                      git('rev-parse', 'HEAD^{tree}') == tree and
                                      not git('status', '--porcelain', '--untracked-files=normal'))
    receipt['executable_checks_passed'] = (receipt['candidate_unchanged'] and
        all(r['exit_code'] == 0 for r in receipt['commands'] if not r['clearance_gate']))
    receipt['automated_release_precheck_passed'] = (receipt['executable_checks_passed'] and
        all(r['exit_code'] == 0 for r in receipt['commands']) and args.gitleaks is not None)
    # Even a scanner-clean tree still needs separate factual permissions and visibility approval.
    receipt['limits'] = ['No automated run grants source rights or contributor consent.',
                         'Hosted CI and anonymous public access are not exercised.',
                         'Finite certificates do not prove Level I or certify analytic proofs.']
    (output / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({k: receipt[k] for k in ('candidate_commit', 'candidate_unchanged', 'executable_checks_passed', 'release_cleared')}))
    return 0 if receipt['automated_release_precheck_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
