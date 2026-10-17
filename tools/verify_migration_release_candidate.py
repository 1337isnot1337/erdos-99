#!/usr/bin/env python3
"""Verify recorded migration coverage and registered Gate 2 on one clean commit.

All reports and logs are detached from the checkout. This wrapper supplements
the original Gate 2 runner without changing its registered checks or claims.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def accepted_gate2(receipt: object, candidate: str, tree: str) -> bool:
    """Reject missing, stale, or incomplete underlying release evidence."""
    return (isinstance(receipt, dict)
            and receipt.get('candidate_commit') == candidate
            and receipt.get('candidate_tree') == tree
            and receipt.get('candidate_unchanged') is True
            and receipt.get('executable_checks_passed') is True
            and receipt.get('automated_release_precheck_passed') is True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, required=True,
                        help='New directory outside the checkout')
    parser.add_argument('--gitleaks', type=Path, required=True)
    parser.add_argument('--actionlint', type=Path, required=True)
    parser.add_argument('--source-repo', type=Path,
                        help='Optional additional source-backed provenance replay')
    args = parser.parse_args()
    root, output = args.root.resolve(), args.output.resolve()
    if output.is_relative_to(root) or output.exists():
        parser.error('output must be a new directory outside the checkout')

    def git(*argv: str) -> str:
        return subprocess.check_output(
            ['git', '--no-replace-objects', '-C', str(root), *argv],
            text=True, stderr=subprocess.PIPE,
        ).strip()

    if git('status', '--porcelain', '--untracked-files=normal'):
        parser.error('candidate checkout must be clean')
    if git('rev-parse', '--is-shallow-repository') != 'false':
        parser.error('release verification requires complete reachable Git history')
    candidate, tree = git('rev-parse', 'HEAD'), git('rev-parse', 'HEAD^{tree}')
    refs_before = git('for-each-ref', '--format=%(refname) %(objectname)').splitlines()
    output.mkdir(parents=True)
    receipt = {
        'candidate_commit': candidate,
        'candidate_tree': tree,
        'ref_inventory_before': refs_before,
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'commands': [],
        'mathematical_proof': False,
        'publication_authorized': False,
        'combined_checks_passed': False,
        'deprecation_readiness_assessed': False,
        'scope': ['pinned source-main preservation', 'recorded branch and worktree evidence',
                  'committed navigation', 'original Gate 2 release verification'],
    }
    child_env = os.environ.copy()
    for key in ('PYTHONPATH', 'PYTHONHOME', 'PYTHONSTARTUP'):
        child_env.pop(key, None)
    child_env['PYTHONPYCACHEPREFIX'] = str(output / 'pycache')

    def save() -> None:
        (output / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')

    def run(name: str, argv: list[str]) -> None:
        started = time.monotonic()
        error = None
        with (output / (name + '.log')).open('wb') as log:
            try:
                result = subprocess.run(argv, cwd=root, env=child_env,
                                        stdin=subprocess.DEVNULL,
                                        stdout=log, stderr=subprocess.STDOUT,
                                        check=False)
                exit_code = result.returncode
            except OSError as exception:
                exit_code = None
                error = type(exception).__name__
        receipt['commands'].append({
            'name': name, 'argv': argv, 'exit_code': exit_code,
            'error': error, 'seconds': round(time.monotonic() - started, 3),
            'log': name + '.log', 'verification_passed': exit_code == 0,
        })
        save()
        print(f'{name}: exit={exit_code}, seconds={receipt["commands"][-1]["seconds"]}',
              flush=True)

    python = sys.executable
    run('migration-union', [python, 'tools/check_migration_union.py',
                            '--repo', str(root), '--ref', candidate,
                            '--output', str(output / 'migration-union.json')])
    run('migration-navigation', [python, 'tools/audit_migration_navigation.py',
                                 '--repo', str(root), '--ref', candidate,
                                 '--output', str(output / 'migration-navigation.json')])
    run('migration-refs', [python, 'tools/check_migration_refs.py',
                           '--repo', str(root), '--candidate', candidate,
                           '--output', str(output / 'migration-refs.json')])
    gate2 = [python, 'tools/verify_publication_candidate.py', '--root', str(root),
             '--output', str(output / 'gate2'),
             '--gitleaks', str(args.gitleaks.resolve()),
             '--actionlint', str(args.actionlint.resolve())]
    if args.source_repo:
        gate2 += ['--source-repo', str(args.source_repo.resolve())]
    run('gate2', gate2)
    try:
        gate2_receipt = json.loads((output / 'gate2/receipt.json').read_text())
    except (OSError, ValueError):
        gate2_receipt = None
    receipt['gate2_receipt_accepted'] = accepted_gate2(gate2_receipt, candidate, tree)
    receipt['candidate_unchanged'] = (
        git('rev-parse', 'HEAD') == candidate
        and git('rev-parse', 'HEAD^{tree}') == tree
        and not git('status', '--porcelain', '--untracked-files=normal')
    )
    receipt['ref_inventory_after'] = git(
        'for-each-ref', '--format=%(refname) %(objectname)',
    ).splitlines()
    receipt['history_refs_unchanged'] = receipt['ref_inventory_after'] == refs_before
    receipt['combined_checks_passed'] = (
        receipt['candidate_unchanged'] and receipt['history_refs_unchanged']
        and receipt['gate2_receipt_accepted']
        and all(command['verification_passed'] for command in receipt['commands'])
    )
    receipt['finished_utc'] = datetime.now(timezone.utc).isoformat()
    receipt['limits'] = [
        'Gate 2 is automated release verification, not publication permission.',
        'Historical references are reported separately from active missing dependencies.',
        'Unrecoverable working-copy data remains outside demonstrated Git preservation.',
        'Finite certificates do not prove Level I or analytic theorems.',
        'Hosted CI and anonymous public access are not exercised.',
    ]
    save()
    print(json.dumps({key: receipt[key] for key in (
        'candidate_commit', 'candidate_tree', 'candidate_unchanged',
        'history_refs_unchanged', 'combined_checks_passed', 'publication_authorized',
    )}), flush=True)
    return 0 if receipt['combined_checks_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
