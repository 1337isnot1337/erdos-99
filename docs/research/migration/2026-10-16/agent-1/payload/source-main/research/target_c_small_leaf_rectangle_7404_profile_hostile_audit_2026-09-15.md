# Hostile audit — `0.7404D` fan rectangle profile

**Date:** 2026-09-15  
**Reviewed:**
- `target_c_small_leaf_rectangle_7404_profile_2026-09-15.md`
- `verify_target_c_small_leaf_rectangle_7404_profile.py`
- audited `>0.7404D` weighted fan theorem
- corrected dual-tree-backbone rectangle theorem

**Disposition:** **PASS at proof-only `t<=1.844` full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

---

## 1. Weighted thresholding does not recreate the retracted fan-floor error

Let `P_VD=sum w_tau` with `0<w_tau<=1`, and let `d_tau D` be the center degree of
`tau`. The audited fan theorem gives

\[
{\sum w_\tau d_\tau\over\sum w_\tau}>0.7404-o(1),
\]

while every `d_tau<=1.063+o(1)`.

For a threshold `lambda<0.7404`, if `G_D=(1/D)sum_{good}w_tau`, direct weighted
thresholding gives

\[
G_D>{(0.7404-\lambda)P_V\over1.063-\lambda}-o(1).
\]

Only after this inequality is established does the proof use `w_tau<=1` to infer

\[
#\{\tau\ good\}/D\ge G_D.
\]

This is valid. It is not the rejected inference that a weighted average degree itself
is an unweighted train-density floor.

**Verdict:** PASS.

---

## 2. Dual-tree backbone scaling is correct

If `m_D` distinct good leaf trains each have more than `lambda D-o(D)` center
neighbors, total good-leaf/center incidence exceeds `lambda m_DD-o(D^2)`. With fewer
than `1.063D+o(D)` center trains, one center path has length

\[
>{\lambda m_D\over1.063}-o(D).
\]

Substituting the good-train count lower bound gives the claimed

\[
s(\lambda)={\lambda g(\lambda)\over1.063}.
\]

The parent dual-tree theorem guarantees that every other center train meets this
backbone in a consecutive interval; no false global-linear-complement assumption is
reintroduced.

**Verdict:** PASS.

---

## 3. Block averaging and denominator monotonicity have the right sign

For a block of `rho D` consecutive backbone leaf cuts, the parent counting identity
gives some common center neighborhood larger than

\[
\left(\lambda-{1.063\rho\over s/D}\right)D-o(D).
\]

The penalty `1.063 rho/x` is decreasing in `x>0`. Since the actual backbone density
satisfies `s/D>s(lambda)-o(1)`, replacing it by the lower bound `s(lambda)` can only
increase the penalty and weaken the conclusion. Thus

\[
|C_{\lambda,\rho}|>
(\lambda-\alpha(\lambda)\rho)D-o(D)
\]

with `alpha=1.063/s(lambda)` is safe.

**Verdict:** PASS.

---

## 4. Balanced constants are exact

For `lambda=0.561`, the certificate checks

\[
g={47541\over1568750}=0.0303050199\ldots,
\]

\[
s={26670501\over1667581250}=0.0159935241\ldots .
\]

At `rho=0.00831`, the common-center lower density is exactly

\[
{1234784329\over142242672000}
=0.0086808291\ldots,
\]

leaving more than `0.0003708` above the requested balanced shore density. Also
`rho<s`, so the block exists.

**Verdict:** PASS.

---

## 5. High-product constants are exact

For `lambda=0.6`, the certificate checks

\[
g={37206\over1446875}=0.0257147300\ldots,
\]

\[
s={892944\over61521125}=0.0145144289\ldots .
\]

At `rho=0.00409`, the common-center density is

\[
{214634280377\over714355200000}
=0.3004587638\ldots>0.3004.
\]

The resulting complete-crossing product exceeds `0.0012288D^2-o(D^2)`.

**Verdict:** PASS.

---

## 6. Scope

The result strengthens only the phase-resolved `t<=1.844` structural branch. It does
not by itself apply the Section-76 common-order theorem across Section-69 grains, and
it does not claim that the complete rectangle already contradicts the diameter bound.
Those are separate geometric tasks.

**Final disposition:** **PASS. C-II and Level I remain open.**
