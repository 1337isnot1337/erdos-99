# Target C-II — optimized common-center backbone forces an adjacent cusp with at most `920` diameter rows

**Date:** 2026-09-15  
**Status:** proof-only source-level quantitative strengthening  
**Scope:** audited full-core Type-II branch with `t=(q-k)/D<=1.844`  
**Dependencies:** the audited smallest-leaf weighted center fan, exact laminar interval support, global strict-rhombus angular-defect budget, KKT interval-switch budget, Hopf--Pannwitz  
**Certificate:** `research/verify_target_c_adjacent_cut_backbone_920.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current Pareto adjacent-cut theorem reduces the finite switching set below `1800`
rows by keeping the original common-center path and changing only the final averaging
thresholds.  The original path itself is far from optimal for this purpose.

The common-center construction has two free parameters:

1. the center-degree threshold `lambda` defining the good smallest-leaf O--O trains;
2. the top center-phase fraction `r` in which the averaging center train `gamma` is
   chosen.

Retuning those parameters nearly doubles the certified path density.  The same exact
global endpoint budget

\[
\sum_i N_i\le2\pi D
\]

then implies that a positive-density set of internal path boundaries has

\[
N_i\le920.
\]

A second averaging step over only that count-good set retains both the switching KKT
mass and adjacent phase gap at `O(D^-1)` on one of the same boundaries.

## Theorem B920 — 920-row adjacent cusp

For every unbounded survivor sequence in the stated scope, all sufficiently large
members contain consecutive smallest-leaf O--O cuts

\[
\tau_i,\tau_{i+1}
\]

on one common-center complement-dual path such that

\[
\boxed{N_i\le920,}
\tag{B920.1}
\]

where `N_i` is the number of actual diameter intervals whose incidence changes between
the two cuts, and simultaneously

\[
\boxed{
B_i<Q_0D^{-1}+o(D^{-1}),
\qquad
Q_i<Q_0D^{-1}+o(D^{-1}),
}
\tag{B920.2}
\]

with the explicit safe constant

\[
Q_0=4.6\times10^{11}.
\]

Here

\[
B_i=\sum_h\beta_h
|\varepsilon_{h,i+1}-\varepsilon_{hi}|
\]

is the switching diameter KKT multiplier mass, and

\[
Q_i=q_i+q_{i+1}
\]

is the parent common-center phase-offset cost.  In particular

\[
\boxed{
 d_{\mathbb {RP}^1}(u_i,u_{i+1})
 =O(D^{-1})
}
\tag{B920.3}
\]

on the same pair.

Combined with the current switching-caterpillar theorem, the large first-order active
set on this pair is a caterpillar forest with **at most 920 edges**.

The constant in (B920.2) is intentionally enormous.  Its only purpose is to retain the
correct inverse-`D` scale while optimizing the discrete blocker count.  No downstream
argument should treat `Q_0` as numerically sharp.

---

## 1. Retune the good-leaf threshold and top phase fraction

Use the audited smallest-leaf inputs

\[
{\sum_\tau w_\tau d_\tau\over\sum_\tau w_\tau}
>0.7404-o(1),
\tag{B920.4}
\]

\[
{1\over D}\sum_\tau w_\tau>0.0848-o(1),
\tag{B920.5}
\]

and total center-train count

\[
N_C<1.063D+o(D).
\tag{B920.6}
\]

Choose the exact rational parameters

\[
\boxed{
\lambda={64033\over100000}=0.64033,
\qquad
r={60237\over100000}=0.60237.
}
\tag{B920.7}
\]

Call a smallest-leaf O--O train good when its center degree exceeds `lambda D`.
Weighted thresholding gives retained good weight, and therefore also distinct good
train count density, at least

\[
\begin{aligned}
g
&={ (0.7404-\lambda)(0.0848)\over1.063-\lambda}\\
&={530371\over26416875}\\
&=0.0200769773109\ldots .
\end{aligned}
\tag{B920.8}
\]

This is substantially larger than the `0.013928...` good density in the original
triple-small parameter choice.

---

## 2. One top-phase center train crosses a `0.006824D` good-leaf path

Order the actual center trains by their real phase representatives and let `H` be the
top `r` fraction.  A good leaf has at least

\[
\begin{aligned}
d_{top}D-o(D)
&:=\left[\lambda-(1-r)(1.063)\right]D-o(D)\\
&={21764931\over100000000}D-o(D)\\
&=0.21764931D-o(D)
\end{aligned}
\tag{B920.9}
\]

neighbors in `H`.

Averaging the good-leaf/`H` incidences over at most `r(1.063)D+o(D)` center trains
therefore gives one center train `gamma in H` crossing more than

\[
\begin{aligned}
pD-o(D)
&:={d_{top}g\over r(1.063)}D-o(D)\\
&={3847829406467\over563841172411875}D-o(D)\\
&=0.00682431435435\ldots D-o(D)
\end{aligned}
\tag{B920.10}
\]

distinct good smallest-leaf O--O trains.

Because good leaves are pairwise noncrossing and one train crosses them all, those
leaves form one simple path in the complement dual.  Write it

\[
P=(\tau_1,\ldots,\tau_m),
\qquad
m>pD-o(D).
\tag{B920.11}
\]

This path is about `1.915` times as dense as the `0.003564...D` path used by the
original triple-small theorem.

---

## 3. The phase-offset budget remains finite

The aggressive choice of `r` leaves only a small lower-phase neighbor margin, but it
is strictly positive:

\[
\begin{aligned}
d_{low}
&:=\lambda-r(1.063)\\
&={1069\over100000000}\\
&=0.00001069.
\end{aligned}
\tag{B920.12}
\]

For every path leaf `tau_j`, let

\[
q_j=\beta_j-\alpha_\gamma-\pi/3>0
\]

be the same common-center phase offset used in the audited triple-small proof.
Every good leaf has at least

\[
d_{low}D-o(D)
\]

center neighbors with real phase at most `alpha_gamma`.  Each corresponding strict
rhombus spends angular defect at least `q_j`.  Since different leaf/center crossings
are different rhombi and the global defect budget is

\[
\sum_R\delta_R<C_{phase}D,
\]

we retain the exact parent argument

\[
\boxed{
\sum_{j=1}^m q_j
\le {C_{phase}\over d_{low}}+o(1).
}
\tag{B920.13}
\]

Hence for

\[
Q_i:=q_i+q_{i+1}
\]

we have

\[
\boxed{
\sum_{i=1}^{m-1}DQ_i
\le {2C_{phase}\over d_{low}}D+o(D).
}
\tag{B920.14}
\]

Although the coefficient is large, the total path phase variation is still `O(1)` and
the average adjacent phase gap is still `O(D^-1)`.

---

## 4. More path boundaries than `N_i>=921` boundaries

For an internal path boundary, let

\[
N_i=\#\{h:\varepsilon_{h,i+1}\ne\varepsilon_{hi}\}.
\]

Every actual diameter interval starts or stops at most twice, so the audited endpoint
budget is

\[
\sum_iN_i\le2h\le2\pi D.
\tag{B920.15}
\]

Call a boundary **count-bad** when

\[
N_i\ge921.
\]

Using the outward bound `pi<355/113`, the density of count-bad boundaries is at most

\[
{2(355/113)\over921}
=0.00682213446\ldots .
\tag{B920.16}
\]

By contrast, the path density in (B920.10) is

\[
p=0.00682431435\ldots .
\]

The exact difference is

\[
\boxed{
\rho
:=p-{2(355/113)\over921}
={42639135602947\over19560214112140355625}
>2\times10^{-6}.
}
\tag{B920.17}
\]

Therefore, for all sufficiently large members of the survivor sequence, at least

\[
\rho D-o(D)
\]

internal path boundaries are count-good.  Since `N_i` is an integer, every such
boundary satisfies

\[
\boxed{N_i\le920.}
\]

This is the discrete improvement that the original final-stage Pareto optimization
cannot reach without first increasing the path density.

---

## 5. Retain small KKT switching mass and phase gap on the same count-good boundary

The exact interval/KKT budget gives

\[
\sum_iB_i\le2,
\qquad
B_i=\sum_h\beta_h
|\varepsilon_{h,i+1}-\varepsilon_{hi}|.
\tag{B920.18}
\]

Multiplying by `D` and adding (B920.14),

\[
\sum_i D(B_i+Q_i)
\le
\left(2+{2C_{phase}\over d_{low}}\right)D+o(D).
\tag{B920.19}
\]

Restrict this nonnegative sum to the positive-density set of count-good boundaries.
At least one such boundary obeys

\[
D(B_i+Q_i)
\le
{2+2C_{phase}/d_{low}\over\rho}+o(1).
\tag{B920.20}
\]

Using the standard outward rational enclosure

\[
C_{phase}
<{3258689123681\over612912000000},
\]

the exact companion verifier proves

\[
{2+2C_{phase}^{up}/d_{low}\over\rho}
<4.6\times10^{11}.
\tag{B920.21}
\]

Both summands are nonnegative, so the selected count-good boundary satisfies
(B920.2).  The parent phase identity gives

\[
d_{\mathbb {RP}^1}(u_i,u_{i+1})
\le Q_i,
\]

and therefore (B920.3).

---

## 6. Interaction with the exact finite-cusp and switching-forest theorems

On the selected adjacent pair:

1. exact laminar interval support is available;
2. the opposite two-cut finite multishear is available;
3. at most `920` actual diameter rows switch incidence;
4. their total positive KKT multiplier is `O(D^-1)`;
5. the two leaf directions have projective gap `O(D^-1)`; and
6. the current switching-graph theorem identifies those switching rows as the edge set
   of one caterpillar forest `delta_H(L)`.

Thus the current source-level blocker has been reduced from

```text
<21200 arbitrary-looking switching rows
```

to

```text
<=920 switching diameter edges
forming one layer-cut caterpillar forest
with beta mass O(1/D)
and adjacent phase gap O(1/D).
```

The next exchange theorem can sharpen this further by eliminating every non-switching
active diameter row **exactly** at a discrete adjacent train-vector transposition.

---

## 7. Scope audit

- The proof changes the good-leaf threshold and top-phase fraction before choosing the
  center train.  It is not merely a looser restatement of the `<1800` result.
- The tiny value of `d_low` is harmless asymptotically because it is a fixed positive
  rational.  It only makes the explicit `O(D^-1)` phase constant large.
- No KKT coefficient lower bound is used.
- No claim is made that `920` is the final optimal constant.  It is close to the limit
  of this particular path/count-budget architecture: the present parameters give
  `2*pi/p about 920.7`.
- The theorem does not itself solve the finite max-function cusp.

**Disposition:** proved proof-only optimized-backbone strengthening. C-II and Level I
remain open.
