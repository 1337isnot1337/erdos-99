"""Offline regression tests for the exact embedded cleanup workflow code."""
from __future__ import annotations

from contextlib import redirect_stdout
from io import BytesIO, StringIO
import json
import os
from pathlib import Path
from unittest import TestCase, main, mock
from urllib.error import HTTPError
from urllib.parse import parse_qs, unquote, urlparse

import yaml


WORKFLOW = Path(__file__).resolve().parents[1] / '.github' / 'workflows' / 'cleanup-closed-pr-branches.yml'
REPO = '1337isnot1337/erdos-99'


class FakeGitHubAPI:
    def __init__(self, closed: dict[str, str], branches: dict[str, tuple[str, bool]],
                 open_heads: set[str] | None = None):
        self.closed = closed
        self.branches = branches
        self.open_heads = open_heads or set()
        self.deleted = []

    def urlopen(self, request, timeout=20):
        url = urlparse(request.full_url)
        path = unquote(url.path)
        prefix = f'/repos/{REPO}/'
        assert path.startswith(prefix), path
        path = path[len(prefix):]
        if request.get_method() == 'DELETE':
            assert path.startswith('git/refs/heads/'), path
            name = path.removeprefix('git/refs/heads/')
            if name not in self.branches:
                raise HTTPError(url.geturl(), 404, 'not found', None, None)
            self.deleted.append(name)
            self.branches.pop(name)
            return BytesIO(b'')

        query = parse_qs(url.query)
        page = int(query.get('page', ['1'])[0])
        per_page = int(query.get('per_page', ['100'])[0])
        if path == 'pulls':
            state = query.get('state', [''])[0]
            if state == 'closed':
                results = [{'head': {'ref': name, 'sha': sha,
                                    'repo': {'full_name': REPO}}}
                           for name, sha in sorted(self.closed.items())]
            else:
                results = [{'base': {'ref': 'main'},
                            'head': {'ref': name, 'repo': {'full_name': REPO}}}
                           for name in sorted(self.open_heads)]
            payload = results[(page - 1) * per_page:page * per_page]
        elif path == 'branches':
            names = sorted(self.branches)
            payload = [{'name': name,
                        'commit': {'sha': self.branches[name][0]},
                        'protected': self.branches[name][1]}
                       for name in names[(page - 1) * per_page:page * per_page]]
        elif path.startswith('branches/'):
            name = path.removeprefix('branches/')
            if name not in self.branches:
                raise HTTPError(url.geturl(), 404, 'not found', None, None)
            sha, protected = self.branches[name]
            payload = {'name': name, 'commit': {'sha': sha},
                       'protected': protected}
        else:
            raise AssertionError(f'Unexpected GitHub API: {path}')
        return BytesIO(json.dumps(payload).encode('utf-8'))


def run_actual_workflow(fake: FakeGitHubAPI) -> str:
    config = yaml.safe_load(WORKFLOW.read_text(encoding='utf-8'))
    command = config['jobs']['prune']['steps'][0]['run']
    start = "python3 - <<'PY'\n"
    assert command.startswith(start)
    assert command.rstrip().endswith('\nPY')
    source = command[len(start):].rsplit('\nPY', 1)[0] + '\n'
    sink = StringIO()
    with mock.patch.dict(os.environ, {'GH_REPO': REPO,
                                   'GH_DEFAULT_BRANCH': 'main',
                                   'GH_TOKEN': 'placeholder-test-token'}), \
         mock.patch('urllib.request.urlopen', side_effect=fake.urlopen), \
         redirect_stdout(sink):
        exec(compile(source, str(WORKFLOW), 'exec'), {'__name__': '__main__'})
    return sink.getvalue()


class CleanupWorkflowTests(TestCase):
    def test_paginated_deletion_preserves_complete_branch_snapshot(self):
        # Deleting from page one must not change which branches are on page two.
        closed = {f'stale-{i:03d}': f'sha-{i:03d}' for i in range(150)}
        branches = {name: (sha, False) for name, sha in closed.items()}
        branches['main'] = ('main-sha', False)
        fake = FakeGitHubAPI(closed, branches)
        run_actual_workflow(fake)
        self.assertEqual(set(fake.branches), {'main'})
        self.assertEqual(len(fake.deleted), 150)

    def test_preserves_main_open_protected_advanced_and_unassociated(self):
        closed = {'stale': '1', 'open': '2', 'protected': '3', 'advanced': '4'}
        branches = {'main': ('main-sha', False), 'stale': ('1', False),
                    'open': ('2', False), 'protected': ('3', True),
                    'advanced': ('new-work', False), 'unassociated': ('8', False)}
        fake = FakeGitHubAPI(closed, branches, open_heads={'open'})
        run_actual_workflow(fake)
        self.assertEqual(fake.deleted, ['stale'])
        self.assertEqual(set(fake.branches),
                         {'main', 'open', 'protected', 'advanced', 'unassociated'})


if __name__ == '__main__':
    main()
