# Target C-II — phase-star residual stability raises the full-core floor to `1.84306`

**Date:** 2026-09-15  
**Status:** proof-only full-core Type-II strengthening  
**Dependencies:** corrected phase-star gap `0.00534`; phase-star residual stability; hostile-audited joint endpoint retention; hostile-audited complement rhombus incidence / restored dominant energy  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The previous restored-incidence argument treated the dominant exact-orbit lower bound
and the residual non-dominant rhombus budget as two independent consequences of a
generic two-bin estimate.  Near the phase-star endpoint they are not independent.
The phase-star capacity theorem forces the residual orbit mass to vanish linearly with
`U-C534`.

Keeping that correlation raises the safe proof-only full-core floor to

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.84306.
}
\tag{RF.1}

The proof is deliberately split into two stages.  First, the already-audited generic
energy/incidence inequalities localize every putative `t<=1.84306` survivor to
`U<1.911`.  Only then is the sharper phase-star residual theorem invoked.

---

## 1. Variables and matched endpoint

Write

\[
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\delta={d_{out}\over D},
\]

\[
U={9t\over2}-2\pi-2\delta-\kappa/2.
\tag{RF.2}

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
C_{534}=2\sqrt{\Delta_2}+0.00534.
\tag{RF.3}

The corrected phase-star theorem gives

\[
U\ge C_{534}.
\tag{RF.4}

Let

\[
F(z)=z-6\sin(z/6).
\tag{RF.5}

---

## 2. Stage A: localize a putative `t<=1.84306` survivor to `U<1.911`

The generic two-bin / restored-incidence stack remains valid after replacing its older
matched floor by the stronger `C534`.  Set

\[
T_0=1.84306,
\qquad
U_{max}={9T_0\over2}-2\pi,
\]

\[
\delta_{max}={U_{max}-C_{534}\over2}.
\]

For

\[
m_2(U)={U+\sqrt{8\Delta_2-U^2}\over2},
\qquad
r_2(U)=U-m_2(U),
\]

the shared-retention and complement-incidence inequalities give

\[
z+p\ge
\pi-U-{t+\kappa\over2}+m_2(U)-o(1),
\tag{RF.6}

\[
p\le
{\delta-F(z)+r_2(U)^2\over2(1-\delta)}+o(1),
\tag{RF.7}

and the dominant selected edge energy gives

\[
\delta\ge F(z)-o(1).
\tag{RF.8}

Exactly as in the dominant-double-outer bootstrap, if `z>=z_j-o(1)`, then
`delta>=F(z_j)-o(1)`, hence

\[
U\le U_j:=U_{max}-2F(z_j)+o(1).
\]

Monotonicity of `m_2`, `r_2`, and the retained-mass lower bound gives one explicit
bootstrap step.  The exact outward certificate proves the four rounded implications

\[
0\Longrightarrow z>2.0782-o(1),
\]

\[
2.0782\Longrightarrow z>2.1915-o(1),
\]

\[
2.1915\Longrightarrow z>2.2098-o(1),
\]

\[
2.2098\Longrightarrow z>2.2129-o(1).
\tag{RF.9}

The final value and (RF.8) imply

\[
\boxed{U<1.910928+o(1)<1.911.}
\tag{RF.10}

Thus every putative survivor in the target interval lies inside the domain of the
phase-star residual-stability theorem.

---

## 3. Stage B: correlated residual bound

Let `M` be the dominant exact-orbit train mass.  The phase-star residual theorem gives,
throughout `C534<=U<=1.911`,

\[
\boxed{
R:=U-M\le c\,(U-C_{534}),
\qquad c=1.003.
}
\tag{RF.11}

For reference, its proof uses the physical one-orbit capacity `Psi`, the exact endpoint
strictness `Psi(C534)<Delta2`, the slope bound `Psi'>0.61`, and the generic preliminary
bound `R<0.007`.

Put

\[
h:=U-C_{534}\ge0,
\qquad
x:={\kappa\over2}\ge0.
\tag{RF.12}

Then

\[
R\le ch.
\tag{RF.13}

The complement complete-train count satisfies

\[
N_c
\le U+{t+\kappa\over2}-M
\le {t\over2}+x+ch.
\tag{RF.14}

Joint endpoint retention therefore gives

\[
\boxed{
z+p\ge
\pi-{t\over2}-x-ch-o(1).}
\tag{RF.15}

Likewise, the exact atomic mass outside the dominant orbit is at most `R<=ch`, so the
complement-rhombus incidence theorem improves to

\[
p(1-\delta)-{e_c\over2}
\le {c^2h^2\over2}+o(1).
\tag{RF.16}

The dominant and complement selected edge supports are disjoint, hence

\[
e_c\le\delta-F(z)+o(1).
\]

Thus

\[
\boxed{
p\le
{\delta-F(z)+c^2h^2\over2(1-\delta)}+o(1).}
\tag{RF.17}

Finally (RF.2) becomes the exact feasible-triangle identity

\[
\boxed{
2\delta+x+h
=R_t:= {9t\over2}-2\pi-C_{534}.
}
\tag{RF.18}

---

## 4. Eliminate `z` and maximize the survivor capacity

For fixed `t,h,x`, equation (RF.18) fixes `delta`.  Every survivor also obeys

\[
F(z)\le\delta.
\tag{RF.19}

On `0<=z<=pi`, define

\[
L(z)=
 z+{\delta-F(z)+c^2h^2\over2(1-\delta)}.
\]

Since

\[
F'(z)=1-\cos(z/6)
\le1-\frac{\sqrt3}{2}<0.134
\]

and `delta<0.051`,

\[
L'(z)=1-{F'(z)\over2(1-\delta)}>0.
\tag{RF.20}

Therefore the largest left side compatible with (RF.19) is obtained at

\[
z=Z(\delta):=F^{-1}(\delta).
\]

Equations (RF.15)--(RF.17) imply the necessary condition

\[
\boxed{
Q(t,h,x):=
Z(\delta)+{c^2h^2\over2(1-\delta)}
-\left(\pi-{t\over2}-x-ch\right)
\ge0.
}
\tag{RF.21}

We now maximize `Q` over the whole feasible triangle.

### `t` direction

At fixed `h,x`,

\[
{\partial\delta\over\partial t}={9\over4},
\]

so every `delta`-dependent term in (RF.21) increases with `t`, and the explicit `t/2`
term also increases.  Thus `Q` is increasing in `t`.  It is enough to check
`t=T0=1.84306`.

### `x` direction

Since `partial delta/partial x=-1/2`,

\[
{\partial Q\over\partial x}
=-{1\over2F'(Z)}
-{1\over2}{\partial\over\partial\delta}
\left[{c^2h^2\over2(1-\delta)}\right]
+1.
\]

Because `F'(Z)<0.134`, the first term is less than `-3.7`, while the middle term is
nonpositive.  Hence

\[
\boxed{Q_x<0.}
\tag{RF.22}

The largest survivor capacity occurs at `x=0`, i.e. `kappa=0`.

### `h` direction

At `x=0`, `partial delta/partial h=-1/2`.  Therefore

\[
Q_h
\le
-{1\over2F'(Z)}
+c+{c^2h\over1-\delta}.
\]

Stage A gives `h<1.04e-3` and `delta<0.051`, so

\[
Q_h<-3.7+1.003+0.0012<0.
\tag{RF.23}

Thus the largest survivor capacity occurs at

\[
\boxed{h=0.}
\tag{RF.24}

The entire correlated feasible region has collapsed to one corner:

\[
\kappa=0,
\qquad
U=C_{534},
\qquad
M=U,
\qquad
p\text{ has zero residual-rhombus allowance}.
\]

---

## 5. Exact corner contradiction

At `h=x=0`,

\[
\delta_0(t)
={1\over2}\left({9t\over2}-2\pi-C_{534}\right),
\tag{RF.25}

and the retained-mass requirement becomes

\[
z+p\ge\pi-{t\over2}.
\]

Equation (RF.17) has zero residual term.  Under the energy constraint `F(z)<=delta`,
the maximum possible `z+p` is reached at `F(z)=delta`, where the complement ceiling is
zero.  Thus every survivor necessarily satisfies

\[
\boxed{
\delta_0(t)
\ge F\left(\pi-{t\over2}\right).
}
\tag{RF.26}

The exact rational verifier

`research/verify_target_c_phase_star_residual_floor_184306.py`

uses Machin bounds for `pi`, integer-square-root bounds, and alternating-series bounds
for `sin`.  At

\[
t=1.84306
\]

it proves

\[
F\left(\pi-{t\over2}\right)
-\delta_0(t)
>2.1087\times10^{-6}>0.
\tag{RF.27}

This contradicts (RF.26).  Since `Q` increases with `t`, every smaller `t` is excluded
as well.

Therefore

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.84306.
}
\]

---

## 6. Frontier effect

The gain from `1.84289` to `1.84306` is numerically small, but the mechanism is new.
At the weakest low-`t` corner, the phase-star theorem now forces **all allowed atomic
mass into one exact three-phase orbit**.  Complement rhombus incidence has no
independent residual-orbit budget there.

This means further progress cannot come from repeatedly assigning a free two-bin
residual `r_2(U)` at the endpoint.  The live geometry is the single dominant exact
orbit together with its large outer-to-outer train population and boundary endpoint
order.

**Disposition:** proved proof-only full-core strengthening; C-II and Level I remain open.
