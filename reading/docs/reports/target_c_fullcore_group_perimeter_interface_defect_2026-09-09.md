> Generated reading edition · [exact source](../../../docs/reports/target_c_fullcore_group_perimeter_interface_defect_2026-09-09.md) · source SHA-256 `d975cdeaa8fb8e154f73c9d33a4158110b40dda71d2df1c1532bb52a890c3443`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-32FF3BB6D683","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fullcore_group_perimeter_interface_defect_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=20b871accb897917673ebf6c0c6a08eec3b64a03; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — full-core semicircle groups force two loaded-interface defect units without cap minimality

**Date:** 2026-09-09  
**Repository branch:** `research/fullcore-interface-perimeter-2026-09-09`  
**Run type:** asymptotic group-perimeter / exact-ledger continuation  
**Target:** full-core `x_B=o(D)` near-circle endpoint  
**Depends on:** HG two-semicircle groups, C36/C49 attachment cells, HBd, NC, NBd, ZU, ZT, local component face identity LI.2  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

LI proved

```math
Q_B\ge (2-o(1))D
```

only under the extra cap-minimal hypothesis `S/D->2`, because its lower bound for the internal Eppstein slack `R_I` used two individual semicircle carriers.

That hypothesis is unnecessary.

HG already proves that **every** full-core near-circle survivor has two dominant attachment-cell groups whose unions converge in measure to complementary half-disks. Perimeter lower semicontinuity, together with the fact that every attachment hull lies within distance one of its harmonic component, converts that group-level half-disk geometry into a lower bound for the sum of the component outer-walk lengths.

The result is

```math
\boxed{
R_I\ge
\left(\frac{\pi+2}{2}-o(1)\right)D
+\frac12Q_{\rm all-int}-S.
}
\tag{GP.1}
```

The `-S` term then cancels **exactly** against the `+S` in NBd. Consequently the two-unit loaded-interface theorem becomes unconditional inside the full-core near-circle phase:

```math
\boxed{
Q_B:=Q-Q_{\rm all-int}\ge(2-o(1))D.
}
\tag{GP.2}
```

Thus nesting extra harmonic components inside the two semicircle groups cannot evade the loaded-interface defect obligation.

---

## 1. Setup

Let `I_r` be the unloaded harmonic components after deleting the loaded terminal set `B`. Write

- `n_r=|I_r|`;
- `K_r=conv(I_r)`;
- `A_r` for the distinct loaded attachment set;
- `P_r=conv(A_r)` for the C49 attachment cell;
- `k_r` for the outer-face boundary-walk length of the connected unit-contact graph `C[I_r]`;
- `delta_r` for its contact-graph diameter;
- `Q_r` for its internal bounded-face degree excess;
- `r_r=2n_r-delta_r-2-e_r` for its Eppstein slack.

Put

```math
S:=\sum_r\delta_r,
\qquad
R_I:=\sum_rr_r,
\qquad
Q_{\rm all-int}:=\sum_rQ_r.
```

As in LI, every bounded full-contact face with no loaded terminal is an internal face of exactly one `C[I_r]`, so

```math
Q_B:=Q-Q_{\rm all-int}
```

is exactly the bounded-face defect carried by faces incident to at least one loaded terminal.

Throughout this report assume the full-core near-circle endpoint

```math
x_B=o(D),
\qquad
(n-v)/D^2\to0.
\tag{1.1}
```

HG then supplies two dominant maximal-cap groups `G_1,G_2`, each asymptotically occupying one of two complementary radius-`D/2` semicircles and each carrying half the quadratic unloaded population.

---

## 2. Attachment-hull perimeter is controlled by the component outer walk

Every loaded attachment `b in A_r` has a unit contact to at least one vertex of `I_r`. Hence

```math
A_r\subset K_r+B(0,1).
```

The right side is convex, so

```math
P_r=\operatorname{conv}(A_r)
\subset K_r+B(0,1).
\tag{2.1}
```

Planar convex perimeter is monotone under inclusion. Steiner's parallel-body formula therefore gives

```math
\operatorname{per}(P_r)
\le
\operatorname{per}(K_r+B(0,1))
=
\operatorname{per}(K_r)+2\pi.
\tag{2.2}
```

