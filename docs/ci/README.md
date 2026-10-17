# Localized verification

## Normal local verification

The normal contribution workflow uses Python and Git. In an activated Python
3.14 virtual environment, run these commands from the repository root:

```text
python -m pip install -r tools/requirements-verification.lock
python tools/check_public.py
```

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for environment setup on your
platform. The version lock is the normal install route for Linux, macOS and
Windows. The `*-linux-x86_64.lock` files record a specific Linux wheel set for
hosted CI and reproducing that environment. Use those hash locks when you want
that specific environment.

The recorded environment is Linux x86_64. Native Windows and macOS verification
has not yet been recorded. A local result applies to the platform, dependencies
and checks that actually ran.

## Verification ownership

The optional [package scaffold and metadata helper](../research/research-package-guide.md)
use the existing protocol without running submitted commands. The
[maintainer intake ledger](../research/pr-intake.md) records exact-head scope and
deferred obligations; it never overrides this verification policy or grants a
merge. Source archival classification must be established by review, not a label
that suppresses unresolved full-verification impact.

**The contributing agent owns evidence reproduction and focused checks.** Run
`python tools/check_public.py`, `git diff --check`, tests for changed behavior,
and the new or changed verifiers or experiments needed to support the result.
Use `python tools/local_ci.py --base-ref origin/main` to report verification
scope. Leave the repository-wide theorem certificate suite to the merging
agent, including after rebases. A contributor need not clear
`full-verification-required` before opening a PR.
Record the suite as **deferred to the merging agent**, together with the
planner's classification, focused results and unresolved scope. Planner errors
must be fixed or disclosed; deferring replay does not turn an error into a pass.

**The merging agent owns required full replay.** Resolve verification scope on
the final integration candidate containing the PR and current main. Canonical,
shared-foundation and unresolved `full-verification-required` impact requires
the full suite before merge:

```text
python tools/run_theorem_certificates.py
python tools/check_public.py
```

Record the candidate commit and tree, PR head, base commit, environment, exact
commands, exit status and results in the PR or merge-review record. Merge the
tested tree. If mathematical inputs, verification code, dependencies or the
verification environment change after a pass, repeat the affected checks on
the new candidate. Contributors need not duplicate this full replay.

Workflow-only changes retain their structural-check exemption. An impact
review may establish that scope, but declared mathematical inputs always take
priority over a workflow path or filename. A pending full replay is never a
full-verification pass. The independent AI-agent proof and adversarial audit
required for consequential canonical promotion remains a separate obligation.

## Verification levels

Tier 0 runs trusted metadata, theorem/task/generated-view consistency, public links, changed-file security and package planning. `python tools/check_public.py` checks the current corpus; it proves no mathematical theorem. Migration checks and import-manifest pinning have been removed.

Workflow and navigation documentation receives structural checks. Current theorem and certificate dependencies take priority over that classification: a document used as a mathematical input still receives the relevant verification. Ordinary README edits require no import receipt or full certificate replay.

Tier 1 is an optional isolated package replay. It replays the complete affected
package set, including transitive dependents, with at most two packages,
120 declared seconds per package and 240 declared seconds in one serial job.
A larger complete set remains `targeted-replay`, with
`replay_schedule: deferred-budget` and `replay_allowed: false`. Its `packages`
list and declared workload remain complete; the budget never drops packages or
changes the required scientific verification level. The merging agent arranges
the complete deferred replay. Timeout-only edits change scheduling, while changed
inputs, commands, domains and environments still require impact review.
The planner unions merge-base, head and current-base
inputs. This backend requires Linux and bubblewrap. It uses separate namespaces,
no network or inherited credentials, read-only declared Git blobs, argument-vector
commands, and time and resource limits. Unavailable isolation produces an explicit
refusal; it never falls back to unisolated execution. No dynamic matrix is used.
See `tools/local_ci.py` and `tools/localized_ci/`.

`local_ci.py --integrity` also uses this isolated backend. Normal local corpus
checks use `python tools/check_public.py` directly. Contributors can use the
ordinary checks without installing the Linux replay backend.

Tier 2 is explicit and owned by the merging agent: `python tools/run_theorem_certificates.py`, followed by `python tools/check_public.py` and appropriate tooling tests. Canonical, shared-foundation, removed-input, changed verifier-domain and unknown impacts report `full-verification-required`; contributors hand off that requirement rather than running the full suite for submission. This is not a full pass. Do not silently replace it with targeted success.

## Hosted CI

Non-draft PRs automatically run the structural integrity and planning job. It
uses a trusted base control checkout and read-only permissions; contributed
code is never run with `pull_request_target`. Actions are commit-pinned and
checkout credentials are not persisted. The job installs Bubblewrap when it is
missing and refuses execution if its required isolation is unavailable.

A successful planning job establishes structural integrity only. Its summary
reports full verification requirements and deferred targeted work. Actual package
execution is a separate job, enabled only by
`E99_PUBLIC_PACKAGE_REPLAY == 'true'` and a plan that fits the automatic budget.
When execution is disabled or over budget, the complete replay remains pending;
planning success is not a replay pass. No full certificate suite runs on every
PR. Per-PR cancellation is not a repository-wide queue limit. The workflow does
not alter billing or spending limits. Hosted execution is unverified until actual
jobs execute; local measurements exclude hosted queue/setup/install time.

Hosted jobs choose Linux runners and their matching hash lock. That deployment
choice does not define the contributor's operating system. See
[RELEASE_REVIEW.md](RELEASE_REVIEW.md) for the recorded hosted status and local
release receipt commands.

A package uses `TASK.json`, `SOURCES.json`, `VERIFY.json` and README with exact inputs, provenance, unresolved closure and bounded commands. Existing registered historical certificates need not be retrofitted into misleading package declarations. New packages must state exact mathematical scope and limitations.

The former `E99_PUBLIC_CI` switch is no longer required for Tier 0. Public-fork
ancestry handling and undeclared package-shadowing checks remain in the trusted
control path. Enabling the workflow does not establish a successful hosted fork
canary; record the actual run and source SHA when one executes.
