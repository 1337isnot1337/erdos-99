> Generated reading edition · [exact source](../../../docs/reports/target_c_endpoint_route_excess_split_2026-09-12.md) · source SHA-256 `501a00cd4e4a00c2808dec432c6346d2c4cba4d77e0d39cd7e4e1c42bc1c7357`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-42BAC5B36130","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Section 96 endpoint route-excess split audit

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical Section 96 forces every wrapping Type-II harmonic-cell limit to have
normalized diameter at least

$$
\mu_4=0.9362157414095831661\ldots .
$$

This module analyzes the equality regime. The corrected endpoint-stability report
already records that the three distinguished Section-96 outer routes are
near-geodesic, but it deliberately leaves the attachment-polygon perimeter
undetermined. Equality in the Section-88 six-cluster packing ceiling supplies the
missing information.

The endpoint split is

$$
\boxed{
{\operatorname{per}(P_D)\over D}\to3\alpha_4,
\qquad
{L_D\over D}\to4\alpha_4,
\qquad
{L_D-\operatorname{per}(P_D)\over D}\to\alpha_4,
}
$$

where

$$
\theta_4=2\arcsin\mu_4,
\qquad
\alpha_4=3\theta_4-2\pi={3\over2}\sin\theta_4
=0.9870310682463526\ldots .
$$

Moreover the linear walk/polygon gap is carried by almost exactly `alpha_4 D`
ordinary two-edge boundary detours over attachment-polygon sides of length `1+o(1)`.
Thus the Section-96 endpoint has a boundary layer of linearly many near-equilateral
unit-unit teeth; the gap does not collapse to zero.

---

# 97. Endpoint six-cluster saturation localizes the outer-walk excess

## 97.1 Endpoint notation

Let `P_D=conv(A_D)` be wrapping Type-II harmonic cells with

$$
{\operatorname{diam}(P_D)\over D}\to\mu_4.
\tag{97.1}
$$

Write

- `a_D=|A_D|`;
- `L_D` for the outer-face walk length of the induced harmonic contact graph;
- `s_D,c_D,Q_D` for the canonical local surplus/contact/face-defect currencies; and
- `c_D^partial` for loaded-loaded contacts that are attachment-polygon sides.

Canonical Section 96 gives

$$
\boxed{
{a_D\over D}\to\alpha_4,
\qquad
{s_D\over D},{c_D\over D},{Q_D\over D}\to0,
\qquad
{L_D\over D}\to4\alpha_4.
}
\tag{97.2}
$$

It also supplies three distinct forbidden cyclic attachment gaps. Put

$$
\phi_4:=2\pi-2\theta_4.
\tag{97.3}
$$

The corrected Section-96 endpoint-stability argument shows that the corresponding
three outer-contact routes have length

$$
D\sin\theta_4+o(D)
\tag{97.4}
$$

each, and their endpoint chords have the same asymptotic length.

## 97.2 Equality in the six-cluster count saturates the allowed boundary arcs

Fix the three wrapping anchors used by Sections 88 and 94 after passing to the endpoint
Hausdorff limit. Their six allowed circular intervals have total angular measure

$$
6\theta_4-4\pi=2\alpha_4.
\tag{97.5}
$$

For the finite cells, every attachment lies in an `o(1)` angular enlargement of these
six intervals. Canonical Type-II annular convergence and the polar-arc estimate of
Section 88 therefore place all attachments in a union of at most six force-hull
boundary arcs of total Euclidean length `S_D` with

$$
\boxed{S_D\le\alpha_4D+o(D).}
\tag{97.6}
$$

Treat touching allowed intervals as one component. Order the attachments on each
nonempty component. If a component contains `N` attachment vertices, the boundary
arclength between its first and last attachment is at least `N-1`: consecutive source
points have Euclidean distance at least one, and boundary arclength dominates chord
length. There are at most six nonempty components. Hence

$$
S_D\ge a_D-6.
\tag{97.7}
$$

Using `a_D=alpha_4 D+o(D)`, (97.6)--(97.7) squeeze

$$
\boxed{S_D=\alpha_4D+o(D).}
\tag{97.8}
$$

The same comparison also controls the slack. Decompose `S_D-(a_D-6)` into the unused
endpoint margins of the allowed components plus the excess of within-component
consecutive boundary separations above one, with only an `O(1)` correction for the
number of nonempty components. Every term is nonnegative, while the total is `o(D)`.
Thus both the total unused endpoint margin and the total spacing excess are `o(D)`.

The force-hull boundary lies in an annulus of radius `(1/2+o(1))D`, so an `o(D)` total
boundary-arclength margin on this fixed finite family corresponds to `o(1)` total
angular margin. Therefore the attachments adjacent to each of the three central
forbidden arcs approach its two endpoints. The three distinguished cyclic attachment
gaps satisfy

$$
\boxed{h_{i,D}=\phi_4+o(1)\qquad(i=1,2,3).}
\tag{97.9}

## 97.3 The attachment-polygon perimeter is `3 alpha_4 D+o(D)`

Type-II annular convergence and (97.9) give the three distinguished polygon-side
lengths

