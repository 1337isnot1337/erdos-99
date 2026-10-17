<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "41a20055beae2f345052440df5fbe226c6312470", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_h6_order_hull_reduction_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "754b064a3ba1c3a6f535b659aadae585bdf361054ca9e2e4458b5591fdd4d352"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: generic H6 order-hull reduction to 4,976 cells

Date: 2026-09-19

This note strengthens the generic support-seven H6 finite branch. It does not change theorem-state authority and does not close C-II.

## Result

The previous exact complete-angle endpoint contains

\[
5692=4464\,C_7+1228\,(C_3\sqcup C_4)
\]

generic H6 cells.

Retaining the physical gap-order disjunction at one pentagonal face and intersecting each order cone with the exact median-threshold hull gives 716 additional exact exclusions:

\[
\boxed{5692\longrightarrow4976}
\]

with

\[
\boxed{4976=3972\,C_7+1004\,(C_3\sqcup C_4).}
\]

The exact exclusion split is

```text
C7       492
C3+C4    224
```

and by normalized ground sign pattern:

```text
145    2
235   98
236  238
245   20
256  238
346   20
347    2
356   98
```

The remaining 4,976 cells have pattern census

```text
145     6
156    16
235   674
236  1286
237    16
245   494
256  1286
345    24
346   494
347     6
356   674
```

## Why the order disjunction is essential

The branch-free physical-pentagon hull theorem shows that after forgetting the cyclic gap order, the closed linear hull is exactly the old turn-simplex polytope. Therefore the newer rank-conditioned information cannot be added as one order-free linear inequality.

This reduction keeps all ten physical strict gap orders separate. Equality cases are not lost: the exact gap-order classification proves that every physical weak order lies in the closure of at least one of those ten strict order cones.

For a fixed order

\[
x_a\le x_b\le x_c\le x_d\le x_e,
\]

the existing 2/5 threshold theorem forces ranks 1 and 2 onto the low secant

\[
x_{k+2}+x_{k+3}\le {2\over3}+{x_k\over3},
\]

and ranks 4 and 5 onto the high secant

\[
x_{k+2}+x_{k+3}\le {1\over2}+{3x_k\over4}.
\]

The median can lie on either side of 2/5. Instead of branching on that bit here, use the exact convex hull of the two median branches. Besides the four rank-forced secants, its two new facets are

\[
5x_b+7x_c+4x_d\ge6+x_a,
\]

\[
8x_b+13x_c+9x_d\ge12.
\]

These inequalities are valid only with the order retained. The verifier does exactly that.

## Global exclusion test

For one generic H6 cell, start with the committed 85-variable complete-angle system. For a physical face `v`, test each of the ten closed gap-order cones after adding the four rank-forced secants and the two median-hull facets above.

If all ten order branches are impossible for the same face, then no physical pentagon can realize that face, so the entire H6 cell is impossible.

The exhaustive discovery scan inspected 88,514 order-branch LPs before early exit on live branches. It found 716 cells with a one-face obstruction. Their witness-face census is

```text
face 2    377
face 3     94
face 4    122
face 6     61
face 7     62
```

Faces 1 and 5 are not needed as the first witness for any of these 716 cells. This is only a census fact, not a theorem about those labels.

## Exact certification

`verify_target_c_support7_h6_order_hull_reduction_2026_09_19.py` reconstructs the previous 5,692-cell endpoint, performs the order scan, and exactifies every branch used in an exclusion.

For each of the 716 excluded cells, all ten order branches at the witness face have a rational Farkas certificate. Thus the reduction contains

\[
716\cdot10=7160
\]

exact branch certificates.

The certificate form is as follows. The original complete-angle facets are strict, with nonnegative multipliers `alpha` normalized by

\[
\sum\alpha_i=1.
\]

The order/secant/hull facets are closed, with nonnegative multipliers `beta`. Equality multipliers are unrestricted. A certificate is accepted only when the weighted variable coefficients cancel exactly over `fractions.Fraction` in all 85 variables and the remaining forced constant is nonpositive. Since the normalized strict contribution is strictly positive while the closed contribution is nonnegative, such an identity is impossible for a feasible branch.

Among the 7,160 accepted certificates, 5,863 have a strictly negative forced constant and 1,297 force exactly zero. The largest denominator among the accepted rational dual coefficients is 16,088. Floating-point LP output only proposes a dual; no branch is excluded from a floating-point sign alone.

## Scope

This does not prove that any of the remaining 4,976 cells is geometrically realizable. It only removes 716 cells by a necessary physical-pentagon condition.

The local median convex hull is deliberately weaker than retaining the median side as a second disjunction. Therefore the immediate next exact layer is the full 20-branch local split per face: ten physical orders times low/high median. Any cell killed there gives another rational one-face certificate without requiring a seven-face Cartesian enumeration.

After exhausting one-face branching, the next stronger finite layer is multi-face branch-and-bound: retain compatible order/median branches on several physical pentagons simultaneously and prune partial assignments with exact Farkas certificates. Cells surviving the linear disjunctive layer still require the non-affine reciprocal metric constraints, especially the fifteen independent sine-law consistency equations. Reciprocal-collinearity walls remain outside this generic branch.
