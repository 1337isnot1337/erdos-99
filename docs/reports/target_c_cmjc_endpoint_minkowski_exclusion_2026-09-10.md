<!-- theorem-state: {"artifact_id":"ART-370E10CB6670","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — CMJC endpoint excluded by strict chord/detour Minkowski geometry

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`, after the CMJC `0.669308...` floor  
**Run type:** equality-case closure  
**Target:** Target C, C-II after ZF/DB/FS/MA/JC/DD/CC/CM  
**LEVEL I STATUS:** `STILL OPEN`

The CMJC endpoint

\[
\lambda_C=0.6693086716797393537\ldots
\]

is not asymptotically attainable. Hence there is an absolute, presently nonexplicit
`eta_C>0` such that every sufficiently large audited post-ZF survivor satisfies

\[
\boxed{
(e_{BB}+2s_C)/D\ge\lambda_C+\eta_C.
}
\tag{MX.1}
\]

The contradiction is an equality incompatibility inside the universal CM theorem.
MA/JC equality gives exactly one missing projective circle interval, so the force-hull
chord vector has two equal macroscopic entries. CM then used Minkowski together with
`||d||_3<=||d||_1` for the outer-pocket detour vector. The first inequality requires
proportional chord and detour vectors for equality; the second requires all positive
detour to lie in one coordinate. Since the chord vector has two positive coordinates
and total detour is positive, both equalities cannot hold.

A direct finite-capacity version below avoids relying only on equality-condition words.

---

## 1. Endpoint data

Assume for contradiction that an audited survivor sequence satisfies

\[
\frac{e_{BB}+2s_C}{D}\to\lambda_C.
\tag{1.1}
\]

CMJC localization gives

\[
\frac hD\to y_C,
\qquad
\frac{Q+2s_Z}{D}\to0,
\tag{1.2}
\]

\[
\frac{P_F}{D}\to p_0(y_C),
\qquad
\frac{e_{BB}}D\to\lambda_C,
\qquad
\frac{s_C}{D}\to0,
\tag{1.3}
\]

where

\[
p_0(y)=y+2\cos(y/2),
\qquad
u(y)=y-2\cos(y/2).
\]

Put

\[
c:=\cos(y_C/2)>0,
\qquad
\nu:=\nu(y_C)>0.
\tag{1.4}
\]

Numerically

\[
c=0.6650396953807457682\ldots,
\qquad
\nu=0.3564193225522907919\ldots .
\]

ZE and (1.2)--(1.3) give

\[
\boxed{
(b-P_F)/D\to\nu.
}
\tag{1.5}
\]

---

## 2. MA equality again gives exactly one projective gap

Let `K_infty` be a normalized FS force-hull limit. As in the MAJC, MADD, and DCJC
equality audits, write its projective missing-circle gap lengths as `alpha_i`, with
`X=sum alpha_i<=pi-y_C`.

The exact cyclic perimeter formula is

\[
P(K_\infty)=\pi-X+2\sum_i\sin(\alpha_i/2).
\tag{2.1}
\]

Merging two positive gaps strictly lowers the sine sum, while

\[
X\mapsto\pi-X+2\sin(X/2)
\]

is strictly decreasing. Because (1.3) attains MA's minimum perimeter `p_0(y_C)`, both
inequalities are equalities. Therefore

\[
\boxed{
X=\pi-y_C,
\qquad
\text{exactly one projective gap has positive length.}
}
\tag{2.2}
\]

Its ordinary-circle lift consists of two antipodal gaps. Hence the normalized force
hull has exactly two macroscopic straight sides, each of length

\[
\boxed{c=\cos(y_C/2).}
\tag{2.3}
\]

All remaining finite force-hull sides have length `o(D)` in the cubic-moment sense:
for every fixed `epsilon`, the sum of cubes of sides shorter than `epsilon D` is at
most `pi epsilon^2D^3+o(D^3)`, and no third side can retain a positive normalized
length without creating another limit gap.

---

## 3. Exact one-gap chain moment

For each outer pocket write

\[
\ell_P=s_P+d_P,
\qquad d_P\ge0.
\]

The two macroscopic sides in (2.3) are noncontact for large `D`, so they determine two
distinct OP pockets. Pass to a subsequence on which their normalized detours tend to
`delta_1,delta_2`. Let

\[
\delta_0:=\nu-\delta_1-\delta_2\ge0
\]

be the remaining normalized detour, using (1.5).

Exactly as in the DCJC one-gap audit, Minkowski on the remaining `o(D)`-chord pockets
gives

\[
\limsup D^{-3}\sum_P\ell_P^3
\le
(c+\delta_1)^3+(c+\delta_2)^3+\delta_0^3.
\tag{3.1}
\]

The right side is convex on the detour simplex. Its maximum is obtained by assigning
all detour to one of the two `c`-based pockets, because

\[
(c+\nu)^3-c^3-\nu^3=3c\nu(c+\nu)>0.
\]

Thus

\[
\boxed{
\limsup D^{-3}\sum_P\ell_P^3
\le
M_{1g}:=(c+\nu)^3+c^3.
}
\tag{3.2}
\]

---

## 4. Strict loss relative to CM

CM's universal scalar chain-moment bound at `z=0` is

\[
\boxed{
M_{CM}:=(2^{1/3}c+\nu)^3.
}
\tag{4.1}
\]

We have

\[
\boxed{M_{1g}<M_{CM}.}
\tag{4.2}
\]

One direct proof is strict Minkowski in `l^3`. The vector `(c,c)` has norm
`2^{1/3}c`. Adding the detour vector `(nu,0)` gives norm cubed

\[
(c+\nu)^3+c^3=M_{1g}.
\]

Since `(c,c)` and `(nu,0)` are not positive scalar multiples when `c,nu>0`, strict
Minkowski gives

\[
M_{1g}^{1/3}<2^{1/3}c+\nu,
\]

which is (4.2).

---

## 5. Contradiction with the CMJC crossover

DD before the scalar moment relaxation gives

\[
H_{out}
\le
\frac1{\sqrt6}
\left(\sum_P\ell_P^3\right)^{1/2}
(b-P_F)^{1/2}.
\]

Using (1.5) and (3.2),

\[
\limsup\frac{H_{out}}{D^2}
\le
\frac1{\sqrt6}\sqrt{M_{1g}\nu}.
\tag{5.1}
\]

Since `z->0`, CC gives

\[
A_{exc}=o(D^2).
\tag{5.2}
\]

On the other hand CMJC defines its crossover by

\[
\boxed{
\Phi(y_C)-\frac\pi4\lambda_C^2
=
\frac1{\sqrt6}\sqrt{M_{CM}\nu}.
}
\tag{5.3}
\]

MA/GU therefore require

\[
\liminf\frac GD^2
\ge
\frac1{\sqrt6}\sqrt{M_{CM}\nu}.
\tag{5.4}
\]

But the cavity decomposition `G<=H_out+A_exc+O(D)`, together with (4.2), (5.1), and
(5.2), gives

\[
\limsup\frac GD^2
\le
\frac1{\sqrt6}\sqrt{M_{1g}\nu}
<
\frac1{\sqrt6}\sqrt{M_{CM}\nu},
\]

contradiction. Thus the CMJC endpoint cannot occur. `square`

A diagonal sequence gives the uniform positive gap (MX.1). `square`

---

## 6. Regression audit

- **Regular odd shell:** its missing projective angle tends to zero, so the two-positive-
  chord equality geometry here is absent.
- **Many microscopic force-hull sides:** allowed; their normalized cubic chord mass
  vanishes without requiring their total perimeter to vanish.
- **One giant detour pocket:** retained and in fact maximizes (3.1), but still gives a
  strict Minkowski loss because the second macroscopic antipodal chord remains.
- **Many detour pockets:** convexity only lowers the cubic moment relative to the one-
  pocket detour allocation.
- **Dense isolated fillings:** no global-optimality inference is made from them.
- **Matching/response-trace regressions:** unused.

---

## 7. Exact effect and remaining implication

This removes the entire equality class at the strongest explicit CMJC threshold and
proves a uniform, though nonexplicit, gap above `0.669308...`.

It still does not close C-II because the current theorem stack has no universal upper
bound below that gap. The next step should not be another isolated scalar iteration.
The remaining useful routes are:

1. a source-wide upper bound on `e_BB+2s_C` from the exact ZU/ZK/loaded-degree ledgers
   plus cyclic force-hull geometry; or
2. a representative-transfer theorem that lets RA's no-isolate global minimizer enter
   the jammed shell/Oler endgame without falsely transferring `C=C_*` or ZF.