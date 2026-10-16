# Target C-II — repaired two-leaf outer energy excludes through `t<=1.843651`

**Date:** 2026-09-15  
**Status:** proof-only full-core Type-II exclusion  
**Scope:** full-core/no-macroscopic-container Type-II branch  
**Dependencies:** scope-safe `g=0.007707` residual stability; hostile-audited two-leaf outer-energy stack through `1.84365`; non-circular strong-branch scope repair; `t<=1.844` phasewise retained-outer theorem; hostile-audited common-center and cross-phase endpoint-energy theorems  
**Certificate:** `research/verify_target_c_two_leaf_outer_energy_exclusion_t1843651.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The repaired two-leaf architecture has one further exact rounded step. The companion verifier proves

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.843651
}
\]

at the stated proof-only full-core scope.

This endpoint is extremely close to exhaustion of the present scalar/phase-localization argument. The smallest certified margins are only of order `10^-7`, so this note records the scope gates and rounding directions explicitly. No claim is made at `1.843652`.

The safe rounded package is

\[
h<0.0003828,
\qquad
W<1.9127155,
\qquad
E_{dom}>0.90689964,
\]

\[
z>2.21936,
\qquad
z_C,z_U,z_V>0.70202,
\]

\[
U,V<0.53052.
\]

Consequently each leaf carries more than `0.1715D` retained O-O pair weight. After charging the entire low-center-degree budget against either leaf, each still has more than `0.13484D` good pair weight. Common center neighbors force the good cross-product to be noncrossing; the exact `pi/3` endpoint-energy cost then closes the detour ledger.

---

## 1. Residual stability remains in its proved scope

Let

\[
C_{707}=2\sqrt{\Delta_2}+0.007707,
\qquad
\Delta_2={\pi\over2\sqrt3},
\]

and use

\[
t={q-k\over D},
\qquad
x={\kappa\over2},
\qquad
h=U_{net}-C_{707},
\qquad
c=1.05.
\]

The residual-stability theorem is stated only for `U_net<=2.013`. The independent `t<=1.844` phase theorem gives

\[
z_C,z_U,z_V>0.616-o(1),
\]

so total retained dominant outer mass exceeds `1.848D`. Hence

\[
\delta\ge F(1.848)-o(1),
\qquad
F(s)=s-6\sin(s/6).
\]

The exact verifier gives `F(1.848)>0.029`, and therefore at `t<=1.843651`,

\[
U_{net}
\le {9t\over2}-2\pi-2\delta
<1.956<2.013.
\]

Thus the existing residual estimate is legitimately available:

\[
\boxed{R:=U_{net}-W\le1.05h,}
\tag{E651.1}
\]

where `W=C+U+V` is the dominant exact `pi/3` orbit mass.

---

## 2. Residual slack is below `0.0003828`

The exact envelope is

\[
2\delta+x+h
=R_t:={9t\over2}-2\pi-C_{707}.
\tag{E651.2}
\]

Put

\[
T=1.843651,
\qquad
H=0.0003828.
\]

At the adverse point `t=T`, `h=H`, `x=0`, let

\[
\delta_H={R_T-H\over2}
\]

and

\[
A_H
=\pi-{T\over2}-1.05H
-{1.05^2H^2\over2(1-\delta_H)}.
\]

The exact outward certificate proves

\[
\boxed{
F(A_H)-\delta_H
>6.73\times10^{-8}.
}
\tag{E651.3}
\]

The hostile-audited feasible-triangle derivatives remain strictly negative,

\[
Q_x<-2.7,
\qquad
Q_h<-2.5,
\]

so every survivor satisfies

\[
\boxed{h<0.0003828-o(1).}
\tag{E651.4}
\]

It follows that

\[
\boxed{W<1.9127155-o(1),}
\tag{E651.5}
\]

and after subtracting the complete residual square contribution,

\[
\boxed{E_{dom}>0.90689964-o(1).}
\tag{E651.6}

The total detour budget obeys

\[
\boxed{\delta<0.05045578955+o(1).}
\tag{E651.7}

---

## 3. Total retained dominant outer mass exceeds `2.21936D`

Let `z` be retained dominant outer-occurrence mass and `p` retained complement O-O pair mass. The established retention/incidence system is

\[
z+p\ge\pi-{t\over2}-x-1.05h-o(1),
\tag{E651.8}
\]

\[
p\le
{1.05^2h^2+\delta-F(z)\over2(1-\delta)}+o(1)
\tag{E651.9}
\]

on the energy-feasible side.

Assume `z<=Z=2.21936`. The capped left side is increasing in `z`; the verifier bounds its derivative below by `0.96`. On the active boundary `delta=F(Z)`, the largest allowed residual cutoff still leaves positive

\[
x>5.58\times10^{-7}.
\]

Thus the boundary is genuinely feasible rather than an extrapolated point. Substitution there at `t=T`, `h=H` gives exact capped survivor excess

\[
\boxed{<-4.56\times10^{-6}.}
\tag{E651.10}
\]

The complementary `delta<F(Z)` region is controlled by the already-audited negative `Q_x,Q_h` derivatives. Therefore

\[
\boxed{z>2.21936-o(1).}
\tag{E651.11}

---

## 4. Every exact phase retains more than `0.70202D`

For phasewise retained masses,

\[
\delta\ge f(z_C)+f(z_U)+f(z_V)-o(1),
\qquad
f(s)=s-2\sin(s/2).
\tag{E651.12}
\]

If one phase were at most

\[
A=0.70202,
\]

strict convexity puts the cheapest other two masses at `(Z-A)/2`. The exact certificate proves

\[
\boxed{
f(A)+2f((Z-A)/2)-{R_T\over2}
>1.10\times10^{-7}.}
\tag{E651.13}
\]

Hence

\[
\boxed{z_C,z_U,z_V>0.70202-o(1).}
\tag{E651.14}

In particular,

\[
V>{0.70202\over2}-o(1)=0.35101-o(1),
\tag{E651.15}
\]

because one train has at most two retained terminal occurrences.

---

## 5. Non-circular strong-branch scope and the leaf mass cap

Assume for contradiction

\[
U\ge U_0:=0.53052.
\]

The previous proof repair showed that branch validity must be certified before replacing the actual leaf mass by `U_0`. Equation (E651.15) and `W<1.9127155` give

\[
C+U=W-V
<1.9127155-0.35101+o(1).
\]

Therefore, with `K_-=2/(\sqrt3)_+`,

\[
{(C+U-K)_+\over U}
\le
{1.9127155-0.35101-K_-\over0.53052}+o(1).
\]

The exact verifier proves

\[
\boxed{
{1.9127155-0.35101-K_-\over0.53052}
<0.767182
<\sqrt{20/29}.}
\tag{E651.16}
\]

On the main center interval `C<1.0443<K`. For fixed `C<K`, the ratio

\[
L\mapsto{(C+L-K)_+\over L}
\]

is nondecreasing. Since `V<=U`, the smaller leaf lies in the same strong physical-pair branch. This establishes the `1/10` pair theorem for the original configuration before any adverse substitution.

Generic center capacity excludes the tails

\[
C\le C_{low}:=1.9127155-2(0.53052)
\]

and

\[
C\ge1.0443.
\]

On the remaining interval, the already-audited capacity monotonicity permits the adverse replacements `W->1.9127155` and `U->0.53052`. Both center/leaf positive parts are strictly positive at the reduced point. Let `G(C)` be the resulting correlated strong capacity. Its exact second derivative satisfies `G''<-2`.

At

\[
c_0=0.9314032,
\]

the tangent bound gives

\[
\max G
\le G(c_0)+{G'(c_0)^2\over4}.
\]

The certificate proves

\[
\boxed{
E_{dom}-\max G>1.29\times10^{-7}.}
\tag{E651.17}
\]

Thus

\[
\boxed{U,V<0.53052-o(1).}
\tag{E651.18}

---

## 6. Both leaves retain more than `0.13484D` good O-O pair weight

The terminal inequality

\[
a_\tau+b_\tau\le1+\min(a_\tau,b_\tau)
\]

gives phasewise

\[
z_i\le M_i+P_i+o(1).
\]

Equations (E651.14) and (E651.18) imply

\[
\boxed{P_U,P_V>0.70202-0.53052-o(1)=0.1715-o(1).}
\tag{E651.19}

Let `B_bad` be total retained leaf O-O pair weight whose center degree is at most half the center family. The center/leaf missing-crossing correlation gives

\[
B_{bad}
\le
{2[C(W-C)-E_{dom}]\over C-U}+o(1).
\tag{E651.20}
\]

Using the safe rounded box, `B_bad<0.03666` is equivalent to positivity of a quadratic in `C`. The verifier obtains exact negative discriminant

\[
\boxed{\operatorname{disc}<-1.76\times10^{-5}.}
\tag{E651.21}
\]

Thus even after charging the entire bad budget against either leaf,

\[
\boxed{G_U,G_V>0.1715-0.03666-o(1)=0.13484-o(1).}
\tag{E651.22}

Every good U/V pair shares a center neighbor and is therefore noncrossing by triangle-freeness. The two leaf phases differ projectively by exactly `pi/3`, so the hostile-audited endpoint theorem gives

\[
e_\tau+e_\sigma\ge2-\sqrt3-o(1).
\]

Weighted product summation yields

\[
\boxed{
E_U+E_V
\ge(2-\sqrt3)(0.13484)-o(1).
}
\tag{E651.23}

At this near-ceiling endpoint the certificate uses its existing 100-digit outward enclosure for `sqrt(3)` rather than the older coarse decimal bound `sqrt(3)<1.7321`. This is only an arithmetic sharpening of the same exact constant.

---

## 7. Final outer-energy contradiction

The selected center occurrences and selected leaf paired terminal occurrences are physically disjoint, so their directional-energy payments add:

\[
\delta
\ge f(z_C)+E_U+E_V-o(1).
\]

The exact certificate gives

\[
f(0.70202)>0.0143272023217,
\]

and

\[
(2-\sqrt3)(0.13484)>0.0361302691074.
\]

Therefore

\[
\delta>0.0504574714291-o(1),
\]

whereas (E651.7) gives

\[
\delta<0.0504557895463+o(1).
\]

The exact contradiction margin is

\[
\boxed{>1.68\times10^{-6}.}
\tag{E651.24}

Thus no full-core Type-II survivor exists with

\[
t\le1.843651.
\]

For orientation only, a corrected continuous optimization of this same rounded architecture places its numerical zero near `1.84365114`; this value is not a theorem and is not used anywhere above. In particular, this note makes no claim at `1.843652`.

**Disposition:** proof-only full-core floor raised from `1.84365` to `1.843651`. C-II and Level I remain open.
