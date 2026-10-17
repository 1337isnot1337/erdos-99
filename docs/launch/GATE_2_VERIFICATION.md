# Gate 2: exact-commit release verification

The detached receipt, produced **after the last merge**, identifies the evaluated
commit and tree. A prior receipt never verifies a later commit, including a
documentation-only merge. Gate 2 does not authorize publication, confer rights,
or promote mathematical claims. Retain the existing repository URL and history.

## Reproduction

Clone the repository with its history and detach at the commit named in the
release report. Use CPython **3.14.7**, Linux x86_64, and an external environment:

```sh
python3.14 -m venv /private/e99-verification-venv
/private/e99-verification-venv/bin/python -m pip install \
  --require-hashes --only-binary=:all: \
  -r tools/requirements-verification-linux-x86_64.lock
/private/e99-verification-venv/bin/python -c \
  'import ctypes, ssl, numpy, scipy, sympy, yaml, jsonschema'
/private/e99-verification-venv/bin/python tools/verify_publication_candidate.py \
  --output /private/new-e99-release-receipt \
  --gitleaks /path/to/gitleaks --actionlint /path/to/actionlint
```

Use Gitleaks **8.30.1** and actionlint **1.7.7**, validating downloaded archives
against their upstream checksum files. Install native development prerequisites
before compiling Python: in particular, missing libffi headers can produce a
Python build without `_ctypes`, which prevents SymPy/NumPy certificate imports.
That is an environment failure, never a passing or skipped certificate.

The optional `--source-repo /private/source-clone` additionally verifies 4,793
versioned source records. Ordinary public reproduction needs no private source
archive. Source/public hashes and all 94 registered certificate commands are
available in the publication corpus. The full auditor runs the destination-only
`tools/verify_frozen_target_c_813_migration.py` check against the frozen report
index, disposition ledger, support-file list and additive rights records. A
source-backed replay of the 813 reports and 21 supporting files is available
with the same `--source-repo` argument documented in `READINESS.md`.

For a scan including GitHub PR heads as well as clone-visible branches, fetch
them before running the same verifier:

```sh
git fetch origin '+refs/pull/*/head:refs/audit/pull/*/head'
git ls-remote origin > /private/advertised-refs.txt
```

Also replay the public A/B/C commands directly from a separate fresh clone:

```sh
python research/tube_shield_cut_audit.py
python research/phase_cut_certificate.py
python research/verify_target_c_paired_cap_spoke_comparison_2026_10_06.py
python research/verify_target_c_common_angle_train_endpoint_2026_10_06.py
python research/verify_target_c_capped_wall_actual_diameter_escape_2026_10_06.py
python research/verify_target_c_face_coupled_quarter_folds_2026_10_07.py
python research/verify_target_c_collective_wall_capacity_audit_2026_10_06.py
```

These are scoped finite/algebraic or numerical checks as stated in their scripts;
they do not establish global optimality, the analytic proofs, or Level I.

## Historical Gitleaks finding and receipt semantics

The Gitleaks history scan uses `--all --full-history -m`, including merge
resolution diffs. Ordinary Git patch logs omit merge diffs and can miss content
introduced only in a merge and deleted later. The full scan detects two pinned
occurrences of one reviewed synthetic fixture:

- Commit: `08784c2440aa2f6f4252adc30f7ce33cd59cf976`.
- Merge retaining the identical blob: `75fad69da5002e28d0ccc770841cd264ad1ba6cb`.
- File/range: `tools/test_local_ci.py`, lines 386–390.
- Rule: `private-key`.
- Git blob: `5cab1430e37d5255bd3fe5e7e58937e1c14a0518`.
- Complete blob SHA256:
  `509b6ed834755b0ae83cd48bcef34cc6a5016d5e375d24f64e92eb4f3f856f92`.

Independent inspection of that exact Git object finds two PEM opening delimiters
inside negative-test string literals, with no closing delimiter or encoded key
payload. The current fixture was already repaired to construct its test strings.
Rewriting the owner's retained Git history is unnecessary for this false positive.

The receipt retains the raw scanner **exit 1**, JSON findings and complete log.
The verifier records a separate `finding_review` and `verification_passed` result
only when every finding matches one of these two pinned occurrences, with the
exact commit/path/rule/range/fingerprint and complete historical blob SHA256.
Duplicate reports of one occurrence are rejected. It reads committed Git bytes
with replacement objects disabled.
There is no scanner suppression or general path/rule exclusion. An unreviewed
finding, changed identity, missing/malformed report, unavailable/different Git
object, or scanner invocation error remains a failure. The raw exit code is
never changed to zero. Receipt consumers must distinguish reviewed findings
from a zero-finding scanner result.

Real-Git regressions exercise exact review, additional and changed findings,
malformed/missing reports, a mismatching blob hash, missing objects and uncommitted
worktree substitutions. Existing tests continue to check hidden index changes,
symlinks and all executable bits. Additional real-Git controls demonstrate that
the scan includes deleted merge-only content and reject a pinned alias whose
committed bytes differ from the reviewed blob.

## Separate publication decisions

The release auditor checks the original exact-manifest owner attestation, the
prior-to-current manifest reconciliation, and the additive 834-path first-party
migration authorization. Ordinary Git author, committer, tagger, and contributor
trailer metadata is preserved regardless of email domain and is not a release
blocker by itself. The previously flagged 14 OpenAI Codex author/committer
occurrences are ordinary attribution, not evidence of a leaked credential or
of independently owned copyrighted expression. Full Git-object credential and
restricted-content scans remain mandatory. Source-rights reconciliation is Gate 1;
visibility authorization and eventual anonymous access remain Gate 3. A scan does
not establish legal ownership or clearance of independently owned prose.

PR #16 merged on 2026-10-16. The schema now uses
`urn:erdos-99:theorem-state.schema`; the imported-file hash and exact-manifest
attestation reconciliation are recorded in Gate 1. Historical schema URLs and
scanner regex literals remain reviewed reference warnings. Each final release
receipt verifies the resulting commit, including this repair.

## Publication candidate 0.1.0-rc.3

The release gate also runs the documented task selector and verifies every page
of the [GitHub reading edition](../../reading/README.md). Reading pages are
generated presentation views: the exact proof sources, source hashes, historical
archives, and mathematical lifecycles remain authoritative. A gate pass must name
the final commit/tree after all publication edits. The private draft release
carries its detached receipts and checksums; a draft does not change visibility.

The maintenance cleanup workflow uses `pull_request_target` solely for trusted
inline API operations, without checking out or executing PR code. Its offline
regressions execute the actual embedded code and check pagination and preserved
branches. Hosted execution remains unverified while account restrictions prevent
jobs from starting. Keep `E99_PUBLIC_CI` and `E99_PUBLIC_PACKAGE_REPLAY` unset;
skipped jobs and zero-step failures are never test passes.
