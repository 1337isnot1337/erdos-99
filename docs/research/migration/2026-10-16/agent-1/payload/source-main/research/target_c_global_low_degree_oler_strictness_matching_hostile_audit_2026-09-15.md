# Hostile audit — global low-degree Oler strictness and near-contact matching

**Date:** 2026-09-15
**Reviewed:** `research/target_c_global_low_degree_oler_strictness_matching_2026-09-15.md`
**Verdict:** `PASS`, with the uniform-gap argument sharpened below.
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The candidate globalizes the previous degree-5/6 residual theorem. The load-bearing claim is that a bounded chamber has strictly positive Oler residual whenever every pair other than a consecutive boundary side is strictly longer than one. That claim survives audit.

## 1. The chamber residual is exactly the Oler functional

Canonical bounded-face convexity gives a simple convex unit-edge polygon of degree `d`. If `z` assigned contact-isolated source points lie in the chamber, the chamber source count is `N=d+z` and the perimeter is `d`. Thus

\[
r={2A\over\sqrt3}+{d\over2}+1-N,
\]

which is exactly the Folkman–Graham/Oler slack. Residual conservation sums these nonnegative chamber residuals without duplication.

## 2. A longest triangulation edge enters Folkman–Graham Case III

Triangulate all chamber source points, preserving the chamber boundary, and choose a triangulation of minimum total edge length as in Folkman–Graham. Boundary edges have length one. A degree-`d>=5` chamber has internal triangulation edges. Under the candidate hypothesis every internal edge is a hidden pair and hence has length `>1`.

Choose a longest triangulation edge `sigma`, of length `d0>1`. It is internal. Its two incident triangles form a convex quadrilateral `Q`. Every side of `Q` is a triangulation edge and hence has length at most `d0`. The other diagonal has length at least `d0`; otherwise flipping `sigma` to that diagonal would shorten total triangulation length. Therefore every diagonal of `Q` is at least every side, and every side is at least one. This is exactly the hypothesis of Folkman–Graham Lemma 2 / Case III.

## 3. Equality in Lemma 2 is impossible when `d0>1`

Use the notation from their proof. Split `Q` along `sigma`. Let `theta,theta'` be the two opposite angles and `(s,t)`, `(s',t')` the adjacent side pairs. Their argument gives

\[
\theta,\theta'\in[\pi/3,2\pi/3],
\qquad \theta+\theta'\le\pi,
\]

and

\[
\Phi(Q):={4A(Q)\over\sqrt3}-P(Q)+2
\ge (s-1)(t-1)+(s'-1)(t'-1)\ge0.
\]

If equality held, then `sin(theta)=sin(theta')=sqrt(3)/2`, and at least one side in each adjacent pair would equal one.

Suppose `theta=pi/3` and, without loss, `s=1`. By the cosine law,

\[
d_0^2=1+t^2-t.
\]

Because `d0>=t`, this implies `t<=1`; since `t>=1`, `t=1` and then `d0=1`, contradiction. Hence `d0>1` forces `theta=2pi/3`. The same argument forces `theta'=2pi/3`, contradicting `theta+theta'<=pi`.

Therefore

\[
\boxed{\Phi(Q)>0}
\]

whenever the longest internal triangulation edge is strictly longer than one. Folkman–Graham Case III inserts this positive local slack into the induction, so the chamber Oler residual is strictly positive.

## 4. Uniformity at fixed degree and fixed hidden-distance margin

The candidate invoked compactness of chamber configurations. That is valid, but an even safer uniform argument is available directly at the Case-III quadrilateral.

Fix `r` and `eta>0`. If every hidden pair has length at least `1+eta`, then the chosen longest internal edge satisfies `d0>=1+eta`. All points of a degree-`d<=r` chamber lie in a convex polygon of perimeter `d`, so the chamber diameter is at most `d/2<=r/2`. Thus every side and diagonal of `Q` lies in a fixed compact metric interval.

On the compact set of Case-III quadrilaterals satisfying

- sides at least one;
- both diagonals at least every side;
- selected diagonal at least `1+eta`;
- diameter at most `r/2`;

`Phi(Q)` is continuous and, by Section 3, has no zero. Hence it has a strictly positive minimum `phi_r(eta)`. The Case-III induction therefore gives a uniform positive chamber residual gap `c_r(eta)>0`.

This avoids any concern about degenerate limiting chamber triangulations or variable numbers of assigned interior points.

## 5. The universal degree-22 population is sufficient

The hostile-audited low-degree staircase gives

\[
F_{\le22}/D>0.0057-o(1)
\]

for every Type-II sequence, because `t<=pi+o(1)` and the degree-22 positivity threshold exceeds `pi`.

If `R_F=o(D)`, the uniform residual gap from Section 4 implies that, for every fixed `eta>0`, only `o(D)` of those chambers can have all hidden pairs at least `1+eta`. Diagonalizing `eta` produces `(0.0057-o(1))D` chambers with one selected inactive pair of length `1+o(1)`.

## 6. The factor-nine endpoint matching is valid

A positive-contact boundary vertex belongs to at most `deg_C(v)<=5` bounded face boundaries. An assigned contact-isolated source point belongs only to its assigned chamber. Hence one source vertex is an endpoint of at most five selected pair occurrences.

The occurrence multigraph has maximum degree at most five. One selected pair conflicts with at most eight other pair occurrences, so greedy selection retains at least one ninth. The exact outward arithmetic gives

\[
F_{\le22}/D>0.0057223373\ldots,
\qquad
|M_D|/D>0.0006358152\ldots>0.00063.
\]

Every selected pair is inactive: a nonconsecutive unit pair among boundary vertices would be a contact chord and split the face, while an assigned contact-isolated point has no unit contact.

## 7. Scope

The theorem does not activate the matching simultaneously and does not upper-bound `R_F`. Its legitimate conclusion is the global Type-II fork

```text
linear R_F along a subsequence
or
linear endpoint-disjoint inactive matching at distance 1+o(1).
```

No upper restriction on `t` is required.

**Final verdict:** PASS at proof-only full-core Type-II scope. C-II remains open.
