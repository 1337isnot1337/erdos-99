# Target C — harmonic wrapping and near-disk cell-diameter audit

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module strengthens the Type-II harmonic-cell geometry after Sections 80, 82,
and 83. It also repairs a false premise in the old unreviewed near-circle cap reports.

Those reports used the assertion

> a subset of the radius-`1/2` circle with Euclidean diameter at most `mu<1` lies in
> one circular arc of angular length `2 asin(mu)`.

That assertion is false once `mu>=sqrt(3)/2`: three equally spaced circle points have
pairwise distance `sqrt(3)/2` and are not contained in any `120`-degree arc.
Therefore the old claimed endpoint `d_max/D -> 1` does not follow from cap geometry
alone.

The current harmonic framework supplies an extra ingredient that those reports did
not use. A harmonic cell of Euclidean diameter `d` has many distinct loaded
attachments. Canonical Section 62 and the loaded degree cap give

\[
|A_r|\ge {d_r+1\over3}.
\]

A circle-supported cell that wraps around the center but has diameter only slightly
above `sqrt(3)/2` can place its support only in six short boundary clusters. Near the
Type-II disk, unit separation bounds how many loaded attachments those clusters can
contain. Combining the two facts gives a new explicit threshold

\[
\boxed{
\mu_0=0.8896708101\ldots,
\qquad
{\mu_0\over3}=6\arcsin(\mu_0)-2\pi.
}
\]

The main result is

\[
\boxed{
\liminf {1\over D}\max_r\operatorname{diam}(P_r)\ge\mu_0
}
\]

in the Type-II branch. More strongly, there are harmonic cells `P_*` with

\[
\operatorname{diam}(P_*)\ge(\mu_0-o(1))D,
\qquad
\operatorname{area}(P_*)\ge c_*D^2
\]

for one absolute `c_*>0`, and these cells have local strict-rhombus filling fraction
`1-o(1)`. Thus Section 82 applies to an actual macroscopic carrier whose diameter is
at least `0.88967...D` asymptotically.

No contact-isolated source point is removed. The theorem is Type-II only.

---

# 88. Type II contains a macroscopic harmonic cell of diameter at least 0.88967 D

Work along a Type-II survivor sequence. Translate by the centers supplied by Section
80 and scale by `D`. Then

\[
D^{-1}F\to B_{1/2}
\tag{88.1}
\]

in Hausdorff distance. Section 83 gives pairwise interior-disjoint harmonic cells

\[
P_r=\operatorname{conv}(A_r)\subset F
\]

such that

\[
\boxed{
\sum_r\operatorname{area}(P_r)
=\operatorname{area}(F)-o(D^2)
={\pi D^2\over4}-o(D^2),
}
\tag{88.2}
\]

\[
\boxed{
\sum_r\operatorname{per}(P_r)
\le2\pi^2D+O(1),
}
\tag{88.3}
\]

and

\[
\boxed{
\sum_r
\bigl(\operatorname{area}(P_r)-A_{4,r}\bigr)
=o(D^2),
}
\tag{88.4}
\]

where `A_{4,r}` is the total area of unloaded-only strict-rhombus faces belonging to
component `I_r`.

For each cell put

\[
d_r:=\operatorname{diam}(P_r).
\]

## 88.1 Boundary arclength in an almost circular convex hull

The attachment-count argument needs a local boundary-length estimate.

### Lemma 88.1 — polar arc length in a thin annulus

Let a convex body `K` satisfy

\[
B(0,r)\subset K\subset B(0,R),
\qquad 0<r\le R.
\]

Parameterize `partial K` radially by polar angle. If `E` is a finite union of angular
intervals of total angular length `|E|`, then the corresponding boundary arcs have
total Euclidean length at most

\[
\boxed{{R^2\over r}|E|.}
\tag{88.5}
\]

### Proof

Write the radial graph as

\[
p(\phi)=\rho(\phi)e_\phi.
\]

The radial function of a convex body containing the origin is locally absolutely
continuous. At almost every differentiability point let `n` be the outward unit
normal. Since the inner disk lies in `K`,

\[
n\cdot p=h_K(n)\ge r.
\]

Also `rho<=R`, so

\[
n\cdot e_\phi\ge {r\over R}.
\]

For a radial graph,

\[
{ds\over d\phi}
={\rho\over n\cdot e_\phi}
\le {R^2\over r}.
\]

Integrate over `E`. The formula holds through the nonsmooth points by absolute
continuity. `square`

By (88.1), for every `epsilon>0` and all sufficiently large survivors,

