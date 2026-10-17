# Target C-II — retracted full-core Type-II two-phase area/train tradeoff

**Date:** 2026-09-13  
**Classification:** rejected; normalization error found before promotion. Theorem-state authority unchanged.
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

**Dependencies:** the audited bridge-subtracted isoperimetry and two-phase
boundary-charge candidates, the canonical Type-II full-core area sandwich, and the
audited-working stopped-train floor of Section 168.

This note is retained as a retracted proof attempt.  The side-charge calculation in
Section 2 is valid under its stated hypotheses, but the area normalization used after
it is invalid: the force-hull area is `Theta(D^2)`, whereas the face-defect variables
`f` and `Q` are only `O(D)`.  The claimed `t` upper bound does not follow.

The implication chain is

```text
near-disk full Type-II core + two face directions
 -> outer bridges are paid by total route surplus
 -> loaded-hull side charge gives Q <= 4f + delta D + o(D)
 -> [retracted] invalid O(D)-scale use of the face-area bound.
```

No tradeoff, endpoint exclusion, or C-II consequence survives this correction.

## 1. Hypotheses and notation

Take a Type-II contact-minimal, then diameter-pair-minimal representative and its
full nonisolated positive-contact core.  Use

- `D` for the source diameter;
- `F` for the loaded force hull, `p=per(F)`, and `q` for its loaded vertex count;
- `b` for the occurrence-counted outer contact walk of the full core;
- `f` and `Q` for the number of bounded nonquadrilateral faces and their degree
  excess, so `P_exc=4f+Q`;
- `k=d_H+s_Z` and `t=(q-k)/D`;
- `u_B` for the nonnegative Type-II loaded-hull outer-walk slack; and
- `T` for the complete stopped-train count.

Assume the canonical Type-II near-disk sandwich

\[
 {p\over D}\to\pi,
 \qquad {\operatorname{area}(F)\over D^2}\to{\pi\over4},
 \qquad {\operatorname{area}(U)\over D^2}\to{\pi\over4},
\tag{TP.1}
\]

where `U` is the union of all bounded faces.  The last limit follows from the
strict-rhombus area saturation and `U\subset F` in the canonical full-core branch.
Assume every bounded quadrilateral face uses one of two projective unit directions.
The bounded exceptional-face areas are then `o(D^2)`, since the strict-rhombus union
already has area `(pi/4-o(1))D^2` inside `F`.

Finally use the audited-working all-regime train floor (Section 168; the weaker
Section 142 constant is enough):

\[
 {T-q/2\over D}\ge C_0-o(1),
 \qquad
 C_0:=2\sqrt{\frac\pi{2\sqrt3}}+0.0004.
\tag{TP.2}
\]

No claim is made that the two-direction hypothesis holds for every Type-II survivor.

## 2. Bridge payment and the loaded-hull side inequality

Put

\[
 \delta={b-p\over D}\ge0,
 \qquad B_o=\#\{\text{outer-face bridges}\}.
\]

The finite bridge-subtracted isoperimetric inequality for the bounded-face union,
combined with (TP.1), gives

\[
 2B_o\le b-\pi D+o(D)=\delta D+o(D).
\tag{TP.3}
\]

Let `H` be the number of loaded-hull side incidences on bounded exceptional faces,
and let `I` be the number of their non-hull side incidences.  The two-direction
hypothesis leaves at most four loaded-hull sides in the selected directions.  Since
Type II has `c_B=0`, every other loaded-hull unit side is either an outer bridge or
is incident to an exceptional bounded face.  The exact loaded-hull identity

\[
 e_{BB}=Q+2k+u_B
\tag{TP.4}
\]

therefore gives

\[
 H\ge Q+2k+u_B-4-B_o.
\tag{TP.5}
\]

The near-disk shared-boundary estimate applies to the exceptional faces (each has
`o(D^2)` area), so `H\le(1+o(1))I`.  Since the full exceptional-face incidence is
`P_exc=H+I`, (TP.5) yields

\[
 4f+Q\ge2(Q+2k+u_B-B_o)-o(D).
\]

Using (TP.3) and dropping nonnegative `k,u_B`,

\[
\boxed{Q\le4f+\delta D+o(D).}
\tag{TP.6}
\]

This is the only place where two-direction purity is used.  The argument is by face
and edge occurrences; repeated outer vertices and bridges do not change it.

## 3. The normalization failure

Every bounded nonquadrilateral face is a convex equilateral polygon with unit-
separated boundary vertices.  Oler's inequality gives the canonical per-face lower
bound

\[
 \operatorname{area}(R)\ge {\sqrt3\over4}(\deg R-2).
\]

The bounded faces have disjoint interiors and lie in `F`.  Therefore (TP.1) implies

\[
 {\sqrt3\over4}(2f+Q)\le {\pi\over4}D^2+o(D^2),
\]
or

\[
 \boxed{ {2f\over D^2}+{Q\over D^2}\le {\pi\over\sqrt3}+o(1). }
\tag{TP.7}
\]

The draft divided this inequality by `D` instead of `D^2`.  That is the normalization
error.  In the canonical regime `f=O(D)` and `Q=O(D)`, so the corrected display is
only a subleading `O(D^{-1})` statement and gives no nontrivial bound on the
`D`-scale quantities `f/D` and `Q/D`.

The exact Type-II outer ledger is

\[
 {Q\over D}=2t-\pi-\delta+o(1).
\tag{TP.8}
\]

The outer ledger (TP.8) remains valid, but it cannot be combined with (TP.7) to
control `t`.  The claimed `D`-scale upper bound

```text
3t <= 3pi/2 + 2 delta + pi/sqrt(3) + o(1)
```

is withdrawn.

## 4. Retained finite fact and disposition

The exact Type-II population identities are

\[
 {q\over D}=t+{k\over D},
 \qquad
 {T\over D}=t+2{f\over D}.
\tag{TP.10}
\]

The side charge (TP.6) is the only retained finite/asymptotic consequence of this
report.  It is already covered by the audited two-phase boundary-charge chain.

The train floor (TP.2) and the population identities are valid inputs, but the
corrected area estimate (TP.7) is on the `D^2` scale.  It cannot supply an upper bound
for `2f/D`, so no train-based upper bound for `t` follows.  The previously displayed
`(TP.13)` and `(TP.14)`, the zero-detour numerical bound, and the claimed endpoint
exclusion are withdrawn.


## 5. Scope and remaining C-II branches

The side charge alone does not give a low-detour/low-`t` reduction.  The report does
not prove that all strict-rhombus directions are globally two-phase.  The remaining
full-core route must handle phase mixtures or an unbounded direction set, while the
macroscopic inactive-container branch still needs a protected discrete exchange, a
source-preserving strict diameter descent, or an exact unit triangle.

Contact-isolated source points remain retained throughout.  No full-source affine
kernel, KKT coefficient floor, or scalar witness is used.

**Disposition:** rejected proof attempt, retained for provenance.  C-II and Level I
remain open.
