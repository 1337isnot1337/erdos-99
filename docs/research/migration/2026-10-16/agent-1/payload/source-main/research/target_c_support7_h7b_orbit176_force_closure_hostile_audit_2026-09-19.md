# Hostile audit — generic H7b orbit-176 force-closure exclusion

**Date:** 2026-09-19  
**Audited note:** `target_c_support7_h7b_orbit176_force_closure_exclusion_2026-09-19.md`  
**Verdict:** PASS at the stated generic-`H7b` scope  
**Theorem-state authority:** unchanged; C-II remains open

This audit rechecked the parts of the orbit-176 exclusion where a sign, indexing, convexity direction, or endpoint estimate could invalidate the contradiction.

## 1. The affine identities are independently machine-checkable

The dedicated verifier rebuilds the survivor-176 full-angle equality system rather than trusting the prose identities. It checks exact rank 57 over rational arithmetic and verifies row-span membership of

\[
x_{i+3,1}+x_{i+4,4}-x_{i,0}=1
\]

for all seven cyclic indices, together with

\[
\sum_i x_{i,0}=1.
\]

The verifier uses the corrected per-vertex force cycle `cyc[i]`; it does not reproduce the dispatch defect found in the earlier historical H7b verifier.

Local execution output:

```text
PASS: orbit 176 exact affine force-gap consequences
equality rank: 57
certified cyclic cross-face relations: 7
certified sum_i x[i,0] = 1
```

## 2. The gap-regime deduction uses strict bounds in the correct direction

From

\[
x_{i+3,1}+x_{i+4,4}=1+x_{i,0}
\]

and the audited physical bound `0<x<2/3`:

- the left side is strictly below `4/3`, so `x_{i,0}<1/3`;
- the left side is strictly above `1`, so either summand is strictly above `1/3` because the other is strictly below `2/3`.

As the cyclic relations cover every index in positions 1 and 4, this gives

\[
0<x_{i,0}<1/3,
\qquad
x_{i,1},x_{i,4}>1/3
\]

for every face. No non-strict endpoint is used as an actual physical configuration.

Summing the seven cross-face relations and the seven face sums gives exactly

\[
\sum_i(x_{i,2}+x_{i,3})=5.
\]

## 3. The two norm identities use the intended gaps

For one force pentagon, set the cyclic gaps to `T,A,B,D,E`. Squaring

\[
u_4+u_0+u_1=-(u_2+u_3)
\]

produces

\[
\cos B=\frac12+\cos E+\cos T+\cos(E+T).
\]

Squaring

\[
u_0+u_1+u_2=-(u_3+u_4)
\]

produces

\[
\cos D=\frac12+\cos T+\cos A+\cos(T+A).
\]

The right-hand pair in the first identity is separated by `B`; the right-hand pair in the second is separated by `D`. No off-by-one gap occurs.

Because every physical gap is in `(0,2pi/3)`, `arccos` recovers `B` and `D` uniquely in `(0,pi)`.

## 4. The Jensen direction is correct

For fixed `T`, the function

\[
H_T(z)=z+f_T(z)
\]

has `H_T'>0` and `H_T''<0` on the relevant connected real domain. Therefore `H_T^{-1}` is convex, not concave. With

\[
H_T(A)+H_T(E)=2\pi-T,
\]

Jensen gives

\[
A+E\ge2H_T^{-1}(\pi-T/2),
\]

so

\[
B+D=2\pi-T-A-E
\]

is bounded **above** by the symmetric case. This is the direction required by the global contradiction.

The sign of `f_T''` was re-expanded. With `C=cos(T/2)` and `X=cos(z+T/2)`, its numerator is a negative positive-factor multiple of

\[
(4C^2-1)\,[4CX^2+(4C^2+3)X+4C].
\]

For `C^2 in (3/4,1)`, the quadratic discriminant

\[
16C^4-40C^2+9
\]

is negative. Thus the quadratic is positive for every real `X` and `f_T''<0` is valid throughout the relevant domain.

## 5. The outer convexity step is also in the correct direction

The sharp upper envelope is

\[
m(T)=2\left[\pi-\arccos\left(\frac12-\cos(T/2)\right)\right].
\]

Direct differentiation gives

\[
\gamma''(T)
=-\frac{2c^2-c+2}{16(1-r^2)^{3/2}}<0,
\]

for `gamma=arccos r`, `r=1/2-c`, `c=cos(T/2)`. Hence `m''(T)>0`: `m` is convex.

A convex function reaches its maximum over

\[
0\le T_i\le\pi/3,
\qquad
\sum_iT_i=\pi
\]

at a polytope vertex. Scaling by `3/pi` gives the hypersimplex

\[
0\le s_i\le1,
\qquad
\sum_i s_i=3,
\]

whose vertices are exactly the zero-one vectors with three ones. Thus the claimed endpoint pattern of three `pi/3` values and four zeros is correct.

## 6. The endpoint comparison is exact

At the two endpoints,

\[
m(0)=2\pi/3,
\]

and

\[
m(\pi/3)=2\left[\pi-\arccos((1-\sqrt3)/2)\right].
\]

The proof needs

\[
\arccos((1-\sqrt3)/2)>11\pi/18.
\]

Writing `a=(sqrt(3)-1)/2`, one has

\[
3a-4a^3-\sqrt3/2=7/2-2\sqrt3>0.
\]

Since `3s-4s^3` is strictly increasing on `(0,1/2)` and `s=sin(pi/9)` satisfies `3s-4s^3=sqrt(3)/2`, it follows that `a>sin(pi/9)`. This is exactly the required comparison after applying the decreasing `arccos` function.

Therefore

\[
3m(\pi/3)+4m(0)<5\pi
\]

with no decimal approximation.

## 7. Scope check

The contradiction excludes only canonical generic `H7b` survivor 176. It does not eliminate the remaining 26 generic `H7b` cells, any reciprocal wall case, `H7a`, `H6`, or `H8`. It uses no complete sine-cycle metric condition, so there is no hidden assumption that the reciprocal coordinates have already been reconstructed.

Verdict: the `27 -> 26` generic-`H7b` reduction is supportable as stated.
