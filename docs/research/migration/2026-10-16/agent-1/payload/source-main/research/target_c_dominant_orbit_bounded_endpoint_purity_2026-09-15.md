# Target C-II — near the joint-orbit floor almost every bounded terminal lies in one atomic orbit

**Date:** 2026-09-15  
**Repository base:** `dc0b174fb5d4e8865c998201a980c7ccb68acf23` plus the safe `1.82516` promotion on this branch  
**Status:** proof-only structural strengthening; theorem-state authority unchanged  
**Scope:** fully force-visible no-container/full-core Type-II branch  
**LEVEL I STATUS:** `STILL OPEN`

The merged joint orbit theorem uses one dominant exact projective `pi/3` train orbit to force outer directional energy.  The same inequalities also control the *complement* of that orbit on bounded exceptional faces.

Let

\[
t={q-k\over D},\qquad
\kappa={k\over D},\qquad
\delta={d_{out}\over D},
\]

and let

\[
C={T-q/2\over D}.
\]

Use the hostile-audited atomic gap

\[
C\ge C_0:=2\sqrt{\Delta_2}+0.0050,
\qquad
\Delta_2={\pi\over2\sqrt3}.
\]

Write

\[
U={9t\over2}-2\pi-2\delta-\kappa/2,
\]

so `C<=U` and

\[
2\delta+\kappa/2\le R(t):={9t\over2}-2\pi-C_0.
\]

Fix the dominant atomic orbit from the Section-168 decomposition.  Along the standard shrinking-window diagonal subsequence let

- `M D+o(D)` be the number of trains in those orbit windows;
- `K D+o(D)` be their outer terminal occurrences;
- `B_nd D+o(D)` be the bounded-face terminal occurrences carried by trains outside those windows.

Then for every survivor with `t<=1.826`,

\[
\boxed{B_{nd}\le0.07561.}
\]

More sharply, at fixed `t` in the interval from the current floor through `1.826`,

\[
\boxed{
B_{nd}
\le
\Psi\!\left({R(t)\over2}\right)-K_0(t),
}
\tag{BP.1}
\]

where

\[
\Phi(z)=z-6\arcsin(\tanh(z/6)),
\qquad
\Psi=\Phi^{-1},
\]

and

\[
K_0(t)=
\pi+{R(t)\over2}-t-2C_0+{8\Delta_2\over C_0}.
\tag{BP.2}
\]

At the scalar root of the joint-orbit theorem the right side of (BP.1) is exactly zero.  Thus bounded terminal purity is not an independent heuristic: it is the stability form of the same scalar equality case.

## 1. Exact bounded-terminal decomposition

The total bounded-face terminal occurrence count is

\[
B=2T-b.
\]

Since

\[
{T\over D}=C+{t+\kappa\over2}+o(1),
\qquad
{b\over D}=\pi+\delta+o(1),
\]

we have

\[
{B\over D}=2C+t+\kappa-\pi-\delta+o(1).
\tag{BP.3}
\]

Every train has exactly two terminal incidences.  Hence the dominant-orbit trains contribute

\[
2M-K
\]

bounded terminal incidences per unit diameter, and therefore

\[
B_{nd}
=2C+t+\kappa-\pi-\delta-2M+K.
\tag{BP.4}
\]

## 2. Lower dominant mass and upper outer mass

The exact atomic-orbit crossing decomposition gives

\[
M\ge{4\Delta_2\over C}.
\tag{BP.5}
\]

The joint route-capacity/phase-energy theorem is first proved for the *actual* dominant-orbit outer mass `K`, before replacing it by its lower bound.  Its exact dual therefore gives

\[
\delta\ge\Phi(K).
\tag{BP.6}
\]

On the present interval `K<3 log 3`, `Phi` is strictly increasing, so

\[
K\le\Psi(\delta).
\tag{BP.7}
\]

Substitute (BP.5)--(BP.7) into (BP.4):

\[
B_{nd}
\le
2C+t+\kappa-\pi-\delta
-{8\Delta_2\over C}
+\Psi(\delta).
\tag{BP.8}
\]

The right side is strictly increasing in `C`, because

\[
{d\over dC}\left(2C-{8\Delta_2\over C}\right)
=2+{8\Delta_2\over C^2}>0.
\]

Thus `C<=U` gives

\[
B_{nd}
\le
2U+t+\kappa-\pi-\delta
-{8\Delta_2\over U}
+\Psi(\delta).
\tag{BP.9}
\]

