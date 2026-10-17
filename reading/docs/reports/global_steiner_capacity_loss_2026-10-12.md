> Generated reading edition · [exact source](../../../docs/reports/global_steiner_capacity_loss_2026-10-12.md) · source SHA-256 `80e31ee8ee8c6d7434148a8ec5d2fe7439a31495a07a19b9c79724690a5a3213`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E46DE5394D85","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Steiner symmetrization can lose exact packing capacity

**Date:** 2026-10-12
**Base:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`
**State version:** `2026-10-10.audit.234`
**Target:** global container comparison, retaining the entire population
**Classification:** exact regressions; report unreviewed
**Level I status:** open

For a compact container `K`, let `N(K)` be its maximum unit-separated point
count. Steiner symmetrization replaces each horizontal section by the centered
interval of the same length. Its geometric diameter reduction is not a
same-cardinality packing construction. The missing proposed bridge is
`N(S K)>=N(K)`. The following exact examples disprove that bridge, including
a small actual global diameter minimizer and an unbounded high-density
triangle-free family of exact fixed-container optima.

They do not disprove an eventual theorem restricted to large global diameter
minimizers. In particular fixed-container optimality is not global diameter
optimality.

## 1. A four-label global-minimizer regression

Take the unit square rotated by the rational unit direction `(4/5,3/5)`:

```math
P=\{(-7/10,-1/10),(-1/10,7/10),
      (7/10,1/10),(1/10,-7/10)\}.
