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

An **Open next questions** entry names the downstream claim or decision and
the exact quantity the extension can affect. State its changed hypothesis and
what either outcome enables. Then give one feasible first action and its blocker.
If no useful next question is justified, say so.
Update the existing investigation thread and link this package; no extra session
report is required. [Archive publication](research-archive-intake.md) and independent
scientific acceptance remain distinct.

Ordinary non-draft PRs run trusted structural checks and report verification scope.
Package execution remains separately opt-in through `E99_PUBLIC_PACKAGE_REPLAY`.
Record the actual environment and timings; local tests do not establish hosted behavior.
Unknown dependency impact remains explicit. A replay above the automatic budget
stays targeted and deferred, with every required package listed. Sandbox refusal
remains visible and never permits an unisolated fallback.
