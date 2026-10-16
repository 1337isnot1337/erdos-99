# Target C-II — orbit-pure flat teeth force unloaded centers and a brace/hidden-pair dichotomy

**Date:** 2026-09-15  
**Repository base:** branch `research/c2-orbit-routing-sol-20260915` after the residual-free flat-tooth theorem  
**Status:** proof-only structural strengthening; theorem-state authority unchanged  
**Scope:** full-core Type-II survivor subsequence with `t=(q-k)/D<=1.826`  
**LEVEL I STATUS:** `STILL OPEN`

The preceding theorem gives

\[
P_{5,\mathrm{pure}}
\ge0.4106157004\ldots D-o(D)
\]

orbit-pure pentagons, each converging to the flat subdivided equilateral trapezoid.

For each such tooth let `m` be its almost-flat base midpoint.  Then:

1. distinct good teeth have distinct flat centers for all sufficiently large sources;
2. only `o(D)` flat centers are loaded force-hull vertices;
3. every remaining flat center is unloaded and has at least one extra unit contact outside its pentagon;
4. if a chosen extra contact has train phase in the dominant shrinking orbit windows, it creates an additional hidden noncontact of length `1+o(1)`;
5. otherwise the chosen edge lies on a non-dominant brace train.

Hence, up to `o(D)`, at least `0.4106157D` distinct unloaded flat centers split between two source-level currencies:

```text
additional hidden near-unit pairs
or
off-orbit brace incidences.
```

This is a weight-free geometric statement.

## 1. Contact rays are separated by more than sixty degrees

At any contact-core vertex `v`, two distinct unit-contact neighbors `x,y` satisfy

\[
|x-y|=2\sin(\angle xvy/2)\ge1.
\]

Therefore

\[
\angle xvy\ge\pi/3.
\]

Equality would make `vxy` a unit equilateral triangle, forbidden in the hypothetical survivor. Thus

\[
\boxed{
\angle xvy>\pi/3
}
\tag{FB.1}
\]

for every two distinct contact rays at one vertex.  In particular the global contact degree is at most five.

## 2. One vertex cannot center two sufficiently flat teeth

At the flat center `m` of a good tooth, the bounded-face interior angle tends to `pi`.
Choose the flatness neighborhood so every good-center face angle exceeds `5pi/6`.

Suppose an unloaded vertex centered two distinct good teeth.  Bounded face sectors are sectors between consecutive contact rays.  The two tooth sectors would contribute more than

\[
2\cdot{5\pi\over6}={5\pi\over3}
\]

to the full angular sum.  Since an unloaded core vertex has degree at least three, there is at least one further sector between consecutive contact rays; by (FB.1) that sector has angle greater than `pi/3`.  The total would exceed `2pi`, impossible.

A loaded force-hull vertex lies on the outer face.  If it has degree two, at most one of its two sectors is bounded.  If it has degree at least three, the same `5pi/6+5pi/6+pi/3>2pi` argument applies.

Therefore, for all sufficiently large sources,

