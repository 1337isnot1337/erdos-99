# Target C-II — a linear THIN upper family forces a phase-pure blocker-rich common cut

**Date:** 2026-09-17  
**Status:** proof-only continuation of the Horn upper-obstruction analysis; no canonical promotion claimed  
**Scope:** the THIN side of the 15-spaced one-sign strong-TB1 Horn upper family through `t=(q-k)/D<=1.8687`  
**Dependencies:** Horn owned-upper extraction; exact path-region interval support; superdiameter geometric-thrackle theorem; 15-spacing of retained owners; global strict-rhombus angular-defect budget; high-`t` crossing-neighbor floor; exact train-step metric/circumdisk flank argument  
**Certificate:** `research/verify_target_c_high_t_tb1_thin_rich_cut_phase_sync_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The previous upper-localization theorem treated SIGNED and THIN upper blockers uniformly and obtained only `D/log D` blockers in one low-defect row/window. The THIN geometry is stronger: every THIN blocker has length greater than `sqrt(D^2-1)`, so the entire THIN graph is a straight-line geometric thrackle.

Using the exact path-region interval of every blocker and the fact that the retained owner coordinates are fifteen-spaced, this thrackle structure forces not merely one common cut for a matching, but a **linear set of blocker-rich cuts for the full owned THIN family**. The global `O(D)` angular-defect budget then makes one of those cuts have `O(1)` total phase defect. Consequently that same row carries a linear THIN blocker population and an almost-full inverse-`D` near-equilateral transverse train family.

Write

\[
s_0={791\over320\,000\,000},
\qquad
\gamma={s_0\over30}={791\over9\,600\,000\,000}.
\]

The Horn upper extraction gives an owned family `E_D` of distinct upper blockers with

\[
|E_D|>\left({\gamma\over8}-o(1)\right)D,
\]

and distinct fifteen-spaced owner coordinates. Split globally into SIGNED and THIN. If THIN wins, let `T_D` be that family. Then

\[
\boxed{
N_D:=|T_D|>
\left({\gamma\over16}-o(1)\right)D
=
\left(5.14973958333\ldots\times10^{-9}-o(1)\right)D.
}
\tag{TR.1}
\]

Every `e in T_D` satisfies

\[
D-|e|<{1\over4D},
\qquad
|e|>\sqrt{D^2-1},
\tag{TR.2}
\]

so every endpoint is a convex-hull vertex and any two THIN segments meet, either at a common source endpoint or in one proper crossing.

The main conclusion is:

> **THIN rich-cut theorem.** The family `T_D` determines more than
> \[
> \left({3\gamma\over16}-o(1)\right)D
> =
> \left(1.544921875\times10^{-8}-o(1)\right)D
> \]
> distinct selected O--O cuts, each supported by more than
> \[
> \left({\gamma\over80}-o(1)\right)D
> =
> \left(1.02994791667\times10^{-9}-o(1)\right)D
> \]
> THIN blockers.
>
> Among these cuts there is one row `tau_*` whose full angular-defect sum is bounded by a source-independent constant. After deleting only `0.01D` transverse columns, `tau_*` retains more than
> \[
> (0.6436-o(1))D
> \]
> complete trains, every one crossing `tau_*` at angle
> \[
> {\pi\over3}+O(D^{-1}),
> \]
> while the row still supports more than `(gamma/80-o(1))D` THIN blocker chords. The same retained column family contains the standard `+-0.01D` circumcenter flanks, each of density
> \[
> 0.0547027254265\ldots-o(1).
> \]

Thus the THIN Horn upper branch is no longer a `D/log D` localization problem. It contains a **linear blocker population on one inverse-`D` phase-pure dense row**.

---

## 1. Closed endpoint-region intervals of all THIN blockers intersect pairwise

Write the selected path as

\[
R_0-\tau_1-R_1-\tau_2-\cdots-\tau_m-R_m.
\tag{TR.3}
\]

For a blocker `e=xy` with endpoint regions `R_a,R_b`, `a<b`, define its closed endpoint-region interval

\[
J(e):=[a,b]\cap\mathbb Z
\tag{TR.4}
\]

and its exact selected-cut support

\[
I(e)=\{a+1,\ldots,b\}.
\tag{TR.5}
\]

Take two THIN blockers `e,f`.

By (TR.2) and the superdiameter-thrackle theorem, their straight segments meet. If they share a source endpoint, that endpoint belongs to one path region contained in both `J(e)` and `J(f)`, so the closed region intervals intersect.

Otherwise the two chords cross properly. If `J(e)` and `J(f)` were disjoint, one selected O--O crosscut would separate both endpoints of `e` from both endpoints of `f`. All four endpoints are hull vertices. The two endpoints of one chord would then lie on one complementary boundary shore of that crosscut and both endpoints of the other chord on the other shore, so the four hull endpoints could not alternate. Two straight hull chords with nonalternating endpoints do not cross. Contradiction.

Therefore

\[
\boxed{
J(e)\cap J(f)\ne\varnothing
\quad(e,f\in T_D).
}
\tag{TR.6}
\]

Intervals on a line have Helly number two. Hence the whole family has one common closed region interval

\[
\boxed{
[A_D,B_D]\cap\mathbb Z
\subseteq J(e)
\quad\text{for every }e\in T_D,
}
\tag{TR.7}
\]

where

\[
A_D:=\max_e \min J(e),
\qquad
B_D:=\min_e \max J(e),
\qquad
A_D\le B_D.
\]

Put

\[
w_D:=B_D-A_D.
\tag{TR.8}
\]

Every cut

\[
\tau_k,
\qquad
A_D<k\le B_D,
\tag{TR.9}
\]

is supported by **every** THIN blocker.

The point of the next section is that even when `w_D` is small, the fifteen-spaced owner coordinates force many nearby cuts to carry a fixed fraction of the full THIN family.

---

## 2. Fifteen-spaced owners force `3N-o(N)` rich cuts

Every blocker in `T_D` has one assigned owner coordinate which is one endpoint region of the blocker, and distinct blockers have distinct owners. All owners belong to the retained Horn set and are pairwise at least fifteen region indices apart.

Write

\[
N=N_D.
\]

We prove that there are

\[
\boxed{(3-o(1))N}
\tag{TR.10}
\]

distinct selected cuts each supported by at least

\[
\boxed{\left({1\over5}-o(1)\right)N}
\tag{TR.11}
\]

THIN blockers.

### Case 1: the common overlap is long

If

\[
w_D\ge3N,
\tag{TR.12}
\]

then the common interval (TR.7) itself contains at least `3N` selected cuts. By (TR.9), all `N` blockers support each of them. Equations (TR.10)--(TR.11) are immediate.

### Case 2: the common overlap is short

Assume

\[
w_D<3N.
\tag{TR.13}
\]

Because owner coordinates are fifteen-spaced, the number of owners lying inside `[A_D,B_D]` is at most

\[
{w_D\over15}+1
< {N\over5}+1.
\tag{TR.14}
\]

Hence more than

\[
{4N\over5}-1
\tag{TR.15}
\]

owners lie strictly to the left of `A_D` or strictly to the right of `B_D`. One side contains at least

\[
M\ge {2N\over5}-O(1)
\tag{TR.16}
\]

owners.

Assume it is the left side; the right side is symmetric. Order these owners from nearest to farthest from `A_D`:

\[
x_1>x_2>\cdots>x_M,
\qquad
x_s<A_D.
\tag{TR.17}
\]

Fifteen-spacing gives

\[
x_s\le A_D-1-15(s-1).
\tag{TR.18}
\]

Choose

\[
s_0=\left\lfloor{M\over2}\right\rfloor+1.
\]

Every blocker whose owner is one of

\[
x_{s_0},x_{s_0+1},\ldots,x_M
\]

has its other endpoint region at least `A_D`, because its closed interval contains `[A_D,B_D]`. Therefore every such blocker supports every cut

\[
\tau_k,
\qquad
x_{s_0}<k\le A_D.
\tag{TR.19}
\]

The number of retained blockers is at least

\[
M-s_0+1
\ge {M\over2}-O(1)
\ge {N\over5}-O(1),
\tag{TR.20}
\]

while the number of cuts in (TR.19) is at least

\[
A_D-x_{s_0}
\ge1+15\left\lfloor{M\over2}\right\rfloor
\ge3N-O(1).
\tag{TR.21}
\]

This proves (TR.10)--(TR.11) in the short-overlap case as well.

Combining the two cases, the number `Q_D` of blocker-rich selected cuts satisfies

\[
\boxed{
Q_D>
\left({3\gamma\over16}-o(1)\right)D
=
\left(1.544921875\times10^{-8}-o(1)\right)D,
}
\tag{TR.22}
\]

and every one supports more than

\[
\boxed{
\left({\gamma\over80}-o(1)\right)D
=
\left(1.02994791667\times10^{-9}-o(1)\right)D
}
\tag{TR.23}
\]

distinct THIN blockers.

No matching extraction or degree bound is used here.

---

## 3. One rich cut has `O(1)` total angular defect

For a selected row `tau_j`, let

\[
F_j:=\sum_{b\in\Gamma_j}\delta_{jb}
\tag{TR.24}
\]

be the full strict-rhombus angular-defect sum over all complete trains crossing that row.

The canonical global defect budget gives

\[
\sum_j F_j\le C_{\rm phase}D,
\qquad
C_{\rm phase}
={\pi^2\sqrt3(2+\sqrt3)\over12}.
\tag{TR.25}
\]

The `Q_D` rich cuts from (TR.22) are distinct, so one of them, say `tau_*`, satisfies

\[
F_*
\le {C_{\rm phase}D\over Q_D}
\le
{16C_{\rm phase}\over3\gamma}+o(1).
\tag{TR.26}
\]

Define

\[
\boxed{
H_{\rm thin}:={16C_{\rm phase}\over3\gamma}
=344128111.925\ldots .}
\tag{TR.27}
\]

Then

\[
\boxed{F_*\le H_{\rm thin}+o(1).}
\tag{TR.28}
\]

At the same time, by construction `tau_*` is supported by more than `(gamma/80-o(1))D` THIN blockers.

This is stronger than the previous upper-localization result on the THIN side: the blocker population on the selected row is linear in `D`, while the row's **total** phase defect is bounded independently of `D`.

---

## 4. Phase-purify the same blocker-rich row

Every selected high-`t` row satisfies

\[
|\Gamma_*|>(0.6536-o(1))D.
\tag{TR.29}
\]

Fix

\[
\sigma=0.01.
\]

Delete every crossing train `b` whose defect satisfies

\[
\delta_{*b}>{H_{\rm thin}+1\over\sigma D}.
\tag{TR.30}
\]

For all sufficiently large `D`, (TR.28) and Markov imply that fewer than `sigma D` columns are deleted. Therefore the retained family `P_*` satisfies

\[
\boxed{|P_*|>(0.6436-o(1))D.}
\tag{TR.31}
\]

Every retained row-column rhombus has

\[
\boxed{
0<\delta_{*b}
\le {K_{\rm thin}\over D}+o(D^{-1}),
\qquad
K_{\rm thin}:={H_{\rm thin}\over0.01}
=3.44128111925\ldots\times10^{10}.
}
\tag{TR.32}
\]

Thus the blocker-rich row is inverse-`D` near-equilateral across almost its full crossing population.

The exact train-step metric and source circumdisk capacity now apply to this same ordered family. With

\[
\mu=0.01,
\]

the retained common row flanks each have density

\[
\boxed{
0.6436-{1.02\over\sqrt3}
=0.0547027254265\ldots .}
\tag{TR.33}
\]

Hence the same row simultaneously carries

```text
> (gamma/80-o(1)) D THIN superdiameter blockers;
> (0.6436-o(1)) D transverse columns with O(1/D) angular defect;
> (0.0547027-o(1)) D retained columns below the -0.01D circumcenter level;
> (0.0547027-o(1)) D retained columns above the +0.01D circumcenter level.
```

Every THIN blocker in the selected subfamily has endpoints on opposite shores of `tau_*`, length greater than `sqrt(D^2-1)`, hull endpoints, and the original distinct retained owner tag.

---

## 5. Consequence for the Horn upper frontier

The non-LOWER Horn upper obstruction now has a sharper metric split.

If the global THIN class wins, then the preceding theorem produces **linear** blocker multiplicity on one row with bounded total phase defect and an inverse-`D` dense train scaffold.

If the global SIGNED class wins, the previous upper-localization theorem still gives a `D/log D` same-type population in one low-defect common cut or one `o(D)`-width low-defect window, with every blocker carrying a fixed macroscopic negative projection on the common TB1 axis.

So the `D/log D` loss is no longer intrinsic to the THIN side. The remaining THIN task is now entirely geometric on one row: exploit a linear geometric-thrackle family of inactive superdiameter chords whose endpoints straddle one inverse-`D` near-equilateral dense train ladder with fixed circumcenter flanks.

No THIN blocker is promoted to an actual diameter edge or assigned KKT mass.

**Disposition:** upgraded the THIN Horn upper branch from `D/log D` low-defect localization to a linear blocker-rich common cut with `O(1)` total phase defect and an almost-full inverse-`D` dense train scaffold. C-II and Level I remain open.