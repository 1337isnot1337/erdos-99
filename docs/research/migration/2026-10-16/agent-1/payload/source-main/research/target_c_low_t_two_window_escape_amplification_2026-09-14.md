# Erdos Problem #99 - low-`t` amplification of global two-window escape

**Date:** 2026-09-14
**Target:** C-II, canonical full-core Type-II branch
**Dependencies:** global pentagon two-window escape; exact stopped-train and outer-walk ledgers; AG42 all-train floor
**Claim class:** proof-only structural consequence; theorem-state authority unchanged

## LEVEL I STATUS

`STILL OPEN`

For every pair of projective direction windows of radius
`epsilon < 2 asin(1/10)`, the global pentagon two-window theorem gives

\[
Q-f+2T_{off}\ge f.
\tag{LT.1}
\]

Write

\[
C_D:=T-{q\over2},\qquad t_D:={q-k\over D},
\qquad \delta_D:={b-P_F\over D},\qquad \kappa_D:={k\over D}.
\]

The exact stopped-train and outer-walk identities upgrade (LT.1) to the finite inequality

\[
\boxed{
2T_{off}\ge
C_D+P_F+(b-P_F)+{k\over2}-{5\over2}(q-k).
}
\tag{LT.2}
\]

Consequently every Type-II subsequence with `limsup t_D <= t_0` satisfies

\[
\boxed{
\liminf {T_{off}\over D}
\ge g_2(t_0):={c_*\over2}+{\pi\over2}-{5t_0\over4},
\qquad
c_*:=2\sqrt{\Delta_2}+0.00042,
\quad \Delta_2={\pi\over2\sqrt3}.
}
\tag{LT.3}
\]

for **every** chosen pair of narrow projective windows. The omitted terms
`delta_D/2+kappa_D/4` are nonnegative.

At the current AG42/Section-171 floor

\[
t_{42}={4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0013751
=1.82088863797944\ldots,
\]

this gives

\[
\boxed{
\liminf {T_{off}\over D}
\ge0.247208336184549\ldots .
}
\tag{LT.4}
\]

Even throughout the older endpoint/common-cap window `t<=1.8585`,

\[
\boxed{
\liminf {T_{off}\over D}
\ge0.200194133658854\ldots .
}
\tag{LT.5}
\]

The lower bound stays positive for

\[
t<{2\over5}(c_*+\pi)=2.01865530692708\ldots .
\tag{LT.6}
\]

Thus a survivor near the current `q-k` floor cannot hide its exceptional-face population in an almost two-directional train system: every window pair misses almost a quarter of `D` complete stopped trains.

## 1. Exact finite derivation

Put `X=Q-f`. Equation (LT.1) gives

\[
2T_{off}\ge2f-Q.
\tag{LT.7}
\]

The complete stopped-train count is exactly

\[
T=q-k+2f.
\tag{LT.8}
\]

Therefore

\[
C_D=T-{q\over2}
={q-k\over2}+2f-{k\over2},
\]

so

\[
2f=C_D-{q-k\over2}+{k\over2}.
\tag{LT.9}
\]

The occurrence-counted outer-walk identity is

\[
b+Q=2(q-k),
\]

hence

\[
Q=2(q-k)-b.
\tag{LT.10}
\]

Substitute (LT.9)--(LT.10) into (LT.7):

\[
2T_{off}\ge C_D+b+{k\over2}-{5\over2}(q-k).
\]

Splitting `b=P_F+(b-P_F)` proves (LT.2). No asymptotic estimate is used.

## 2. Type-II normalization

Divide (LT.2) by `2D`:

\[
{T_{off}\over D}
\ge {C_D\over2D}+{P_F\over2D}
+{\delta_D\over2}+{\kappa_D\over4}-{5\over4}t_D.
\tag{LT.11}
\]

Canonical full-core Type II gives `P_F/D -> pi`, while AG42 gives

\[
\liminf {C_D\over D}\ge c_*.
\tag{LT.12}
\]

Since `delta_D,kappa_D>=0`, (LT.3) follows. The important new feature is the linear dependence on `t_D`; the earlier uniform `f_*/2` escape discarded it.

## 3. Equivalent inverse form

Rearranging (LT.2) gives

\[
\boxed{
{q-k\over D}
\ge {2\over5}{C_D\over D}
+{2\over5}{P_F\over D}
+{2\over5}\delta_D+{1\over5}\kappa_D
-{4\over5}{T_{off}\over D}.
}
\tag{LT.13}
\]

Thus any independent theorem placing all but `alpha D` stopped trains in two narrow windows would imply

\[
\liminf {q-k\over D}
\ge {2\over5}(c_*+\pi)-{4\over5}\alpha.
\tag{LT.14}
\]

Conversely, near `t_42`, (LT.4) proves that no two-window localization with `alpha<0.2472...` can coexist with the current pentagon/face ledger.

## 4. Interaction with the current small-residual endpoint

The concurrent flat-pentagon chain extraction proves that on `R_F=o(D)`, low degree excess produces linearly many vertex-disjoint positive-core paths `l-m-r` with two exact unit contacts and turning angle tending to zero. The present theorem is orthogonal: it does not assume `R_F=o(D)` and forces a macroscopic third-direction population whenever `t_D` is low.

Hence the hard low-`t`, low-residual corner now simultaneously contains

```text
Omega(D) near-straight positive-core two-contact chains,
and
at least 0.2472 D off-any-two-window trains near t_42.
```

This is a more rigid three-phase deformation target than either theorem alone. It does not yet turn a hidden diagonal into an exact unit contact or construct a strict sub-`D` source.

## 5. Scope audit

- `T_off` counts complete stopped trains, with the terminal-incidence factor inherited exactly from the global pentagon theorem.
- `C_D=T-q/2` is the all-stopped-train surplus, including singleton trains.
- `b` is the canonical occurrence-counted old outer contact walk.
- `P_F` is Euclidean force-hull perimeter and `b-P_F>=0`.
- `k=d_H+s_Z>=0` is retained in the finite theorem and dropped only for the conservative asymptotic constant.
- AG42 remains proof-only, so the numerical consequences inherit that lifecycle.
- No exact triangle, source-preserving strict competitor, or C-II closure is claimed.

**Disposition:** new proof-only exact composition and low-`t` structural theorem.
C-II and Level I remain open.
