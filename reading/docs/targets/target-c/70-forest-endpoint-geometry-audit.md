> Generated reading edition · [exact source](../../../../docs/targets/target-c/70-forest-endpoint-geometry-audit.md) · source SHA-256 `353798b0cb60fd552be6bb8fc29a26306b3b84918fbcc436c838848b3b985e93`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — sharp forest endpoint geometry audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module independently certifies the valid mathematics from stale PR #219 against
canonical Sections 58, 62, 63, 66, 67, 68, and 69. It does not inherit that PR's old
section numbering or theorem-state snapshot.

The result has two layers.

1. Every Woodall-forest subsequence with `q/D -> x` satisfies
   $$
   \liminf {\operatorname{area}(F)\over D^2}\ge {x+\sin x\over4},
   \qquad
   \liminf {r_o(F)\over D}\ge {1\over2}\sin(x/2).
   $$
2. At the sharp Section-66 endpoint,
   $$
   q/D\to2\kappa,
   \quad e_{BB}/D,x_B/D\to\kappa,
   \quad \kappa=2\cos\kappa,
   $$
   there are `(kappa-o(1))D` **distinct** unloaded vertices in an `o(1)` force-hull
   boundary layer, each on a two-edge outer detour over a nonunit loaded hull side of
   length `2-o(1)`. Each has an extra unit contact with inward normal component
   `sqrt(3)/2-o(1)`, and at least `(kappa/2-o(1))D` such extra contacts are distinct.

No KKT coefficient floor, rejected Reuleaux-cap argument, hull-saturated
normalization, or deletion of source points is used.

---

## 70.1 Heterogeneous doubled gaps give force-hull area

Let

$$
a_D:=\arcsin{1\over2D},
\qquad d_H=q-h>0.
$$

Order the `h` projective actual-diameter directions cyclically with gaps
`g_1,...,g_h`, summing to `pi`. Canonical Section 66 proves every gap is at least
`2a_D` and at least `d_H` gaps are at least `4a_D`.

Put

$$
P_H:=D\operatorname{conv}\{\pm u_e:e\in E(H)\}\subseteq F-F.
$$

Then

$$
\operatorname{area}(P_H)=D^2\sum_i\sin g_i.
\tag{70.1}
$$

Since `sin` is concave on `[0,pi]`, the minimum under the gap lower bounds and fixed
sum occurs with all but one gap at a lower bound. The two finite extreme types are

$$
A_D=(h-d_H)\sin(2a_D)+(d_H-1)\sin(4a_D)
     +\sin(2(q-2)a_D),
\tag{70.2}
$$

and, when an ordinary gap exists,

$$
A_N=(h-d_H-1)\sin(2a_D)+d_H\sin(4a_D)
     +\sin(2(q-1)a_D).
\tag{70.3}
$$

No ordering between these finite expressions is assumed.

Section 58 gives one full-source circumcenter `o` and `L_D=O(D^(3/4))=o(D)` such that
every actual diameter midpoint is within `L_D` of `o`. Hence

$$
d_{Haus}(F-o,-(F-o))\le2L_D
$$

and

$$
\operatorname{area}(F-F)
\le4\operatorname{area}(F)+4L_D\operatorname{per}(F)+4\pi L_D^2.
\tag{70.4}
$$

Along any forest subsequence with `q/D->x`, both (70.2) and (70.3) tend to
`x+sin x`: the lower-bound gaps contribute `x` and the free gap contributes `sin x`.
Therefore

$$
\boxed{
\liminf {\operatorname{area}(F)\over D^2}
\ge{x+\sin x\over4}.}
\tag{70.5}
$$

---

## 70.2 The same gaps give a common-center inball

Let `g_max=max_i g_i`. If the largest gap is doubled, the remaining gap lower bounds
sum to at least `2(q-2)a_D`; if it is ordinary the lower sum is larger. Thus

$$
\boxed{g_{max}\le\pi-2(q-2)a_D.}
\tag{70.6}
$$

The centrally symmetric polygon `P_H/2` has circumradius `D/2`, hence centered
inradius at least

$$
{D\over2}\sin((q-2)a_D).
$$

Every vertex of `P_H/2` lies within `L_D` of `F-o`. Support-function comparison gives

$$
B\!\left(o,{D\over2}\sin((q-2)a_D)-L_D\right)\subseteq F.
\tag{70.7}
$$

Consequently, along `q/D->x`,

$$
\boxed{
\liminf {r_o(F)\over D}\ge {1\over2}\sin(x/2).}
\tag{70.8}
$$

---

## 70.3 Geometry at the sharp Section-66 endpoint

Canonical Section 66 proves that approach to

$$
\kappa=2\cos\kappa=1.0298665293\ldots
$$

forces

$$
q/D\to2\kappa,
\qquad e_{BB}/D,x_B/D\to\kappa,
\qquad \operatorname{per}(F)/D\to3\kappa,
\qquad u_B+c_B=o(D).
\tag{70.9}
$$

Equations (70.5) and (70.8) yield

$$
\boxed{
\liminf {\operatorname{area}(F)\over D^2}
\ge A_\kappa:={2\kappa+\sin(2\kappa)\over4}
=0.7356414549\ldots,}
\tag{70.10}
$$

$$
\boxed{
\liminf {r_o(F)\over D}
\ge {1\over2}\sin\kappa
=0.4286151341\ldots.}
\tag{70.11}
$$

Since `area(K)<=pi D^2/4`,

