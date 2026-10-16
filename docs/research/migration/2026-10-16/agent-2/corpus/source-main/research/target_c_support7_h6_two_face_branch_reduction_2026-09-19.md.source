# Target C: partial two-face generic H6 reduction to 4,910 cells

Date: 2026-09-19

Status: exact finite reduction inside the generic H6 branch. The theorem-state authority is unchanged. C-II remains open.

## Result

The exact one-face adaptive-branch endpoint is

\[
4944=3940\,C_7+1004\,(C_3\sqcup C_4).
\]

Combining the same 20-way physical-pentagon branch description at two faces excludes 34 more cells:

\[
\boxed{4944\longrightarrow4910}
\]

with

\[
\boxed{4910=3914\,C_7+996\,(C_3\sqcup C_4).}
\]

This is a partial two-face scan, not a claim that two-face branching has been exhausted. The 34 cells come from the first 100 cells of the 4,944-cell endpoint. The purpose of this step is to turn the first strong pair-face signal into exact certificates before extending the scan to the rest of the endpoint.

The 34 exclusions split by ground pattern as

```text
235    1
245    7
256   19
345    2
346    1
356    4
```

and by missing graph as

```text
C7       26
C3+C4     8
```

The resulting current pattern census is

```text
145      4
156     16
235    673
236   1282
237     16
245    477
256   1263
345     22
346    483
347      4
356    670
```

These counts sum to 4,910.

## Two-face covering argument

At one physical pentagon face, the local necessary-condition system has 20 closed branches: ten admissible cyclic gap orders times the two closed median sides. Each branch includes the five exact rank-specific closure secants from the branch-adaptive pentagon theorem.

Fix two physical faces `a,b`. There are 400 branch products. It is not necessary to solve all 400 as two-face systems. First exact-certify every locally impossible branch at `a` and `b`. Any branch product containing one of those branches is already impossible. Only products of locally surviving branches need a genuine two-face certificate.

For each of the 34 cells in this reduction, every one of the 400 branch products is covered in one of those two ways. Therefore no simultaneous physical realization of the chosen two faces exists, so the entire generic H6 cell is impossible.

The witness face-pair census is

```text
faces 2,3   16
faces 2,7   11
faces 2,6    5
faces 2,4    2
```

Face 2 appearing in every witness is an observation about this first scanned block, not a theorem about all remaining H6 cells.

## Exact certificate audit

`verify_target_c_support7_h6_two_face_branch_reduction_2026_09_19.py` records the 34 cells by their position in the committed 5,692-cell complete-angle endpoint and independently checks their state indices, missing-graph types, and ground patterns. It also checks that each cell survives the previous exact order-hull reduction and is not one of the 32 one-face adaptive exclusions.

The complete covering proof uses 2,491 exact rational Farkas certificates:

```text
one-face certificates used       929
two-face product certificates   1562
total                           2491
```

Of these, 2,390 force a strictly negative constant and 101 force exactly zero. The largest denominator among active exact dual coefficients is

\[
3575688275930909083760258.
\]

As in the preceding reductions, numerical LPs are used only to find candidate dual supports. A certificate is accepted only after an exact `fractions.Fraction` solve and exact checks that:

- strict and closed inequality multipliers are nonnegative;
- the original strict-facet weights sum to one;
- all 85 variable coefficients cancel exactly;
- equality multipliers are unrestricted;
- the forced constant is nonpositive.

Thus the logical exclusion does not rely on floating-point infeasibility.

## Validation performed in this run

The 32-cell one-face exactifier was rerun from scratch data and again returned 32/32 exact exclusions, zero failures, and 640 valid branch certificates.

For the two-face layer, the 34 candidate cells were exactified in six independent chunks. All 34 passed with zero certificate failures. Across those chunks the totals were exactly 929 one-face certificates and 1,562 two-face certificates, with 2,390 negative forced values, 101 zero forced values, and the denominator maximum quoted above.

The repository-level verifier reconstructs the committed finite state census rather than depending on the scratch pickle/cache files used to accelerate this research run. Its logic mirrors the successful exact chunk checks.

## Next target

The pair-face attack is clearly productive, but only the first 100 of 4,944 cells have been screened to completion here. The immediate next job is to run the same adaptive two-face search over the remaining endpoint, prioritizing face pairs with the smallest products of locally surviving branches, exactify every candidate, and update the census in batches.

The useful pruning rule is exact branch coverage, not blind enumeration: locally dead branches remove whole rows or columns of the 20-by-20 product table before any two-face LP is solved. This keeps the finite search manageable and generalizes directly to three or more faces if needed.

After multi-face affine branching stops producing useful reductions, surviving cells still have to satisfy the fifteen independent complete reciprocal sine-law metric consistency equations. Reciprocal-collinearity walls remain a separate nongeneric branch.