\[
\boxed{d_{i,D}=D\sin\theta_4+o(D).}
\tag{97.10}
$$

Their total is

$$
3D\sin\theta_4+o(D)=2\alpha_4D+o(D).
\tag{97.11}
$$

The three distinguished sides are exactly the polygon sides crossing the three
central forbidden arcs. Every other attachment-polygon side joins two consecutive
attachments within one allowed boundary component; the selected anchor attachments
separate the neighboring allowed pieces at each anchor. Its chord is no longer than
the corresponding force-hull boundary arc. Hence the sum `P_D^short` of the remaining
`a_D-3` side lengths obeys

$$
P_D^{short}\le S_D+o(D)=\alpha_4D+o(D).
\tag{97.12}
$$

Source separation gives the reverse bound

$$
P_D^{short}\ge a_D-3=\alpha_4D+o(D).
\tag{97.13}
$$

Thus

$$
\boxed{P_D^{short}=\alpha_4D+o(D).}
\tag{97.14}
$$

Adding (97.11) gives

$$
\boxed{
{\operatorname{per}(P_D)\over D}\to3\alpha_4.
}
\tag{97.15}

This differs from the false first version of the endpoint-stability report. The
canonical local capacity `per(P_D)<=4a_D-6` is not tight at the Section-96 endpoint;
it retains a linear gap of asymptotic size `alpha_4 D`.

## 97.4 The entire linear gap is contact-walk detour

From Section 96 and (97.15),

\[
\boxed{
{L_D-\operatorname{per}(P_D)\over D}\to\alpha_4.
}
\tag{97.16}

This gap has a precise combinatorial location.

Let the three distinguished routes have edge lengths `r_{i,D}`. The corrected
endpoint-stability argument gives

\[
r_{i,D}=D\sin\theta_4+o(D)
\qquad(i=1,2,3),
\tag{97.17}
$$

so their total path-minus-chord excess is `o(D)`.

Also `c_D^partial=o(D)`. Apart from those one-edge direct-contact intervals, every
ordinary consecutive-attachment route has at least two unit edges. The lower
Section-96 route decomposition and `L_D=4alpha_4D+o(D)` imply that the sum of all
ordinary excess above two edges is `o(D)`. Since route lengths are integers,

$$
\boxed{
\#\{\text{ordinary routes with at least three edges}\}=o(D).
}
\tag{97.18}

Hence all but `o(D)` of the `a_D-3=alpha_4D+o(D)` ordinary intervals are exactly
length-two contact routes.

## 97.5 Almost every two-edge route is a near-equilateral tooth

Let `d_{k,D}` be the attachment-polygon side length for an ordinary interval. By
(97.14),

\[
\sum_{k\ ordinary}(d_{k,D}-1)=o(D),
\qquad d_{k,D}\ge1.
\tag{97.19}
$$

Therefore for every fixed `epsilon>0`,

$$
\boxed{
\#\{k:\ d_{k,D}\ge1+\epsilon\}=o(D).
}
\tag{97.20}
$$

Equivalently, there is a sequence `epsilon_D ->0` for which all but `o(D)` ordinary
sides satisfy

$$
1\le d_{k,D}\le1+\epsilon_D.
\tag{97.21}

Intersect this set with the length-two routes from (97.18). For
`alpha_4D-o(D)` intervals the outer route is

\[
p_k-x_k-p_{k+1},
\qquad
|p_k-x_k|=|x_k-p_{k+1}|=1,
\tag{97.22}
$$

where `x_k` is an unloaded vertex of the harmonic component, while

$$
1<|p_k-p_{k+1}|\le1+\epsilon_D.
\tag{97.23}
$$

The strict lower inequality follows from triangle-freeness: equality would make
`p_k,x_k,p_{k+1}` a unit equilateral triangle.

Thus the angle at `x_k` is

$$
2\arcsin(|p_k-p_{k+1}|/2)=\pi/3+o(1),
\tag{97.24}
$$

and the altitude from `x_k` to the short polygon side is

$$
\sqrt{1-|p_k-p_{k+1}|^2/4}=\sqrt3/2+o(1).
\tag{97.25}
$$

The Section-96 endpoint therefore contains a linear family of genuine unit-unit
outer-contact teeth converging to equilateral geometry while retaining a strictly
nonunit base.

## 97.6 What this changes

The endpoint cannot be modeled by an outer contact walk that hugs the attachment
polygon. Its first-order geometry is instead

```text
three macroscopic near-geodesic contact corridors
+
(alpha_4-o(1)) D short near-equilateral two-edge teeth.
```

The next closure theorem should exploit the teeth together with unloaded positive
equilibrium and the locally rhombic-saturated carrier. Each tooth's intermediate apex
vertex is unloaded and therefore has additional inward positive-contact support. A
successful next step would show that linearly many nearly equilateral boundary teeth
force either

1. an exact unit triangle;
2. a forbidden amount of train/interface currency; or
3. a source-preserving deformation with strict global diameter gain.

The present theorem does not assert any of those conclusions.

## 97.7 Dependency and regression audit

- **Canonical Section 96 / `C-WRAP-OUTER-WALK-GAP`:** endpoint attachment density,
  vanishing local defect, exact outer-walk limit, and three forbidden routes.
- **Canonical Sections 88 and 94:** six allowed angular intervals and their three
  central forbidden arcs.
- **Canonical Type-II annular convergence:** converts fixed angular unions to
  `(D/2+o(D))` force-hull boundary arclength.
- **Canonical Section 62:** the outer-face routes between consecutive attachment
  vertices lie in the induced graph on the unloaded component and its attachment set,
  so the internal vertex of a two-edge noncontact route is unloaded.
- **Unit separation:** gives one unit of boundary arclength and polygon-side length per
  ordinary consecutive attachment pair.
- **Triangle-free source:** makes the bases in (97.23) strictly greater than one.
- **No KKT coefficient floor, no Fox--Pach constant, no rejected cap theorem.**

**Status:** proved candidate, proof-only pending independent hostile audit/promotion.
**Theorem state:** unchanged by this proof.