$$
\limsup {\operatorname{area}(K\setminus F)\over D^2}
\le {\pi\over4}-A_\kappa
=0.0497567084\ldots .
\tag{70.12}
$$

For every source point outside `F`, the open radius-`1/2` disks are pairwise disjoint,
lie in `K_{+1/2}`, and avoid the interior of `F_{-1/2}`. Steiner's outer formula and
the convex inner-strip estimate therefore give the conservative bound

$$
\boxed{
\limsup {Z_{ext}\over D^2}
\le {4\over\pi}\left({\pi\over4}-A_\kappa\right)
=0.0633522087\ldots .}
\tag{70.13}
$$

---

## 70.4 Almost all nonunit sides are shallow two-edge detours

Let the loaded force-hull vertices be `b_i`, let `s_i=|b_i-b_{i+1}|`, and let the
distinguished outer-contact interval from `b_i` to `b_{i+1}` have `ell_i` unit-edge
occurrences. Canonical Section 63 gives

$$
x_B=\sum_i(\ell_i-1).
$$

Let `M_D={i:s_i>1}` and `m=|M_D|`. Since `u_B=x_B-m`,

$$
u_B=
\sum_{i\in M_D}(\ell_i-2)
+\sum_{i\notin M_D}(\ell_i-1).
\tag{70.14}
$$

At the endpoint `u_B=o(D)` and `m=(kappa-o(1))D`. Hence all but `o(D)` nonunit hull
sides have `ell_i=2`. Write those paths as

$$
(b_i,z_i,b_{i+1}).
$$

Also

$$
b-\operatorname{per}(F)=\sum_i(\ell_i-s_i)=o(D).
$$

Thus for the two-edge family

$$
\sum_i(2-s_i)=o(D).
\tag{70.15}
$$

After discarding only `o(D)` further indices, uniformly

$$
s_i=2-o(1).
\tag{70.16}
$$

In coordinates with the hull side on `y=0` and `F` in `y>=0`, the intermediate point
has height

$$
t_i=\sqrt{1-s_i^2/4}=o(1).
\tag{70.17}
$$

Cauchy-Schwarz and (70.15) show that the associated triangular outer pockets have
total area `o(D)`.

Every `z_i` is unloaded: it is a contact-core vertex inside the hull interval between
consecutive loaded hull vertices. Canonical C26 gives

$$
3\le\deg_C(z_i)\le5.
$$

---

## 70.5 Triangle freeness forces an almost-normal inward contact

Choose a contact neighbor `w_i` of `z_i` other than the two hull-side endpoints and
write

$$
w_i-z_i=(X_i,Y_i),
\qquad X_i^2+Y_i^2=1.
$$

Since `w_i in F`, `t_i+Y_i>=0`. Triangle-freeness plus unit separation gives

$$
|w_i-b_i|>1,
\qquad |w_i-b_{i+1}|>1.
$$

Writing `t_i=sin(alpha_i)` and `s_i/2=cos(alpha_i)`, these imply

$$
\cos\alpha_i |X_i|-\sin\alpha_iY_i<1/2.
$$

If `Y_i=sin(beta_i)` with `beta_i in[-pi/2,pi/2]`, then the hull-side condition gives
`beta_i>=-alpha_i`, while the last inequality gives
`cos(alpha_i+beta_i)<1/2`. Hence

$$
\boxed{Y_i\ge\sqrt3/2-o(1)}
\tag{70.18}
$$

uniformly. The extra contact penetrates from an `o(1)` boundary layer to inward normal
depth at least `sqrt3/2-o(1)`.

---

## 70.6 The shallow intermediate vertices are asymptotically all distinct

Suppose one physical unloaded vertex `z` served two good hull sides.

If the sides share a loaded endpoint, their other endpoints both approach the antipode
of that endpoint on the unit circle centered at `z`, so two distinct source points
become `o(1)` apart.

If the sides have four distinct endpoints, compare their supporting lines. If the acute
line angle stays bounded below, both lines pass `o(1)` from `z` and the length-`2-o(1)`
sides properly cross. If the line angle tends to zero, two endpoint directions on the
unit circle about `z` become `o(1)` apart. Both alternatives contradict, respectively,
convexity or unit separation.

Therefore

$$
\boxed{|\{z_i\}|=(\kappa-o(1))D.}
\tag{70.19}
$$

Choose one extra inward contact at each distinct `z_i`. An undirected edge can be
chosen by at most its two endpoints, so at least

$$
\boxed{(\kappa/2-o(1))D}
\tag{70.20}
$$

distinct penetration contacts occur.

Every containing unloaded component has at least three distinct loaded attachments by
canonical Section 62. The theorem does not assert that the penetration edges belong to
distinct unloaded components or carry a uniform positive KKT weight.

---

## 70.7 Canonical effect

The sharp Woodall-forest endpoint forces a concrete physical interface:

```text
q/D -> 2 kappa
  -> area(F)/D^2 >= 0.73564145...
  -> centered inradius >= 0.42861513... D
  -> (kappa-o(1))D nonunit hull sides of length 2-o(1)
  -> (kappa-o(1))D distinct unloaded boundary-layer vertices
  -> at least (kappa/2-o(1))D distinct unit contacts penetrating inward
     with normal component sqrt(3)/2-o(1).
```

Together with canonical Sections 68–69, the next target is a global interface/phase
theorem charging these penetrations against the forced coherent grain structure or a
strict diameter-decreasing deformation.