```

Its minimum distance is one, diameter squared is two, and contact graph is
a four-cycle. It is a global minimizer for four labels.

For completeness, every four-label unit-separated planar source has diameter
at least `sqrt(2)`: in the convex-quadrilateral case, an angle is at least
90 degrees, so the chord between its two adjacent vertices has squared length
at least two by the cosine rule. If one point is strictly inside the triangle
of the others, two rays at that point make an angle at least 120 degrees and
the corresponding outer pair has squared length at least three. A point on
a hull edge gives a collinear pair with an intervening unit-separated point,
so its diameter is at least two; lower-dimensional cases are also immediate.
The square attains `sqrt(2)`.

Its convex hull has area one. The symmetrized hull is the hexagon

```math
S K=\operatorname{conv}\{(0,\pm7/10),(\pm5/8,\pm1/10)\}.
```

The notation includes all four independent sign choices in the latter term.
The section widths are zero at `y=+-7/10`, `5/4` at `y=+-1/10`, constant
between those middle levels, and linear in each end interval. This verifies
the symmetrization exactly. The area remains one, while the maximum squared
vertex distance is `49/25<2`. Consequently `N(S K)<=3` by the four-point
bound. The sites `(0,7/10)`, `(-5/8,-1/10)`, `(5/8,-1/10)` are all mutually
more than unit distance apart, so `N(S K)=3`. The original hull has capacity
exactly four (also directly from Oler's bound below). Thus

```math
\boxed{N(K)=4>3=N(S K)}
```

even for a triangle-free actual global diameter minimizer. This finite
regression does not settle the eventual Level I quantifier.

## 2. Unbounded quadratic population with exact fixed-container optimality

For any integer `m>=20`, put

```math
t=\tfrac12-\frac1{m^2},\qquad h=\sqrt{1-t^2},\qquad
u=(4/5,3/5),\qquad
v=((4t-3h)/5,(3t+4h)/5).
```

These are unit vectors with `u dot v=t<1/2`. Use the actual source

```math
P_m=\{iu+jv:0\le i,j\le m,\ i,j\in\mathbb Z\},
\qquad K_m=\operatorname{conv}P_m.
```

There are `n=(m+1)^2` labels. Every squared source distance is
`a^2+b^2+2tab` for an integer pair `(a,b)`. If `ab>=0`, this is at least
`a^2+b^2`. If `ab<0`, it equals
`(|a|-|b|)^2+2(1-t)|ab|>1`. Thus the only unit contacts are coordinate
neighbors: the actual contact graph is the bipartite square grid and has
no unit triangle.

The rhombus hull has perimeter `4m` and area `hm^2`. With `a0=sqrt(3)/2`,

```math
1<\frac h{a_0}
=\sqrt{1+\frac4{3m^2}-\frac4{3m^4}}
\le1+\frac2{3m^2}.
```

Canonical Oler Lemma 21.1 gives

```math
N(K_m)\le(h/a_0)m^2+2m+1
\le(m+1)^2+2/3.
```

The count is integral and the explicit source attains `(m+1)^2`, so
`N(K_m)=(m+1)^2` exactly. Its point count per container area tends to the
Thue constant `1/a0`. No attainment or stress assumption is hidden here.

Write `b=v_y=(3t+4h)/5`. We have `3/5<b<=1`. The centered symmetrized
rhombus is a hexagon with top and bottom heights `+-m(b+3/5)/2`, middle
heights `+-m(b-3/5)/2`, and middle half-width `mh/(2b)`. This follows by
taking its horizontal sections; the constant middle width is `mh/b`.
Its perimeter is exactly

```math
\operatorname{per}(S K_m)
=2m(b-3/5)+4m\sqrt{(h/(2b))^2+(3/5)^2}.
```

For `m>=20`, `14h<=27t`: squaring reduces this to
`196<=925t^2`, which holds already at `t=199/400` and improves thereafter.
Equivalently `h/(2b)<=9/20`. Thus

```math
\operatorname{per}(S K_m)
\le 2m(1-3/5)+4m(3/4)=19m/5.
```

The symmetrized hull still has area `hm^2`. Applying Oler again yields

```math
N(S K_m)\le m^2+\tfrac23+\tfrac{19}{10}m+1
=n-\frac m{10}+\frac23.
```

Therefore

```math
\boxed{N(K_m)-N(S K_m)\ge
\left\lceil\frac m{10}-\frac23\right\rceil.}
```

This is an unbounded loss, linear in source diameter and in `sqrt(n)`.
The original unit-separated source labels cannot all be repacked into the
symmetrized body, even though the source is triangle-free, its container
capacity is exactly optimal, and its area density tends to the optimal
planar packing density.

### Source/container/diameter distinction

These rhombus sources are **nonglobal for diameter**. Their squared diameter
is `2m^2(1+t)=3m^2-2`. Fundamental-cell lattice averaging gives
`D(n)^2<=4a0 n/pi<(6/5)n`, which is strictly below `3m^2-2` for `m>=20`.
The family is not a Level I counterexample, and its normalized hull is not
the disk limit of global minimizers. The regression kills capacity
preservation based on triangle-freeness, fixed-container optimality, or
leading area density alone; it leaves a large-global-source theorem open.

## 3. Exact computation and frontier effect

Run `python3 research/verify_global_steiner_capacity_loss_2026_10_12.py`.
The script uses rational arithmetic for the square, symmetrized hexagon,
section widths, areas, and all diameter comparisons. It checks the rhombus
upper-bound inequalities by squaring positive quantities; no floating roots
are used. For `m=20,40,100`, it certifies original capacities `441,1681,10201`
and symmetrized upper capacities `439,1677,10191`. It independently enumerates
all 97,020 source pairs at `m=20` and the 840 actual contacts. The analytical
argument, not the finite enumeration, establishes every `m>=20`.

The only non-elementary dependency is canonical Oler Lemma 21.1 in
[`../theory/03-oler-shell.md`](../theory/03-oler-shell.md). No external theorem
or unpromoted report is imported. Preserve this as an unreviewed regression;
no theorem-state promotion has occurred.

The exact global obligation is still a same-cardinality strict-sub-`D`
competitor for every sufficiently large triangle-free global minimizer.
Symmetrizing its convex hull cannot be substituted for a certified full-label
repacking theorem. The capacity step needs actual global-source information
beyond the hypotheses defeated here.

## Autonomous audit (2026-10-15)

The [PR #959 AI audit](../audits/pr959_autonomous_proof_audit_2026-10-15.md)
records the full proof scope and computational repairs. This remains a
noncanonical artifact; the destination's independent exact-head AI-agent mathematical audit has not been completed. Claims remain unreviewed and unpromoted.
