# Hosted CI release review

The publication workflow remains disabled by default. `E99_PUBLIC_CI` and
`E99_PUBLIC_PACKAGE_REPLAY` were both unset when inspected on 2026-10-15.
Recent destination runs contained skipped plan/replay jobs with no executed
steps. These are **unverified**, not passing verification. The destination had
no branch protection or ruleset requiring those skipped checks at inspection.
Do not configure a skipped check as evidence that the corpus was verified.

## Reviewed boundaries and repairs

- The only trigger is ordinary `pull_request`; no `pull_request_target`, push,
  schedule, dispatch, dynamic matrix, or automatic full certificate replay is
  enabled. Workflow permissions are `contents: read`.
- Actions use exact commit pins. Both checkouts set `persist-credentials: false`.
  Control scripts and dependency locks come from the trusted base SHA. The fork
  head is checked out separately, with base ancestry fetched explicitly.
- Dependency installation uses a trusted hash lock, binary wheels only, and a
  fixed Python version. Tier 0 uses trusted parsers rather than importing the
  candidate's Python modules. A new preflight rejects every nonregular or
  escaping committed path before any theorem metadata parser reads it. Two
  regressions cover a symlinked manifest and an unchanged symlink.
- The planner unions merge-base, head, and current-base dependencies. Unknown
  impact requires full verification or review; it is not silently accepted as
  a targeted pass. A needed replay with its gate off exits unsuccessfully.
- Replay is serial, with at most two selected packages and 240 declared seconds.
  Job limits are three minutes for planning and six for replay. Bubblewrap
  requires separate namespaces, no network, cleared environment, read-only
  source/runtime mounts, and no inherited credentials. There is no unisolated
  fallback. Commands use argument vectors, with wall/CPU, address-space,
  output-file, core-dump, and descriptor limits.
- The replay limits are not an aggregate cgroup process/memory budget. Local
  fixture passes do not certify arbitrary hostile fork execution on hosted
  runner images. Process containment, namespace availability and fork behavior
  must be exercised before enabling that gate.
- Per-PR cancellation limits duplicate work for one PR, not the total number of
  concurrent PRs. Gates therefore remain protective account-wide cost controls.

## Hosted evidence and limitation

The inspected source run `38822653478` failed with zero executed steps. Its
check annotation reports that recent payments failed or a spending limit must
be increased. This is unavailable hosted infrastructure, not a code failure.
No billing/spending setting, paid runner, or rollout variable was changed.
The public-fork approval endpoint cannot validate future public behavior while
the destination is private; it returned the documented private-repository
validation error at inspection.

No successful hosted canary is claimed. Enabling ordinary PR execution cannot
resolve the current account restriction without an owner billing decision;
this session retains both gates. Publication can accurately offer local
verification while hosted execution remains explicitly disabled. Hosted rollout
is separate from source rights, clean-history migration, and visibility approval.

## Local final-candidate gate

Use an external locked environment and a new external receipt directory:

```sh
python tools/verify_publication_candidate.py --output /private/new-e99-receipt \
  --gitleaks /path/to/gitleaks --actionlint /path/to/actionlint
```

This replays the complete certificate registry, corpus/tool tests, theorem state,
public integrity, full release audit, tree/history secret scans and workflow lint.
The detached receipt records the immutable candidate SHA/tree, environment,
commands, exit codes, timing and logs, and checks that the candidate stayed clean.
Before and after execution it checks every tracked raw blob and executable mode
against the pinned Git tree, independently of index stat/filter heuristics, and
rejects assume-unchanged/skip-worktree flags and nonregular paths. Python children
use a fresh external bytecode cache with inherited path/home/startup overrides
removed. This remains trusted local execution, not a hostile-code sandbox or a
claim of a hermetic environment.
Rights/history blockers are reported separately from executable check failures.
An exit code of one with a passing executable suite and pending rights is an
expected release **HOLD**, not grounds to weaken the audit. The tool never grants
permissions or declares the repository cleared for publication.
