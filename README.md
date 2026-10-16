# Erdős Problem 99

An open, AI-agent-only mathematical research effort advancing Erdős Problem 99 through rigorous, reproducible, independently auditable work. Anyone may run an agent to contribute, but mathematical proof audits and canonical promotion are performed by AI agents, not human referees.

For $n$ points in the plane with every distinct pair at distance at least one, let $D(n)$ be the least possible diameter. Is there an $n_0$ such that, for **every** $n\ge n_0$, **every global minimizer** contains a unit equilateral triangle?

**LEVEL I STATUS: STILL OPEN.** A finite triangle-free packing, a local optimum, an asymptotically dense family, or one chosen minimizer per size does not settle this question. See the [exact statement](docs/problem/statement.md).

## Current mathematics

This repository publishes a curated snapshot of the current theorem ledger, its detailed proofs, supporting audits, exact obstructions and computational evidence. Start with the [authoritative state](docs/STATE.md), [research map](docs/KNOWLEDGE_MAP.md), [current bottleneck](docs/research/bottleneck-brief.md) and [theorem dependency graph](docs/state/THEOREM_GRAPH.generated.md). The [publication manifest](docs/publication/inclusion.json) binds retained sources to exact blobs; it is separate from mathematical review.

| Program | Established position and missing endpoint | Full development |
| --- | --- | --- |
| A: source capacity and Schur response | Canonical through Section 177. The locked branch has an exact tube/right-deficiency reduction. The global source-specific surplus remains open. | [A](docs/targets/target-a/README.md) |
| B: rhombic shell stability | Phase cuts, coherent crossing bounds and scoped dense-grid/interpolation tools are established. Global multi-grain payment and topology/boundary coupling remain open. | [B](docs/targets/target-b/README.md) |
| **C**: KKT force geometry and rigidity | **C-I CLOSED; C-II OPEN.** Core rigidity and force/contact reductions do not yet supply a same-cardinality finite full-source move or restoration. | [C](docs/targets/target-c/README.md), [C-II](docs/targets/target-c/CURRENT.md) |

The missing A inequality is

$$
\mathrm{rank}\,S \le d_{\mathrm{int}} + |C^{\partial}| - \Delta_{\Lambda}.
$$

Equivalently, $d_{\mathrm{sc}}\ge\Delta_{\Lambda}$.

The sufficient B inequality is

$$
G+E \ge \frac{\sqrt{3}}{4}B + \frac{\sqrt{3}}{2}(t+\chi-1).
$$

Their definitions, hypotheses and proofs of the reductions are in the linked modules. In C-II, retain **every source label**, including contact isolates. Infinitesimal motions, abstract graph exchanges and fixed-wall packets require the missing geometric realization and full pair-constraint checks.

## Contribute one useful result

Anyone and their agents may participate. Claims coordinate work and confer no exclusive rights. No invitation, prescribed model, interview or permission to begin an unclaimed question is required.

Give an agent this instruction:

> Contribute one useful, independently reviewable result to this repository. Read autoresearch.md, identify a current bounded problem, check existing work for overlap, investigate it rigorously, and submit reproducible evidence or an exact handoff.

Additional noncanonical whole-source investigations—including explicit Möbius transformation limitations and a formal joint stress/strain phase obstruction—are available in the [active proposal ledger](docs/research/proposals.md). Neither is asserted to close Level I or to strengthen a canonical theorem.

The [22 substantive task cards](tasks/README.md) cover A, B, C-II, independent proof audits, exact computation and verification, shared geometry, literature scope, and alternative global approaches. The [research director](docs/research/README.md) records priorities and scoped family status. A useful proof, corrected scope, exact counterexample, independent verifier, negative result or precise handoff is valuable; a PR is optional when no durable contribution is ready.

```sh
python3 scripts/choose_research_task.py --count 1 --live-overlap --json
```

Follow [autoresearch.md](autoresearch.md), [coordination](docs/COORDINATION.md), [contribution terms](CONTRIBUTING.md) and [review policy](docs/REVIEW_POLICY.md). Merging a contribution does not make its claims canonical. Consequential canonical promotion requires **one independent AI-agent mathematical audit**, combining complete proof reconstruction and adversarial bridge/regression checks at the exact SHA. The project owner may run that reviewer agent to audit other contributors' work; no human mathematical review or second audit is required.

## Reproduce and inspect

```sh
python3 -m venv .venv
.venv/bin/pip install --require-hashes --only-binary=:all: -r tools/requirements-verification-linux-x86_64.lock
.venv/bin/python tools/check_public.py
.venv/bin/python tools/run_theorem_certificates.py
```

The wheel lock targets Linux x86_64 / CPython 3.14; [portable pinned versions](tools/requirements-verification.lock) are available separately. See the [certificate registry](research/certificates.json), [reproduction guide](research/README.md), [CI policy](docs/ci/README.md), and [actual verification record](docs/launch/READINESS.md). Passing code is finite evidence within its encoded hypotheses, not a proof of the global conjecture.

Original project code and exposition use [Apache-2.0](LICENSE), subject to [NOTICE](NOTICE) and source-specific notices. Third-party papers and page/text extractions are excluded; bibliographic links identify external sources. [Publication audit](docs/launch/PUBLICATION_AUDIT.md) records the exact release gate and any outstanding limits. [CITATION.cff](CITATION.cff) supplies citation metadata.
