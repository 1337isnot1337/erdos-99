> Generated reading edition · [exact source](../../research/target_c_fan_inactive_deep_layer_2026-10-02.md) · source SHA-256 `68eb750a1157c2a0de5e8e3b6367974f9f81cb92f287d7a01e64606ef5ceb6b3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "7f8530a394fb7aa8648762ebc586106a81b7f246", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_fan_inactive_deep_layer_2026-10-02.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "3f5f63b778483522e24ad66c67016617a748502c169a28259c150637a4858b0d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: low outer-walk excess forces fan-inactive points into a deep loaded-hull layer

**Date:** 2026-10-02  
**Base main:** \`ace8036408dc62e4a5d27231cbc038343a43eda0\`  
**Status:** proof-only source-level reduction. Level I and C-II remain open.

## 1. Purpose and conclusion

Let $B$ be the canonical loaded actual-diameter endpoint set and
$$
F:=\operatorname{conv}(B).
$$
Retain
$$
q=|B|,
\qquad
P_F=\operatorname{per}(F),
\qquad
x_B=b_{\rm out}-q.
$$

Canonical Section 63 gives the exact nonnegative split
$$
x_B=(P_F-q)+(b_{\rm out}-P_F).
\tag{1}
$$
It also proves that if $m$ is the number of nonunit sides of the loaded polygon
$F$, then
$$
m\le x_B.
\tag{2}
$$

This note proves a boundary-layer statement that is stronger than the earlier
half-unit estimate for the present low-$x_B$ branch.

### Theorem 1.1 — $\sqrt3/2$ shallow-layer bound

Let
$$
Y_{\rm sh}:=
\left\{
y\in A\cap(F\setminus B):
\operatorname{dist}(y,\partial F)<{\sqrt3\over2}
\right\}.
$$
Then
$$
\boxed{
|Y_{\rm sh}|<15x_B.
}
\tag{3}
$$

Every source point
$$
y\in F,
\qquad
\operatorname{dist}(y,\partial F)\ge{\sqrt3\over2},
$$
has the full-source diameter margin
$$
\boxed{
|y-z|\le D-{\sqrt3\over2}
\qquad
(z\in A).
}
\tag{4}
$$

Consequently, combine (3) with the current exact fan-flip theorem
$$
\#\{y:\deg_H(y)=0\}
\ge
{I\over12},
\qquad
I\ge
\lceil D\rceil-(4K_\nu+2K_x)\sqrt D
\tag{5}
$$
in the branch
$$
\nu(H)\le K_\nu\sqrt D,
\qquad
x_B\le K_x\sqrt D.
\tag{6}
$$
All fan-produced inactive points in (5) lie inside $F$. Hence at least
$$
\boxed{
{I\over12}-15x_B
}
\tag{7}
$$
of them have loaded-hull boundary depth at least $\sqrt3/2$, and therefore satisfy
the fixed upper-distance margin (4).

In particular,
$$
\boxed{
\#\left\{
y:\deg_H(y)=0,\ 
\operatorname{dist}(y,\partial F)\ge{\sqrt3\over2}
\right\}
\ge
(1/12-o(1))D.
}
\tag{8}
$$

Thus the low-$x_B$, square-root-matching fan branch does not merely contain a
linear population of diameter-inactive points. Almost all of that forced population
lies a fixed positive Euclidean depth inside the loaded hull and has a fixed positive
margin from every global diameter constraint.

No computation is used.

## 2. Nonunit loaded-hull sides have total length at most $2x_B$

Write the loaded hull sides cyclically as
$$
s_i:=|b_i-b_{i+1}|,
\qquad i=1,\ldots,q.
$$
Unit separation gives
$$
s_i\ge1.
$$

Put
$$
U_F:=P_F-q=\sum_i(s_i-1).
\tag{9}
$$
By (1),
$$
0\le U_F\le x_B.
\tag{10}
$$

Let
$$
\mathcal N:=\{i:s_i>1\},
\qquad
m=|\mathcal N|.
$$
Canonical Section 63 gives (2). Since the remaining $q-m$ sides have length
exactly one,
$$
\sum_{i\in\mathcal N}s_i
=
P_F-(q-m)
=
U_F+m.
$$
Therefore
$$
\boxed{
\sum_{i\in\mathcal N}s_i\le2x_B.
}
\tag{11}
$$

This exact estimate is the only global loaded-hull input needed below.

## 3. A point shallower than $\sqrt3/2$ must project to a nonunit side

Fix
$$
y\in A\cap(F\setminus B)
$$
with
$$
d:=\operatorname{dist}(y,\partial F)<{\sqrt3\over2}.
\tag{12}
$$

Choose a nearest boundary point $w\in\partial F$.

The point $w$ cannot be a loaded vertex. If $w=b_i\in B$, then
$$
|y-b_i|=d<1,
$$
contradicting source unit separation.

Hence $w$ lies in the relative interior of one hull side $b_ib_{i+1}$.
Let
$$
s:=|b_i-b_{i+1}|,
$$
and let $t\in(0,s)$ be the distance along that side from $b_i$ to the orthogonal
projection $w$. Then
$$
|y-b_i|^2=t^2+d^2,
\qquad
|y-b_{i+1}|^2=(s-t)^2+d^2.
\tag{13}
$$

Suppose this hull side were a unit side, $s=1$. Unit separation from both endpoints
would give
$$
t\ge\sqrt{1-d^2},
\qquad
1-t\ge\sqrt{1-d^2}.
$$
Adding,
$$
1\ge2\sqrt{1-d^2},
$$
so
$$
d\ge{\sqrt3\over2},
$$
contrary to (12).

Therefore every point in $Y_{\rm sh}$ has a nearest boundary point on a nonunit
loaded-hull side.

This is the sharp local threshold for a unit segment: at depth exactly
$\sqrt3/2$, the equilateral location is possible.

## 4. Tube packing proves the $15x_B$ bound

Put
$$
r_0={\sqrt3\over2},
\qquad
\rho_0=r_0+{1\over2}={1+\sqrt3\over2}.
\tag{14}
$$

Around every point of $Y_{\rm sh}$, place the closed disk of radius $1/2$.
The interiors of these disks are disjoint by source unit separation.

By Section 3, the center of each such disk is at distance $<r_0$ from one of the
nonunit sides. Hence the entire radius-$1/2$ disk lies in the
$\rho_0$-neighborhood of that side.

The $\rho_0$-neighborhood of a segment of length $s$ has area
$$
2\rho_0s+\pi\rho_0^2.
$$
Taking the sum of these capsule areas is an upper bound on the area of their union.
Using (2) and (11),
$$
|Y_{\rm sh}|{\pi\over4}
\le
2\rho_0\sum_{i\in\mathcal N}s_i
+
\pi\rho_0^2m
\le
\left(4\rho_0+\pi\rho_0^2\right)x_B.
$$
Thus
$$
|Y_{\rm sh}|
\le
\left(
{16\rho_0\over\pi}+4\rho_0^2
\right)x_B.
\tag{15}
$$

The coefficient is
$$
{8(1+\sqrt3)\over\pi}+(1+\sqrt3)^2
=
14.42\ldots<15.
$$
For a rational check, $\pi>3$ and $\sqrt3<7/4$ give
$$
{8(1+\sqrt3)\over\pi}+(1+\sqrt3)^2
<
{22\over3}+{121\over16}
=
{715\over48}
<15.
$$
This proves (3).

No smoothness of $F$ and no restriction on the number of nonunit sides is used.

## 5. Deep loaded-hull points have a fixed global diameter margin

Let
$$
y\in F,
\qquad
d_F:=\operatorname{dist}(y,\partial F)\ge r
$$
for some $r>0$.

Because $F$ is convex,
$$
\overline B(y,r)\subseteq F.
\tag{16}
$$

Let $z\in A$ be any source point. Since
$$
F\subseteq K:=\operatorname{conv}(A),
$$
and the convex hull $K$ has the same diameter $D$ as the source, every two points
of $K$ are at distance at most $D$.

If $z\ne y$, put
$$
y':=
y+r{y-z\over|y-z|}.
$$
Then $y'\in F\subseteq K$, and
$$
|y'-z|=|y-z|+r\le D.
$$
Therefore
$$
\boxed{|y-z|\le D-r.}
\tag{17}
$$

Taking
$$
r={\sqrt3\over2}
$$
gives (4).

This is a full-source statement: $z$ may be loaded, unloaded, or contact-isolated.

## 6. Composition with the linear fan-inactive theorem

The current exact fan-flip theorem proves that under (6) there are at least
$$
{I\over12}
$$
distinct diameter-inactive source vertices produced by the exact fan geometry, with
$I$ as in (5).

Every such vertex lies strictly inside a triangle whose vertices are loaded actual
diameter endpoints:

- a degree-three third-contact port lies in
  $$
  \operatorname{int}\operatorname{conv}\{a,p_-,p_+\};
  $$
- a degree-two flip blocker lies in the same type of triangle.

Hence every one of these inactive points belongs to
$$
A\cap(F\setminus B).
$$

At most $15x_B$ of them can lie in $Y_{\rm sh}$. Therefore the number at boundary
depth at least $\sqrt3/2$ is at least
$$
\boxed{
N_{\rm deep}
\ge
{I\over12}-15x_B.
}
\tag{18}
$$

Substituting (5)--(6),
$$
\boxed{
N_{\rm deep}
\ge
{\lceil D\rceil\over12}
-
\left(
{K_\nu\over3}
+
{91K_x\over6}
\right)\sqrt D.
}
\tag{19}
$$

Thus
$$
N_{\rm deep}=(1/12-o(1))D.
$$

Every one of these points satisfies
$$
|y-z|\le D-{\sqrt3\over2}
\qquad(z\in A)
\tag{20}
$$
by Section 5.

## 7. Refined consequences in the two fan subbranches

The same shallow-layer estimate sharpens both sides of the current fan split.

### 7.1 Degree-three-heavy side

If
$$
T\ge I/2,
$$
the current third-contact theorem gives at least $T/5$ distinct diameter-inactive
positive-contact ports. Hence at least
$$
\boxed{
{T\over5}-15x_B
\ge
{I\over10}-15x_B
}
\tag{21}
$$
of those actual-contact ports have loaded-hull depth at least $\sqrt3/2$.

They are therefore nonisolated unloaded points with a fixed global diameter margin.

### 7.2 Degree-two-heavy side

If
$$
U\ge I/2,
$$
the current fan-flip theorem supplies $U$ distinct selected almost-unit blocker
edges
$$
py,
\qquad
1<|p-y|\le1+{1\over D},
$$
where $p\in B$ is a loaded diameter leaf and $y$ is diameter-inactive.

For $D\ge9$, the full near-unit graph has maximum degree at most six. Since there
are fewer than $15x_B$ shallow inactive vertices, at most
$$
90x_B
$$
of the selected blocker edges can have a shallow inactive endpoint.

Therefore at least
$$
\boxed{
U-90x_B
}
\tag{22}
$$
selected blocker edges have their inactive endpoint at depth at least
$\sqrt3/2$.

A greedy matching in a degree-six graph loses at most eleven edges per selected
matching edge, so these deep blocker edges contain a vertex-disjoint matching of
size at least
$$
\boxed{
{U-90x_B\over11}.
}
\tag{23}
$$

Under $U\ge I/2$ and $x_B=O(\sqrt D)$,
$$
\boxed{
\nu_{\rm deep,near}
\ge
(1/22-o(1))D.
}
\tag{24}
$$

Every inactive endpoint in this matching has the global upper-distance margin
$$
D-{\sqrt3\over2}.
$$

Thus the degree-two-heavy branch now carries a linear disjoint almost-contact matching
whose inactive endpoints are uniformly protected from the diameter constraint.

## 8. Frontier effect and exact remaining obstruction

The low-$x_B$, square-root-matching branch has now acquired a genuinely interior
linear population:
$$
(1/12-o(1))D
$$
diameter-inactive source points at loaded-hull depth at least $\sqrt3/2$.

This is stronger than the canonical Section-80 statement
$n-m=o(D^2)$: a merely subquadratic invisible population could have been diffuse
and arbitrarily close to the loaded hull. The fan geometry instead forces a linear
population at a fixed physical depth.

The two realizations remain different.

1. **Positive-contact realization.**  
   In the degree-three-heavy subbranch, a linear population of deep inactive points
   already lies in canonical unloaded harmonic components and enters the
   attachment-incidence machinery.

2. **Almost-contact realization.**  
   In the degree-two-heavy subbranch, there is a linear vertex-disjoint family
   $$
   1<|p-y|\le1+1/D
   $$
   from loaded fan leaves to deep diameter-inactive points.

The canonical deep inactive-pair theorem requires both endpoints of an isolate pair
to lie at depth $>1$, so it does not directly close the second realization:
the loaded endpoint $p$ lies on $\partial F$, and the sharp unit-side threshold
here is only $\sqrt3/2$.

The next closing obligation is therefore specific:

> exploit a linear family of loaded-to-deep-inactive inverse-$D$ pairs with a
> fixed upper-distance margin, or show that their inactive endpoints must enter
> enough positive-contact harmonic structure to trigger the attachment-cell branch.

No pair-closing feasibility, macroscopic inactive chamber, strict sub-$D$ source,
C-II closure, or Level I closure is claimed.

**Disposition:** exact proof-only geometric strengthening. No numerical search,
verifier execution, CI output, or unexecuted certificate code is used.
