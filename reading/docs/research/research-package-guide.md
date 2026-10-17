> Generated reading edition · [exact source](../../../docs/research/research-package-guide.md) · source SHA-256 `bcfaa24541d4597d6b3e48e963915103317a0971716ae149bcea481f9befe44a`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Optional research packages

A focused proof note, counterexample or handoff can be enough. Use a package for
reusable code/evidence when its exact inputs and bounded commands can be declared.
Keep frozen predecessors unchanged. This scaffold uses the existing
[isolated package protocol](../ci/PUBLIC_LOCALIZED_CI.md); it adds no executor.

```sh
python scripts/new_research_package.py my-experiment \
  --task verify-a-schur-linkage-bound --author 'Your public name or handle' \
  --source docs/problem/statement.md
python scripts/research_package.py --package research-packages/my-experiment --check-only
```

Run from the repository root. The source must be a committed regular file whose
working bytes match HEAD. Repeat `--source` for each input. The generator refuses
an existing directory, unsafe name, symlink or modified source. It creates:

- `README.md`: objective, falsification, evidence, credit and **Open next questions**.
- `TASK.json`: scope, finite domain, limitations and unreviewed classification.
- `SOURCES.json`: baseline, exact source commits/hashes, package dependencies and unresolved closure.
- `VERIFY.json`: declared input set, Python environment and bounded argument-vector commands.
- `verify.py`: a deliberately failing draft, including under optimized Python.

Metadata-valid is not evidence-valid. The checker is unresolved and cannot receive
a successful replay designation until implemented. Replace draft text, supply a
positive case and meaningful failure controls, and update the checker hash after
editing. Declare every helper/data/generator input; justify clearing unresolved
closure. Pin immutable inputs without rewriting their source or predecessor.
Record source notices, contributor credit and actual AI roles.

The metadata helper reads working-tree files and checks manifests/source identities
without running commands or installing dependencies. It reports unresolved closure,
not a mathematical verdict. Commit the package before the Git-blob planner can
inspect it:

```sh
python tools/check_public.py
python tools/local_ci.py --base-ref origin/main
```

Contributors still reproduce their own evidence. The optional backend requires
Linux/Bubblewrap and its supported Python 3.14 environment, read-only declared
inputs, no network, and existing serial time/resource limits. Unsupported dynamic
inputs or dependencies remain explicit full-verification obligations; do not alter
the protocol merely to turn a draft green. Full repository replay belongs to the
merging agent when required. Neither metadata nor a finite replay promotes claims.

An **Open next questions** entry gives the exact question, why it matters, a
feasible first action and its blocker. If no next question is justified, say so.
Update the existing investigation thread and link this package; no extra session
report is required. [Archive publication](research-archive-intake.md) and independent
scientific acceptance remain distinct.

Hosted rollout remains governed by the existing owner gates. The first stage is
local metadata, failure-control and planner checks; record environment and timings.
Only a separately authorized canary can establish actual hosted behavior. Scope
selection must retain unknown/dependency impact, sandbox refusal must remain
visible, and observed queue/setup/replay cost must fit a declared budget before
expansion. This change enables no paid jobs or repository variables.
