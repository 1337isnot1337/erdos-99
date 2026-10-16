# Target C-II — summing the three orbit cusp costs

**Date:** 2026-09-14  
**Repository base:** `815c8b6ce3c4d8ce1b5c256f384e85811e25f995`  
**Status:** proved proof-only strengthening of audited §§166/171 in the small-detour regime; theorem-state authority unchanged  
**LEVEL I STATUS:** `STILL OPEN`

Audited §171 converts a heavy three-direction `pi/3` train orbit into outer-walk detour
by first pigeonholing one of its at most three outer atoms.  That step loses a factor
of three in the cubic cusp payment and produces the coefficient `81` in §171.14.

When the normalized outer detour is small, the three cusp neighborhoods are forced to
be disjoint.  Their costs can then be summed directly.  The coefficient improves from
`81` to `27`.

Use the audited §166 notation.  The limiting occurrence-counted outer direction
measure `nu` has total mass

\[
M=\pi+\delta,
\]

where

\[
\delta=\lim {b-\operatorname{per}(F)\over D}\ge0.
\]

Let

\[
F(\alpha)=\int|\cos(\theta-\alpha)|\,d\nu(\theta),
\qquad
h=F-2\ge0.
\]

Audited §166 gives

\[
\int_0^\pi h(\alpha)\,d\alpha=2\delta
\tag{CS.1}
\]

and, distributionally,

\[
h''\ge-M.
\tag{CS.2}
\]

An atom of `nu` of mass `w` produces a derivative jump `2w` in `h` at the shifted
location.

## 1. One-sided parabolic cusp interval

At an atom location `alpha_0`, the derivative jump satisfies

\[
h'_+(\alpha_0)-h'_-(\alpha_0)=2w.
\]

Hence at least one of

\[
h'_+(\alpha_0)\ge w,
\qquad
h'_-(\alpha_0)\le-w
\]

holds.  Choose the corresponding outward side.  From (CS.2) and `h(alpha_0)>=0`,

\[
\boxed{
h(\alpha_0+\varepsilon t)
\ge wt-{M\over2}t^2
\qquad
0\le t\le {2w\over M},
}
\tag{CS.3}
\]

for one sign `epsilon in {+1,-1}`.  Integrating the positive parabola gives

\[
\boxed{
\int_{I(w)}h
\ge {2w^3\over3M^2},
}
\tag{CS.4}
\]

where `I(w)` is a one-sided projective interval of length `2w/M` beginning at the
shifted atom.

This is exactly the local estimate inside the audited proof of §166.7; the only new
step below is to retain all three intervals instead of one.

## 2. Small detour makes a `pi/3` orbit disjoint

The audited single-atom cusp bound is

\[
\delta\ge {w^3\over3M^2}.
\]

Therefore every outer atom obeys

\[
{w\over M}
\le r_\delta:=\left({3\delta\over M}\right)^{1/3}.
\tag{CS.5}
\]

Consider the three projective directions in one orbit of

\[
\phi\mapsto\phi+\pi/3\pmod\pi.
\]

After the common `pi/2` shift used in the cusp equation, their locations remain
pairwise separated by `pi/3` on the projective circle.

Assume

\[
\boxed{
r_\delta\le\pi/12.}
\tag{CS.6}
\]

Equivalently,

\[
\boxed{
{\delta\over M}\le {\pi^3\over5184}.
}
\tag{CS.7}
\]

Then every interval `I(w)` from (CS.4) has length

\[
{2w\over M}\le {\pi\over6}.
\]

Three arbitrary one-sided intervals of length at most `pi/6` launched from three
points spaced by `pi/3` have pairwise disjoint interiors.  This remains true no matter
which outward side is selected at each cusp; equality can only make two endpoints
meet, which has zero integration measure.

## 3. Sum the three cusp costs

Let the outer-atom masses at one `pi/3` orbit be

\[
w_1,w_2,w_3\ge0,
\qquad
S=w_1+w_2+w_3.
\]

Under (CS.6), the intervals in (CS.4) are disjoint.  Hence (CS.1) gives

\[
2\delta
\ge {2\over3M^2}\sum_{i=1}^3w_i^3,
\]

or

\[
\boxed{
\delta\ge {1\over3M^2}\sum_{i=1}^3w_i^3.
}
\tag{CS.8}
\]

Convexity gives

\[
\sum_{i=1}^3w_i^3\ge {S^3\over9}.
\]

Therefore

\[
\boxed{
S^3\le27M^2\delta.
}
\tag{CS.9}
\]

Compare audited §171: pigeonholing only the largest of the three atoms gives the weaker
`S^3<=81M^2 delta`.  No new train-crossing estimate is used here; the gain is purely
from spatial separation of the three outer cusps.

## 4. Improved orbit endpoint payment

For one train atomic orbit `r`, let `A_r` be its total train-atom mass and let

\[
B=\lim {Q+4f\over D}
\]

be the total bounded exceptional-face endpoint capacity.  Audited §171.11 gives

\[
\sum_{\phi\in r}\nu(\{\phi\})
\ge(2A_r-B)_+.
\tag{CS.10}
\]

Apply (CS.9):

\[
\boxed{
(2A_r-B)_+^3\le27M^2\delta.
}
\tag{CS.11}
\]

Equivalently,

\[
\boxed{
2A_r\le B+(27M^2\delta)^{1/3}.
}
\tag{CS.12}
\]

Audited §171.10 supplies atomic orbits with mass approaching

\[
R\ge {4\Delta_2\over C},
\]

where `C=(T-q/2)/D`.  Letting `A_r->R` yields the strengthened necessary condition

\[
\boxed{
B+(27M^2\delta)^{1/3}
\ge {8\Delta_2\over C}.
}
\tag{CS.13}
\]

This replaces the coefficient `81` in audited §171.4 by `27`, subject only to the
explicit small-detour condition (CS.7).

## 5. The current low-`t` band is safely inside the disjoint-cusp regime

At the current proof-only floor profile, the low-`t` topology squeeze gives

\[
\delta\le0.002883975+o(1).
\]

Also `M=pi+delta>3`.  Therefore

\[
{\delta\over M}<0.001+o(1).
\]

On the other hand

\[
{\pi^3\over5184}>{27\over5184}={1\over192}>0.005.
\]

Thus (CS.7) holds with a wide margin throughout a neighborhood of the current floor.
The factor-three improvement is therefore available exactly where the present §171
scalar frontier is binding.

## 6. Scope and remaining work

- The theorem reuses the audited §166 distributional cusp estimate; it does not assume
  smoothness of the outer direction measure.
- The three orbit locations are separated exactly by `pi/3` even after the common
  `pi/2` cusp shift.
- Other atoms of `nu` inside a cusp interval can only improve (CS.3), because they add
  positive curvature to `h''`; they do not invalidate the lower bound.
- Endpoint and bridge occurrences retain their canonical multiplicities.
- If (CS.7) fails, audited §171 with coefficient `81` remains available.
- No theorem-state promotion is claimed here.

The immediate next task is numerical but rigorous: rerun the one-variable §171 scalar
elimination with `27` in place of `81`, verify that its maximizing detour still obeys
(CS.7), and certify the resulting stronger all-Type-II `q-k` floor.  That calculation
is logically downstream of (CS.13), not part of its proof.
