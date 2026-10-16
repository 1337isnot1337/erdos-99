# Hostile audit — Target C Section 127 interface/augmented-defect dichotomy

**Date:** 2026-09-12
**Artifact:** `research/target_c_section127_interface_augmented_defect_dichotomy.md`
**State lock:** audit.46; theorem authority unchanged
**Verdict:** **PASS at proof-only scope.**

## 1. Exact augmented identity

Canonical Section 123 gives

\[
e_{BB}-k={1\over2}\sum_r(a_r-T_r+Q_r^+)+d_{tile}.
\]

Therefore for

\[
J_{aug}:=\sum_r(a_r-T_r)+\sum_rQ_r^++2d_{tile}
\]

one has exactly

\[
J_{aug}=2(e_{BB}-k).
\]

No asymptotic replacement is used.

**Verdict:** valid.

## 2. Global exceptional-face payment

Canonical Section 63 gives

\[
e_{BB}=Q+2k+u_B+c_B
\]

with `Q,k,u_B,c_B>=0`. Hence

\[
e_{BB}-k=Q+k+u_B+c_B\ge Q.
\]

Every global bounded nonquadrilateral contact face has degree at least five, so each contributes at least one to

\[
Q=\sum_f(\deg f-4).
\]

Thus `Q>=f`, where `f` is the number of such faces, and therefore

\[
J_{aug}=2(e_{BB}-k)\ge2f.
\]

This argument does not identify any augmented local face with a global contact face; only the canonical scalar ledgers are coupled.

**Verdict:** valid.

## 3. Interface theorem composition

Canonical Section 85 proves the finite inequality

\[
q-k+2f\ge2\sqrt{R_4}.
\]

Since `J_aug>=2f`,

\[
(q-k)+J_{aug}\ge(q-k)+2f\ge2\sqrt{R_4}.
\]

All inequality directions are correct.

**Verdict:** valid.

## 4. Type-II limit

In the canonical full-core Type-II branch,

\[
R_4=(\Delta+o(1))D^2,
\qquad \Delta={\pi\over2\sqrt3}.
\]

Hence

\[
{2\sqrt{R_4}\over D}\to2\sqrt\Delta.
\]

Dividing the finite theorem by `D` and taking `liminf` gives

\[
\liminf{(q-k)+J_{aug}\over D}\ge2\sqrt\Delta.
\]

If `J_aug=o(D)`, subtraction of an `o(D)` term gives

\[
\liminf{q-k\over D}\ge2\sqrt\Delta.
\]

Likewise, if along a subsequence

\[
(q-k)/D\le2\sqrt\Delta-\eta+o(1),
\]

then the finite inequality forces

\[
J_{aug}/D\ge\eta-o(1).
\]

**Verdict:** valid.

## 5. Independence from the recent half-perimeter note

The proof of Section 127 does not use the proof-only recent bound

\[
\liminf(q-k)/D\ge\pi/2.
\]

That bound appears only as contextual comparison. Removing it leaves every theorem statement through (127.6) unchanged.

**Verdict:** dependency scope is accurate.

## 6. Interaction with proof-only Section 125

Section 125 gives independently

\[
\liminf D^{-1}
\left[\Delta_{ad}+{A_*\over2}+3Q_*\right]
\ge{\pi\over4}(2-\sqrt3).
\]

If `A_*+Q_*+d_tile=o(D)`, then Section 127 gives the high loaded-density limit and Section 125 gives the linear `Delta_ad` limit. No claim is made that either one alone contradicts global minimality.

**Verdict:** valid.

## 7. Source retention and theorem authority

- No source point is deleted.
- Contact-isolated coordinates never enter the Section-57 affine kernel.
- The finite theorem uses only canonical scalar identities and the canonical global interface inequality.
- Audit.46 remains theorem-state authority; Section 127 is proof-only.

## 8. Surviving obstruction

The theorem leaves two genuine Type-II regimes:

1. high loaded density, potentially with `(q-k)/D` at or above `2sqrt(Delta)` and very small augmented defect;
2. linear augmented/tile defect.

There is no canonical upper bound below `2sqrt(Delta)`, so Section 127 is a dichotomy rather than a closure theorem.

**Final audit verdict:** Section 127 is proof-valid at proof-only scope. C-II remains open.