## 3. The worst topology defect is `kappa=0`

Put

\[
A(t)={9t\over2}-2\pi,
\qquad
U=A(t)-2\delta-\kappa/2.
\]

The affine terms in (BP.9) simplify:

\[
2U+t+\kappa-\pi-\delta
=10t-5\pi-5\delta.
\]

Hence

\[
B_{nd}
\le
10t-5\pi-5\delta
-{8\Delta_2\over U}
+\Psi(\delta).
\tag{BP.10}
\]

For fixed `t,delta`, the only remaining `kappa` dependence is through `U`.  Increasing `kappa` decreases `U`, which makes `-8Delta_2/U` smaller.  Therefore the right side is maximized at

\[
\boxed{\kappa=0.}
\tag{BP.11}
\]

Then

\[
U=A(t)-2\delta.
\]

## 4. The bound increases with detour on `t<=1.826`

Define

\[
N_t(\delta)=
10t-5\pi-5\delta
-{8\Delta_2\over A(t)-2\delta}
+\Psi(\delta).
\tag{BP.12}
\]

The feasible interval has

\[
0\le\delta\le R(t)/2,
\qquad
A(t)-2\delta\ge C_0.
\]

Differentiating,

\[
N_t'(\delta)
=-5-{16\Delta_2\over U^2}+\Psi'(\delta).
\tag{BP.13}
\]

Since

\[
\Phi'(z)=1-\operatorname{sech}(z/6),
\qquad
\Psi'(\delta)={1\over\Phi'(\Psi(\delta))},
\]

and, throughout `t<=1.826`,

\[
\delta\le0.012095,
\qquad
\Psi(\delta)<1.384,
\]

we have

\[
\Psi'(\delta)>38.4.
\]

Meanwhile

\[
5+{16\Delta_2\over U^2}
\le
5+{16\Delta_2\over C_0^2}
<8.98.
\]

Thus

\[
\boxed{N_t'(\delta)>29.4>0.}
\tag{BP.14}
\]

The worst point is therefore maximal detour:

\[
\delta=R(t)/2,
\qquad U=C_0.
\]

At that point (BP.10) simplifies exactly to (BP.1).

## 5. Numerical stability window

The independent verifier gives

\[
\Psi(R(1.826)/2)=1.3833159431\ldots,
\]

\[
K_0(1.826)=1.3077133762\ldots,
\]

hence

\[
\boxed{
B_{nd}\le0.0756025669\ldots<0.07561
}
\tag{BP.15}
\]

for every survivor with `t<=1.826`.

Closer to the scalar floor the collapse is much stronger:

\[
t\le1.8255
\Longrightarrow
B_{nd}<0.03157,
\]

\[
t\le1.8253
\Longrightarrow
B_{nd}<0.01311.
\]

At the exact scalar root \(t_*=1.82516142463113334\ldots\), the joint-orbit equality relation gives

\[
\Psi(R(t_*)/2)=K_0(t_*),
\]

so the limiting upper bound is zero.

## 6. Consequence for the pentagon sea

The low-`t` pentagon ledger is symbolic in the same atomic floor.  With `g=0.0050`,

\[
{p_5\over D}
\ge
\pi+C_0-{5t\over2}+\delta+{\kappa\over2}-o(1).
\tag{BP.16}
\]

For `t<=1.826`, dropping the nonnegative last two terms gives

\[
{p_5\over D}
\ge0.4862182673\ldots-o(1).
\tag{BP.17}
\]

Call a pentagon **orbit-pure** if all five of its bounded terminal occurrences belong to the dominant shrinking phase windows.  Every impure pentagon consumes at least one non-dominant bounded terminal occurrence, and one terminal occurrence belongs to only one bounded face.  Therefore

\[
P_{5,pure}\ge p_5-B_{nd}D-o(D).
\]

Using (BP.15)--(BP.17),

\[
\boxed{
{P_{5,pure}\over D}
\ge0.4106157004\ldots-o(1).
}
\tag{BP.18}

In particular, throughout the entire narrow band from the current floor through `1.826`, the source contains more than `0.4106D-o(D)` pentagons whose five boundary side trains all lie in one common shrinking triangular phase orbit.

This conclusion does not use small face residual, empty-face assumptions, or a KKT coefficient floor.

**Disposition:** proof-only structural strengthening. C-II and Level I remain open.
