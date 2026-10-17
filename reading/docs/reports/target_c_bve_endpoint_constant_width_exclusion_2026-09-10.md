> Generated reading edition · [exact source](../../../docs/reports/target_c_bve_endpoint_constant_width_exclusion_2026-09-10.md) · source SHA-256 `733508a849cd34886dfdf37a806301f04f148d86f476d79577023e00039fa979`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C27F87D706FB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — constant-width boundary rigidity excludes the exact BVE feedback endpoint

**Date:** 2026-09-10  
**Branch base:** `80411b93179346b4d3c43e3504e1ba867ac85382`  
**Depends on:** BVE and BF on this branch; ZK/C44/C49 attachment geometry  
**Run type:** equality audit / compactness / endpoint exclusion  
**Target:** Target C, C-II after ZF

## LEVEL I STATUS

`STILL OPEN`.

BF defines the exact generic post-ZF feedback threshold

```math
\lambda_{BVE}=0.5983402429824461\ldots
```

and proves every unbounded survivor has normalized pinned/contact surplus at least this
value.  This report proves the exact endpoint cannot occur.

### Theorem CW — feedback endpoint exclusion

No unbounded post-ZF survivor sequence can satisfy

```math
\boxed{
\frac{e_{BB}+2s_C}{D}\to\lambda_{BVE}.
}
\tag{CW.1}
```

Consequently there are absolute constants

```math
\boxed{
\epsilon_{CW}>0,
\qquad D_0<\infty
}
```

such that every sufficiently large post-ZF survivor satisfies

```math
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge\lambda_{BVE}+\epsilon_{CW}.
}
\tag{CW.2}
```

The new epsilon is nonexplicit.  The certified explicit generic floor remains
`>0.59834`.

The mechanism differs from ND.  At the old RD endpoint the dominant attachment hull
had to converge to a disk.  After BVE inserts the correct boundary-sharing defect, the
new endpoint hull is no longer isodiametric.  Instead, equality in the Bonnesen step
forces its perimeter to approach `pi` times its diameter.  The limit is therefore a
strictly convex constant-width body.  That is still enough: polygon vertices become
dense on its entire boundary, and every one of those vertices also lies on the full
force-hull boundary.  A convex body cannot strictly contain another full-dimensional
convex body while preserving its entire boundary.

---

## 1. Endpoint saturation concentrates the attachment-cell budget

Assume for contradiction that CW.1 holds.  BF localizes the scalar variables to its
unique optimizer

```math
\frac hD\to y_{BVE},
\qquad
\frac{\operatorname{per}F}{D}\to p_{BVE}.
\tag{1.1}
```

At this point the force-hull area lower bound and the two upper capacities meet:

```math
A_*
:=\Phi(y_{BVE})=\Psi(p_{BVE})
=
G(\lambda_{BVE})+\Delta(y_{BVE},p_{BVE}).
\tag{1.2}
```

Let

```math
C_D:=\sum_r\operatorname{area}(\operatorname{conv}A_r)
```

be the total harmonic attachment-cell area.  BVE gives

```math
\limsup\frac{C_D}{D^2}
\le G(\lambda_{BVE}).
\tag{1.3}
```

RD/DD gives the complementary outer-pocket plus exceptional-face capacity

```math
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le\Delta(y_{BVE},p_{BVE}).
\tag{1.4}
```

ZG charges the force-hull complement to these two classes up to `O(D)`, while
FSDB/RSR gives

```math
\liminf\frac{\operatorname{area}F}{D^2}
\ge A_*.
\tag{1.5}
```

Hence both upper budgets must saturate separately.  In particular

```math
\boxed{
\frac{C_D}{D^2}
\to G(\lambda_{BVE}).
}
\tag{1.6}
```

---

## 2. One unloaded component carries asymptotically all component diameter

Write

```math
\lambda_*:=\lambda_{BVE}.
```

ZK gives

```math
\sum_r\delta_r
\le6+e_{BB}+2s_C,
```

so

