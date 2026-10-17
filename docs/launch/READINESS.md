# Current publication candidate

Candidate **0.1.0-rc.3** has **23 current task cards**. The
[current release summary](RELEASE_CANDIDATE.md) controls present publication
status and points to the final-commit evidence. The narrative below is preserved
history: its earlier task counts and uses of “current” refer to those snapshots.
PR #16 has merged; the schema uses `urn:erdos-99:theorem-state.schema`.
The repository remains private pending the separate visibility decision.

# Migration completion scope

The [current integration status](../research/migration/2026-10-16/integration/STATUS.md)
accounts for all 4,717 pinned source-main paths: 4,654 exact source identities
and 63 external-reference exclusions. All 813 frozen report bindings, 1,643
captured branch-artifact rows, and 30 known captured dirty-file identities are
preserved. The [five-version local recovery](../research/migration/2026-10-16/ref-reconciliation/LOCAL_RECOVERY.md)
retains exact historical bytes separately from active documents.

Two historical working-copy states remain unknown at migration capture;
earlier clean backup observations are bounded evidence. After the exact final
main verification passes, `1337isnot1337/erdos-99` is the home for future work
and the source receives a reversible deprecation pointer. The private source
repository, history, PRs, branches, working copies and reference collection
remain intact. The two unknown states remain explicit; no exhaustive historical
preservation or source deletion is claimed. Neither repository is made public.
Exact current Gate 2 results belong in detached receipts naming the
tested SHA/tree, as required by [migration verification](MIGRATION_VERIFICATION.md)
and the handoff on [PR #75](https://github.com/1337isnot1337/erdos-99/pull/75).
Historical results below do not establish a current-commit pass. The complete
historical readiness narrative follows unchanged.

# Frozen publication candidate: verification and release evidence

## Expanded Target C migration and exact-commit receipt

The five-shard migration adds 813 frozen source-main Target C reports and four
newly imported cross-shard support files beyond the older publication candidate.
Its additive rights record accounts for those reports and 21 total support
files. The full path-level scientific and rights reconciliation is in
[the migration report](../research/migration/2026-10-16/scientific-reconciliation.md).
The earlier Gate 2 receipt does not cover this expanded tree. Run the full
[Gate 2 procedure](GATE_2_VERIFICATION.md) against the exact final destination
`main` commit and retain its detached receipt; do not infer a current PASS from
any receipt naming an earlier SHA. Keep the separate visibility decision and
private repository setting unchanged.


The scientific source freeze is reconciled through
`eb51394f371aee958b0d9332f80faf75ae694b9e`, with inherited baseline
`5dcbdc3dfa1f9be370602cc54d50e68eabb88f56`. Publication state
`2026-10-15.publication.2` withdraws one unsupported canonical inference without
promoting its proposed repair. The corpus has 451 claim IDs, 845 edges, 94
registered certificates, 810 source records and 20 task cards. Level I/A/B/C-II
remain open; C-I is closed in its stated scope.

Those counts describe the frozen 2026-10-15 publication candidate. The expanded
migration tree has 23 task cards according to the current public-integrity check.
Rebuild the final publication receipt against the final migration commit before
any Gate 2 claim.

## Final receipt contract

See [Gate 2 reproduction and scanner review](GATE_2_VERIFICATION.md) for the
exact environment, public A/B/C routes and retained raw historical fixture
finding. A reviewed false positive is distinct from a zero-finding scan.

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
The full publication auditor also runs the destination-only frozen Target C
integrity verifier. The source-backed form independently checks all 813 frozen
source blobs and 21 support-file blobs and replays recorded transformations:

```sh
python tools/verify_frozen_target_c_813_migration.py --destination .
python tools/verify_frozen_target_c_813_migration.py \
  --source-repo /private/source-clone --destination .
```

`executable_checks_passed` and `automated_release_precheck_passed` are distinct.
The current rights records reconcile the previous 810-entry manifest and the
additive 834-path migration. Under the owner-directed Git-attribution policy,
ordinary author, committer, tagger and contributor-trailer email metadata is
preserved and does not by itself block release. The earlier 14 non-noreply
Codex occurrences are attribution, not a credential finding. All credential,
restricted-content, and substantive source-rights checks remain enforced.
A previous Gate 2 receipt blocked by the old email rule is historical;
rerun the complete release precheck on the actual final commit.

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

The [updated publication audit](PUBLICATION_AUDIT.md) and
[current rights review](../publication/rights-review.md) record the owner's
authorization for the 810-entry manifest and the separate 834-path Target C
migration. The original exact-manifest check now verifies the prior-to-current
entry reconciliation; the additive rights check validates every frozen report
and support path. The owner wishes to preserve original contributor attribution and PR history;
ordinary Git email metadata requires no separate release clearance. The owner
has separately consented to the publication of their own email, but this is
historical context, not a per-address allowlist or a grant of third-party
content rights. Gate 2 must run on the exact final commit, and no visibility
change is authorized here.

Hosted execution remains unverified because the account restriction prevented
jobs from starting. Both protective rollout gates remain unset. No paid usage or
spending limit was changed. Anonymous public cloning can be confirmed only after
an explicit final visibility decision.