\[
B\left(0,\left({1\over2}-\epsilon\right)D\right)
\subset F
\subset
B\left(0,\left({1\over2}+\epsilon\right)D\right).
\tag{88.6}
\]

Hence for angular sets of total length `L`, the corresponding force-hull boundary
length is

\[
\boxed{
\left({D\over2}+o(D)\right)L.
}
\tag{88.7}
\]

uniformly for every fixed finite number of angular intervals.

Consecutive loaded vertices on a force-hull boundary arc are source points at mutual
Euclidean distance at least one. Therefore an angular union of at most `M` intervals
and total length `L` contains at most

\[
\boxed{
\left({L\over2}+o(1)\right)D+M
}
\tag{88.8}
\]

loaded vertices.

## 88.2 Circle sets: cap type versus wrapping type

Let `S` be a compact subset of the radius-`1/2` circle and suppose

\[
\operatorname{diam}(S)=\lambda<1.
\]

Put

\[
\theta:=2\arcsin\lambda\in(0,\pi).
\tag{88.9}
\]

Any two points of `S` have minor angular separation at most `theta`.

Call `S` **cap type** if it is contained in an open semicircle. Otherwise call it
**wrapping**.

### Lemma 88.2 — cap-type support lies in one short arc

If `S` is cap type, then `S` is contained in one circular arc of angular length at
most `theta`.

### Proof

Unwrap the containing open semicircle to a real interval of length less than `pi`.
Within that interval chord length is strictly increasing with angular separation.
Every pair has separation at most `theta`, so the difference between the largest and
smallest lifted angles is at most `theta`. `square`

This elementary lemma remains valid for every `lambda<1`; the old reports failed only
because they applied it without first establishing the open-semicircle hypothesis.

### Lemma 88.3 — a wrapping set lies in six clusters

If `S` is wrapping, then necessarily `theta>=2pi/3`. Moreover there exist three points
`y_1,y_2,y_3 in S` such that every point of `S` lies in a union of at most six circular
arcs whose total angular length is

\[
\boxed{6\theta-4\pi.}
\tag{88.10}
\]

### Proof

Because `S` is not contained in an open semicircle, the origin lies in
`conv(S)`. Since `lambda<1`, `S` contains no antipodal pair. Caratheodory's theorem
therefore gives three points `y_1,y_2,y_3` whose triangle contains the origin in its
interior.

Put the three points in cyclic order and let their three circular gaps be

\[
g_1,g_2,g_3\in(0,\pi),
\qquad
g_1+g_2+g_3=2\pi.
\]

Every pair of anchors is in `S`, so

\[
g_i\le\theta
\qquad(i=1,2,3).
\]

Thus `3theta>=2pi`.

Consider the gap of length `g_1` from `y_1` to `y_2`. A point in this gap is already
within angular distance at most `theta` of `y_1` and `y_2`. To be within distance
`theta` of `y_3`, it must lie either

- within angular length `theta-g_3` of `y_1`, or
- within angular length `theta-g_2` of `y_2`.

These two endpoint intervals are disjoint because `theta<pi`; their total length is

\[
2\theta-g_2-g_3.
\]

Repeat in the other two gaps. The total allowed angular measure is

\[
\sum_{cyc}(2\theta-g_i-g_j)
=6\theta-2(g_1+g_2+g_3)
=6\theta-4\pi.
\]

Every member of `S` must lie in this allowed set because it is within angular
distance `theta` of all three anchors. `square`

At the sharp threshold `theta=2pi/3`, (88.10) collapses to zero: a wrapping set of
diameter `sqrt(3)/2` consists of the three equally spaced support points.

## 88.3 Harmonic attachment multiplicity forbids small wrapping cells

The preceding circle statement becomes quantitative for harmonic cells.

### Lemma 88.4 — wrapping harmonic-cell inequality

Let `P_j=conv(A_j)` be a sequence of harmonic cells in Type II such that

\[
{d_j\over D_j}\to\lambda<1,
\qquad
{A_j\over D_j}\to S
\]

in Hausdorff distance after passing to a subsequence of the finite attachment sets.
If the limiting support set `S` is wrapping, then

\[
\boxed{
{\lambda\over3}
\le
6\arcsin\lambda-2\pi.
}
\tag{88.11}
\]

### Proof

All loaded attachments lie on `partial F_j`. By the annular convergence (88.6), every
Hausdorff limit of `D_j^{-1}A_j` lies on the radius-`1/2` circle, and convex-hull
continuity gives

\[
D_j^{-1}P_j\to\operatorname{conv}(S).
\]