```math
\boxed{
S_D:=\sum_r\delta_r
\le\lambda_*D+o(D).
}
\tag{2.1}
```

Fix `eta>0`.  For all sufficiently large `D`, every attachment hull

```math
K_r:=\operatorname{conv}A_r
```

has, by C44,

```math
\operatorname{diam}K_r
\le\delta_r+2
\le(\lambda_*+\eta)D.
\tag{2.2}
```

BVE therefore gives

```math
\operatorname{area}K_r
\le
C(\lambda_*+\eta)(\delta_r+2)^2,
\tag{2.3}
```

where

```math
C(c)=\frac\pi4-\frac{\kappa(c)^2}{4}.
```

Sum (2.3), divide by `D^2`, let `D->infinity`, and then let `eta downarrow0`.
Because `c_I=O(D)` and `S_D=O(D)`, the `+2` terms are lower order.  Equation (1.6)
gives

```math
C(\lambda_*)\lambda_*^2
\le
C(\lambda_*)
\liminf\frac1{D^2}\sum_r\delta_r^2.
```

Thus

```math
\boxed{
\frac1{D^2}\sum_r\delta_r^2\to\lambda_*^2,
\qquad
\frac{S_D}{D}\to\lambda_*.
}
\tag{2.4}
```

Choose an unloaded component `I_*` with maximal graph diameter `delta_*`.  Since

```math
\sum_r\delta_r^2
\le\delta_*S_D,
```

(2.4) implies

```math
\boxed{
\frac{\delta_*}{D}\to\lambda_*.
}
\tag{2.5}
```

Moreover

```math
\boxed{
\frac1D\sum_{r\ne *}\delta_r\to0.
}
\tag{2.6}
```

Let

```math
K_D:=\operatorname{conv}A_*
```

be the dominant attachment hull.  The other attachment cells contribute `o(D^2)`
area, so (1.6) and (2.3) force

```math
\boxed{
\frac{\operatorname{area}K_D}{D^2}
\to C(\lambda_*)\lambda_*^2.
}
\tag{2.7}
```

C44 and (2.5) give

```math
\operatorname{diam}K_D\le\lambda_*D+o(D).
```

Applying BVE to `K_D` itself shows that any fixed relative deficit in its diameter
would create a fixed quadratic area deficit in (2.7).  Therefore

```math
\boxed{
\frac{d_D}{D}:=
\frac{\operatorname{diam}K_D}{D}
\to\lambda_*.
}
\tag{2.8}
```

Consequently

```math
\boxed{
\frac{\operatorname{area}K_D}{d_D^2}
\to
C(\lambda_*)
=
\frac\pi4-\frac{\kappa_*^2}{4},
}
\tag{2.9}
```

where

```math
\kappa_*:=\kappa(\lambda_*)>0.
\tag{2.10}
```

---

## 3. BVE equality forces perimeter/diameter ratio to `pi`

Let

```math
P_D:=\operatorname{per}K_D.
```

The perimeter-diameter inequality gives

```math
P_D\le\pi d_D.
\tag{3.1}
```

We prove

```math
\boxed{
\frac{P_D}{d_D}\to\pi.
}
\tag{3.2}
```

Suppose otherwise.  Pass to a subsequence on which

```math
\frac{P_D}{d_D}\to p_0<\pi.
\tag{3.3}
```

Apply the same Bonnesen theorem used in BVE.  It supplies concentric disks around some
center with annulus half-width `w_D` satisfying

```math
w_D^2
\le
\frac{P_D^2-4\pi\operatorname{area}K_D}{4\pi}.
\tag{3.4}
```

Put

```math
x_D:=\frac{2w_D}{d_D}.
```

Using (2.9),

```math
\begin{aligned}
\limsup x_D^2
&\le
\frac{p_0^2}{\pi}
-
4C(\lambda_*)\\
&=
\frac{p_0^2}{\pi}-\pi+\kappa_*^2\\
&<\kappa_*^2.
\end{aligned}
\tag{3.5}
```

