> Generated reading edition · [exact source](../../../docs/reports/target_c_renorm_sidecost_floor_08364_2026-09-10.md) · source SHA-256 `8d1e2ea33a66f7806186f6fc98498032d54fd3a6aaeb3133e2f265f91942a4e0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-71AEAFDF0AB4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — projective side-cost feedback raises the renormalized floor to `mu_SC`

**Date:** 2026-09-10  
**Repository branch:** `research/c2-renorm-paired-pocket-20260910` after RL/RLE  
**Run type:** force-area / paired-pocket feedback optimization  
**Target:** Target C, all post-ZF survivors  

## LEVEL I STATUS

`STILL OPEN`.

This report feeds the macroscopic projective-gap side cost back into the force-hull
area lower bound.  Combined with the perimeter-capped pocket LP, it raises the
all-phase renormalized lower endpoint from `mu_rho=0.809273...` to a new analytically
defined constant

$$
\boxed{
\liminf\mu_D\ge\mu_{SC},
\qquad
\mu_{SC}=0.836440399\ldots .
}
\tag{SC.1}
$$

The decimal is diagnostic.  The proof gives the rigorous bracket

$$
\boxed{0.834<\mu_{SC}<0.84.}
\tag{SC.2}
$$

No numerical optimizer is used.

---

## 1. The projective side-cost area floor

Let the projective diameter-direction gaps with positive limiting size be

$$
r_1,\ldots,r_t.
$$

The FS midpoint Hausdorff theorem and radial flat-side transfer used in RP/RLE show
that a macroscopic projective gap `r_j` creates two opposite actual force-hull sides,
each of normalized limiting length

$$
\sin(r_j/2).
$$

Each such side is longer than one for large `D`, hence is a missing force-hull contact
side and has an OP contact chain.  By the triangle inequality the two chains consume,
at leading order, at least

$$
c_j:=2\sin(r_j/2)
\tag{1.1}
$$

of `d_P/D`.  Consequently

$$
\boxed{
\sum_jc_j\le\tau:=\liminf d_P/D.
}
\tag{1.2}
$$

The FS midpoint theorem also gives

$$
\frac{area(F)}{D^2}
=
\frac14\sum_i\sin\gamma_i+o(1),
\tag{1.3}
$$

where all projective gaps `gamma_i` sum to `pi`.  Gaps tending to zero have total
sine deficit `o(1)`, so

$$
\liminf\frac{area(F)}{D^2}
\ge
\frac14\left[
\pi-\sum_j(r_j-\sin r_j)
\right].
\tag{1.4}
$$

For

$$
c=2\sin(r/2),
\qquad
\varphi(c):=r-\sin r
=2\arcsin(c/2)-c\sqrt{1-c^2/4},
$$

one has

$$
\varphi'(c)=\frac{c^2}{2\sqrt{1-c^2/4}}>0,
$$

and `varphi'` is increasing.  Thus `varphi` is increasing, convex, and, because
`varphi(0)=0`, superadditive whenever the summed argument remains below `2`:

$$
\varphi(c_1)+\varphi(c_2)\le\varphi(c_1+c_2).
\tag{1.5}
$$

Let

$$
x=\lim(d_P+Q)/D.
$$

Since `tau<=x`, whenever `x<2`, equations (1.2)-(1.5) imply

$$
\boxed{
\liminf\frac{area(F)}{D^2}
\ge
A(x):=
\frac{\pi-r_x+\sin r_x}{4},
\qquad
r_x=2\arcsin(x/2).
}
\tag{SC.3}
$$

Because `A` decreases in `x`, RL's upper bound `x<=M(mu,y)` yields

$$
\boxed{
\liminf\frac{area(F)}{D^2}
\ge A(M(\mu,y))
}
\tag{1.6}
$$

throughout the range `mu<=0.84`, where `M<2` automatically.

Together with FSDB,

$$
\boxed{
\liminf\frac{area(F)}{D^2}
\ge
\max\{\Phi(y),A(M(\mu,y))\}.
}
\tag{1.7}
$$

---

## 2. Necessary side-cost/cavity inequality

GR/ZK gives

$$
C_{att}/D^2\le\frac\pi4\mu^2+o(1),
$$

and RP paired-pocket capacity gives

$$
G/D^2\le\frac{M(\mu,y)^2}{4\pi}+o(1).
$$

Since `area(F)=C_att+G`, every survivor limit with `mu<=0.84` must satisfy

