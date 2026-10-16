<!-- theorem-state: {"artifact_id":"ART-CA0CE458D3C8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`, PS: an infinite exact family of symmetric SCE roots

**Date:** 2026-09-10  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact analytic regression / infinite shell-closure family  
**Target:** PS branch after complete P2 exclusion  
**Depends on:** SW staircase-word normal form; D2C defect cells; SCE exact shell closure  
**External literature:** none  
**Computation:** none used in the proof

## LEVEL I STATUS

`STILL OPEN`

P2X eliminates the complete P2 branch for sufficiently large shells. The next tempting route would be to prove that the nonzero midpoint error in PS/S2 makes the two-staircase closure equation impossible.

That route is false already for PS, in an infinite exact family.

### Theorem PSR — infinite symmetric PS closure roots

For every integer

\[
k\ge1,
\]

put

\[
\boxed{q=8k+4,\qquad L_A=L_B=4k}
\tag{PSR.1}
\]

and choose both staircase words to be

\[
\boxed{
\varepsilon^A=\varepsilon^B=(-,+,+,-)^k.
}
\tag{PSR.2}
\]

Then there exists a diameter parameter

\[
D_k>1
\]

for which the exact SCE equations hold in the genuine PS regime:

1. the first defect cell is parallel,
   \[
   G_1=\Delta_2:=2\arcsin(1/D_k);
   \]
2. the second defect cell is strictly short,
   \[
   2\delta<G_2<\Delta_2,
   \qquad
   \delta:=2\arcsin(1/(2D_k));
   \]
3. the second midpoint offset is nonzero;
4. the complete complex SCE closure holds exactly.

Thus SCE, even with the exact defect-vector directions retained, cannot by itself eliminate PS for large `q`.

The proof is constructive by a scalar intermediate-value argument.

---

## 1. The repeated staircase polynomial is explicit

Put

\[
z=e^{i\delta}.
\]

One block of the word `(-,+,+,-)` contributes

\[
-1+z+z^2-z^3=(z-1)(1-z^2).
\]

Repeating the block `k` times gives

\[
\begin{aligned}
P_k(z)
&=(-1+z+z^2-z^3)\sum_{j=0}^{k-1}z^{4j}\\
&=(z-1)(1-z^2)\frac{1-z^{4k}}{1-z^4}\\
&=\boxed{\frac{(z-1)(1-z^{4k})}{1+z^2}.}
\end{aligned}
\tag{1.1}

For the admissible range below all relevant sines and cosines are positive. Therefore

\[
\boxed{
P_k(e^{i\delta})
=
\frac{\sin(2k\delta)}{D\cos\delta}
\,e^{i(2k-1/2)\delta}.
}
\tag{1.2}

Indeed

\[
|z-1|=2\sin(\delta/2)=1/D,
\]

and the geometric-series phase gives the displayed argument.

---

## 2. PS kinematics reduce SCE to one scalar equation

Fix the first cell at the parallel endpoint

\[
G_1=\Delta_2.
\]

Because

\[
L_A=L_B=4k,
\]

the second projective switch gap is forced by the half-circle direction sum:

\[
\boxed{
G_2
=\pi-8k\delta-\Delta_2.
}
\tag{2.1}

The B-direction block begins at

\[
\theta_B=4k\delta+\Delta_2.
\tag{2.2}

The first parallel cell has midpoint offset

\[
W_1=0.
\]

For the second cell put

\[
\boxed{
W(D):=
\sqrt{1-D^2\sin^2(G_2/2)}.
}
\tag{2.3}

Its bisector direction, using the lift whose final B diameter direction is `pi-G_2`, is

\[
\boxed{
\phi_2=\pi-G_2/2
=\frac\pi2+4k\delta+\frac{\Delta_2}{2}.
}
\tag{2.4}

Now insert `P_A=P_B=P_k` into SCE. The two staircase midpoint terms sum to

\[
M(D)
:=\frac i2 e^{i\delta/2}P_k
\left(1+e^{i\theta_B}\right).
\tag{2.5}

Using (1.2) and

\[
1+e^{i\theta_B}
=2\cos(\theta_B/2)e^{i\theta_B/2},
\]

we obtain the exact phase identity

\[
\boxed{
M(D)=\mu_k(D)e^{i\phi_2},
}
\tag{2.6}

where

\[
\boxed{
\mu_k(D)
=
\frac{\sin(2k\delta)\,
\cos(2k\delta+\Delta_2/2)}{D\cos\delta}.
}
\tag{2.7}

Thus the vector SCE equation is solved by the geometrically correct second-cell sign precisely when

\[
\boxed{
\mu_k(D)=W(D).
}
\tag{2.8}

There is no remaining phase equation.

---

## 3. The genuine-PS admissible interval is nonempty

Let `D_-` be the unique solution of

\[
\boxed{
(8k+2)\delta(D_-)+\Delta_2(D_-)=\pi.
}
\tag{3.1}

By (2.1), this is exactly the lower switch boundary

\[
G_2=2\delta.
\]

Let `D_+` be the unique solution of

\[
\boxed{
8k\delta(D_+)+2\Delta_2(D_+)=\pi.
}
\tag{3.2}

This is exactly the upper switch boundary

\[
G_2=\Delta_2.
\]

Both left sides are continuous and strictly decreasing for `D>1`, from values above `pi` to zero, so both roots exist uniquely.

For every `D>1`,

\[
\Delta_2>2\delta,
\]

because

\[
\arcsin(1/D)>2\arcsin(1/(2D)).
\]

Hence at a common `D`, the left side of (3.1) is strictly smaller than the left side of (3.2). Since both functions decrease in `D`,

\[
\boxed{D_-<D_+.}
\tag{3.3}

For

\[
D\in(D_-,D_+),
\]

we therefore have exactly

\[
\boxed{2\delta<G_2<\Delta_2,}
\tag{3.4}

so the second cell is a genuine short D2C cell and

\[
W(D)>0.
\]

---

## 4. Sign at the lower endpoint

At `D=D_-`, equation (3.1) gives

\[
4k\delta+\delta+\Delta_2/2=\pi/2.
\tag{4.1}

Put

\[
a:=2k\delta.
\]

Then

\[
a+\Delta_2/2=\pi/2-a-\delta,
\]

so

\[
\cos(a+\Delta_2/2)=\sin(a+\delta).
\]

Therefore

\[
\begin{aligned}
\mu_k(D_-)
&=\frac{\sin a\sin(a+\delta)}{D_-\cos\delta}\\
&=\frac{\cos\delta-\cos(2a+\delta)}{2D_-\cos\delta}.
\end{aligned}
\tag{4.2}

Equation (4.1) also gives

\[
0<2a+\delta<\pi/2,
\]

hence

\[
\cos(2a+\delta)>0.
\]

Thus

\[
\boxed{
\mu_k(D_-)<\frac1{2D_-}.
}
\tag{4.3}

At the lower cell boundary `G_2=2delta`,

\[
\begin{aligned}
W(D_-)^2
&=1-D_-^2\sin^2\delta\\
&=1-\cos^2(\delta/2)\\
&=\sin^2(\delta/2),
\end{aligned}
\]

using

\[
2D_-\sin(\delta/2)=1.
\]

Hence

\[
\boxed{W(D_-)=\frac1{2D_-}.}
\tag{4.4}

Combining (4.3)-(4.4),

\[
\boxed{
\mu_k(D_-)-W(D_-)<0.
}
\tag{4.5}

---

## 5. Sign at the upper endpoint

At `D=D_+`,

\[
G_2=\Delta_2,
\]

so D2C gives

\[
\boxed{W(D_+)=0.}
\tag{5.1}

Equation (3.2) is

\[
8k\delta+2\Delta_2=\pi,
\]

hence

\[
2k\delta+\Delta_2/2=\pi/4.
\tag{5.2}

Also

\[
0<2k\delta<\pi/4.
\]

Therefore both factors in the numerator of (2.7) are positive and

\[
\boxed{\mu_k(D_+)>0=W(D_+).}
\tag{5.3}

---

## 6. Intermediate value gives an interior PS root

The functions

\[
\delta(D),\quad\Delta_2(D),\quad G_2(D),\quad\mu_k(D),\quad W(D)
\]

are continuous on the closed admissible interval `[D_-,D_+]`.

Sections 4-5 give opposite signs for

\[
f_k(D):=\mu_k(D)-W(D)
\]

at its endpoints. Hence by the intermediate value theorem there is

\[
\boxed{D_k\in(D_-,D_+)}
\tag{6.1}

with

\[
f_k(D_k)=0.
\]

At this root,

\[
2\delta<G_2<\Delta_2,
\]

so `W>0` and the second cell is strictly short. Equation (2.6) gives the exact bisector direction, and choosing the opposite D2C midpoint-offset sign makes

\[
M-W e^{i\phi_2}=0.
\]

This is the complete complex SCE equation.

Thus PSR is proved for every `k>=1`. `square`

---

## 7. First numerical values, for regression only

The theorem does not depend on numerical root finding. For orientation, the first few roots are approximately

```text
k=1, q=12:  D_1 = 3.8388448948514875...
k=2, q=20:  D_2 = 6.37530877418456...
k=3, q=28:  D_3 = 8.9185745201426...
k=4, q=36:  D_4 = 11.46350241188385...
```

These values are included only to make later computational shell reconstruction reproducible.

---

## 8. Scope and regression audit

### This is an SCE theorem, not yet a full-source construction

PSR proves exact solutions of the complete two-staircase **shell closure equations** in the PS regime. It does not by itself claim that every reconstructed polygon has no unintended shorter-than-unit chord, no unintended diameter chord, or the required positive PSD KKT stress. Those properties are separate geometric/mechanical checks.

The `q=12` root has already been reconstructed numerically and passes all of them; a separate audited report/script should handle the infinite family before any stronger claim is promoted.

### P2 exclusion

No conflict. PSR has one genuine short cell with `W>0`; P2X only excludes the double-parallel case `W_1=W_2=0`.

### SSR/Reinhardt boundary

The family approaches a DGE/Reinhardt-type boundary at the short cell, but every finite root lies strictly inside the PS interval by (6.1).

### Arbitrary Littlewood words

None are used. The special repeated word has the exact closed form (1.1), and its phase alignment with the short-cell bisector is exact.

---

## 9. What this changes

P2X removed the easiest `d_H=2` branch. PSR immediately shows that the next strategy cannot be

> prove the exact PS/S2 SCE system has no positive-defect solution.

That statement is false for infinitely many shell cardinalities already at the exact SCE level.

The next task is sharper:

1. reconstruct the PSR roots as actual convex equilateral shells and prove the full distance graph is exactly the intended PS graph; then
2. determine whether the unique D2 mixed self-stress has the required positive signs and rank-`q-3` PSD matrix throughout the family.

If both hold for arbitrarily large `k`, shell geometry + KKT is asymptotically nonclosing and the proof must use the `Theta(D^2)` force-invisible interior population/global optimality.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For every k>=1 set q=8k+4, LA=LB=4k and both staircase words eps=(-,+,+,-)^k.
Let delta=2asin(1/(2D)), Delta=2asin(1/D), set G1=Delta and
  G2=pi-8k delta-Delta.
The repeated Littlewood polynomial is
  P=(z-1)(1-z^(4k))/(1+z^2), z=e^(i delta),
and exactly
  P=[sin(2k delta)/(D cos delta)] exp(i(2k-1/2)delta).
Thus the two staircase midpoint sum has exactly the second-cell bisector phase and
magnitude
  mu=sin(2k delta) cos(2k delta+Delta/2)/(D cos delta).
PS SCE reduces to mu=W, W=sqrt(1-D^2 sin^2(G2/2)).

Let D_- solve (8k+2)delta+Delta=pi (G2=2delta) and D_+ solve
8k delta+2Delta=pi (G2=Delta). Then D_-<D_+.
At D_-:
  W=1/(2D),
  mu=[cos delta-cos((4k+1)delta)]/(2D cos delta)<1/(2D).
At D_+:
  W=0<mu.
IVT gives D_k in (D_-,D_+) with exact SCE closure and genuine short second cell.

Next: prove full reconstructed shell + distance graph + positive PSD KKT for this infinite family.
```
