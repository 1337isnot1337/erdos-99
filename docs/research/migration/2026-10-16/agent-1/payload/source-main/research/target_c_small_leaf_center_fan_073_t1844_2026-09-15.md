# Target C-II — one smallest-leaf O--O train is crossed by more than `0.73D` center trains

**Date:** 2026-09-15  
**Status:** proof-only phase-resolved structural strengthening  
**Scope:** full-core Type-II branch with `t=(q-k)/D<=1.844`  
**Dependencies:** small-leaf outer-pair theorem; small-leaf/center crossing theorem; dominant-orbit triangle-free correlation  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding phase-resolved theorem proved that the smallest leaf phase of the dominant exact `pi/3` orbit carries retained O--O pair weight `>0.0848D` and total weighted center-crossing incidence `>0.072D^2`.  Dividing those two independent lower/upper bounds only yielded one train with `>0.135D` center crossings.

The retained outer-occurrence lower bound contains much more information.  Let the dominant phase masses be

\[
C\ge U\ge V,
\]

and let `z_V` be the retained outer-occurrence mass in the smallest leaf phase.  The exact parent certificates give, for every survivor with `t<=1.844`,

\[
W:=C+U+V<1.915963+o(1),
\tag{FAN.1}

\[
E_{dom}>0.9068958-o(1),
\tag{FAN.2}

\[
C>0.8538-o(1),
\tag{FAN.3}

\[
z_V>0.616-o(1).
\tag{FAN.4}

For the retained `V`-phase O--O pair family `Q_V`, this note proves the weighted average center-crossing degree bound

\[
\boxed{
{E(C,Q_V)\over P_VD}>0.73D-o(D),
}
\tag{FAN.5}

where `P_VD` is the total retained pair weight.  Hence some positive-weight `V`-phase O--O train is crossed by

\[
\boxed{>0.73D-o(D)}
\tag{FAN.6}

center-phase complete trains.

This is a major strengthening of the previous `0.135D` fan.

---

## 1. The leaf phase itself has mass greater than `0.308D`

Every complete stopped train has exactly two terminal face incidences, and every retained occurrence weight is at most one.  Therefore the total retained outer-occurrence mass in the `V` window satisfies

\[
z_V\le2V+o(1).
\tag{FAN.7}

Together with (FAN.4),

\[
\boxed{V>0.308-o(1).}
\tag{FAN.8}

This simple inequality removes the ordering-limited branch that controlled the cruder crossing-incidence estimate.

Let `P_V` be the normalized retained O--O pair weight in the `V` phase.  Summing

\[
a_\tau+b_\tau\le1+\min(a_\tau,b_\tau)
\]

over `V`-phase trains gives

\[
z_V\le V+P_V+o(1),
\]
so

\[
\boxed{P_V>0.616-V-o(1).}
\tag{FAN.9}

---

## 2. Missing center--leaf crossings

Write

\[
y:=CV-e(C,V)
\]

for the missing crossing mass between center and smallest-leaf phases, and put

\[
h:=C(U+V)-E_{dom}.
\]

The hostile-audited dominant-orbit correlation gives

\[
\left(1-{V\over C}\right)x+
\left(1-{U\over C}\right)y\le h,
\]
where `x>=0` is the other center-leaf missing mass.  Therefore, with

\[
b:=1-{U\over C},
\]

\[
\boxed{y\le CV,}
\qquad
\boxed{y\le h/b\quad(b>0).}
\tag{FAN.10}

The weighted O--O family is a submeasure of the full `V`-phase train measure, so its missing center incidences are at most `y`.  Hence

\[
E(C,Q_V)\ge CP_VD^2-yD^2-o(D^2).
\]

Using (FAN.9),

\[
\boxed{
{E(C,Q_V)\over P_VD^2}
\ge
C-{y\over0.616-V}-o(1).}
\tag{FAN.11}

It remains to lower-bound the right side uniformly.

---

## 3. The adverse total orbit mass is `W_0=1.915963`

Use the rounded safe constants

\[
W_0=1.915963,
\qquad
E_0=0.9068958,
\qquad
a=0.616.
\]

For fixed `C,V`, write

\[
U=W-C-V,
\qquad
b={2C+V-W\over C},
\]

and

\[
h=C(W-C)-E_{dom}.
\]

Since `V>a/2=0.308` and `C>0.8538`,

\[
2C+V>2(0.8538)+0.308=2.0156>W_0.
\]

Thus the ordering `U<=C` does not prevent taking the adverse upper mass `W=W_0`.

Moreover

\[
{h\over b}
={C[C(W-C)-E_{dom}]\over2C+V-W}
\]

is increasing in `W` throughout the feasible region: its `W` derivative has numerator

\[
C[C^2+CV-E_{dom}]>0,
\]
using the same rounded lower bounds.  It is also decreasing in `E_dom`.  Hence the adverse choice is

\[
W=W_0,
\qquad E_{dom}=E_0.
\tag{FAN.12}

Put

\[
H(C):=C(W_0-C)-E_0,
\qquad
d:=2C+V-W_0.
\]

The generic capacity gives

\[
H(C)\le {W_0^2\over4}-E_0<0.010833.
\]

But throughout the domain

\[
Vd
>0.308[2(0.8538)+0.308-W_0]
>0.03068.
\]

Therefore

\[
{h\over b}={CH(C)\over d}<CV.
\tag{FAN.13}

The correlated bound is always the stronger one.  Equation (FAN.11) becomes

\[
\boxed{
{E(C,Q_V)\over P_VD^2}
\ge
R(C,V):=
C-{CH(C)\over(2C+V-W_0)(a-V)}-o(1).}
\tag{FAN.14}

---

## 4. For fixed center mass only two leaf endpoints matter

The ordering `U>=V` gives

\[
V\le {W_0-C\over2}.
\]

Thus

\[
{a\over2}<V\le {W_0-C\over2}.
\tag{FAN.15}

For fixed `C`, the only `V`-dependent denominator in (FAN.14) is

\[
q_C(V)=(2C+V-W_0)(a-V).
\]

This is a concave quadratic in `V`.  Therefore its minimum on (FAN.15), and hence the minimum of `R(C,V)`, occurs at one of the two endpoints:

1. `V=a/2=0.308`;
2. `V=(W_0-C)/2`, the balanced-leaf endpoint `U=V`.

The generic center capacity `E_0<=C(W_0-C)` and (FAN.3) restrict

\[
0.8538<C<1.063,
\tag{FAN.16}

because the exact verifier checks

\[
1.063(W_0-1.063)<E_0.
\]

The remaining problem is two one-variable cubic inequalities on this compact interval.

---

## 5. Exact low-leaf endpoint

At `V=a/2`, condition `R(C,V)>L` with

\[
L=0.73
\]

is equivalent, after multiplying by the positive denominator, to

\[
N_{lo}(C)>0,
\]
where

\[
N_{lo}(C)
=(C-L)(2C+a/2-W_0)(a/2)
-C[C(W_0-C)-E_0].
\tag{FAN.17}

The exact `Fraction` verifier proves `N_lo''>0` throughout (FAN.16), brackets its unique critical point in

\[
0.8810<C_*<0.8811,
\]

and uses an exact derivative-Lipschitz interval bound to obtain

\[
\boxed{N_{lo}(C)>0.0028412}
\tag{FAN.18}

at the minimum.

---

## 6. Exact balanced-leaf endpoint

At

\[
V={W_0-C\over2},
\]

the denominator factors are

\[
2C+V-W_0={3C-W_0\over2},
\]

\[
a-V=a-{W_0-C\over2}.
\]

Again `R(C,V)>0.73` is equivalent to

\[
N_{hi}(C)>0,
\]
where

\[
N_{hi}(C)
=(C-L){3C-W_0\over2}
\left(a-{W_0-C\over2}\right)
-C[C(W_0-C)-E_0].
\tag{FAN.19}

The exact verifier proves `N_hi''>0`, brackets the unique critical point in

\[
0.9033<C_*<0.9034,
\]

and obtains the rigorous minimum bound

\[
\boxed{N_{hi}(C)>0.00046028.}
\tag{FAN.20}

This is the controlling endpoint, but it is still comfortably positive.

Equations (FAN.18)--(FAN.20) prove

\[
R(C,V)>0.73
\]
throughout the feasible domain.  Therefore (FAN.5) holds.

---

## 7. Extract one macroscopic exact-phase fan

Write the retained weighted O--O family as weights `w_tau>0`.  If `d_tauD` is the number of center-phase complete trains crossing `tau`, then

\[
E(C,Q_V)=D^2\sum_\tau w_\tau d_\tau/D.
\]

Equation (FAN.5) says the weighted average of `d_tau/D` exceeds `0.73-o(1)`.  Hence one positive-weight `V`-phase O--O train satisfies

\[
\boxed{d_\tau>0.73-o(1).}
\]

That train is crossed by more than `0.73D-o(D)` center-phase complete trains.

Because the `V`-phase O--O trains are pairwise noncrossing and all have one exact projective direction, the center crossings along this train are linearly ordered.  Section 157 simultaneously gives actual diameter edges crossing this same train cut with both transverse signs.

---

## 8. Frontier effect

For every survivor in the current live band

\[
1.843555\lesssim t\le1.844,
\]

there is now a single exact-leaf outer-to-outer train carrying a macroscopic ordered fan:

```text
>0.73 D center-phase strict-rhombus crossings
+ two-sided actual-diameter bracing
+ membership in a linear pairwise-noncrossing same-phase O-O family.
```

The next obstruction is no longer a population-count problem.  It is a multi-cut/order problem: compare the ordered center crossings on this fan with neighboring parallel leaf O--O cuts, and subtract their Section-157 KKT cut resultants.  Such differences localize diameter force to the strips between consecutive leaf cuts and may bound how often a fixed diameter edge can provide the required sign changes.

No exact unit equilateral triangle or strict sub-`D` competitor is claimed.  C-II remains open.
