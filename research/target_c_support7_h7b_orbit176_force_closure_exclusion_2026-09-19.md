<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d22ab755d68e6804a08188328c7fb98fb6981cd9", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_h7b_orbit176_force_closure_exclusion_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "2126fe6c6a32f5b9ccdabc7ff40dc2415e6c9004cb613097e620e5b61fb54f67"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — exact force-closure exclusion of generic H7b orbit 176

**Date:** 2026-09-19  
**Claim class:** rigorous nonlinear exclusion inside generic interior-ground `H7b`  
**Input endpoint:** 27 affine `C7` survivors  
**Certificate:** `research/verify_target_c_support7_h7b_orbit176_affine_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The full-angle affine reduction leaves 27 generic `C7` cells. One of them, survivor 176 in the repaired canonical enumeration, is already impossible before imposing complete reciprocal metric integrability. The seven equilateral force-pentagon closures alone contradict exact affine angle identities of this cell.

Thus the generic `H7b` endpoint sharpens from

\[
\boxed{27\longrightarrow26.}
\]

## 1. Exact affine identities in survivor 176

For each non-ground force pentagon `i`, write its normalized cyclic turn gaps as

\[
x_{i,0},\ldots,x_{i,4},
\qquad
\sum_{k=0}^4x_{i,k}=2.
\]

All vertex indices below are modulo seven in `{1,...,7}`.

Exact elimination in the 84-variable full-angle equality system gives, for every `i`,

\[
\boxed{
x_{i+3,1}+x_{i+4,4}-x_{i,0}=1.}
\tag{1.1}
\]

It also gives

\[
\boxed{\sum_{i=1}^7x_{i,0}=1.}
\tag{1.2}
\]

The verifier reconstructs the exact survivor-176 order/sign state, rebuilds all 92 full-angle equalities over `fractions.Fraction`, finds equality rank 57, and checks all eight displayed consequences by exact row-span reduction.

The audited physical pentagon bounds give

\[
0<x_{i,k}<\frac23.
\tag{1.3}
\]

Equation (1.1) therefore implies, for every face,

\[
0<x_{i,0}<\frac13,
\tag{1.4}
\]

and, because the two terms on the left of (1.1) sum to more than one while each is below `2/3`, it also implies

\[
x_{i,1}>\frac13,
\qquad
x_{i,4}>\frac13.
\tag{1.5}
\]

Summing (1.1) over `i` and using (1.2) gives

\[
\sum_i(x_{i,1}+x_{i,4})=8.
\tag{1.6}
\]

Since the seven face sums total 14,

\[
\boxed{\sum_i(x_{i,2}+x_{i,3})=5.}
\tag{1.7}
\]

The rest of the argument shows that seven closed physical force pentagons satisfying (1.2), (1.4), and (1.5) must instead have a strict total below 5 in (1.7).

## 2. A sharp two-gap bound for a closed equilateral pentagon

Consider one closed equilateral pentagon with actual angular gaps

\[
T=\pi x_0,
\quad
A=\pi x_1,
\quad
B=\pi x_2,
\quad
D=\pi x_3,
\quad
E=\pi x_4.
\]

In the survivor-176 regime,

\[
0<T<\frac\pi3,
\qquad
\frac\pi3<A,E<\frac{2\pi}3.
\tag{2.1}
\]

Let the five unit force directions be `u_0,...,u_4` in cyclic order. Closure gives

\[
u_4+u_0+u_1=-(u_2+u_3).
\]

Taking squared norms yields

\[
\cos B
=
\frac12+\cos E+\cos T+\cos(E+T).
\tag{2.2}
\]

Likewise, from

\[
u_0+u_1+u_2=-(u_3+u_4),
\]

one gets

\[
\cos D
=
\frac12+\cos T+\cos A+\cos(T+A).
\tag{2.3}
\]

For fixed `T`, define on the relevant real interval

\[
f_T(z)
:=
\arccos\!\left(
\frac12+\cos T+\cos z+\cos(T+z)
\right),
\tag{2.4}
\]

and

\[
H_T(z):=z+f_T(z).
\]

Equations (2.2)-(2.3) and the total turn `2pi` give

\[
B=f_T(E),
\qquad
D=f_T(A),
\qquad
H_T(A)+H_T(E)=2\pi-T.
\tag{2.5}
\]

### Concavity of `H_T`

Put

\[
C=\cos(T/2),
\qquad
W=z+T/2,
\qquad
X=\cos W.
\]

Then the argument of `arccos` in (2.4) is

\[
R=2C(C+X)-\frac12.
\]

On (2.1), `sin W>0`, so

\[
R'=-2C\sin W<0
\]

and therefore `f_T'>0` wherever the actual pentagon makes (2.4) real.

A direct differentiation gives

\[
f_T''(z)
=
\frac{
2CX(1-R^2)-4C^2(1-X^2)R
}{(1-R^2)^{3/2}}.
\tag{2.6}
\]