The outer-face walk of the connected plane graph `C[I_r]` is a closed polygonal walk of length `k_r` whose convex hull is `K_r`. The perimeter of the convex hull of any closed rectifiable walk is at most the walk length. Thus

```math
\operatorname{per}(K_r)\le k_r.
\tag{2.3}
```

Combining (2.2)--(2.3),

```math
\boxed{
k_r\ge\operatorname{per}(P_r)-2\pi.}
\tag{GP.3}
```

HBd proves `c_I=o(D)`, so summing the additive `2pi` error over all harmonic components costs only `o(D)`.

---

## 3. Each dominant group pays one half-disk perimeter

Normalize by `D` and use the common translations/rotations from HG. For `i=1,2`, let

```math
E_{i,D}:=D^{-1}\bigcup_{r\in G_i}P_r.
```

The attachment-cell interiors are pairwise disjoint. HG proves that the cells in `G_i` lie asymptotically inside a fixed diameter-one semicircle `H_i`, and that

```math
\operatorname{area}(E_{i,D})\to\operatorname{area}(H_i)=\frac\pi8.
\tag{3.1}
```

The containing cap itself converges to `H_i`. Therefore

```math
\mathbf 1_{E_{i,D}}\to\mathbf 1_{H_i}
\quad\text{in }L^1.
\tag{3.2}
```

For completeness, the only perimeter fact needed here is the standard lower semicontinuity under `L^1` convergence:

```math
\operatorname{per}(H_i)
\le
\liminf_D\operatorname{per}(E_{i,D}).
\tag{3.3}
```

It follows immediately from the variational characterization

```math
\operatorname{per}(E)
=
\sup_{\substack{\varphi\in C_c^1(\mathbb R^2;\mathbb R^2)\\
\|\varphi\|_\infty\le1}}
\int_E\operatorname{div}\varphi,
```

because each fixed test-field integral is continuous under `L^1` convergence.

Perimeter is subadditive for finite unions of finite-perimeter sets, and each `P_r` is a convex polygon. Hence

```math
\operatorname{per}(E_{i,D})
\le
\frac1D\sum_{r\in G_i}\operatorname{per}(P_r).
\tag{3.4}
```

The diameter-one semicircle has perimeter

```math
\operatorname{per}(H_i)=1+\frac\pi2.
```

Equations (3.3)--(3.4) give

```math
\boxed{
\sum_{r\in G_i}\operatorname{per}(P_r)
\ge
\left(1+\frac\pi2-o(1)\right)D,
\qquad i=1,2.
}
\tag{GP.4}
```

All remaining groups have nonnegative perimeter, so summing the two dominant groups yields

```math
\boxed{
\sum_r\operatorname{per}(P_r)
\ge(\pi+2-o(1))D.
}
\tag{GP.5}
```

Insert GP.3 and `c_I=o(D)`:

```math
\boxed{
\sum_r k_r\ge(\pi+2-o(1))D.
}
\tag{GP.6}
```

This is the group-level replacement for SI's two-individual-carrier semicircle-perimeter bound.

---

## 4. Convert group perimeter into exact internal slack

For every unloaded component, LI's local Euler identity is exact:

```math
r_r=\frac{k_r+Q_r}{2}-\delta_r.
\tag{4.1}
```

Sum over all components:

```math
R_I
=\frac12\sum_rk_r
+\frac12Q_{\rm all-int}
-S.
\tag{4.2}
```

Apply GP.6:

```math
\boxed{
R_I\ge
\left(\frac{\pi+2}{2}-o(1)\right)D
+\frac12Q_{\rm all-int}
-S.
}
```

This proves GP.1.

The point is the sign of `S`: unlike the cap-minimal SI/LI argument, no upper or equality control of `S` is required. The exact NBd ledger contains the opposite `+S`, so the entire harmonic graph-diameter budget disappears in the next step.

---

## 5. Exact NBd cancellation

NBd gives

```math
S+R_I+s_B+2E_{BB}+3c_I+s_C=q+2x_B.
\tag{5.1}
```

In the near-circle branch, NC and HBd give

```math
E_{BB}=o(D),
\qquad
c_I=o(D),
\tag{5.2}
```

