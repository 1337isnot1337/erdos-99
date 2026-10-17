# Localized public E99 CI (staged; disabled until explicit rollout)

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
  dependents are eligible. At most two packages, 240 seconds of declared work,
  one serial job; no matrix. Replay requires bubblewrap namespace isolation and
  Python 3.14. It never exposes credentials, network or dynamic installation.
- **Tier 2, comprehensive verification or explicit independent AI-agent impact audit:**
  Canonical mathematics, theorem-state/route changes, shared verification code,
  historical/unpackaged research inputs, unknown closure, malformed manifests,
  removed inputs, unsafe Git ancestry and overload require this gate. Tier 2 is
  NOT scheduled automatically. Required full certificate replay belongs to the
  merging agent on the final integration candidate, not to each contributing
  agent before submission. Contributors reproduce their own evidence and
  report full replay as deferred. Workflow-only changes retain their structural
  checks. See [verification ownership](README.md#verification-ownership).

Output classifications: `fast-only`, `targeted-replay`, and
`full-verification-required`. `full_verified` is always `false` for Tier 0
and Tier 1. Planning success is not proof that a replay ran. An affected
package whose replay switch is off fails the plan job.

## Owner-controlled activation and cost containment

Workflow: `.github/workflows/public-research-integrity.yml`.

Both repository variables are intentionally **unset**:

- `E99_PUBLIC_CI`: authorizes one Tier 0 job on each non-draft PR.
- `E99_PUBLIC_PACKAGE_REPLAY`: separately authorizes bounded Tier 1 replay.

Until the owner enables them, both hosted jobs skip. There is no push trigger,
cron, large matrix, full-certificate automatic run, or paid-runner setting change.
Standard GitHub-hosted runners only.

Before enabling Tier 0, check available included minutes and spending limits,
confirm hosted Python 3.14.7 and the locked wheels, and validate that unprivileged
bubblewrap namespaces work. Test a real public fork PR: the workflow fetches
the fork's exact head and the repository's current base ancestry.
If the sandbox is unavailable, fail closed; do not remove isolation.
Do not require a check that is skipped or blocked.

After one controlled, measured Tier 0 canary, separately consider package replay.
Keep full-verification/review requirements visible rather than silently green.

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

