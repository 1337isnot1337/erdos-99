"""Version 1 opt-in research packages: strict manifests and conservative input audit."""
from __future__ import annotations

import ast
import hashlib
import json
import re
from pathlib import PurePosixPath

PREFIX = 'research-packages/'
MAX_PACKAGES = 2
MAX_SECONDS = 240
MAX_PACKAGE_SECONDS = 120
MAX_INPUTS = 256
MAX_BLOB = 2 * 1024 * 1024
MANIFESTS = ('TASK.json', 'SOURCES.json', 'VERIFY.json', 'README.md')
SAFE_MODULES = {'math', 'itertools', 'functools', 'collections', 'fractions',
                'decimal', 'operator', 'json', 'statistics', 'bisect', 'heapq'}


class Invalid(ValueError):
    pass


def path(value):
    if (not isinstance(value, str) or not value or len(value) > 240
            or not re.fullmatch(r'[A-Za-z0-9_./-]+', value)
            or any(p in ('', '.', '..') for p in value.split('/'))
            or value.startswith('/') or value.startswith('-')):
        raise Invalid(f'noncanonical relative path: {value!r}')
    return value


def strict_json(raw):
    def pairs(items):
        result = {}
        for k, v in items:
            if k in result:
                raise Invalid(f'duplicate JSON key: {k}')
            result[k] = v
        return result
    try:
        return json.loads(raw, object_pairs_hook=pairs)
    except (ValueError, UnicodeError) as exc:
        raise Invalid(str(exc)) from exc


def keys(obj, required, optional=()):
    if not isinstance(obj, dict) or set(obj) - set(required) - set(optional) or set(required) - set(obj):
        raise Invalid(f'expected keys {required}, optional {optional}')


def strings(values, label, empty=True):
    if not isinstance(values, list) or (not empty and not values) or any(not isinstance(x, str) or not x.strip() for x in values):
        raise Invalid(f'{label}: expected list of nonempty strings')
    if len(values) != len(set(values)):
        raise Invalid(f'{label}: duplicate declaration')
    return values


def text(value):
    if not isinstance(value, str) or not value.strip():
        raise Invalid('expected nonempty text')


def sha(value, size):
    if not isinstance(value, str) or not re.fullmatch('[0-9a-f]{%d}' % size, value):
        raise Invalid(f'expected {size}-character hex digest')


def discover(tree):
    packages = set()
    for p in tree:
        if p.startswith(PREFIX):
            bits = p.split('/')
            if len(bits) < 3:
                raise Invalid(f'file outside a package: {p}')
            path(bits[1])
            packages.add('/'.join(bits[:2]))
    if len(packages) > 1000:
        raise Invalid('package registry exceeds 1000 entries; owner review required')
    return sorted(packages)


def load_package(snapshot, directory, *, audit=True):
    """Read Git blobs, never symlinks, and return normalized declared input graph."""
    path(directory)
    files = {p for p in snapshot.tree if p.startswith(directory + '/')}
    for name in MANIFESTS:
        if directory + '/' + name not in files:
            raise Invalid(f'{directory}: missing {name}')
    for p in files:
        path(p)
        snapshot.regular(p)
    text(snapshot.read(directory + '/README.md').decode('utf-8'))
    task, sources, verify = [strict_json(snapshot.read(directory + '/' + n)) for n in MANIFESTS[:3]]
    keys(task, ('version', 'id', 'scope', 'result', 'remaining_questions', 'classification'))
    if task['version'] != 1 or task['id'] != directory.split('/')[-1]:
        raise Invalid('task version/id mismatch')
    keys(task['scope'], ('statement', 'domain', 'limitations'))
    for value in [*task['scope'].values(), task['result']]:
        text(value)
    strings(task['remaining_questions'], 'remaining_questions')
    if task['classification'] not in ('unreviewed', 'conditional', 'regression'):
        raise Invalid('packages cannot promote canonical mathematics')
    keys(sources, ('version', 'baseline_commit', 'inputs', 'packages', 'unresolved'))
    if sources['version'] != 1:
        raise Invalid('source version')
    sha(sources['baseline_commit'], 40)
    if not snapshot.ancestor(sources['baseline_commit']):
        raise Invalid('source baseline is missing or is not an ancestor')
    deps = strings(sources['packages'], 'packages')
    for dep in deps:
        path(dep)
        if not dep.startswith(PREFIX) or len(dep.split('/')) != 2 or dep == directory:
            raise Invalid('invalid package dependency')
    unresolved = strings(sources['unresolved'], 'unresolved')
    if not isinstance(sources['inputs'], list) or not 1 <= len(sources['inputs']) <= MAX_INPUTS:
        raise Invalid('expected 1..256 source inputs')
    inputs = {}
    identities = set()
    for item in sources['inputs']:
        keys(item, ('path', 'sha256', 'identity', 'generated_from'), ('commit',))
        p = path(item['path'])
        text(item['identity'])
        if p in inputs or item['identity'] in identities:
            raise Invalid('duplicate source declaration or identity')
        identities.add(item['identity'])
        sha(item['sha256'], 64)
        snapshot.regular(p)
        if hashlib.sha256(snapshot.read(p)).hexdigest() != item['sha256']:
            raise Invalid(f'input hash mismatch: {p}')
        if 'commit' in item:
            sha(item['commit'], 40)
            if not snapshot.ancestor(item['commit']) or snapshot.read_at(item['commit'], p) != snapshot.read(p):
                raise Invalid(f'pinned commit does not contain input bytes: {p}')
        for generator in strings(item['generated_from'], 'generated_from'):
            path(generator)
        inputs[p] = item
    for item in inputs.values():
        if set(item['generated_from']) - inputs.keys():
            raise Invalid('generated source lacks declared generator inputs')
    keys(verify, ('version', 'inputs', 'environment', 'commands', 'domain'))
    if verify['version'] != 1 or verify['domain'] != task['scope']['domain']:
        raise Invalid('verification domain differs from task domain')
    if set(strings(verify['inputs'], 'VERIFY.inputs', empty=False)) != inputs.keys():
        raise Invalid('VERIFY/SOURCES input mismatch')
    keys(verify['environment'], ('python', 'dependencies'))
    # Runtime installations, even pip build hooks, are outside this small replay protocol.
    if verify['environment'] != {'python': '3.14', 'dependencies': []}:
        raise Invalid('unsupported environment/dependency installation; owner environment required')
    commands = verify['commands']
    if not isinstance(commands, list) or not 1 <= len(commands) <= 4:
        raise Invalid('expected 1..4 commands')
    total = 0
    for command in commands:
        keys(command, ('argv', 'timeout_seconds'))
        argv = strings(command['argv'], 'argv', empty=False)
        # No shell, interpreter options, environment overrides, or domain-reducing CLI flags.
        if len(argv) != 2 or argv[0] != '{python}' or path(argv[1]) not in inputs or not argv[1].endswith('.py'):
            raise Invalid('command must be ["{python}", "declared/script.py"]')
        timeout = command['timeout_seconds']
        if type(timeout) is not int or not 1 <= timeout <= MAX_PACKAGE_SECONDS:
            raise Invalid('command timeout outside 1..120 seconds')
        total += timeout
    if total > MAX_PACKAGE_SECONDS:
        raise Invalid('package total timeout exceeds 120 seconds')
    if audit:
        unresolved += audit_python(snapshot, inputs)
    return dict(directory=directory, task=task, sources=sources, verify=verify,
                files=files, inputs=set(inputs), dependencies=set(deps),
                unresolved=sorted(set(unresolved)), seconds=total)


