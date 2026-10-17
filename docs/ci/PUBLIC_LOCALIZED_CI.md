# Localized public E99 CI

This is the public-repository adaptation of E99's scoped verification architecture.
It intentionally has **no dependency on the private E99 Git repository**, its
historical archives, theorem certificates, or private CI environment.

The authoritative scientific corpus is managed separately. This system does
not assert any theorem to be proved merely because its CI passed.

## Verification semantics

- **Tier 0, fast integrity:** A trusted control checkout classifies changed Git
  objects; checks required public-facing files, task references, changed JSON
  syntax and straightforward changed Markdown links; checks whitespace and
  common credentials/privileged workflows. It never executes contributed research
  code or certifies a mathematical proof.
- **Tier 1, localized replay:** Opt-in packages under
  `research-packages/<id>/{TASK,SOURCES,VERIFY}.json` and README declare exact
  inputs and reproducible commands. Only affected packages and transitive
  dependents are eligible. At most two packages, 120 declared seconds per package
  and 240 seconds of declared work,
  one serial job; no matrix. Replay requires bubblewrap namespace isolation and
  Python 3.14. It never exposes credentials, network or dynamic installation.
- **Tier 2, comprehensive verification or explicit independent AI-agent impact audit:**
  Canonical mathematics, theorem-state/route changes, shared verification code,
  historical/unpackaged research inputs, unknown closure, malformed manifests,
  removed inputs and unsafe Git ancestry require this gate. Tier 2 is
  NOT scheduled automatically. Required full certificate replay belongs to the
  merging agent on the final integration candidate, not to each contributing
  agent before submission. Contributors reproduce their own evidence and
  report full replay as deferred. Workflow-only changes retain their structural
  checks. See [verification ownership](README.md#verification-ownership).

Output classifications: `fast-only`, `targeted-replay`, and
`full-verification-required`. `full_verified` is always `false` for Tier 0
and Tier 1. Planning success is not proof that a replay ran.

Automatic scheduling is reported separately:

| `replay_schedule` | Meaning |
|---|---|
| `not-required` | No package replay was selected. |
| `ready` | The complete required package set fits the automatic budget; execution still needs its separate switch. |
| `deferred-budget` | The complete set exceeds the automatic budget and remains pending. |
| `requires-review` | Scientific impact or integrity cannot be resolved by targeted replay. |

An over-budget set retains `level: targeted-replay`, every required `packages`
entry and its full `workload_seconds`. It does not become a full-theorem change
or receive a partial automatic pass. `--require-localized` exits with status 3
for either a full-verification handoff or budget-deferred targeted work.

## Hosted execution and cost containment

Workflow: `.github/workflows/theorem-state.yml`.

Tier 0 runs automatically on non-draft PRs. The former `E99_PUBLIC_CI` variable
does not gate these structural checks. Tier 1 remains separately enabled by
`E99_PUBLIC_PACKAGE_REPLAY == 'true'` and runs only when the entire selected set
fits the automatic budget.

The planning summary states which verification remains pending. Its green status
means structural checks passed, not that targeted or full replay passed.
There is no push trigger,
cron, large matrix, full-certificate automatic run, or paid-runner setting change.
Standard GitHub-hosted runners only.

The workflow uses Python 3.14.7 and the trusted locked wheels. It installs
Bubblewrap if missing; the runtime probe rejects unavailable namespaces.
The fork's exact head and current base ancestry are fetched separately from the
trusted control checkout. There is no unisolated fallback. Actual hosted runs
must establish runtime availability; enabling the workflow is not canary evidence.

Optional package execution remains separate from structural checks. Keep its
pending results and any full-verification requirement visible in the handoff.

Per-PR cancellation does not cap concurrent PRs across a repository. With
hundreds of independent PRs, even inexpensive plan jobs can queue.

## Local reproduction

Use a clean committed checkout with complete Git ancestry:

~~~sh
python3 -B -m unittest tools.test_local_ci tools.test_ci_integrity -q
python3 -B tools/local_ci.py --base-ref origin/main \
  --output /tmp/e99-public-plan
python3 -B tools/local_ci.py --base-ref origin/main \
  --integrity --require-localized --output /tmp/e99-public-check
~~~

Only base-control scripts execute while candidate PR files are untrusted data.
Tier 1 uses `python3 -I -S`, declared read-only inputs, isolated namespaces,
bounded logs and CPU/wall timeouts. None of these mechanics proves the scientific
claim or complete Python dependency inference.

## Current-corpus integration

The planner conservatively protects `docs/state/`, `docs/targets/`,
`docs/theory/`, `docs/problem/` and the theorem manifest if present. Unknown
paths require Tier 2, not a fictional selective success. As the real canonical
corpus is integrated, extend protected paths and independently validate the
complete theorem-state/certificate verifier; never assume a missing verifier
can be replaced by a quick metadata check.

One independent AI-agent mathematical audit is required for promoting consequential
claims, in addition to the complete theorem-state transaction. The review must cover
both the full proof and adversarial bridge/regression checks. No human mathematical
review or second agent audit is required. Finite computational evidence is not an
all-size theorem.

No hosted benchmark, bubblewrap canary, public fork replay, or public
complete-corpus certificate sweep is claimed here.


## Local package shadowing regression

The upstream localized protocol was independently audited for import-shadowing
errors. An undeclared local regular package (for example, `math/__init__.py`)
could otherwise be absent from the isolated replay and silently replaced by the
standard library module with the same import name. The public port includes
the corrective dependency audit: both `module.py` and
`module/__init__.py` candidates in the repository root and entry-script root
must be declared, or the affected package requires Tier 2/review. A declared
local initializer is included in the isolated replay rather than substituted
with a standard library import.

Regression coverage:
`test_undeclared_package_shadowing_standard_library_requires_review` and
`test_declared_package_shadowing_standard_library_is_replayed`. The second
test needs the actual Python 3.14/Bubblewrap sandbox and has not been
independently executed in the available Python 3.12 environment. The private
source worker reports complete verification of the corresponding fix.

