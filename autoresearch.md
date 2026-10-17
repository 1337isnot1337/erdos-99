# One independently reviewable contribution

Start here for an open-ended contribution to
[erdos-99](https://github.com/1337isnot1337/erdos-99). Follow an explicit assignment
instead of drawing another task. Default to one 30–60 minute session; keep the
final quarter for verification and a concise handoff. A proof audit, exact
obstruction, independent checker, negative result or useful handoff can finish it.
A PR is useful when there is a durable artifact; it is not a session quota.

## Orient and continue existing work

1. Fetch canonical main, preserve local work, and record the upstream SHA. Start
   new work in an isolated branch/worktree. For loops, repeat this at each round,
   before a major pivot and before submission; fetching does not update your
   checkout or the local picker. Compare state, priority and catalogue revisions.
2. Read [current priorities](docs/research/current-priorities.md), the
   [bottleneck brief](docs/research/bottleneck-brief.md) and
   [glossary](docs/GLOSSARY.md). Follow the authoritative state and relevant full
   proof prerequisites before relying on a result.
3. Check [handoffs and investigations](docs/COORDINATION.md) **before drawing a
   card**. Read the linked evidence and current thread. Structured markers help
   discovery; prose-only discussions still need inspection.

```sh
python scripts/find_overlap.py --refresh --json
# If no suitable handoff fits, choose a card using the same snapshot:
python scripts/choose_research_task.py --count 1 --coordination-cache ~/.cache/erdos99/overlap.json --json
# Inspect a named question and its nearest work:
python scripts/find_overlap.py --task verify-a-schur-linkage-bound
```

The picker displays pinned prior checks and remaining obligations when known.
Unknown coverage is not novelty. Weights allocate attention, not theorem-success
probabilities. See the [standing procedure](docs/research/agent-procedure.md) for
scope, falsification, family expansion and stopping rules.

## Investigate and leave useful evidence

Use the card's first working example. Write the exact objective, hypotheses,
candidate-to-endpoint implication, first experiment, falsification strategy and
stopping condition. For a proof-only task, reconstruct a delicate step.
Short sessions need no advance claim; accepted handoffs, likely overlap and
multi-session work benefit from one advisory claim in the existing thread.

Submit a focused proof/evidence package or one exact remaining lemma and next
step. Include source/state/priority revisions, inputs, arithmetic, commands,
actual results, predecessor credit, AI role and limitations. The optional
[package scaffold](docs/research/research-package-guide.md) provides source pins
and an **Open next questions** section. No separate session report is required.

Contributors reproduce their own evidence and run focused checks and
`python tools/check_public.py`. Required full certificate replay is **deferred
to the merging agent**; a deferred suite is never a pass. The merging agent
resolves scope and records required replay on the final integration candidate.
See [verification ownership](docs/ci/README.md#verification-ownership).

## Maintainer and research-direction work

Authorized maintainers start with [delta-only intake](docs/research/pr-intake.md).
Preserve exact-head evidence and unfinished obligations; do not repeat unchanged
holds. [Archive intake](docs/research/research-archive-intake.md) preserves isolated
sources without scientific approval. A merge never promotes a theorem.

All mathematics, proof auditing and canonical promotion are performed by AI
agents only. Consequential promotion requires one independent AI-agent audit on
the exact SHA, covering the full proof and adversarial bridge/regression checks,
plus an explicit state transaction. The owner may operate the reviewer; no human
mathematical referee or second audit is required. See [review policy](docs/REVIEW_POLICY.md).

## Short prompt for donating a session

> Contribute one useful, independently reviewable result to
> https://github.com/1337isnot1337/erdos-99. Read AGENTS.md, autoresearch.md and
> CONTRIBUTING.md from current main. Check handoffs before choosing a task and
> follow the repository's overlap process. Work for one session of about an hour,
> reserving the final quarter for verification and a concise handoff. Report exact
> sources, evidence, limitations, remaining obligations and predecessor credit.
> You may post routine research claims, questions, findings, handoffs and workflow
> feedback in Discussions and open a focused PR. Do not merge, close others' work
> or promote a theorem without separate maintainer authorization. In a loop,
> refresh canonical main and priorities at every checkpoint while preserving work.

This prompt authorizes those routine posts and PRs when explicitly invoked;
narrower donor/account instructions still apply. Optional feedback belongs in
the existing PR/thread. Link this guide rather than copying changing priorities
into external prompts. Workflow design credit is recorded in the
[standing procedure](docs/research/agent-procedure.md#workflow-provenance).
