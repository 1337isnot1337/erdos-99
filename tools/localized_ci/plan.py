"""Git-aware impact classification. Uncertain impact requests Tier 2, never executes it."""
from __future__ import annotations

import ast
import re
import subprocess
from pathlib import Path

from .packages import Invalid, MAX_BLOB, MAX_PACKAGES, MAX_PACKAGE_SECONDS, MAX_SECONDS, discover, load_package

try:
    from ..ci_document_scope import is_workflow_document, mathematical_inputs
except ImportError:
    from ci_document_scope import is_workflow_document, mathematical_inputs

SHARED = ('tools/', '.github/workflows/', 'tests/', 'requirements')


def git(root, *args):
    return subprocess.check_output(['git', '--no-replace-objects', '-C', str(root), *args],
                                   stderr=subprocess.PIPE, timeout=30)


def revision(root, value):
    if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9_./^~-]+', value) or value.startswith('-'):
        raise Invalid('unsafe Git revision')
    return git(root, 'rev-parse', '--verify', value + '^{commit}').decode().strip()


class Snapshot:
    def __init__(self, root, commit, cache=None):
        self.root, self.commit = root, commit
        self.cache = cache if cache is not None else {}
        self.ancestry = {}
        self.tree = {}
        for record in git(root, 'ls-tree', '-rz', '--full-tree', commit).split(b'\0'):
            if not record:
                continue
            metadata, name = record.split(b'\t', 1)
            mode, kind, oid = metadata.decode().split()
            self.tree[name.decode('utf-8', 'surrogateescape')] = (mode, kind, oid)

    def prefetch_manifests(self):
        # Two Git calls per registry, instead of two processes per manifest.
        oids = sorted({v[2] for p, v in self.tree.items() if p.startswith('research-packages/')
                       and p.rsplit('/', 1)[-1] in ('TASK.json', 'SOURCES.json', 'VERIFY.json', 'README.md')
                       and v[0] in ('100644', '100755') and v[2] not in self.cache})
        if not oids:
            return
        request = ('\n'.join(oids) + '\n').encode()
        command = ['git', '--no-replace-objects', '-C', str(self.root), 'cat-file']
        sizes = subprocess.check_output([*command, '--batch-check'], input=request, timeout=30)
        sizes = [int(row.split()[2]) for row in sizes.splitlines()]
        if max(sizes) > MAX_BLOB or sum(sizes) > 32 * 1024 * 1024:
            raise Invalid('package manifest registry exceeds blob/32 MiB aggregate budget')
        if sum(sizes) + sum(map(len, self.cache.values())) > 64 * 1024 * 1024:
            raise Invalid('aggregate planning input budget exceeds 64 MiB')
        data = subprocess.check_output([*command, '--batch'], input=request, timeout=30)
        offset = 0
        for oid, size in zip(oids, sizes):
            offset = data.index(b'\n', offset) + 1
            self.cache[oid] = data[offset:offset+size]
            offset += size + 1

    def regular(self, p):
        if p not in self.tree or self.tree[p][0] not in ('100644', '100755'):
            raise Invalid(f'missing, symlink, or nonregular input: {p}')

    def read(self, p):
        self.regular(p)
        oid = self.tree[p][2]
        if oid not in self.cache:
            size = int(git(self.root, 'cat-file', '-s', oid))
            if size > MAX_BLOB:
                raise Invalid(f'input exceeds {MAX_BLOB} bytes: {p}')
            if size + sum(map(len, self.cache.values())) > 64 * 1024 * 1024:
                raise Invalid('aggregate planning input budget exceeds 64 MiB')
            self.cache[oid] = git(self.root, 'cat-file', 'blob', oid)
        return self.cache[oid]

    def read_at(self, commit, p):
        return Snapshot(self.root, commit).read(p)

    def ancestor(self, commit):
        if commit in self.ancestry:
            return self.ancestry[commit]
        try:
            git(self.root, 'merge-base', '--is-ancestor', commit, self.commit)
            answer = True
        except subprocess.CalledProcessError:
            answer = False
        self.ancestry[commit] = answer
        return answer


