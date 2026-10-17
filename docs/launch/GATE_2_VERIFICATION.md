# Release verification

Use this procedure to check a release candidate's current code and research.
Migration checks and source-import replay have been removed.

For ordinary documentation or workflow edits, run structural checks and tests
for the changed behavior. Run relevant certificates when their mathematical
inputs change. A full release replay is available for a new release of the
research or verification tooling; it is not a requirement after every README edit.

## Full release run

The runner has no general operating-system restriction. Use Python 3.14 and
the platform-neutral dependency lock, as shown in `README.md`. Install Gitleaks
**8.30.1** and actionlint **1.7.7** for a full release precheck. Their executables
can be on `PATH` or supplied with `--gitleaks` and `--actionlint`.

On macOS or Linux:

```sh
python3 -m venv ../e99-verification-venv
../e99-verification-venv/bin/python -m pip install -r tools/requirements-verification.lock
../e99-verification-venv/bin/python tools/verify_publication_candidate.py \
  --output ../new-e99-release-receipt --require-release-tools
```

On Windows PowerShell:

```powershell
py -3.14 -m venv ../e99-verification-venv
..\e99-verification-venv\Scripts\python.exe -m pip install -r tools/requirements-verification.lock
..\e99-verification-venv\Scripts\python.exe tools/verify_publication_candidate.py --output ../new-e99-release-receipt --require-release-tools
```

The output directory must be new and outside the checkout. Without
`--require-release-tools`, the runner can run the standard code and research
checks when external release tools are unavailable. Its receipt identifies
skipped tools; that result is not a full automated release precheck.

The runner executes current
theorem-state, task, reading-edition and public-integrity checks, tooling and
corpus tests, registered certificates, credential scans, and workflow lint.
Use the dependency lock shipped with the code. Missing runtime dependencies
are an environment failure, not a passing certificate.

The optional isolated package replay tests need Linux, Bubblewrap, supported
namespaces and their declared Python 3.14 runtime. They report explicit skips
when those capabilities are unavailable. Ordinary checks do not need that
backend. The Linux x86_64 wheel lock remains an option for Linux CI.

The output records the tested commit and tree, commands, environment, results
and logs. The checkout must stay unchanged during the run so those results
describe what executed. Later commits remain ordinary Git changes; they do not
require rewriting an earlier receipt or the old migration records. Record
additional verification according to what changed.

## Credential scanning

Both current files and reachable Git history are scanned. To include GitHub PR
heads beyond the refs in the clone, fetch them before the run:

```sh
git fetch origin '+refs/pull/*/head:refs/audit/pull/*/head'
```

The history scan includes merge diffs. Raw scanner results remain in the output.
The reviewer in `tools/review_scanner_findings.py` recognizes specific previously
inspected false positives only when a scanner actually reports them. Other
findings and scanner errors fail verification. This is credential review, not a
migration-completeness check.

Ordinary Git author, committer, tagger and contributor attribution is allowed.
The project's recorded owner authorization and license remain in force without
per-file migration attestation or hash-refresh requirements.

## What a passing run establishes

A run reports the checks it executed. Finite or numerical certificate results
retain their stated scope; they do not prove Level I or promote theorem claims.

Hosted jobs remain disabled or unverified until they actually execute. Skipped
jobs and startup failures are not passes. Local verification is supported.
Repository visibility is a separate owner decision.
