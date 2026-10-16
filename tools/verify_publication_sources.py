#!/usr/bin/env python3
"""Verify public manifest bytes, optionally against a frozen source repository.

The default invocation needs only this publication checkout. The optional source
checkout is an auditor input, never a prerequisite of proofs or certificate replay.
No source text, author metadata, or credential values are printed or recorded.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

HEX40 = re.compile(r'[0-9a-f]{40}\Z')
HEX64 = re.compile(r'[0-9a-f]{64}\Z')


def safe_path(value):
    if not isinstance(value, str) or not value or '\\' in value or ':' in value:
        raise ValueError('noncanonical manifest path')
    p = PurePosixPath(value)
    if p.is_absolute() or any(x in ('', '.', '..') for x in value.split('/')):
        raise ValueError('noncanonical manifest path')
    return value


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(repo, *args):
    return subprocess.check_output(['git', '--no-replace-objects', '-C', str(repo), *args])


def source_tree(repo, commit):
    if not isinstance(commit, str) or not HEX40.fullmatch(commit):
        raise ValueError('invalid source commit')
    if git(repo, 'rev-parse', '--verify', '--end-of-options', commit + '^{commit}').decode().strip() != commit:
        raise ValueError('source commit identity mismatch')
    out = {}
    for raw in git(repo, 'ls-tree', '-r', '-z', commit).split(b'\0'):
        if raw:
            meta, name = raw.split(b'\t', 1)
            mode, kind, blob = meta.decode().split()
            out[name.decode()] = (mode, kind, blob)
    return out


def blob_hashes(repo, blobs):
    """Use one bounded Git batch; inspect types and lengths before hashing bytes."""
    wanted = sorted(set(blobs))
    if any(not isinstance(b, str) or not HEX40.fullmatch(b) for b in wanted):
        raise ValueError('invalid source blob identity')
    raw = b'' if not wanted else subprocess.check_output(
        ['git', '--no-replace-objects', '-C', str(repo), 'cat-file', '--batch'],
        input=('\n'.join(wanted) + '\n').encode())
    hashes = {}; offset = 0
    for requested in wanted:
        end = raw.index(b'\n', offset)
        header = raw[offset:end].decode().split()
        if len(header) != 3 or header[:2] != [requested, 'blob']:
            raise ValueError('source object missing or not a blob')
        size = int(header[2]); start = end + 1; offset = start + size + 1
        if raw[start + size:offset] != b'\n':
            raise ValueError('invalid Git batch framing')
        hashes[requested] = digest(raw[start:start + size])
    if offset != len(raw):
        raise ValueError('unexpected Git batch output')
    return hashes


def verify(root, source_repo=None):
    inc = json.loads((root / 'docs/publication/inclusion.json').read_text())
    exc = json.loads((root / 'docs/publication/exclusion.json').read_text())
    errors = []; records = []; imported = set(); public_paths = set(); excluded = set()
    for e in inc['entries']:
        path = safe_path(e['source_path']); public = safe_path(e['public_path'])
        if path in imported or public in public_paths:
            raise ValueError('duplicate retained manifest path')
        imported.add(path); public_paths.add(public)
        commit = e['source_commit']; blob = e['source_blob']; sha = e['source_sha256']
        if not HEX40.fullmatch(commit) or not HEX40.fullmatch(blob) or not HEX64.fullmatch(sha):
            raise ValueError('invalid retained source identity')
        target = root / public
        if not target.is_file() or target.is_symlink() or digest(target.read_bytes()) != e['public_sha256']:
            errors.append({'path': public, 'error': 'public bytes differ from inclusion manifest'})
        records.append({'source_path': path, 'source_commit': commit, 'source_blob': blob,
                        'source_mode': e['source_mode'], 'source_sha256': sha, 'kind': 'retained'})
    for e in exc:
        path = safe_path(e['source_path'])
        if path in excluded or path in imported:
            raise ValueError('duplicate or retained excluded path')
        excluded.add(path)
        records.append({'source_path': path, 'source_commit': e.get('source_commit', inc['source_commit']),
                        'source_blob': e['source_blob'], 'source_mode': e['source_mode'],
                        'source_sha256': e.get('source_sha256'), 'kind': 'excluded'})
        later = e.get('later_source_review')
        if later:
            records.append(dict(later, source_path=path, kind='later-excluded'))
    source_verified = 0
    if source_repo:
        trees = {c: source_tree(source_repo, c) for c in sorted({e['source_commit'] for e in records})}
        hashes = blob_hashes(source_repo, [e['source_blob'] for e in records])
        for e in records:
            path = e['source_path']; got = trees[e['source_commit']].get(path)
            if got != (e['source_mode'], 'blob', e['source_blob']):
                errors.append({'path': path, 'error': 'source tree/blob/mode mismatch'})
            elif e['source_sha256'] and hashes[e['source_blob']] != e['source_sha256']:
                errors.append({'path': path, 'error': 'source SHA256 mismatch'})
            else:
                source_verified += 1
    return {'retained_files': len(imported), 'excluded_files': len(excluded),
            'public_hashes_checked': len(public_paths), 'source_records_verified': source_verified,
            'source_verification_requested': source_repo is not None, 'errors': errors,
            'scope': 'byte and Git provenance only; no rights grant or proof correctness inferred'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--source-repo', type=Path)
    p.add_argument('--output', type=Path)
    a = p.parse_args()
    try:
        result = verify(a.root.resolve(), a.source_repo.resolve() if a.source_repo else None)
    except (KeyError, ValueError, OSError, subprocess.CalledProcessError) as e:
        # Do not print raw command output or manifest values on error.
        result = {'errors': [{'error': 'manifest/source verification failed', 'type': type(e).__name__}]}
    encoded = json.dumps(result, indent=2) + '\n'
    if a.output:
        a.output.write_text(encoded)
    print(encoded, end='')
    return 1 if result['errors'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