$$
\boxed{
\max\{\Phi(y),A(M(\mu,y))\}
\le
\frac\pi4\mu^2+
\frac{M(\mu,y)^2}{4\pi},
\quad 2\rho\le y\le\pi.
}
\tag{SC.4}

---

## 3. The second RL branch is still impossible below `0.84`

For

\[
y\ge y_c(\mu)=\frac{2\pi+\mu}{3},
$$

RL gives

$$
M(\mu,y)=\frac{2\mu+\pi}{3}.
$$

Discarding `A(M)` only weakens SC.4.  The resulting `Phi` gap is concave in `y`, so
its minimum on this branch is at `y=y_c` or `y=pi`.

At `mu=0.84`, exact rational pi/Taylor bounds give

$$
F(0.84,y_c)
>
0.00736,
\tag{3.1}
$$

and

$$
F(0.84,\pi)
>
\frac{100733847}{3926875000}>0.0256.
\tag{3.2}
$$

The two endpoint gaps decrease with `mu` throughout the already-live interval
`mu>=mu_rho>0.8`.  Therefore no state with `mu<=0.84` is feasible on the second RL
branch.

---

## 4. The first branch has one area-floor crossover

Now

$$
2\rho\le y\le y_c(\mu),
\qquad
M(\mu,y)=m:=\frac{\mu+y}{2}.
\tag{4.1}
$$

The function `Phi(y)` strictly increases in `y`, while `A(m)` strictly decreases.
Moreover there is an exact geometric characterization of their crossover.

Write

$$
r_m=2\arcsin(m/2).
$$

Since

$$
A(m)=\frac{\pi-r_m+\sin r_m}{4}
=\Phi(\pi-r_m),
$$

and `Phi` is strictly increasing on `(0,pi)`,

$$
A(m)=\Phi(y)
\iff
\pi-r_m=y.
$$

Equivalently

$$
\boxed{m=2\cos(y/2),}
\tag{4.2}
$$

or, after inserting (4.1),

$$
\boxed{
\mu=4\cos(y/2)-y.
}
\tag{4.3}
$$

The right side is strictly decreasing because its derivative is

$$
-2\sin(y/2)-1<0.
$$

At `y=2rho` it equals `2rho>0.84`, while at `y=2pi/3` it is
`2-2pi/3<0`; and `2pi/3<y_c(mu)`.  Thus every relevant `mu` has exactly one crossover
inside the first branch.

Below the crossover, `A(m)` is the larger area floor.  The gap

$$
A(m)-\frac\pi4\mu^2-\frac{m^2}{4\pi}
$$

strictly decreases with `y`, because `m` increases, `A` decreases, and the quadratic
term increases.

Above the crossover, `Phi(y)` is larger.  The corresponding gap is the strictly
concave RL first-branch function, so its minimum between the crossover and `y_c` is at
one of those two endpoints.  Section 3 rules out `y_c` through `mu=0.84`.

Therefore the global easiest point below `mu=0.84` is exactly the unique crossover
(4.3).

---

## 5. One-variable analytic threshold

At the crossover put

$$
c=\cos(y/2),
\qquad
\mu(y)=4c-y,
\qquad
m=2c.
$$

SC.4 becomes

$$
E(y)\le0,
$$

where

$$
\boxed{
E(y)
:=
\frac{y+\sin y}{4}
-
\frac\pi4\bigl(4\cos(y/2)-y\bigr)^2
-
\frac{\cos^2(y/2)}{\pi}.
}
\tag{SC.5}
$$

Differentiate.  With

$$
s=\sin(y/2),\qquad c=\cos(y/2),\qquad \mu(y)=4c-y,
$$

one obtains

$$
\boxed{
E'(y)
=
\frac{c^2}{2}
+
\frac\pi2\mu(y)(2s+1)
+
\frac{cs}{\pi}>0
}
\tag{5.1}
$$

whenever `mu(y)>0`.  Thus `E` has at most one zero in the relevant interval.

Exact alternating Taylor bounds, together with

$$
6283/2000<\pi<3927/1250,
$$

give

$$
E(1.74)<-0.00416<0,
\tag{5.2}
$$

and

$$
E(1.742)>0.00308>0.
\tag{5.3}
$$

Hence there is a unique

$$
y_*\in(1.74,1.742)
$$

with

$$
E(y_*)=0.
$$

Define

$$
\boxed{
\mu_{SC}:=4\cos(y_*/2)-y_*.
}
\tag{SC.6}
$$

Because `mu(y)` is strictly decreasing, the same exact Taylor bounds give

$$
\mu(1.742)>0.834,
\qquad
\mu(1.74)<0.84.
$$

This proves SC.2.

High-precision evaluation gives

$$
\boxed{
\begin{aligned}
y_*&=1.74113348\ldots,\\
\mu_{SC}&=0.836440399\ldots,\\
m_*&=1.28878694\ldots .
\end{aligned}}
\tag{5.4}
$$

These decimals are not proof inputs.

For every `mu<mu_SC`, the crossover gap is positive, while Sections 3-4 show all other
`y` values have an even larger gap.  SC.4 is therefore impossible.  This proves SC.1.

---

## 6. Equality structure

A sequence with

$$
\mu_D\to\mu_{SC}
$$

must satisfy

$$
\boxed{
h/D\to y_*,}
\tag{6.1}
$$

$$
\boxed{
(d_P+Q)/D\to m_*=2\cos(y_*/2),
}
\tag{6.2}
$$

and equality in both force-area floors:

$$
\boxed{
area(F)/D^2
\to
\Phi(y_*)=A(m_*).
}
\tag{6.3}
$$

The exact RPE remainder then forces

$$
\boxed{
s_Z+a+c_B+2s_C=o(D).}
\tag{6.4}
$$

Since this endpoint lies in the first RL branch, the uncapped LP equality also gives

$$
\frac{d_H}{D}	o\frac{y_*-\mu_{SC}}2>0.
\tag{6.5}
$$

The next question is whether simultaneous equality in the side-cost area floor and
paired-pocket cavity capacity is possible.  The side-cost equality already consumes
all of `m_*D` in the two opposite hull chords associated with the unique macroscopic
projective gap.  That leaves no linear detour for the positive quadratic paired-pocket
area required by SC.5.  This suggests the endpoint is impossible.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| side-cost area floor SC.3 | proved asymptotically | FS midpoint polygon + radial side transfer + convex/superadditive gap defect |
| combined floor SC.4 | proved | max of FSDB and SC.3 + GR/ZK + paired cavity |
| second RL branch excluded through 0.84 | proved | branch concavity + rational endpoint margins |
| one crossover on first branch | proved | `Phi` increasing, `A` decreasing, exact equation `mu=4cos(y/2)-y` |
| scalar optimizer | proved | monotonicity on each side of crossover |
| unique threshold `mu_SC` | proved analytically | `E'(y)>0` and exact rational sign bracket |
| decimal `0.836440399...` | diagnostic | not a proof dependency |
| SC endpoint impossible | not proved here | addressed next |
| Level I | open | high-renormalized-surplus phase remains |

---

## 8. Next target

Prove the simultaneous-equality obstruction indicated in Section 6.  At SC equality,
projective-gap concentration should force one gap `pi-y_*`, hence two opposite force
sides whose combined normalized chord length is exactly

$$
2\cos(y_*/2)=m_*.
$$

But `(d_P+Q)/D->m_*`, so side-cost saturation should force `Q=o(D)` and make the two
outer chains asymptotically taut.  Their area is then `o(D^2)`, while SC equality
requires a positive cavity limit `m_*^2/(4pi)`.  Formalizing this closes the scalar
endpoint and yields a uniform gap above `mu_SC`.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let M(mu,y) be RL's exact LP upper bound for x=(d_P+Q)/D.
FS midpoint geometry implies every macroscopic projective gap r creates two opposite
F sides of total normalized chord cost c=2sin(r/2), paid by d_P/D.  Convexity of
  phi(c)=2asin(c/2)-c sqrt(1-c^2/4)
gives the second force-area floor
  area(F)/D^2 >= A(M)=[pi-r_M+sin r_M]/4.
Thus every survivor needs
  max(Phi(y),A(M)) <= pi mu^2/4+M^2/(4pi).
The second RL branch stays impossible through mu=.84.
On the first branch M=(mu+y)/2.  The two area floors cross exactly when
  M=2cos(y/2), i.e. mu=4cos(y/2)-y.
The global minimum occurs at this crossover.  Substitution gives E(y), with
  E'(y)=c^2/2+(pi/2)mu(y)(2s+1)+cs/pi>0.
There is one root y_* in (1.74,1.742), defining
  mu_SC=4cos(y_*/2)-y_*=0.836440399...,
with rigorous 0.834<mu_SC<0.84.
Therefore liminf mu_D>=mu_SC.

Next: side-cost equality uses all d_P on two taut opposite pockets but cavity equality
needs positive quadratic area; exclude the endpoint.
```
