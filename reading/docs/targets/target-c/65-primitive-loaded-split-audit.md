> Generated reading edition · [exact source](../../../../docs/targets/target-c/65-primitive-loaded-split-audit.md) · source SHA-256 `d200d1bf676626677e901a3285898ad087f392f71d3f4c445334aa82e2ac8d5c`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 6 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — strengthened primitive loaded-boundary split

**Date:** 2026-09-11  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module combines two already canonical exact inequalities in a way that removes the
nonmatching-excess variable. The result strengthens Section 63's primitive split

```math
\liminf {\max\{e_{BB},x_B\}\over D}\ge\rho
```

to

```math
\boxed{
\liminf {\max\{e_{BB},x_B\}\over D}
\ge {4\rho\over3}
=0.9854468442\ldots ,
\qquad \rho=\cos\rho.
}
```

No new structural hypothesis is imposed. The theorem holds in both Woodall branches,
for arbitrary `s_Z>=0`, and retains every contact-isolated source point.

---

# 65. A near-unit primitive boundary currency is unavoidable

Use the canonical post-ZF notation

- `q`: loaded force-hull vertices;
- `h`: actual loaded diameter edges;
- `e_BB`: unit contacts between loaded vertices;
- `x_B=b-q`: outer contact-walk excess;
- `Q`: bounded exceptional-face defect;
- `s_Z=e+h-(2v-2)>=0`;
- `a_D=asin(1/(2D))`.

Set

```math
r_H:=2h-q.
\tag{65.1}
```

Section 61 gives the exact defect identity

```math
\boxed{r_H=x_B+Q+2s_Z.}
\tag{65.2}
```

Section 63 gives the exact loaded-hull inequality

```math
\boxed{e_{BB}+x_B\ge q.}
\tag{65.3}
```

Section 59 gives the exact defect-sensitive difference-body inequality

```math
\boxed{
Q+2s_Z
\le h+1-2D\cos((h-1)a_D).
}
\tag{65.4}
```

These three statements already force a stronger primitive split.

## 65.1 Two lower bounds for the same maximum

Put

```math
M:=\max\{e_{BB},x_B\}.
```

From (65.3),

```math
M\ge {e_{BB}+x_B\over2}\ge {q\over2}.
```

Since `q=2h-r_H`,

```math
\boxed{M\ge h-{r_H\over2}.}
\tag{65.5}
```

On the other hand, (65.2) and (65.4) give

```math
\begin{aligned}
x_B
&=r_H-(Q+2s_Z)\\
&\ge r_H-h-1+2D\cos((h-1)a_D).
\end{aligned}
```

Therefore

```math
\boxed{
M\ge r_H-h-1+2D\cos((h-1)a_D).
}
\tag{65.6}
```

The first lower bound decreases with `r_H`; the second increases with it. A fixed
weighted average cancels `r_H` exactly. Since `M>=A` and `M>=B` imply
`M>=(2A+B)/3`, equations (65.5)-(65.6) yield the finite theorem

```math
\boxed{
M
\ge
{h-1+2D\cos((h-1)a_D)\over3}.
}
\tag{65.7}
```

No optimization or limiting argument is used in (65.7).

## 65.2 Asymptotic constant

Consider an arbitrary unbounded survivor sequence. The diameter graph has `h<=q`, and
Cauchy's perimeter-diameter inequality gives `q<=pi D`; hence `h/D` is bounded.
Pass to any subsequence on which

```math
{h\over D}\to y.
```

Canonical Section 59 gives

```math
\liminf {h\over D}\ge2\rho,
\qquad \rho=\cos\rho,
\tag{65.8}
```

so every such limit has `y>=2rho`. Also `y<=pi`. Since

```math
a_D={1\over2D}+O(D^{-3}),
```

we have

```math
(h-1)a_D\to {y\over2}.
```

Divide (65.7) by `D`:

```math
\liminf {M\over D}
\ge
{y+2\cos(y/2)\over3}.
\tag{65.9}
```

The function

```math
\phi(y):={y+2\cos(y/2)\over3}
```

is nondecreasing on `[0,pi]`, because