def audit_python(snapshot, inputs):
    """Conservative tripwire, not a Python dependency completeness proof.

    Actual replay additionally exposes only declared repository inputs. Python patterns
    outside this restricted subset require review; no dynamic-import closure claim.
    """
    issues = []
    for p in sorted(inputs):
        if not p.endswith('.py'):
            continue
        try:
            tree = ast.parse(snapshot.read(p), filename=p)
        except (ValueError, SyntaxError) as exc:
            raise Invalid(f'invalid Python input {p}: {exc}') from exc
        for node in ast.walk(tree):
            modules = []
            if isinstance(node, ast.Import):
                modules = [a.name for a in node.names]
            if isinstance(node, ast.ImportFrom):
                if node.level or not node.module:
                    issues.append(f'{p}: relative/ambiguous import')
                else:
                    modules = [node.module]
            for module in modules:
                rel = module.replace('.', '/') + '.py'
                local_candidates = {rel, str(PurePosixPath(p).parent / rel)}
                if module in SAFE_MODULES and not (local_candidates & snapshot.tree.keys()):
                    continue
                choices = {rel, str(PurePosixPath(p).parent / rel)} & inputs.keys()
                if len(choices) != 1:
                    issues.append(f'{p}: unresolved import {module}')
                for choice in choices:
                    for parent in PurePosixPath(choice).parents:
                        initializer = str(parent / '__init__.py')
                        if initializer in snapshot.tree and initializer not in inputs:
                            issues.append(f'{p}: undeclared package initializer {initializer}')
            if isinstance(node, ast.Name) and (node.id.startswith('__') or node.id in {
                    'eval', 'exec', 'compile', 'globals', 'locals', 'vars', 'getattr', 'setattr',
                    'delattr', 'input', 'breakpoint', 'help', 'type', 'object', 'memoryview'}):
                issues.append(f'{p}: dynamic capability {node.id}')
            if isinstance(node, ast.Attribute) and (node.attr.startswith('__') or node.attr in {
                    'read_text', 'read_bytes', 'write_text', 'write_bytes', 'glob', 'rglob',
                    'iterdir', 'listdir', 'walk', 'open', 'load', 'loads', 'system', 'popen'}):
                # json.loads is harmless for dependency discovery, but deliberately conservative.
                issues.append(f'{p}: unresolved attribute capability {node.attr}')
            if isinstance(node, ast.Name) and node.id == 'open':
                parent_calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and n.func is node]
                if not parent_calls:
                    issues.append(f'{p}: aliased filesystem input')
                for call in parent_calls:
                    if (not call.args or not isinstance(call.args[0], ast.Constant)
                            or call.args[0].value not in inputs
                            or len(call.args) > 2 or call.keywords
                            or (len(call.args) == 2 and (not isinstance(call.args[1], ast.Constant)
                                or call.args[1].value not in ('r', 'rb')))):
                        issues.append(f'{p}: undeclared/dynamic filesystem input')
    return sorted(set(issues))
