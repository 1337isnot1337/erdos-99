<!-- theorem-state: {"artifact_id":"ART-983E8825932A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C52: bounded-face Oler terms cancel to the outer contact boundary

**Date:** 2026-08-31  
**Target:** C-II / force-bulk  
**Depends on:** C51, canonical Oler finite-packing inequality, planar Euler counting  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C51 makes every bounded contact face a convex unit-edge polygon. Applying Oler separately to every bounded face, including both its contact-boundary vertices and all contact-isolated source points in its interior, produces an exact cancellation of all internal face-perimeter terms.

Let

- `m` be the force-visible contact-core population;
- `B` be the outer contact-face boundary-walk length;
- `A_bnd` be the total area of all bounded contact faces;
- `Z_def` be the total number of contact-isolated source points lying in bounded faces.

Then

\[
\boxed{
\frac{\sqrt3}{2}(m+Z_{def}-1)
\le
A_{bnd}+\frac{\sqrt3}{4}B.}
\]

Equivalently,

\[
\boxed{
 m+Z_{def}
\le
\frac{2}{\sqrt3}A_{bnd}
+\frac12B+1.}
\]

Since `A_bnd<=area(F)<=pi D^2/4` and C49 gives `B<=4|B_+|-4<=4pi D-4`,

\[
\boxed{
 m+Z_{def}
\le
\Delta_2D^2+2\pi D-1,}
\]

with `Delta_2=pi/(2sqrt3)`.

Thus *all bounded-face rattlers*, including the giant-hole phase of C50, are absorbed into one source-capacity estimate with only an `O(D)` correction. The only KKT-invisible population not controlled by this inequality is the population in the outer contact face.

---

## 1. Oler on one bounded face

Let `f` be a bounded contact face. By C51 its closure is a convex polygon with `k_f` distinct boundary vertices and exactly `k_f` unit contact sides.

Let `z_f` be the number of contact-isolated source points in the interior of `f`.

The set consisting of the `k_f` boundary vertices and the `z_f` isolated points is unit-separated and lies in the convex container `closure(f)`. Oler therefore gives

\[
\frac{\sqrt3}{2}(k_f+z_f-1)
\le
\operatorname{area}(f)
+
\frac{\sqrt3}{4}k_f.
\tag{C52.1}
\]

Rearrange:

\[
\operatorname{area}(f)
\ge
\frac{\sqrt3}{2}z_f
+
\frac{\sqrt3}{4}k_f
-
\frac{\sqrt3}{2}.
\tag{C52.2}
\]

For a quadrilateral with `z_f=0`, this recovers the familiar lower area `sqrt3/2`; triangle-freeness makes the actual area strict, but C52 does not need that strictness.

---

## 2. Sum over all bounded faces

Let `f_b` be the number of bounded faces. Sum C52.1 over all bounded faces:

\[
\frac{\sqrt3}{2}
\left(
\sum_f k_f+Z_{def}-f_b
\right)
\le
A_{bnd}
+
\frac{\sqrt3}{4}\sum_f k_f.
\tag{C52.3}
\]

For a connected plane graph,

\[
\sum_f k_f=2e-B,
\tag{C52.4}
\]

because every edge is counted twice among all face boundary walks and the outer face contributes `B`.

Euler gives

\[
f_b=e-m+1.
\tag{C52.5}
\]

Substitute C52.4-C52.5 into the expression on the left after moving half of the boundary sum to the left:

\[
\begin{aligned}
&Z_{def}-f_b+\frac12\sum_f k_f\\
&=Z_{def}-(e-m+1)+\frac12(2e-B)\\
&=m+Z_{def}-1-\frac B2.
\end{aligned}
\tag{C52.6}
\]

Therefore C52.3 becomes:

### Theorem C52 — bounded-face Oler cancellation

\[
\boxed{
\frac{\sqrt3}{2}(m+Z_{def}-1)
\le
A_{bnd}+\frac{\sqrt3}{4}B.}
\tag{C52.7}
\]

The internal face perimeters and the number of bounded faces have disappeared exactly. Only the outer contact boundary remains.

---

## 3. Diameter form

Every bounded face lies inside the force hull `F`, and the bounded face interiors are pairwise disjoint. Hence

\[
A_{bnd}\le\operatorname{area}(F)
\le\frac\pi4D^2.
\tag{C52.8}
\]

C49 gives

\[
B+Q\le4q-4,
\qquad q=|B_+|,
\]

so

\[
B\le4q-4.
\tag{C52.9}
\]

The convex force-hull boundary is unit-separated, hence

\[
q\le\operatorname{per}(F)\le\pi D.
\tag{C52.10}
\]

Insert C52.8-C52.10 into C52.7:

\[
 m+Z_{def}
\le
\frac{2}{\sqrt3}\frac\pi4D^2
+2q-1
\le
\Delta_2D^2+2\pi D-1.
\tag{C52.11}
\]

---

## 4. Force-bulk consequence

Split the invisible population as in C50:

\[
n-m=Z_{def}+Z_{out},
\]

where `Z_out` consists of isolated points in the outer contact face.

C52 controls the entire first part together with the force-visible core:

\[
\boxed{
 n-Z_{out}
=m+Z_{def}
\le
\Delta_2D^2+O(D).}
\tag{C52.12}
\]

Thus the bounded giant-hole phase of C50 is no longer an independent source-capacity obstruction. A quadratic invisible population can matter beyond ordinary finite-packing error only if it lies in the **outer contact face**.

The exact remaining force-bulk target is therefore:

> **Outer-shell force-bulk theorem.** Bound the number of contact-isolated source points in the outer contact face sharply enough to combine with C52 and the global minimum-diameter comparison.

---

## 5. Geometric gap form

Define the outer-area gap inside the force hull

\[
H:=\operatorname{area}(F)-A_{bnd}\ge0.
\tag{C52.13}
\]

Then C52.7 gives the sharper exact form

\[
\boxed{
 m+Z_{def}
\le
\frac{2}{\sqrt3}(\operatorname{area}(F)-H)
+rac B2+1.}
\tag{C52.14}
\]

So any substantial area of `F` belonging to the outer contact face appears with a favorable explicit deficit `-(2/sqrt3)H`. Outer-face isolated points are the only points capable of compensating for that deficit.

This is the natural bridge to an outer-shell packing estimate.

## Regression audit

- A huge bounded convex defect face with `Theta(D^2)` isolated points is allowed locally, but C52 shows its points are already charged by the same global area/boundary budget as the core.
- One regular shell with a large invisible interior that lies in the **outer** contact face remains a live regression; this is now the sole macroscopic force-bulk geometry.
- C52 does not count contact-isolated points outside the force hull or elsewhere in the outer contact face.
