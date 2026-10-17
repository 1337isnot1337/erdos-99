> Generated reading edition · [exact source](../../../docs/reports/target_c_chord_moment_joint_floor_0669308_2026-09-10.md) · source SHA-256 `e525399ec45d491cd9ef9c0ad4ca9f031ef162d17a7d02bf9938cabca46b7dfc`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-D791B0FC9B9E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic chord cubic capacity raises the post-ZF floor to 0.669309

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`, after CM  
**Run type:** exact asymptotic inequality synthesis  
**Target:** Target C, C-II after ZF/DB/FS/MA/JC/DD/CC/CM  
**External web search:** not used  
**Computation:** decimal evaluation only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

The universal cyclic chord-cubic theorem CM substantially reduces the only quadratic
outer-pocket capacity available to a post-ZF survivor. Combined with MA/GU/CC and the
independent MA/JC threshold, it gives

```math
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{CMJC}
=0.6693086716797393537\ldots .
}
\tag{CJ2.1}
```

The constant is the unique crossover of two monotone analytic threshold functions. No
numerical optimization is a proof input.

---

## 1. Defect-aware CM capacity

Pass to a convergent survivor subsequence and put

```math
\lambda=\lim\frac{e_{BB}+2s_C}{D},
\qquad
y=\lim\frac hD,
\qquad
z=\lim\frac{Q+2s_Z}{D}.
```

DB gives

```math
y\ge2\rho,
\qquad
0\le z\le u(y):=y-2\cos(y/2).
\tag{1.1}
```

MA and GU give

```math
\boxed{
\liminf\frac GD^2
\ge
\Phi(y)-\frac\pi4\lambda^2,
\qquad
\Phi(y)=\frac{y+\sin y}{4}.
}
\tag{1.2}
```

CM and CC give

```math
\boxed{
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le
C(y,z),
}
\tag{1.3}
```

where

```math
\boxed{
C(y,z)=
\frac1{\sqrt6}
\left(2^{1/3}\cos(y/2)+u(y)-z\right)^{3/2}
\sqrt{u(y)-z}
+\frac{z^2}{4\pi}.
}
\tag{1.4}
```

Since `G<=H_out+A_exc+O(D)`, every survivor limit satisfies

```math
\Phi(y)-\frac\pi4\lambda^2\le C(y,z).
\tag{1.5}
```

---

## 2. On the critical interval the worst defect is z=0

Take

```math
I=[2\rho,17/10].
```

For `y in I`, the elementary estimate

```math
\cos(y/2)\ge\cos(17/20)>1-(17/20)^2/2>3/5
```

gives

```math
0\le u(y)<1/2.
\tag{2.1}
```

Fix `y` and write

```math
A=2^{1/3}\cos(y/2),
\qquad
w=u(y)-z.
```

The outer term in (1.4) is

```math
O(w)=\frac1{\sqrt6}(A+w)^{3/2}w^{1/2}.
```

For `w>0`,

```math
O'(w)=
\frac1{2\sqrt6}(A+w)^{1/2}w^{-1/2}(A+4w)
>\frac{A}{2\sqrt6}.
\tag{2.2}
```

Since `A>3/5` and `sqrt6<5/2`,

```math
O'(w)>3/25.
\tag{2.3}
```

The exceptional-face derivative is

```math
\frac{d}{dz}\frac{z^2}{4\pi}=\frac z{2\pi}
<\frac1{12}
\tag{2.4}
```

by (2.1) and `pi>3`. Therefore

```math
\frac{\partial C}{\partial z}
=-O'(w)+\frac z{2\pi}
<-\frac3{25}+\frac1{12}<0.
\tag{2.5}
```

So

```math
\boxed{
\max_{0\le z\le u(y)}C(y,z)=C(y,0)
}
\tag{2.6}
```

throughout the critical interval.

Define

```math
H_C(y)=
\frac1{\sqrt6}
\left(2^{1/3}\cos(y/2)+u(y)\right)^{3/2}
\sqrt{u(y)}
\tag{2.7}
```

and, whenever the radicand is nonnegative,

```math
\boxed{
T_C(y)=
\sqrt{\frac4\pi\,[\Phi(y)-H_C(y)]}.
}
\tag{2.8}
```

Then every survivor with `y in I` satisfies `lambda>=T_C(y)` when the latter is real;
if its radicand is negative, this condition is vacuous.

---

## 3. The CM threshold decreases

Put

```math
A(y)=2^{1/3}\cos(y/2),
\qquad
B(y)=A(y)+u(y).
```

We have

```math
u'(y)=1+\sin(y/2)>1
```

and, because `2^{1/3}<2`,

```math
B'(y)=1+\left(1-2^{1/3}/2\right)\sin(y/2)>1.
\tag{3.1}
```

Differentiate (2.7). Dropping no negative terms gives

```math
H_C'(y)>
\frac{\sqrt B}{2\sqrt6}
\left(3\sqrt u+\frac{B}{\sqrt u}\right).
\tag{3.2}
```

AM--GM yields

```math
3\sqrt u+\frac B{\sqrt u}\ge2\sqrt{3B},
```

hence

```math
\boxed{H_C'(y)>\frac B{\sqrt2}.}
\tag{3.3}
```

On `I`, `2^{1/3}>5/4` and `cos(y/2)>3/5`, so `B>A>3/4`. Thus

```math
H_C'(y)>\frac3{4\sqrt2}>\frac12.
\tag{3.4}
```

But

```math
0\le\Phi'(y)=\frac{1+\cos y}{4}\le\frac12.
```

Therefore

```math
\boxed{[\Phi(y)-H_C(y)]'<0.}
\tag{3.5}
```

So the nonnegative threshold obtained from (2.8) is strictly decreasing until its
radicand vanishes.

---

## 4. The independent MA/JC threshold increases

MAJC proves the independent necessary condition

```math
\boxed{\lambda\ge R(y),}
\tag{4.1}
```

where `R(y)` is the positive root of

```math
\boxed{
(\pi^2+1)R^2
+4\cos(y/2)R
+4\cos^2(y/2)
-\pi(y+\sin y)=0,
}
\tag{4.2}
```

and `R` is strictly increasing for every `y>=2rho`.

At `y=2rho`, `u=0`, so `H_C=0`. The exact MAJC root identity gives

```math
R(2\rho)<T_C(2\rho).
\tag{4.3}
```

At `y=17/10`, the inequalities reverse. We give rational certificates.

Let `x=17/20`. Alternating Taylor gives

```math
\cos x<1-x^2/2+x^4/24<661/1000,
\tag{4.4}
```

and

```math
\sin(17/10)>17/10-(17/10)^3/6+(17/10)^5/120-(17/10)^7/5040>99/100.
\tag{4.5}
```

Using `pi<22/7` in positive terms and `pi>3141/1000` in the negative term, substitution
of `R=2/3` into the left side of (4.2) gives

```math
Q_R(17/10,2/3)
<-\frac{23036123}{220500000}<0.
\tag{4.6}
```

Since `Q_R` increases in `R`,

```math
\boxed{R(17/10)>2/3.}
\tag{4.7}
```

For the CM threshold, (4.4) implies

```math
u(17/10)>189/500>(61/100)^2.
\tag{4.8}
```

Also `2^{1/3}>5/4` and `cos x<2/3`, so

```math
B(17/10)
=17/10-(2-2^{1/3})\cos x
>6/5.
\tag{4.9}
```

Since `sqrt5<56/25`, (4.8)--(4.9) give

```math
H_C(17/10)
>
\frac1{\sqrt6}(6/5)^{3/2}(61/100)
=
\frac{183}{250\sqrt5}
>\frac{183}{560}.
\tag{4.10}
```

Using only `sin(17/10)<1`,

```math
\Phi(17/10)<27/40.
```

Therefore

```math
\Phi(17/10)-H_C(17/10)
<\frac{39}{112}
<\frac\pi9,
\tag{4.11}
```

where the last inequality follows from `pi>3141/1000`. Thus, whether or not the
radicand in (2.8) is positive,

```math
\boxed{T_C(17/10)<2/3<R(17/10).}
\tag{4.12}
```

---

## 5. Unique crossover and global floor

By continuity, strict increase of `R`, and strict decrease of the CM threshold, there is
a unique

```math
\boxed{y_C\in(2\rho,17/10)}
```

such that

```math
\boxed{R(y_C)=T_C(y_C).}
\tag{5.1}
```

Every survivor with `y in I` satisfies

```math
\lambda\ge\max\{R(y),T_C(y)\},
```

whose minimum is the crossover value

```math
\boxed{\lambda_{CMJC}:=R(y_C)=T_C(y_C).}
\tag{5.2}
```

For `y>=17/10`, monotonicity gives

```math
\lambda\ge R(y)>R(y_C),
```

so (5.2) is the global post-ZF threshold. This proves CJ2.1. `square`

---

## 6. Numerical evaluation and endpoint structure

Evaluation of the analytic crossover gives

```math
\boxed{y_C=1.6864987133137823283\ldots,}
```

```math
\boxed{\lambda_{CMJC}=0.6693086716797393537\ldots .}
```

At the crossover,

```math
u(y_C)=0.3564193225522907919\ldots,
```

```math
\cos(y_C/2)=0.6650396953807457682\ldots,
```

and

```math
H_C(y_C)=0.3181151302082901501\ldots .
```

Every sequence approaching this endpoint must have

```math
\frac hD\to y_C,
\qquad
\frac{Q+2s_Z}{D}\to0.
\tag{6.1}
```

The independent MA/JC equality forces

```math
\frac{P_F}{D}\to p_0(y_C),
\qquad
\frac{e_{BB}}D\to\lambda_{CMJC},
\qquad
\frac{s_C}{D}\to0.
\tag{6.2}
```

Thus MA perimeter equality again gives exactly one projective missing circle interval.
This makes the CM scalar Minkowski relaxation non-sharp: the chord vector has two equal
macroscopic entries, while equality in the detour `l^3<=l^1` step would concentrate all
detour in one pocket. The endpoint is therefore expected to be excluded by a direct
one-gap moment audit.

---

## 7. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| defect maximum at `z=0` on the critical interval | proved | derivative gap `3/25>1/12` |
| CM threshold decreases | proved | derivative lower bound `H_C'>B/sqrt2>1/2` |
| endpoint sign at `17/10` | proved | rational Taylor certificates |
| unique crossover | proved | opposing monotone thresholds |
| explicit floor `0.6693086716...` | proved asymptotically | analytic crossover |
| endpoint exclusion | not claimed here | handled by the next equality audit |
| Level I | still open | high-surplus sources remain possible under current inequalities |

---

## 8. Exact next implication

Do not treat `0.6693` as the objective. At equality, MA gives one projective gap and
therefore exactly two macroscopic force-hull chord entries. The CM proof can only be
sharp if the chord and detour vectors are proportional in Minkowski and the detour
cube norm equals its `l^1` norm. Those conditions are incompatible when the total
detour is positive. A direct proof excludes the entire CMJC endpoint class and yields a
uniform gap above CJ2.1.
