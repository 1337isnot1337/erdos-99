> Generated reading edition · [exact source](../../../docs/reports/target_c_paired_lens_surplus_09449_2026-09-10.md) · source SHA-256 `1ad9aeb13b962231f0a226ddde4484e8997412824680a0293794ad99e46fd8dd`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 4 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- theorem-state: {"artifact_id":"ART-1C94DE66CF87","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — paired-lens coupling raises the explicit C-II surplus floor to 0.944988

**Date:** 2026-09-10  
**Repository state:** branch `research/c99-c2-dpc-20260910-sol` after PP; contemporaneous `main` head `f977f2d0d25f5022c2a587e59cab38375d85caee`  
**Run type:** closing proof / coupled convex-geometric optimization  
**Target:** Target C, C-II after FS/MP/PP  
**External input:** none beyond the planar isoperimetric inequality already used in the project  
**Computation:** decimal evaluation of an analytically unique root only

## LEVEL I STATUS

`STILL OPEN`

PP treats the force-hull side budget and outer-pocket area as separate currencies. This report couples them exactly at quadratic scale.

For a pair of opposite outer pockets, let `T` be the sum of their old unit-chain lengths and let `2s` be the sum of the two equal limiting hull-chord lengths. Put

```math
p=\frac{2s}{T}\in[0,1].
```

The sharp pair-area coefficient is

```math
\boxed{
J(p)=
\begin{cases}
\dfrac1{4\pi},&0\le p\le 2/\pi,\\[1ex]
\dfrac{\theta-\sin\theta\cos\theta}{8\theta^2},
&2/\pi<p\le1,
\quad p=\dfrac{\sin\theta}{\theta},\ 0\le\theta<\pi/2.
\end{cases}
}
\tag{PL.1}
```

It is nonnegative, nonincreasing, and concave. If `cD` is the total macroscopic opposite-side chord cost and `tau D` the macroscopic pocket-chain budget, then

```math
\boxed{
\limsup\frac{H_{out}}{D^2}
\le\tau^2J(c/\tau).
}
\tag{PL.2}
```

while the same side cost forces

```math
\boxed{
\liminf\frac{area(F)}{D^2}
\ge A(c):=
\frac{\pi-r_c+\sin r_c}{4},
\qquad r_c=2\arcsin(c/2).
}
\tag{PL.3}
```

After exact exceptional-face elimination, every survivor limit with `lambda=(e_BB+2s_C)/D<1` must have some `c in [0,lambda]` satisfying

```math
\boxed{
A(c)-\frac\pi4\lambda^2
\le
\lambda^2J(c/\lambda).
}
\tag{PL.4}
```

For each `lambda`, the left-minus-right side has one global minimum. The unique threshold at which that minimum reaches zero is

```math
\boxed{
\lambda_{PL}=0.94498826734389577438\ldots .
}
\tag{PL.5}
```

Hence every post-ZF survivor sequence obeys

```math
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge\lambda_{PL}.
}
\tag{PL.6}
```

Unlike the PP endpoint, the PL equality normal form is not contradicted by the present ledgers: it consists of one macroscopic projective gap and one opposite pair of equal giant pockets whose limiting chains are circular Dido arcs. Level I therefore remains open.

## 1. Exact two-pocket extremal

For one pocket with chain length `ell` and chord `s`, let `D(ell,s)` denote the sharp Dido upper area from DI.1.

### Lemma PL.1 — sharp opposite-pair area

Let two pockets have a common chord length `s` and chain lengths `ell_1,ell_2`, with

```math
T=\ell_1+\ell_2,
\qquad p=2s/T.
```

Then

```math
\boxed{
area(P_1)+area(P_2)\le T^2J(p).
}
\tag{1.1}
```

#### Proof

If `p<=2/pi`, equivalently `s<=T/pi`, PP.2 already gives

```math
area(P_1)+area(P_2)\le T^2/(4\pi),
```

which is (1.1).

Assume `p>2/pi`, or `s>T/pi`. By DI.1,

```math
area(P_1)+area(P_2)
\le D(\ell_1,s)+D(T-\ell_1,s).
\tag{1.2}
```

For `ell>s`, define `theta(ell) in (0,pi)` by

```math
\frac{s}{\ell}=\frac{\sin\theta}{\theta}.
```

Differentiating the Dido formula at fixed `s` gives the exact identity

```math
\boxed{
\frac{\partial D}{\partial\ell}(\ell,s)
=\frac{\ell}{2\theta}
=\frac{s}{2\sin\theta}.
}
\tag{1.3}
```

At `ell=T/2`, the common Dido angle lies in `(0,pi/2)` because `p>2/pi`.

For `ell>T/2`, write `theta_1=theta(ell)>theta_2=theta(T-ell)`. The derivative of the right side of (1.2) is

```math
\frac s2\left(\frac1{\sin\theta_1}-\frac1{\sin\theta_2}\right).
\tag{1.4}
```

It is negative immediately to the right of `T/2`. It can never vanish later. Indeed, equality would require `sin theta_1=sin theta_2`. Since `theta_1>theta_2`, this would force

```math
\theta_1+\theta_2=\pi.
```

Then

```math
T
=s\left(\frac{\theta_1}{\sin\theta_1}
+
\frac{\theta_2}{\sin\theta_2}
\right)
=\frac{s\pi}{\sin\theta_1},
```

so `s/T<=1/pi`, contrary to `s>T/pi`. Thus (1.4) stays negative for all `ell>T/2`; by symmetry the maximum is at `ell_1=ell_2=T/2`.

Let `theta in (0,pi/2)` solve `p=sin theta/theta`. Substituting `ell_1=ell_2=T/2` into DI.2 gives

```math
2D(T/2,s)
=T^2\frac{\theta-\sin\theta\cos\theta}{8\theta^2}
=T^2J(p).
```

This proves (1.1). `square`

### Lemma PL.2 — concavity of the pair coefficient

`J` is nonnegative, nonincreasing, and concave on `[0,1]`.

#### Proof

It is constant on `[0,2/pi]`. In the lens range, use `p=sin theta/theta`. DI.2 gives

```math
\boxed{J'(p)=-\frac{\cos\theta}{4\theta}<0.}
\tag{1.5}
```

Moreover

```math
\frac{d}{d\theta}J'(p(\theta))
=\frac{\theta\sin\theta+\cos\theta}{4\theta^2}>0,
```

while

```math
\frac{dp}{d\theta}
=\frac{\theta\cos\theta-\sin\theta}{\theta^2}<0.
```

Thus `J''(p)<0`. At `p=2/pi`, the right derivative is zero, matching the constant branch. Hence `J` is globally concave. `square`

## 2. Global paired-lens envelope

Let `c` denote the total normalized chord cost of all positive macroscopic opposite-side pairs:

```math
c=\sum_j\frac{2s_j}{D}.
\tag{2.1}
```

A macroscopic pocket whose chord is `o(D)` is treated as a one-pocket group with chord cost zero; DI.1 gives the limiting coefficient `1/(4pi)=J(0)`.

### Theorem PL.3

If

```math
\frac{d_P}{D}\to\tau,
```

then

```math
\boxed{
\limsup\frac{H_{out}}{D^2}
\le\tau^2J(c/\tau).
}
\tag{2.2}
```

#### Proof

Discard pockets with `x_P<epsilon D`; as in DI.3 and PP.3 their total area is `O(epsilon D^2)+O(D)`. Pair the remaining positive-chord pockets by PP.1 and group every zero-chord macroscopic pocket separately.

For group `j`, let `T_jD` be its total chain length, let `c_jD` be its doubled common chord length (zero for a collapsed-chord singleton), and put `p_j=c_j/T_j`. Lemma PL.1 and the zero-chord Dido limit give

```math
\limsup\frac{H_{out}}{D^2}
\le\sum_jT_j^2J(p_j)+O(\epsilon).
```

Set `T=sum T_j` and `w_j=T_j/T`. Since `w_j^2<=w_j` and `J` is concave and nonnegative,

```math
\begin{aligned}
\sum_jT_j^2J(p_j)
&=T^2\sum_jw_j^2J(p_j)\\
&\le T^2\sum_jw_jJ(p_j)\\
&\le T^2J\left(\sum_jw_jp_j\right)\\
&=T^2J(c/T).
\end{aligned}
\tag{2.3}
```

The function `T^2J(c/T)` is increasing in `T` at fixed `c`, because

```math
\frac d{dT}\left[T^2J(c/T)\right]
=T\,[2J-pJ']>0.
```

The total retained macroscopic chain mass is at most `tau+o(1)`. Letting `epsilon downarrow0` proves (2.2). `square`

## 3. The same chord cost controls force-hull area

The PP projective-gap argument gives, with the **actual** macroscopic side cost `c`,

```math
\boxed{
\liminf\frac{area(F)}{D^2}
\ge A(c):=
\frac{\pi-r_c+\sin r_c}{4},
\qquad r_c=2\arcsin(c/2),
}
\tag{3.1}
```

whenever `c<2`. This follows because the area-defect function

```math
\varphi(c)=2\arcsin(c/2)-c\sqrt{1-c^2/4}
```

is increasing, convex, and superadditive, so for fixed total side cost the force-hull area is minimized by concentrating all macroscopic gap cost in one projective gap.

## 4. Exceptional faces still optimize at zero

Let

```math
\nu=\lim Q/D,
\qquad
\lambda=\lim(e_{BB}+2s_C)/D<1.
```

PC gives

```math
\tau+\nu\le\lambda.
```

For fixed `c`, PL.3 therefore gives the pocket upper bound

```math
(\lambda-\nu)^2J\left(\frac{c}{\lambda-\nu}\right).
\tag{4.1}
```

Add the exceptional-face term `nu^2/(4pi)`. We claim the maximum occurs at `nu=0`.

If `c/lambda<=2/pi`, use `J<=1/(4pi)`:

```math
(\lambda-\nu)^2J\left(\frac c{\lambda-\nu}\right)
+\frac{\nu^2}{4\pi}
\le
\frac{(\lambda-\nu)^2+\nu^2}{4\pi}
\le\frac{\lambda^2}{4\pi}
=\lambda^2J(c/\lambda).
\tag{4.2}
```

If `c/lambda>2/pi`, then `c/(lambda-nu)>2/pi` throughout the feasible interval. Let `T=lambda-nu`. In the lens branch a direct calculation from (1.5) gives

```math
\frac{\partial}{\partial T}
\left[T^2J(c/T)\right]
=\frac{T}{4\theta},
\tag{4.3}
```

where `theta<pi/2`. Also

```math
\nu\le\lambda-c
<\lambda\left(1-\frac2\pi\right)<\frac\lambda2,
```

using `pi<4`. Hence `T=lambda-nu>nu`, and

```math
\frac d{d\nu}
\left[
T^2J(c/T)+\frac{\nu^2}{4\pi}
\right]
=-\frac{T}{4\theta}+\frac\nu{2\pi}
<-\frac{T}{2\pi}+\frac\nu{2\pi}<0.
\tag{4.4}
```

Thus `nu=0` is again optimal. ZG yields

```math
\boxed{
\limsup\frac G{D^2}
\le\lambda^2J(c/\lambda).
}
\tag{4.5}
```

## 5. Coupled necessary inequality

GU gives the attachment-cell upper bound

```math
\limsup\frac{C_{att}}{D^2}
\le\frac\pi4\lambda^2.
```

Combining with (3.1) and (4.5), every survivor limit with `lambda<1` requires some `c in [0,lambda]` such that

```math
\boxed{
F_\lambda(c):=
A(c)-\frac\pi4\lambda^2
-\lambda^2J(c/\lambda)
\le0.
}
\tag{5.1}
```

## 6. Exact optimization in the side-cost variable

On `c/lambda<=2/pi`, `J` is constant and `A'(c)<0`, so `F_lambda` strictly decreases.

In the lens range, write

```math
\frac c\lambda=\frac{\sin\theta}{\theta},
\qquad 0<\theta<\frac\pi2.
```

The exact derivatives are

```math
A'(c)
=-\frac{c^2}{8\sqrt{1-c^2/4}},
\qquad
J'(c/\lambda)
=-\frac{\cos\theta}{4\theta}.
\tag{6.1}
```

Thus a stationary point satisfies

```math
A'(c)-\lambda J'(c/\lambda)=0.
```

Substituting `c/lambda=sin theta/theta` and simplifying gives the exact equivalent pair

```math
\boxed{
\lambda=2\theta\cot\theta,
\qquad
c=2\cos\theta.
}
\tag{6.2}
```

The function `2theta cot theta` is strictly decreasing from `2` to `0` on `(0,pi/2)`, since

```math
\frac d{d\theta}(2\theta\cot\theta)
=2\frac{\sin\theta\cos\theta-\theta}{\sin^2\theta}<0.
```

Hence for each `lambda in (0,1)` there is exactly one stationary point in the lens branch. The derivative is negative at the branch entrance and positive as `c->lambda`, so this stationary point is the unique global minimum.

For fixed `c`, `F_lambda(c)` is strictly decreasing in `lambda`, because

```math
\frac{\partial F_\lambda}{\partial\lambda}
=-\frac\pi2\lambda
-\lambda[2J-pJ']<0.
\tag{6.3}
```

Therefore

```math
m(\lambda):=\min_{0\le c\le\lambda}F_\lambda(c)
```

is strictly decreasing. It is positive for sufficiently small `lambda`, while at `lambda=1`, choosing `c=0` gives

```math
m(1)\le-\frac1{4\pi}<0.
```

So there is a unique threshold `lambda_PL in (0,1)` with `m(lambda_PL)=0`.

At the minimizer, put `theta=theta_*`. Since `c=2cos theta`,

```math
r_c=2\arcsin(c/2)=\pi-2\theta.
```

The threshold is therefore characterized by

```math
\boxed{
\lambda_{PL}=2\theta_*\cot\theta_*,
}
\tag{6.4}
```

where `theta_* in (0,pi/2)` is the unique solution of

```math
\boxed{
\frac{\theta+\sin\theta\cos\theta}{2}
=\pi\theta^2\cot^2\theta
+\frac{\cot^2\theta}{2}
(\theta-\sin\theta\cos\theta).
}
\tag{6.5}
```

Numerically,

```math
\boxed{
\begin{aligned}
\theta_*&=1.19397451295414573142\ldots,\\
\lambda_{PL}&=0.94498826734389577438\ldots,\\
c_*&=0.73593426396540645627\ldots,\\
r_*&=0.75364362768150177561\ldots .
\end{aligned}}
\tag{6.6}
```

Thus (5.1) is impossible for `lambda<lambda_PL`, proving PL.6.

## 7. Equality normal form

If a survivor sequence approaches `lambda_PL`, equality in the strict relaxations above forces

```math
\frac QD\to0,
\qquad
\frac{d_P}{D}\to\lambda_{PL},
\tag{7.1}
```

and PC then gives

```math
\frac{s_C}{D},\frac{d_H}{D},\frac{s_Z}{D},\frac{c_B}{D}\to0.
\tag{7.2}
```

Equality in the force-area concentration gives one macroscopic projective gap of angular size `r_*`, hence two opposite force-hull sides of normalized length

```math
\sin(r_*/2)=c_*/2.
\tag{7.3}
```

Equality in PL.3 forces one opposite pocket-pair to carry all macroscopic chain mass. Since `c_*/lambda_PL>2/pi`, Lemma PL.1 is in its lens branch, so the two giant chain lengths are equal:

```math
\frac{\ell_1}{D},\frac{\ell_2}{D}
\to\frac{\lambda_{PL}}2,
\tag{7.4}
```

and each chain is asymptotically a Dido circular arc with chord

```math
\frac{s_1}{D},\frac{s_2}{D}
\to\frac{c_*}{2}
\tag{7.5}
```

and half-angle `theta_*`.

This normal form is geometrically compatible with the currently proved local constraints. No contradiction is claimed.

## 8. Exact target implication

The explicit report-level lower bound advances to

```math
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge0.9449882673438957\ldots .
}
```

The live closing target is now the PL equality/high-surplus normal form. A theorem excluding the two-opposite-Dido-pocket normal form, or any universal upper bound below `lambda_PL`, closes this branch.

## 9. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| sharp pair coefficient PL.1 | proved finite | Dido + exact one-variable split derivative |
| concavity of `J` | proved | exact derivatives |
| global paired-lens envelope | proved asymptotically | MP pairing + truncation + Jensen |
| exceptional density `Q/D=0` in the relaxed optimum | proved | two-case exact derivative |
| unique side-cost minimizer | proved | stationary equations reduce to `lambda=2theta cot theta` |
| threshold `lambda_PL` | proved analytically; decimal evaluated numerically | unique monotone root |
| PL endpoint excluded | not proved | current local geometry permits the symmetric lens normal form |
| Level I | still open | high-surplus normal form survives |

## 10. Regressions

- Odd shells and dense isolated fillings remain compatible because the global contradiction still enters only through the FS/GU source comparison.
- Collapsed-chord giant pockets are retained by the `J(0)=1/(4pi)` branch.
- Macroscopic opposite pockets are treated at their sharp pair-Dido capacity rather than assumed small.
- No response-trace or conductance lower bound is used.

## 11. Canonical promotion recommendation

Hold as a report pending independent audit. The finite pair theorem and concavity are strong promotion candidates; the full threshold depends on the unpromoted FS/MP/PP/GU/ZG chain.

## 12. Next run

The PL endpoint forces `Q,s_C,d_H,s_Z,c_B=o(D)` and exactly one opposite pair of giant Dido pockets. The exact PC identities then imply that all remaining linear-density outer pockets have degree excess zero, hence are triangular two-contact-chain pockets. The next structural question is whether the resulting near-maximal diameter thrackle (`h=q-o(D)`) and the rounded force-hull arcs can support that many triangular notches without either an exact unit equilateral triangle or a strict diameter-improving rearrangement.