def endpoints(root, base, head='HEAD', event=None):
    push = False
    if event is not None:
        if 'pull_request' in event:
            pr = event['pull_request']
            base, head = pr['base']['sha'], pr['head']['sha']
        else:
            if event.get('forced') is not False:
                raise Invalid('force push or absent fast-forward metadata')
            base, head, push = event['before'], event['after'], True
        if any(not isinstance(s, str) or not re.fullmatch('[0-9a-f]{40}', s) or s == '0'*40 for s in (base, head)):
            raise Invalid('missing event endpoint')
    if git(root, 'rev-parse', '--is-shallow-repository').strip() != b'false':
        raise Invalid('shallow Git history')
    if git(root, 'status', '--porcelain', '--untracked-files=all').strip():
        raise Invalid('dirty checkout: commit inputs before planning')
    base, head = revision(root, base), revision(root, head)
    if revision(root, 'HEAD') != head:
        raise Invalid('stale PR head: checkout differs from event head')
    bases = git(root, 'merge-base', '--all', base, head).decode().splitlines()
    if len(bases) != 1:
        raise Invalid('missing or ambiguous merge base')
    if push:
        if bases != [base]:
            raise Invalid('non-fast-forward push')
        start = base
    else:
        start = bases[0]
    # A rename is removal + addition. Neither endpoint can disappear from impact.
    records = git(root, 'diff', '--no-renames', '--name-status', '-z', start, head, '--').split(b'\0')
    changes = []
    for i in range(0, len(records)-1, 2):
        changes.append({'status': records[i].decode(), 'path': records[i+1].decode('utf-8', 'surrogateescape')})
    return base, head, start, changes


def mathematical_paths(snapshot):
    import yaml
    try:
        state = (yaml.safe_load(snapshot.read('docs/state/theorem-state.yaml'))
                 if 'docs/state/theorem-state.yaml' in snapshot.tree else {})
    except yaml.YAMLError as exc:
        raise Invalid(f'malformed theorem-state YAML: {exc}') from exc
    if not isinstance(state, dict):
        raise Invalid('theorem-state must be a mapping')
    return mathematical_inputs(
        state, lambda p: snapshot.read(p) if p in snapshot.tree else None)


def domain_signature(snapshot, inputs):
    signatures = []
    for p in sorted(inputs):
        if not p.endswith('.py'):
            continue
        tree = ast.parse(snapshot.read(p))
        # Conservative domain-sensitive tripwires. They do not prove semantic coverage.
        nodes = [n for n in ast.walk(tree) if isinstance(n, (ast.For, ast.comprehension, ast.If, ast.Continue))]
        signatures.append((p, [ast.dump(n.iter if isinstance(n, (ast.For, ast.comprehension)) else n.test if isinstance(n, ast.If) else n, include_attributes=False) for n in nodes]))
    return signatures


def verification_contract(verify):
    """Keep the checked inputs, environment, commands and domain separate from time limits."""
    return {**verify, 'commands': [command['argv'] for command in verify['commands']]}