Hence for some fixed `eta>0`, eventually

```math
x_D\le\kappa_*-\eta.
\tag{3.6}
```

BVE's exact support-normal argument gives

```math
D
\le
 d_D\,
\frac{(1+x_D)^3}{1-6x_D+x_D^2}
\tag{3.7}
```

because the full force hull has diameter `D`.  Divide by `D` and pass to the limit.
The rational function in (3.7) is strictly increasing on
`[0,3-2sqrt(2))`, so (2.8) and (3.6) give

```math
1
\le
\lambda_*
\frac{(1+\kappa_*-\eta)^3}
{1-6(\kappa_*-\eta)+(\kappa_*-\eta)^2}
<
\lambda_*
\frac{(1+\kappa_*)^3}
{1-6\kappa_*+\kappa_*^2}
=1,
```

where the last equality is exactly the defining equation for `kappa_*`.
Contradiction.  Therefore (3.2) holds.

---

## 4. The dominant attachment hull converges to a constant-width body

Normalize by the source diameter and translate by one point of `K_D`:

```math
\widehat K_D=D^{-1}(K_D-x_D),
\qquad
\widehat F_D=D^{-1}(F_D-x_D).
\tag{4.1}
```

Both families lie in a common bounded disk.  Pass to a subsequence with

```math
\widehat K_D\to K_\infty,
\qquad
\widehat F_D\to F_\infty
\tag{4.2}
```

in Hausdorff distance.

Inclusion gives

```math
K_\infty\subseteq F_\infty.
\tag{4.3}
```

By (2.8),

```math
\operatorname{diam}K_\infty=\lambda_*.
\tag{4.4}
```

By (3.2) and continuity of convex perimeter under Hausdorff convergence,

```math
\operatorname{per}K_\infty=\pi\lambda_*.
\tag{4.5}
```

For every planar convex body of diameter `lambda_*`, every directional width is at
most `lambda_*`.  Cauchy's perimeter formula gives

```math
\operatorname{per}K_\infty
=
\int_0^\pi w_{K_\infty}(\theta)\,d\theta.
\tag{4.6}
```

Since the continuous integrand satisfies

```math
0\le w_{K_\infty}(\theta)\le\lambda_*
```

and its integral equals `pi lambda_*`, it must be identically equal to
`lambda_*`.  Thus

```math
\boxed{K_\infty\text{ has constant width }\lambda_*.}
\tag{4.7}
```

---

## 5. A constant-width body is strictly convex

We record the short proof needed below.

### Lemma CW.1

A planar convex body of constant width `w>0` has no nontrivial boundary line segment.

### Proof

Suppose distinct boundary points `x,y` lie in one support line with outward unit normal
`u`.  Let `z` lie in the opposite support face.  Constant width gives

```math
(x-z)\cdot u=w.
```

The diameter of a constant-width body is `w`, so

```math
|x-z|\le w.
```

Equality in the scalar projection therefore forces

```math
x-z=wu.
```

But `y` lies in the same support line, so

```math
(y-z)\cdot u=w,
```

while `y-x` is a nonzero vector orthogonal to `u`.  Hence

```math
|y-z|^2=w^2+|y-x|^2>w^2,
```

contradicting the diameter bound.  `square`

Therefore `K_infty` is strictly convex.

---

## 6. Polygon vertices become dense on the full constant-width boundary

Let `V_D` be the vertex set of the polygon `K_D`.  Since

```math
K_D=\operatorname{conv}A_*,
```

every polygon vertex belongs to `A_*`.  Every point of `A_*` is a loaded force-hull
vertex, so

```math
\boxed{V_D\subseteq\partial F_D.}
\tag{6.1}
```

We claim the normalized vertex sets become dense in `partial K_infty`.

If not, then along a subsequence some polygon edge has normalized length bounded below
by a fixed positive constant.  Choose such edges and pass to limits of their endpoints
and supporting normals.  Hausdorff convergence implies the limiting nontrivial segment
lies in a support line of `K_infty`, hence in `partial K_infty`.  This contradicts the
strict convexity from Section 5.

