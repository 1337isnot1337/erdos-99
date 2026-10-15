# Instructions for human and AI contributors

This repository studies Erdős Problem 99, the eventual unit-equilateral-triangle question for **every global minimum-diameter configuration**. Preserve that quantifier. A finite result, local optimum, dense packing or one minimizer per size is not an answer to the eventual problem.

## One bounded contribution

1. Start from a clean clone and current `main`: `git fetch origin` and inspect `git status`.
2. Read [the problem](docs/problem.md), [current status](docs/current-status.md), and one self-contained task from [`tasks/index.json`](tasks/index.json).
3. Search open Issues, Discussions and pull requests for the task ID. Claims are advisory, expire as stated in the issue, and do not confer ownership. If there is overlap, coordinate in public; if there is none, begin without requesting approval.
4. Pick one bounded proof, counterexample search, reproduction, audit or alternative approach. State what observation would falsify it before doing lengthy work.
5. Run the relevant reproduction and lightweight checks. Keep a complete, small evidence package and distinguish exact results from numerical or heuristic evidence.
6. Open a focused pull request or leave a useful issue handoff. If no publishable change is ready, report the result and exact next question in the issue or Discussion.

Use a session of roughly 30–60 minutes by default. Continue longer only when a concrete proof or computation is actively progressing; do not run indefinite searches or expensive jobs without a bound and a reason.

## Evidence and scientific status

State assumptions, quantifiers, data sources, code versions, commands, outputs, failures and negative controls. Preserve useful negative results. A merged contribution may remain author-checked, agent-audited, conditional or finite evidence. Only maintainers can mark a statement canonical, and consequential theorem promotion requires independent human mathematical review. Agent review must never be described as human review.

Do not use files, certificates or access from a private repository as an unstated dependency. Do not add third-party papers, extracted text, scans, or images unless the redistribution basis is clear and notices are included. Cite public bibliographic records instead.

## Local checks

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_repo.py
```

Reproduce the included finite computation with `python3 scripts/triangular_lattice.py --max-n 5`. No external package is required. The checks are intentionally small and do not certify a mathematical proof.
