# One independently reviewable contribution

All mathematics, proof auditing and canonical promotion are performed by AI
agents only. A consequential canonical promotion requires one independent agent
audit (full proof plus adversarial bridge/regression checks) on the exact SHA.
The project owner may operate the independent reviewer on others' submissions.
No human mathematical referee or second reviewer is required.

Start here when given only “Contribute one useful, independently reviewable result to this repository.” Default to a 30–60 minute session. A proof audit, exact obstruction, independent checker, negative result or useful handoff can complete it.
The repository is [https://github.com/1337isnot1337/erdos-99](https://github.com/1337isnot1337/erdos-99). 

## Refresh at every checkpoint

1. Fetch `origin/main`; inspect your working tree and preserve local work. Start an isolated branch from current main. Record its SHA.
2. Read `docs/STATE.md`, the exact problem, `docs/research/bottleneck-brief.md` and `docs/research/priority-state.json`. Compare `priority_revision`, `catalogue_revision` and `state_version` with the prior session checkpoint. Read changed evidence and decisions before reusing an old assignment.
3. Read the relevant route and full load-bearing prerequisites. The public claim graph is navigation; follow statements and proofs, including implicit section references.
4. Query live overlap and inspect matching files, hypotheses, methods and drafts. A title match is only a lead. Failure to query is explicit; do not infer that the topic is free.

```sh
python3 scripts/choose_research_task.py --count 1 --live-overlap --json
gh pr list --repo 1337isnot1337/erdos-99 --state open --limit 100
gh issue list --repo 1337isnot1337/erdos-99 --state open --limit 100
```

Discussions, when enabled, are an additional coordination surface; the overlap helper queries them and reports availability. Issues and PRs remain usable if Discussions are disabled. See `docs/COORDINATION.md`.

## Select and investigate

Choose one card from `tasks/README.md`. The selector's weights allocate attention, not theorem-success probabilities. Direct frontier work is distinguished from finite-model, independent-audit and exploratory tasks. Read the family status before expanding an unchanged search.

Write the exact objective, definitions, hypotheses, candidate-to-endpoint chain, first finite experiment, falsification strategy, and stopping condition. Reproduce the relevant starting evidence. For a proof-only task, independently reconstruct one delicate step instead of adding a decorative numerical test.

Record a scoped claim issue when useful. Anyone may begin; claims expire within seven days and confer no ownership. Avoid redundant work, but independent review is welcome. Run a finite investigation and check every encoded source lower bound and actual-diameter upper bound where a motion or replacement is proposed.

## Finish, review and continue

Submit a focused PR with a self-contained proof or evidence package. Include commands, exact inputs, scope, source/priority revision, predecessor comparison, attribution, AI role, falsification checks, unresolved gap, and what the result does not establish. `docs/reports/REPORT_TEMPLATE.md` is a starting format. Request review of the exact head.

```sh
python3 tools/check_public.py
python3 tools/local_ci.py --base-ref origin/main
# Run the new or changed verifier/experiment that supports your contribution.
```

Contributing agents do not need to run the repository-wide certificate suite.
Record any required full replay as **deferred to the merging agent**, with the
planner's scope and the focused checks actually run. A
`full-verification-required` result is a merge-verification handoff, not a
submission failure or a full-verification pass. Planning errors still need to
be fixed or disclosed. Do not omit the experiment that produces your evidence.

The merging agent resolves the verification scope and runs required full replay
on the final integration candidate before merging:

```sh
python3 tools/run_theorem_certificates.py
python3 tools/check_public.py
```

Record the tested candidate commit/tree, PR head, base, environment, commands
and outcomes. Workflow-only changes retain the structural-check exemption.
See [verification ownership](docs/ci/README.md#verification-ownership).

The localized planner never labels unknown impact fully verified. A handoff without a PR should identify the exact remaining lemma and one next action. Close or release a claim when finished. A merge leaves lifecycle unchanged unless an explicit reviewed promotion transaction changes it.

At the checkpoint, record upstream SHA, state version, priority revision, task/method, bounded result, evidence and remaining obligation in the contribution or issue. Fetch and compare again before the next session. Maintainers fold reviewed findings into the priority log, family status and task catalogue; automatic PR activity alone is not a scientific priority decision.
