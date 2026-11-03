#!/usr/bin/env python3
"""Verify the archive's full inventory and text payload without executing research.

Optionally compare every original byte to --source, or restore inert text files
to a NEW --extract directory. No archived research launcher is ever invoked.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe_path(s):
    require(isinstance(s, str) and bool(s), 'path must be a nonempty string')
    require('\\' not in s and ':' not in s and '\x00' not in s, 'unsafe path characters')
    require(not s.startswith('/') and all(p not in {'', '.', '..'} for p in s.split('/')), 'unsafe relative path')
    require(PurePosixPath(s).as_posix() == s, 'noncanonical path')
    return s


def verify(root, source=None, extract=None):
    root = root.resolve()
    manifest = json.loads((root / 'inventory.json').read_text(encoding='utf-8'))
    require(manifest['schema'] == 'erdos99-text-progress-archive-v2', 'unknown schema')
    entries = []
    entry_paths = []
    for shard in manifest['entry_shards']:
        rel = safe_path(shard['path'])
        entry_paths.append(rel)
        p = root / rel
        require(not p.is_symlink() and p.resolve().is_relative_to(root), 'unsafe inventory shard')
        data = p.read_bytes()
        require(len(data) < 2 * 1024 * 1024, 'inventory exceeds intake blob limit')
        require(len(data) == shard['bytes'] and sha(data) == shard['sha256'], 'inventory shard bytes differ')
        rows = json.loads(data)
        require(isinstance(rows, list) and len(rows) == shard['records'], 'inventory shard count differs')
        entries.extend(rows)
    require(len(set(entry_paths)) == len(entry_paths), 'duplicate inventory shard')
    require({p.relative_to(root).as_posix() for p in (root / 'inventory').glob('*')} == set(entry_paths), 'unlisted or missing inventory shard')
    require(len(entries) == manifest['source_files'], 'source count differs')
    require([e['source_path'] for e in entries] == sorted(e['source_path'] for e in entries), 'inventory not sorted')
    require(len({e['source_path'] for e in entries}) == len(entries), 'duplicate original path')
    tree = hashlib.sha256()
    included, omitted = {}, []
    for e in entries:
        safe_path(e['source_path'])
        require(e['source_kind'] == 'regular-file', 'nonregular source kind')
        require(re.fullmatch('[0-9a-f]{64}', e['source_sha256']), 'bad source hash')
        require(e['source_bytes'] >= 0, 'bad source byte length')
        tree.update((e['source_sha256'] + '  ' + e['source_path'] + '\n').encode('utf-8'))
        if e['disposition'] == 'included':
            rel = safe_path(e['export_path'])
            require(rel not in included, 'duplicate export path')
            require(not rel.endswith(('.py', '.ps1', '.pyc', '.pdf', '.png', '.jpg', '.jpeg')), 'executable or binary export path')
            included[rel] = e
        else:
            require(e['disposition'] == 'omitted' and bool(e['reason']), 'unexplained omission')
            omitted.append(e)
    require(tree.hexdigest() == manifest['source_tree_sha256'], 'source tree pin differs')
    require(len(included) == manifest['included_files'] and len(omitted) == manifest['omitted_files'], 'disposition count differs')
    require(sum(e['source_bytes'] for e in entries) == manifest['source_bytes'], 'source byte total differs')
    if source is not None:
        source = source.resolve()
        actual = {p.relative_to(source).as_posix() for p in source.rglob('*') if p.is_file()}
        require(actual == {e['source_path'] for e in entries}, 'original source file inventory changed')
        for e in entries:
            p = source / e['source_path']
            require(not p.is_symlink() and p.resolve().is_relative_to(source), 'unsafe original file')
            data = p.read_bytes()
            require(len(data) == e['source_bytes'] and sha(data) == e['source_sha256'], 'original source bytes changed: ' + e['source_path'])
    if extract is not None:
        extract = extract.resolve()
        require(not extract.exists(), 'extraction requires a new directory')
        require(not extract.is_relative_to(root), 'extract outside the archive')
    pieces, syntax_errors, invalid_json = {}, [], []
    scans = {
        'private_home': re.compile(r'(?i)[a-z]:[\\/]+Users[\\/]+[^\\/\s"<>]+|/(?:home|Users)/[^/\s"<>]+'),
        'github_credential': re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b'),
        'openai_credential': re.compile(r'\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b'),
        'google_credential': re.compile(r'\bAIza[0-9A-Za-z_-]{35}\b'),
        'private_key': re.compile(r'(?m)^-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----'),
        'private_chat': re.compile(r'https?://(?:chatgpt\.com|chat\.openai\.com)/(?:c|g)/[^\s"<>]+'),
        'email_address': re.compile(r'(?i)(?<![\w.+-])[\w.+-]+@[\w.-]+\.[a-z]{2,}(?![\w.-])'),
        'local_service_url': re.compile(r'https?://(?:localhost|127\.0\.0\.1)(?::\d+)?(?:/[^\s"<>]*)?'),
    }
    shard_paths = [safe_path(s['path']) for s in manifest['shards']]
    require(len(set(shard_paths)) == len(shard_paths), 'duplicate shard')
    require({p.relative_to(root).as_posix() for p in (root / 'payload').glob('*')} == set(shard_paths), 'unlisted or missing payload shard')
    transformations = Counter()
    syntax_checked = 0
    for shard in manifest['shards']:
        p = root / shard['path']
        require(not p.is_symlink() and p.resolve().is_relative_to(root), 'unsafe shard')
        data = p.read_bytes()
        require(len(data) < 2 * 1024 * 1024, 'payload exceeds intake blob limit')
        require(len(data) == shard['bytes'] and sha(data) == shard['sha256'], 'shard bytes differ: ' + shard['path'])
        lines = data.decode('utf-8').splitlines()
        require(len(lines) == shard['records'], 'shard record count differs')
        for line in lines:
            row = json.loads(line)
            require(set(row) == {'path', 'part', 'parts', 'content'} and isinstance(row['content'], str), 'invalid payload record')
            rel, text = safe_path(row['path']), row['content']
            require(rel in included, 'unlisted payload record')
            e = included[rel]
            chunks = pieces.setdefault(rel, [])
            require(type(row['part']) is int and row['part'] == len(chunks), 'duplicate or noncontiguous fragment')
            require(row['parts'] == len(e['chunks']) and row['part'] < len(e['chunks']), 'fragment count differs')
            expected = e['chunks'][row['part']]
            require(expected['part'] == row['part'] and expected['shard'] == shard['path'], 'fragment assignment differs')
            content = text.encode('utf-8')
            require(len(content) == expected['bytes'] and sha(content) == expected['sha256'], 'fragment bytes differ: ' + rel)
            chunks.append(text)
    require(set(pieces) == set(included), 'payload incomplete')
    texts = {}
    for rel, chunks in pieces.items():
        e = included[rel]
        require(len(chunks) == len(e['chunks']), 'missing fragment')
        text = ''.join(chunks)
        texts[rel] = text
        content = text.encode('utf-8')
        require(len(content) == e['published_bytes'] and sha(content) == e['published_sha256'], 'published bytes differ: ' + rel)
        for label, rx in scans.items():
            require(not rx.search(text), label + ' indicator in ' + rel + ' (value not logged)')
        transformations.update(e['transformations'])
        if rel.endswith('.py.source'):
            syntax_checked += 1
            try:
                ast.parse(text, filename=rel)
            except SyntaxError as exc:
                syntax_errors.append(dict(path=rel, line=exc.lineno, error=exc.msg))
        if rel.endswith('.json'):
            try:
                json.loads(text)
            except ValueError:
                invalid_json.append(rel)
    # Write only after every integrity check succeeds; archived scripts stay .source.
    if extract is not None:
        extract.mkdir(parents=True)
        for rel, text in texts.items():
            p = extract / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            with p.open('xb') as f:
                f.write(text.encode('utf-8'))
    return dict(integrity='passed', source_compared=source is not None,
                source_tree_sha256=manifest['source_tree_sha256'], included_files=len(texts),
                omitted_files=len(omitted), shard_files=len(shard_paths),
                bounded_privacy_scan='passed', transformations=dict(transformations),
                archived_python_syntax_checked=syntax_checked, historical_syntax_errors=syntax_errors,
                historical_invalid_json=invalid_json,
                mathematical_proof=False, historical_launchers_executed=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--source', type=Path)
    parser.add_argument('--extract', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    result = verify(args.archive, args.source, args.extract)
    output = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + '\n'
    if args.report:
        args.report.write_text(output, encoding='utf-8', newline='\n')
    print(output, end='')
