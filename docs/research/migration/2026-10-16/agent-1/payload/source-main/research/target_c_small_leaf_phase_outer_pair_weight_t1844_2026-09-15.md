# Target C-II — `t<=1.844` forces a linear O--O family in the smallest leaf phase

**Date:** 2026-09-15  
**Status:** proof-only phase-resolved structural theorem  
**Scope:** full-core Type-II branch with the corrected `g=0.0076` matched floor  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The dominant double-outer bootstrap previously produced a large O--O family somewhere in the three-phase dominant orbit.  This note resolves that family by exact phase.

For every survivor with

\[
\boxed{t=(q-k)/D\le1.844,}
\]

write the dominant exact `pi/3` orbit phase masses as

\[
C\ge U\ge V\ge0.
\]

Freeze shrinking phase windows around these three exact atoms and perform the hostile-audited joint routewise retention.  Let `z_C,z_U,z_V` be the retained dominant outer-occurrence masses in the three windows, and define the retained O--O pair weight in the smallest leaf window by

\[
P_V={1\over D}
\sum_{\tau\in V\text{-window}}
\min(a_\tau,b_\tau),
\]

where `a_tau,b_tau in[0,1]` are the retained weights of the two outer terminal occurrences, with a missing outer terminal assigned weight zero.

Then

