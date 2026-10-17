> Generated reading edition · [exact source](../../../docs/reports/target_c_db_upgraded_component_gap_2026-09-09.md) · source SHA-256 `60afa03b35a020f133d5507ac42656999ecafe0a4d988e8eb708d49497285237`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-6BA84AC0AB44","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — DB-upgraded component-gap stability

**Date:** 2026-09-09  
**Repository base:** `78b922cbbbf09a63c0cfa3f1d6b786cc1fcdfa24`  
**Run type:** quantitative cross-route strengthening  
**Target:** Target C C-II after ZF  
**Depends on:** DB force-hull area floor, ZK component-slack cancellation, ZG attachment-cell localization  
**External web search:** not used  
**Computation:** arithmetic only for displayed decimals

## LEVEL I STATUS

`STILL OPEN`

The existing ZG stability theorem predates two later improvements:

1. ZK replaces its component-diameter currency `e_BB+3s_C` by the exact smaller currency `e_BB+2s_C`;
2. DB raises the post-ZF force-hull area floor from the old C67 constant `(1/2)sin(1/4)` to the saturated value `sqrt(3)/4`.

Combining both gives a substantially stronger quantitative dichotomy.

Let

```math
G:=\operatorname{area}(F)-\sum_r\operatorname{area}(\operatorname{conv}A_r)\ge0
```

be the attachment-cell area gap and put

```math
\lambda_2:=\limsup_{D\to\infty}\frac{e_{BB}+2s_C}{D}.
```

Then

```math
\boxed{
\liminf\frac G{D^2}
\ge
\frac{\sqrt3}{4}-\frac\pi4\lambda_2^2.
}
\tag{GU.1}
```

Hence a positive quadratic gap is forced whenever

```math
\boxed{
\lambda_2<\lambda_*:=\sqrt{\frac{\sqrt3}{\pi}}
=0.7425152492\ldots .
}
\tag{GU.2}
```

The prior ZG threshold was about `0.396`; GU nearly doubles the range in which the post-ZF source is forced into macroscopic cavity/shell geometry.

---

## 1. Correct component-diameter budget

ZK defines

```math
k=d_H+s_Z
```

and proves

```math
\sum_r\delta_r+R_I+s_B+3k
=6+e_{BB}+2s_C.
```

Therefore with

```math
L_2:=6-3k+e_{BB}+2s_C\ge0
```

we have

```math
\sum_r\delta_r\le L_2.
\tag{1.1}
```

The C49 attachment hulls have pairwise disjoint interiors, and the same elementary diameter estimate used in ZG gives

```math
\operatorname{diam}(A_r)\le\delta_r+2.
```

By the planar isodiametric inequality,

```math
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le
\frac\pi4L_2^2+\pi L_2+\pi^2D.
\tag{1.2}
```

Since `k>=0`,

```math
\limsup\frac{L_2}{D}\le\lambda_2.
\tag{1.3}
```

---

## 2. Insert the DB area floor

DB proves for every unbounded post-ZF sequence

```math
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge\frac{\sqrt3}{4}.
\tag{2.1}
```

Subtract (1.2) from (2.1), divide by `D^2`, and use (1.3). The linear terms vanish, giving GU.1:

```math
\liminf\frac G{D^2}
\ge
\frac{\sqrt3}{4}-\frac\pi4\lambda_2^2.
```

The right side is positive exactly when

```math
\lambda_2^2<\frac{\sqrt3}{\pi},
```

which proves GU.2.

In particular, if

```math
e_{BB}+s_C=o(D),
```

then also `e_BB+2s_C=o(D)` and

```math
\boxed{
\liminf\frac G{D^2}
\ge\frac{\sqrt3}{4}
=0.4330127019\ldots .
}
\tag{2.2}
```

This replaces the old sublinear-surplus gap constant `0.1237019796...`.

---

## 3. DB also improves exceptional-face perimeter capacity

Let `Q=sum_F(deg F-4)` over bounded nonquadrilateral contact faces. DB proves

```math
Q+2s_Z
\le
h+1-2D\cos((h-1)a_D),
\qquad
a_D=\arcsin\frac1{2D}.
```

The C67 gap-feasibility condition implies `(h-1)a_D<pi/2`, so the cosine term is positive. Thus

```math
Q<h+1\le q+1\le\pi D+1.
\tag{3.1}
```

For exceptional faces let `f` be their count and

```math
g_F=\sum_F(\deg F-5).
```

Their total perimeter is exactly

```math
K_{exc}=5f+g_F=Q+4f\le5Q.
```

Therefore DB sharpens the old crude post-ZF estimate to

```math
\boxed{
K_{exc}\le5\pi D+O(1).
}
\tag{3.2}
```

The previous ZG localization used `K_exc<=10pi D`.

---

## 4. Stronger macroscopic-gap localization

ZG proves the geometric charging inequality

```math
G\le H_{out}+A_{exc}+2q,
\tag{4.1}
```

where

- `H_out` is the part of the force hull in the outer contact face;
- `A_exc` is the total area of bounded nonquadrilateral contact faces.

Assume along a subsequence

```math
G\ge gD^2
```

for some fixed `g>0`.

