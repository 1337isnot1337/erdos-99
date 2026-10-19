import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path('/home/cinna/.local/state/erdos99-merge/20261019')
REPO = Path('/home/cinna/.local/state/erdos99-merge/20261019/review-b')
REV = 'ee8f9df94a8a1043098482386bbbc6a893214330'
ASSIGN = json.loads((ROOT / 'reviews/b-assignment.json').read_text())
REVIEW = json.loads((ROOT / 'reviews/b-review.json').read_text())
REPINS = json.loads((ROOT / 'final-metadata-repins.json').read_text())

def git_bytes(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)

def tree_bytes(rev, path):
    return git_bytes('show', f'{rev}:{path}')

def sha(data):
    return hashlib.sha256(data).hexdigest()

assert git_bytes('rev-parse', REV).decode().strip() == REV
packages = sorted({str(Path(p).parent) for pr in ASSIGN for p in pr['paths'] if p.endswith('/SOURCES.json')})
failures = []
checked = []
for package in packages:
    manifest_path = f'{package}/SOURCES.json'
    try:
        manifest = json.loads(tree_bytes(REV, manifest_path))
    except Exception as e:
        failures.append(f'{manifest_path}: cannot parse at {REV}: {e}')
        continue
    for row in manifest.get('inputs', []):
        path = row.get('path')
        expected = row.get('sha256')
        commit = row.get('commit')
        if not path or not expected:
            failures.append(f'{manifest_path}: incomplete input row: {row!r}')
            continue
        try:
            actual_tree = sha(tree_bytes(REV, path))
        except subprocess.CalledProcessError:
            failures.append(f'{manifest_path}: missing at frozen tree: {path}')
            continue
        if actual_tree != expected:
            failures.append(f'{manifest_path}: frozen-tree sha mismatch {path} expected={expected} actual={actual_tree}')
        actual_commit = None
        if commit:
            try:
                actual_commit = sha(tree_bytes(commit, path))
            except subprocess.CalledProcessError:
                failures.append(f'{manifest_path}: missing at pinned commit {commit}: {path}')
                continue
            if actual_commit != expected:
                failures.append(f'{manifest_path}: pinned-commit sha mismatch {path} commit={commit} expected={expected} actual={actual_commit}')
        checked.append({'package': package, 'path': path, 'commit': commit, 'expected': expected, 'tree_sha': actual_tree, 'commit_sha': actual_commit})

# Independently authenticate every B-assigned row in the final mutable-metadata repin manifest.
assigned_packages = {str(Path(p).parent) for pr in ASSIGN for p in pr['paths'] if p.endswith('/SOURCES.json')}
repin_rows = [r for r in REPINS if r['package'] in assigned_packages]
repin_checks = []
for row in repin_rows:
    old = sha(tree_bytes(row['old_commit'], row['path']))
    new = sha(tree_bytes(row['new_commit'], row['path']))
    package_pin = json.loads(tree_bytes(REV, f"{row['package']}/SOURCES.json"))
    pins = [x for x in package_pin.get('inputs', []) if x.get('path') == row['path']]
    ok = old == row['old_sha256'] and new == row['new_sha256'] and len(pins) == 1 and pins[0].get('commit') == row['new_commit'] and pins[0].get('sha256') == row['new_sha256']
    repin_checks.append({'package': row['package'], 'old_sha_matches': old == row['old_sha256'], 'new_sha_matches': new == row['new_sha256'], 'single_final_pin_matches': ok})
    if not ok:
        failures.append(f"repin row invalid at {row['package']}: {repin_checks[-1]}")

# Persisted B dossier must still identify its exact frozen source-pin evidence and lifecycle state.
assert REVIEW['evidence_complete'] is True
assert REVIEW['metadata_repin_validation_commit'] == '173b3dd14fa784f65f80bb9485b0f72ed1a36916'
assert REVIEW['final_metadata_repin_validation']['commit'] == 'e185b58bfffa27be92d4ec91d919f1aa4f939725'
assert REV in REVIEW['candidate_lifecycle_recheck']['commits']

result = {
    'reviewer': '/root/review_b',
    'integration_commit': REV,
    'integration_tree': git_bytes('rev-parse', f'{REV}^{{tree}}').decode().strip(),
    'packages_checked': len(packages),
    'inputs_checked': len(checked),
    'source_pin_result': 'PASS' if not failures else 'FAIL',
    'repin_packages_checked': len(repin_checks),
    'repin_checks': repin_checks,
    'failures': failures,
    'sample_inputs': checked[:6],
    'command': 'python reviews/b-run-logs/review-b-ee8-source-pins.py',
}
print(json.dumps(result, indent=2))
if failures:
    raise SystemExit(1)
