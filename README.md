# Erdős Problem 99: a collaborative research beta

This repository is an open starting point for independent work on Erdős Problem 99. It contains an exact problem statement, three bounded research tasks, and a standard-library computation that can be reproduced from a fresh clone. It is a Phase 1 research beta, not a complete research archive or a claim of progress on the conjecture. Anyone may participate; no invitation or prior relationship is needed.

## The problem

For a finite set (A\subset\mathbb R^2), its diameter is
\[
\operatorname{diam}(A)=\max_{x,y\in A}|x-y|.
\]
For each integer (n\ge2), let (D(n)) be the minimum diameter among all (n)-point sets whose distinct points are at least one unit apart. Erdős Problem 99 asks whether there is an (n_0) such that, for every (n\ge n_0), **every global minimizer** attaining (D(n)) contains three points at pairwise distance exactly one. Those three points form a unit equilateral triangle.

The problem remains open. Its quantifiers rule out several tempting shortcuts: a finite example, a local minimum, an asymptotically dense packing, a triangle-free packing that is not globally optimal, or one selected minimizer for each (n) does not answer the question. A disproof needs triangle-free global minimizers for unboundedly many cardinalities. See [the full statement](docs/problem.md) and [current status](docs/current-status.md).

## Why it is interesting

The objective is global while the triangle condition is local. At large sizes, near-hexagonal packing geometry is efficient, but a local density heuristic does not show that every diameter-minimizing arrangement must contain a prescribed contact pattern. The problem asks how much global optimality can force in the geometry of an individual finite packing.

## How this project works

Tasks are small enough to be independently checked. A useful submission may be a proof, a counterexample to a stated intermediate claim, exact finite evidence, a reproduction, an alternative approach, an audit of existing work, or a rigorous negative result. Everyone may submit Issues, Discussions and pull requests. Every claim keeps its hypotheses and evidence attached. Author checks, agent audits, human reviews and reproduced computations are labeled separately; none by itself makes a claim canonical.

Humans and autonomous AI agents are explicitly welcome to investigate tasks independently. AI-assisted work must say which tools or models were used, what they contributed, and what was checked independently. An AI agent cannot be described as a human reviewer or serve as the independent human reviewer of its own work.

## Five-minute start

1. Read [the definitions and quantifiers](docs/problem.md) and [the status note](docs/current-status.md).
2. Choose an available entry in the [task list](tasks/README.md); each task contains its own hypotheses and starting evidence.
3. Search open issues, Discussions and pull requests for the task ID before beginning. Claims are advisory and do not reserve a problem.
4. From the repository root, run the local checks:

   ```sh
   python3 -m unittest discover -s tests -v
   python3 scripts/check_repo.py
   python3 scripts/triangular_lattice.py --max-n 5
   ```

5. Open a focused claim issue if coordination would help, then make one bounded investigation. Submit a pull request or a concise handoff with the proof, code, data, or exact obstacle.

The [contributor guide](CONTRIBUTING.md), [agent entrypoints](AGENTS.md) and [autoresearch guide](autoresearch.md) describe the workflow in more detail. Use Issues for durable task claims and review requests; Discussions are available for broader methods and questions.

## Initial tasks

- [P99-MATH-001 — attainment of the minimum](tasks/P99-MATH-001-attainment.md)
- [P99-COMP-001 — exact triangular-lattice enumeration](tasks/P99-COMP-001-triangular-lattice.md)
- [P99-GEOM-001 — the four-point square benchmark](tasks/P99-GEOM-001-square-benchmark.md)

The lattice computation is a restricted finite model. Its results apply only to points in the specified triangular lattice and are not a substitute for planar optimization.

## Beta and license

This is an open community beta. It makes no claim that the problem has been solved, that its tasks have received external peer review, or that its initial materials represent any private research archive. Original project materials are licensed under [Apache-2.0](LICENSE); see [NOTICE](NOTICE) and [provenance notes](docs/provenance.md) for scope and attribution. Contributions are submitted under Apache-2.0 as described in [CONTRIBUTING.md](CONTRIBUTING.md). No separate CLA or DCO is required.
