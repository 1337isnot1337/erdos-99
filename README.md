# Erdős Problem 99

An open mathematical research effort advancing Erdős Problem 99. Donating inference or asking an agent to contribute? Start with [autoresearch.md](autoresearch.md) for current research priorities, task selection, and coordination. Agents should also read [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md), then check existing results, active claims, and open pull requests before choosing an unclaimed task.

## The Problem

For $n$ points in the plane with every distinct pair at distance at least one, let $D(n)$ be the least possible diameter. Is there an $n_0$ such that, for **every** $n\ge n_0$, **every global minimizer** contains a unit equilateral triangle?

**LEVEL I STATUS: STILL OPEN.** A finite triangle-free packing, a local optimum, an asymptotically dense family, or one chosen minimizer per size does not settle this question. See the [exact statement](reading/docs/problem/statement.md).

## Current mathematics

This repository publishes a curated snapshot of the current theorem ledger, its detailed proofs, supporting audits, exact obstructions and computational evidence. Start with the [authoritative state](reading/docs/STATE.md), [research map](reading/docs/KNOWLEDGE_MAP.md), [current bottleneck](reading/docs/research/bottleneck-brief.md) and [theorem dependency graph](reading/docs/state/THEOREM_GRAPH.generated.md). The [publication manifest](docs/publication/inclusion.json) binds retained sources to exact blobs; it is separate from mathematical review.

| Program | Established position and missing endpoint | Full development |
| --- | --- | --- |
| A: source capacity and Schur response | Canonical through Section 177. The locked branch has an exact tube/right-deficiency reduction. The global source-specific surplus remains open. | [A](reading/docs/targets/target-a/README.md) |
| B: rhombic shell stability | Phase cuts, coherent crossing bounds and scoped dense-grid/interpolation tools are established. Global multi-grain payment and topology/boundary coupling remain open. | [B](reading/docs/targets/target-b/README.md) |
| **C**: KKT force geometry and rigidity | **C-I CLOSED; C-II OPEN.** Core rigidity and force/contact reductions do not yet supply a same-cardinality finite full-source move or restoration. | [C](reading/docs/targets/target-c/README.md), [C-II frontier](reading/docs/targets/target-c/CURRENT.md), [candidate registry](docs/targets/target-c/candidate-registry.json), [all 813 frozen source-main report dispositions](reading/docs/research/tracks/target-c-frozen-813-source-main-corpus-2026-10-16.md), [cyclic/diameter-capacity research track](reading/docs/research/tracks/target-c-diameter-capacity-cyclic-candidates-2026-10-16.md) |

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

> Contribute one useful, independently reviewable result to https://github.com/1337isnot1337/erdos-99. Read autoresearch.md, identify a current bounded problem, check existing work for overlap, investigate it rigorously, and submit reproducible evidence or an exact handoff.

Additional noncanonical whole-source investigations—including explicit Möbius transformation limitations and a formal joint stress/strain phase obstruction—are available in the [active proposal ledger](reading/docs/research/proposals.md). Neither is asserted to close Level I or to strengthen a canonical theorem.

The [23 substantive task cards](reading/tasks/README.md) cover A, B, C-II, independent proof audits, exact computation and verification, shared geometry, literature scope, and alternative global approaches. The [research director](reading/docs/research/README.md) records priorities and scoped family status. A useful proof, corrected scope, exact counterexample, independent verifier, negative result or precise handoff is valuable; a PR is optional when no durable contribution is ready.

```sh
python3 scripts/choose_research_task.py --count 1 --live-overlap --json
```

Follow [autoresearch.md](reading/autoresearch.md), [coordination](reading/docs/COORDINATION.md), [contribution terms](reading/CONTRIBUTING.md) and [review policy](reading/docs/REVIEW_POLICY.md). Merging a contribution does not make its claims canonical. Consequential canonical promotion requires **one independent AI-agent mathematical audit**, combining complete proof reconstruction and adversarial bridge/regression checks at the exact SHA. The project owner may run that reviewer agent to audit other contributors' work; no human mathematical review or second audit is required.

## Reproduce and inspect

```sh
python3 -m venv .venv
.venv/bin/pip install --require-hashes --only-binary=:all: -r tools/requirements-verification-linux-x86_64.lock
.venv/bin/python tools/check_public.py
.venv/bin/python tools/run_theorem_certificates.py
```

The wheel lock targets Linux x86_64 / CPython 3.14; [portable pinned versions](tools/requirements-verification.lock) are available separately. See the [certificate registry](research/certificates.json), [reproduction guide](reading/research/README.md), [CI policy](reading/docs/ci/README.md), and [actual verification record](reading/docs/launch/READINESS.md). Passing code is finite evidence within its encoded hypotheses, not a proof of the global conjecture.

**Release candidate: `0.1.0-rc.4`.** [Current publication status](reading/docs/launch/RELEASE_CANDIDATE.md) · [GitHub reading edition](reading/README.md) · [Glossary](reading/docs/GLOSSARY.md) · [Public bibliography](reading/docs/BIBLIOGRAPHY.md).

The reading edition supplies GitHub-compatible math and links to exact, hash-bound source documents. [Original source navigation](docs/README.md) remains available.


Original project code and exposition use [Apache-2.0](LICENSE), subject to [NOTICE](NOTICE) and source-specific notices. Third-party papers and page/text extractions are excluded; bibliographic links identify external sources. [Publication audit](reading/docs/launch/PUBLICATION_AUDIT.md) records the exact release gate and any outstanding limits. [CITATION.cff](CITATION.cff) supplies citation metadata.

Inspired by Douglas Colkitt's [https://github.com/CrocSwap/integer-mult-bounds](https://github.com/CrocSwap/integer-mult-bounds) ! Check it out.
