<!-- theorem-state: {"artifact_id":"ART-2875B8001BBD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — joint pocket/face cavity budget sharpens the pinned-surplus floor

**Date:** 2026-09-09  
**Run type:** exact perimeter-currency coupling / post-PI branch exclusion  
**Target:** Target C C-II after ZF/DB/PI  
**Depends on:** PI, GU/ZG gap charging, OP/PC pocket identities, HB, ZE/ZT post-ZF ledgers  
**Computation:** decimal root evaluation only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

The first post-PI currency theorem bounded outer-pocket area and exceptional-face area separately, obtaining

\[
\liminf\frac{e_{BB}+2s_C}{D}\ge0.4198649147\ldots .
\]

There is a stronger joint bound. The total excess perimeter available to the convex outer pockets and the total exceptional-face degree cannot both independently use the full force-hull perimeter budget. Two elementary upper bounds on `per(F)` imply

\[
\boxed{
E_{out}+Q
\le e_{BB}+\min\{h,\pi D-h\}
\le e_{BB}+\frac{\pi D}{2},
}
\tag{JC.1}
\]

where

\[
E_{out}:=\sum_P(L_P-3).
\]

This collapses the two quadratic cavity capacities into one square and raises the unconditional post-ZF pinned/contact floor to

\[
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge
\lambda_1
=0.4633168953789\ldots .
}
\tag{JC.2}
\]

---

## 1. Exact outer-pocket excess

Retain the notation

- `a`: number of missing loaded force-hull sides, equivalently OP outer pockets;
- `P_F=per(F)`;
- `x_B=b-q`;
- `L_P`: Euclidean perimeter of pocket `P`.

OP/PC gives

\[
\boxed{
E_{out}:=\sum_P(L_P-3)
=x_B+P_F-q-a.
}
\tag{JC.3}
\]

PC gives

\[
\boxed{a+e_{BB}\ge q,}
\tag{JC.4}
\]

hence

\[
E_{out}
\le x_B+P_F-2q+e_{BB}.
\tag{JC.5}
\]

Let

\[
z:=Q+2s_Z.
\]

The exact post-ZF identities are

\[
r_H:=2h-q=x_B+z,
\qquad
q-h=:d_H\ge0.
\tag{JC.6}
\]

Thus

\[
h=r_H+d_H,
\qquad
q=r_H+2d_H,
\qquad
x_B=r_H-z.
\tag{JC.7}
\]

---

## 2. The outer contact walk gives one joint upper bound

The outer contact walk has length

\[
b=q+x_B=2h-z,
\]

and its convex hull is `F`, so OP gives

\[
P_F\le b=q+x_B.
\tag{JC.8}
\]

Insert JC.8 into JC.5:

\[
E_{out}
\le2x_B-q+e_{BB}.
\tag{JC.9}
\]

Add `Q`. Since `Q<=z`,

\[
\begin{aligned}
E_{out}+Q
&\le2(r_H-z)-(r_H+2d_H)+e_{BB}+Q\\
&=r_H-2d_H+e_{BB}-(2z-Q)\\
&\le r_H-2d_H+e_{BB}\\
&=h-3d_H+e_{BB}\\
&\le h+e_{BB}.
\end{aligned}
\]

Therefore

\[
\boxed{E_{out}+Q\le h+e_{BB}.}
\tag{JC.10}
\]

The dropped terms are all explicitly nonnegative; no asymptotic relaxation occurs before the last line.

---

## 3. The isodiametric perimeter ceiling gives the complementary bound

Cauchy's perimeter-diameter inequality gives

\[
P_F\le\pi D.
\tag{JC.11}
\]

Insert this in JC.5 and add `Q`:

\[
\begin{aligned}
E_{out}+Q
&\le x_B+\pi D-2q+e_{BB}+Q\\
&=(r_H-z)+\pi D-2(r_H+2d_H)+e_{BB}+Q\\
&=\pi D-r_H-4d_H+e_{BB}-(z-Q)\\
&\le\pi D-r_H-4d_H+e_{BB}\\
&=\pi D-h-3d_H+e_{BB}\\
&\le\pi D-h+e_{BB}.
\end{aligned}
\]

Hence

\[
\boxed{E_{out}+Q\le\pi D-h+e_{BB}.}
\tag{JC.12}
\]

Combining JC.10 and JC.12 proves the first inequality in JC.1:

\[
E_{out}+Q
\le e_{BB}+\min\{h,\pi D-h\}.
\]

For every real `h`,

\[
\min\{h,\pi D-h\}\le\frac{\pi D}{2},
\]

which proves the second inequality in JC.1.

This is the new coupling. The outer pockets and the bounded exceptional faces are competing for complementary halves of the same perimeter/diameter budget.

---

## 4. Joint quadratic area capacity

For each OP pocket, write

\[
L_P=3+u_P,
\qquad u_P\ge0.
\]

As in the first currency theorem,

\[
H_{out}
\le
\frac{E_{out}^2+O(D)}{4\pi}.
\tag{JC.13}
\]

For bounded exceptional faces, writing `r_i=k_i-4>=1`, one has

\[
A_{exc}
\le
\frac{Q^2+O(D)}{4\pi}.
\tag{JC.14}
\]

Since `E_out,Q>=0`,

\[
E_{out}^2+Q^2
\le(E_{out}+Q)^2.
\]

Thus JC.1 gives the **joint** cavity capacity

\[
\boxed{
H_{out}+A_{exc}
\le
\frac{(e_{BB}+\pi D/2)^2}{4\pi}
+o(D^2).
}
\tag{JC.15}
\]

