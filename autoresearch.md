# Bounded autonomous research guide

Use this file as an entrypoint for a human or autonomous agent asked to contribute one independently reviewable result to Erdős Problem 99. The default is a single bounded investigation, not an open-ended attempt to solve the entire problem.

## Start from public evidence

1. Fetch current public `main` and record its commit:

   ```sh
   git fetch origin
   git rev-parse origin/main
   git status --short --branch
   ```

2. Read [`docs/problem.md`](docs/problem.md), [`docs/current-status.md`](docs/current-status.md), [`tasks/README.md`](tasks/README.md), and the complete task file you select.
3. Confirm the problem is still open and check the task's references. Do not rely on a private archive or assume that an old status is current.

## Check overlap

Search the task ID in the repository's open Issues, Discussions and pull requests. With GitHub CLI:

```sh
gh issue list --repo 1337isnot1337/erdos-99 --state open --search P99-COMP-001
gh pr list --repo 1337isnot1337/erdos-99 --state open --search P99-COMP-001
```

Use the task's actual ID in place of `P99-COMP-001`. In a browser, use GitHub's repository search with the same ID and inspect open results. If another contributor has an active claim, make a distinct subquestion or coordinate publicly. Claims are not exclusive and expire on the date or event their author states.

## Run one bounded investigation

Choose one task, one lemma, one finite exact computation, one counterexample attempt, or one independent audit. Before work, write down:

- the exact claim and all hypotheses;
- the known starting evidence;
- one concrete experiment or proof step;
- what would falsify the claim or invalidate the approach;
- a stopping condition and a time or computation bound.

Default to 30–60 minutes. A rigorous negative result, a correction to a conjecture, an exact counterexample, or a precise obstacle can be a useful outcome. Do not continue a search just because it has not found an answer.

## Verify and package

- Reproduce the relevant baseline from this repository.
- Keep exact finite evidence separate from numerical evidence and mathematical conclusions.
- Include a minimal executable command, input data, expected output, actual output and relevant environment details.
- For proofs, include definitions, quantifiers, hypotheses, each main implication and a falsification attempt.
- Record source attribution, contributor names/handles and AI assistance.
- Run the lightweight local checks before submitting:

  ```sh
  python3 -m unittest discover -s tests -v
  python3 scripts/check_repo.py
  ```

## Submit or hand off

Create a pull request for a self-contained, reviewable change. Use the PR template and state the evidence status accurately. It is acceptable to leave a concise issue or Discussion handoff instead of a PR when the result is negative or the work is incomplete. Ask for the next exact question; do not describe agent review as human review or a local result as a solution to the eventual problem.

Maintainership may update `tasks/index.json` and `docs/research-directions.md` as community priorities change. These files are the Phase 1 task-priority interface; there is no automated director.
