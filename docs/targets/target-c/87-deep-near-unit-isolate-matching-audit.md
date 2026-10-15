# Target C — deep near-unit isolate matching audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical C-INACTIVE-NEAR-MATCHING forces linearly many vertex-disjoint isolate pairs at distance
`1+O(1/D)` inside the macroscopic inactive chamber. This module shows that those pairs
cannot all be explained by a thin boundary layer next to the positive core.

For every fixed physical depth `w>0`, the Section-77 chamber contains
`Omega_w(D)` vertex-disjoint near-unit pairs whose **both endpoints** lie at Euclidean
distance at least `w` from the chamber boundary. The threshold remains

\[
1<|x-y|\le1+{K_w\over D}
\]

for a fixed constant `K_w` depending only on `w` and the canonical chamber constants.

For `w>1` this has a useful dynamical consequence. The line segment joining each
matched pair lies in the inner parallel body of the convex chamber. Moving one
endpoint toward its mate by at most `K_w/D`

- stays inside the chamber and therefore inside the full source hull;
- cannot violate the global diameter bound;
- stays a fixed distance greater than one from every positive-core vertex and every
  source point outside the chamber for all sufficiently large `D`.

Hence if the desired pair does not reach unit distance first, the only possible first
unit-separation obstruction is another inactive source point inside the same chamber.
This isolates the remaining local obstruction to the rattler packing itself.

The theorem does not assert that all matched pairs can be closed simultaneously, and
it does not infer a triangle from the resulting near-contact graph.

---

# 87. Boundary strips contain only linearly many unit-separated points

Let `C` be a convex body satisfying, for fixed positive constants,

\[
A:=\operatorname{area}C\ge\alpha D^2,
\qquad
P:=\operatorname{per}C\le P_0D.
\tag{87.1}
\]

Let `Z subset C` be the specified contact-isolated source points of an inactive
chamber, with isolate-only Oler slack

\[
\sigma:={A\over a_0}+{P\over2}+1-|Z|,
\qquad
0\le\sigma\le S_0D.
\tag{87.2}
\]

Here `a_0=sqrt(3)/2`. Canonical Section 77 supplies such constants in its macroscopic
chamber branch.

Canonical C-INACTIVE-HULL-STABILITY gives a linear inradius lower bound

\[
r(C)\ge\kappa D
\tag{87.3}
\]

for some fixed `kappa>0`.

Fix once and for all a depth `w>0`. For sufficiently large `D`,

\[
w+{1\over2}<r(C).
\tag{87.4}
\]

Define the width-`w` boundary strip

\[
U_w:=\{x\in C:\operatorname{dist}(x,\partial C)<w\}.
\tag{87.5}
\]

## 87.1 Packing bound for the boundary strip

### Lemma 87.1

The number of chamber isolates in `U_w` satisfies

\[
\boxed{
|Z\cap U_w|
\le {4(w+1)P\over\pi}+1
\le C_wD+1,
}
\tag{87.6}
\]

where

\[
C_w:={4(w+1)P_0\over\pi}.
\tag{87.7}
\]

### Proof

Center an open radius-`1/2` disk at each point of `Z cap U_w`. The source is
unit-separated, so these disks have pairwise disjoint interiors.

Let

\[
C_{+1/2}:=C+B(0,1/2)
\]

and let `C_{-(w+1/2)}` be the inner parallel body at depth `w+1/2`.
Every radius-`1/2` disk centered in `U_w` lies in

\[
C_{+1/2}\setminus C_{-(w+1/2)}.
\tag{87.8}
\]

Steiner's outer parallel formula gives

\[
\operatorname{area}(C_{+1/2})
=A+{P\over2}+{\pi\over4}.
\tag{87.9}
\]

For `t=w+1/2<r(C)`, inner-parallel coarea and convex perimeter monotonicity give

\[
A-\operatorname{area}(C_{-t})
=\int_0^t\operatorname{per}(C_{-s})\,ds
\le tP.
\tag{87.10}
\]