Thus the maximum normalized edge length of `K_D` tends to zero.  Given any
`x in partial K_infty`, choose boundary points `x_D in partial widehat K_D` with
`x_D->x`.  Each `x_D` lies on a polygon edge whose endpoint is a vertex at distance
tending to zero.  Therefore there exist normalized vertices `v_D` with

```math
v_D\to x.
```

Hence

```math
\boxed{
\partial K_\infty
\subseteq
\liminf V_D.
}
\tag{6.2}
```

---

## 7. The full force hull must have the same boundary

Because every `v_D in V_D` lies on `partial F_D`, and
`widehat F_D->F_infty`, the standard supporting-normal compactness argument gives:
if `v_D->x`, then

```math
x\in\partial F_\infty.
```

Using Section 6,

```math
\boxed{
\partial K_\infty\subseteq\partial F_\infty.
}
\tag{7.1}
```

We need only the following elementary convexity fact.

### Lemma CW.2 — nested full-boundary rigidity

If compact convex bodies `K subset F` have nonempty interior and

```math
\partial K\subseteq\partial F,
```

then `K=F`.

### Proof

Suppose `y in F\setminus K`.  Choose `x_0 in int(K)`.  The segment from `x_0` to `y`
leaves `K` at some `z in partial K`.  Since `x_0 in int(F)` and `z` is a strict convex
combination of `x_0` and `y`, a small ball around `x_0` contracts along the segment to
a small ball around `z` contained in `F`.  Hence `z in int(F)`, contradicting
`z in partial F`.  `square`

Apply CW.2 to (4.3) and (7.1):

```math
\boxed{F_\infty=K_\infty.}
\tag{7.2}
```

But the full force hull contains an actual source diameter, so

```math
\operatorname{diam}F_\infty=1.
\tag{7.3}
```

Equation (4.4) gives instead

```math
\operatorname{diam}K_\infty=\lambda_*<1.
```

Contradiction.  This proves CW.1.

---

## 8. Uniform nonattainment gap

BF proves

```math
\liminf\lambda_D\ge\lambda_{BVE}.
```

If CW.2 failed, choose for each integer `j` a sufficiently large survivor with

```math
\lambda_D<\lambda_{BVE}+1/j.
```

A diagonal subsequence would then satisfy

```math
\lambda_D\to\lambda_{BVE},
```

contradicting CW.1.  Hence some absolute `epsilon_CW>0` exists.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| endpoint attachment capacity saturates | proved | lower area equals BVE + DD upper capacities |
| one component has `delta_*/D->lambda_BVE` | proved | sum-square concentration |
| dominant attachment hull has `diam/D->lambda_BVE` | proved | BVE area saturation |
| dominant hull `per/diam->pi` | proved | otherwise Bonnesen annulus is strictly thinner and BVE diameter bound contradicts `diam F=D` |
| Hausdorff limit has constant width | proved | Cauchy widths plus maximal perimeter |
| constant-width limit is strictly convex | proved | opposite support point argument |
| polygon vertices become dense | proved | a macroscopic limiting edge would violate strict convexity |
| nested-boundary rigidity | proved | convex segment from an interior point |
| exact BVE endpoint impossible | proved | would force `diam F_infty=lambda_BVE<1` |
| positive gap above BVE endpoint | proved nonconstructively | diagonal-sequence argument |
| Level I | still open | survivors with larger surplus remain possible |

---

## 10. Next run

Quantify the strictness in Section 3 or Section 6.  A perimeter deficit

```math
\pi\operatorname{diam}K_*-\operatorname{per}K_*
```

shrinks the Bonnesen annulus and therefore improves the BVE coefficient explicitly.
Conversely, near-maximal perimeter makes the attachment hull close to a constant-width
body, while its shared force-hull boundary vertices constrain any larger containing
force hull.  An explicit stability modulus for either step would convert
`epsilon_CW` into the next certified generic surplus increase.