\[
\boxed{
z_C,z_U,z_V>0.616-o(1),}
\tag{LV.1}

\[
\boxed{V<0.5311+o(1),}
\tag{LV.2}

and consequently

\[
\boxed{P_V>0.0848-o(1).}
\tag{LV.3}

Thus all three exact phase atoms are present, and a **specific leaf phase** contains a linear weighted family of outer-to-outer complete stopped trains.  Every train in that family is pairwise noncrossing with the other trains of the same phase and is subject to Section-157 two-sided actual-diameter bracing.

---

## 1. Retained dominant outer mass at `t<=1.844`

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
C_{76}=2\sqrt{\Delta_2}+0.0076,
\]

and retain

\[
U_{net}={9t\over2}-2\pi-2\delta-\kappa/2.
\]

The matched atomic theorem gives `U_net>=C76-o(1)`.  The shared-retention and restored complement-rhombus-incidence inequalities give total retained dominant outer-occurrence mass

\[
z=z_C+z_U+z_V.
\]

Rerunning the finite bootstrap at the endpoint `T=1.844` with the stronger `C76` input gives the exact rounded implications

\[
0\Longrightarrow z>2.0720-o(1),
\]

\[
2.0720\Longrightarrow z>2.1850-o(1),
\]

\[
2.1850\Longrightarrow z>2.2033-o(1),
\]

\[
2.2033\Longrightarrow z>2.2064-o(1),
\]

\[
2.2064\Longrightarrow z>2.2069-o(1).
\tag{LV.4}

The companion exact verifier checks every implication with outward rational arithmetic.  Hence

\[
\boxed{z>2.2069-o(1).}
\tag{LV.5}

The same certificate gives the uniform outer-energy ceiling

\[
\delta<0.051295+o(1).
\tag{LV.6}

---

## 2. Phasewise bathtub energy

The ordinary dominant-orbit energy theorem records only the total retained measure and then allows all three orbit directions at once.  Before taking that relaxation, decompose the retained measure by exact phase.

For one phase atom `phi`, let `nu_phi` be the limiting retained outer-occurrence measure on the projective loaded-hull direction circle.  Joint routewise retention gives

\[
0\le\nu_\phi\le d\theta
\]

as measures, because the total retained dominant measure is already dominated by the round loaded-hull perimeter measure.  If `z_phi=nu_phi(R/pi Z)`, each retained occurrence in this phase pays projective directional energy at least

\[
1-\cos d(\theta,\phi).
\]

The one-well bathtub minimum is therefore

\[
\boxed{
f(z_\phi)
:=z_\phi-2\sin(z_\phi/2).}
\tag{LV.7}

Indeed, fill the interval of radius `z_phi/2` around `phi` at unit density.  Since `z_phi<=z<pi`, this remains inside the projective circle without wrap ambiguity.

Summing the three disjoint selected edge-energy contributions gives the phase-resolved lower bound

\[
\boxed{
\delta
\ge f(z_C)+f(z_U)+f(z_V)-o(1).}
\tag{LV.8}

The function `f` is increasing and strictly convex on `(0,pi)`.

---

## 3. Every phase carries more than `0.616D` retained outer mass

Suppose, for contradiction, that one phase has retained mass at most

\[
a=0.616.
\]

For fixed total mass `Z>=2.2069`, convexity makes the other two phase masses cheapest when equal.  Moreover, while the exceptional phase mass is below `Z/3`, the quantity

\[
f(x)+2f((Z-x)/2)
\]

decreases with `x`; hence the least possible energy under `x<=a` occurs at

\[
x=a,
\qquad
z_2=z_3={2.2069-a\over2}=0.79545.
\]

The exact verifier proves

\[
f(0.616)+2f(0.79545)
>0.05130558,
\]

while (LV.6) gives

\[
\delta<0.05129454+o(1).
\]

The gap is more than `1.10e-5`.  This contradicts (LV.8).

Therefore

\[
\boxed{z_C,z_U,z_V>0.616-o(1).}
\]

In particular, none of the three orbit atoms can vanish.

---

## 4. The smallest train phase has mass below `0.5311D`

Feed (LV.5) into the dominant energy floor.  Since `F(z)=z-6sin(z/6)` is increasing,

\[
\delta\ge F(2.2069)-o(1).
\]

At `t<=1.844` and `kappa>=0`, the network envelope therefore gives

\[
\boxed{U_{net}<1.915963+o(1).}
\tag{LV.9}

The `g=0.0076` residual-stability theorem then gives exact atomic mass outside the dominant orbit at most

\[
R\le1.05(U_{net}-C_{76})<0.003924+o(1).
\tag{LV.10}

Thus the dominant orbit itself carries strict-rhombus crossing mass

\[
E_{dom}
\ge\Delta_2-{R^2\over4}
>0.90689583-o(1).
\tag{LV.11}

For the dominant orbit phase masses `C>=U>=V`, triangle-freeness gives the generic center capacity

\[
E_{dom}\le C(U+V)=C(W-C),
\tag{LV.12}

where

\[
W=C+U+V\le U_{net}<1.915963+o(1).
\]

If `C<=0.8538`, then `W>1.9` follows already from (LV.11) and `E_dom<=W^2/4`, so `C<W/2`.  Hence the right side of (LV.12) is maximized under the displayed upper bounds by

\[
0.8538(1.915963-0.8538).
\]

The exact certificate proves this is smaller than the lower bound in (LV.11) by more than `2.14e-5`.  Therefore

\[
\boxed{C>0.8538-o(1).}
\tag{LV.13}

Since `U>=V`,

\[
2V\le U+V=W-C.
\]

Using (LV.9) and (LV.13),

\[
\boxed{
V<{1.915963-0.8538\over2}+o(1)
<0.5311+o(1).}
\]

This proves (LV.2).

---

## 5. The smallest leaf phase has linear O--O pair weight

For one complete stopped train `tau` in the smallest leaf window, let `a_tau,b_tau` be its retained outer terminal weights.  The elementary inequality

\[
a_\tau+b_\tau
\le1+\min(a_\tau,b_\tau)
\tag{LV.14}

holds whether the train has two, one, or zero selected outer terminals.

Summing (LV.14) over the smallest-leaf window and then taking the source limit followed by shrinking the phase window gives

\[
z_V\le V+P_V+o(1).
\tag{LV.15}

Equations (LV.1)--(LV.2) therefore imply

\[
P_V
\ge z_V-V-o(1)
>0.616-0.5311-o(1)
>0.0848-o(1).
\]

This proves (LV.3).

---

## 6. Frontier effect

For every current survivor in the live band

\[
1.843555\lesssim t\le1.844,
\]

the dominant exact orbit has the following resolved structure:

1. all three exact phases occur;
2. every phase contributes more than `0.616D` retained outer terminal weight;
3. the smallest train phase has mass below `0.5311D`; and
4. that smallest leaf phase alone contains more than `0.0848D` retained O--O pair weight.

This is substantially sharper than the total dominant O--O bound.  The `V`-phase O--O trains are pairwise noncrossing, all have one exact projective direction, and every one is crossed by actual diameter edges with both transverse signs by Section 157.

The next target is now concrete: couple this ordered `V`-phase O--O family to its near-saturated crossing incidence with the center phase.  A successful theorem should force a large center-by-O--O crossing rectangle and then use cyclic boundary order or cut-resultant differences to constrain diameter-edge reuse.

No Level-I closure is claimed.  C-II remains open.