def make_plan(root: Path, base=None, head='HEAD', event=None):
    result = {'version': 1, 'level': 'full-verification-required', 'full_verified': False,
              'dependency_closure': 'not-established', 'reasons': [], 'errors': [],
              'packages': [], 'replay_allowed': False, 'workload_seconds': 0,
              'replay_schedule': 'requires-review', 'scheduling_reasons': [],
              'limits': {'packages': MAX_PACKAGES, 'seconds': MAX_SECONDS,
                         'package_seconds': MAX_PACKAGE_SECONDS}, 'changes': []}
    try:
        base, head, start, changes = endpoints(root, base, head, event)
        result.update(base=base, head=head, merge_base=start, changes=changes)
        cache = {}
        old, new = Snapshot(root, start, cache), Snapshot(root, head, cache)
        target = old if base == start else Snapshot(root, base, cache)
        snapshots = (old, new) if target is old else (old, new, target)
        for snapshot in snapshots:
            snapshot.prefetch_manifests()
        # The target base can have advanced since the fork; its canonical paths also matter.
        protected = mathematical_paths(old) | mathematical_paths(new) | mathematical_paths(target)
        graphs = []
        for snapshot in snapshots:
            packages = {}
            for directory in discover(snapshot.tree):
                try:
                    packages[directory] = load_package(snapshot, directory)
                except (Invalid, KeyError, TypeError, UnicodeError) as exc:
                    result['errors'].append(f'{snapshot.commit[:12]}:{directory}: {exc}')
            for directory, package in packages.items():
                if package['dependencies'] - packages.keys():
                    result['errors'].append(f'{directory}: missing package dependency')
            visited, active = set(), set()
            def visit(p):
                if p in active:
                    raise Invalid('cyclic package dependencies')
                if p in visited:
                    return
                active.add(p)
                for d in packages[p]['dependencies'] & packages.keys():
                    visit(d)
                active.remove(p)
                visited.add(p)
            for p in packages:
                visit(p)
            graphs.append(packages)
        before, after = graphs[:2]
        target_packages = before if target is old else graphs[2]
        affected = set()
        shared = False
        for change in changes:
            p = change['path']
            safe = is_workflow_document(p, protected)
            if not safe and (p in protected or p.startswith(('docs/state/', 'docs/targets/', 'docs/theory/', 'docs/problem/')) or p == 'docs/STATE.md'):
                result['reasons'].append(f'canonical/foundation/generated state changed: {p}')
            if not safe and p.startswith(('research/', 'src/', 'scripts/', 'docs/reports/', 'docs/audits/', 'docs/archive/')):
                result['reasons'].append(f'legacy mathematical input has no complete dependency closure: {p}')
            if p.startswith(SHARED):
                shared = True
                result['reasons'].append(f'shared verification infrastructure changed: {p}')
            owners = set()
            for graph in graphs:
                owners |= {d for d, pkg in graph.items() if p in pkg['files'] or p in pkg['inputs']}
            affected |= owners
            if protected and owners and not safe and not p.startswith(('research-packages/', 'research-package-inputs/')):
                result['reasons'].append(f'declared external input may affect unmodeled legacy certificates: {p}')
            if not owners and not safe and not p.startswith(SHARED):
                result['reasons'].append(f'unknown/unpackaged impact: {p}')
            for snapshot in (old, new):
                if p in snapshot.tree and snapshot.tree[p][0] not in ('100644', '100755'):
                    result['errors'].append(f'changed symlink/submodule forbidden: {p}')
        if shared:
            affected |= {d for graph in graphs for d in graph}
        # Union of both graphs preserves dropped and transitive dependency edges.
        while True:
            more = {d for graph in graphs for d, pkg in graph.items() if pkg['dependencies'] & affected}
            if more <= affected:
                break
            affected |= more
        result['affected_packages'] = sorted(affected)
        for d in sorted(affected):
            if d not in after:
                result['reasons'].append(f'deleted or invalid package needs review: {d}')
                continue
            pkg = after[d]
            if d in target_packages and target is not old:
                target_pkg = target_packages[d]
                def contract(p):
                    return p['sources'], verification_contract(p['verify']), p['task']['scope']
                if (d not in before or contract(target_pkg) != contract(before[d])) and contract(target_pkg) != contract(pkg):
                    result['reasons'].append(f'{d}: affected package changed on target base; rebase/review required')
            if pkg['unresolved']:
                result['reasons'].extend(f'{d}: {s}' for s in pkg['unresolved'])
            if d in before:
                previous = before[d]
                if domain_signature(old, previous['inputs']) != domain_signature(new, pkg['inputs']):
                    result['reasons'].append(f'{d}: domain-sensitive verifier structure changed')
                if previous['inputs'] - pkg['inputs'] or previous['dependencies'] - pkg['dependencies']:
                    result['reasons'].append(f'{d}: dependency declarations removed')
                # Scope and verifier contract changes require an independent AI-agent impact audit.
                for key in ('scope', 'classification'):
                    if previous['task'][key] != pkg['task'][key]:
                        result['reasons'].append(f'{d}: task {key} changed')
                if verification_contract(previous['verify']) != verification_contract(pkg['verify']):
                    result['reasons'].append(f'{d}: verification contract changed')
            result['packages'].append(d)
            result['workload_seconds'] += pkg['seconds']
        if result['errors'] or result['reasons']:
            result['level'] = 'full-verification-required'
        else:
            result['level'] = 'targeted-replay' if affected else 'fast-only'
            result['dependency_closure'] = 'declared-inputs-only; static tripwires and filesystem isolation required'
            # A queue budget does not change mathematical impact or discard part
            # of the required affected set. Defer the entire set when it cannot
            # fit the automatic job; a maintainer must arrange its complete replay.
            if len(result['packages']) > MAX_PACKAGES:
                result['scheduling_reasons'].append('automatic replay package cap exceeded')
            if result['workload_seconds'] > MAX_SECONDS:
                result['scheduling_reasons'].append('automatic replay time cap exceeded')
            for directory in result['packages']:
                if after[directory]['seconds'] > MAX_PACKAGE_SECONDS:
                    result['scheduling_reasons'].append(
                        f'{directory}: automatic per-package time cap exceeded')
            if result['scheduling_reasons']:
                result['replay_schedule'] = 'deferred-budget'
            else:
                result['replay_schedule'] = 'ready' if affected else 'not-required'
                result['replay_allowed'] = bool(affected)
    except (Invalid, OSError, ValueError, KeyError, TypeError, RecursionError, subprocess.SubprocessError) as exc:
        result['errors'].append(f'cannot safely classify impact: {exc}')
    return result

