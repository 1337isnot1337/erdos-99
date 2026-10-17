# Target C-II — `g=0.0071` reflection / long-side / blocker normal form

**Date:** 2026-09-15  
**Repository base:** `767d480d6036344bde979ecab9999833566cc9c8`  
**Status:** proof-only full-core Type-II geometric reduction; theorem-state authority unchanged  
**Scope:** fully force-visible no-container/full-core Type-II branch  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Current main has the hostile-audited matched atomic gap

\[
C_{71}=2\sqrt{\Delta_2}+0.0071,
\qquad
\Delta_2={\pi\over2\sqrt3},
\]

and the safe low-`t` floor

\[
t:={q-k\over D}\ge1.84323-o(1).
\]

This note rebases the support-reflection route onto that current scalar frontier and
keeps the physical information that the scalar train argument does not record.

Fix

\[
\beta_0={\pi\over6}-10^{-4}.
\]

Let

\[
L_{>2}:=\sum_{s_i>1}(s_i-2)_+
\]

be the total literal length of consecutive loaded-force-hull sides beyond two.
Let `B_beta` count distinct nonunit loaded sides for which one can select an internal
`beta`-straight Section-63 route vertex `x`, of support depth at most `1/2`, together
with an actual source point `y` satisfying

\[
|x-y|>D-1.
\]

Then at the current safe endpoint every survivor satisfies the physical alternative

\[
\boxed{
B_{\beta_0}\ge0.1929093045D-o(D)
}
\tag{R71.1}
\]

or

