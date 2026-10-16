# Target C-II — `g=0.0076` residual stability raises the full-core floor to `1.843555`

**Date:** 2026-09-15  
**Status:** proof-only full-core Type-II strengthening  
**Dependencies:** hostile-audited corrected `g=0.0076` one-orbit capacity; `g=0.0076` endpoint residual stability; hostile-audited joint endpoint retention; complement-rhombus incidence with restored dominant energy  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The generic restored-energy proof still allowed an independent two-bin residual orbit budget at the matched endpoint.  The `g=0.0076` physical orbit capacity rules that out: if

\[
U=C_{76}+h,
\qquad
C_{76}=2\sqrt{\Delta_2}+0.0076,
\]

then the total exact atomic mass outside the dominant orbit is at most

\[
1.05h.
\]

This single correlation improves both the complement complete-train count and the complement-rhombus incidence budget.  Propagating it through the whole feasible triangle gives

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.843555.}
\tag{RF76.1}

A non-load-bearing high-precision solve of the collapsed corner equation places the scalar crossing at

\[
1.843555705238933\ldots .
\]

Only the exact-rationally certified value `1.843555` is claimed.

---

## 1. Variables and correlated residual

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
\tag{RF76.2}

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
C_{76}=2\sqrt{\Delta_2}+0.0076.
\tag{RF76.3}

The matched atomic theorem gives

