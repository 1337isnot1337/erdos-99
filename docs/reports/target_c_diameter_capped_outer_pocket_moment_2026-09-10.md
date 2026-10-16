<!-- theorem-state: {"artifact_id":"ART-84D19E54EAE5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — source diameter caps the outer-pocket cubic moment

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`  
**Run type:** exact finite cavity-capacity theorem  
**Target:** Target C, C-II after OP/DD  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

DD bounded the total outer-pocket area by a cubic moment of the old-contact chain
lengths, then relaxed that moment by

\[
\sum_P\ell_P^3\le\left(\sum_P\ell_P\right)^3.
\]

For a diameter-`D` source this loses a decisive finite constraint. Every outer-pocket
force-hull chord joins two source points, so its length is at most `D`. If

\[
d_P:=\ell_P-s_P
\]

is the chain--chord detour, then

\[
\ell_P\le D+d_P.
\]

Consequently only the total normalized detour can support chain length above `D`.
This gives an exact extremal moment theorem.

---

## 1. Excess-over-diameter budget

For each outer pocket `P`, DD notation gives

\[
\ell_P=\text{old unit-contact chain length},
\qquad
s_P=\text{force-hull chord length},
\]

with

\[
d_P:=\ell_P-s_P\ge0.
\]

Since both chord endpoints lie in the source configuration of diameter `D`,

\[
0\le s_P\le D.
\tag{1.1}
\]

Normalize

\[
r_P:=\frac{\ell_P}{D},
\qquad
\delta_P:=\frac{d_P}{D}.
\]

Then (1.1) gives

\[
(r_P-1)_+
\le\delta_P.
\tag{1.2}
\]

OD/DD give the exact total detour identity

\[
\sum_Pd_P=b-P_F.
\]

Thus, with

\[
L:=\sum_Pr_P,
\qquad
\nu:=\frac{b-P_F}{D},
\]

we obtain

\[
\boxed{
\sum_P(r_P-1)_+\le\nu.
}
\tag{1.3}
\]

This is a finite source-diameter constraint, not an asymptotic approximation.

---

## 2. Exact cubic moment with an excess budget

### Lemma DC.1

Let `r_1,...,r_m>=0` satisfy

\[
\sum_i r_i=L,
\qquad
\sum_i(r_i-1)_+\le\nu.
\tag{2.1}
\]

Define `A=1+nu`.

If `L<=A`, then

\[
\boxed{
\sum_i r_i^3\le L^3.
}
\tag{2.2}
\]

If `L>A`, write

\[
R:=L-A,
\qquad
k:=\lfloor R\rfloor,
\qquad
\xi:=R-k\in[0,1).
\]

Then

\[
\boxed{
\sum_i r_i^3
\le
A^3+k+\xi^3.
}
\tag{2.3}
\]

Both bounds are sharp in the abstract finite optimization.

### Proof

First consider coordinates above one. If two coordinates satisfy `r_i>=r_j>1`,
transfer an amount `epsilon` from `r_j` to `r_i` until either `r_j=1` or the total
excess budget is exhausted. The total mass and total excess above one do not change,
while strict convexity of `x^3` increases the cubic sum. Repeating shows that at a
maximizer at most one coordinate exceeds one, and all available excess is placed in
that coordinate whenever `L>1+nu`.

If `L<=1+nu`, all mass can be placed in one coordinate; convexity gives the sharp
value `L^3`.

Now assume `L>1+nu`. The unique coordinate above one is maximized at

\[
r_1=1+\nu=A.
\]

The remaining mass is `R=L-A` and every remaining coordinate lies in `[0,1]`.
For variables in `[0,1]`, convexity again says to fill as many coordinates to one as
possible, leaving at most one fractional coordinate. Thus the remaining vector is

\[
\underbrace{1,\ldots,1}_{k\text{ times}},\ \xi,\ 0,\ldots,0,
\]

which gives (2.3). `square`

Define the sharp abstract moment function `M(L,nu)` by the right sides of
(2.2)--(2.3). It is nondecreasing in both `L` and `nu`.

---

## 3. Improved global DD bound

DD before its scalar moment relaxation gives

\[
H_{out}
\le
\frac1{\sqrt6}
\left(\sum_P\ell_P^3\right)^{1/2}
\left(\sum_Pd_P\right)^{1/2}.
\tag{3.1}
\]

Using Lemma DC.1 and scaling by `D`,

\[
\boxed{
\frac{H_{out}}{D^2}
\le
\frac1{\sqrt6}
\sqrt{M(L,\nu)\,\nu},
}
\tag{3.2}
\]

where exactly

\[
L=\frac{x_B+a}{D},
\qquad
\nu=\frac{b-P_F}{D}.
\]

This strictly improves DD.14 whenever `L>1+nu` and more than one diameter-scale chain
is required.

A convenient weaker consequence is

\[
\sum_Pr_P^3
\le(1+\nu)^2L,
\tag{3.3}
\]

because every `r_P<=1+nu`; however the piecewise exact `M(L,nu)` is substantially
stronger in the critical Target C regime.

---

## 4. Post-ZF specialization

Put

\[
y=\frac hD,
\qquad
z=\frac{Q+2s_Z}{D}.
\]

PC gives

\[
L
=\frac{2h-(Q+2s_Z)-e_{BB}+c_B}{D}
\le2(y-z).
\tag{4.1}
\]

MA and ZE give

\[
\nu
=\frac{b-P_F}{D}
\le u(y)-z+o(1),
\qquad
u(y):=y-2\cos(y/2).
\tag{4.2}
\]

Since `M` is nondecreasing in both arguments,

\[
\boxed{
\limsup\frac{H_{out}}{D^2}
\le
\frac1{\sqrt6}
\sqrt{
M(2(y-z),u(y)-z)\,[u(y)-z]
}.
}
\tag{4.3}
\]

CC still gives

\[
\limsup\frac{A_{exc}}{D^2}
\le\frac{z^2}{4\pi}.
\tag{4.4}
\]

Equations (4.3)--(4.4) are the new cavity-capacity surface.

---

## 5. Critical branch formula

On the interval

\[
2\rho\le y\le\frac85,
\]

we have

\[
0\le u(y)<\frac14.
\tag{5.1}
\]

Indeed `u` increases and

\[
\cos(4/5)>1-\frac{(4/5)^2}{2}=\frac{17}{25},
\]

so

\[
u(8/5)<\frac85-\frac{34}{25}=rac6{25}<\frac14.
\]

At `z=0`, put

\[
L=2y,
\qquad
\nu=u(y),
\qquad
p_0(y)=y+2\cos(y/2).
\]

Then

\[
L-(1+\nu)=p_0(y)-1.
\tag{5.2}
\]

The function `p_0` is strictly increasing. At the lower endpoint,

\[
p_0(2\rho)=4\rho>2,
\]

while the Taylor upper bound

\[
\cos(4/5)<1-\frac{(4/5)^2}{2}+\frac{(4/5)^4}{24}
=\frac{1307}{1875}
\]

gives

\[
p_0(8/5)<3.
\]

Hence

\[
1<p_0(y)-1<2
\]

throughout the interval. Lemma DC.1 therefore reduces to the explicit smooth formula

\[
\boxed{
M_y
=(1+u(y))^3+1+[p_0(y)-2]^3.
}
\tag{5.3}

This is the exact abstract cubic capacity at the largest permitted post-ZF chain length
and detour on the critical interval.

---

## 6. Regression audit

- **Single long chain:** DC allows one chain to exceed `D`, but only by spending the
  same amount of the global detour budget.
- **Many unit-scale pockets:** normalized lengths below one cost no excess budget and
  are packed exactly by the `k+xi^3` term.
- **Regular odd shell:** its outer-pocket detour is not in the small critical regime;
  DC remains a valid finite inequality without asserting a matching or response bound.
- **Dense isolated fillings:** DC uses only source diameter and actual OP pockets; it
  makes no global-optimality inference from them.
- **Backtracking contact chains:** allowed. DD defines `ell` by arclength; the chord
  bound `s<=D` and detour identity remain exact.

---

## 7. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| excess budget (1.3) | proved finite | each chord is at most the source diameter |
| exact moment DC.1 | proved | convex mass transfer |
| global cavity bound (3.2) | proved | DD pre-relaxation + DC.1 |
| post-ZF surface (4.3) | proved asymptotically | PC/MA/ZE monotone substitution |
| critical formula (5.3) | proved | exact branch of the piecewise moment function |
| Level I | still open | theorem has not yet been combined with MA/JC |

---

## 8. Exact next implication

Insert (4.3)--(4.4) into the MA/GU attachment-cell lower gap. On
`[2rho,8/5]`, the combined cavity maximum occurs at `z=0`; then (5.3) produces a
one-variable decreasing detour threshold. Its crossover with the increasing MA/JC
threshold is substantially above the previous `0.6056` floor.
