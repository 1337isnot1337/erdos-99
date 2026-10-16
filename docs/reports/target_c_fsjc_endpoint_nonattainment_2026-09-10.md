<!-- migration-source: path=docs/reports/target_c_fsjc_endpoint_nonattainment_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=11c38e20bdf064ec4bd9abd74d1c74ec9bde1f68; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — FSJC endpoint nonattainment by constant-width area

**Date:** 2026-09-10  
**Repository state:** branch from `1ea7a3c5970d614c9f860841eea5ad3718ca171f`  
**Run type:** equality-case exclusion / compactness  
**Target:** Target C C-II after FSDB/FSJC  
**External input:** Rosenthal--Szász and Blaschke--Lebesgue exactly as audited in `target_c_joint_cavity_threshold_nonattainment_2026-09-09.md`  
**Computation:** no numerical computation is a proof dependency

## LEVEL I STATUS

`STILL OPEN`

Let

\[
L=e_{BB}+2s_C,
\qquad
\lambda_* =0.5882283437736394\ldots
\]

where `lambda_*` is the positive root of

\[
(\pi^2+1)\lambda^2+\pi\lambda-\frac{\pi^2}{4}-\pi=0.
\tag{FN.1}
\]

FSJC proves

\[
\liminf \frac LD\ge\lambda_*
\]

and shows that approach to this scalar endpoint forces `h/D -> pi/2`.
The equality case is in fact impossible.

### Theorem FN — the FSJC endpoint is uniformly excluded

There exists an absolute constant `eta_FS>0` such that every sufficiently large audited post-ZF survivor satisfies

\[
\boxed{
\frac{e_{BB}+2s_C}{D}\ge\lambda_*+\eta_{FS}.
}
\tag{FN.2}
\]

The theorem is qualitative: no explicit value of `eta_FS` is claimed.

The new content is not another decimal iteration.  It eliminates the entire near-FSJC equality class.  A sequence trying to approach the endpoint would force the force hull to have asymptotically maximal perimeter, hence a constant-width Hausdorff limit.  Blaschke--Lebesgue then gives strictly more force-hull area than the FSJC equality budget can accommodate.

---

## 1. Endpoint data from FSJC

Assume for contradiction that there is an unbounded post-ZF survivor sequence indexed by `j` with

\[
\lambda_j:=\frac{e_{BB,j}+2s_{C,j}}{D_j}\longrightarrow\lambda_*.
\tag{1.1}
\]

Pass to a subsequence on which

\[
t_j:=\frac{e_{BB,j}}{D_j}\to t,
\qquad
y_j:=\frac{h_j}{D_j}\to y.
\tag{1.2}
\]

Write

\[
m(y)=\min\{y,\pi-y\},
\qquad
\Phi(y)=\frac{y+\sin y}{4}.
\]

FSDB plus GU and JC give the necessary inequality

\[
\Phi(y)-\frac\pi4\lambda_*^2
\le
\frac{(t+m(y))^2}{4\pi}
\le
\frac{(\lambda_*+m(y))^2}{4\pi}.
\tag{1.3}
\]

FSJC proves that the threshold root of the rightmost relaxed inequality is uniquely minimized at

\[
y=\frac\pi2.
\]

Therefore (1.1)--(1.3) force

\[
\boxed{y=\frac\pi2.}
\tag{1.4}
\]

At this value, FN.1 is exactly the equality

\[
\Phi(\pi/2)-\frac\pi4\lambda_*^2
=
\frac{(\lambda_*+\pi/2)^2}{4\pi}.
\tag{1.5}
\]

The first inequality in (1.3) can therefore hold only if `t=lambda_*`; otherwise its right side is strictly smaller than (1.5). Hence

\[
\boxed{
t=\lambda_*,
\qquad
\frac{s_{C,j}}{D_j}\to0.
}
\tag{1.6}
\]

Define the common equality value

\[
U_*:=
\Phi(\pi/2)-\frac\pi4\lambda_*^2
=
\frac{(\lambda_*+\pi/2)^2}{4\pi}.
\tag{1.7}
\]

The FSDB/GU lower bound and JC upper bound now squeeze the attachment-cell gap `G_j`:

\[
\boxed{
\frac{G_j}{D_j^2}\longrightarrow U_*.
}
\tag{1.8}
\]

Indeed the lower normalized limit is at least the left side of (1.7), while the upper normalized limit is at most the right side.

---

## 2. Tight cavity capacity forces maximal force-hull perimeter

Retain the JC notation

\[
E_{out}=\sum_P(L_P-3),
\qquad
z=Q+2s_Z,
\qquad
d_H=q-h.
\]

The exact remainder form of JC.12 is

\[
\boxed{
E_{out}+Q
\le
\pi D-h+e_{BB}
-
\left[(\pi D-P_F)+3d_H+(z-Q)\right],
}
\tag{2.1}
\]

where `P_F=per(F)` and every term in brackets is nonnegative. Since

