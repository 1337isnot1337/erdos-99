# Target C support-seven H6: interior radial-order restriction

Date: 2026-09-19

Status: exact geometric necessary condition inside the generic H6 branch. The theorem-state authority is unchanged. C-II remains open.

## Statement

Let the reciprocal convex hull be

\[
0,1,2,3,4,5
\]

in cyclic order, with reciprocal interior vertices `6,7`. Fix `v in {6,7}`. From the ground hull vertex `0`, the generic ray `0v` lies strictly between two consecutive visible non-ground hull rays `0a` and `0b`, where

\[
1\le a<b\le5,
\qquad b=a+1.
\]

Write

\[
\rho_i=|y_i-y_0|.
\]

Then

\[
\boxed{
\rho_v<\max(\rho_a,\rho_b).
}
\tag{1}
\]

Equivalently, using the metric angle-difference variables from `target_c_support7_metric_radius_order_2026-09-19.md`,

\[
D_{ij}:=\angle 0ij-\angle 0ji,
\qquad
\operatorname{sgn}D_{ij}=\operatorname{sgn}(\rho_j-\rho_i),
\]

we have the exact two-branch disjunction

\[
\boxed{
D_{av}<0\quad\text{or}\quad D_{bv}<0.
}
\tag{2}
\]

This holds independently for `v=6` and `v=7`.

## Proof

Because `a,b` are consecutive visible hull vertices around `0`, the polygon edge `ab` is the boundary edge met by every ray from `0` whose direction lies strictly between `0a` and `0b`. The generic reciprocal interior point `v` lies on one such ray and strictly inside the convex hull. Therefore the ray from `0` through `v` meets the segment `ab` at a point `q` strictly beyond `v`:

\[
\rho_v<|q|.
\tag{3}
\]

Write

\[
q=(1-t)y_a+t y_b,
\qquad 0<t<1,
\]

after translating `y_0` to the origin. Since the two hull rays are distinct, `y_a` and `y_b` are not positive collinear. Strict triangle inequality gives

\[
|q|
< (1-t)|y_a|+t|y_b|
\le \max(|y_a|,|y_b|).
\tag{4}
\]

Combining (3) and (4) proves (1). The sign identity for `D` then gives (2).

This proof uses only convexity, strict interiority, and generic noncollinearity. It does not use the equilateral-pentagon equations.

## Where the bracketing hull vertices come from

The generic H6 state representation stores the seven rays from `0` in strict angular order. Removing interior labels `6,7` leaves

```text
1,2,3,4,5
```

in that order. Hence for each interior label `v`, the nearest hull label before `v` and the nearest hull label after `v` in the ground raw order are automatically a consecutive pair `(a,a+1)` with `a in {1,2,3,4}`. No geometric reconstruction is required to identify the branch.

## Reduction of the radius-order disjunction

The metric radius-order theorem gives a covering disjunction of `7! = 5040` closed total-order cones for the seven non-ground radii. Condition (1) removes every strict order in which an interior vertex is later than both of its bracketing hull endpoints.

Let `s_6,s_7 in {1,2,3,4}` denote the ground hull slots, so the bracketing pairs are `(s_6,s_6+1)` and `(s_7,s_7+1)`. Exhaustive exact enumeration of the 5040 strict radius orders gives:

```text
|s6-s7|    permitted strict orders
0          2520 = 1/2 * 5040
1          2352 = 7/15 * 5040
2 or 3     2240 = 4/9 * 5040
```

Thus before any nonlinear sine magnitude is used, the H6 interiority information removes between one half and five ninths of the naive strict radius orders.

This strict-order count is also a valid closed-cone cover when equal radii occur. Any realizable weak radius order satisfies (1) strictly for each interior point, so at least one bracketing hull endpoint has strictly larger radius than that interior point. Every linear extension that respects weak-radius levels therefore places that endpoint later; in particular a permitted strict linear extension exists. Hence it is safe to search only the permitted closed total-order cones.

## Cheaper two-branch test

The full radius-order enumeration is not necessary for a first cut. For one interior vertex `v`, every realization lies in the union

\[
\{D_{av}\le0\}
\cup
\{D_{bv}\le0\}.
\tag{5}
\]

The realized inequality is actually strict, but the two closed halfspaces cover it. Therefore if the current affine/physical system has an exact Farkas contradiction on both branches in (5), the entire generic H6 cell is impossible.

This gives a two-LP discovery test and two exact rational certificates per witness interior point. It is substantially cheaper than testing 5040 radius orders or the fifteen nonlinear sine identities.

The two interior vertices can also be coupled: every realization lies in one of four closed branch products obtained by selecting one bracketing endpoint for `6` and one for `7`. If no single interior point supplies a two-branch contradiction, exactifying all four products is the next natural strengthening.

## Scope

The result applies only to generic H6 reciprocal cells with `6,7` strictly interior and no reciprocal collinearity. It does not resolve reciprocal-collinearity walls or other reciprocal hull types. It is a necessary metric/interiority restriction, not a complete realization theorem.

Finite certificate: `research/verify_target_c_support7_h6_interior_radius_order_2026_09_19.py`.
