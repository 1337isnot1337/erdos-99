# P99-GEOM-001 — The four-point square benchmark

**Availability:** open to everyone; no exclusive claim.
**Evidence status:** unreviewed proof-audit task.
**Type:** independent mathematical verification.

## Mathematical question

Prove that (D(4)=\sqrt2), or provide a feasible four-point set with diameter strictly less than (\sqrt2). If the lower bound is proved, verify that the unit square is a triangle-free global minimizer at (n=4).

## Definitions and hypotheses

Here (D(4)) is the minimum diameter among four points in (\mathbb R^2) with every pair at distance at least one. The unit square has four vertices, adjacent side lengths one, and diagonal lengths (\sqrt2). Its unit-contact graph is a 4-cycle, which has no triangle.

## Why it matters

This is a small, exact benchmark for the global quantifier. A triangle-free finite minimizer is compatible with the eventual conjecture because the conjecture allows finitely many exceptions. It also tests whether a submitted argument confuses local contacts with global optimality.

## Public prerequisites

Only Euclidean geometry and the problem definition are needed to formulate the task. The [references page](../docs/references.md) links to the published small-case literature and the public problem record. The primary task is to provide a complete proof that a reader can inspect without access to a paywalled paper.

## Starting point

The square gives (D(4)\le\sqrt2). The public problem record identifies the four-point square as a finite exception, and the cited early-case literature provides context. This task asks for an independently inspectable proof of the matching global lower bound, not merely a numerical search.

## First step

Assume a four-point feasible set has diameter (d<\sqrt2). Choose a diameter pair and place it at ((0,0)) and ((d,0)). Derive the region in which either remaining point may lie from its lower-distance constraints to the endpoints and upper-distance constraints from the diameter. Then use the mutual constraint between the remaining points. Treat boundary cases explicitly.

## Evidence expected

A proof covering all planar configurations, including nonconvex, collinear and boundary cases. An exact-coordinate counterexample with all six distances checked would falsify the claimed value; a numerical optimizer alone would not prove the lower bound.

## Falsification strategy

Search for four explicit points with all pairwise squared distances at least one and all pairwise squared distances strictly below two. For a proof attempt, test its inequalities on the square, near-collinear sets and configurations with more than one diameter pair.

## Reproduction

No code is needed. Any computational search should report its bounded domain, exactness or error bounds, and a direct reproduction command. Failure to find a counterexample is not a proof.

## Stopping condition

Stop with either a complete proof of (D(4)\ge\sqrt2), an exact feasible counterexample below (\sqrt2), or a specific flaw in a proposed proof. State whether the submission establishes global minimality of the square.

## Scope limit

Even a complete proof at (n=4) does not prove or disprove the eventual statement for sufficiently large (n).

## Next questions

After settling this benchmark, compare the proof method with the known small cases cited in the literature. Any extension to other cardinalities is a new task with a separate completeness argument.

## Attribution and AI disclosure

Credit proof authors, sources and independent auditors. Disclose AI assistance and identify steps checked by humans. Agent review must not be described as human review.
