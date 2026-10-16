<!-- theorem-state: {"artifact_id":"ART-672AFB251896","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`: exact difference-body area defect energy

**Date:** 2026-09-10  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact convex-area reduction / two-cell scalarization  
**Target:** cyclic primitive endpoint, `d_H=2`  
**Depends on:** D2C two defect cells; AD difference-body defect split; D2S within-tree direction saturation  
**External literature:** none  
**Computation:** symbolic expansion was used only to check the displayed asymptotic before deriving it directly; the exact theorem is elementary

## LEVEL I STATUS

`STILL OPEN`

D2C localizes every non-Reinhardt metric defect to two cross-tree cells with projective gaps

\[
2\delta<G_j\le\Delta_2,
\qquad
\delta=2\arcsin\frac1{2D},
\qquad
\Delta_2=2\arcsin\frac1D.
\]

The staircase words control which primal shell edge belongs to which block, but they do **not** affect the area of the difference body

\[
K:=F-F.
\]

The complete area is an additive function of the two scalar cell gaps.

### Theorem AE2 — exact two-cell area formula

For

\[
W(G):=\sqrt{1-D^2\sin^2(G/2)},
\]

and

\[
L(G):=D\cos(G/2)+W(G),
\]

define the full-cell area contribution

\[
\boxed{
C_D(G):=2D\,L(G)\sin(G/2).
}
\tag{AE2.1}
\]

Then every sufficiently large cyclic `d_H=2` survivor satisfies

\[
\boxed{
\operatorname{area}(K)
=(q-4)D^2\sin\delta+C_D(G_1)+C_D(G_2).
}
\tag{AE2.2}
\]

This formula is valid uniformly in all three AD branches `S2`, `PS`, and `P2`.  At a parallel cell `G=Delta_2`, one has `W=0`; the same expression becomes the area of the single merged length-two edge.

Equivalently, define the cell defect energy

\[
\boxed{
\mathcal E_D(G)
:=2D^2\sin\delta-C_D(G).
}
\tag{AE2.3}
\]

Then

\[
\boxed{
\operatorname{area}(K)
=qD^2\sin\delta
-\mathcal E_D(G_1)-\mathcal E_D(G_2).
}
\tag{AE2.4}
\]

Moreover

\[
\boxed{
\mathcal E_D(2\delta)=0,
\qquad
\mathcal E_D(G)>0
\quad(2\delta<G\le\Delta_2),
}
\tag{AE2.5}
\]

and `mathcal E_D(G)` is strictly increasing on the full allowed interval.

Thus every true D2 cell pays a **strict additive difference-body area loss**, while the SSR/Reinhardt boundary is exactly the zero-energy point.

---

## 1. Half-boundary decomposition of `K`

Because `K=F-F` is centrally symmetric, take one projective half of its boundary.  D2S gives exactly `q-4` within-tree transitions.  Each such transition joins two circular difference-body vertices of radius `D` whose polar-angle gap is exactly `delta`.

For one such ordinary transition, if the consecutive circular vertices are `x,y`, then

\[
|x|=|y|=D,
\qquad
\angle(x,y)=\delta,
\]

so

\[
x\times y=D^2\sin\delta.
\tag{1.1}
\]

The second antipodal half contributes the identical cross product.  Since polygon area is one half of the full cross-product sum, each ordinary transition contributes exactly

\[
D^2\sin\delta
\]

to `area(K)` after the antipodal doubling.

There are `q-4` such transitions.

---

## 2. One short cell

Take a D2C short cell.  In one projective half its difference-body boundary is

\[
a\to x\to b,
\]

where

\[
|a|=|b|=D,
\qquad
|x|=L(G),
\]

and `x` lies on the angular bisector of `a,b`.  Hence, after centering the bisector at angle zero,

\[
\arg a=-G/2,
\qquad
\arg x=0,
\qquad
\arg b=G/2.
\]

Therefore

\[
a\times x=DL(G)\sin(G/2),
\]

and

\[
x\times b=DL(G)\sin(G/2).
\]

The cross-product sum on the chosen half is

\[
2DL(G)\sin(G/2).
\tag{2.1}
\]

As above, antipodal doubling and the factor `1/2` in the polygon-area formula cancel.  Thus the full contribution of this cell to `area(K)` is exactly

\[
C_D(G)=2DL(G)\sin(G/2).
\]

---

## 3. A parallel cell is the same formula at `W=0`

At the D2C parallel endpoint,

\[
G=\Delta_2,
\qquad
W(G)=0,
\qquad
L(G)=D\cos(G/2).
\]

The off-circle middle vertex has collapsed and the two unit Minkowski edges merge into one length-two edge joining the two circular radius-`D` vertices.

Its cross product is

\[
D^2\sin G.
\]

But

\[
C_D(G)
=2D^2\cos(G/2)\sin(G/2)
=D^2\sin G.
\]

So AE2.1 remains exact without a separate branch convention.

This proves AE2.2 in S2, PS, and P2. `square`

---

## 4. Defect-energy form

If a switch were at the forbidden equality value

\[
G=2\delta,
\]

D2C gives

\[
L(G)=D.
\]

Hence its contribution would be

\[
C_D(2\delta)
=2D^2\sin\delta.
\]

This is exactly the contribution of the two ordinary circular unit edges obtained when the missing completion state returns to the radius-`D` circle.

Replacing the two actual switch cells by this zero-defect value gives

\[
(q-4)D^2\sin\delta+4D^2\sin\delta
=qD^2\sin\delta.
\]

Subtracting the actual cell contributions proves AE2.4.

---

## 5. Strict monotonicity of one cell contribution

It remains to show that `C_D(G)` strictly decreases as `G` moves away from `2delta` toward `Delta_2`.

Put

\[
t:=D\sin(G/2).
\]

On the allowed interval,

\[
D\sin\delta\le t\le1.
\tag{5.1}
\]

Since

\[
D\sin\delta
=2D\sin(\delta/2)\cos(\delta/2)
=\cos(\delta/2),
\tag{5.2}
\]
we have

\[
t^2\ge1-\frac1{4D^2}.
\tag{5.3}
\]

Write

\[
A:=\sqrt{D^2-t^2},
\qquad
B:=\sqrt{1-t^2}.
\]

Then

\[
D\cos(G/2)=A,
\qquad
W(G)=B,
\]

and

\[
\frac12C_D(G)=t(A+B)=:f(t).
\tag{5.4}
\]

Differentiate on the open interval:

\[
 f'(t)
 =\frac{D^2-2t^2}{A}
  +\frac{1-2t^2}{B}.
\tag{5.5}
\]

For sufficiently large `D`, the first numerator is positive and the second is negative.  To compare their magnitudes, square after moving the negative term to the other side.  The numerator of the difference is exactly

\[
\begin{aligned}
&(2t^2-1)^2(D^2-t^2)
 -(D^2-2t^2)^2(1-t^2)\\
&\qquad=(D^2-1)\bigl((D^2+1)t^2-D^2\bigr).
\end{aligned}
\tag{5.6}
\]

By (5.3), for `D>1`,

\[
t^2
\ge1-\frac1{4D^2}
>\frac{D^2}{D^2+1}.
\]

Hence the right side of (5.6) is positive.  Therefore

\[
\frac{2t^2-1}{B}
>
\frac{D^2-2t^2}{A},
\]
so

\[
f'(t)<0.
\]

Because `t` strictly increases with `G`, `C_D(G)` is strictly decreasing.  Therefore `mathcal E_D(G)` is strictly increasing, proving AE2.5. `square`

---

## 6. Uniform asymptotic energy scale

D2C writes

\[
G_j=(2+s_j)\delta,
\qquad
s_1+s_2=s=q_R(D)-q,
\qquad
s_j=O(D^{-2}).
\]

A useful parameter with no endpoint singularity is

\[
\lambda_j:=D W(G_j).
\tag{6.1}
\]

D2C gives

\[
0\le\lambda_j<\frac12
\]
for a true cell, with `lambda_j=0` at a parallel cell and the formal SSR boundary value `lambda_j=1/2` at `s_j=0`.

Uniform Taylor expansion of AE2.2 on the compact two-cell range gives

\[
\boxed{
\operatorname{area}(K)
=
\pi D^2-\frac\pi6
-\frac{2(1-\lambda_1-\lambda_2)}{D}
+O(D^{-2}).
}
\tag{AE2.6}
\]

The derivation is short.  First,

\[
D^2\sin\delta
=D-\frac1{8D}+O(D^{-3}),
\]

\[
q
=\frac\pi\delta-s
=\pi D-\frac\pi{24D}-s+O(D^{-3}),
\]

so

\[
qD^2\sin\delta
=
\pi D^2-\frac\pi6-Ds+O(D^{-2}).
\tag{6.2}
\]

For one cell put `u=D^2s_j=O(1)`.  From

\[
t=D\sin((1+s_j/2)\delta)
=1+\frac{u/2-1/8}{D^2}+O(D^{-4})
\]
and `W=lambda_j/D`, equation (5.4) gives

\[
C_D(G_j)
=2D+\frac{u-5/4+2\lambda_j}{D}+O(D^{-3}).
\tag{6.3}
\]

Since

\[
2D^2\sin\delta
=2D-\frac1{4D}+O(D^{-3}),
\]
we get

\[
\mathcal E_D(G_j)
=
\frac{1-u-2\lambda_j}{D}+O(D^{-3}).
\tag{6.4}
\]

Summing (6.4), using

\[
D s=\frac{u_1+u_2}{D},
\]
and substituting into (6.2) yields AE2.6.

Because every true cell has `lambda_j<1/2`,

\[
1-\lambda_1-\lambda_2>0.
\]

Thus a true D2 source has a strict order-`1/D` difference-body area loss beyond the universal regular `2q`-gon baseline `pi D^2-pi/6`.

---

## 7. Scaled defect coordinates

Along a sequence for which

\[
u_j:=D^2s_j\to u_j^\infty\in[0,1/4],
\]
D2C gives

\[
\lambda_j
\to\sqrt{\frac14-u_j^\infty}.
\]

Therefore AE2.6 becomes

\[
\boxed{
\operatorname{area}(K)
=
\pi D^2-\frac\pi6
-\frac{
2-\sqrt{1-4u_1^\infty}-\sqrt{1-4u_2^\infty}
}{D}
+o(D^{-1}).
}
\tag{AE2.7}
\]

The coefficient is strictly positive whenever at least one limiting cell defect is positive.

For P2, both `lambda_j=0`, so

\[
\boxed{
\operatorname{area}(K)
=
\pi D^2-\frac\pi6-\frac2D+O(D^{-2}).
}
\tag{AE2.8}
\]

---

## 8. What this changes

D2 geometry now has two independent exact scalarizations:

1. SCE encodes primal shell closure through the two staircase words and the two defect cells;
2. AE2 removes the staircase words entirely and encodes the **difference-body area** by the two defect cells alone.

The latter supplies a monotone geometric energy whose unique zero is the SSR/Reinhardt boundary.  Any future second-order packing or mixed-area argument can therefore charge the true D2 defect without reopening the staircase combinatorics.

In particular a proposed transversality theorem no longer needs an ad hoc defect norm: one may use

\[
\mathcal E_D(G_1)+\mathcal E_D(G_2)
=qD^2\sin\delta-\operatorname{area}(F-F),
\]
which is exact, positive, additive, and canonical.

---

## 9. Regression audit

### SSR boundary

At `G_1=G_2=2delta`, both energies vanish and AE2 gives

\[
\operatorname{area}(K)=qD^2\sin\delta,
\]
the area of the regular `2q`-gon difference body.  Thus the selected-support Reinhardt regression is retained exactly.

### P2

At each parallel cell `W=0`; the collapsed length-two edge gives the same cell contribution as AE2.1.  No missing-vertex area is double-counted.

### Staircase words

No word appears in AE2.  This is correct because the word chooses which primal summand contributes each Minkowski edge but does not alter the already-fixed difference-body vertex sequence.

### Positivity scale

The order-`1/D` loss in AE2.6 is not claimed to close the source-packing problem.  Existing source-hull area bounds have order-`D` slack.  AE2 is a precise defect currency, not a Level I contradiction by itself.

---

## 10. Next theorem

The most direct uses of AE2 are now:

1. combine it with a sharper mixed-area / source-capacity expansion if one can improve the current order-`D` hull-area window;
2. compare AE2 with the fixed-perimeter polygonal isoperimetric defect of `K` to obtain a convexity penalty quadratic in the scaled cell defects;
3. use the exact energy as the scalar in an SSR-boundary second-variation calculation of the full source problem.

The second item is purely finite convex geometry and is the next immediate target on this branch.