If `H_out<(g/2)D^2` along a further subsequence, then (4.1) and `q=O(D)` imply

```math
A_{exc}\ge(g/2-o(1))D^2.
\tag{4.2}
```

Let `k_max` be the maximum exceptional-face perimeter. C51 makes each exceptional face convex, so

```math
A_{exc}
\le\frac1{4\pi}\sum_i k_i^2
\le\frac{k_{max}}{4\pi}K_{exc}.
```

Using (3.2),

```math
A_{exc}
\le\left(\frac54+o(1)\right)k_{max}D.
```

Together with (4.2),

```math
\boxed{
\liminf\frac{k_{max}}D\ge\frac{2g}{5}
}
\tag{4.3}
```

along that subsequence.

Thus any quadratic gap yields the sharpened dichotomy:

```math
\boxed{
H_{out}\ge\frac g2D^2
\quad\text{or}\quad
k_{max}\ge\left(\frac{2g}{5}-o(1)\right)D.
}
\tag{4.4}
```

The constants are not claimed optimal; the point is that DB improves both the gap density and the total exceptional-perimeter budget.

---

## 5. Explicit low-surplus consequence

If `e_BB+s_C=o(D)`, take any

```math
g<\frac{\sqrt3}{4}.
```

Eventually `G>=gD^2`. Hence after passing to a subsequence either

```math
H_{out}\ge\left(\frac{\sqrt3}{8}-o(1)\right)D^2
=0.2165063509\ldots D^2-o(D^2),
```

or one bounded exceptional face has perimeter at least

```math
\left(\frac{\sqrt3}{10}-o(1)\right)D
=0.1732050807\ldots D-o(D).
```

So the sublinear loaded-contact/pinned-stress branch now forces a quantitatively large visible cavity, not merely some unspecified `Omega(D^2)` gap.

---

## 6. Interaction with NM

NM independently proves

```math
x_B+Q+2s_Z
\ge(2\rho/3-o(1))D
=0.4927234221\ldots D-o(D).
```

Thus every post-ZF survivor already carries a mandatory linear **diameter-branching/contact-topology** defect. GU concerns the different boundary/stress currency `e_BB+2s_C`.

The combined frontier is therefore a genuine two-axis split:

1. if `e_BB+2s_C<lambda_*D` asymptotically, a quadratic attachment-cell gap is forced and localizes to a macroscopic outer pocket or giant bounded face;
2. if `e_BB+2s_C>=lambda_*D` along a subsequence, the pinned/contact surplus itself is quantitatively linear;
3. in both cases NM separately forces `x_B+Q+2s_Z=Omega(D)`.

A closing theorem must couple these two mandatory currencies rather than treating them independently.

---

## 7. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| GU.1 gap bound | proved | ZK attachment-cell bound + DB area floor |
| threshold `lambda_*=sqrt(sqrt3/pi)` | proved | positivity of GU.1 |
| `Q<pi D+O(1)` | proved post-ZF | DB exact finite inequality |
| `K_exc<=5pi D+O(1)` | proved | exact exceptional perimeter + preceding bound |
| sharpened gap localization | proved | ZG charging + C51 isoperimetry + new perimeter budget |
| cavity/shell geometry impossible | not proved | still requires global capacity or motion theorem |
| Level I | still open | high-surplus and macroscopic-container branches remain |

---

## 8. Promotion recommendation

**Hold as report pending independent audit.**

If DB/ZK are promoted, GU should replace the numerical constants in the earlier ZG low-surplus stability report.

---

## 9. Next theorem

The quantitative post-ZF source now satisfies simultaneously:

```math
x_B+Q+2s_Z\ge(0.4927234-o(1))D
```

and either

```math
e_{BB}+2s_C\ge(0.7425152-o(1))D
```

or a macroscopic force-hull cavity is present.

The highest-value next lemma is a **currency coupling theorem** showing that the linear NM defect and the GU contact/stress surplus cannot coexist within the loaded degree-three boundary budget, unless enough area is lost to contradict the global minimum-diameter density.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

GU stability upgrade:
Let
    lambda_2=limsup(e_BB+2s_C)/D.
ZK gives
    L_2=6-3(d_H+s_Z)+e_BB+2s_C,
    sum delta_r<=L_2,
and attachment-cell area
    <= (pi/4)L_2^2+pi L_2+pi^2D.
DB gives
    liminf area(F)/D^2 >= sqrt(3)/4.
Therefore
    liminf G/D^2
      >= sqrt(3)/4-(pi/4)lambda_2^2.
A quadratic gap is forced whenever
    lambda_2 < sqrt(sqrt(3)/pi)
             =0.7425152492...

DB also gives Q<pi D+O(1), hence total exceptional-face perimeter
    K_exc<=5pi D+O(1).
If G>=gD^2, then along a subsequence
    H_out >= (g/2)D^2
or
    k_max >= (2g/5-o(1))D.

For e_BB+s_C=o(D), g may approach sqrt(3)/4, giving
    H_out >= (sqrt(3)/8-o(1))D^2
or
    k_max >= (sqrt(3)/10-o(1))D.

Combine with NM:
    x_B+Q+2s_Z >= (0.4927234-o(1))D.
Next: couple these two mandatory linear currencies through boundary degree/area.
```