Apply Lemma 88.3 to `S`. Put `theta=2asin(lambda)`. Choose the three anchor points
there and attachment vertices converging to them. Since every pair of actual
attachments has distance at most `d_j=(lambda+o(1))D_j`, compactness implies that for
all sufficiently large `j` every attachment lies in an `o(1)` angular enlargement of
the six-cluster set from Lemma 88.3. Otherwise a violating subsequence would converge
to a point of `S` outside that allowed set.

Equations (88.8) and (88.10) therefore give

\[
\limsup { |A_j|\over D_j}
\le {6\theta-4\pi\over2}
=3\theta-2\pi
=6\arcsin\lambda-2\pi.
\tag{88.12}
\]

On the other hand canonical Section 62 gives, for the corresponding unloaded
component,

\[
t_j\ge\delta_j+3,
\qquad
d_j\le\delta_j+2.
\]

Thus

\[
t_j\ge d_j+1.
\]

Every loaded attachment has total positive-contact degree at most three, so
`t_j<=3|A_j|`. Hence

\[
\liminf {|A_j|\over D_j}
\ge{\lambda\over3}.
\tag{88.13}
\]

Combine (88.12)--(88.13). `square`

Define

\[
H(\lambda)
:=6\arcsin\lambda-2\pi-{\lambda\over3}.
\tag{88.14}
\]

On `[sqrt(3)/2,1)`,

\[
H'(\lambda)
={6\over\sqrt{1-\lambda^2}}-{1\over3}>0.
\]

Also

\[
H(\sqrt3/2)=-{\sqrt3\over6}<0,
\qquad
\lim_{\lambda\uparrow1}H(\lambda)=\pi-{1\over3}>0.
\]

Therefore there is a unique root

\[
\boxed{
\mu_0=0.889670810115\ldots
}
\tag{88.15}
\]

satisfying

\[
\boxed{
{\mu_0\over3}=6\arcsin\mu_0-2\pi.
}
\tag{88.16}
\]

Lemma 88.4 implies:

\[
\boxed{
\text{every wrapping harmonic-cell limit has diameter at least }\mu_0.
}
\tag{88.17}
\]

This is the harmonic improvement beyond the pure convex-cell threshold
`sqrt(3)/2=0.866025...`.

## 88.4 Capacity of cap-type disk cells

Fix `mu<1` and put

\[
\theta_\mu:=2\arcsin\mu<\pi.
\]

Consider a finite family of pairwise interior-disjoint positive-area convex sets

\[
Q_i=\operatorname{conv}(S_i)\subset B_{1/2},
\]

where every `S_i` is a compact circle subset of cap type and
`diam(Q_i)<=mu`.

By Lemma 88.2 choose for each `S_i` its minimal supporting circle arc `J_i`, of length
at most `theta_mu`. The arc endpoints belong to `S_i`, and the chord between them is a
supporting edge of `Q_i`.

### Lemma 88.5 — the support arcs are laminar

The arcs `J_i` are laminar: two of them are disjoint in their interiors or one is
contained in the other.

### Proof

All arc lengths are less than `pi`. If two arcs partially overlapped without
containment, their four endpoints would alternate around the circle. Their base chords
would cross properly. At that crossing each chord is a relative-interior point of a
supporting boundary edge of a positive-area convex set, and both convex sets lie on
the circular-cap side of their respective chord. The two selected half-planes overlap
in an open sector at the chord crossing. Consequently the interiors of the two convex
sets intersect near the crossing, contrary to the hypothesis. `square`

Take the inclusion-maximal support arcs. Their interiors are pairwise disjoint, so if
their angular lengths are `alpha_1,...,alpha_s`,

\[
0<\alpha_i\le\theta_\mu,
\qquad
\sum_i\alpha_i\le2\pi.
\tag{88.18}
\]

All cells whose support arcs lie below one maximal arc are contained in the circular
cap cut off by that maximal arc. Interior-disjointness therefore gives total cell
area at most the sum of the maximal cap areas.

For the radius-`1/2` disk, the cap cut off by an arc of angle `alpha` has area

\[
G(\alpha):={\alpha-\sin\alpha\over8}.
\tag{88.19}
\]

The function `alpha-sin(alpha)` is increasing and convex on `[0,pi]`. Thus under
(88.18) the cap-area sum is maximized by filling as many arcs as possible to
`theta_mu`, followed by one remainder. Put

\[
k_\mu:=\left\lfloor{2\pi\over\theta_\mu}\right\rfloor,
\qquad
r_\mu:=2\pi-k_\mu\theta_\mu\in[0,\theta_\mu).
\tag{88.20}
\]

Then every such cap-type family satisfies