More sharply, retaining the actual diameter-edge density,

\[
\boxed{
H_{out}+A_{exc}
\le
\frac{(e_{BB}+\min\{h,\pi D-h\})^2}{4\pi}
+o(D^2).
}
\tag{JC.16}
\]

The first post-PI theorem used two independent squares. JC.15 is strictly smaller in the low-surplus range.

---

## 5. Compare with the PI/GU lower gap

Put

\[
L:=e_{BB}+2s_C,
\qquad
\lambda:=\lim\frac LD,
\qquad
t:=\lim\frac{e_{BB}}D
\]

along a convergent subsequence. Then `0<=t<=lambda`.

PI/GU gives

\[
\liminf\frac G{D^2}
\ge
A_{PI}-\frac\pi4\lambda^2,
\qquad
A_{PI}:=\frac12\sin(2\rho).
\tag{JC.17}
\]

ZG/GU gives

\[
G\le H_{out}+A_{exc}+2q.
\]

Because `q=O(D)`, JC.15 yields

\[
\boxed{
A_{PI}-\frac\pi4\lambda^2
\le
\frac{(t+\pi/2)^2}{4\pi}.
}
\tag{JC.18}
\]

This two-parameter inequality is already stronger than the first currency theorem.

Since `t<=lambda`, every survivor must satisfy the weaker one-variable necessary condition

\[
\boxed{
A_{PI}-\frac\pi4\lambda^2
\le
\frac{(\lambda+\pi/2)^2}{4\pi}.
}
\tag{JC.19}
\]

---

## 6. New unconditional threshold

The left side of JC.19 is strictly decreasing for positive `lambda`; the right side is strictly increasing. Their unique positive intersection is

\[
\boxed{
\lambda_1
=0.4633168953789\ldots .
}
\tag{JC.20}
\]

Equivalently, `lambda_1` is the positive root of

\[
\boxed{
(\pi^2+1)\lambda^2
+\pi\lambda
+\frac{\pi^2}{4}
-4\pi A_{PI}=0.
}
\tag{JC.21}
\]

Thus no unbounded post-ZF subsequence can satisfy

\[
\frac{e_{BB}+2s_C}{D}	o\lambda<\lambda_1.
\]

This proves JC.2.

Numerically, the improvement over the first currency theorem is

\[
0.4633168954-0.4198649147
=0.0434519807\ldots .
\]

---

## 7. Diameter-density-sensitive form

JC.16 should be retained for future optimization. If

\[
\frac hD\to y,
\]

then the same proof gives

\[
\boxed{
A_{PI}-\frac\pi4\lambda^2
\le
\frac{(t+\min\{y,\pi-y\})^2}{4\pi}.
}
\tag{JC.22}
\]

Together with DB/NB constraints on `(y,r_H/D)`, this is a sharper feasible-region inequality than the universal threshold JC.20. It may be possible to raise the floor further by optimizing the actual diameter density rather than replacing the minimum by `pi/2`.

---

## 8. Consequences for the two mandatory currencies

Every post-ZF survivor now satisfies

\[
\boxed{
\frac{x_B+Q+2s_Z}{D}
\ge0.6099043189\ldots-o(1)
}
\tag{JC.23}
\]

from NB and

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge0.4633168954\ldots-o(1)
}
\tag{JC.24}
\]

from JC.

ZK also gives

\[
3(d_H+s_Z)\le6+e_{BB}+2s_C.
\]

Since `h=r_H+d_H` and `s_Z>=0`, one obtains the additional asymptotic slope constraint

\[
\boxed{
\frac{r_H}{D}
+\frac13\frac{e_{BB}+2s_C}{D}
\ge2\rho-o(1).
}
\tag{JC.25}
\]

Thus a survivor near the minimum allowed pinned/contact currency must have very large diameter branching. At `lambda=lambda_1`, JC.25 gives

\[
\frac{r_H}{D}
\ge
2\rho-\frac{\lambda_1}{3}-o(1)
=1.3237313013\ldots-o(1).
\tag{JC.26}
\]

This is far stronger than the universal NB floor `0.609904...` in that part of parameter space.

---

## 9. Regression audit

- Regular odd shells have large `e_BB` and large branching, so they remain outside the eliminated low-surplus phase.
- Many triangular outer pockets contribute only `O(D)` baseline perimeter and cannot create quadratic area capacity in JC.13.
- One giant pocket and one giant exceptional face are both included: their excess-perimeter/degree currencies add before squaring.
- Pinned-stress-dominated `L` is treated honestly through `t<=lambda`; JC.18 is stronger than the final worst-case relaxation.
- JC.1 is finite and exact; only the conversion to area constants discards lower-order `O(D)` terms.

---

## 10. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| joint perimeter bound JC.1 | proved | OP/PC + outer-walk and Cauchy perimeter bounds |
| joint cavity capacity JC.15 | proved asymptotically | convex isoperimetry after baseline subtraction |
| two-parameter necessary inequality JC.18 | proved | PI/GU lower + ZG charging upper |
| universal floor `0.4633168954...` | proved | monotone scalar root |
| slope constraint JC.25 | proved | ZK + DB |
| Level I | still open | high pinned-surplus / high branching coexistence remains |

---

## 11. Next target

The surviving feasible region is now sharply constrained by JC.18, JC.22, NB, DB, and ZK. The next step should optimize these constraints jointly in the actual diameter density `y=h/D` and then attack the extremal geometry of the resulting high-branching/high-loaded-contact boundary state.
