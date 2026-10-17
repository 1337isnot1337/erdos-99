> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_reuleaux_aggregate_composition_energy_2026-09-09.md) · source SHA-256 `f2f9e2e840d9a3ab823c67964c3accb35ad2531604ab1423f29d6d788eb6ea2b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AB02ECDD6D66","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — additive Reuleaux energy controls the full Reinhardt leaf composition

**Date:** 2026-09-09  
**Run type:** exact constant-width variational inequality / composition stability  
**Target:** Target C cyclic `d_H=0` Reinhardt endpoint  
**Depends on:** LC Reuleaux leaf composition in this PR; PR #118 exact Reinhardt completion and WG finite-packing area bound  
**External literature:** none for the new variational inequality  
**Computation:** displayed decimals only

## LEVEL I STATUS

`STILL OPEN`

The previous CC theorem tested one Reuleaux arc at a time and obtained a cubic penalty for the largest arc. The same support-function method can be optimized **simultaneously on all arcs**.

The resulting inequality is additive and sharp for regular Reuleaux polygons.

Let `R` be the width-`D` Reuleaux completion. Let its defining arcs have normal-angle lengths

$$
\phi_0,\ldots,\phi_{r-1}>0,
\qquad
\sum_i\phi_i=\pi.
\tag{AE.1}
$$

Then

$$
\boxed{
\frac{\pi D^2}{4}-\operatorname{area}(R)
\ge
\frac{D^2}{4}
\sum_{i=0}^{r-1}
\left(
2\tan\frac{\phi_i}{2}-\phi_i
\right).
}
\tag{AE.2}
$$

Because

$$
2\tan\frac\phi2-\phi\ge\frac{\phi^3}{12},
\tag{AE.3}
$$

we obtain

$$
\boxed{
\frac{\pi D^2}{4}-\operatorname{area}(R)
\ge
\frac{D^2}{48}\sum_i\phi_i^3.
}
\tag{AE.4}
$$

Insert the exact leaf composition

$$
\phi_i=\ell_i\frac\pi q,
\qquad
\ell_i\in\mathbb Z_{>0},
\qquad
\sum_i\ell_i=q.
$$

Then

$$
\boxed{
\sum_i\ell_i^3
\le
\frac{48q^3}{\pi^3D^2}
\left(
\frac{\pi D^2}{4}-\operatorname{area}(R)
\right).
}
\tag{AE.5}
$$

PR #118 WG gives

$$
\frac{\pi D^2}{4}-\operatorname{area}(F)
\le(C_W+o(1))D,
$$

where

$$
C_W
=\frac\pi2-
\frac{2-\sqrt3}{4}\sqrt{2\pi\sqrt3}
=1.349811370903931\ldots .
$$

Since `F subset R`, the Reuleaux deficit is no larger. With `q/(pi D)->1`, AE.5 yields the full cubic-energy bound

$$
\boxed{
\sum_i\ell_i^3
\le
(48C_W+o(1))D^2
= (64.7909458034\ldots+o(1))D^2.
}
\tag{AE.6}
$$

Consequences include

$$
\boxed{
\max_i\ell_i
\le
(48C_W+o(1))^{1/3}D^{2/3}
=(4.0164\ldots+o(1))D^{2/3},
}
\tag{AE.7}
$$

and hence

$$
\boxed{
\Delta(H)
\le
(4.0164\ldots+o(1))D^{2/3}+1.
}
\tag{AE.8}
$$

The same inequality also controls the complete distribution of diameter branching, not only the maximum.

---

## 1. Constant-width support-function setup

Write the support function of `R` as

$$
h(\theta)=\frac D2+p(\theta),
$$

with the constant-width normalization

$$
p(\theta+\pi)=-p(\theta).
\tag{1.1}
$$

Translations add first harmonics to `p`; they will be quotient out automatically below.

Let

$$
\rho=h+h''
$$

be the radius-of-curvature density in normal-angle coordinates, interpreted piecewise on the Reuleaux arcs and vertex normal intervals. Put

$$
f:=\rho-\frac D2=p+p''.
\tag{1.2}
$$

For a Reuleaux polygon:

- on every circular arc normal interval `I_i`, `rho=D`, hence `f=D/2`;
- on the antipodal vertex-normal interval `I_i+pi`, `rho=0`, hence `f=-D/2`.

The intervals

$$
I_i\cup(I_i+\pi)
$$

are pairwise disjoint up to endpoints and cover the projective normal circle.

Let

$$
L:=-\partial_\theta^2-1.
$$

Then

$$
Lp=-f.
$$

The first-harmonic kernel of `L` is exactly the translation freedom. Since `f` is the curvature data of a closed body, it is orthogonal to that kernel.

The standard support-function area formula gives

$$
\operatorname{area}(R)
=\frac12\int_0^{2\pi}(h^2-(h')^2)\,d\theta.
$$

Using antiperiodicity, the disk-area deficit is

$$
\boxed{
\delta_R
:=\frac{\pi D^2}{4}-\operatorname{area}(R)
=\frac12\int((p')^2-p^2)
=\frac12\langle f,L^{-1}f\rangle,
}
\tag{1.3}
$$

where `L^{-1}` means the inverse on the first-harmonic orthogonal complement.

---

## 2. The optimal local interval test

Fix one arc interval and rotate coordinates so

$$
I=[0,\phi],
\qquad0<\phi<\pi.
$$

Instead of the cosine bump used in CC, solve the exact Dirichlet variational problem

$$
-L?\quad\text{equivalently}\quad
-g''-g=1,
\qquad
g(0)=g(\phi)=0.
\tag{2.1}
$$

The solution is

$$
\boxed{
 g_\phi(x)
 =\cos x+\tan\frac\phi2\sin x-1
 =\frac{\cos(x-\phi/2)}{\cos(\phi/2)}-1.
}
\tag{2.2}
$$

It is nonnegative on the interval. Its integral is

$$
\begin{aligned}
C(\phi)
&:=\int_0^\phi g_\phi(x)\,dx\\
&=\sin\phi+	an\frac\phi2(1-\cos\phi)-\phi\\
&=\boxed{2\tan\frac\phi2-\phi.}
\end{aligned}
\tag{2.3}
$$

Since `Lg_phi=1` on the interval and `g_phi=0` at both endpoints,

$$
\boxed{
\int_0^\phi((g_\phi')^2-g_\phi^2)\,dx
=C(\phi).
}
\tag{2.4}
$$

Extend `g_phi` by zero outside `I`, and impose antiperiodicity by putting

$$
g(\theta+\pi)=-g(\theta).
$$

For this paired test:

$$
\boxed{
\langle f,g\rangle=DC(\phi),
\qquad
\langle g,Lg\rangle=2C(\phi).
}
\tag{2.5}
$$

Derivative jumps at the interval endpoints cause no boundary term because `g` itself vanishes there.

---

## 3. All arc tests can be added with no cross-energy

For each Reuleaux arc interval `I_i`, construct the paired antiperiodic test `g_i` from Section 2.

Their supports are pairwise disjoint up to measure-zero endpoints. Therefore

$$
\langle g_i,Lg_j\rangle=0
\qquad(i\ne j),
\tag{3.1}
$$

and for

$$
g:=\sum_i g_i
$$

we have

$$
\boxed{
\langle f,g\rangle
=D\sum_iC(\phi_i),
}
\tag{3.2}
$$

$$
\boxed{
\langle g,Lg\rangle
=2\sum_iC(\phi_i).
}
\tag{3.3}
$$

Project `g` orthogonally away from the first-harmonic kernel if necessary. This changes neither (3.2) nor (3.3): `f` is orthogonal to the kernel and `L` annihilates it.

Cauchy-Schwarz in the positive `L` energy gives

$$
\langle f,g\rangle^2
\le
\langle f,L^{-1}f\rangle
\langle g,Lg\rangle.
$$

Using (1.3), (3.2), and (3.3):

$$
D^2\left(\sum_iC_i\right)^2
\le
(2\delta_R)\left(2\sum_iC_i\right).
$$

Every `C_i>0`, so division gives

$$
\boxed{
\delta_R
\ge\frac{D^2}{4}\sum_iC(\phi_i).
}
$$

This proves AE.2. `square`

The additivity is the key gain over CC: the global positive quadratic form cannot simultaneously hide many long Reuleaux arcs.

---

## 4. Cubic composition energy

For `x>=0`,

$$
\tan x\ge x+\frac{x^3}{3}.
$$

With `x=phi/2`,

$$
2\tan\frac\phi2-\phi
\ge\frac{\phi^3}{12}.
$$

Insert into AE.2 to obtain AE.4.

LC gives

$$
\phi_i=\frac{\pi\ell_i}{q}.
$$

Hence

$$
\delta_R
\ge
\frac{D^2}{48}
\frac{\pi^3}{q^3}
\sum_i\ell_i^3,
$$

which rearranges to AE.5.

---

## 5. Insert the sharp available packing bound

WG gives

$$
\delta_F
:=\frac{\pi D^2}{4}-\operatorname{area}(F)
\le(C_W+o(1))D.
$$

The exact completion has

$$
F\subset R,
$$

so

$$
0\le\delta_R\le\delta_F.
$$

Therefore AE.5 gives

$$
\sum_i\ell_i^3
\le
\frac{48(C_W+o(1))q^3}{\pi^3D}.
\tag{5.1}
$$

The exact Reinhardt relation gives

$$
q=\pi D+o(D),
$$

hence AE.6.

Numerically

$$
48C_W=64.7909458033887\ldots .
$$

Taking cube roots gives AE.7-AE.8.

---

## 6. Distributional consequences

AE.6 is stronger than a maximum-degree estimate.

### Tail count

For every threshold `L>0`,

$$
\boxed{
\#\{i:\ell_i\ge L\}
\le
\frac{(48C_W+o(1))D^2}{L^3}.
}
\tag{6.1}
$$

Thus, for example, only `O(D^(1/2))` cycle vertices can have `ell_i` of order `D^(1/2)`, and no part can be larger than order `D^(2/3)`.

### Quadratic branching energy

Cauchy-Schwarz/Hölder gives

$$
\left(\sum_i\ell_i^2\right)^2
\le
\left(\sum_i\ell_i\right)
\left(\sum_i\ell_i^3\right).
$$

Since `sum ell_i=q=Theta(D)`, AE.6 yields

$$
\boxed{
\sum_i\ell_i^2=O(D^{3/2}).
}
\tag{6.2}
$$

Hence the squared diameter-degree excess is subquadratic.

### Core-size bound

Hölder also gives

$$
q^3
=\left(\sum_i\ell_i\right)^3
\le r^2\sum_i\ell_i^3.
$$

Using (5.1):

$$
r^2
\ge
\frac{\pi^3D}{48C_W+o(1)}.
$$

Therefore

$$
\boxed{
\liminf\frac r{\sqrt D}
\ge
\sqrt{\frac{\pi^3}{48C_W}}
=0.6917794379\ldots .
}
\tag{6.3}
$$

This recovers the WG/Firey-Sallee core-size constant from the stronger composition-energy theorem.

---

## 7. Sharpness and the regular Reuleaux polygon

The function

$$
C(\phi)=2\tan(\phi/2)-\phi
$$

is strictly convex because

$$
C'(\phi)=\tan^2(\phi/2),
\qquad
C''(\phi)=\tan(\phi/2)\sec^2(\phi/2)>0.
\tag{7.1}
$$

For `r` equal arc lengths `phi_i=pi/r`, AE.2 becomes

$$
\delta_R
\ge
\frac{D^2}{4}
\left(
2r\tan\frac\pi{2r}-\pi
\right).
\tag{7.2}
$$

The right side is exactly the known disk-area deficit of the regular Reuleaux `r`-gon. Thus AE.2 is sharp on the regular family.

More generally Jensen gives

$$
\sum_iC(\phi_i)
\ge
rC(\pi/r),
$$

so AE.2 independently recovers the usual regular-Reuleaux maximal-area envelope for a fixed number of arcs.

The new information is stronger: it retains the full composition instead of discarding it through Jensen.

---

## 8. Integer-balanced refinement

LC gives the additional arithmetic constraint

$$
\phi_i=\frac{\pi\ell_i}{q},
\qquad \ell_i\in\mathbb Z_{>0}.
$$

For fixed integers `q,r`, strict convexity of `C` means the sum in AE.2 is minimized when the positive integer parts `ell_i` differ by at most one.

Write

$$
q=ar+b,
\qquad
0\le b<r.
$$

Then every exact Reinhardt completion with this `(q,r)` satisfies

$$
\boxed{
\delta_R
\ge
\frac{D^2}{4}
\left[
(r-b)C\left(\frac{a\pi}{q}\right)
+bC\left(\frac{(a+1)\pi}{q}\right)
\right].
}
\tag{8.1}
$$

This is strictly stronger than the continuous regular-`r` envelope whenever `r` does not divide `q`.

It provides a finite arithmetic filter on possible odd cycle lengths `r` for each exact terminal count `q`.

---

## 9. What this changes

The exact `d_H=0` branch now has a quantitative global branching budget:

```text
sum ell_i = q ~ pi D,
sum ell_i^3 <= (64.79095+o(1)) D^2,
sum ell_i^2 = O(D^(3/2)),
max ell_i <= (4.0164+o(1)) D^(2/3),
r >= (0.6917794-o(1)) sqrt(D).
```

Since `deg_H(v_i)=ell_i+1`, these are direct diameter-graph constraints, not only Reuleaux geometry.

---

## 10. Next theorem

The next useful coupling is with the exact KKT stress polygon and the curvature/degree identity:

> convert the cubic degree budget into a quantitative bound on the geometry of the KKT-polygon facets or on the aggregate variation of contact stress across the odd diameter core.

A second route is finite arithmetic: combine the integer-balanced bound AE.8.1 with the cyclotomic Reinhardt sign condition to exclude large classes of `(q,r,ell)` compositions.

Neither route requires returning to generic near-disk stability.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For width-D Reuleaux completion R write h=D/2+p, f=(h+h'')-D/2 and
L=-d^2/dtheta^2-1. Then
  delta_R=pi D^2/4-area(R)=1/2 <f,L^{-1}f>.

On one radius-D arc interval I of length phi, f=D/2; on I+pi, f=-D/2.
Solve the optimal local Dirichlet test
  -g''-g=1, g(0)=g(phi)=0,
so
  g=cos x+tan(phi/2)sin x-1,
  C(phi)=int g=2tan(phi/2)-phi.
Pair it antiperiodically. Then
  <f,g>=D C(phi),
  <g,Lg>=2 C(phi).
The tests for distinct Reuleaux arcs have disjoint supports, so summing them and using
energy Cauchy gives
  delta_R >= D^2/4 sum_i C(phi_i).
Since C(phi)>=phi^3/12,
  delta_R >= D^2/48 sum phi_i^3.

LC: phi_i=pi ell_i/q, sum ell_i=q. WG: delta_R<=(C_W+o(1))D,
C_W=1.349811370903931.... Therefore
  sum ell_i^3 <= (48 C_W+o(1))D^2
              =(64.7909458...+o(1))D^2.
Consequences:
  max ell_i <= (4.0164...+o(1))D^(2/3),
  sum ell_i^2=O(D^(3/2)),
  r >= (0.6917794379...-o(1))sqrt(D).

C(phi) is strictly convex, so for fixed integer q,r the minimum occurs at the balanced
integer composition q=ar+b. This gives an exact finite arithmetic area lower bound.

Next: couple the cubic degree budget to the exact KKT stress polygon / cyclotomic sign word.
```