\[
z-Q=2s_Z,
\]

write the bracket as

\[
R_j=(\pi D_j-P_{F,j})+3d_{H,j}+2s_{Z,j}\ge0.
\tag{2.2}
\]

JC also gives

\[
G_j
\le
H_{out,j}+A_{exc,j}+O(D_j)
\le
\frac{(E_{out,j}+Q_j)^2}{4\pi}+o(D_j^2).
\tag{2.3}
\]

By (1.4) and (1.6),

\[
\frac{\pi D_j-h_j+e_{BB,j}}{D_j}
\longrightarrow
\frac\pi2+\lambda_*.
\tag{2.4}
\]

If `R_j/D_j` did not tend to zero, some subsequence would have `R_j>=epsilon D_j` for a fixed `epsilon>0`. Equations (2.1)--(2.4) would then give

\[
\limsup\frac{G_j}{D_j^2}
\le
\frac{(\lambda_*+\pi/2-\epsilon)^2}{4\pi}
<U_*,
\]

contradicting (1.8). Therefore

\[
\boxed{
\frac{R_j}{D_j}\to0.
}
\tag{2.5}
\]

Since all three terms in (2.2) are nonnegative, individually

\[
\boxed{
\frac{P_{F,j}}{D_j}\to\pi,
\qquad
\frac{d_{H,j}}{D_j}\to0,
\qquad
\frac{s_{Z,j}}{D_j}\to0.
}
\tag{2.6}
\]

Only the first conclusion is needed for the contradiction.

---

## 3. The normalized force hull converges to constant width

Translate and rescale the force hulls:

\[
\widetilde F_j=D_j^{-1}(F_j-p_j),
\]

choosing one point `p_j in F_j` as origin. Then

\[
\operatorname{diam}(\widetilde F_j)=1.
\]

The normalized bodies lie in a fixed bounded region, so Blaschke selection gives a Hausdorff-convergent subsequence

\[
\widetilde F_j\to F_\infty.
\tag{3.1}
\]

Diameter, perimeter and area are continuous under Hausdorff convergence for planar convex bodies. Equation (2.6) yields

\[
\operatorname{diam}(F_\infty)=1,
\qquad
\operatorname{per}(F_\infty)=\pi.
\tag{3.2}
\]

Rosenthal--Szász states

\[
\operatorname{per}(K)\le\pi\operatorname{diam}(K),
\]

with equality exactly for bodies of constant width equal to the diameter. Hence

\[
\boxed{F_\infty\text{ has constant width }1.}
\tag{3.3}
\]

Blaschke--Lebesgue now gives

\[
\boxed{
\operatorname{area}(F_\infty)
\ge
A_{BL}:=\frac{\pi-\sqrt3}{2}.
}
\tag{3.4}
\]

Thus

\[
\liminf_j\frac{\operatorname{area}F_j}{D_j^2}
\ge A_{BL}.
\tag{3.5}
\]

---

## 4. Constant width exceeds the FSJC equality budget

GU gives, along (1.1),

\[
\limsup_j
\frac1{D_j^2}
\sum_r\operatorname{area}(P_{r,j})
\le
\frac\pi4\lambda_*^2.
\tag{4.1}
\]

Since

\[
G_j=\operatorname{area}F_j-\sum_r\operatorname{area}(P_{r,j}),
\]

(3.5)--(4.1) imply

\[
\liminf_j\frac{G_j}{D_j^2}
\ge
A_{BL}-\frac\pi4\lambda_*^2.
\tag{4.2}
\]

But (1.8) gives

\[
\frac{G_j}{D_j^2}\to
\Phi(\pi/2)-\frac\pi4\lambda_*^2.
\tag{4.3}
\]

The common subtraction cancels. It remains only to compare

\[
A_{BL}
\quad\text{and}\quad
\Phi(\pi/2)=\frac{\pi+2}{8}.
\]

Their exact difference is

\[
\boxed{
A_{BL}-\Phi(\pi/2)
=
\frac{3\pi-4\sqrt3-2}{8}>0.
}
\tag{4.4}
\]

For a completely elementary sign certificate, use `pi>3` and `sqrt(3)<7/4`:

\[
3\pi>9>4\sqrt3+2.
\]

Thus (4.2) is strictly larger than (4.3), a contradiction.

Numerically, only for scale,

\[
A_{BL}-\Phi(\pi/2)=0.0620718413\ldots .
\]

No decimal enters the proof.

Therefore no unbounded post-ZF survivor sequence can satisfy (1.1). `square`

---

## 5. Uniform gap

FSJC already gives the universal asymptotic lower bound

\[
\liminf\frac LD\ge\lambda_*.
\]

If FN.2 failed for every `eta_FS>0`, choose for each integer `m` a sufficiently large survivor with

\[
\frac LD<\lambda_*+\frac1m.
\]

Using the FSJC lower bound to take the diameters increasingly large gives an unbounded diagonal sequence with