\[
\boxed{
\text{the flat-center map from good teeth to source vertices is injective.}
}
\tag{FB.2}

Consequently there are at least

\[
0.4106157004\ldots D-o(D)
\tag{FB.3}

**distinct** flat centers.

## 3. Loaded flat centers are negligible

Let `m` be a loaded flat center.  Then `m` is a vertex of the convex loaded force hull `F_D`.
The bounded tooth sector at `m` lies inside the tangent cone of `F_D` at `m`.  Its opening is `pi-o(1)`, while the tangent-cone opening is at most `pi`.  Therefore both boundary rays of the tangent cone differ by `o(1)` from the two almost-opposite tooth base rays.

The tooth base projective direction lies in the dominant shrinking three-axis orbit windows.  Hence at least one of the two force-hull sides incident to `m` has projective direction in a slightly enlarged shrinking union of the same three windows.

Assign to each loaded flat center one such incident hull side.  One hull side is assigned by at most its two endpoints.  Every force-hull side has Euclidean length at least one because all source points are unit-separated.  Thus

\[
\#\{\text{loaded flat centers}\}
\le
2\sum_{\substack{\text{hull sides }e\\\operatorname{dir}(e)\in W_D}}
|e|,
\tag{FB.4}
\]

where `W_D` is a union of three projective windows whose total angular width tends to zero.

Type-II near-disk perimeter-measure convergence gives

\[
{1\over D}\sum_e |e|\,\delta_{\operatorname{dir}(e)}
\Longrightarrow d\theta
\]

on the projective direction circle.  Choose the same standard diagonal subsequence used for the shrinking atomic windows.  Then the normalized perimeter mass of `W_D` tends to zero.  Equation (FB.4) yields

\[
\boxed{
\#\{\text{loaded flat centers}\}=o(D).
}
\tag{FB.5}

Combining (FB.3)--(FB.5),

\[
\boxed{
\#\{\text{unloaded flat centers}\}
\ge0.4106157004\ldots D-o(D).
}
\tag{FB.6}

## 4. Every unloaded flat center has an extra contact

Canonical C26 gives contact degree `3`, `4`, or `5` at every unloaded core vertex.  The good tooth uses exactly two contact edges at its flat center, namely the two almost-opposite base edges.  By center injectivity there is only one centered tooth there.

Hence every unloaded flat center has at least one additional unit-contact edge not on the pentagon boundary.

Choose one such edge `mx` at each unloaded flat center.

## 5. A dominant-orbit extra contact creates another hidden near-edge

Rotate so the tooth majority/base projective axis tends to angle zero.  The two base contact rays tend to directed angles `0` and `pi`, and the bounded face occupies one of the two half-plane sectors between them.

The chosen extra contact ray lies outside that face sector.  By (FB.1) it stays at angular separation strictly greater than `pi/3` from each base ray.  In the flat limit its directed angle therefore belongs to

\[
[4\pi/3,5\pi/3]
\]

up to reversing the orientation convention, and its projective direction belongs to the interval between the two minority orbit axes.

If the train phase of `mx` lies in the dominant shrinking orbit windows, it cannot converge to the majority axis.  It must converge to one of the two minority axes.  Therefore the angle between `mx` and the adjacent base edge tends to exactly `pi/3` from above.

Let `y` be the endpoint of that adjacent base edge.  Since

\[
|m-x|=|m-y|=1,
\]

the law of cosines gives

\[
|x-y|
=2\sin\left({\angle xmy\over2}\right)
=1+o(1).
\tag{FB.7}
\]

The pair `xy` is not an old contact: if `|x-y|=1`, the three unit edges `mx,my,xy` would form a forbidden equilateral triangle.  Hence

\[
\boxed{|x-y|>1,\qquad |x-y|=1+o(1).}
\tag{FB.8}

Thus every chosen **dominant-orbit** extra brace creates an additional hidden near-unit pair.

## 6. Dichotomy

Partition the unloaded flat centers into

- `A_D`: centers whose chosen extra edge belongs to the dominant shrinking orbit windows;
- `N_D`: centers whose chosen extra edge lies outside those windows.

Equation (FB.6) gives

\[
\boxed{
|A_D|+|N_D|
\ge0.4106157004\ldots D-o(D).
}
\tag{FB.9}

Every center in `A_D` yields a hidden near-unit noncontact by (FB.8).  Every center in `N_D` yields a selected contact incidence on a non-dominant stopped train.

Therefore at least one alternative holds:

\[
\boxed{|A_D|\ge0.2053078D-o(D)}
\tag{FB.10}
\]

or

\[
\boxed{|N_D|\ge0.2053078D-o(D).}
\tag{FB.11}
\]

In the first branch the hidden-pair graph has maximum degree at most five: an endpoint can participate only through one of its at most five contact neighbors serving as the corresponding flat center.  A greedy edge matching therefore extracts at least

\[
{|A_D|\over9}
\ge0.0228119D-o(D)
\tag{FB.12}
\]

endpoint-disjoint **additional** hidden `1+o(1)` pairs.

In the second branch there are at least

\[
{|N_D|\over2}
\ge0.1026539D-o(D)
\tag{FB.13}

 distinct selected off-orbit contact edges, since one physical edge has only two endpoints.

## 7. What remains

The off-orbit brace branch is not yet a train-count theorem: one stopped train can contain many selected parallel edges.  However the bounded-endpoint purity theorem already says that only `0.07561D+o(D)` **bounded terminal incidences** may belong to non-dominant trains.  Consequently any proof that converts a fixed fraction of the selected off-orbit brace edges into distinct train variables would immediately force a linear outer-to-outer train family and invoke audited two-sided diameter bracing.

The hidden-pair branch is equally concrete: it supplies a new endpoint-disjoint near-active matching on top of the two hidden tooth diagonals already extracted in the preceding theorem.

The surviving closure target is therefore no longer local pentagon geometry.  It is one of:

1. an occupancy bound converting off-orbit brace edges to distinct stopped trains;
2. a simultaneous activation/deformation theorem for the hidden near-unit matching; or
3. a stress theorem ruling out a linear population of asymptotically weak braces at unloaded flat centers.

**Disposition:** proof-only structural strengthening. C-II and Level I remain open.