Therefore the container in (87.8) has area at most

\[
(w+1)P+{\pi\over4}.
\tag{87.11}
\]

The disjoint radius-`1/2` disks have total area

\[
|Z\cap U_w|{\pi\over4}.
\]

Comparing with (87.11) proves (87.6). `square`

Thus every fixed-width chamber boundary layer contains only `O_w(D)` of the
`Omega(D^2)` inactive points.

---

# 87.2 Matching abundance beats every fixed-width boundary layer

For `epsilon>0`, let `G_epsilon` be the near-contact graph on `Z`:

\[
xy\in E(G_\epsilon)
\quad\Longleftrightarrow\quad
|x-y|\le1+\epsilon.
\]

Let `nu_epsilon` be its maximum matching number.

Canonical C-INACTIVE-NEAR-MATCHING proves, for `0<epsilon<=1`,

\[
\boxed{
\nu_\epsilon
\ge {3A\over8a_0}\epsilon-{\sigma\over2}.
}
\tag{87.12}
\]

Set

\[
\epsilon={K\over D}
\]

for a fixed `K>0`. Using (87.1)--(87.2), for all sufficiently large `D`,

\[
\nu_{K/D}
\ge
\left({3\alpha K\over8a_0}-{S_0\over2}\right)D.
\tag{87.13}
\]

Choose `K=K_w` so large that

\[
\boxed{
\gamma_w
:={3\alpha K_w\over8a_0}-{S_0\over2}-C_w
>0.
}
\tag{87.14}
\]

This is always possible because `alpha>0` and all other constants are fixed.

Take a maximum matching `M` in `G_{K_w/D}`. Since its edges are vertex-disjoint, at
most `|Z cap U_w|` matching edges can have an endpoint in `U_w`: assign to each such
edge one of its boundary-strip endpoints; no endpoint is reused by another matching
edge.

Therefore the number of matching edges whose **both** endpoints lie outside `U_w` is
at least

\[
\nu_{K_w/D}-|Z\cap U_w|.
\]

Equations (87.6), (87.13), and (87.14) give

\[
\boxed{
\#\{xy\in M:x,y\notin U_w\}
\ge \gamma_wD-1.
}
\tag{87.15}
\]

For all sufficiently large `D`, this is at least `(gamma_w/2)D`.

Because every chamber point in `Z` is contact-isolated, every such edge satisfies

\[
\boxed{
1<|x-y|\le1+{K_w\over D},
\qquad
\operatorname{dist}(x,\partial C),
\operatorname{dist}(y,\partial C)\ge w.
}
\tag{87.16}
\]

This proves the deep near-unit matching theorem.

---

# 87.3 Core-protected pair-closing paths

The inner parallel body

\[
C_{-w}:=\{x\in C:\operatorname{dist}(x,\partial C)\ge w\}
\tag{87.17}
\]

is convex. Hence for every pair in (87.16), the whole segment `[x,y]` lies in
`C_{-w}`.

Assume now `w>1`. Move `x` at unit speed along `[x,y]` toward `y` until either

1. `|x-y|` reaches one, or
2. some other source distance reaches one first.

The required displacement in case (1) is

\[
|x-y|-1\le {K_w\over D}=o(1).
\tag{87.18}
\]

For all sufficiently large `D`, this is smaller than `w-1`. Throughout the motion,
the moved point stays in `C_{-w}`.

### Diameter safety

Every inactive chamber is contained in the force hull `F`, hence in the full source
hull `K_source=conv(A)`. The moved point remains in `C subset K_source`. Since a
convex hull has the same diameter as its extreme source set,

\[
\operatorname{diam}K_{source}=D.
\]

Therefore throughout the motion the moved point remains at distance at most `D` from
every source point. The global diameter constraint cannot be the first obstruction.

### Positive-core safety

