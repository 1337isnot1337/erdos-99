# Localized verification

Tier 0 runs trusted metadata, theorem/task/generated-view consistency, public links, changed-file security and package planning. `python tools/check_public.py` checks the candidate corpus; it proves no mathematical theorem. The proposed source CI implementation was inspected at `d54097cb` and merged upstream as `aa9b4566` during construction; public-specific integrity checks replace archive-only assumptions.

Tier 1 replays only declared affected packages and their dependency closure, with at most two packages and 240 declared seconds in one serial job. The planner unions merge-base, head and current-base inputs. Replay uses Linux bubblewrap, no network, no inherited credentials, read-only declared Git blobs, shell-free commands, time and resource limits. Missing isolation refuses replay. No dynamic matrix is used. See `tools/local_ci.py` and `tools/localized_ci/`.

Tier 2 is explicit: `python tools/run_theorem_certificates.py`, followed by `python tools/check_public.py` and appropriate tooling tests. Canonical, shared-foundation, removed-input, changed verifier-domain and unknown impacts report `full-verification-required`; this is not a full pass. Do not silently replace it with targeted success.

Ordinary PRs use a trusted base control checkout and read-only permissions; contributed code is never run with `pull_request_target`. Actions are commit-pinned and checkout credentials are not persisted. No full certificate suite runs on every PR. Per-PR cancellation is not a repository-wide queue limit. The replay rollout variable defaults unset; a required replay then remains visibly blocked. This launch does not enable paid usage or alter spending limits. Hosted execution is unverified until actual jobs execute; local measurements exclude hosted queue/setup/install time.

A package uses `TASK.json`, `SOURCES.json`, `VERIFY.json` and README with exact inputs, provenance, unresolved closure and bounded commands. Existing registered historical certificates need not be retrofitted into misleading package declarations. New packages must state exact mathematical scope and limitations.
