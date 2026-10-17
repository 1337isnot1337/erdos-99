# Target C — Section 125: augmented-cell route compression isolates the triangular-tooth regression

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate stacked on canonical audit.46.  
**Dependencies:** canonical Sections 62, 82, 122 and 123.

Canonical Section 123 uses the augmented harmonic-cell graph to pay bounded nonquadrilateral perimeter. The same augmented face identity controls the **ordinary outer route length itself**.

For each unloaded component let

- `a_r=|A_r|` be its attachment count;
- `L_r` be the outer-face walk length of the actual induced harmonic graph;
- `T_r` and `Q_r^+` be the triangular-face count and degree-above-four defect of the canonical Section-123 augmented graph; and
- `d_r=diam(P_r)`.

Then the finite route-compression theorem is

\[
\boxed{
L_r-2a_r\le a_r-T_r+Q_r^+.
}
\tag{125.1}
\]

Summing and using canonical Section 123 gives

\[
\boxed{
\sum_r(L_r-2a_r)
\le2\bigl(e_{BB}-k-d_{tile}\bigr),
}
\tag{125.2}
\]

where

\[
d_{tile}=q-2-\sum_r(a_r-2)\ge0,
\qquad k=d_H+s_Z.
\]

More importantly, retaining the correlation with `Q_r^+` instead of replacing it by `e_BB-k` gives a cleaner Type-II consequence. Put

\[
A_*:=\sum_r(a_r-T_r),
\qquad
Q_*:=\sum_rQ_r^+,
\qquad
\Delta_{ad}:=\sum_r(a_r-d_r).
\tag{125.3}
\]

Canonical Section 122's aggregate detour theorem and Section 123's local estimate

\[
P_{{\rm exc},r}\le5Q_r^+
\]

imply

\[
\boxed{
\liminf_{D\to\infty}{1\over D}
\left(
\Delta_{ad}+{A_*\over2}+3Q_*
\right)
\ge
{\pi\over4}(2-\sqrt3).
}
\tag{125.4}
\]

Thus the promoted return demand can be paid only by three exact augmented-cell currencies:

1. attachment count beyond Euclidean cell diameter, `sum(a_r-d_r)`;
2. attachment sides whose augmented side-face is not triangular, `A_*`; or
3. augmented degree defect `Q_*`.

The theorem identifies the sharp residual regression. If `A_*=o(D)` and `Q_*=o(D)`, then all but `o(D)` attachment sides bound two-edge triangular teeth and

\[
\boxed{
\liminf {1\over D}\sum_r(a_r-d_r)
\ge {\pi\over4}(2-\sqrt3)
=0.2104468\ldots .
}
\tag{125.5}
\]

No contradiction is claimed: an oblique near-triangular-lattice boundary can realize linearly many two-edge teeth without an exact unit triangle. The remaining closure must use the positive-contact structure behind those triangular teeth or couple `sum(a_r-d_r)` to global diameter minimality.

---

## 125.1 Remove loaded-loaded edges and expose the unsimplified outer walk

Fix one unloaded component `I_r`. Let `G_r^0` be the plane graph on `I_r\cup A_r` containing only

- contacts internal to `I_r`; and
- attachment contacts from `I_r` to `A_r`.

Thus the loaded-loaded contacts among `A_r` are omitted. The graph is connected because `I_r` is connected and every member of `A_r` is incident to at least one attachment contact.

Write `\widetilde L_r` for its occurrence-counted outer-face walk length. Since the graph is triangle-free, every bounded face has degree at least four. Define

\[
\widetilde Q_r
:=\sum_{f\text{ bounded}}
(\deg f-4)\ge0.
\tag{125.6}
\]

Use the canonical Section-62 local counts

\[
V=n_r+a_r,
\qquad
E=e_r+t_r=2n_r+1+s_r.
\]

Euler gives

\[
F_b=E-V+1=n_r+2+s_r-a_r.
\]

Face incidence gives

\[
2E=\widetilde L_r+4F_b+\widetilde Q_r.
\]

Substitution yields the exact unsimplified outer-walk identity

\[
\boxed{
\widetilde L_r+\widetilde Q_r
=4a_r-6-2s_r.
}
\tag{125.7}
\]

This identity is valid with bridges and repeated outer occurrences because all face degrees and `\widetilde L_r` use the plane-walk multiplicity convention.

---

## 125.2 Insert the canonical augmented-face identity

Canonical Section 123 adds all `a_r` sides of the convex attachment polygon to `G_r^0`, producing `J_r^+`. With `T_r` triangular bounded faces and

\[
Q_r^+=\sum_{\deg f\ge5}(\deg f-4),
\]

Section 123 proves exactly

\[
\boxed{
a_r-3-s_r
={a_r-T_r+Q_r^+\over2}.
}
\tag{125.8}
\]

Equivalently,

\[
2a_r-6-2s_r=a_r-T_r+Q_r^+.
\tag{125.9}
\]

Insert (125.9) into (125.7):

\[
\begin{aligned}
\widetilde L_r+\widetilde Q_r
&=2a_r+(2a_r-6-2s_r)\\
&=2a_r+a_r-T_r+Q_r^+.
\end{aligned}
\]

Therefore

\[
\boxed{
\widetilde L_r-2a_r
=a_r-T_r+Q_r^+-\widetilde Q_r
\le a_r-T_r+Q_r^+.
}
\tag{125.10}
\]

This proof does not need to assign individual side faces to individual outer-route fragments. The entire occurrence-counted outer walk is controlled at once by two exact Euler/face identities.

---

## 125.3 Loaded-loaded contacts can only shorten the outer walk

