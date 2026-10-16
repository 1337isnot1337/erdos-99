<!-- theorem-state: {"artifact_id":"ART-6C3F896ABFE5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — endpoint corridor bridge/rhombus dichotomy

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical Section 96 raises the Type-II wrapping threshold to

\[
\mu_4=0.936215741409583\ldots
\]

and identifies three distinguished macroscopic outer-contact routes at equality.  A
separate corrected audit shows that those three routes individually have `o(D)` path
excess over their endpoint chords.  The next issue is whether such a route actually
interfaces with the strict-rhombus bulk.  One cannot simply assume this: the outer
face of the induced harmonic-cell contact graph may contain bridge occurrences.

This section keeps that obstruction explicit.  It proves that each distinguished
corridor has one of two sharply constrained forms:

1. a linear bridge-rich block-tree corridor, giving a linear nested chain of attachment
   separators; or
2. a linear family of boundary strict rhombi whose exposed unit sides are
   asymptotically aligned with the corridor chord.

No bridge is silently discarded, and no whole-outer-walk perimeter equality is used.

---

# 97. Endpoint corridors are bridge-rich or rhombus-rich

## 97.1 Endpoint notation and route-level geodesic collapse

Work along a wrapping Type-II sequence at the canonical Section-96 endpoint.  Let
`H_D` be the induced contact graph of the selected harmonic component and its loaded
attachment set `A_D`, and let

\[
P_D=\operatorname{conv}(A_D).
\]

Put

\[
\theta_4=2\arcsin\mu_4,
\qquad
s_4:=\sin\theta_4
=0.658020712164235\ldots,
\]

and

\[
\alpha_4={3\over2}s_4
=3\theta_4-2\pi
=0.987031068246352\ldots .
\]

Canonical Section 96 gives

\[
{a_D\over D}\to\alpha_4,
\qquad
{Q_D\over D},{s_D\over D},{c_D\over D}\to0,
\tag{97.1}
\]

and the exact local identity

\[
L_D+Q_D=4a_D-6-2s_D-2c_D.
\tag{97.2}
\]

Therefore

\[
\boxed{L_D=6s_4D+o(D).}
\tag{97.3}
\]

Let `W_{1,D},W_{2,D},W_{3,D}` be the three outer-face routes corresponding to the
three distinguished forbidden attachment gaps from Section 96.  Let `ell_{j,D}` be
their unit-edge path lengths and `d_{j,D}` their endpoint chord lengths.

The Section-96 annular gap estimate gives

\[
d_{j,D}\ge s_4D-o(D).
\tag{97.4}
\]

Every remaining attachment interval costs two outer-walk edges unless it is a direct
loaded-loaded polygon-side contact.  If `c_D^partial` is the number of such direct
sides, then `c_D^partial<=c_D=o(D)` and

\[
L_D
\ge
\sum_{j=1}^3\ell_{j,D}
+2(a_D-3)-c_D^\partial.
\tag{97.5}
\]

Insert (97.1) and (97.3) into (97.5):

\[
\sum_{j=1}^3\ell_{j,D}
\le3s_4D+o(D).
\tag{97.6}
\]

But `ell_{j,D}>=d_{j,D}` and (97.4) give the reverse lower bound.  Hence, separately
for `j=1,2,3`,

\[
\boxed{
\ell_{j,D}=s_4D+o(D),
\qquad
d_{j,D}=s_4D+o(D),
\qquad
e_{j,D}:=\ell_{j,D}-d_{j,D}=o(D).
}
\tag{97.7}

This proof uses only the canonical Section-96 route budget; it does not use the false
claim `L_D-per(P_D)=o(D)` from the first version of the endpoint-stability report.

## 97.2 Metric stability of one distinguished route

Orient one route from its first attachment endpoint to its second.  Let its unit edge
vectors be `z_1,...,z_m`, let `q` be the unit chord direction, and let
`psi_k in [-pi,pi]` be the signed angle from `q` to `z_k`.

Projection onto `q` gives the exact identity

\[
\sum_{k=1}^m(1-\cos\psi_k)=m-d=e.
\tag{97.8}
\]

Since `1-cos x >= 2x^2/pi^2` on `[-pi,pi]`,

\[
\boxed{
\sum_{k=1}^m\psi_k^2\le {\pi^2\over2}e=o(D).
}
\tag{97.9}
\]

Consequently, for every fixed `eta>0`, only `o(D)` edge occurrences of the route make
angle at least `eta` with the chord direction.

The path also lies in the ellipse with its two endpoints as foci and major-axis length
`m`.  Hence its transverse width is at most

\[
{1\over2}\sqrt{m^2-d^2}
=
\sqrt{{de\over2}+{e^2\over4}}
=o(D),
\tag{97.10}
\]

and its longitudinal overshoot is at most `e/2=o(D)`.

Thus each special route is a genuinely thin macroscopic contact corridor.

## 97.3 Outer nonbridge edges fail to border rhombi only `o(D)` times

Consider an edge occurrence on the outer-face walk of `H_D`.

- If the underlying edge is a bridge, both sides are the outer face and the edge occurs
  twice in the complete outer walk.
- If it is not a bridge, its other side is one bounded face.

Canonical Section 82 proves that every bounded four-face is a strict unit rhombus and
that every other bounded face has degree at least five.  If `f_exc,D` is the number of
nonquadrilateral bounded faces, then

\[
f_{exc,D}\le Q_D
\]

and

\[
\sum_{f\text{ nonquad}}\deg f
=4f_{exc,D}+Q_D
\le5Q_D=o(D).
\tag{97.11}
\]

Therefore among **all** nonbridge outer-face edge occurrences, only `o(D)` can have a
nonquadrilateral bounded face on their inner side.  Every other nonbridge outer
occurrence is a side of a strict unit rhombus.

## 97.4 The finite corridor dichotomy

Fix one of the three special routes and let `B_D` be the number of its edge
occurrences whose underlying edge is a bridge of `H_D`.

For every fixed `eta` with

\[
0<\eta<s_4,
\]

one of the following holds along a subsequence:

### Branch BR — bridge-rich corridor

\[
\boxed{B_D\ge\eta D.}
\tag{97.12}
\]

### Branch RH — rhombus-rich corridor

\[
\boxed{
\text{at least }(s_4-\eta-o(1))D
\text{ route-edge occurrences border strict unit rhombi.}
}
\tag{97.13}
\]

Indeed the route has `(s_4+o(1))D` edge occurrences by (97.7).  If (97.12) fails,
all but at most `eta D` are nonbridges; by (97.11), all but another `o(D)` of those
border strict rhombi.

Intersecting with the angular conclusion (97.9), Branch RH strengthens to:
for every fixed angular tolerance `delta>0`,

\[
\boxed{
\text{at least }(s_4-\eta-o(1))D
\text{ route occurrences border strict rhombi and have exposed side direction}
\text{ within }\delta\text{ of the corridor chord.}
}
\tag{97.14}

A single rhombus has four sides, so (97.14) contains at least

\[
\boxed{
\left({s_4-\eta\over4}-o(1)\right)D
}
\tag{97.15}
\]

distinct boundary strict rhombi with an exposed side in that narrow direction cone.
No phase-coherence conclusion is asserted yet.

## 97.5 Structure in the bridge-rich branch

The bridge alternative is not an unstructured escape.

### Lemma 97.1 — each bridge separates attachment vertices on both sides

Let `e=uv` be a bridge of `H_D`.  Every component of `H_D-e` contains at least one
loaded attachment.

### Proof

Suppose one component `S` contains no attachment.  All its vertices are unloaded.
The only contact from `S` to the rest of the graph is the bridge `uv`; take `v` on the
outside.  Positive harmonic equilibrium on the unloaded component makes each
coordinate on `S` harmonic with the sole boundary value `p_v`.  The discrete maximum
principle forces every point of `S` to equal `p_v`, contradicting distinct source
points. `square`

### Lemma 97.2 — a bridge cut is a nonalternating attachment split

The attachment sets on the two sides of a bridge cannot alternate around the cyclic
order on `partial P_D`.

### Proof

If attachments `a_1,a_2` on one side and `b_1,b_2` on the other occurred in alternating
cyclic order, connectedness of the two bridge-deletion components would give two
vertex-disjoint plane arcs inside the convex disk `P_D`, one joining `a_1` to `a_2`
and the other joining `b_1` to `b_2`.  Alternating boundary pairs force those arcs to
cross, impossible in the plane contact graph. `square`

Contract every maximal 2-edge-connected block of `H_D`; its bridges form the edges of
a tree `T_D`.  Project a special outer route to this bridge tree.  Any excursion over
a bridge and back traverses that same bridge twice in opposite directions.  Such a
pair contributes exactly two to the left side of (97.8), because the two edge vectors
are negatives of each other.  Since `e_{j,D}=o(D)`, only `o(D)` bridge edges are
traversed twice within the route.

Therefore, in Branch BR, after deleting `o(D)` backtracking bridge occurrences, at
least

\[
\boxed{(\eta-o(1))D}
\tag{97.16}

distinct bridge edges lie on the simple path in `T_D` between the endpoint blocks of
the special route.  Their bridge cuts are nested along that tree path, and Lemmas
97.1--97.2 identify them with a linear nested chain of nontrivial, nonalternating
attachment separators.

Thus Branch BR is a linear-depth laminar attachment-cut phenomenon, not a generic
boundary defect.

## 97.6 What remains in each branch

Section 97 turns the Section-96 endpoint into two concrete obligations.

### Bridge-rich obligation

Rule out, or exploit, a harmonic component whose block tree has linear depth along a
macroscopic almost-straight contact corridor while every bridge cut separates
nonempty cyclic attachment intervals.  Natural inputs are the Section-62 attachment
incidence currency and the selected-circuit attachment-block theorem.

### Rhombus-rich obligation

Use the linear family of boundary strict rhombi with nearly common exposed side
direction.  The interior of the same harmonic cell is locally rhombus-saturated and
contains the canonical dense/ordered train structure.  A closing theorem must show
that this boundary phase concentration either spends too much angular/interface defect,
forces an exact unit equilateral triangle, or enables a strict diameter-reducing
source deformation.

The dichotomy itself does not close C-II.

## 97.7 Regression audit

- **Bridges:** retained explicitly; no 2-connectedness of `H_D` is assumed.
- **Repeated outer edge occurrences:** counted with multiplicity in `L_D`.  Repeated
  traversal of one bridge inside a special route is charged by (97.8).
- **Nonquadrilateral faces:** their total boundary incidence is at most `5Q_D=o(D)`.
- **Contact-isolated source points:** absent from the positive-contact harmonic cell and
  untouched.
- **Whole-walk perimeter equality:** not used.
- **KKT coefficient lower bounds:** not used.
- **Rejected Reuleaux-cap route:** not used.

**Status:** proved candidate, proof-only pending independent hostile audit/promotion.
**Theorem state:** unchanged by this proof.
