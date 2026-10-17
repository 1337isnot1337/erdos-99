> Generated reading edition · [exact source](../../research/target_c_section119_analytic_slack_envelope.md) · source SHA-256 `0106983a68527ed6378532703fd5b7a3aeefd435ba942fc6f518981b3fb770fa`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — Section 119: analytic optimization of the correlated bad-direction slack

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate stacked on Section 118.

Section 118 restores the exact Section-101 slack decomposition

```math
\sigma=x+y+z+w,
```

and proves the directional bad-train estimate

```math
B(x,y,z,w)
\le Q_{tooth}(y)+y+{3\over2}x+15z+{35\over3}w.
```

That theorem then deliberately relaxes everything to
`Q_tooth(sigma)+15sigma`.  The exact four-variable linear part can instead be
optimized analytically.  The result is still one-dimensional and does not require a
numerical simplex solver.

The safe explicit consequence is

```math
\boxed{\sigma(\theta)\le0.0073}
```

with proof-only carrier coefficient

```math
\boxed{
\mu_{22}=0.9762093528016385\ldots .
}
```

The corresponding coarse analytic envelope is

```math
\boxed{
\sigma_{22,\rm env}=0.007323817327\ldots,
\qquad
\mu_{22,\rm env}=0.976209901782\ldots .
}
```

No theorem-state mutation is proposed.

---

## 119.1 Start from the exact correlated bad-end bound

Use Section 118's nonnegative slacks

```math
x=U-|S|,
\qquad
y=|S|-2\alpha,
\qquad
z=2\alpha-C,
\qquad
w=C-M,
```

so

```math
\boxed{x+y+z+w=\sigma.}
\tag{119.1}
```

Its proof gives

```math
\boxed{
B(x,y,z,w)
\le Q_{tooth}(y)+y+{3\over2}x+15z+{35\over3}w,
}
\tag{119.2}
```

where `Q_tooth(t)` is the unique nonnegative solution of

```math
\boxed{
F(Q):=\sin Q+\sqrt3(1-\cos Q)-Q={t\over2}.
}
\tag{119.3}
```

For fixed `y`, the remaining slack is `sigma-y`.  Among the coefficients of `x,z,w`
in (119.2), the largest is the coefficient `15` of `z`.  Therefore

```math
{3\over2}x+15z+{35\over3}w
\le15(x+z+w)=15(\sigma-y),
```

and hence

```math
\boxed{
B(x,y,z,w)
\le15\sigma+H(y),
\qquad
H(y):=Q_{tooth}(y)-14y.
}
\tag{119.4}
```

Thus the exact four-slack optimization reduces immediately to one scalar function.

## 119.2 `H(y)` has a unique universal maximum

Differentiate the inverse relation (119.3).  On the relevant interval
`0<Q<pi/3`,

```math
F'(Q)
=\cos Q+\sqrt3\sin Q-1
=:\psi(Q)>0.
```

Therefore

```math
Q_{tooth}'(y)={1\over2\psi(Q_{tooth}(y))}.
\tag{119.5}
```

Also

```math
\psi'(Q)=-\sin Q+\sqrt3\cos Q>0
```

for `0<Q<pi/3`.  Hence `Q_tooth'(y)` is strictly decreasing, so

```math
H'(y)=Q_{tooth}'(y)-14
```

is strictly decreasing.  It starts positive as `y->0+` and is eventually negative.
Consequently `H` has one global maximum on the relevant interval.

The maximizing point is characterized exactly by

```math
Q_{tooth}'(y_*)=14,
```

or equivalently

```math
\boxed{
\cos Q_*+\sqrt3\sin Q_*-1={1\over28}.
}
\tag{119.6}
```

Then

```math
y_*=2F(Q_*).
\tag{119.7}
```

The regression certificate gives

```math
\boxed{
\begin{aligned}
Q_*&=0.0207453732819050\ldots,\\
y_*&=0.000742420858663266\ldots,\\
K_*:=H(y_*)&=0.0103514812606193\ldots .
\end{aligned}}
\tag{119.8}
```

Therefore, for **every** nonnegative slack allocation satisfying (119.1),

```math
\boxed{
B(x,y,z,w)
\le15\sigma+K_*.
}
\tag{119.9}
```

For `sigma>=y_*` this bound is sharp for the relaxed bad-end expression (119.2): take
`y=y_*`, `z=sigma-y_*`, and `x=w=0`.

No black-box optimization is present in (119.9).

## 119.3 Keep the remaining Section-118 estimates conservative

