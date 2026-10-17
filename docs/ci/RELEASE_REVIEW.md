# Hosted CI release review

Normal local contribution uses the platform-neutral dependency version lock and
Python commands in [the CI guide](README.md#normal-local-verification). The Linux
runner and bubblewrap details below describe hosted CI and optional isolated
package replay.

The structural integrity and planning job now runs automatically on non-draft
PRs. `E99_PUBLIC_PACKAGE_REPLAY` still controls optional isolated package
execution. A passing plan is structural evidence; its summary preserves pending
targeted replay and full-verification requirements.

Historical inspection on 2026-10-15 found both rollout variables unset and
plan/replay jobs skipped without executed steps. Those runs remain unverified.
No branch protection or ruleset required them at that inspection. The current
workflow change does not turn those historical skips into verification evidence.

## Reviewed boundaries and repairs

- The research workflow's only trigger is ordinary `pull_request`; no `pull_request_target`, push,
  schedule, dispatch, dynamic matrix, or automatic full certificate replay is
  enabled. Workflow permissions are `contents: read`.
- The separate branch-maintenance workflow uses `pull_request_target: closed`,
  a workflow-path-only main push and manual dispatch. Its trusted inline code
  performs GitHub API operations with `contents: write`; it has no checkout or
  execution of PR code. It snapshots paginated branches before deletion and
  preserves protected/default/open-PR/advanced/unassociated branches. Offline
  tests of its actual embedded code are distinct from hosted execution evidence.
- Actions use exact commit pins. Both checkouts set `persist-credentials: false`.
  Control scripts and dependency locks come from the trusted base SHA. The fork
  head is checked out separately, with base ancestry fetched explicitly.
- Hosted dependency installation uses the trusted Linux x86_64 hash lock,
  binary wheels only, and a fixed Python version. Tier 0 uses trusted parsers rather than importing the
  candidate's Python modules. A new preflight rejects every nonregular or
  escaping committed path before any theorem metadata parser reads it. Two
  regressions cover a symlinked manifest and an unchanged symlink.
- The planner unions merge-base, head, and current-base dependencies. Unknown
  impact requires full verification or review; it is not silently accepted as
  a targeted pass. A needed replay with its switch off remains explicitly pending.
- Automatic workload limits affect scheduling only. An over-budget targeted set
  retains its complete package list and scientific classification; no package is
  omitted to fit the automatic job. Complete required replay remains the merging agent's duty.
- The optional Linux package replay is serial, with at most two selected packages and 240 declared seconds.
  Each hosted job is limited to six minutes. The complete Tier 0 corpus check
  has a separate 120-second process limit, leaving job time for trusted control
  tests, checkout and installation. These limits do not change the package replay
  budget. Bubblewrap
  requires separate namespaces, no network, cleared environment, read-only
  source/runtime mounts, and no inherited credentials. Hosted jobs install
  Bubblewrap when missing. There is no unisolated
  fallback. Commands use argument vectors, with wall/CPU, address-space,
  output-file, core-dump, and descriptor limits.
- The replay limits are not an aggregate cgroup process/memory budget. Local
  fixture passes do not certify arbitrary hostile fork execution on hosted
  runner images. Process containment, namespace availability and fork behavior
  must be exercised before enabling that gate.
- Per-PR cancellation limits duplicate work for one PR, not the total number of
  concurrent PRs. Package execution remains opt-in and bounded separately.

## Hosted evidence and limitation

The historically inspected source run `38822653478` failed with zero executed steps. Its
check annotation reports that recent payments failed or a spending limit must
be increased. This is unavailable hosted infrastructure, not a code failure.
No billing/spending setting, paid runner, or rollout variable was changed.
The public-fork approval endpoint cannot validate future public behavior while
the destination is private; it returned the documented private-repository
validation error at inspection.

No successful hosted canary is established by this configuration change. Enabling
ordinary PR checks cannot resolve account restrictions or change spending
limits. Record the actual run ID and source SHA to establish current hosted
execution; keep any failed allocation or unavailable sandbox distinct from a
scientific verification result.

## Local release verification

Use an external virtual environment with
`tools/requirements-verification.lock`. Choose a new receipt directory outside
the checkout for each run. From the repository root:

```text
python tools/verify_publication_candidate.py --output ../e99-check-receipt
```

The runner replays the certificate registry, corpus/tool tests, theorem state,
public integrity and the release audit. It also runs Gitleaks and actionlint when
their executables are available. A standard run records unavailable external
tools as skipped.

For a release review that requires tree/history secret scans and workflow lint,
install Gitleaks and actionlint for your platform, then run:

```text
python tools/verify_publication_candidate.py --output ../e99-release-receipt --require-release-tools
```

The runner finds the tools on `PATH`. Use `--gitleaks PATH` and `--actionlint PATH`
to select executables explicitly. `--require-release-tools` requires both tools
to run and pass. The receipt's `automated_release_precheck_passed` field is true
only when the required checks and both release tools pass.

The detached receipt records the candidate SHA/tree, operating system, machine,
Python environment, commands, exit codes, timing, logs and skipped scope. It
checks that the candidate stayed clean. Before and after execution it checks
every tracked raw blob against the Git tree, independently of index stat/filter
heuristics, and rejects assume-unchanged/skip-worktree flags and nonregular paths.
POSIX hosts also compare executable-mode bits. Windows records that comparison
as inapplicable. Preserve the committed file
bytes, including line endings, when preparing an exact release checkout.
Python children
use a fresh external bytecode cache with inherited path/home/startup overrides
removed. This remains trusted local execution, not a hostile-code sandbox or a
claim of a hermetic environment.

The receipt also records availability of the optional Linux isolation backend.
Unavailable isolation and skipped tests remain visible. A receipt establishes
only the checks completed in its recorded environment; native Windows and macOS
end-to-end verification has not yet been recorded.

Migration checks and source-rights manifest reconciliation have been removed.
The scanner still reports actual credential and restricted-content findings.
Run this complete suite for a release of changed research or verification
tooling; routine prose edits receive structural and relevant behavior checks.
A receipt records a completed run and does not freeze future repository edits.
