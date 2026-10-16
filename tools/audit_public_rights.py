#!/usr/bin/env python3
"""Group exact publication provenance for human rights decisions; never grant rights.

Reads immutable public and source Git objects. Observed author names are evidence
of Git attribution, not proof that aliases are distinct people or rights holders.
Private Git author names and email values are never emitted in the public report.
The report intentionally leaves imported rights pending.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
import hashlib
import json
import os
import secrets
from pathlib import Path
import re
import subprocess


ADAPTATION_SOURCE = 'd54097cb'
ADAPTATION_PATHS = {
    'tools/local_ci.py', 'tools/ci_integrity.py', 'tools/test_local_ci.py',
    'tools/localized_ci/__init__.py', 'tools/localized_ci/packages.py',
    'tools/localized_ci/plan.py', 'tools/localized_ci/replay.py',
    'tools/requirements-integrity-linux-x86_64.lock',
}


def git(root, *args):
    return subprocess.check_output(['git', '--no-replace-objects', '-C', str(root), *args],
                                   stderr=subprocess.PIPE, timeout=120)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def history(root, ref, paths):
    # Rename/copy ancestry is not inferred. Exact pinned path/blob remains checked.
    data = git(root, 'log', '--format=%x1e%H%x00%an', '--name-only', '--no-renames', '--full-history', '-m', ref, '--', *paths)
    result = defaultdict(lambda: {'authors': set(), 'commits': []})
    for block in data.decode('utf-8').split('\x1e')[1:]:
        lines = block.splitlines()
        commit, author = lines[0].split('\0', 1)
        if not re.fullmatch('[0-9a-f]{40}', commit):
            raise ValueError('invalid history commit')
        for path in lines[1:]:
            if path in paths:
                result[path]['authors'].add(author)
                if commit not in result[path]['commits']:
                    result[path]['commits'].append(commit)
    return result


def classify(path, content, derived=False):
    text = content.decode('utf-8', 'replace')
    if path == 'LICENSE':
        return 'standard-license-text'
    if derived:
        return 'adapted-project-ci'
    if path.startswith(('docs/problem/literature',)) or path in {
        'docs/literature_review.md', 'docs/reports/erdos_problem_99_1.6.0.md',
        'docs/reports/target_c_woodall_diameter_topology_2026-09-10.md',
    }:
        return 'project-exposition-of-external-mathematics'
    if re.search(r'(?im)^(?:#|//|/\*|\*)?\s*(?:Copyright\s+(?:\(c\)\s*)?\d|SPDX-License-Identifier:)', text):
        return 'source-specific-notice-review'
    return 'project-origin-candidate'


def valid_path(value):
    return isinstance(value, str) and bool(value) and not value.startswith(('/', '-')) and not any(c in value for c in ('\\', '\0', '\n', '\r')) and all(x not in ('', '.', '..') and x.casefold() != '.git' for x in value.split('/'))


def audit(public, source, ref='HEAD', identities=None):
    if ref.startswith('-'):
        raise ValueError('invalid ref')
    candidate = git(public, 'rev-parse', '--verify', ref + '^{commit}').decode().strip()
    manifest_bytes = git(public, 'show', candidate + ':docs/publication/inclusion.json')
    manifest = json.loads(manifest_bytes)
    if git(source, 'rev-parse', '--is-shallow-repository').strip() != b'false':
        raise ValueError('complete nonshallow source history required')
    baseline = manifest['source_commit']
    if not isinstance(baseline, str) or not re.fullmatch('[0-9a-f]{40}', baseline):
        raise ValueError('invalid source pin')
    baseline_paths = set(git(source, 'ls-tree', '-rz', '--name-only', baseline).decode().rstrip('\0').split('\0'))
    entries = manifest['entries']
    source_groups = defaultdict(list)
    seen = set()
    for e in entries:
        if not valid_path(e.get('source_path')) or not valid_path(e.get('public_path')):
            raise ValueError('unsafe manifest path')
        for key, length in (('source_commit',40),('source_blob',40),('source_sha256',64),('public_sha256',64)):
            if not isinstance(e.get(key), str) or not re.fullmatch('[0-9a-f]{%d}' % length, e[key]):
                raise ValueError('invalid manifest source/hash field')
        if e['public_path'] in seen:
            raise ValueError('duplicate inclusion path')
        seen.add(e['public_path'])
        source_groups[e['source_commit']].append(e)
    histories = {}
    for rev, subset in source_groups.items():
        histories[rev] = history(source, rev, {e['source_path'] for e in subset})
    pubpaths = git(public, 'ls-tree', '-rz', '--name-only', candidate).decode().rstrip('\0').split('\0')
    pub_history = history(public, candidate, set(pubpaths))
    imported = {e['public_path']: e for e in entries}
    records = []
    failures = []
    groups = {}
    adapted_ref = git(source, 'rev-parse', '--verify', ADAPTATION_SOURCE + '^{commit}').decode().strip()
    adapted_history = history(source, adapted_ref, ADAPTATION_PATHS)
    identity_map = identities if identities is not None else {}
    names = set()
    for collection in [pub_history, adapted_history, *histories.values()]:
        for evidence in collection.values():
            names.update(evidence['authors'])
    for name in sorted(names):
        if name not in identity_map:
            identity_map[name] = 'IDENTITY-' + secrets.token_hex(8).upper()
    for path in pubpaths:
        data = git(public, 'show', candidate + ':' + path)
        item = {'public_path': path, 'public_sha256': sha(data)}
        if path in imported:
            e = imported[path]
            blob = git(source, 'rev-parse', e['source_commit'] + ':' + e['source_path']).decode().strip()
            original = git(source, 'cat-file', 'blob', blob)
            if blob != e['source_blob'] or sha(original) != e['source_sha256'] or sha(data) != e['public_sha256']:
                failures.append({'path': path, 'kind': 'pinned-hash-mismatch'})
            h = histories[e['source_commit']].get(e['source_path'])
            if not h:
                failures.append({'path': path, 'kind': 'missing-path-history'})
                h = {'authors': set(), 'commits': []}
            item.update({'source_commit': e['source_commit'], 'source_blob': blob,
                         'source_sha256': sha(original), 'source_path': e['source_path'],
                         'manifest_disposition': e['publication_clearance']})
            provenance = 'included-source'
        elif path in ADAPTATION_PATHS:
            h = {'authors': pub_history[path]['authors'] | adapted_history[path]['authors'],
                 'commits': list(dict.fromkeys(pub_history[path]['commits'] + adapted_history[path]['commits']))}
            original = git(source, 'show', adapted_ref + ':' + path)
            item.update({'source_commit': adapted_ref, 'source_path': path,
                         'source_blob': git(source, 'rev-parse', adapted_ref + ':' + path).decode().strip(),
                         'source_sha256': sha(original),
                         'derivation_evidence': 'NOTICE identifies this proposal as CI adaptation source; no identity/equivalence claim'})
            provenance = 'notice-declared-ci-adaptation'
        else:
            h = pub_history[path]
            provenance = 'publication-tree-origin-not-independently-established'
            if path in baseline_paths:
                possible = git(source, 'show', baseline + ':' + path)
                item['same_path_source_evidence'] = {
                    'source_commit': baseline,
                    'source_blob': git(source, 'rev-parse', baseline + ':' + path).decode().strip(),
                    'source_sha256': sha(possible), 'byte_identical': possible == data,
                    'meaning': 'Shared path is a review lead, not an assertion of derivation or permission'}
                if possible == data:
                    provenance = 'unmanifested-byte-identical-source'
        kind = classify(path, data, path in ADAPTATION_PATHS)
        authors = sorted(identity_map[name] for name in h['authors'])
        key = (provenance, item.get('source_commit', candidate), tuple(authors), kind)
        identifier = 'RIGHTS-' + sha(json.dumps(key, ensure_ascii=True).encode())[:12].upper()
        item.update({'group': identifier, 'observed_author_ids': authors,
                     'touching_commit_count': len(h['commits']),
                     'earliest_observed_path_commit': h['commits'][-1] if h['commits'] else None})
        if key not in groups:
            groups[key] = {'id': identifier, 'provenance_class': provenance,
                           'source_commit': item.get('source_commit', candidate),
                           'content_class': kind, 'observed_author_ids': authors,
                           'disposition': 'OWNER DECISION REQUIRED', 'files': []}
        groups[key]['files'].append(path)
        records.append(item)
    return {'schema_version': 1, 'status': 'BLOCKED' if failures else 'OWNER DECISION REQUIRED',
            'public_candidate': candidate,
            'public_tree': git(public, 'rev-parse', candidate + '^{tree}').decode().strip(),
            'inclusion_sha256': sha(manifest_bytes),
            'counts': {'retained_files': len(records), 'included_source_files': len(entries),
                       'public_only_files': len(records)-len(entries), 'provenance_groups': len(groups),
                       'source_pins': len(source_groups), 'verified_source_hashes': len(entries)-sum(x['kind'] == 'pinned-hash-mismatch' for x in failures)},
            'failures': failures, 'groups': sorted(groups.values(), key=lambda x:x['id']),
            'files': records,
            'permission_evidence': [
                {'path':'NOTICE', 'meaning':'Conditional project Apache offer and attribution, not proof of upstream ownership'},
                {'path':'CONTRIBUTING.md', 'meaning':'Prospective inbound Apache contribution terms; not retroactive consent from archive contributors'},
                {'path':'docs/publication/provenance.md', 'meaning':'Records intended Apache terms; actual ownership, contributor grants and alias control still require confirmation'},
            ],
            'limits': ['This report grants no license and changes no inclusion clearance.',
                       'Opaque identity IDs describe observed Git author labels, not distinct people, ownership or consent; exact name mapping remains private.',
                       'Path history is complete within the selected ref without following renames/copies.',
                       'Content categories are review queues, not determinations of originality or legal exceptions.',
                       'Cited mathematical statements and project exposition require separate judgment from copied paper expression.',
                       'The report covers its exact public_candidate; regenerate for a changed candidate.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--public', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--ref', default='HEAD')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--private-identities', type=Path, help='External private name-to-opaque-ID mapping; reuse for stable IDs across candidates')
    args = parser.parse_args()
    try:
        identities = {}
        if args.private_identities:
            mapping_path = args.private_identities.resolve()
            if mapping_path.is_relative_to(args.public.resolve()):
                raise ValueError('private identity map must stay outside publication repository')
            if mapping_path.exists():
                identities = json.loads(mapping_path.read_text())
                if not isinstance(identities, dict) or not all(isinstance(k,str) and isinstance(v,str) and re.fullmatch('IDENTITY-[0-9A-F]{16}',v) for k,v in identities.items()) or len(set(identities.values())) != len(identities):
                    raise ValueError('invalid private identity map')
        result = audit(args.public, args.source, args.ref, identities)
        if args.private_identities:
            fd = os.open(mapping_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
            with os.fdopen(fd, 'w') as output:
                output.write(json.dumps(identities, indent=2) + '\n')
            mapping_path.chmod(0o600)
        args.output.write_text(json.dumps(result, indent=2, ensure_ascii=True) + '\n')
        print(json.dumps({k:result[k] for k in ('status','public_candidate','counts','failures')}, indent=2))
        return int(bool(result['failures']))
    except (ValueError, KeyError, OSError, subprocess.SubprocessError) as error:
        print(json.dumps({'status':'BLOCKED','error_type':type(error).__name__}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
