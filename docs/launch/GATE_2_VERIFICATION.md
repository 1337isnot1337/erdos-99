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
available in the publication corpus.

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

The unchanged Gitleaks history scan detects one reviewed synthetic fixture:

- Commit: `08784c2440aa2f6f4252adc30f7ce33cd59cf976`.
- File/range: `tools/test_local_ci.py`, lines 386–390.
- Rule: `private-key`.
- Git blob: `5cab1430e37d5255bd3fe5e7e58937e1c14a0518`.
- Complete blob SHA256:
  `509b6ed834755b0ae83cd48bcef34cc6a5016d5e375d24f64e92eb4f3f856f92`.

Independent inspection of that exact Git object finds two PEM opening delimiters
inside negative-test string literals, with no closing delimiter or encoded key
payload. The current fixture was already repaired to construct its test strings.
Rewriting the owner's retained Git history is unnecessary for this false positive.

The receipt retains the raw scanner **exit 1**, JSON finding and complete log.
The verifier records a separate `finding_review` and `verification_passed` result
only when the report contains exactly this one finding, with the exact pinned
commit/path/rule/range/fingerprint, and the complete historical blob SHA256
matches. It reads committed Git bytes with replacement objects disabled.
There is no scanner suppression or general path/rule exclusion. An additional
finding, changed identity, missing/malformed report, unavailable/different Git
object, or scanner invocation error remains a failure. The raw exit code is
never changed to zero. Receipt consumers must distinguish reviewed findings
from a zero-finding scanner result.

Real-Git regressions exercise exact review, additional and changed findings,
malformed/missing reports, a mismatching blob hash, missing objects and uncommitted
worktree substitutions. Existing tests continue to check hidden index changes,
symlinks and all executable bits.

## Separate publication decisions

The release auditor checks the original exact-manifest owner attestation and
the narrowly authorized Git email. Source-rights reconciliation remains Gate 1;
visibility authorization and eventual anonymous access remain Gate 3. A scan
does not establish legal ownership or clearance of independently owned prose.

The schema's existing source-repository URL is a local schema identifier, not a
credential or a runtime network/private-archive dependency. Scanner regex
literals and their historical versions are also reviewed reference warnings.
PR #16 proposes optional removal of that identifier; changing its imported-file
hash also changes the exact inclusion-manifest blob and requires separate
attestation reconciliation before that PR can be release-ready. It is not part
of this frozen candidate, and its claimed checks do not verify this release.

The maintenance cleanup workflow uses `pull_request_target` solely for trusted
inline API operations, without checking out or executing PR code. Its offline
regressions execute the actual embedded code and check pagination and preserved
branches. Hosted execution remains unverified while account restrictions prevent
jobs from starting. Keep `E99_PUBLIC_CI` and `E99_PUBLIC_PACKAGE_REPLAY` unset;
skipped jobs and zero-step failures are never test passes.
