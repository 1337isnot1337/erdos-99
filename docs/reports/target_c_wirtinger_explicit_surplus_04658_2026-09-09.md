<!-- theorem-state: {"artifact_id":"ART-FF0623F40478","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Wirtinger detour raises the explicit pinned/contact floor to 0.4658

**Date:** 2026-09-09  
**Repository base:** current PR #138 branch after WD  
**Run type:** explicit asymptotic branch exclusion  
**Target:** Target C C-II after PI/JC/PC/WD  
**Depends on:** `target_c_detour_explicit_surplus_0465_2026-09-09.md`, with OD replaced by the sharper WD detour constant  
**LEVEL I STATUS:** STILL OPEN

The DE report proved

\[
\liminf\frac{e_{BB}+2s_C}{D}\ge0.465
\]

using the ellipse detour constant `pi/(4sqrt(2))`.  WD replaces that constant by the smaller exact value `sqrt(2)/pi`.  The DE proof then carries through verbatim and gives the stronger explicit floor

\[
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge0.4658.
}
\tag{WE.1}
\]

The endpoint margin is more than `6e-3`, so the improvement is not sensitive to displayed decimal truncation.

---

## 1. Reuse the DE scalar reduction

Put

\[
\lambda:=\lim\frac{e_{BB}+2s_C}{D}
\]

along an arbitrary convergent post-ZF subsequence, and define

\[
A_{PI}:=\frac12\sin(2\rho),
\qquad
L(\lambda):=A_{PI}-\frac\pi4\lambda^2,
\tag{WE.2}
\]

where `rho=cos rho`.

DE combines the PI/GU lower attachment-gap bound with the actual-perimeter JC upper bound and proves that every survivor must satisfy

\[
z+\varepsilon\le R(\lambda),
\tag{WE.3}
\]

where

\[
z:=\frac hD-\frac\pi2,
\qquad
\varepsilon:=\pi-\frac{per(F)}D\ge0,
\]

and

\[
\boxed{
R(\lambda)
:=
\lambda+\frac\pi2
-2\sqrt{\pi L(\lambda)}.
}
\tag{WE.4}
\]

Consequently, if `nu=lim Q/D`,

\[
\frac{L_{chain}}D
\le\pi+2R-2\nu,
\tag{WE.5}
\]

\[
\frac{U_{det}}D
\le2R-\nu,
\tag{WE.6}
\]

and

\[
0\le\nu\le2R.
\tag{WE.7}
\]

No change is made to these parts of DE.

---

## 2. Insert the sharper WD pocket bound

WD proves

\[
H_{out}
\le
C_W L_{chain}^{3/2}U_{det}^{1/2},
\qquad
\boxed{C_W:=\frac{\sqrt2}{\pi}}.
\tag{WE.8}
\]

Using WE.5-WE.7 and discarding the negative `nu` terms gives

\[
\boxed{
\limsup\frac{H_{out}}{D^2}
\le
C_W(\pi+2R)^{3/2}\sqrt{2R}.
}
\tag{WE.9}
\]

CC's exceptional-face estimate is unchanged:

\[
\limsup\frac{A_{exc}}{D^2}
\le\frac{R^2}{\pi}.
\tag{WE.10}
\]

Since ZG/GU gives

\[
G\le H_{out}+A_{exc}+O(D),
\]

every survivor must satisfy the one-variable necessary condition

\[
\boxed{
L(\lambda)
\le
U_W(\lambda)
:=
\frac{\sqrt2}{\pi}
(\pi+2R(\lambda))^{3/2}
\sqrt{2R(\lambda)}
+
\frac{R(\lambda)^2}{\pi}.
}
\tag{WE.11}
\]

This is exactly DE.27 with the improved WD constant.

---

## 3. Monotonicity

DE already proves

\[
L'(\lambda)=-\frac\pi2\lambda<0
\]

and

\[
R'(\lambda)
=1+
\frac{\pi^2\lambda}{2\sqrt{\pi L(\lambda)}}
>0
\]