\[
U\ge C_{76}-o(1).
\tag{RF76.4}

Let `M` be the mass of the dominant exact `pi/3` orbit.  The endpoint residual-stability theorem proves, throughout `C76<=U<=2.013`,

\[
\boxed{
R:=U-M\le c(U-C_{76}),
\qquad c=1.05.}
\tag{RF76.5}

No preliminary localization is needed below: the entire target feasible triangle lies inside `U<2.013`.

---

## 2. Shared retention and incidence with one common slack

Set

\[
h:=U-C_{76}\ge0,
\qquad
x:={\kappa\over2}\ge0.
\tag{RF76.6}

Then (RF76.2) becomes

\[
\boxed{
2\delta+x+h
=R_t:={9t\over2}-2\pi-C_{76}.}
\tag{RF76.7}

The complement complete-train density is at most

\[
N_c
\le U+{t+\kappa\over2}-M
={t\over2}+x+R
\le {t\over2}+x+ch.
\]

The hostile-audited shared endpoint-retention theorem therefore gives retained dominant outer-occurrence mass `z` and retained complement O--O pair mass `p` satisfying

\[
\boxed{
z+p
\ge
\pi-{t\over2}-x-ch-o(1).}
\tag{RF76.8}

The complement-rhombus incidence theorem depends quadratically on the exact atomic mass outside the dominant orbit.  Equation (RF76.5) gives

\[
\boxed{
p(1-\delta)-{e_c\over2}
\le {c^2h^2\over2}+o(1),}
\tag{RF76.9}

where `e_cD` is the exact terminal directional energy on the retained complement pairs.

The dominant and complement selected edge occurrences are disjoint.  With

\[
F(z):=z-6\sin(z/6),
\]

the dominant selected occurrences consume at least `F(z)D-o(D)` of the total outer directional energy.  Hence

\[
e_c\le\delta-F(z)+o(1).
\]

Therefore

\[
\boxed{
p\le
{\delta-F(z)+c^2h^2\over2(1-\delta)}+o(1).}
\tag{RF76.10}

Every feasible survivor also has

\[
\boxed{F(z)\le\delta+o(1).}
\tag{RF76.11}

---

## 3. Replace the implicit threshold by a direct survivor-capacity maximum

Ignore vanishing terms and fix `t,h,x`.  Equation (RF76.7) fixes

\[
\delta={R_t-x-h\over2}.
\tag{RF76.12}

Combining (RF76.8) and (RF76.10), every survivor requires

\[
L(z):=
 z+{\delta-F(z)+c^2h^2\over2(1-\delta)}
\ge
\pi-{t\over2}-x-ch.
\tag{RF76.13}

On `0<=z<=pi`,

\[
F'(z)=1-\cos(z/6)
\le1-{\sqrt3\over2}<0.134.
\]

On the target feasible triangle, the exact certificate gives `delta<0.051`, so

\[
L'(z)
=1-{F'(z)\over2(1-\delta)}>0.
\tag{RF76.14}

By (RF76.11), `z` is at most

\[
Z(\delta):=F^{-1}(\delta).
\]

Thus the largest possible left side of (RF76.13) occurs at `z=Z(delta)`, where `F(z)=delta`.  A necessary condition for survival is consequently

\[
\boxed{
Q(t,h,x):=
Z(\delta)
+{c^2h^2\over2(1-\delta)}
-\left(\pi-{t\over2}-x-ch\right)
\ge0.}
\tag{RF76.15}

This formulation makes the feasible-triangle monotonicity transparent.

---

## 4. The whole feasible triangle collapses to `h=x=0`

The exact companion certificate covers `t<=T`, where

\[
T=1.843555,
\]

and gives

\[
U<2.013,
\qquad
\delta<0.051,
\qquad
h<0.101.
\tag{RF76.16}

### `t` direction

At fixed `h,x`,

\[
\delta_t={9\over4}>0.
\]

The inverse `Z(delta)` increases with `delta`, the residual denominator term increases with `delta`, and the explicit `t/2` term in `Q` increases.  Therefore

\[
\boxed{Q_t>0.}
\tag{RF76.17}

It is enough to exclude `t=T`.

### Topology slack `x`

On the interior `delta>0`,

\[
Z'(\delta)={1\over F'(Z)}.
\]

Since `delta_x=-1/2`,

\[
Q_x
=-{1\over2F'(Z)}
-{c^2h^2\over4(1-\delta)^2}
+1.
\tag{RF76.18}

Using `F'(Z)<0.134`,

\[
\boxed{Q_x<-2.7<0.}
\tag{RF76.19}

The same conclusion extends to `delta=0` by continuity.  Survivor capacity is largest at

\[
\boxed{x=0,\quad\kappa=0.}
\tag{RF76.20}

### Residual slack `h`

Similarly, `delta_h=-1/2`, so

\[
Q_h
=-{1\over2F'(Z)}
+c
+{c^2h\over1-\delta}
-{c^2h^2\over4(1-\delta)^2}.
\tag{RF76.21}

Drop the final nonpositive term.  With

\[
c=1.05,
\qquad h<0.101,
\qquad\delta<0.051,
\qquad F'(Z)<0.134,
\]

the exact rational certificate gives

\[
\boxed{Q_h<-2.56<0.}
\tag{RF76.22}

Thus survivor capacity is largest at

\[
\boxed{h=0,\quad U=C_{76}.}
\tag{RF76.23}

The entire correlated feasible triangle has collapsed to one corner.

---

## 5. Exact corner contradiction

At `h=x=0`,

\[
\delta_0(t)
={1\over2}\left({9t\over2}-2\pi-C_{76}\right),
\tag{RF76.24}

and (RF76.15) reduces to

\[
Z(\delta_0)
\ge\pi-{t\over2}.
\]

Because `F` is increasing, this is equivalent to

\[
\boxed{
\delta_0(t)
\ge
F\left(\pi-{t\over2}\right).}
\tag{RF76.25}

The exact rational verifier

`research/verify_target_c_g0076_residual_stability_floor_1843555.py`

uses Machin bounds for `pi`, integer-square-root enclosures, and alternating-series bounds for `sin`.  At

\[
t=1.843555
\]

it proves the strict reverse inequality

\[
\boxed{
F\left(\pi-{t\over2}\right)-\delta_0(t)
>1.5\times10^{-6}.}
\tag{RF76.26}

This contradicts (RF76.25).  Since `Q_t>0`, every smaller `t` is also excluded.

Therefore

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.843555.}
\]

---

## 6. Frontier effect

This is a larger gain than the preceding `g=0.0076` generic-residual propagation:

\[
1.843555-1.84332=0.000235.
\]

More importantly, the endpoint normal form is sharper.  At the weakest low-`t` corner,

\[
U=C_{76},
\qquad
R=U-M=0,
\qquad
\kappa=0.
\]

So all allowed exact atomic mass is in one exact three-phase orbit, and the complement-rhombus incidence budget has no independent residual-orbit allowance.  Further progress at the floor must use the internal geometry and cyclic boundary order of that single orbit, not another free complement mass parameter.

The live `t<=1.860` theorem simultaneously supplies retained dominant O--O pair weight `>0.0740D` on a much wider interval.  Together these results isolate the next target: the cyclic endpoint/crossing structure of a single dominant exact three-phase orbit under two-sided diameter bracing.

No exact unit equilateral triangle or same-cardinality strict sub-`D` competitor is claimed.  C-II remains open.