The interior of an inactive chamber contains no positive-core vertex. Every
positive-core vertex is on or outside `partial C`. A point of `C_{-w}` is at distance
at least `w` from every point outside the chamber and from every chamber-boundary
point. Hence throughout the motion its distance to every positive-core vertex is at
least

\[
w-{K_w\over D}>1
\tag{87.19}
\]

for all sufficiently large `D`.

Thus no positive-core contact can be the first unit-separation obstruction.

We obtain:

### Corollary 87.2 — first blockers are inactive

For each of the `Omega_w(D)` pairs in (87.16), the straight pair-closing motion can be
run while preserving both the diameter constraint and all distances to positive-core
vertices. More generally, every source point outside the chamber is at distance at
least `w` from the moving point because the entire motion stays in `C_{-w}`.
Therefore, if the chosen mate does not reach unit distance first, the first blocker is
another source point lying in the same inactive chamber.

In particular, at depth `w>1` the remaining obstruction to closing the `1+O(1/D)`
gaps is entirely internal to the inactive packing.

---

# 87.4 Application to the canonical Section-77 chamber

Canonical `C-INACTIVE-CHAMBER`, `C-INACTIVE-NEAR-MATCHING`, and
`C-INACTIVE-HULL-STABILITY` supply absolute constants
`alpha,P_0,S_0,kappa>0` for the selected macroscopic chamber in the
subquadratic-core branch.

Therefore for every fixed `w>0` there are constants

\[
K_w<\infty,
\qquad
c_w>0
\]

such that every sufficiently large survivor in that branch contains at least

\[
\boxed{c_wD}
\]

vertex-disjoint pairs of actual contact-isolated source points with

\[
\boxed{
1<|x-y|\le1+{K_w\over D},
\qquad
\operatorname{dist}(\{x,y\},\partial C_*)\ge w.
}
\tag{87.20}
\]

For every fixed `w>1`, all of their pair-closing segments are uniformly protected
from the positive KKT core and from the diameter constraint as in Corollary 87.2.

---

# 87.5 What this changes and what remains open

Section 81 left open the possibility that all inverse-diameter almost-contacts were a
boundary phenomenon caused by squeezing against the active core. Section 87 excludes
that explanation. An arbitrarily prescribed fixed-width boundary layer contains only
linearly many inactive points with a fixed coefficient, while the matching coefficient
can be made larger by increasing the fixed threshold constant `K_w`.

The chamber branch therefore contains a linear family of **deep** almost-contacts whose
first-order feasibility is decoupled from the positive core.

This still does not prove an exact contact in the original canonical representative.
A pair-closing motion can be blocked by another inactive point, and near-triangular
strict packings can make such isolate-only blocking ubiquitous. Nor does creating
additional zero-weight contacts contradict the contact-minimal canonicalization.

The next missing chamber theorem is now purely inactive at the local scale:

> use the deep near-contact graph, together with the near-capacity and hull-saturation
> structure, to prove a source-preserving collective deformation with a strict global
> diameter gain, or force a contact pattern that necessarily couples back to the
> active boundary/diameter loads.

---

# 87.6 Dependency audit

- **Canonical Section 77 / `C-INACTIVE-CHAMBER`:** convex macroscopic chamber,
  `A>=alpha D^2`, `P<=P_0D`, isolate-only Oler slack `sigma<=S_0D`.
- **Canonical `C-INACTIVE-NEAR-MATCHING`:** matching inequality (87.12).
- **Canonical `C-INACTIVE-HULL-STABILITY`:** linear chamber inradius, used to justify fixed-width inner
  parallel bodies for all sufficiently large `D`.
- **Convex geometry:** Steiner outer parallel formula, inner-parallel coarea, convexity
  of inner parallel bodies.
- **Contact isolates:** retained; all strict pair gaps are actual source distances.

**Status:** canonical after the independent deep-matching promotion audit.
**Theorem state:** promoted as `C-INACTIVE-DEEP-MATCHING`; C-II remains open.
