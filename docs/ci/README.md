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

## Verification levels

Tier 0 runs trusted metadata, theorem/task/generated-view consistency, public links, changed-file security and package planning. `python tools/check_public.py` checks the current corpus; it proves no mathematical theorem. Migration checks and import-manifest pinning have been removed.

Workflow and navigation documentation receives structural checks. Current theorem and certificate dependencies take priority over that classification: a document used as a mathematical input still receives the relevant verification. Ordinary README edits require no import receipt or full certificate replay.

Tier 1 is an optional isolated package replay. It replays declared affected
packages and their dependency closure, with at most two packages and 240 declared
seconds in one serial job. The planner unions merge-base, head and current-base
inputs. This backend requires Linux and bubblewrap. It uses separate namespaces,
no network or inherited credentials, read-only declared Git blobs, argument-vector
commands, and time and resource limits. Unavailable isolation produces an explicit
refusal; it never falls back to unisolated execution. No dynamic matrix is used.
See `tools/local_ci.py` and `tools/localized_ci/`.

`local_ci.py --integrity` also uses this isolated backend. Normal local corpus
checks use `python tools/check_public.py` directly. Contributors can use the
ordinary checks without installing the Linux replay backend.

Tier 2 is explicit: `python tools/run_theorem_certificates.py`, followed by `python tools/check_public.py` and appropriate tooling tests. Canonical, shared-foundation, removed-input, changed verifier-domain and unknown impacts report `full-verification-required`; this is not a full pass. Do not silently replace it with targeted success.

## Hosted CI

Ordinary PRs use a trusted base control checkout and read-only permissions; contributed code is never run with `pull_request_target`. Actions are commit-pinned and checkout credentials are not persisted. No full certificate suite runs on every PR. Per-PR cancellation is not a repository-wide queue limit. Both hosted rollout variables default unset; a required replay remains visibly blocked until separately authorized. This launch does not enable paid usage or alter spending limits. Hosted execution is unverified until actual jobs execute; local measurements exclude hosted queue/setup/install time.

Hosted jobs choose Linux runners and their matching hash lock. That deployment
choice does not define the contributor's operating system. See
[RELEASE_REVIEW.md](RELEASE_REVIEW.md) for the recorded hosted status and local
release receipt commands.

A package uses `TASK.json`, `SOURCES.json`, `VERIFY.json` and README with exact inputs, provenance, unresolved closure and bounded commands. Existing registered historical certificates need not be retrofitted into misleading package declarations. New packages must state exact mathematical scope and limitations.

Concurrent destination PRs #1 and #2 landed at `213d179` during construction. Their public-fork ancestry handling and undeclared package-shadowing fix are integrated. One consolidated workflow remains; Tier 0 is intentionally owner-gated by `E99_PUBLIC_CI == 'true'`, and Tier 1 is separately gated by `E99_PUBLIC_PACKAGE_REPLAY == 'true'`. Both remain unset pending an authorized hosted-fork canary. No hosted fork canary is claimed.
