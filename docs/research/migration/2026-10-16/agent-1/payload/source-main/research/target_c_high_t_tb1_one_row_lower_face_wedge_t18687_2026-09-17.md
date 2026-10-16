# Target C-II — a one-row LOWER blocker forces a wrong-phase train terminal in its owner strip

**Date:** 2026-09-17  
**Status:** proof-only local strengthening of the one-row LOWER exact-swap branch; no canonical promotion claimed  
**Scope:** one-sign strong-TB1 interfaces through `t=(q-k)/D<=1.8687`  
**Dependencies:** one-row LOWER classification; transversal/rooted-shore sign theorem; exact contact-swap algebra; strict unit-rhombus crossing-angle theorem; train pseudosegment topology  
**Certificate:** `research/verify_target_c_high_t_tb1_one_row_lower_face_wedge_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The one-row theorem identifies every LOWER exact-swap witness with the diagonal of one strict unit rhombus on its unique support row. Combining that identification with the exact contact swap determines the local face almost completely.

Let the owner layer `R_i` lie between consecutive selected rows `tau_i,tau_{i+1}`. Suppose a LOWER blocker has one endpoint in the fixed region left of `tau_i` and the moving endpoint in `R_i`, so its unique support row is `tau_i`. Let

\[
a=u_i,
\qquad b=-u_{i+1}
\tag{FW.1}
\]

be the two rooted boundary-contact vectors from the fixed exterior into `R_i`, as fixed by the transversal/rooted-shore sign theorem. Let

\[
\varepsilon_i:=\pi-\angle(a,b)>0
\tag{FW.2}
\]

be the residual TB1 opening angle. On the one-sign branch,

\[
\varepsilon_i=O(D^{-1}).
\tag{FW.3}
\]

The blocker rhombus has `a` as one side direction. Orient its other unit side as `c` so that the blocker diagonal is

\[
r=a+c.
\tag{FW.4}
\]

The exact swap of `R_i` is

\[
v_i=-(a+b),
\tag{FW.5}
\]

so the blocker vector becomes

\[
r'=r+v_i=c-b.
\tag{FW.6}
\]

The initial pair is previously strict and the exact swap hits the lower metric boundary:

\[
|a+c|>1,
\qquad
|c-b|\le1.
\tag{FW.7}
\]

These two inequalities force one scalar wedge parameter. After a rigid rotation and, if necessary, reflection, take

\[
\arg a=0,
\qquad
\arg b=\pi-\varepsilon_i.
\tag{FW.8}
\]

For all sufficiently large `D`, `0<\varepsilon_i<\pi/6`. Then there is a unique

\[
\boxed{0<\delta_i\le\varepsilon_i}
\tag{FW.9}
\]

such that

\[
\boxed{
\arg c={2\pi\over3}-\delta_i.
}
\tag{FW.10}
\]

Consequently the blocker support face has acute projective row/transverse angle

\[
\boxed{
{\pi\over3}+\delta_i,
}
\tag{FW.11}
\]

while the same transverse train has projective separation from the opposite boundary row `tau_{i+1}` equal to

\[
\boxed{
{\pi\over3}+\delta_i-\varepsilon_i
\le {\pi\over3}.
}
\tag{FW.12}
\]

Strict unit-rhombus train crossings require projective separation strictly larger than `pi/3`. Therefore the transverse train through the blocker rhombus crosses `tau_i` but cannot cross `tau_{i+1}`.

By train pseudosegment topology it cannot cross `tau_i` a second time either. Hence it must terminate on the outer or bounded exceptional boundary inside the owner strip `R_i`:

\[
\boxed{
\sigma(e)\in\Gamma(\tau_i)\setminus\Gamma(\tau_{i+1}),
\qquad
\sigma(e)\text{ has a terminal occurrence in }R_i.
}
\tag{FW.13}
\]

The right-support case is symmetric, with

\[
\sigma(e)\in\Gamma(\tau_{i+1})\setminus\Gamma(\tau_i).
\tag{FW.14}
\]

Thus a LOWER blocker is not merely a near-unit diagonal on one row. It is an exact one-face defect which forces one transverse train into the opposite `60`-degree phase branch and forces that train to die inside the owner strip.

---

## 1. The blocker diagonal uses one rooted row side

By the one-row LOWER classification, the blocker endpoints are opposite vertices of the unique strict unit rhombus `F` crossed by its support row `tau_i`.

The midpoint centerline of `tau_i` joins the midpoints of the two opposite contact edges parallel to the row contact vector. Under the rooted-shore convention, those two row edges point from the fixed side of `tau_i` into the owner layer with direction `a=u_i`.

Choose the fixed blocker endpoint as the origin. Of the two possible opposite diagonals of `F`, the one leading into `R_i` can therefore be written

\[
r=a+c,
\]

for one unit vector `c` parallel to the other pair of rhombus sides. This proves (FW.4).

The vector `c` is the projective phase of the second complete stopped train crossing `tau_i` in the blocker rhombus.

---

## 2. The exact contact swap cancels the rooted row side

For the physical layer between `tau_i` and `tau_{i+1}`, the transversal/rooted-shore theorem gives the two boundary vectors

\[
a=u_i,
\qquad b=-u_{i+1}.
\]

The exact TB1 contact swap translates every point of `R_i` by

\[
v_i=-(a+b).
\]

Only the blocker endpoint inside `R_i` moves. Hence

\[
r'=a+c-(a+b)=c-b,
\]

which is (FW.6).

No approximation is used here.

---

## 3. The two metric inequalities determine the face wedge

Normalize as in (FW.8). Write

\[
\phi:=\arg c
\]

with `phi` chosen in `(-pi,pi]`.

Because `|a|=|c|=1`, the original strict inequality gives

\[
|a+c|>1
\iff
2+2\cos\phi>1
\iff
\cos\phi>-{1\over2}.
\tag{FW.15}
\]

Thus

\[
-{2\pi\over3}<\phi<{2\pi\over3}.
\tag{FW.16}
\]

Similarly, `|b|=|c|=1` and the lower-bound violation after the swap give

\[
|c-b|\le1
\iff
2-2\cos(\phi-(\pi-\varepsilon_i))\le1.
\tag{FW.17}
\]

Therefore the ordinary angular distance between `c` and `b` is at most `pi/3`.

Since `b` has argument `pi-epsilon_i`, the allowed arc for `c` is

\[
\left[{2\pi\over3}-\varepsilon_i,
      {4\pi\over3}-\varepsilon_i\right]
\pmod{2\pi}.
\tag{FW.18}
\]

For `0<epsilon_i<pi/6`, intersecting (FW.18) with (FW.16) leaves exactly

\[
{2\pi\over3}-\varepsilon_i
\le \phi
< {2\pi\over3}.
\tag{FW.19}
\]

Hence there is a unique `delta_i` satisfying (FW.9)--(FW.10).

This is an exact local normal form for every sufficiently large LOWER blocker.

---

## 4. Exact length and defect formulas

Equation (FW.10) gives the original blocker length

\[
\begin{aligned}
|r|^2
&=2+2\cos\left({2\pi\over3}-\delta_i\right)\\
&=2-\cos\delta_i+\sqrt3\sin\delta_i.
\end{aligned}
\tag{FW.20}
\]

The projective acute angle between the support-row phase `[a]` and the transverse phase `[c]` is

\[
\pi-\left({2\pi\over3}-\delta_i\right)
={\pi\over3}+\delta_i,
\tag{FW.21}
\]

because `delta_i<pi/6` for large `D`. This proves (FW.11). Thus `delta_i` is exactly the strict-rhombus angular defect of the blocker face above `pi/3`.

The post-swap angle between `c` and `b` is

\[
(\pi-\varepsilon_i)
-\left({2\pi\over3}-\delta_i\right)
={\pi\over3}+\delta_i-\varepsilon_i.
\tag{FW.22}
\]

Hence

\[
|r'|^2
=2-2\cos\left({\pi\over3}+\delta_i-\varepsilon_i\right).
\tag{FW.23}
\]

Because `delta_i<=epsilon_i`, (FW.23) is at most one. Equality holds exactly when

\[
\delta_i=\varepsilon_i.
\tag{FW.24}
\]

Thus a LOWER witness reaches a new unit contact exactly when its blocker-face defect uses the whole local opening wedge; it becomes strictly subunit exactly when

\[
0<\delta_i<\varepsilon_i.
\tag{FW.25}
\]

---

## 5. The blocker transverse train cannot cross the other boundary

The opposite selected row has rooted phase

\[
[u_{i+1}]=[-b].
\]

In the normalization (FW.8), a real representative of `u_{i+1}` has argument `-epsilon_i`. The ordinary difference from `c` is

\[
{2\pi\over3}-\delta_i+\varepsilon_i.
\]

This lies in `(pi/2,pi)` for all sufficiently large `D`. Therefore its acute projective complement is

\[
\pi-\left({2\pi\over3}-\delta_i+\varepsilon_i\right)
={\pi\over3}+\delta_i-\varepsilon_i
\le {\pi\over3}.
\tag{FW.26}
\]

But two complete stopped trains can cross in a strict unit rhombus only when their acute projective contact-direction gap is strictly greater than `pi/3`.

Let `sigma(e)` be the transverse train with phase `[c]` through the blocker face. Then

\[
\boxed{
\sigma(e)\notin\Gamma(\tau_{i+1}).
}
\tag{FW.27}
\]

while by construction

\[
\sigma(e)\in\Gamma(\tau_i).
\tag{FW.28}
\]

This proves the set difference in (FW.13).

---

## 6. The transverse train must terminate in the owner strip

At its unique crossing with `tau_i`, the midpoint path of `sigma(e)` enters the strip `R_i`. Two complete trains meet at most once, so `sigma(e)` cannot leave `R_i` by crossing `tau_i` again. Equation (FW.27) says it does not leave by crossing `tau_{i+1}`.

Every complete stopped train is a finite path. Therefore the portion of `sigma(e)` inside `R_i` must terminate on an outer or bounded exceptional boundary component of the strip.

This is exactly the terminal-topology mechanism used in the adjacent crossing-neighborhood theorem, now forced individually by every LOWER blocker rather than obtained from a symmetric-difference count.

The right-support case is obtained by reflecting the strip and interchanging `tau_i,tau_{i+1}`.

---

## 7. Consequences for the direct LOWER population

Combine this theorem with the direct exact-swap witness injection theorem. If LOWER is the metric winner, there are more than

\[
\left({s_0\over4}-o(1)\right)D
\]

distinct blockers with injective owner layers.

Each such blocker now carries four simultaneous pieces of exact local structure:

```text
one unique support row;
one unique strict unit blocker rhombus;
one blocker-face defect 0 < delta_i <= epsilon_i = O(1/D);
one transverse train which crosses the support row but terminates before the opposite boundary.
```

Splitting by whether the support is the left or right boundary of the owner strip leaves a linear same-orientation subfamily. In that subfamily all blocker transverse phases lie in the same shrinking projective neighborhood of one of the two `pi/3` companion phases of the common row phase.

The global stopped-train terminal ledger is only `O(D)`, so this linear terminal family is not itself a contradiction. The remaining LOWER closure problem is now sharper: exploit the fact that a positive-density family of distinct owner strips each contains a forced terminal from the same wrong-phase train sector while almost all of the row's `0.6536D` crossing neighborhood continues across the strip in the opposite dense common-column sector.

A viable next theorem should charge these forced wrong-phase terminals against either the atomic three-phase endpoint budget or the owner-strip KKT/terminal energy, rather than treating them as generic terminal occurrences.

**Disposition:** derived an exact face-wedge parameter `0<delta_i<=epsilon_i` for every one-row LOWER blocker, identified `delta_i` with the blocker rhombus defect, and proved that the blocker transverse train cannot cross the owner strip's opposite boundary and therefore must terminate inside that strip. C-II and Level I remain open.