\[
\frac LD\to\lambda_*,
\]

contradicting Sections 1--4. Hence some absolute `eta_FS>0` exists.

This proves FN.2.

---

## 6. Exact effect on the C-II endpoint

FN eliminates the complete near-equality class

\[
\frac{e_{BB}+2s_C}{D}=\lambda_*+o(1).
\]

Any surviving unbounded C-II sequence therefore has a fixed positive separation from the FSJC floor. In particular the formal FSJC optimizer

\[
\frac hD\to\frac\pi2,
\quad
\frac{e_{BB}}D\to\lambda_*,
\quad
\frac{s_C}{D}\to0,
\quad
\frac{P_F}{D}\to\pi,
\quad
\frac{d_H+s_Z}{D}\to0
\]

is impossible.

This is a qualitative class exclusion, not a claimed Level I closure and not merely a new printed decimal.

---

## 7. Audit and regressions

| Item | Classification | Check |
| --- | --- | --- |
| FSJC endpoint forces `h/D->pi/2` | dependency | proved in the September 10 FSJC report |
| endpoint also forces `e_BB/D->lambda_*` | proved here | strictness of `t<=lambda` in the exact equality budget |
| endpoint forces `P_F/D->pi` | proved here | exact nonnegative remainder (2.1) plus cavity saturation |
| constant-width limit | classical dependency | Rosenthal--Szász equality, already audited in JN |
| area floor `(pi-sqrt3)/2` | classical dependency | Blaschke--Lebesgue, already audited in JN |
| strict area mismatch | proved exactly | `(3pi-4sqrt3-2)/8>0` |
| uniform `eta_FS>0` | proved nonconstructively | diagonal compactness |
| explicit value of `eta_FS` | not proved | would require quantitative stability or a different finite inequality |
| Level I | open | survivors with larger pinned/contact currency remain |

Regression checks:

1. **Regular odd shell.** It has near-maximal perimeter and larger area; FN does not exclude it merely for being shell-like. It excludes only simultaneous saturation of the FSJC lower and cavity upper budgets.
2. **Dense isolated fillings.** Isolates are retained in FSDB. FN never assumes that the positive core contains the full source population.
3. **Perfect matching.** Already independently excluded by MFS; FN neither uses nor reopens that branch.
4. **High-surplus survivors.** Explicitly remain. FN proves no universal upper bound on `L/D`.

---

## 8. Failed shortcuts

- Replacing FSJC by the old JN statement without rechecking the new functional area floor would be insufficient. The new proof uses the new endpoint `lambda_*` and verifies a fresh strict area margin.
- Near-maximal perimeter of a finite member is not called constant width. Constant width appears only after Hausdorff compactness and equality in the limiting Rosenthal--Szász theorem.
- The result does not iterate the scalar floor numerically and stop; it excludes the entire asymptotic optimizer class.

---

## 9. Promotion recommendation

**Hold as report pending independent audit.** If FSDB/FSJC are accepted, FN should be indexed immediately after FSJC as the equality-case exclusion. It supersedes applying the older JN theorem only at the obsolete `0.4633...` threshold.

---

## 10. Remaining closing obligation

A Level I proof still needs to exclude all survivors with

\[
\frac{e_{BB}+2s_C}{D}\ge\lambda_*+\eta_{FS}.
\]

A useful next theorem must exploit the resulting high pinned/contact currency itself, or convert it to a strict sub-`D` competitor/source-capacity contradiction. Another isolated lower-bound decimal is not enough.

The most concrete next split is between loaded-loaded contact currency `e_BB` and pinned nullity `s_C`, retaining the exact PC/ZK incidence ledgers. A closure must show that at least one of those two currencies becomes incompatible with triangle-free global optimality at the forced linear scale.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New FN theorem:
Let lambda_* be the FSJC root
  (pi^2+1)lambda^2+pi lambda-pi^2/4-pi=0.
No post-ZF survivor sequence can have
  (e_BB+2s_C)/D -> lambda_*.
Hence some absolute eta_FS>0 exists with
  (e_BB+2s_C)/D >= lambda_*+eta_FS
for all sufficiently large survivors.

Reason:
FSJC endpoint equality forces h/D->pi/2 and e_BB/D->lambda_*.
Exact JC remainder then forces per(F)/D->pi, d_H/D->0, s_Z/D->0.
A normalized Hausdorff limit of F has diameter 1 and perimeter pi, hence
constant width 1. Blaschke--Lebesgue forces area >=(pi-sqrt3)/2.
But the same FSJC equality budget uses force-hull area Phi(pi/2)=(pi+2)/8.
Their difference is
  (3pi-4sqrt3-2)/8 >0,
so the lower gap exceeds the saturated cavity upper gap by a fixed amount.
Contradiction.

Remaining class:
all survivors have pinned/contact currency separated by a positive constant from
lambda_*, but no universal upper bound is yet proved.
```