\[
\boxed{
\sum_i\operatorname{area}(Q_i)
\le
\mathcal C(\mu)
:={1\over8}
\left[k_\mu(\theta_\mu-\sin\theta_\mu)
+r_\mu-\sin r_\mu\right].
}
\tag{88.21}
\]

Equivalently,

\[
\boxed{
\mathcal C(\mu)
={1\over8}
\left[2\pi-k_\mu\sin\theta_\mu-\sin r_\mu\right]
<{\pi\over4}
}
\tag{88.22}
\]

for every fixed `mu<1`.

## 88.5 Transfer the cap capacity to the Type-II harmonic cells

For fixed `mu<mu_0`, split the Type-II cells into

\[
\mathcal S_\mu(D):=\{r:d_r\le\mu D\},
\qquad
\mathcal L_\mu(D):=\{r:d_r>\mu D\}.
\tag{88.23}
\]

### Theorem 88.6 — short-cell area ceiling

For every fixed `mu<mu_0`,

\[
\boxed{
\limsup_{D\to\infty}
{1\over D^2}
\sum_{r\in\mathcal S_\mu(D)}
\operatorname{area}(P_r)
\le\mathcal C(\mu).
}
\tag{88.24}
\]

### Proof

Section 83 and isoperimetry give

\[
\sum_r\sqrt{\operatorname{area}(P_r)}=O(D).
\tag{88.25}
\]

Fix `eta>0`. Cells of area below `eta D^2` therefore carry only

\[
O(\sqrt\eta\,D^2)
\tag{88.26}
\]

total area. The remaining cells are finite in number, uniformly in `D` for fixed
`eta`.

Pass to a subsequence on which all of these macroscopic cells, and their finite
attachment sets in the Hausdorff hyperspace, converge after scaling by `D`. Every
attachment-set limit lies on the radius-`1/2` circle, and every cell limit is its
convex hull. Convex Hausdorff convergence preserves area and diameter. The positive
`eta` area floor also preserves nonempty interiors, so the limiting cells remain
pairwise interior-disjoint.

Every limiting short cell has diameter `lambda<=mu<mu_0`. By Lemma 88.4 it cannot be
wrapping. It is therefore cap type. Lemma 88.5 and the capacity bound (88.21) give

\[
\limsup {1\over D^2}
\sum_{\substack{r\in\mathcal S_\mu(D)\\
                 \operatorname{area}(P_r)\ge\eta D^2}}
\operatorname{area}(P_r)
\le\mathcal C(\mu).
\]

Now let `eta` tend to zero and use (88.26). `square`

Combining (88.2) and (88.24), define

\[
\Gamma(\mu):={\pi\over4}-\mathcal C(\mu)>0.
\tag{88.27}
\]

Then

\[
\boxed{
\liminf {1\over D^2}
\sum_{r\in\mathcal L_\mu(D)}
\operatorname{area}(P_r)
\ge\Gamma(\mu).
}
\tag{88.28}
\]

So a positive area fraction of the near-disk force hull lies in harmonic cells of
diameter larger than every fixed `mu<mu_0`.

## 88.6 One long cell is macroscopic and rhombus-saturated

Every convex body satisfies

\[
\operatorname{per}(P_r)\ge2d_r.
\]

Using the total perimeter bound (88.3),

\[
\boxed{
|\mathcal L_\mu(D)|
\le {\pi^2\over\mu}+o(1).
}
\tag{88.29}
\]

for every fixed `mu>0`. Equations (88.28)--(88.29) imply that one cell in
`mathcal L_mu(D)` has

\[
\boxed{
\operatorname{area}(P_r)=\Omega_\mu(D^2).
}
\tag{88.30}
\]

For such a macroscopic cell, the global local-deficit identity (88.4) gives

\[
\boxed{
{A_{4,r}\over\operatorname{area}(P_r)}\to1
}
\tag{88.31}
\]

along a maximizing subsequence, because its individual nonnegative deficit is at most
the global `o(D^2)` deficit.

Let `mu_j` increase to `mu_0` sufficiently slowly. The capacity function is continuous
at `mu_0` from below and

\[
\mathcal C(\mu_0)=0.4638645974\ldots,
\qquad
\Gamma(\mu_0)=0.3215335659\ldots>0.
\tag{88.32}
\]

while the long-cell count in (88.29) stays uniformly bounded. A diagonal choice of
maximal-area long cells therefore gives one sequence `P_*` with

\[
\boxed{
{d_*\over D}\ge\mu_0-o(1),
\qquad
\operatorname{area}(P_*)\ge c_*D^2,
\qquad
{A_{4,*}\over\operatorname{area}(P_*)}\to1
}
\tag{88.33}
\]

