# Target C-II — global matching of signed straight-event penetrations

**Date:** 2026-09-15  
**Status:** proved proof-only strengthening; theorem-state authority unchanged  
**Scope:** current low-`t` full-core Type-II endpoint  
**LEVEL I STATUS:** `STILL OPEN`

The current straight-event stack produces more than `1.154D` distinct `15`-degree
signed inward contacts, but a priori many could terminate at the same core vertex.
Low outer detour rules out that concentration.

The key local-to-global observation is quantitative. If two outer straight vertices
are within bounded Euclidean distance, then the inward normals of their associated
loaded-hull sides differ by only about `0.003` radians: any macroscopic normal
difference would separate the two hull-side midpoints by `Theta(D)` and would force
`Theta(D)` outer-route detour. Consequently, at one common endpoint, all incoming
signed penetration directions lie in a cone of width only slightly more than `90`
degrees. Triangle-freeness requires more than `60` degrees between any two contact
rays, so at most two penetration edges can share an endpoint.

Moreover a signed penetration cannot terminate at another `15`-degree-straight outer
vertex. Hence the all-extra penetration graph is bipartite, with degree at most two on
both sides, and contains a matching of at least half its edges.

At the current endpoint this gives

\[
\boxed{
M_{15}\ge0.57715584605858637\ldots D-o(D)
}

pairwise vertex-disjoint unit contacts, each pointing inward by more than
`1/sqrt(2)` relative to its associated loaded-hull side normal.

Combining with the rhombic-train support theorem also gives a vertex-disjoint matching
of at least

\[
\boxed{
0.11903971156372519\ldots D-o(D)
}

such contacts that lie on non-singleton strict-rhombus trains.

---

## 1. Normal-closeness lemma for nearby outer-route vertices

Let `x` be an internal occurrence on distinguished route `W_i`, and `y` an internal
occurrence on `W_j`. Let `n_i,n_j` be the corresponding loaded-hull inward normals,
`M_i,M_j` the midpoints of the loaded-hull sides, and `d_i,d_j` the individual route
detours.

The signed penetration theorem already proves the route-midpoint estimates

\[
|x-M_i|\le s_i+{d_i\over2},
\qquad
|y-M_j|\le s_j+{d_j\over2},
\tag{PM.1}
\]

where

\[
\max_r s_r=o(D).
\tag{PM.2}
\]

Suppose

\[
|x-y|\le C
\]

for one fixed constant `C`. Then

\[
|M_i-M_j|
\le s_i+s_j+C+{d_i+d_j\over2}.
\tag{PM.3}
\]

Type-II near-disk geometry gives, uniformly in the side indices,

\[
|M_r-o_D|={D\over2}+o(D)
\]

and aligns the radial direction at `M_r` with `-n_r` up to `o(1)`. If

\[
\theta_{ij}:=\angle(n_i,n_j)\in[0,\pi],
\]

then the chord formula and (PM.3) give

\[
D\sin{\theta_{ij}\over2}
\le {d_i+d_j\over2}+o(D).
\tag{PM.4}
\]

Since `d_i+d_j<=d_out`, writing `delta=d_out/D`,

\[
\boxed{
\sin{\theta_{ij}\over2}
\le {\delta\over2}+o(1).
}
\tag{PM.5}
\]

At the current endpoint

\[
\delta\le0.002883975+o(1),
\]

so any two bounded-distance outer-route occurrences satisfy

\[
\boxed{
\theta_{ij}
\le
2\arcsin(0.0014419875)+o(1)
<0.0028841+o(1).
}
\tag{PM.6}
\]

This is less than `0.166` degrees. The important point is not the decimal: it is far
below the `30`-degree margin needed below.

---

## 2. At most two signed penetrations can share one endpoint

Fix `beta=pi/12`. Let

\[
x_1w,\ldots,x_rw
\]

be distinct extra contacts from `15`-degree-straight outer occurrences `x_a`, all
terminating at the same physical vertex `w`. Put

\[
e_a=w-x_a,
\qquad |e_a|=1,
\]

and let `n_a` be the loaded-hull inward normal associated to the occurrence at `x_a`.

Every pair `x_a,x_b` is at distance at most two through `w`. Applying (PM.5) with
`C=2`, all normals `n_a` lie within

\[
\varepsilon_D
:=2\arcsin(\delta/2)+o(1)
\tag{PM.7}
\]

of one another.

The signed straight-event estimate gives

\[
\boxed{e_a\cdot n_a>{1\over\sqrt2}.}
\tag{PM.8}
\]

Thus every `e_a` lies within angle `<pi/4` of `n_a`. Relative to one fixed normal,
all `e_a` therefore lie in an angular interval of width at most

\[
{\pi\over2}+2\varepsilon_D.
\tag{PM.9}
\]

For sufficiently large `D`, (PM.6) makes this width strictly less than `2pi/3`.

At the common contact vertex `w`, the contact rays toward `x_a` are `-e_a`.
Triangle-freeness and unit separation require the smaller angular separation between
any two of these rays to be strictly greater than `pi/3`.

Three directions contained in an interval of width `<2pi/3` cannot have successive
separations both `>pi/3`. Therefore

\[
\boxed{r\le2.}
\tag{PM.10}
\]

### Theorem PM.1 — penetration endpoint multiplicity

Every physical vertex is the non-straight endpoint of at most two `15`-degree signed
extra contacts.

This uses no contact-weight lower bound and no train structure.

---

## 3. A penetration cannot terminate at another `15`-degree-straight vertex

Let `xw` be an extra contact at a `15`-degree-straight occurrence `x` on `W_i`, and
suppose for contradiction that `w` also supports a `15`-degree-straight occurrence on
`W_j`.

Since `|x-w|=1`, (PM.5)--(PM.6) make `n_i,n_j` asymptotically identical.
Put

\[
e=w-x.
\]

There are only two possibilities for the contact `xw` at the straight occurrence of
`w`.

### Case 1: `xw` is extra at `w`

Signed inwardness at the two endpoints gives

\[
e\cdot n_i>{1\over\sqrt2},
\qquad
(-e)\cdot n_j>{1\over\sqrt2}.
\]

Hence

\[
e\cdot(n_i-n_j)>\sqrt2,
\]

which is impossible when `|n_i-n_j|=o(1)` by (PM.6).

### Case 2: `xw` is a route edge at `w`

A route contact ray at a `15`-degree-straight occurrence is within `pi/12` of the
local tangent axis. Therefore

\[
|e\cdot n_j|<\sin(\pi/12).
\tag{PM.11}
\]

Normal closeness gives

\[
e\cdot n_i
\le
|e\cdot n_j|+|n_i-n_j|
<\sin(\pi/12)+0.003
<{1\over\sqrt2}
\]

for all sufficiently large `D`, contradicting signed inwardness at `x`.

Both cases are impossible. Hence

\[
\boxed{
\text{the other endpoint of a `15`-degree signed penetration is not a
`15`-degree-straight outer vertex.}
}
\tag{PM.12}
\]

This is stronger than edge-injectivity: the straight and nonstraight endpoint sets are
disjoint.

---

## 4. The all-extra penetration graph has maximum degree two

Let `L` be the set of distinct `15`-degree-straight outer vertices and let `R` be the
set of opposite endpoints of **all** extra contacts at vertices of `L`.

By (PM.12),

\[
L\cap R=\varnothing.
\tag{PM.13}
\]

Theorem DG.1 gives contact degree exactly three or four at each vertex of `L`, so its
number of extra contacts is exactly one or two. Hence the penetration graph

\[
G_{pen}=(L,R;E_{all,15})
\]

has left degree at most two. Theorem PM.1 gives right degree at most two. Therefore

\[
\boxed{\Delta(G_{pen})\le2.}
\tag{PM.14}
\]

It is a bipartite disjoint union of paths and even cycles. Its edges can be partitioned
into two matchings. Consequently

\[
\boxed{
\nu(G_{pen})\ge {E_{all,15}\over2},
}
\tag{PM.15}
\]

where `nu` is maximum matching size.

The near-simple signed degree/phase theorem gives

\[
{E_{all,15}\over D}
\ge1.1543116921171727469\ldots-o(1).
\]

Therefore

\[
\boxed{
{\nu(G_{pen})\over D}
\ge0.5771558460585863734\ldots-o(1).
}
\tag{PM.16}
\]

Every matching edge is a unit contact with signed inward component greater than
`1/sqrt(2)` relative to its associated hull-side normal, and the matching edges are
pairwise vertex-disjoint in the **physical contact graph**.

---

## 5. Rhombic-train penetration matching

Restrict `G_pen` to those penetration edges that lie on non-singleton strict-rhombus
trains. Deleting edges cannot increase either endpoint degree, so the restricted graph
still has maximum degree at most two and remains bipartite.

The train-support theorem gives

\[
{E_{R,15}\over D}
\ge0.2380794231274503948\ldots-o(1).
\tag{PM.17}
\]

Therefore its edge set contains a physical matching of size at least half:

\[
\boxed{
{M_{R,15}\over D}
\ge0.1190397115637251974\ldots-o(1).
}
\tag{PM.18}

Likewise, restricting first to simple-outer straight vertices and then to rhombic-train
penetrations, (TS.11) gives

\[
\boxed{
{M_{R,simp,15}\over D}
\ge0.0960714416082082916\ldots-o(1).
}
\tag{PM.19}

These are vertex-disjoint train-supported penetration families, not merely distinct
edges.

---

## 6. Why the matching matters

The current obstruction to a simultaneous deformation is edge reuse and endpoint
coupling. Equations (PM.16), (PM.18), and (PM.19) remove physical endpoint reuse on a
linear subfamily.

A closing argument can now work with at least `0.577D` disjoint two-vertex penetration
constraints, or with at least `0.119D` disjoint penetrations that are known to sit on
non-singleton rhombic trains. The remaining reuse can only occur at the level of

- a common stopped train containing several matching edges at different vertices;
- a common exceptional face adjacent to several tails; or
- a common diameter brace crossing several resulting train cuts.

The first of these is now the most concrete local target. A train carrying many edges
of the matching cannot hide them by endpoint multiplicity; it must physically traverse
many distinct boundary penetration sites.

No contradiction from that occupancy is claimed here.

**C-II remains open.**

---

## 7. Reproducibility

Run

```bash
python3 research/verify_target_c_global_signed_penetration_matching.py
```

for the displayed endpoint constants and the numerical normal-angle margin.
