> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_uniform_width_collapse_2026-09-09.md) · source SHA-256 `b3d17cb6be326c6c599b032abb3e50bac18b10d46ca9d88f7eb9700ad40370a8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8DC434EF0E29","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — every cyclic force hull is uniformly constant-width to order `1/D`

**Date:** 2026-09-09  
**Repository branch:** PR #118 after DA/RP/R2/AD  
**Run type:** exact difference-body inradius theorem / uniform geometric stability  
**Target:** complete cyclic primitive endpoint  
**Depends on:** C67 projective diameter-direction separation, RP/R2 ladder notation, DA inclusion `P_H subset F-F`  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The cyclic reports previously controlled the **average** width through

$$
\operatorname{per}(F)=q=\pi D-O(D^{-1}),
$$

and controlled the force-hull area only to a much coarser linear error through packing. The actual diameter directions give a stronger pointwise statement.

### Theorem UW — uniform width collapse

Put

$$
\delta:=2\arcsin\frac1{2D},
\qquad
q_R(D):=\frac\pi\delta,
\qquad
s:=q_R(D)-q\ge0,
\qquad
d:=d_H\in\{0,1,2\}.
\tag{UW.1}
$$

Then every directional width of the cyclic force hull satisfies the exact finite bound

$$
\boxed{
D\cos\left(\frac{(d+s+1)\delta}{2}\right)
\le
w_F(\theta)
\le D
\qquad(\theta\in\mathbb R/\pi\mathbb Z).}
\tag{UW.2}
$$

Equivalently the centered difference body obeys the concentric sandwich

$$
\boxed{
D\cos\left(\frac{(d+s+1)\delta}{2}\right)B_2
\subseteq
F-F
\subseteq
DB_2.}
\tag{UW.3}
$$

Using R2, this yields the phase-specific asymptotics

$$
\boxed{
0\le D-w_F(\theta)
\le
\frac{(d+1)^2}{8D}+o(D^{-1})
\quad\text{uniformly in }\theta.}
\tag{UW.4}
$$

Thus

$$
\begin{array}{c|c}
 d_H & \displaystyle\sup_\theta(D-w_F(\theta))\\ \hline
0 & \le\dfrac1{8D}+o(D^{-1}),\\[2mm]
1 & \le\dfrac1{2D}+o(D^{-1}),\\[2mm]
2 & \le\dfrac9{8D}+o(D^{-1}).
\end{array}
\tag{UW.5}
$$

For `d_H=0`, RE actually gives the exact regular difference body and the first bound is sharp for its side-normal directions.

### Corollary UW.1 — every canonical short antipodal pair is only `O(1/D)` short

In the AD short-antipodal branches, every off-circle vertex `x` of `F-F` satisfies

$$
\boxed{
D-|x|
\le
D\left[1-\cos\left(\frac{(d+s+1)\delta}{2}\right)\right].}
\tag{UW.6}
$$

Hence

$$
\boxed{
\limsup D(D-|x|)
\le\frac{(d+1)^2}{8}.}
\tag{UW.7}
$$

In particular:

$$
\boxed{
d_H=1:\quad D-|x|\le\frac1{2D}+o(D^{-1}),}
\tag{UW.8}
$$

$$
\boxed{
d_H=2:\quad D-|x|\le\frac9{8D}+o(D^{-1}).}
\tag{UW.9}
$$

So the one/two canonical antipodal defects of AD cannot be macroscopically short.

---

## 1. Exact actual-direction gap budget

Let the `h=q-d` projective actual diameter directions be ordered cyclically and let

$$
g_1,\ldots,g_h>0,
\qquad
\sum_{i=1}^h g_i=\pi.
\tag{1.1}
$$

C67 gives

$$
g_i\ge\delta.
\tag{1.2}
$$

Write

$$
g_i=\delta+x_i,
\qquad x_i\ge0.
$$

Then

$$
\sum_i x_i
=\pi-h\delta.
$$

Using

$$
q_R\delta=\pi,
\qquad h=q-d=q_R-s-d,
$$

we get the exact identity

$$
\boxed{
\sum_i x_i=(s+d)\delta.}
\tag{1.3}
$$

Therefore every individual gap satisfies

$$
\boxed{
g_i\le\delta+(s+d)\delta=(s+d+1)\delta.}
\tag{1.4}
$$

Let

$$
G:=\max_i g_i.
$$

Then

$$
\boxed{G\le(s+d+1)\delta.}
\tag{1.5}
$$

---

## 2. The diameter-vector polygon contains a large centered disk

For each actual diameter edge choose its projective unit direction `u_i`. DA defines the centrally symmetric diameter-direction polygon

$$
P_H:=\operatorname{conv}\{\pm D u_i:1\le i\le h\}.
\tag{2.1}
$$

All its `2h` vertices lie on the radius-`D` circle. Consecutive oriented vertices are separated by the projective gaps `g_i`, repeated antipodally.

The edge joining two radius-`D` circle points with angular separation `g` lies on a line at distance

$$
D\cos(g/2)
$$

from the origin. Since `P_H` is centrally symmetric and contains the origin, its centered inradius is therefore

$$
\boxed{
r_{in}(P_H)=D\min_i\cos(g_i/2)=D\cos(G/2).}
\tag{2.2}
$$

Thus

$$
\boxed{D\cos(G/2)B_2\subseteq P_H.}
\tag{2.3}
$$

Using (1.5), cosine monotonicity on the small-angle Target C regime gives

$$
D\cos\left(\frac{(s+d+1)\delta}{2}\right)B_2
\subseteq P_H.
\tag{2.4}
$$

---

## 3. Sandwich the complete difference body

Every actual diameter vector is a difference of two force-hull vertices, so

$$
P_H\subseteq F-F.
\tag{3.1}
$$

The force hull has diameter `D`, hence every difference vector has norm at most `D`:

$$
F-F\subseteq DB_2.
\tag{3.2}
$$

Combining (2.4), (3.1), and (3.2) proves UW.3.

For a convex body `F`, the support function of its difference body is exactly the width:

$$
h_{F-F}(u)
=h_F(u)+h_F(-u)
=w_F(u).
\tag{3.3}
$$

Taking support functions in the concentric sandwich gives UW.2. `square`

---

## 4. Asymptotic width constants

R2 gives

$$
s=O(D^{-2}),
$$

and

$$
\delta=\frac1D+O(D^{-3}).
$$

Therefore

$$
(s+d+1)\delta
=\frac{d+1}{D}+o(D^{-1}).
$$

Using

$$
1-\cos x=\frac{x^2}{2}+O(x^4),
$$

UW.2 gives uniformly

$$
\begin{aligned}
D-w_F(\theta)
&\le D\left[1-\cos\frac{(s+d+1)\delta}{2}\right]\\
&=\frac{(d+1)^2}{8D}+o(D^{-1}).
\end{aligned}
$$

This proves UW.4-UW.5. `square`

---

## 5. Short antipodal vertices inherit the same radial bound

AD proves that an off-circle difference-body vertex exists only in the short-antipodal branches, and there are at most two antipodal pairs of them.

Every boundary point of a convex body containing the centered disk of radius `r` has Euclidean norm at least `r`. Therefore UW.3 gives, for every `x in partial(F-F)`,

$$
|x|
\ge
D\cos\left(\frac{(s+d+1)\delta}{2}\right).
$$

For an off-circle vertex, `|x|<D`, so

$$
D-|x|
\le
D\left[1-\cos\left(\frac{(s+d+1)\delta}{2}\right)\right],
$$

proving UW.6. The asymptotic forms follow as above.

---

## 6. Geometric interpretation

The complete cyclic source is now close to a constant-width body in a much stronger metric than normalized perimeter:

$$
\sup_\theta|w_F(\theta)-D|=O(D^{-1}).
$$

Equivalently, the central symmetral

$$
\frac12(F-F)
$$

is at Hausdorff distance `O(D^-1)` from the radius-`D/2` disk.

This statement permits highly asymmetric near-constant-width primal shapes; exact constant-width bodies such as Reuleaux polygons show that difference-body roundness alone does not force `F` itself to be centrally symmetric or disk-like.

The dense source-packing lower bounds remain necessary for that additional control.

---

## 7. Comparison with previous stability statements

- RP gave average width defect
  $$
  \int_0^\pi(D-w_F(\theta))d\theta
  =\pi D-q
  =\frac\pi{24D}+O(D^{-2}).
  $$
- Bonnesen/isodiametric stability from packing gives only much coarser primal Hausdorff control in the general cyclic branch.
- UW upgrades the **difference-body / width function** to a uniform `O(D^-1)` estimate.
- AD then converts that directly into `O(D^-1)` Euclidean length defects for every canonical short antipodal pair.

---

## 8. Regression audit

### Reuleaux triangle-type asymmetry

Not excluded by width control alone. Constant-width bodies have perfectly circular difference body but can be far from disks. UW does not make the false inference that `F` is centrally symmetric.

### Parallel-side AD branches

Allowed. Parallel sides reduce the vertex count of `F-F` but do not affect the diameter-direction polygon `P_H`; UW applies unchanged.

### Short-antipodal branches

Their off-circle vertices are forced near the radius-`D` circle but need not be actual diameter vertices.

### `d_H=0`

RE gives `s=0` and exact projective gaps `g_i=delta`; UW reduces to the exact inradius bound for the regular `2q`-gon `F-F`.

---

## 9. Next theorem

UW+AD reduces the tree phases to finite `O(D^-1)` defects:

```text
P1/P2: only one/two pairs of parallel primal sides;
S1/PS/S2: only one/two canonical antipodal pairs shorter than D,
           each by at most O(1/D);