The numerator in (2.6) factors as a positive scalar times

\[
-\,(4C^2-1)
\left(
4CX^2+(4C^2+3)X+4C
\right).
\tag{2.7}
\]

Here

\[
C^2\in(3/4,1).
\]

The quadratic in `X` in (2.7) has leading coefficient `4C>0` and discriminant

\[
16C^4-40C^2+9.
\]

For `C^2 in (3/4,1)`, this discriminant is strictly negative: the polynomial `16u^2-40u+9` is decreasing on this interval and already equals `-12` at `u=3/4`. Hence the quadratic is positive for every real `X`. Therefore

\[
f_T''<0,
\qquad
H_T'>0,
\qquad
H_T''<0.
\tag{2.8}
\]

So `H_T` is strictly increasing and strictly concave on its relevant interval, and its inverse is strictly convex.

Applying Jensen to (2.5) gives

\[
A+E
\ge
2H_T^{-1}\!\left(\pi-\frac T2\right).
\tag{2.9}
\]

At equality, `A=E=a`. Writing

\[
\gamma(T):=a+\frac T2,
\]

condition (2.5) simplifies to

\[
\cos\gamma(T)
=
\frac12-\cos(T/2),
\]

so

\[
\gamma(T)
=
\arccos\!\left(\frac12-\cos(T/2)\right).
\tag{2.10}
\]

Consequently every such closed pentagon satisfies

\[
\boxed{
B+D
\le
m(T)
:=
2\left[
\pi-\arccos\!\left(\frac12-\cos(T/2)\right)
\right].
}
\tag{2.11}
\]

Equality is the reflected-symmetric gap pattern `T,A,B,B,A`.

## 3. The sharp bound is convex in `T`

Let

\[
r(T)=\frac12-\cos(T/2),
\qquad
\gamma(T)=\arccos r(T).
\]

With `c=cos(T/2)`, direct differentiation gives

\[
\gamma''(T)
=
-\frac{2c^2-c+2}{16(1-r^2)^{3/2}}
<0.
\tag{3.1}
\]

Therefore

\[
\boxed{m''(T)>0}
\tag{3.2}
\]

on `(0,pi/3)`. Extend `m` continuously to `[0,pi/3]`.

For seven values

\[
0\le T_i\le\frac\pi3,
\qquad
\sum_iT_i=\pi,
\tag{3.3}
\]

a convex function attains its maximum over this hypersimplex at a vertex. Its vertices have exactly three coordinates `pi/3` and four coordinates `0`. Hence

\[
\sum_i m(T_i)
\le
3m(\pi/3)+4m(0).
\tag{3.4}
\]

Now

\[
m(0)=\frac{2\pi}{3},
\]

while

\[
m(\pi/3)
=
2\left[
\pi-\arccos\left(\frac{1-\sqrt3}{2}\right)
\right].
\]

Let

\[
a=\frac{\sqrt3-1}{2}.
\]

Since `sin(pi/9)<1/2`, the function `3s-4s^3` is strictly increasing at `s=sin(pi/9)`. Moreover

\[
3a-4a^3-\frac{\sqrt3}{2}
=
\frac72-2\sqrt3
>0.
\]

Because

\[
3\sin(\pi/9)-4\sin^3(\pi/9)
=
\sin(\pi/3)
=
\frac{\sqrt3}{2},
\]

we obtain

\[
a>\sin(\pi/9).
\]

Thus

\[
\frac{1-\sqrt3}{2}
<
-\sin(\pi/9)
=
\cos(11\pi/18),
\]

and since `arccos` is decreasing,

\[
\arccos\left(\frac{1-\sqrt3}{2}\right)
>
\frac{11\pi}{18}.
\tag{3.5}
\]

Substituting (3.5) into (3.4) gives the strict estimate

\[
\boxed{
\sum_i m(T_i)<5\pi.
}
\tag{3.6}
\]

## 4. Contradiction

For survivor 176, set

\[
T_i=\pi x_{i,0}.
\]

The exact affine identity (1.2) gives

\[
\sum_iT_i=\pi.
\]

Applying (2.11) face by face and then (3.6),

\[
\sum_i\pi(x_{i,2}+x_{i,3})
=
\sum_i(B_i+D_i)
<5\pi.
\]

But exact affine bookkeeping (1.7) requires

\[
\sum_i\pi(x_{i,2}+x_{i,3})=5\pi.
\]

Contradiction.

Therefore

\[
\boxed{\text{generic H7b survivor 176 is impossible.}}
\]

This exclusion uses only the full-angle affine identities and the seven non-ground equilateral-pentagon closures. It does not use the fifteen complete metric sine-cycle equations.

The generic interior-ground `H7b` affine endpoint is therefore reduced from 27 to 26 cells. The surviving IDs are

```text
115, 118, 129, 130,
134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148,
169, 170, 171, 172, 173, 174, 175
```

No theorem-state file is changed. C-II remains open.