The actual induced harmonic graph `H_r` is obtained from `G_r^0` by adding the loaded-loaded unit-contact edges with both endpoints in `A_r`.

Add these noncrossing straight edges one at a time. If an added edge lies in a bounded face, the outer-face walk is unchanged. If it lies in the current outer face, it splits that face into a bounded face and a new outer face. The old outer boundary contains two endpoint-to-endpoint walks, while the new outer boundary keeps one of them and replaces the other by the new single edge. Since the discarded walk has at least one edge occurrence, the outer-face length cannot increase.

Thus

\[
\boxed{L_r\le\widetilde L_r.}
\tag{125.11}
\]

Combining (125.10)--(125.11) proves the finite local theorem (125.1).

This monotonicity statement permits loaded-loaded polygon sides, internal loaded chords, articulation repetitions, and bridges. No claim that the old outer face was a simple cycle is needed.

---

## 125.4 Global finite route compression

Sum (125.1):

\[
\sum_r(L_r-2a_r)
\le
\sum_r(a_r-T_r+Q_r^+).
\tag{125.12}
\]

Canonical Section 123 gives the exact global augmented-cell ledger

\[
\boxed{
e_{BB}-k
={1\over2}\sum_r(a_r-T_r+Q_r^+)+d_{tile}.
}
\tag{125.13}
\]

Hence

\[
\boxed{
\sum_r(L_r-2a_r)
\le2(e_{BB}-k-d_{tile}).
}
\tag{125.14}
\]

This is (125.2). The right side is nonnegative by (125.13); the left side itself need not be nonnegative because direct loaded-loaded polygon sides can make `L_r<2a_r`.

Since every closed outer walk contains a diameter pair of its attachment polygon,

\[
L_r\ge2d_r.
\]

Equation (125.14) also gives the finite compatibility condition

\[
\boxed{
\sum_r(a_r-d_r)+e_{BB}-k-d_{tile}\ge0.
}
\tag{125.15}
\]

---

## 125.5 Keep the face currencies correlated in the Type-II aggregate theorem

Canonical Section 122 gives, in the Type-II full-core branch,

\[
\liminf {1\over D}
\sum_r\bigl(L_r+P_{{\rm exc},r}-2d_r\bigr)
\ge
R_0,
\qquad
R_0={\pi\over2}(2-\sqrt3).
\tag{125.16}
\]

For each cell canonical Section 123 proves

\[
P_{{\rm exc},r}\le5Q_r^+.
\tag{125.17}
\]

Use the exact decomposition

\[
L_r-2d_r
=(L_r-2a_r)+2(a_r-d_r).
\tag{125.18}
\]

Equations (125.1), (125.17), and (125.18) imply the finite upper payment

\[
\begin{aligned}
\sum_r\bigl(L_r+P_{{\rm exc},r}-2d_r\bigr)
&\le
2\Delta_{ad}+A_*+Q_*+5Q_*\\
&=2\Delta_{ad}+A_*+6Q_*.
\end{aligned}
\tag{125.19}
\]

Combine (125.16) and (125.19), then divide by two:

\[
\liminf {1\over D}
\left(\Delta_{ad}+{A_*\over2}+3Q_*\right)
\ge {R_0\over2}
={\pi\over4}(2-\sqrt3).
\]

This proves (125.4).

The same result could be weakened to a loaded-contact payment using (125.13), but doing so would destroy the useful correlation between ordinary route excess and exceptional-face perimeter. Equation (125.4) is the sharper handoff.

---

## 125.6 Exact meaning of the triangular-face regime

Every triangular bounded face of `J_r^+` must use an added attachment-polygon side, because `G_r^0` is a triangle-free contact graph. It cannot use two added polygon sides: every attachment vertex has an attachment contact entering `int(P_r)`, which separates the two boundary-side sectors, and a three-loaded-vertex triangle would require a loaded-loaded edge that is absent from `G_r^0`.

Therefore a triangular face consists of

- one artificial side `[a_i,a_{i+1}]`; and
- two unit attachment/internal contact edges through one unloaded apex.

Its artificial side has length strictly greater than one: equality would make the two unit edges plus that side an actual unit-contact triangle in the source.

Thus `T_r` counts genuine two-edge **near-triangular teeth**, not exact contact triangles. When

\[
A_*=\sum_r(a_r-T_r)=o(D),
\qquad
Q_*=o(D),
\]

all but `o(D)` attachment sides are of this two-edge form. Equation (125.4) then forces (125.5).

This is the exact all-regime regression exposed by route compression. A large ordered family of near-equilateral triangular teeth is compatible with triangle-freeness unless an additional source-level rigidity or diameter-minimality theorem forces one artificial base to reach length exactly one.

---

## 125.7 Scope and next target

- Every source point is retained.
- No Section-57 affine-kernel statement is applied to contact-isolated coordinates.
- All outer-face lengths use occurrence counting.
- The proof uses no phase-bin estimate, carrier decimal, or KKT coefficient floor.
- The only asymptotic input is canonical Section 122 in the final Type-II consequence.
- Theorem authority remains audit.46 through Section 123; Sections 124--125 are proof-only.

The live full-core closing problem is now sharper:

> rule out the regime in which almost every attachment side bounds a two-edge triangular tooth, augmented degree defect is small, and `sum_r(a_r-d_r)` carries the return demand; or show that a positive density of nontriangular/defective augmented faces forces a source-level contradiction through the already exposed `A_*+Q_*` currency.

Pure Oler density cannot rule out the triangular-tooth regime: the artificial base lengths may approach one from above without ever creating an exact unit triangle.

**Disposition:** proof-only route-compression theorem. C-II remains open.
