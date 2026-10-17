# Standing agent procedure

Use [autoresearch](../../autoresearch.md) as the short entry point. This procedure
supports one useful contribution; it is not a demand for a new theorem or PR.

## Refresh and orient

At each new session, each loop round, a major pivot and submission, fetch the
remote pointing to `1337isnot1337/erdos-99`. Inspect remotes and local changes;
preserve other work. Record the fetched SHA immediately and start a new isolated
branch/worktree for new work. Fetching does not update working files or the picker.
For longer rounds, refresh at a safe checkpoint roughly hourly; avoid interrupting
an artifact-writing run. If offline, name the last checked version and limitation.

Compare `state_version`, `priority_revision` and `catalogue_revision` with your
checkpoint. Read changed decisions/evidence before reusing an assignment.
[STATE](../STATE.md) and the theorem manifest control authority. Read the
[exact problem](../problem/statement.md), [bottleneck](bottleneck-brief.md), relevant
route and **full load-bearing prerequisites**, including implicit section references.
The proof graph is navigation, not a substitute for statements and proofs.

## Handoffs before cards

Follow [coordination](../COORDINATION.md). Inspect live handoffs, their artifact
links and latest status before drawing a card. Join a complementary scope; an
independent audit may deliberately overlap. Explicit assignments take precedence.
If nothing suitable fits, use the weighted picker and its first experiment.
An empty `existing_checks` array means unknown coverage. Prior checks apply only
to their pinned source, domain and stated status; a changed theorem state requires
reassessing applicability. Read full matched files and hypotheses.

```sh
python scripts/find_overlap.py --refresh --json
python scripts/choose_research_task.py --count 1 --coordination-cache ~/.cache/erdos99/overlap.json --json
python scripts/find_overlap.py --task verify-a-schur-linkage-bound
```

The cache defaults to `~/.cache/erdos99/overlap.json`; `--cache PATH` supports
parallel sessions. Pass the same path as `--coordination-cache PATH`. Keep caches
outside Git: they contain repository text. `--offline` uses explicitly dated
coverage; query failure and unavailable surfaces are never absence of overlap.
`--include-closed` also queries closed/merged PR bodies. PR comments, closed Issues
and remote changed-file inventories are not searched. Metadata markers are
advisory; inspect prose-only threads as well.

## Bound the investigation

Write the objective, definitions, complete hypotheses, implication to a canonical
quantity, first experiment, falsification strategy and stop condition. Reproduce
starting evidence. For proof-only work reconstruct a delicate implication rather
than adding a decorative numerical test. Run a finite investigation; use exact
arithmetic where an exact certificate exists. Name the remaining global bridge.

Keep every sufficiently-large-cardinality and every-global-minimizer quantifier,
and every source label including contact isolates. A scaffold, smaller optimum,
response network, local optimum or infinitesimal feasible motion cannot replace
a full source without a theorem. Every proposed motion/replacement must check all
encoded source lower bounds and actual-diameter upper bounds, including inactive
pairs. At diameter D a C-II endpoint remains triangle-free and improves the
lexicographic pair (unit contacts, actual diameter pairs); strict sub-D competition
uses the same cardinality and unit separation.

Read [family status](research-family-status.md) before expansion. One useful
sublemma may finish a contribution. Before another substantial search or dependent
optimization, record the changed hypothesis, complete endpoint ledger, evidence
that it can affect the route, and one discriminating experiment with a stop rule.
A solo agent can make this research decision in its existing thread; no extra
approval or separate director agent is required. A new random seed alone does not
reopen an unchanged obstruction.

## Verify, submit or hand off

Keep the final quarter for checks and a concise handoff. Run the new/changed
verifier or experiment, focused behavior tests, `git diff --check`, and
`python tools/check_public.py`. Use `python tools/local_ci.py --base-ref origin/main`
to report scope. Contributors defer required full certificate replay to the merging
agent, including after rebases. Do not omit your own evidence-producing run.

One focused PR includes exact source/head/base, state/priority revisions,
hypotheses, arithmetic, commands/output, falsification checks, predecessor
comparison, attribution, AI roles, unchecked obligations and what is not proved.
Use the optional [package guide](research-package-guide.md) for reusable code.
A precise remaining lemma plus one feasible next action is a useful handoff when
no durable artifact is ready. Update the same investigation thread; release claims
when finished. No separate session diary or performance score is required.

The merging agent records the tested final candidate commit/tree, PR head, base,
environment, commands/results and required full replay or established exemption.
See [verification ownership](../ci/README.md#verification-ownership). A planner error
must be fixed or disclosed; `full-verification-required` is a handoff, not a pass.
Independent AI proof/bridge review and canonical promotion remain separate.

## Maintainer continuity and direction

Start authorized PR work with [intake](pr-intake.md). The ledger records acceptance
and review scope; the scheduling cache avoids unchanged work. Neither can promote
mathematics. Group related mechanisms and review each changed implication once,
retaining predecessor credit. Reuse exact-source evidence only with explicit
coverage and invalidation; an unrelated main SHA or compaction does not invalidate it.
Changed environments or comment-only evidence may require an explicit wake.

When reviewed evidence changes a bottleneck, update affected cards, family status
and the [priority log](research-priority-log.md) together. Keep weights unchanged
without a scientific allocation reason. Read author-checked archives as leads;
publication alone is not supplier admission or theorem approval. Optional workflow
feedback belongs in the existing PR or feedback hub, with one concrete improvement.

## Workflow provenance

The coordination, handoff-first, package and delta-intake design is adapted from
[CrocSwap/integer-mult-bounds](https://github.com/CrocSwap/integer-mult-bounds/tree/463113d675af7410ac91d53a4fed51ec6494eb9a),
Apache-2.0, prepared there by Douglas Colkitt with OpenAI Codex assistance.
The erdos-99 implementation was written by OpenAI Codex and retains this project's
agent-only mathematical review and verification-ownership policies. No mathematical
result or proof from that project is imported.