As in Section 118, use the one-variable circular-segment area floor

```math
A(\sigma)
={\pi\over4}
-G(\theta)
-2G\left(\phi_8+{13\sigma\over3}\right)
-G\left({13\sigma\over3}\right),
\tag{119.10}
```

where `G(t)=(t-sin t)/8`.

Also keep the conservative train ceiling

```math
{T_D\over D}
\le C_T(\sigma)+o(1),
\qquad
C_T(\sigma)=U(\theta)+2\sigma,
\tag{119.11}
```

and the conservative principal-route excess budget

```math
E_D/D\le\sigma+o(1).
\tag{119.12}
```

The signed-return area-transport theorem and diffuse-bad-train estimate therefore imply
the necessary scalar inequality

```math
\boxed{
\lambda\sigma
\ge
(2-\sqrt3)
\left[
A(\sigma)
-2C_T(\sigma)(15\sigma+K_*)
\right]_+,
}
\tag{119.13}
```

where

```math
\lambda=\sin(\theta/2).
```

This theorem is intentionally weaker than a full optimization of the exact product
`T_D B`; it only optimizes the bad-end term analytically while retaining the old scalar
upper bounds for `T_D` and `E_D`.

## 119.4 Contradiction at `sigma=0.0073`

Let `theta_22` solve

```math
\sigma(\theta_{22})=0.0073.
```

Then

```math
\boxed{
\theta_{22}=2.704460337165959\ldots,
\qquad
\mu_{22}=\sin(\theta_{22}/2)
=0.9762093528016385\ldots .
}
\tag{119.14}
```

The stability proof retains large room:

```math
{10\over3}\sigma=0.0243333\ldots<0.1,
```

```math
{13\over3}\sigma=0.0316333\ldots
<\phi=0.8742646\ldots,
```

and

```math
U+{13\over3}\sigma
=1.86182903765\ldots<\pi.
```

At this endpoint,

```math
\boxed{
\begin{aligned}
A&=0.4702300098665401\ldots,\\
C_T&=1.844795704318292\ldots,\\
B_*&:=15\sigma+K_*
=0.1198514812606193\ldots .
\end{aligned}}
\tag{119.15}
```

Hence

```math
\boxed{
A-2C_TB_*
=0.0280270142949906\ldots>0.
}
\tag{119.16}
```

The signed-return theorem forces normalized route excess at least

```math
\boxed{
{2-\sqrt3\over\mu_{22}}
\left(A-2C_TB_*\right)
=0.00769283333031559\ldots .
}
\tag{119.17}
```

This is larger than the available `0.0073` by

```math
\boxed{3.92833330316\times10^{-4}.}
\tag{119.18}
```

Thus no full-core Type-II countersequence can have every positive-area macroscopic
harmonic carrier of normalized diameter at most `mu_22`.

The standard finite-macroscopic-cell transfer yields a quadratic-area locally
rhombus-saturated carrier `P_*` with

```math
\boxed{
\operatorname{diam}(P_*)
\ge(0.9762093528016385\ldots-o(1))D.
}
\tag{119.19}
```

## 119.5 Analytic correlated envelope

Define

```math
H_{119}(s)
={2-\sqrt3\over\lambda(s)}
\left[
A(s)-2C_T(s)(15s+K_*)
\right]-s.
\tag{119.20}
```

On the present neighborhood, `A` decreases while `lambda`, `C_T`, and `15s+K_*`
increase.  Hence `H_119` is strictly decreasing while the bracket is positive.

The unique zero above the safe endpoint is

```math
\boxed{
\sigma_{22,\rm env}
=0.007323817327\ldots .
}
\tag{119.21}
```

At that point,

```math
\boxed{
\mu_{22,\rm env}
=0.976209901782\ldots .
}
\tag{119.22}
```

This is still not the final correlated-slack envelope.  The exact train ceiling is
`U-x-y+2z`, the principal-route excess is `z`, and the area floor can also use the
actual `x,w` rather than the total `sigma`.  A later compact optimization can retain
those correlations.  Section 119 deliberately stops before that step so the theorem
remains analytically transparent.

## 119.6 Scope

The proof uses the finite signed-return/area-transport theorem from Section 117 and the
exact correlated leakage formula from Section 118.  It does not introduce a new
geometric lemma; its new content is the exact analytic optimization (119.4)--(119.9).

No source point is deleted.  Hole and bridge boundary data remain occurrence-counted.
The separate inactive-container branch is untouched.

**Theorem state:** unchanged.  C-II and LEVEL I remain open.
