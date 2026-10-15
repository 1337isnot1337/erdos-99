# P99-MATH-001 — Attainment and elementary bounds for (D(n))

**Availability:** open to everyone; no exclusive claim.
**Evidence status:** unreviewed task proposal.
**Type:** proof audit.

## Mathematical question

For every integer (n\ge2), prove that the infimum (D(n)) defined in [the problem statement](../docs/problem.md) is attained. Also prove the elementary bounds
\[
\frac{\sqrt n-1}{2}\le D(n)\le \sqrt2\bigl(\lceil\sqrt n\rceil-1\bigr).
\]
State precisely where finiteness, normalization, compactness and continuity enter.

## Definitions and hypotheses

A feasible set has exactly (n) points in (\mathbb R^2), with all distinct-point distances at least one. Its diameter is the maximum of its finitely many pairwise distances. (D(n)) is the infimum of these diameters.

## Why it matters

The main problem uses global minimizers. Compactness is what turns the infimum into a genuine minimum at each fixed (n). The coarse bounds are elementary scale checks for later finite work; they are not sharp asymptotics.

## Public prerequisites

Only Euclidean distance, continuity of a maximum of finitely many continuous functions, and compactness of closed bounded subsets of finite-dimensional Euclidean space are needed. No private repository or external paper is required.

## Starting point

- The (n) points (0,1,\ldots,n-1) on a line are feasible, so (D(n)\le n-1\).
- If (A) has diameter (d), radius-(1/2) disks around its points have disjoint interiors. They all lie in the radius-(d+1/2) disk around any chosen point of (A), giving (n\pi/4\le\pi(d+1/2)^2\).
- A square grid with (m=\lceil\sqrt n\rceil) sites on each side contains at least (n) sites with spacing one and diameter \(\sqrt2(m-1)\).
- For attainment, translate a point of each member of a minimizing sequence to the origin. Since a sequence can be chosen with diameter at most (n), all (n) labeled points lie in the closed radius-(n) disk. The constraints are closed and diameter is continuous. Check that this argument handles the unlabeled-set formulation by choosing any ordering for each finite set.

These are proof cues, not a substitute for checking every quantifier and limit step.

## First step

Write the configuration space after anchoring one point as a closed subset of a product of (n-1) closed disks. Verify that every subsequential limit preserves each pairwise lower bound, including pairs involving the anchor.

## Evidence expected

A self-contained proof for all (n\ge2), followed by a line-by-line audit of the two area/grid inequalities. A short independent derivation or formalized proof is welcome.

## Falsification strategy

Try to identify an escaping minimizing sequence after translation, a collision in a limit, or a gap between the infimum and the limit diameter. For the inequalities, test (n=2) and perfect-square values and verify the disk-containment and grid-cardinality arguments. A valid counterexample must satisfy the exact hypotheses.

## Reproduction

No computation is needed. If code is added, keep it optional, use only public inputs, and include a direct command plus an independent check of its output.

## Stopping condition

Stop when a proof for every (n\ge2) is written and independently checked, or when a specific invalid step in the proposed compactness argument is demonstrated. A list of finite cases is not a substitute.

## Scope limit

Attainment and coarse bounds do not imply that any minimizer contains a unit equilateral triangle, and do not address the eventual universal claim.

## Next questions

If the proof is sound, record which parts generalize to other dimensions or norms. Keep such extensions as separate claims with their own hypotheses.

## Attribution and AI disclosure

Credit all human authors and proof auditors. Report any AI model or tool used, when available, and distinguish generated suggestions from steps checked by the human authors. An AI audit is not human review.
