#!/usr/bin/env python3
"""Plan localized CI, optionally check Tier 0 and replay Tier 1. Tier 2 stays explicit."""
from __future__ import annotations
import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from localized_ci.packages import Invalid, strict_json
from localized_ci.plan import Snapshot, git, make_plan
from localized_ci.replay import integrity, replay


def security(root, plan):
    errors = []
    if not plan.get('merge_base'):
        return ['no trustworthy changed-file range']
    check = subprocess.run(['git', '--no-replace-objects', '-C', str(root), 'diff', '--check',
                            plan['merge_base'], plan['head'], '--'], capture_output=True, text=True)
    if check.returncode:
        # Do not echo changed lines: a whitespace failure can itself contain a secret.
        errors.append('changed-file whitespace failed; inspect git diff --check locally')
    snapshot = Snapshot(root, plan['head'])
    for change in plan['changes']:
        p = change['path']
        if p not in snapshot.tree:
            continue
        try:
            data = snapshot.read(p)
            if re.search(rb'(?m)^-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----\r?$|gh[pousr]_[A-Za-z0-9]{30,}', data):
                errors.append(f'possible credential in changed file: {p}')
            if p.startswith('.github/workflows/') and b'pull_request_target' in data:
                errors.append(f'privileged PR trigger forbidden: {p}')
        except Invalid as exc:
            errors.append(str(exc))
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--base-ref')
    parser.add_argument('--head-ref', default='HEAD')
    parser.add_argument('--event-file', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--github-output', type=Path)
    parser.add_argument('--integrity', action='store_true')
    parser.add_argument('--replay', action='store_true')
    parser.add_argument('--require-localized', action='store_true',
                        help='exit 3 when impact needs full review or required replay exceeds the automatic budget')
    args = parser.parse_args(argv)
    if bool(args.base_ref) == bool(args.event_file):
        parser.error('choose exactly one of --base-ref or --event-file')
    root = args.root.resolve()
    try:
        event = strict_json(args.event_file.read_bytes()) if args.event_file else None
        plan = make_plan(root, args.base_ref, args.head_ref, event)
    except (Invalid, OSError) as exc:
        plan = make_plan(root, None)
        plan['errors'].append(str(exc))
    plan['errors'].extend(security(root, plan))
    if plan['errors']:
        plan.update(level='full-verification-required', replay_allowed=False,
                    replay_schedule='requires-review')
    output = args.output or Path(tempfile.gettempdir()) / 'e99-local-ci'
    if args.integrity:
        try:
            plan['integrity'] = integrity(root, Path(__file__).resolve().parents[1], plan, output)
            if plan['integrity']['status'] != 'passed':
                plan['errors'].append('Tier 0 metadata check failed; see integrity.log')
        except (Invalid, OSError, subprocess.SubprocessError) as exc:
            plan['errors'].append(f'Tier 0 failed: {exc}')
    if plan['errors']:
        plan.update(level='full-verification-required', replay_allowed=False,
                    replay_schedule='requires-review')
    # Publish output even on failure. Job status must not hide review requirements.
    output.mkdir(parents=True, exist_ok=True)
    (output / 'plan.json').write_text(json.dumps(plan, indent=2, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
    if args.github_output:
        with args.github_output.open('a', encoding='utf-8', newline='\n') as handle:
            handle.write('replay=' + str(plan['replay_allowed']).lower() + '\n')
            handle.write('level=' + plan['level'] + '\n')
            handle.write('replay_schedule=' + plan['replay_schedule'] + '\n')
    if args.replay:
        try:
            # Integrity fields are observational, not part of dependency authorization.
            authorization = make_plan(root, args.base_ref, args.head_ref, event)
            if plan['errors']:
                raise Invalid('Tier 0 failed')
            result = replay(root, authorization, output)
            plan['replay'] = result
            if result['status'] != 'passed':
                plan['errors'].append('targeted replay failed')
        except (Invalid, OSError, subprocess.SubprocessError) as exc:
            plan['errors'].append(f'targeted replay refused/failed: {exc}')
    (output / 'plan.json').write_text(json.dumps(plan, indent=2, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(plan, indent=2, sort_keys=True))
    if plan['errors']:
        return 1
    needs_handoff = (plan['level'] == 'full-verification-required'
                     or plan['replay_schedule'] == 'deferred-budget')
    return 3 if args.require_localized and needs_handoff else 0

if __name__ == '__main__':
    raise SystemExit(main())

