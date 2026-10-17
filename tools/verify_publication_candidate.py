#!/usr/bin/env python3
"""Verify the current release snapshot and write a detached receipt.

This executes trusted candidate code locally. It is not a fork CI entrypoint.
The receipt records current checks and whether files changed during this run.
No source repository, migration receipt, credentials, or hosted runner is required.
Native scanners are optional for standard checks. Use --require-release-tools
to require both Gitleaks and actionlint for the full release scope.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import stat
import sys
import time

try:
    from tools.review_scanner_findings import review_combined_history_gitleaks, review_tree_gitleaks
    from tools.localized_ci.replay import sandbox_unavailable_reason
except ModuleNotFoundError:
    from review_scanner_findings import review_combined_history_gitleaks, review_tree_gitleaks
    from localized_ci.replay import sandbox_unavailable_reason


# A reviewed scanner match, not a Gitleaks allowlist. The unmodified scanner
# still runs over all reachable history and its raw report/exit are retained.
REVIEWED_HISTORY_FIXTURE = {
    'Commit': '08784c2440aa2f6f4252adc30f7ce33cd59cf976',
    'File': 'tools/test_local_ci.py',
    'RuleID': 'private-key',
    'StartLine': 386,
    'EndLine': 390,
    'Fingerprint': '08784c2440aa2f6f4252adc30f7ce33cd59cf976:tools/test_local_ci.py:private-key:386',
}
REVIEWED_HISTORY_BLOB_SHA256 = '509b6ed834755b0ae83cd48bcef34cc6a5016d5e375d24f64e92eb4f3f856f92'
# This merge retained exactly the same reviewed blob. No arbitrary commit may
# borrow its disposition, even when a scanner reports similar-looking text.
REVIEWED_HISTORY_ALIASES = ('75fad69da5002e28d0ccc770841cd264ad1ba6cb',)
GITLEAKS_HISTORY_LOG_OPTIONS = '--all --full-history -m'
CHECK_POSIX_EXECUTE_BITS = os.name != 'nt'


def find_executable(name: str, requested: str | None = None) -> str | None:
    """Resolve an optional native tool by its PATH name or explicit location."""
    executable = shutil.which(requested or name)
    if executable is None:
        if requested is not None:
            raise ValueError(f'{name} executable was not found or is not executable: {requested}')
        return None
    return str(Path(executable).resolve())


def unittest_summary(log: Path) -> dict | None:
    """Keep skipped test scope visible without treating skipped cases as passes."""
    text = log.read_text(encoding='utf-8', errors='replace')
    runs = re.findall(r'^Ran (\d+) tests? in ', text, flags=re.MULTILINE)
    if not runs:
        return None
    summaries = list(re.finditer(r'^(?:OK|FAILED)(?: \(([^\n]*)\))?$', text, flags=re.MULTILINE))
    summary = summaries[-1] if summaries else None
    skipped = re.search(r'\bskipped=(\d+)\b', summary[1] or '') if summary else None
    reasons = sorted(set(re.findall(r"\.\.\. skipped ['\"]([^\r\n]*)['\"]$", text, flags=re.MULTILINE)))
    return {'tests_run': int(runs[-1]), 'tests_skipped': int(skipped[1]) if skipped else 0,
            'skip_reasons': reasons}


def review_history_gitleaks(root: Path, report: Path) -> dict | None:
    """Recognize only the exact reviewed, payload-free historical test fixture.

    Missing/malformed reports, unreviewed matches, changed identities and unavailable
    or different Git objects all fail closed. No worktree/index bytes are used.
    """
    try:
        findings = json.loads(report.read_text(encoding='utf-8'))
        if not isinstance(findings, list) or not findings:
            return None
        allowed = {REVIEWED_HISTORY_FIXTURE['Commit'], *REVIEWED_HISTORY_ALIASES}
        reviewed = []; seen = set()
        for match in findings:
            if not isinstance(match, dict) or not isinstance(match.get('Commit'), str) or match['Commit'] not in allowed:
                return None
            commit = match['Commit']
            if commit in seen:
                return None
            seen.add(commit)
            expected = {**REVIEWED_HISTORY_FIXTURE, 'Commit': commit,
                        'Fingerprint': f'{commit}:{REVIEWED_HISTORY_FIXTURE["File"]}:{REVIEWED_HISTORY_FIXTURE["RuleID"]}:{REVIEWED_HISTORY_FIXTURE["StartLine"]}'}
            if any(match.get(k) != v for k, v in expected.items()):
                return None
            data = subprocess.check_output([
                'git', '--no-replace-objects', '-C', str(root), 'show',
                commit + ':' + expected['File'],
            ], stderr=subprocess.PIPE)
            if hashlib.sha256(data).hexdigest() != REVIEWED_HISTORY_BLOB_SHA256:
                return None
            reviewed.append(expected)
        return {
            'disposition': 'reviewed-false-positive',
            'finding': reviewed[0],
            'findings': reviewed,
            'finding_count': len(reviewed),
            'committed_blob_sha256': REVIEWED_HISTORY_BLOB_SHA256,
            'reason': 'Two PEM opening delimiters in negative-test strings; no closing delimiter or encoded private-key payload. Exact historical blob independently inspected.',
            'raw_scanner_result_preserved': True,
        }
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


def verify_committed_worktree(root: Path, candidate: str) -> int:
    """Check raw bytes and Git modes; compare POSIX execute bits where available."""
    root = root.resolve()

    def git(*argv):
        return subprocess.check_output(['git', '--no-replace-objects', '-C', str(root), *argv])

    flags = git('ls-files', '-v', '-z').split(b'\0')
    if any(row and (row[:1].islower() or row[:1] == b'S') for row in flags):
        raise ValueError('candidate index contains assume-unchanged or skip-worktree entries')
    count = 0
    for row in git('ls-tree', '-r', '-z', candidate).split(b'\0'):
        if not row:
            continue
        metadata, raw_path = row.split(b'\t', 1)
        mode, kind, oid = metadata.decode('ascii').split()
        relative = raw_path.decode('utf-8')
        parts = relative.split('/')
        if (mode not in ('100644', '100755') or kind != 'blob'
                or any(p in ('', '.', '..') or p.lower() == '.git' for p in parts)
                or '\\' in relative or ':' in relative
                or any(ord(char) < 32 or ord(char) == 127 for char in relative)):
            raise ValueError('candidate has a special object or unsafe tracked path')
        target = root.joinpath(*parts)
        if any(parent.is_symlink() for parent in (target, *target.parents) if parent != root and root in parent.parents):
            raise ValueError('candidate worktree contains a symlink')
        if not target.resolve().is_relative_to(root):
            raise ValueError('candidate tracked path escapes the checkout')
        metadata = target.lstat()
        if not stat.S_ISREG(metadata.st_mode):
            raise ValueError('candidate worktree contains a nonregular tracked file')
        if CHECK_POSIX_EXECUTE_BITS and bool(metadata.st_mode & 0o111) != (mode == '100755'):
            raise ValueError('candidate worktree execute mode differs from committed tree')
        data = target.read_bytes()
        actual = hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()
        if actual != oid:
            raise ValueError('candidate worktree bytes differ from committed tree')
        count += 1
    return count


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, required=True, help='New directory OUTSIDE the checkout')
    parser.add_argument('--gitleaks', help='Gitleaks executable name or path; otherwise discover on PATH')
    parser.add_argument('--actionlint', help='actionlint executable name or path; otherwise discover on PATH')
    parser.add_argument('--require-release-tools', action='store_true',
                        help='Require Gitleaks and actionlint for successful full release scope')
    args = parser.parse_args(argv)
    root, output = args.root.resolve(), args.output.resolve()
    if output.is_relative_to(root) or output.exists():
        parser.error('output must be a new directory outside the checkout')
    try:
        gitleaks = find_executable('gitleaks', args.gitleaks)
        actionlint = find_executable('actionlint', args.actionlint)
    except ValueError as error:
        parser.error(str(error))

    def git(*argv):
        return subprocess.check_output(['git', '--no-replace-objects', '-C', str(root), *argv], text=True).strip()

    if git('status', '--porcelain', '--untracked-files=normal'):
        parser.error('candidate checkout must be clean')
    candidate, tree = git('rev-parse', 'HEAD'), git('rev-parse', 'HEAD^{tree}')
    try:
        tracked_files = verify_committed_worktree(root, candidate)
    except (ValueError, OSError, subprocess.SubprocessError) as error:
        parser.error('candidate committed-byte validation failed: ' + type(error).__name__)
    output.mkdir(parents=True)
    versions = {d.metadata['Name']: d.version for d in importlib.metadata.distributions()}
    receipt = {'candidate_commit': candidate, 'candidate_tree': tree,
               'started_utc': datetime.now(timezone.utc).isoformat(),
               'python': sys.version, 'packages': dict(sorted(versions.items())),
               'platform': {'system': platform.system(), 'release': platform.release(),
                            'machine': platform.machine()},
               'commands': [], 'skipped_checks': [], 'mathematical_proof': False,
               'require_release_tools': args.require_release_tools}
    receipt['tracked_files_verified'] = tracked_files
    receipt['worktree_validation'] = {
        'raw_bytes': True, 'git_modes_and_types': True,
        'posix_execute_bits': CHECK_POSIX_EXECUTE_BITS,
        'execute_bit_scope': ('Compared with the committed executable mode' if CHECK_POSIX_EXECUTE_BITS
                              else 'Not represented by this host; committed Git modes and raw bytes are still checked'),
    }
    receipt['capabilities'] = {
        'gitleaks': {'available': gitleaks is not None, 'executable': gitleaks},
        'actionlint': {'available': actionlint is not None, 'executable': actionlint},
    }
    for name, require_python in (('isolated_integrity', False), ('isolated_package_replay', True)):
        reason = sandbox_unavailable_reason(require_replay_python=require_python)
        receipt['capabilities'][name] = {'available': reason is None, 'unavailable_reason': reason}
    if gitleaks is None:
        receipt['skipped_checks'].append({
            'names': ['gitleaks-version', 'gitleaks-tree', 'gitleaks-history'],
            'reason': 'Optional Gitleaks executable was not found on PATH',
        })
    if actionlint is None:
        receipt['skipped_checks'].append({
            'names': ['actionlint'], 'reason': 'Optional actionlint executable was not found on PATH',
        })
    for skipped in receipt['skipped_checks']:
        print(', '.join(skipped['names']) + ': skipped; ' + skipped['reason'], flush=True)
    child_env = os.environ.copy()
    for key in ('PYTHONPATH', 'PYTHONHOME', 'PYTHONSTARTUP'):
        child_env.pop(key, None)
    child_env['PYTHONPYCACHEPREFIX'] = str(output / 'pycache')
    receipt['python_import_controls'] = 'Inherited Python path/home/startup overrides removed; fresh external bytecode cache'

    def run(name, argv, *, history_report=None, tree_report=None):
        started = time.monotonic()
        exit_code = None
        invocation_error = None
        log_path = output / (name + '.log')
        with log_path.open('wb') as log:
            try:
                proc = subprocess.run(argv, cwd=root, stdout=log, stderr=subprocess.STDOUT,
                                      stdin=subprocess.DEVNULL, env=child_env)
                exit_code = proc.returncode
            except OSError as error:
                invocation_error = type(error).__name__ + ': ' + str(error)
                log.write((invocation_error + '\n').encode('utf-8'))
        record = {'name': name, 'argv': argv, 'exit_code': exit_code,
                  'seconds': round(time.monotonic() - started, 3),
                  'log': name + '.log'}
        record['verification_passed'] = exit_code == 0
        if invocation_error is not None:
            record['invocation_error'] = invocation_error
        if name in ('tool-tests', 'corpus-tests'):
            summary = unittest_summary(log_path)
            if summary is not None:
                record['test_summary'] = summary
        # Exit 1 denotes detected findings. Invocation failures and every other
        # finding remain failures; never change or discard the raw exit code.
        if exit_code == 1 and (history_report is not None or tree_report is not None):
            review = (review_tree_gitleaks(root, tree_report, candidate) if tree_report is not None
                      else review_combined_history_gitleaks(root, history_report, review_history_gitleaks))
            if review is not None:
                record['finding_review'] = review
                record['verification_passed'] = True
        receipt['commands'].append(record)
        (output / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
        print(f'{name}: exit={exit_code}, seconds={record["seconds"]}' +
              ('; exact committed findings reviewed as false positives' if 'finding_review' in record else ''), flush=True)

    python = sys.executable
    run('environment', [python, '-m', 'pip', 'check'])
    run('newcomer-task-selection', [python, 'scripts/choose_research_task.py',
                                   '--count', '1', '--json'])
    run('reading-edition', [python, 'tools/build_reading_edition.py', '--check'])
    run('public-integrity', [python, 'tools/check_public.py'])
    run('theorem-state', [python, 'tools/check_theorem_state.py'])
    run('tool-tests', [python, '-m', 'unittest', 'discover', '-s', 'tools', '-p', 'test_*.py', '-v'])
    run('corpus-tests', [python, '-m', 'unittest', 'discover', '-s', 'tests', '-v'])
    run('certificates', [python, 'tools/run_theorem_certificates.py'])
    run('release-audit', [python, 'tools/audit_public_release.py', '--output', str(output / 'release-audit.json')])
    if gitleaks:
        run('gitleaks-version', [gitleaks, 'version'])
        run('gitleaks-tree', [gitleaks, 'dir', '--no-banner', '--redact', '--report-format', 'json',
                              '--report-path', str(output / 'gitleaks-tree.json'), '.'],
            tree_report=output / 'gitleaks-tree.json')
        run('gitleaks-history', [gitleaks, 'git', '--no-banner', '--redact', '--report-format', 'json',
                                 '--report-path', str(output / 'gitleaks-history.json'), '--log-opts=' + GITLEAKS_HISTORY_LOG_OPTIONS, '.'],
            history_report=output / 'gitleaks-history.json')
    if actionlint:
        run('actionlint', [actionlint])
    run('whitespace', ['git', 'diff', '--check'])
    receipt['finished_utc'] = datetime.now(timezone.utc).isoformat()
    try:
        committed_bytes_unchanged = verify_committed_worktree(root, candidate) == tracked_files
    except (ValueError, OSError, subprocess.SubprocessError):
        committed_bytes_unchanged = False
    receipt['candidate_unchanged'] = (committed_bytes_unchanged and git('rev-parse', 'HEAD') == candidate and
                                      git('rev-parse', 'HEAD^{tree}') == tree and
                                      not git('status', '--porcelain', '--untracked-files=normal'))
    receipt['executable_checks_passed'] = (receipt['candidate_unchanged'] and
        all(r['verification_passed'] for r in receipt['commands']))
    receipt['automated_release_precheck_passed'] = (receipt['executable_checks_passed'] and
        gitleaks is not None and actionlint is not None)
    receipt['required_scope_passed'] = (receipt['automated_release_precheck_passed']
                                      if args.require_release_tools else receipt['executable_checks_passed'])
    receipt['limits'] = ['No automated run grants source rights or contributor consent.',
                         'Hosted CI and anonymous public access are not exercised.',
                         'Unavailable optional tools and skipped test cases are not verified.',
                         'This receipt describes the recorded host; it does not certify other operating systems.',
                         'Trusted local candidate execution; no hostile-code sandbox or hermetic environment is claimed.',
                         'Finite certificates do not prove Level I or certify analytic proofs.']
    (output / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({k: receipt[k] for k in ('candidate_commit', 'candidate_unchanged', 'executable_checks_passed',
                                             'automated_release_precheck_passed', 'required_scope_passed', 'skipped_checks')}))
    return 0 if receipt['required_scope_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
