# Target C-II — bilateral force-pair order halves the remaining narrow-pair capacity

**Date:** 2026-09-17  
**Status:** proof-only high-`t` quantitative/structural strengthening; no canonical promotion claimed  
**Scope:** exact-antipodal force pairs on one fixed one-sided high-`t` shore through `t=(q-k)/D<=1.8687`  
**Dependencies:** global one-sided switch half-plane/resultant theorem; exact-antipodal exact-force pair; host-cap bilateral force-pair separation; exact diameter-normal order; ordered O--O crosscut rectangle; C67 projective diameter-direction separation; coupled host transverse margin  
**Certificate:** `research/verify_target_c_high_t_ordered_bilateral_narrow_pair_capacity_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The one-arc narrow-pair theorem uses the host transverse margin to show that every projectively narrow exact force pair is almost antiparallel in one common oriented switching semicircle. It then packs the two projective diameter directions into one radius-`rho` neighborhood of the common semicircle boundary and obtains

\[
N_D^{\rm narrow}(\rho)\le \rho D+o(D).
\]

That count treats the `2N` directions as an unordered set. The current bilateral normal form contains more information. At every exact-force interface one force bar is born on each physical host. The two host birth orders are opposite, while the corresponding diameter directions are exact outward hull normals. Therefore, after one global choice of orientation, the lower force lane moves monotonically upward in the common semicircle and the upper force lane moves monotonically downward. Each lane separately spends at least one C67 direction gap per retained interface.

For an almost-antiparallel pair, its projective gap is the sum of the two distances from the common semicircle boundary line. Both of those distances therefore increase by at least one C67 gap at each step. The projective pair gap increases by at least **two** C67 gaps per interface.

This yields the finite capacity

\[
\boxed{
N_D^{\rm narrow}(\rho_D)
\le {\rho_D\over 2\delta_D}+1,
\qquad
\delta_D=2\arcsin{1\over2D},
}
\]

and hence, for fixed `rho`,

\[
\boxed{
N_D^{\rm narrow}(\rho)
\le {\rho\over2}D+o(D).
}
\]

It halves the already-sharpened one-arc loss. The same order statement also strengthens a terminal-terminal paired regime: a TT block of `M` cells forces the far terminal piece to contain a support-normal interval of width at least

\[
2\gamma_H+2(M-1)\delta_D-o(1),
\qquad
\gamma_H=\arcsin c_H.
\]

Thus TT has a fixed macroscopic terminal span even for one cell, plus a deterministic `2 delta_D` widening for every additional cell.

---

## 1. Common semicircle and fixed physical force lanes

Fix one strict side of the common diameter-routing hub. The global one-sided theorem supplies a linear functional `phi` for which every consistently oriented switching diameter direction `d` on this shore satisfies

\[
\phi(d)>0.
\tag{OB.1}
\]

Thus all switching directions and all exact strip reaction directions lie in one open angular semicircle

\[
\mathcal H_\phi=(\beta,\beta+\pi)
\tag{OB.2}
\]

after choosing one real angular lift.

At every exact-antipodal interface `i`, choose the exact positive force pair from the exact-force theorem. Its two lifted angles strictly bracket the exact reaction angle `alpha_i`:

\[
\theta_i^-<\alpha_i<\theta_i^+,
\qquad
\beta<\theta_i^-<\theta_i^+<\beta+\pi.
\tag{OB.3}
\]

The host-cap theorem gives one birth endpoint on each of the two fixed physical O--O host arcs. The selected row phases occupy one shrinking projective window, while every force bar has transverse component at least

\[
c_H-o(1),
\qquad
c_H=0.453819885927\ldots .
\tag{OB.4}

Hence the two physical host normal branches stay a fixed positive angular distance from the row/reaction axis. For sufficiently large `D`, the lower ray in (OB.3) always belongs to one fixed physical host, call it `A`, and the upper ray always belongs to the other, call it `B`. A host swap cannot occur without a selected switching normal crossing the shrinking reaction-axis window, contradicting (OB.4).

Write

\[
a_i:=\theta_i^-,
\qquad
b_i:=\theta_i^+.
\tag{OB.5}

The bars with directions `a_i` are therefore the `A`-born force lane and the bars with directions `b_i` the `B`-born force lane throughout the shore.

---

## 2. The two exact-normal lanes move in opposite angular directions

List any selected exact-force interfaces in their path order on this shore. The proper O--O crosscuts connect the same two disjoint host arcs and are pairwise noncrossing. Their layer subarcs occur in opposite cyclic orders on the two hosts.

Reverse the interface order if necessary so the `A`-host birth subarcs occur forward in the ambient convex-boundary orientation. Then the corresponding `B`-host birth subarcs occur backward.

Every actual diameter direction, oriented outward at its birth endpoint, is an **exact hull support normal**. Outward support-normal angle is monotone along a convex boundary. Therefore the `A`-lane angles increase and the `B`-lane angles decrease:

\[
a_1<a_2<\cdots<a_N,
\qquad
b_1>b_2>\cdots>b_N.
\tag{OB.6}

The inequalities are strict because the force bars at distinct interfaces are distinct actual diameter edges and canonical C67 forbids equal projective diameter directions.

Let

\[
\delta_D:=2\arcsin{1\over2D}.
\tag{OB.7}

C67 gives projective separation at least `delta_D` between any two distinct actual diameter directions. Since all angles in either host lane lie in one lifted interval of width below `pi`, projective separation at least `delta_D` implies ordinary angular separation at least `delta_D`. Thus for consecutive selected interfaces,

\[
\boxed{
a_{j+1}-a_j\ge\delta_D,}
\tag{OB.8}
\]

\[
\boxed{
b_j-b_{j+1}\ge\delta_D.}
\tag{OB.9}
\]

Define the ordinary force-pair opening inside the common semicircle by

\[
\Delta_j:=b_j-a_j\in(0,\pi).
\tag{OB.10}
\]

Then (OB.8)--(OB.9) give the key ordered contraction law

\[
\boxed{
\Delta_j-\Delta_{j+1}\ge2\delta_D.
}
\tag{OB.11}

This statement uses no KKT coefficient lower bound and no endpoint-disjoint thinning. Partner collisions are irrelevant because the order is read from the two distinct birth lanes.

---

## 3. Narrow pairs are one initial segment and consume two C67 gaps per step

The coupled host theorem gives every force ray projective distance at least

\[
\gamma_H-\varepsilon_D,
\qquad
\gamma_H:=\arcsin c_H,
\qquad
\varepsilon_D\to0,
\tag{OB.12}

from its own exact row/reaction axis. Hence

\[
\boxed{
\Delta_j\ge2(\gamma_H-\varepsilon_D).
}
\tag{OB.13}

Let

\[
\eta_j
:=d_{\mathbb{RP}^1}([d_j^-],[d_j^+])
=\min\{\Delta_j,\pi-\Delta_j\}
\tag{OB.14}
\]

be the projective force-pair gap. Suppose `rho_D` satisfies eventually

\[
0<\rho_D<\gamma_H-\varepsilon_D.
\tag{OB.15}

If `eta_j<rho_D`, the ordinary-narrow alternative `Delta_j<rho_D` is impossible by (OB.13). Therefore every `rho_D`-narrow pair is almost antiparallel:

\[
\eta_j=\pi-\Delta_j.
\tag{OB.16}

Combining (OB.11) and (OB.16), whenever two retained narrow pairs occur in increasing interface order,

\[
\boxed{
\eta_{j+1}-\eta_j\ge2\delta_D.
}
\tag{OB.17}

In fact (OB.11) shows that once an interface leaves the near-antipodal `rho_D` window it cannot re-enter it later. The narrow interfaces form an initial segment of the ordered exact-force population.

If there are `N` narrow interfaces, then

\[
\eta_N
\ge \eta_1+2(N-1)\delta_D
\ge2(N-1)\delta_D.
\]

Since `eta_N<rho_D`,

\[
2(N-1)\delta_D<\rho_D.
\]

Thus

\[
\boxed{
N_D^{\rm narrow}(\rho_D)
\le {\rho_D\over2\delta_D}+1.
}
\tag{OB.18}

For every fixed `0<rho<gamma_H`, `D delta_D ->1`, so

\[
\boxed{
N_D^{\rm narrow}(\rho)
\le {\rho\over2}D+o(D).
}
\tag{OB.19}

The previous one-arc theorem had coefficient `rho`. The factor `1/2` here is not another circle-packing estimate. It comes from simultaneous exact-normal motion of both physical force lanes.

---

## 4. Sharpened host-force/TB1 density fork

Use the current host-sharpened parent fork

\[
|E_D|+|U_D|>c_0D-o(D),
\qquad
c_0={113\over20{,}000{,}000}.
\tag{OB.20}

Delete exact-force interfaces whose projective pair gap is below a fixed `rho<gamma_H`. By (OB.19) the deletion costs at most `(rho/2)D+o(D)`. Hence

\[
\boxed{
|S_D^{host}|+|E_D^{force}(\rho)|
>\left(c_0-{\rho\over2}\right)D-o(D).
}
\tag{OB.21}

One mechanism therefore has population

\[
\boxed{
>{1\over2}\left(c_0-{\rho\over2}\right)D-o(D).
}
\tag{OB.22}

For a later estimate paying one power of the pair gap, maximize

\[
{\rho\over2}\left(c_0-{\rho\over2}\right).
\]

The optimum is

\[
\boxed{\rho=c_0,}
\tag{OB.23}

where the winning mechanism still has density

\[
\boxed{{c_0\over4}=1.4125\times10^{-6}.}
\tag{OB.24}

The optimized gap-weighted product is

\[
\boxed{{c_0^2\over4},}
\tag{OB.25}

exactly twice the value from the preceding one-arc capacity theorem.

If the later estimate pays `rho^2`, the optimum is

\[
\boxed{\rho={4c_0\over3},}
\tag{OB.26}

with winning density

\[
\boxed{{c_0\over6}=9.416666\ldots\times10^{-7}.}
\tag{OB.27}

The optimized square-gap product is

\[
\boxed{{8c_0^3\over27},}
\tag{OB.28}

four times the preceding one-arc optimum.

All optimized `rho` values are many orders of magnitude below `gamma_H`, so (OB.15) is automatic for large sources.

---

## 5. Deep exact-force blocks lose only `m rho D / 2`

In a radius-`r` fully force-loaded block put

\[
m=2r+1.
\]

The existing deep-block counting loses at most `m` candidate centers for each globally narrow constituent interface. Replacing the one-arc capacity `rho D+o(D)` by (OB.19) therefore changes the neighborhood-wide narrow-pair loss from `m rho D` to

\[
{m\rho\over2}D+o(D).
\]

Thus the retained fixed-depth density sharpens to

\[
\boxed{
\Lambda_r^{ord}
={c\over2}-\eta_0-\eta_r-{m\rho\over2},
\qquad
c={113\over5{,}000{,}000},
}
\tag{OB.29}

whenever the displayed coefficient is positive.

At the schedule used by the growing diagonal, the one-arc theorem allowed

\[
\rho_n={\varepsilon_n\over4m_n}
\]

for a fixed neighborhood-wide loss. The ordered capacity permits

\[
\boxed{
\rho_n={\varepsilon_n\over2m_n}
}
\tag{OB.30}

at the same density cost. Relative to the original pre-host two-arc capacity, the resolved projective force-diamond aperture is now four times larger at fixed loss.

---

## 6. Adjacent double-force cells retain seven eighths at the existing aperture

Use the current adjacent exact-double-force density

\[
p_0={2599\over960{,}000{,}000}
\tag{OB.31}

and keep the existing aperture

\[
\rho_*={p_0\over8}.
\tag{OB.32}

The one-arc theorem bounded the number of narrow constituent interfaces by `p_0D/8+o(D)`. Equation (OB.19) halves this to

\[
{p_0\over16}D+o(D).
\]

Each narrow interface can spoil at most two adjacent double cells, so at most

\[
{p_0\over8}D+o(D)
\]

cells are lost. Therefore

\[
\boxed{
>{7p_0\over8}D-o(D)
}
\tag{OB.33}

adjacent double-force cells have both exact force pairs of projective gap at least `rho_*`. Numerically,

\[
\boxed{
{7p_0\over8}=2.36888020833\times10^{-6}.
}
\tag{OB.34}

The previous one-arc retention was `3p_0/4=2.03046875e-6` at the same aperture.

---

## 7. A TT regime has a fixed terminal span plus two C67 gaps per additional cell

The same lane-order identity gives a stronger geometric consequence for the near-full paired destination trichotomy.

Suppose `M` ordered exact-force cells lie in the **TT** regime, so both force-bar partner endpoints lie in the far terminal boundary piece `T_m`. Apply (OB.11) to these `M` selected interfaces. The last pair still has ordinary opening at least `2(gamma_H-epsilon_D)` by (OB.13). Therefore the first pair satisfies

\[
\boxed{
\Delta_1
\ge
2(\gamma_H-\varepsilon_D)
+2(M-1)\delta_D.
}
\tag{OB.35}

At a diameter partner endpoint, the outward support normal is exactly the antipode of the birth normal. Hence the two TT partner normals at the first selected cell have the same ordinary separation `Delta_1`, and both occur on `T_m`. Consequently

\[
\boxed{
\operatorname{normalspan}(T_m)
\ge
2(\gamma_H-\varepsilon_D)
+2(M-1)\delta_D.
}
\tag{OB.36}

This is stronger than direction-counting from `2M` unrelated terminal diameter bars because it retains the fixed host-margin separation inside every pair and adds the two ordered lane increments.

Type-II near-disk convergence makes radial and support-normal directions uniformly `o(1)` apart on the source hull. Thus the terminal central angular diameter satisfies

\[
\boxed{
\operatorname{angdiam}_o(T_m\cap S)
\ge
2\gamma_H+2(M-1)\delta_D-o(1).
}
\tag{OB.37}

If

\[
M>\theta D-o(D),
\]

then necessarily

\[
2\gamma_H+2\theta\le\pi
\]

and

\[
\boxed{
\liminf\operatorname{angdiam}_o(T_m\cap S)
\ge2\gamma_H+2\theta.
}
\tag{OB.38}

Radial projection to radius `D/2` gives

\[
\boxed{
\liminf {\operatorname{diam}(T_m\cap S)\over D}
\ge \sin(\gamma_H+\theta).
}
\tag{OB.39}

For the current near-full paired trichotomy, if TT is the winning regime then

\[
\theta={c\over6}={113\over30{,}000{,}000}.
\]

Using `c_H=0.453819885927...`,

\[
\boxed{
\liminf\operatorname{angdiam}_o(T_m\cap S)
\ge0.94210237937\ldots\ {m radians},
}
\tag{OB.40}

and

\[
\boxed{
\liminf {\operatorname{diam}(T_m\cap S)\over D}
\ge0.45382324237\ldots .
}
\tag{OB.41}

The previous TT direction-packing statement only recorded the tiny density-scale angular lower bound `c/3`. The host-separated paired order shows that the terminal piece is actually forced to span about `54` degrees and `45.38%` of the source diameter as soon as TT occurs at all, with a further deterministic widening proportional to the number of TT cells.

---

## 8. Frontier effect

The projectively narrow exact-force escape now has an ordered form:

```text
lower physical force lane moves toward the reaction axis;
upper physical force lane moves toward the reaction axis;
ordinary pair opening contracts by at least 2*delta_D per retained interface;
near-antipodal projective gap expands by at least 2*delta_D per interface;
therefore rho-narrow pairs occupy only a prefix of capacity (rho/2)D+o(D).
```

This removes another factor two from the narrow-pair loss and strengthens every fixed-gap deep-force extraction that was paying that loss. It also changes the TT geometry qualitatively: a terminal-terminal block is not merely a positive-density collection of terminal incidences. Its first paired cell already forces a macroscopic terminal chord, and the ordered two-lane weave widens that terminal normal span at twice the C67 rate.

C-II remains open. The new bound still leaves linear capacity because `delta_D` is only order `1/D`. The live geometric seam is the OO/mixed/TT paired destination regime inside the common dense near-equilateral grid: one must turn the ordered antipodal normal transport into an incompatibility with the train endpoint/terminal-normal ledger, or into a source-preserving strict diameter decrease.

**Disposition:** proved two-lane ordered contraction of exact-force openings, halved the one-arc narrow-pair capacity to `(rho/2)D+o(D)`, propagated the improved constants through the force/TB1 fork and deep blocks, and strengthened TT to a macroscopic terminal-span theorem with `2 delta_D` widening per cell. C-II and Level I remain open.