# Frozen publication candidate: verification and release evidence

The scientific source freeze is reconciled through
`eb51394f371aee958b0d9332f80faf75ae694b9e`, with inherited baseline
`5dcbdc3dfa1f9be370602cc54d50e68eabb88f56`. Publication state
`2026-10-15.publication.2` withdraws one unsupported canonical inference without
promoting its proposed repair. The corpus has 451 claim IDs, 845 edges, 94
registered certificates, 810 source records and 20 task cards. Level I/A/B/C-II
remain open; C-I is closed in its stated scope.

## Final receipt contract

The immutable candidate is identified by the **detached release manifest and
verification receipt** delivered alongside it. Keeping the receipt outside the
Git tree avoids a self-referential commit hash. Each receipt records the candidate
commit/tree, actual Python/package versions, exact commands, exit codes, timings,
full logs and a check that the checkout stayed unchanged. The same gate is run on
the integrated staging commit and the separate clean-root candidate.

```sh
python3 -m venv /private/e99-verification-venv
/private/e99-verification-venv/bin/python -m pip install --require-hashes --only-binary=:all: -r tools/requirements-verification-linux-x86_64.lock
/private/e99-verification-venv/bin/python tools/verify_publication_candidate.py \
  --output /private/new-e99-final-receipt \
  --gitleaks /path/to/gitleaks --actionlint /path/to/actionlint
```

This gate runs public integrity, standalone retained-byte provenance, theorem
state/generated views, all tool regressions, adversarial corpus tests, the complete
registered certificate suite, full publication content/history audit, Gitleaks
on tree and history, workflow lint and clean-state checks. Local release engineers
may additionally pass `--source-repo /private/source-clone`; public users never
need that clone. This optional audit checks all 4,793 versioned source records.

`executable_checks_passed` and `automated_release_precheck_passed` are distinct.
The release scanner returns one while factual rights/history questions are open.
The receipt never grants permissions: `release_cleared` remains false. Do not
weaken a check to turn the owner's HOLD into a green automated result.

## Targeted evidence executed during closure

- A fresh external CPython 3.14.7 environment installed all Linux x86_64 wheels
  from the hash lock successfully; `pip check` found no broken requirements.
- The source auditor checked all 810 retained public hashes and 4,793 versioned
  source records, including mode/blob identities and later exclusion versions,
  with zero errors. Its five corruption/path/mode regression tests passed.
- Full tooling tests passed after integration; the final receipt supplies their
  exact count after the last safety/prerequisite regression was added.
- Independent public-only replays include A's 17,104 tube/shield cases, B's exact
  phase-cut models including all 4,096 balanced graphs, and C's full-source
  paired-cap, moved-core, common-angle, actual-diameter escape, quarter-fold and
  capacity regressions. These have the finite and nonglobal scopes in their
  scripts and linked proofs. The complete 94-suite final result belongs to the
  detached immutable-candidate receipt, not a historical timing copied here.
- Gitleaks 8.30.1 and actionlint 1.7.7 are used for final scans/lint. Tree and
  all-ref history outputs are redacted; private author identity mappings remain
  outside the repository. A zero-finding scan is not rights clearance.

The [certificate registry](../../research/certificates.json) states each encoded
proposition, arithmetic, inputs and limitations. Earlier
[replay outputs](../../research/replay-results.json) retain their historical
candidate scope; they are not a substitute for the final run.

## Remaining decisions

The [publication audit](PUBLICATION_AUDIT.md) and
[rights review](../publication/rights-review.md) identify the remaining factual
rights grant and clean-remote migration choices. All included source rights remain
pending. The existing staging repository retains historical metadata and must
stay private; the clean-root artifact contains the same final tree with no old
commit objects and no remote. No visibility change is authorized by this receipt.

Hosted execution remains unverified because the account restriction prevented
jobs from starting. Both protective rollout gates remain unset. No paid usage or
spending limit was changed. Anonymous public cloning can be confirmed only after
an explicit final visibility decision.