while DC gives

```math
q=(\pi+o(1))D,
\qquad
x_B=o(D).
\tag{5.3}
```

Insert GP.1 into (5.1). The `S` terms cancel exactly:

```math
\left(\frac\pi2+1-o(1)\right)D
+\frac12Q_{\rm all-int}
+s_B+s_C
\le
(\pi+o(1))D.
```

Therefore

```math
\boxed{
s_B+s_C+\frac12Q_{\rm all-int}
\le
\left(\frac\pi2-1+o(1)\right)D.
}
\tag{GP.7}
```

In particular,

```math
\boxed{
s_C
\le
\left(\frac\pi2-1+o(1)\right)D
-\frac12Q_{\rm all-int}.
}
\tag{GP.8}
```

---

## 6. Push the defect to loaded-interface faces

HBd combines NC with ZU to give

```math
d_H+s_Z=s_C+o(D).
\tag{6.1}
```

ZT gives the exact terminal partition

```math
q=x_B+Q+2(d_H+s_Z).
\tag{6.2}
```

Thus, using (5.3), (6.1), and GP.8,

```math
\begin{aligned}
Q
&=q-x_B-2(d_H+s_Z)\\
&=(\pi+o(1))D-2s_C\\
&\ge
(\pi+o(1))D
-2\left[
\left(\frac\pi2-1+o(1)\right)D
-\frac12Q_{\rm all-int}
\right]\\
&=Q_{\rm all-int}+(2-o(1))D.
\end{aligned}
```

Hence

```math
\boxed{
Q_B=Q-Q_{\rm all-int}\ge(2-o(1))D.
}
```

This proves GP.2.

---

## 7. What changed

The old LI theorem needed

```math
S/D\to2
```

in order to identify two individual half-density semicircle carriers and derive their outer-walk cost.

GP replaces that step by a group-perimeter argument. HG already gives two **groups** whose attachment-cell unions converge to half-disks. The unit attachment distance transfers the group attachment-hull perimeter to the sum of component outer walks with only `2pi c_I=o(D)` loss.

Therefore nesting is irrelevant at leading order:

```text
full core + near circle
    -> two half-disk attachment-cell groups (HG)
    -> total attachment-hull perimeter >= (pi+2)D-o(D)
    -> total component outer walk >= (pi+2)D-o(D)
    -> R_I >= (pi+2)D/2 + Q_int/2 - S-o(D)
    -> exact NBd cancels S
    -> s_C + Q_int/2 <= (pi/2-1)D+o(D)
    -> ZU + ZT
    -> Q_B >= 2D-o(D).
```

So the sharp loaded-interface obstruction is now present in **every** full-core near-circle survivor.

---

## 8. Audit / failure modes

- No claim is made that `per(conv(I_r))` itself approaches a semicircle perimeter. Only the attachment-cell union has that shape; GP.3 is the bridge between the two objects.
- The `2pi` parallel-body loss is summed only after HBd supplies `c_I=o(D)`.
- `L^1` convergence is justified by both containment in the convergent dominant cap and saturation of its area; area convergence alone without containment would be insufficient.
- Perimeter lower semicontinuity is applied to the **union** of one group, then perimeter subadditivity passes to the sum of cell perimeters. No false monotonicity of perimeter for disconnected unions is used.
- The theorem remains asymptotic. It does not supply an `O(1)` additive gap above `2D`.
- A long thin loaded-interface face, or a linear family of near-degenerate pentagonal interface faces, remains a valid regression at this stage.

---

## 9. Next target

The full-core near-circle endpoint is now uniformly reduced to

```math
Q_B\ge(2-o(1))D,
```

with no cap-cost split.

The next theorem should exploit the **geometry of the loaded-interface faces themselves**. A useful quantitative split is:

1. macroscopic interface faces: use strict convexity, unit separation, and half-disk area saturation to show that a face of perimeter `lambda D` removes a definite boundary-order amount of usable half-disk capacity;
2. submacroscopic interface faces: use the one-interior-contact-slot property of all but `o(D)` loaded terminals and stopped-train incidence to charge their total degree excess to distinct boundary slots.

Any estimate whose combined maximum is strictly below `2D` closes the full-core near-circle branch.