\[
\boxed{
L_{>2}\ge0.1430972650D-o(D).
}
\tag{R71.2}

The blocker branch has additional structure.  It contains at least

\[
\boxed{
0.04822732613D-o(D)
}
\tag{R71.3}

**distinct physical unloaded contact-core vertices** `x`, every one of contact degree
three or four, each with a source point farther than `D-1`.  No single source point
can be the blocker for a positive fraction of the selected sides:

\[
\boxed{
\max_y r_D(y)=o(D),
}
\tag{R71.4}

where `r_D(y)` is the number of selected loaded sides using blocker `y`.
Consequently the selected `D-1` pairs contain a vertex-disjoint matching whose size
tends to infinity.

The scalar support-reflection tradeoff remains positive up to

\[
\boxed{
1.8569406450521027102\ldots,
}
\tag{R71.5}

so it stays informative through most of the present low-`t` window.

---

## 1. Exact route energy and straight-side selection

For consecutive loaded vertices `b_i,b_{i+1}`, let

\[
s_i=|b_i-b_{i+1}|,
\qquad
W_i:b_i=x_{i,0},x_{i,1},\ldots,x_{i,\ell_i}=b_{i+1}
\]

be the distinguished Section-63 outer route.  Canonical Section 67 and the audited
pocket identification make every nonunit route the complementary chain of one simple
convex augmented pocket.

Let `e_i` be the chord direction and let `v_{i,j}` be the unit route-edge vectors.
The exact route directional energy is

\[
d_{out}:=b-\operatorname{per}(F)
=\sum_{i,j}(1-v_{i,j}\cdot e_i).
\tag{R71.6}

A route edge whose principal angle from `e_i` is at least `beta` costs at least
`1-cos beta`.  Hence the number of nonunit sides on which no internal vertex lies
between two `beta`-good adjacent route edges is at most

\[
{d_{out}\over1-\cos\beta}.
\tag{R71.7}

Choose one `beta`-straight internal vertex on every remaining nonunit side.

---

## 2. Support projection and depth losses

Use side coordinates `a=(0,0), b=(s,0)` with force hull in the inward half-plane.
For the oriented route let `c_j` be the horizontal component of edge `j`.  If `P,N`
are positive and negative horizontal variations, then

\[
P-N=s,
\]

while every negative increment pays at least twice its magnitude in (R71.6).  Thus
`N<=d_i/2` on route `i`.  Clipping horizontal coordinates to `[0,s]` shows that
selected straight vertices whose perpendicular projection falls outside the side can
be charged injectively to positive variation outside the interval.  Therefore

\[
N_{outside}(\beta)
\le {d_{out}\over2\cos\beta}.
\tag{R71.8}

For a remaining selected vertex with support depth `h>1/2`, the two route subpaths
from the side endpoints have total length at least `sqrt(s^2+1)`.  Hence its route
cost is at least

\[
f(s):=\sqrt{s^2+1}-s.
\]

The function `f` is positive, decreasing and convex.  If `M_deep` distinct selected
sides are deep, their total side length is at most `per(F)<=pi D`, so Jensen gives

\[
\boxed{
M_{deep}
\le\sqrt{d_{out}(d_{out}+2\pi D)}.
}
\tag{R71.9}

---

## 3. Support-line reflection produces a `D-1` blocker or an exterior isolate

Take a retained shallow selected vertex

\[
x=(p,h),\qquad 0\le p\le s,\qquad0<h\le1/2,
\]

and reflect it through the loaded side line:

\[
x^-=(p,-h).
\]

For every source point `w=(r,q)`,

\[
\boxed{|w-x^-|^2-|w-x|^2=4hq.}
\tag{R71.10}

Every positive-core point lies in `F`, hence in the inward half-plane, so no old
positive contact incident to `x` becomes shorter.  At least one old contact becomes
strictly longer: an internal route neighbor has positive support height; if both route
neighbors are the loaded side endpoints, C26 supplies a third positive-height contact.

If some source point lies within unit distance of `x^-`, original unit separation and
(R71.10) force it into the exterior half-plane.  If no strict unit blocker and no
diameter violation exists, the reflected source remains unit-separated with diameter
at most `D` while losing an old contact.  Diameter minimality and the contact-minimal
tie-break then force a new unit contact, and (R71.10) again puts its source point in
the exterior half-plane.  Such a point is contact-isolated in the canonical source.

The other possibility is a source point `y` with

\[
|y-x^-|>D.
\]

Then `y` lies on the inward side and, because `|x-x^-|=2h<=1`,

\[
\boxed{|x-y|>D-1.}
\tag{R71.11}

---

## 4. Exterior reflection witnesses occur on only `o(D)` selected sides

For an exterior witness `z=(u,-r)` with `|z-x^-|<=1`, the shallow condition
`h<=1/2`, old endpoint separation, and the witness inequality imply

\[
0<u<s.
\tag{R71.12}

Thus the perpendicular foot of `z` lies in the relative interior of the selected
loaded side and is the unique Euclidean projection of `z` onto `F`.  The same exterior
point cannot witness two distinct loaded sides.

For every fixed `beta<pi/6`, compactness plus triangle freeness gives a fixed witness
depth `r_beta>0`: otherwise a witness could approach the support line, and in the
limit its unit ray from `x` would lie within `pi/6` of a tangent direction while an
adjacent `beta`-good route contact lies within `beta` of the same tangent direction.
Their angle would be below `pi/3`, violating unit separation/triangle freeness.

Canonical Section 77 makes every loaded diameter endpoint an extreme vertex of the
full source hull `K` and decomposes `K\setminus F` into disjoint exterior caps over
consecutive loaded sides.  A witnessed selected side of length `s` has cap
arc-minus-chord cost at least

\[
\sqrt{s^2+4r_\beta^2}-s.
\]

Convexity/Jensen and total selected side length at most `pi D` yield, for `M_ext`
witnessed selected sides,

\[
\operatorname{per}(K)-\operatorname{per}(F)
\ge
\sqrt{(\pi D)^2+4r_\beta^2M_{ext}^2}-\pi D.
\tag{R71.13}

Type II has `per(F)=pi D-o(D)` and `per(K)<=pi D`, so

\[
\boxed{M_{ext}=o(D).}
\tag{R71.14}

All but `o(D)` retained shallow selected sides therefore lie in the `D-1` blocker
branch.

---

## 5. Eliminate the unknown nonunit-side count

Let `m_B` be the number of nonunit loaded sides and let `u_B=x_B-m_B` be the exact
Section-63 integer slack.  Sections 1--4 give

\[
B_\beta
\ge m_B
-{d_{out}\over1-\cos\beta}
-{d_{out}\over2\cos\beta}
-\sqrt{d_{out}(d_{out}+2\pi D)}
-o(D).
\]

Adding `u_B=x_B-m_B` cancels `m_B` exactly:

\[
\boxed{
 u_B+B_\beta
 \ge x_B
 -{d_{out}\over1-\cos\beta}
 -{d_{out}\over2\cos\beta}
 -\sqrt{d_{out}(d_{out}+2\pi D)}
 -o(D).
}
\tag{R71.15}

Normalize

\[
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\delta={d_{out}\over D}.
\]

Type-II perimeter convergence gives

\[
{x_B\over D}=\pi+\delta-t-\kappa+o(1).
\]

The current `g=0.0071` network envelope is

\[
2\delta+{\kappa\over2}
\le R_{71}(t):={9t\over2}-2\pi-C_{71}.
\tag{R71.16}

At fixed `t,delta`, (R71.15) is weakest at the largest feasible `kappa`.  After that
substitution its derivative in `delta` is negative for `beta=beta_0`, so the weakest
point is

\[
\boxed{
\kappa=0,
\qquad
\delta={R_{71}(t)\over2}.
}
\tag{R71.17}

Define

\[
\mathcal L_\beta(\delta)
={\delta\over1-\cos\beta}
+{\delta\over2\cos\beta}
+\sqrt{\delta(\delta+2\pi)}
\]

and

\[
G^{71}_\beta(t)
:=\pi+{R_{71}(t)\over2}-t
-\mathcal L_\beta\!\left({R_{71}(t)\over2}\right).
\tag{R71.18}

The Decimal certificate gives

\[
G^{71}_{\beta_0}(1.84323)
=0.38581860911632497\ldots,
\tag{R71.19}

so

\[
B_{\beta_0}\ge0.19290930455816248D-o(D)
\]

or the same lower bound holds for `u_B`.

The exact integer route theorem gives

\[
0\le u_B-L_{>2}\le d_{out}.
\tag{R71.20}

At the weakest endpoint point

\[
\delta
={R_{71}(1.84323)\over2}
=0.0498120395462494157\ldots,
\]

hence the `u_B` branch yields

\[
L_{>2}
\ge
(0.19290930455816248-0.04981203954624941)D-o(D),
\]

which is (R71.2).

The first zero of (R71.18) is (R71.5).

---

## 6. Straight selected tails have degree three or four

At a `beta`-straight internal vertex let `tau` be the forward turn of the convex
pocket chain.  The two adjacent edge directions are both within `beta` of the loaded
chord and convexity gives

\[
0\le\tau<2\beta.
\]

The pocket interior angle is `pi-tau`, so every non-route contact ray lies in the
complementary core-side sector of size

\[
\pi+\tau<\pi+2\beta<{4\pi\over3}.
\]

Distinct unit contact-neighbor rays are separated by strictly more than `pi/3`:
equality would create a forbidden unit equilateral triangle.  Three non-route
neighbors would require four such gaps between the two route rays, totaling more than
`4pi/3`.  Therefore there are at most two non-route neighbors.

Loaded internal-route exclusion makes the selected vertex unloaded; C26 gives the
lower contact-degree bound.  Hence

\[
\boxed{3\le\deg_C(x)\le4.}
\tag{R71.21}

One physical vertex has at most its degree many occurrences on one facial boundary
walk.  Thus one selected physical tail can account for at most four selected loaded
sides.  The blocker alternative therefore contains at least

\[
{0.19290930455816248\over4}D-o(D)
=0.04822732613954062D-o(D)
\]

distinct physical unloaded tails, proving (R71.3).

---

## 7. One blocker cannot serve a positive fraction of the selected sides

Let `c_D` be Type-II near-disk centers.  Canonical Type II gives

\[
D^{-1}(F-c_D)\to B(0,1/2)
\]

in Hausdorff distance.  Because `F\subset K=conv(A)` and `diam(K)<=D`, the same center
also gives

\[
D^{-1}(K-c_D)\to B(0,1/2).
\tag{R71.22}

Indeed the near-radius-`D/2` inball in `F` supplies, opposite any source-hull point,
a point whose distance would exceed `D` if the source-hull radius exceeded
`D/2+o(D)`.

Thus every pair with distance `>D-1` is uniformly asymptotically antipodal about
`c_D`.  The selected tail is within `1/2` of its loaded support side, and the support
number of every loaded side is `D/2+o(D)` uniformly.  Cauchy--Schwarz therefore shows
that the loaded-side normal is `o(1)` from the radial direction of the selected tail.

Consequently, all selected sides blocked by one fixed source point `y` have normals in
one angular window of radius `rho_D->0` centered at the antipodal radial direction to
`y`.

The normalized loaded-side perimeter measure

\[
\mu_D={1\over D}\sum_i s_i\,\delta_{n_i}
\]

converges to Lebesgue measure `dtheta` on the projective direction circle.  Since the
limit is nonatomic, this convergence is uniformly nonatomic on shrinking windows:

\[
\sup_\theta\mu_D(B(\theta,\rho_D))\to0.
\tag{R71.23}

Every loaded side has length at least one, so the number `r_D(y)` of selected sides
blocked by `y` satisfies

\[
{r_D(y)\over D}
\le\mu_D(B(\theta_y,\rho_D)).
\]

Taking the supremum proves (R71.4).

---

## 8. Near-diameter matching consequence

Deduplicate the blocker side family to the distinct physical unloaded tails from
Section 6 and choose one blocker for each tail.  This gives `Omega(D)` physical
`D-1` pairs.  Passing to a simple graph loses at most a factor two, because one
unordered pair can be generated from at most its two endpoints.

Each tail generates only one chosen edge.  By (R71.4), blocker-role degree is `o(D)`
uniformly.  Hence this near-diameter graph has `Omega(D)` edges and maximum degree
`o(D)`.  Greedy edge deletion gives a matching of size at least

\[
{|E|\over2\Delta-1}\to\infty.
\]

Every matched pair has an unloaded positive-contact-core endpoint, so it is not an
actual diameter edge at that endpoint.

---

## 9. Frontier effect

At the current `g=0.0071` frontier, every low-`t` full-core Type-II survivor therefore
has one of two concrete physical obstructions:

```text
REFLECTION / NEAR-DIAMETER BRANCH
    >= 0.1929093 D distinct loaded sides with D-1 blockers;
    >= 0.0482273 D distinct unloaded degree-3/4 shallow route vertices;
    blocker reuse is o(D);
    an unbounded vertex-disjoint matching of D-1 pairs follows;

ROUNDED LONG-SIDE BRANCH
    L_{>2} >= 0.1430973 D-o(D)
    of literal consecutive loaded-hull side length beyond two.
```

Neither branch is closed.  The first requires promotion of distributed near-diameter
pairs into KKT/diameter-thrackle or deformation currency.  The second requires a
geometric obstruction to a linear rounded long-side boundary in the near-disk
positive core.  Abstract Woodall caterpillar topology alone is known to be
insufficient.

The result is intentionally source-level and does not request theorem-state promotion.