```math
\phi'(y)={1-\sin(y/2)\over3}\ge0.
```

Its minimum on `[2rho,pi]` is therefore attained at `y=2rho`. Using
`rho=cos rho`,

```math
\phi(2rho)
={2rho+2\cos rho\over3}
={4rho\over3}.
```

Hence every unbounded post-ZF survivor sequence satisfies

```math
\boxed{
\liminf_{D\to\infty}
{\max\{e_{BB},x_B\}\over D}
\ge {4\rho\over3}.
}
\tag{65.10}
```

Numerically

```math
{4\rho\over3}=0.9854468442\ldots .
```

This strictly improves the Section 63 lower bound `rho=0.739085...` without any new
geometric input.

## 65.3 Structural trichotomy in the high-outer-walk branch

Section 63 writes

```math
x_B=m+u_B,
\tag{65.11}
```

where `m` is the number of nonunit sides of the loaded convex polygon and `u_B>=0`
is outer-walk excess beyond the one mandatory excess occurrence for each such side.
Thus (65.10) gives the explicit asymptotic trichotomy

```math
\boxed{
\max\left\{e_{BB},m,u_B\right\}
\ge {2\rho\over3}D-o(D)
=0.4927234221\ldots D-o(D).
}
\tag{65.12}
```

Indeed, if the maximum in (65.10) is achieved by `e_BB`, the stronger bound holds on
`e_BB`; otherwise `m+u_B=x_B>=(4rho/3-o(1))D`, so one of `m,u_B` is at least half.

This separates the next geometric attack into three concrete objects:

1. a near-unit linear count of loaded-loaded contacts;
2. linearly many nonunit loaded hull sides, each requiring an outer contact detour;
3. linearly many excess outer-walk occurrences beyond those mandatory one-per-side
   detours, which must be carried by deeper detours or articulation/bridge repetition.

## 65.4 Interaction with the renormalized surplus

Section 63 also gives

```math
e_{BB}+2s_C-3(d_H+s_Z)
=x_B+Q+s_C-c_I-2.
\tag{65.13}
```

The new split does not replace the canonical `z_*>0.9604` renormalized-surplus theorem:
the two results control different currencies. Instead they show that even before
pinned self-stress is used, one of the two directly visible boundary currencies is
already at least `(4rho/3-o(1))D`.

This is useful numerically because

```math
{4\rho\over3}>0.9854>z_*>0.9604.
```

No implication between the two inequalities is asserted; the point is that the live
obstruction can no longer hide entirely in `s_C`, `Q`, or mixed-row defect while both
primitive boundary currencies stay below one unit per diameter scale.

## 65.5 Regressions and scope

- **Regular odd shell:** has `x_B=0` and `e_BB=q`, with `q/D->pi`; it satisfies the
  theorem comfortably.
- **Perfect matching:** already excluded asymptotically by Section 60; the finite
  inequality (65.7) remains valid before that exclusion.
- **Positive `s_Z`:** retained explicitly through (65.2)-(65.4).
- **Forest and Woodall-cyclic branches:** both covered.
- **Bridge excursions and articulation repetitions:** retained inside `x_B` and `u_B`.
- **Contact-isolated source points:** untouched; all statements concern the positive
  force-visible core but make no identification of its population with `n`.
- **KKT weights:** no individual coefficient lower bound is used or proved.
- **Rejected cyclic cap theorem:** not used.

## 65.6 Canonical effect

The primitive post-ZF boundary split is now

```math
\boxed{
\text{either }e_{BB}\ge(4\rho/3-o(1))D
\quad\text{or}\quad
x_B\ge(4\rho/3-o(1))D.
}
\tag{65.14}
```

Equivalently, after resolving the outer-walk currency,

```math
\boxed{
\text{either }e_{BB}\ge(4\rho/3-o(1))D,
\quad m\ge(2\rho/3-o(1))D,
\quad\text{or }u_B\ge(2\rho/3-o(1))D.
}
\tag{65.15}
```

The next theorem should attack one of these geometric branches directly. Pure scalar
optimization of the existing defect ledger is no longer the main obstruction.
