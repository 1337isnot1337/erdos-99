# Target C-II — singleton/full-flower normal form extends through `t<=2.02`

**Date:** 2026-09-15
**Status:** proof-only high-`t` scope propagation
**Scope:** canonical full-core/no-macroscopic-container Type-II train-measure branch
**Dependencies:** uniform all-train pentagon sea through `t<=2.02`; exact singleton identity; modern train-slack floor
**Certificate:** `research/verify_target_c_singleton_full_flower_extended_range.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The existing singleton-or-fully-rhombic-pentagon theorem was numerically tabulated only through `t<=1.8623`, but its proof uses no O--O path input. Its only quantitative input is the modern pentagon floor

\[
{P_5\over D}\ge p_5(T)-o(1),\qquad
p_5(T)=\pi+C_{707}-{5T\over2},
\]

where

\[
C_{707}=2\sqrt{\Delta_2}+0.007707,
\qquad
\Delta_2={\pi\over2\sqrt3}.
\]

The uniform all-train theorem now proves this pentagon floor through every fixed `T<2.0215...`. Therefore the same flower argument extends unchanged.

Let `S` be the singleton stopped-train count and let `F_5^{full}` count bounded pentagons whose five sides all border strict rhombi. The exact finite face-side inequality is

\[
P_5-F_5^{full}\le2S.
\tag{EF.1}
\]

Balancing at `s(T)=p_5(T)/3` gives

\[
\boxed{
\max\{S,F_5^{full}\}
\ge s(T)D-o(D)
}
\tag{EF.2}
\]

for every fixed endpoint for which `p_5(T)>0`. In particular this remains a linear dichotomy through `t<=2.02`.

Conditional on the full-flower branch `S<s(T)D+o(D)`, the exact stopped-train identity

\[
2\tau_D=2S+\sigma_R
\]

and the modern floor `\tau_D\ge(0.7467921-o(1))D` give

\[
\boxed{
{\sigma_R\over D}>2(0.7467921-s(T))-o(1).
}
\tag{EF.3}
\]

The exact Mantel identity

\[
{T_R^2\over4}-R_4
={\sigma_R\sqrt{R_4}\over2}+{\sigma_R^2\over16}
\tag{EF.4}
\]

then yields a quadratic strict-rhombus train deficit, while the flower terminal incidences give

\[
\boxed{N_{full}\ge{5\over2}F_5^{full}.}
\tag{EF.5}
\]

The exact outward certificate proves the following safe rows:

\[
\begin{array}{c|c|c|c|c}
T & \max(S,F_5^{full})/D & \sigma_R/D\text{ in full branch}
& (T_R^2/4-R_4)/D^2 & N_{full}/D\\ \hline
1.880 & >0.1179 & >1.257 & >0.697 & >0.2949\\
1.900 & >0.1013 & >1.290 & >0.718 & >0.2532\\
1.920 & >0.0846 & >1.324 & >0.740 & >0.2116\\
1.960 & >0.0513 & >1.390 & >0.783 & >0.1282\\
2.000 & >0.0179 & >1.457 & >0.826 & >0.0449\\
2.010 & >0.0096 & >1.474 & >0.837 & >0.0241\\
2.020 & >0.0013 & >1.490 & >0.848 & >0.00327
\end{array}
\tag{EF.6}
\]

This changes the post-path frontier. The path mass disappears near `t=1.861799`, but the full-core branch does not become structurally unconstrained there. Up to the pentagon-sea threshold it must instead carry one of two network pathologies:

```text
singleton branch:
    linearly many contact edges belong to no strict rhombus;

full-flower branch:
    linearly many source-empty pentagons are terminated on all five sides
    by non-singleton rhombic trains,
    while the rhombic train graph is very far from the Mantel endpoint.
```

The balanced population tends to zero as `T` approaches the pentagon positivity threshold, so this theorem alone cannot close the entire interval. It does, however, remove the obsolete `1.8623` cutoff from the flower normal form and makes the high-`t` obstruction available for composition with the multi-rhombic and isolate-host theorems.

**Disposition:** proved proof-only singleton/full-flower extension through `t<=2.02`. C-II and Level I remain open.
