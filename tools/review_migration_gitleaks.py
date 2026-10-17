"""Review only pinned mathematical grouping labels reported by Gitleaks.

The scanner remains unmodified. Reports and nonzero exits remain intact. Every
accepted finding is bound to an exact path, blob SHA1 and SHA256, line, column,
rule, fingerprint, redacted match, and the mathematical stem in committed JSON.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
import re
import subprocess
import tempfile


REVIEWED_MATH_GROUPS = {
    'docs/research/migration/2026-10-16/agent-1/evidence/source-main-three-way-assignment.jsonl': {
        'git_blob_sha': '7e465ddb9ff53fb529200531c25844555ac2d4e4',
        'sha256': 'c53df5cf13e198f26beffac7def573b62f61cd5d06f78570b64990d310c0cd27',
        'findings': {
            457: (618, 680, 'global_discrete_replacement_preservation_2026_10_15'),
            3480: (605, 656, 'global_convexity_exit_barrier_2026_10_12'),
        },
    },
    'docs/research/migration/2026-10-16/agent-1/evidence/source-main-three-way-units.jsonl': {
        'git_blob_sha': '15fc4368898a5dc48c595f7ad7e051156594a5b0',
        'sha256': 'a53dbb9cae6e7f5a44a888c9fdea0458e3293da99e98b5b76b43de564afab474',
        'findings': {
            510: (123, 174, 'global_convexity_exit_barrier_2026_10_12'),
            513: (131, 193, 'global_discrete_replacement_preservation_2026_10_15'),
        },
    },
    'docs/research/migration/2026-10-16/agent-2/corpus-assignment.jsonl': {
        'git_blob_sha': '92275d3ca0cd358ad03db1dd0d7e95437dc09d35',
        'sha256': '449d402bd36d5c001e83e08b65f78774074e794bd0fd25febb4f7df5ddeb739e',
        'findings': {
            455: (736, 787, 'global_convexity_exit_barrier_2026_10_12'),
            457: (665, 727, 'global_discrete_replacement_preservation_2026_10_15'),
            458: (749, 813, 'global_joint_stress_strain_phase_mechanism_2026_10_12'),
            3479: (703, 750, 'global_convex_bank_defect_2026_10_02'),
            3480: (625, 676, 'global_convexity_exit_barrier_2026_10_12'),
        },
    },
}

REVIEWED_SOURCE_FIXTURE = {
    'path': 'docs/research/migration/2026-10-16/integration/source-main/tools/test_local_ci.py.source',
    'git_blob_sha': 'c613e6d61df45ce818cf3f3d21218e48947d0fa4',
    'sha256': '0a54855e41dede9c9a4ace2923f8a1eff2f8c4aec29f7ce00822b17341a23f8a',
    'StartLine': 409, 'EndLine': 413, 'StartColumn': 55, 'EndColumn': 88,
}


def load_findings(report: Path, *, allow_duplicates: bool = False) -> list[dict] | None:
    try:
        findings = json.loads(report.read_text())
        if not isinstance(findings, list) or not findings:
            return None
        if any(not isinstance(match, dict) for match in findings):
            return None
        fingerprints = [match.get('Fingerprint') for match in findings]
        if any(not isinstance(value, str) for value in fingerprints):
            return None
        if not allow_duplicates and len(set(fingerprints)) != len(fingerprints):
            return None
        return findings
    except (OSError, ValueError, TypeError):
        return None


def committed_blob(root: Path, revision: str, path: str) -> bytes:
    return subprocess.check_output([
        'git', '--no-replace-objects', '-C', str(root), 'show', revision + ':' + path,
    ], stderr=subprocess.PIPE)


def pinned_blob(data: bytes, record: dict) -> bool:
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()
    return blob == record['git_blob_sha'] and hashlib.sha256(data).hexdigest() == record['sha256']


def review_math_finding(root: Path, match: dict, *, candidate: str | None) -> dict | None:
    """Resolve report identities against Git bytes, never worktree substitutes."""
    try:
        path, line = match.get('File'), match.get('StartLine')
        if not isinstance(path, str) or type(line) is not int:
            return None
        record = REVIEWED_MATH_GROUPS.get(path)
        if record is None or line not in record['findings']:
            return None
        start, end, stem = record['findings'][line]
        if candidate is None:
            commit = match.get('Commit')
            if not isinstance(commit, str) or not re.fullmatch('[0-9a-f]{40}', commit):
                return None
            revision = commit
            fingerprint = f'{commit}:{path}:generic-api-key:{line}'
        else:
            if not re.fullmatch('[0-9a-f]{40}', candidate):
                return None
            commit, revision = '', candidate
            fingerprint = f'{path}:generic-api-key:{line}'
        expected = {
            'Commit': commit, 'File': path, 'RuleID': 'generic-api-key',
            'StartLine': line, 'EndLine': line,
            'StartColumn': start, 'EndColumn': end,
            'Fingerprint': fingerprint,
            'Match': 'unit_' + 'key":"REDACTED"', 'Secret': 'REDACTED',
            'SymlinkFile': '',
        }
        if any(match.get(key) != value for key, value in expected.items()):
            return None
        data = committed_blob(root, revision, path)
        if not pinned_blob(data, record):
            return None
        source_line = data.splitlines()[line - 1]
        source = json.loads(source_line)
        field = 'unit_' + 'key'
        if not isinstance(source, dict) or source.get(field) != stem:
            return None
        # Detector columns are pinned above to the observed scanner report.
        # Independently bind its field/value to the exact committed JSON line.
        literal = ('"' + field + '":"' + stem + '"').encode('ascii')
        if source_line.count(literal) != 1:
            return None
        return {**expected, 'committed_git_blob': record['git_blob_sha'],
                'committed_blob_sha256': record['sha256'], 'mathematical_stem': stem}
    except (OSError, ValueError, TypeError, IndexError, KeyError, subprocess.SubprocessError):
        return None


def review_source_fixture(root: Path, match: dict, *, candidate: str | None) -> dict | None:
    try:
        record = REVIEWED_SOURCE_FIXTURE
        path = record['path']
        if candidate is None:
            commit = match.get('Commit')
            if not isinstance(commit, str) or not re.fullmatch('[0-9a-f]{40}', commit):
                return None
            revision = commit
            fingerprint = f'{commit}:{path}:private-key:{record["StartLine"]}'
        else:
            if not re.fullmatch('[0-9a-f]{40}', candidate):
                return None
            commit, revision = '', candidate
            fingerprint = f'{path}:private-key:{record["StartLine"]}'
        expected = {key: record[key] for key in ('StartLine', 'EndLine', 'StartColumn', 'EndColumn')}
        expected.update({'Commit': commit, 'File': path, 'RuleID': 'private-key',
                         'Fingerprint': fingerprint, 'Match': 'REDACTED',
                         'Secret': 'REDACTED', 'SymlinkFile': ''})
        if any(match.get(key) != value for key, value in expected.items()):
            return None
        data = committed_blob(root, revision, path)
        if not pinned_blob(data, record):
            return None
        opening = ('-----BEGIN ' + 'PRIVATE KEY-----').encode('ascii')
        closing = ('-----END ' + 'PRIVATE KEY-----').encode('ascii')
        if data.count(opening) != 2 or closing in data:
            return None
        return {**expected, 'committed_git_blob': record['git_blob_sha'],
                'committed_blob_sha256': record['sha256'],
                'reason': 'Two exact negative-test opening delimiters; no closing delimiter or encoded key payload.'}
    except (OSError, ValueError, TypeError, KeyError, subprocess.SubprocessError):
        return None


def review_migration_finding(root: Path, match: dict, *, candidate: str | None) -> dict | None:
    return (review_math_finding(root, match, candidate=candidate)
            or review_source_fixture(root, match, candidate=candidate))


def history_occurrences(root: Path, finding: dict) -> int | None:
    """Count the exact parent diffs adding the matched committed source lines."""
    try:
        commit, path = finding['Commit'], finding['File']
        parents = subprocess.check_output([
            'git', '--no-replace-objects', '-C', str(root), 'show', '-s', '--format=%P', commit,
        ], text=True, stderr=subprocess.PIPE).split()
        if len(parents) < 2:
            return 1
        source = committed_blob(root, commit, path).splitlines()
        matched = source[finding['StartLine'] - 1:finding['EndLine']]
        count = 0
        for parent in parents:
            diff = subprocess.check_output([
                'git', '--no-replace-objects', '-C', str(root), 'diff',
                '--no-ext-diff', '--no-textconv', '--no-renames', '--unified=0',
                parent, commit, '--', path,
            ], stderr=subprocess.PIPE).splitlines()
            added = {line[1:] for line in diff if line.startswith(b'+') and not line.startswith(b'+++')}
            if matched and all(line in added for line in matched):
                count += 1
        return count
    except (OSError, ValueError, KeyError, subprocess.SubprocessError):
        return None


def review_tree_gitleaks(root: Path, report: Path, candidate: str) -> dict | None:
    findings = load_findings(report)
    if findings is None:
        return None
    reviewed = [review_migration_finding(root, match, candidate=candidate) for match in findings]
    if any(match is None for match in reviewed):
        return None
    return {
        'disposition': 'reviewed-false-positive',
        'finding_count': len(reviewed), 'findings': reviewed,
        'reason': 'Exact reviewed mathematical grouping blobs and payload-free source test fixture.',
        'raw_scanner_result_preserved': True,
    }


def review_combined_history_gitleaks(root: Path, report: Path, legacy_review) -> dict | None:
    findings = load_findings(report, allow_duplicates=True)
    if findings is None:
        return None
    reviewed, remainder = [], []
    for match in findings:
        result = review_migration_finding(root, match, candidate=None)
        if result is None:
            remainder.append(match)
        else:
            reviewed.append(result)
    if not reviewed:
        return legacy_review(root, report)
    multiplicities = Counter(finding['Fingerprint'] for finding in reviewed)
    by_fingerprint = {finding['Fingerprint']: finding for finding in reviewed}
    for fingerprint, actual in multiplicities.items():
        expected = history_occurrences(root, by_fingerprint[fingerprint])
        if actual != expected:
            return None
    legacy = None
    if remainder:
        # The raw report stays untouched. The original strict legacy reviewer
        # receives every unmatched finding, so an added secret still fails.
        with tempfile.TemporaryDirectory(prefix='history-review-', dir=report.parent) as folder:
            subset = Path(folder) / 'remaining-findings.json'
            subset.write_text(json.dumps(remainder))
            legacy = legacy_review(root, subset)
        if legacy is None:
            return None
    return {
        'disposition': 'reviewed-false-positive',
        'finding_count': len(findings), 'migration_findings': reviewed,
        'mathematical_findings': [finding for finding in reviewed if finding['RuleID'] == 'generic-api-key'],
        'legacy_finding_review': legacy,
        'reason': 'Exact reviewed migration blobs with parent-diff multiplicities plus the original pinned historical fixture review.',
        'raw_scanner_result_preserved': True,
    }
