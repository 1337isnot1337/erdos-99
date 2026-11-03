#!/usr/bin/env python3
"""Create a text-only archival export; never run or alter the supplied research.

Usage: python build_snapshot.py --source INPUT_DIRECTORY --destination NEW_ARCHIVE
The four historical root documents and research/ are the source boundary.
This is an archival transformation, not a mathematical or licensing verifier.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


def sha(data):
    return hashlib.sha256(data).hexdigest()


def dump(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2) + '\n'


SECRET_PATTERNS = {
    'github_token': r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b',
    'openai_key': r'\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b',
    'google_key': r'\bAIza[0-9A-Za-z_-]{35}\b',
    'private_key': r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----[\s\S]*?-----END (?:RSA |OPENSSH |EC )?PRIVATE KEY-----',
}
HOME = re.compile(r'''(?i)[a-z]:[\\/]+Users[\\/]+[^\\/\s"'<>]+|/(?:home|Users)/[^/\s"'<>]+''')
EMAIL = re.compile(r'(?i)(?<![\w.+-])[\w.+-]+@[\w.-]+\.[a-z]{2,}(?![\w.-])')
PRIVATE_CHAT = re.compile(r'https?://(?:chatgpt\.com|chat\.openai\.com)/(?:c|g)/[^\s"<>\\)]+')
LOCAL_URL = re.compile(r'https?://(?:localhost|127\.0\.0\.1)(?::\d+)?(?:/[^\s"<>\\)]*)?')
SENSITIVE_KEYS = {'apikey', 'accesstoken', 'refreshtoken', 'executiontoken', 'turntoken',
                  'password', 'authorization', 'cookie', 'cookies', 'secret',
                  'threadid', 'turnid', 'browserprofile', 'browserid', 'projectid',
                  'systemprompt', 'developerprompt', 'hiddenreasoning', 'chainofthought'}
EXCLUDED_BINARY = {'.pdf', '.png', '.jpg', '.jpeg', '.gif', '.tiff', '.bmp'}


def omit_reason(rel):
    p = Path(rel)
    if '__pycache__' in p.parts or p.suffix.lower() == '.pyc':
        return 'operational bytecode cache; not a source research artifact'
    if p.suffix.lower() in EXCLUDED_BINARY:
        return 'third-party paper or page image; reference only, no redistribution clearance asserted'
    if '/sources/' in rel and p.suffix.lower() == '.txt':
        return 'third-party full-text paper extraction; reference only'
    if '/primary-source-check/' in rel and rel.endswith('.lean.excerpt.txt'):
        return 'third-party Lean source excerpt; pinned retrieval metadata retained instead'
    return None


def decode(data):
    if data.startswith(b'\xff\xfe') or data.startswith(b'\xfe\xff'):
        return data.decode('utf-16'), 'UTF-16 BOM decoded to UTF-8'
    if data.startswith(b'\xef\xbb\xbf'):
        return data.decode('utf-8-sig'), 'UTF-8 BOM removed'
    return data.decode('utf-8'), None


def sanitize(text, rel, excerpts):
    counts = Counter()

    def clean(s):
        for label, rx, replacement in [
            ('private_home_path', HOME, '<USER_HOME>'),
            ('email_address', EMAIL, '[REDACTED_EMAIL]'),
            ('private_chat_url', PRIVATE_CHAT, '[PRIVATE_CHAT_URL]'),
            ('local_service_url', LOCAL_URL, '[LOCAL_SERVICE_URL]'),
        ]:
            s, n = rx.subn(replacement, s)
            counts[label] += n
        for label, pattern in SECRET_PATTERNS.items():
            s, n = re.subn(pattern, '[REDACTED_' + label.upper() + ']', s)
            counts[label] += n
        for excerpt in excerpts:
            for candidate in (excerpt, excerpt.replace('\r\n', '\n')):
                n = s.count(candidate)
                if n:
                    s = s.replace(candidate, '[Third-party source excerpt omitted; see pinned primary-source-check/retrieval.json.]')
                    counts['third_party_excerpt'] += n
        if rel.endswith('1339-supplied-core-counting-source-audit.task.md'):
            s, n = re.subn(r'(?m)^(?:\d{3,5}:.*(?:\r?\n|$))+',
                           '[Numbered third-party Lean excerpt omitted; see pinned retrieval metadata.]\n', s)
            counts['third_party_numbered_excerpt_block'] += n
        return s

    def walk(o):
        if isinstance(o, dict):
            result = {}
            for k, v in o.items():
                normalized = re.sub(r'[^a-z]', '', k.lower())
                if normalized in SENSITIVE_KEYS and v:
                    result[k] = '[REDACTED_PRIVATE_EXECUTION_METADATA]'
                    counts['private_execution_metadata'] += 1
                else:
                    result[k] = walk(v)
            return result
        if isinstance(o, list):
            return [walk(v) for v in o]
        if isinstance(o, str):
            return clean(o)
        return o

    if rel.endswith('.json'):
        try:
            original = json.loads(text)
        except ValueError:
            # Preserve historically malformed JSON as text, explicitly inventoried.
            return clean(text), {k: v for k, v in counts.items() if v}, 'historically invalid JSON; exported as text'
        updated = walk(original)
        if any(counts.values()):
            text = dump(updated)
    elif rel.endswith('.jsonl'):
        lines = text.splitlines(keepends=True)
        updated = []
        for line in lines:
            try:
                obj = json.loads(line)
            except ValueError:
                updated.append(clean(line))
                continue
            before = sum(counts.values())
            obj = walk(obj)
            updated.append(json.dumps(obj, ensure_ascii=False) + '\n' if sum(counts.values()) != before else line)
        text = ''.join(updated)
    else:
        text = clean(text)
    return text, {k: v for k, v in counts.items() if v}, None


def build(source, destination):
    source, destination = source.resolve(), destination.resolve()
    if destination.is_relative_to(source) or source.is_relative_to(destination):
        raise ValueError('source and destination must be disjoint')
    files = sorted((p for p in source.rglob('*') if p.is_file()),
                   key=lambda p: p.relative_to(source).as_posix())
    for p in files:
        if p.is_symlink() or not p.resolve().is_relative_to(source):
            raise ValueError('source must contain only regular files inside its root')
        rel = p.relative_to(source)
        if rel.parts[0] != 'research' and rel.as_posix() not in {
            'START_HERE.md', 'CONTINUE_PROMPT.md', 'DIRAC_COMPLETION_SUMMARY.md', 'MANIFEST.json'
        }:
            raise ValueError('unexpected source boundary: ' + rel.as_posix())
    excerpts = [decode(p.read_bytes())[0] for p in files if p.name.endswith('.lean.excerpt.txt')]
    destination.mkdir(parents=True, exist_ok=True)
    payload = destination / 'payload'
    payload.mkdir(exist_ok=True)
    entries, shards, batch = [], [], []
    tree = hashlib.sha256()
    batch_bytes = 0

    def flush():
        nonlocal batch, batch_bytes
        if not batch:
            return
        name = 'payload/part-%03d.jsonl' % (len(shards) + 1)
        data = b''.join(batch)
        (destination / name).write_bytes(data)
        shards.append(dict(path=name, bytes=len(data), sha256=sha(data), records=len(batch)))
        batch, batch_bytes = [], 0

    for p in files:
        rel = p.relative_to(source).as_posix()
        data = p.read_bytes()
        h = sha(data)
        tree.update((h + '  ' + rel + '\n').encode('utf-8'))
        entry = dict(source_path=rel, source_kind='regular-file', source_bytes=len(data), source_sha256=h)
        reason = omit_reason(rel)
        if reason:
            entry.update(disposition='omitted', reason=reason)
        else:
            text, normalization = decode(data)
            text, changes, note = sanitize(text, rel, excerpts)
            exported_path = rel + '.source' if p.suffix in {'.py', '.ps1'} else rel
            published = text.encode('utf-8')
            entry.update(disposition='included', export_path=exported_path,
                         published_bytes=len(published), published_sha256=sha(published),
                         transformations=changes)
            if normalization:
                entry['normalization'] = normalization
            if note:
                entry['format_note'] = note
            # Bound every Git blob below the intake scanner's 2 MiB limit,
            # including research files that are individually several MiB.
            chunks = [text[i:i + 120_000] for i in range(0, len(text), 120_000)] or ['']
            entry['chunks'] = []
            for part, chunk in enumerate(chunks):
                line = (json.dumps(dict(path=exported_path, part=part, parts=len(chunks), content=chunk),
                                   ensure_ascii=False, separators=(',', ':')) + '\n').encode('utf-8')
                if batch_bytes + len(line) > 1_500_000:
                    flush()
                fragment = chunk.encode('utf-8')
                entry['chunks'].append(dict(shard='payload/part-%03d.jsonl' % (len(shards) + 1),
                                            part=part, bytes=len(fragment), sha256=sha(fragment)))
                batch.append(line)
                batch_bytes += len(line)
        entries.append(entry)
    flush()
    source_tree = tree.hexdigest()
    inventory_dir = destination / 'inventory'
    inventory_dir.mkdir(exist_ok=True)
    entry_shards, entry_batch, entry_bytes = [], [], 0

    def flush_entries():
        nonlocal entry_batch, entry_bytes
        if not entry_batch:
            return
        name = 'inventory/entries-%03d.json' % (len(entry_shards) + 1)
        data = dump(entry_batch).encode('utf-8')
        (destination / name).write_bytes(data)
        entry_shards.append(dict(path=name, bytes=len(data), sha256=sha(data), records=len(entry_batch)))
        entry_batch, entry_bytes = [], 0

    for entry in entries:
        size = len(dump(entry).encode('utf-8')) + 100
        if entry_bytes + size > 1_300_000:
            flush_entries()
        entry_batch.append(entry)
        entry_bytes += size
    flush_entries()
    manifest = dict(schema='erdos99-text-progress-archive-v2', snapshot_date='2026-11-04',
                    research_status='paused', scientific_status='partially_reviewed',
                    upstream_base='b05cd57b15252fe99577de3edb0b73070e79544f',
                    source_identity='Non-Git handoff directory plus saved follow-up research and read-only job recovery',
                    source_tree_sha256=source_tree,
                    source_tree_algorithm='SHA256 of concatenated source_sha256 + two ASCII spaces + source_path + LF, files sorted by relative path using Unicode code point order',
                    source_files=len(entries), source_bytes=sum(e['source_bytes'] for e in entries),
                    included_files=sum(e['disposition']=='included' for e in entries),
                    omitted_files=sum(e['disposition']=='omitted' for e in entries),
                    shards=shards, entry_shards=entry_shards)
    (destination / 'inventory.json').write_text(dump(manifest), encoding='utf-8', newline='\n')
    report = dict(source_tree_sha256=source_tree, source_files=manifest['source_files'],
                  included_files=manifest['included_files'], omitted_files=manifest['omitted_files'],
                  transformed_files=sum(bool(e.get('transformations') or e.get('normalization')) for e in entries),
                  transformations=dict(sum((Counter(e.get('transformations', {})) for e in entries), Counter())),
                  omitted_reasons=dict(Counter(e['reason'] for e in entries if e['disposition']=='omitted')),
                  shard_files=len(shards), payload_bytes=sum(s['bytes'] for s in shards),
                  policy='No binary/base64 payloads. Private home paths, emails, private chat and local service URLs, credentials and private execution metadata are redacted. Known full third-party source extracts are omitted. This is a bounded scan, not a universal privacy or rights guarantee.')
    (destination / 'export-report.json').write_text(dump(report), encoding='utf-8', newline='\n')
    print(dump(report), end='')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True, type=Path)
    parser.add_argument('--destination', required=True, type=Path)
    args = parser.parse_args()
    build(args.source, args.destination)