all phases: every directional width is D-O(1/D).
```

The highest-value continuations are now:

1. combine the packing lower bound on `area(F)` with quantitative stability for almost-constant-width bodies to force primal near-central-symmetry;
2. use SL local diameter minimality to eliminate the one/two parallel-side branches;
3. feed the `O(D^-1)` short-antipodal defect into the Reinhardt/difference-body Hessian to sharpen R2 from `O(D^-2)` to a classified finite normal form.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

UW is an exact elementary consequence of the report-level cyclic direction stack. No external theorem is imported.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let delta=2asin(1/(2D)), q_R=pi/delta, s=q_R-q, d=d_H.
Actual projective diameter gaps satisfy g_i>=delta and sum pi. Since h=q-d,
  sum(g_i-delta)=pi-h delta=(s+d)delta.
Hence
  G=max g_i <=(s+d+1)delta.

The diameter-vector polygon
  P_H=conv{+/-D u_h}
is a centered polygon inscribed in the radius-D circle. Its inradius is
  D cos(G/2).
Since
  P_H subset F-F subset D B_2,
we get for every direction
  D cos((s+d+1)delta/2) <= w_F(theta) <=D.

R2 has s=O(D^-2), delta=1/D+O(D^-3), so uniformly
  D-w_F(theta) <=(d+1)^2/(8D)+o(D^-1).
Thus constants are 1/8,1/2,9/8 for d=0,1,2.

Every AD off-circle antipodal vertex x lies on partial(F-F), hence
  D-|x| <= same width defect bound.
So S1 short pair has D-|x|<=1/(2D)+o(D^-1), and d2 short pairs have
D-|x|<=9/(8D)+o(D^-1).
```