throughout the positive-`L` interval.  The right side `U_W` is an increasing function of nonnegative `R`.

Therefore, to exclude every

\[
\lambda\le\lambda_*,
\]

it is enough to verify

\[
L(\lambda_*)>U_W(\lambda_*).
\tag{WE.12}
\]

If `R(lambda)<0`, the earlier JC inequality is already impossible.

---

## 4. Endpoint `lambda_*=0.4658`

Take

\[
\boxed{\lambda_*=0.4658.}
\]

Using

\[
\rho
=0.7390851332151606416553\ldots
\]

gives

\[
A_{PI}
=0.4978566363242109995910\ldots .
\tag{WE.13}
\]

Then

\[
\boxed{
L(\lambda_*)
=0.32744907955520547\ldots,
}
\tag{WE.14}
\]

\[
\boxed{
R(\lambda_*)
=0.00808788682687567\ldots,
}
\tag{WE.15}
\]

and

\[
\boxed{
U_W(\lambda_*)
=0.32128926820354703\ldots .
}
\tag{WE.16}
\]

Hence

\[
\boxed{
L(\lambda_*)-U_W(\lambda_*)
=0.00615981135165844\ldots>0.
}
\tag{WE.17}
\]

The necessary condition WE.11 fails at `lambda_*`; monotonicity makes it fail for every smaller `lambda` as well.  This proves WE.1.

---

## 5. Comparison with preceding explicit bounds

The report-level sequence is now

\[
0.4633168954\ldots
\quad\text{(JC)},
\]

\[
0.4647922503\ldots
\quad\text{(GS)},
\]

\[
0.465
\quad\text{(DE / ellipse detour)},
\]

\[
\boxed{0.4658}
\quad\text{(WE / Wirtinger detour)}.
\]

The point of WE is not the fourth decimal place by itself.  It establishes that the cavity threshold is controlled by the **metric detour** of the outer contact chains, a quantity absent from the previous scalar optimization.

---

## 6. Remaining slack

WE still throws away several favorable terms:

1. `L_chain/D <= pi+2R-2nu` is relaxed to `pi+2R`;
2. `U_det/D <=2R-nu` is relaxed to `2R`;
3. `A_exc/D^2<=nu^2/(4pi)` is then bounded only by `R^2/pi`;
4. the negative `s_Z`, `d_H`, and `c_B` terms in PC/OD are discarded;
5. the exact PI force-hull area floor can depend on `h/D`, but WE uses only the universal constant `A_PI`.

A joint optimization retaining `nu` is therefore expected to improve `0.4658` further.  Such an optimization should be proved as a finite analytic inequality or independently certified; WE does not promote a numerical optimizer output to theorem status.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| WE.11 necessary condition | proved | DE reduction + WD constant |
| monotonic endpoint reduction | proved | inherited DE derivatives |
| endpoint margin WE.17 | direct evaluation | margin `>0.006` |
| explicit floor `0.4658` | proved asymptotically | WE.11-WE.17 |
| optimal WD/JC floor | not claimed | favorable defect terms discarded |
| Level I | still open | high-surplus coexistence remains |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

DE defines
    L(lambda)=A_PI-(pi/4)lambda^2,
    R(lambda)=lambda+pi/2-2sqrt(pi L(lambda)),
and proves
    L_chain/D <= pi+2R-2(Q/D),
    U_det/D   <= 2R-(Q/D),
    0<=Q/D<=2R.

WD sharpens the pocket constant to C_W=sqrt(2)/pi, hence every survivor must obey
    L(lambda)
      <= C_W(pi+2R)^(3/2)sqrt(2R)+R^2/pi.

At lambda=0.4658:
    L=0.32744907955520547...,
    R=0.00808788682687567...,
    RHS=0.32128926820354703...,
    L-RHS=0.00615981135165844...>0.
Monotonicity excludes all smaller lambda.
Therefore
    liminf (e_BB+2s_C)/D >= 0.4658.
```
