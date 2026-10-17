> Generated reading edition · [exact source](../../../../docs/targets/target-c/96-outer-walk-forbidden-gap-threshold-audit.md) · source SHA-256 `9001b412866b3735a849bb62a28fc7dd0a283cf57efac706fd97655c10d9389d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — outer-walk forbidden-gap threshold audit

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical Section 94 uses the three forbidden angular gaps of a wrapping harmonic
attachment set only as long sides of the convex attachment polygon.  The same gaps
carry strictly more information in the induced contact graph: between consecutive
attachment vertices, the outer-face contact route must connect the same endpoints by
unit edges.  Across each forbidden gap that route therefore has macroscopic length,
while every other non-contact attachment interval costs at least two contact edges.

Combining this sharpened outer-walk lower bound with the exact Section-82 face ledger
raises the Type-II wrapping threshold from `0.9197786626... D` to

$$
\boxed{
\mu_4=0.936215741409583\ldots .
}
$$

No KKT coefficient floor, Fox--Pach constant, or proof-only Section 95 theorem is
used.

---

# 96. Three forbidden gaps force three long outer-contact routes

## 96.1 Setup

Work along a Type-II sequence with source diameters `D_j -> infinity`.  Let

$$
P_j=\operatorname{conv}(A_j)
$$

be harmonic attachment cells such that, after passing to a subsequence,

$$
{\operatorname{diam}(P_j)\over D_j}\to\lambda<1
$$

and the normalized attachment sets have a wrapping Hausdorff limit on the radius
`1/2` circle.  Put

$$
\theta:=2\arcsin\lambda\in[2\pi/3,\pi).
\tag{96.1}
$$

Use the finite local notation of canonical Sections 62 and 82:

- `a_j=|A_j|`;
- `L_j` is the outer-face walk length of the induced contact graph on the unloaded
  component together with `A_j`;
- `s_j>=0` is the pinned-contact surplus;
- `c_j` is the number of loaded-loaded contacts with both endpoints in `A_j`;
- `c_j^partial` is the number of those contacts that are sides of `P_j`; and
- `Q_j>=0` is the bounded-face degree excess.

Canonical Section 82 gives the exact finite identity

$$
\boxed{
L_j+Q_j=4a_j-6-2s_j-2c_j.
}
\tag{96.2}

Canonical Section 62 also records the relevant outer-walk decomposition: between two
consecutive attachment vertices on `partial P_j`, the outer-face route has length one
exactly when that polygon side is a direct loaded-loaded contact; otherwise its length
is at least two.

## 96.2 The three forbidden gaps are three macroscopic outer-walk intervals

Canonical Section 94 proves that the wrapping limit supplies three pairwise distinct
cyclic attachment gaps of angular size

\[
\phi-o(1),
\qquad
\phi:=2\pi-2\theta.
\tag{96.3}
$$

The Type-II force hull lies in the annulus

$$
\left({1\over2}-o(1)\right)D_j
\le |x| \le
\left({1\over2}+o(1)\right)D_j
$$

after translation by the canonical near-disk center.  Therefore the Euclidean chord
between the two attachment endpoints of each distinguished gap has length at least

$$
2\left({1\over2}-o(1)\right)D_j
\sin\left({\phi-o(1)\over2}\right)
=
D_j\sin\theta-o(D_j),
\tag{96.4}
$$

because `phi/2=pi-theta`.

The corresponding outer-face route is a polygonal chain of unit contact edges with
those same endpoints.  Its number of edges equals its Euclidean path length and is at
least the endpoint distance.  Hence each of the three distinguished routes has length
at least

$$
D_j\sin\theta-o(D_j).
\tag{96.5}
$$

For large `j` these three polygon sides have length greater than one, so none is a
direct contact.  On each of the remaining `a_j-3` attachment intervals, the Section-62
rule gives length one for the `c_j^partial` direct-contact sides and length at least two
for all others.  The attachment intervals are consecutive disjoint pieces of the
outer-face walk, counted with the same multiplicity as `L_j`.  Summing gives

$$
\boxed{
L_j
\ge
3D_j\sin\theta
+2(a_j-3)-c_j^\partial
-o(D_j).
}
\tag{96.6}
$$

This is the new input.  Section 94 used only the chord lengths in the perimeter of
`P_j`; (96.6) also charges the contact route needed to realize those chords.

## 96.3 Exact face currency forces a stronger attachment-density floor

Insert (96.6) in (96.2):

$$
3D_j\sin\theta+2a_j-6-c_j^\partial-o(D_j)+Q_j
\le
4a_j-6-2s_j-2c_j.
$$

After cancellation,

$$
3D_j\sin\theta
\le
2a_j+c_j^\partial-2s_j-2c_j-Q_j+o(D_j).
\tag{96.7}
$$

Since `c_j^partial<=c_j`,

$$
\boxed{
2a_j
\ge
3D_j\sin\theta+2s_j+c_j+Q_j-o(D_j).
}
\tag{96.8}
$$

In particular, after passing to a subsequence with

$$
{a_j\over D_j}\to\alpha,
$$

every wrapping limit satisfies

$$
\boxed{
\alpha\ge {3\over2}\sin\theta.
}
\tag{96.9}
$$

The retained nonnegative terms give the stronger quantitative form

$$
\boxed{
\alpha
\ge {3\over2}\sin\theta
+\limsup_j\left(
{s_j\over D_j}+{c_j\over2D_j}+{Q_j\over2D_j}
\right)
}
\tag{96.10}
$$

whenever the displayed defect ratios have limits after a further subsequence.

## 96.4 Combine with the six-cluster ceiling

Canonical Section 88, equivalently Section 94, gives the independent wrapping
attachment-count ceiling

$$
\boxed{
\alpha\le3\theta-2\pi.
}
\tag{96.11}
$$

Therefore every wrapping harmonic-cell limit must satisfy

$$
\boxed{
{3\over2}\sin\theta\le3\theta-2\pi.
}
\tag{96.12}
$$

Define

$$
F(\theta):=3\theta-2\pi-{3\over2}\sin\theta
\qquad(2\pi/3\le\theta<\pi).
\tag{96.13}
$$

Then

$$
F'(\theta)=3-{3\over2}\cos\theta>0
\tag{96.14}
$$

on the whole interval.  Also

$$
F(2\pi/3)=-{3\sqrt3\over4}<0,
\qquad
F(\pi)=\pi>0.
$$

Hence there is a unique root `theta_4` in `(2pi/3,pi)`.  Numerically,

$$
\boxed{
\theta_4
=2.4234054584753130275\ldots,
}
\tag{96.15}
$$

and

$$
\boxed{
\mu_4:=\sin(\theta_4/2)
=0.9362157414095831661\ldots .
}
\tag{96.16}
$$

Thus every wrapping Type-II harmonic-cell limit obeys

$$
\boxed{
\lambda\ge\mu_4.
}
\tag{96.17}
$$

This strictly improves the canonical Section-94 threshold
`0.919778662688621...`.

## 96.5 Propagate the threshold to an actual macroscopic carrier

Fix any `mu<mu_4`.  By (96.17), every macroscopic harmonic-cell limit of normalized
diameter at most `mu` is cap type.  The canonical Section-88 cap-family theorem therefore
applies exactly as in Section 94:

$$
\limsup {1\over D^2}
\sum_{\operatorname{diam}(P_r)\le\mu D}
\operatorname{area}(P_r)
\le\mathcal C(\mu)<{\pi\over4}.
\tag{96.18}
$$

Hence cells longer than `mu D` carry a positive fraction of the Type-II force-hull
area.  The canonical total harmonic-cell perimeter bound makes their number uniformly
bounded for fixed `mu`, while canonical Section 83 makes the summed local rhombic
deficit `o(D^2)`.  Consequently one such cell is macroscopic and locally
rhombus-saturated.

At `mu_4`, the same cap-capacity expression used in Sections 88 and 94 remains
strictly below `pi/4`; numerically its gap is about

$$
{\pi\over4}-\mathcal C(\mu_4)
=0.2883775\ldots>0.
\tag{96.19}
$$

Thus the diagonal choice `mu upward mu_4` is uniform and produces actual cells `P_*`
with

$$
\boxed{
\operatorname{diam}(P_*)
\ge(\mu_4-o(1))D,
\qquad
\operatorname{area}(P_*)\ge c_4D^2,
\qquad
{A_{4,*}\over\operatorname{area}(P_*)}\to1
}
\tag{96.20}

for one absolute `c_4>0`.

## 96.6 Endpoint rigidity becomes stronger

Suppose a wrapping sequence approaches `lambda=mu_4`.  Equations (96.8) and (96.11)
then squeeze the attachment density to

\[
{a_j\over D_j}
\to
{3\over2}\sin\theta_4
=3\theta_4-2\pi.
\tag{96.21}
$$

The nonnegative retained currency in (96.8) must vanish:

$$
\boxed{
{s_j\over D_j}\to0,
\qquad
{c_j\over D_j}\to0,
\qquad
{Q_j\over D_j}\to0.
}
\tag{96.22}
$$

Moreover (96.6) and the exact identity (96.2) must both be asymptotically tight.  Thus

- the three forbidden-gap contact routes are asymptotically Euclidean geodesics;
- all but `o(D)` remaining attachment intervals are two-edge routes rather than
  direct loaded-loaded contacts;
- the bounded contact faces are quadrilateral up to `o(D)` total degree excess; and
- the pinned/contact surplus of the selected carrier is sublinear.

The surviving endpoint is therefore much more rigid than the Section-94 endpoint:
it is a near-quadrangulated macroscopic harmonic cell with three macroscopic
near-geodesic outer-contact corridors and almost every other attachment interval paid
by exactly two unit edges.

## 96.7 Dependency and regression audit

- **Canonical Section 62 / `C-ATTACH-CURRENCY`:** the outer-face route between
  consecutive attachment vertices has length one exactly for a direct attachment-polygon
  contact side and at least two otherwise.
- **Canonical Section 82 / `C-HARMONIC-CARRIER-QUAD`:** exact local identity
  `L+Q=4a-6-2s-2c`.
- **Canonical Sections 88 and 94:** wrapping three-anchor geometry, three distinct
  forbidden cyclic gaps, six-cluster attachment ceiling, and the cap-family
  propagation to an actual macroscopic carrier.
- **Bridges and repeated outer edges:** harmless.  `L` is the outer-face walk length
  with multiplicity, and the consecutive-attachment routes partition that walk in the
  same multiplicity convention used in Section 62.
- **Large-gap direct contacts:** impossible for large `D`, since their endpoint
  distance is `(sin(theta)+o(1))D`.
- **Contact-isolated source points:** untouched.
- **No rejected Reuleaux-cap route, no KKT coefficient floor, and no external
  pseudosegment theorem.**

**Status:** canonical as `C-WRAP-OUTER-WALK-GAP`; see `docs/state/theorem-state.yaml` for lifecycle authority. C-II remains open.