for one absolute constant `c_*>0`.

In particular

\[
\boxed{
\liminf {1\over D}\max_r d_r\ge\mu_0.
}
\tag{88.34}
\]

The exact value of `c_*` is not important. The displayed constants show that it can
be chosen uniformly positive.

## 88.7 Apply the local near-quadrangulation theorem

The cells selected in (88.33) are macroscopic and locally rhombus-saturated. Their
unloaded populations are quadratic by Oler capacity and the local rhombus area, while
their attachment counts are linear because

\[
|A_*|\ge{d_*+1\over3}=\Omega(D),
\qquad
|A_*|\le q\le\pi D.
\]

Therefore the exact Section-82 local ledger applies at macroscopic scale:

\[
\boxed{
|I_*|=\Theta(D^2),
\qquad
|A_*|=\Theta(D),
\qquad
F_{4,*}=|I_*|+O(D)=\Theta(D^2),
}
\tag{88.35}
\]

and the full strict-rhombus complex of the cell has physical boundary `O(D)`.
After every fixed Section-68/69 phase cut, essentially all of its rhombi lie in
`epsilon`-coherent grains with total physical perimeter `O_epsilon(D)`.

Thus the Type-II branch contains an actual boundary-order near-quadrangulated harmonic
carrier whose diameter is at least

\[
0.8896708101\ldots D-o(D).
\]

This is substantially stronger than merely knowing that some carrier has diameter
`Omega(D)`.

## 88.8 Sharp regression of pure cap geometry

The threshold `sqrt(3)/2` is a genuine barrier if one ignores harmonic attachment
multiplicity.

Take a regular `3N`-gon inscribed in the radius-`1/2` disk. Choose three equally spaced
vertices. Their convex hull is an equilateral central triangle of diameter
`sqrt(3)/2`. The three sets obtained by taking the convex hulls of the boundary
vertices on each `120`-degree arc between consecutive chosen vertices are three
peripheral cells. The four convex polygons have pairwise disjoint interiors, tile the
regular polygon, and every one has diameter at most `sqrt(3)/2`.

So pairwise interior-disjoint boundary-supported convex cells alone cannot force a
cell diameter above `sqrt(3)/2`. The harmonic lower bound on the number of attachments
is exactly what moves the rigorous threshold to `mu_0`.

This also pinpoints the error in the old near-circle cap reports: their full-core
endpoint treated the central wrapping configuration as if it were a one-arc cap.
Their low-`mu` calculations below `sqrt(3)/2` are not invalidated by this correction.

## 88.9 Remaining obstruction

Section 88 still does not close Type II. It gives a large, near-quadrangulated carrier
with almost `0.89D` diameter, but Section 76's complete-grid bound still needs enough
quantitative grid coverage inside that cell to force a contradiction.

The next targets are now much narrower:

1. exploit the wrapping/cap support structure together with the local train-interface
   currency of Section 85 to raise the diameter threshold further or force a large
   common-order grid directly; or
2. show that a locally rhombus-saturated convex harmonic cell of diameter
   `>=mu_0D-o(D)` inside the near-disk force hull cannot satisfy the global diameter
   support/minimality conditions without creating a unit equilateral triangle.

The Type-I inactive-container branch remains separate and is strengthened by Section
86.

## 88.10 Dependency and regression audit

- **Canonical Section 80 / `C-FULLCORE-NEAR-DISK`:** Type-II near-disk force hull and
  asymptotic full-core branch.
- **Canonical Section 83 / `C-HARMONIC-CELL-TILING`:** pairwise interior-disjoint
  harmonic cells, asymptotic area tiling, total cell-perimeter bound, and summed local
  rhombic deficit `o(D^2)`.
- **Canonical Section 62:** `t_r>=delta_r+3`, `d_r<=delta_r+2`, and loaded
  positive-contact degree at most three, giving `|A_r|>=(d_r+1)/3`.
- **Canonical Section 82 / `C-HARMONIC-CARRIER-QUAD`:** local near-quadrangulation
  consequences for the selected macroscopic carrier.
- **Convex geometry:** elementary circle chords, Caratheodory in the plane, radial
  arclength for a convex body between concentric disks, cap area, and isoperimetry.
- **Old cap reports:** not used as premises; their high-`mu` arc-containment step is
  explicitly corrected here.
- **Contact isolates:** retained throughout and excluded only because harmonic cells
  concern the nonisolated positive-contact core.

**Status:** canonical as `C-HARMONIC-WRAPPING`; see `docs/state/theorem-state.yaml` for lifecycle authority. C-II remains open.
