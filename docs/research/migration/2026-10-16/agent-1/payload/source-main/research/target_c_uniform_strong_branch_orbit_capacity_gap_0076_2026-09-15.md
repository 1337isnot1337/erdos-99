# Target C-II — corrected uniform strong-branch orbit capacity gives matched atomic gap `0.0076`

**Date:** 2026-09-15  
**Status:** proof-only strengthening of the matched all-train/rhombic atomic gap  
**Scope:** canonical full-core Type-II train-measure branch  
**Dependencies:** hostile-audited iterative-pruning physical pair theorem; audited exact `pi/3` orbit decomposition and center/leaf correlation  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

This is the scope-corrected version of the `0.0076` strong-branch orbit-capacity proof.  The physical pair theorem applies only when both selected phase families have mass at most

\[
K={2\over\sqrt3}.
\]

Accordingly, the proof uses the strong `1/10` pair deficit near the actual capacity maximizer, the unconditional `2/29` pair deficit only while the center mass still satisfies `C<=K`, and the generic triangle-free capacity when `C>K`.

Let

\[
r_*:=\sqrt{20\over29}.
\]

For two exact train-phase atom families of masses `a,b<=K`, at projective separation `pi/3`, with normalized missing-pair mass `rho`, the hostile-audited iterative-pruning theorem gives

\[
\boxed{
\rho\ge
\min\left\{
{(a+b-K)_+^2\over10},
{2\min(a,b)^2\over29}
\right\}.}
\tag{US.1}

If

\[
{(a+b-K)_+\over\min(a,b)}\le r_*,
\]
then

\[
\boxed{
\rho\ge{(a+b-K)_+^2\over10}.}
\tag{US.2}

The corrected capacity argument proves

\[
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.0076,
\qquad
\Delta_2={\pi\over2\sqrt3}.}
\tag{US.3}

Repeating it independently on the strict-rhombus train graph gives

\[
\boxed{
\liminf {T_R\over D}
\ge2\sqrt{\Delta_2}+0.0076,
\qquad
\liminf {\sigma_R\over D}\ge0.0152.}
\tag{US.4}

A non-load-bearing numerical solve of the controlling low-center capacity equation gives a ceiling near `0.0077072732`; only `0.0076` is claimed.

---

## 1. Contradiction domain and dominant orbit

Put

\[
s:=\sqrt{\Delta_2},
\qquad
g:=0.0076,
\qquad
A_0:=2s+g.
\tag{US.5}

Assume for contradiction that the total exact atomic train mass satisfies

\[
A\le A_0.
\tag{US.6}

Let the exact orbit masses be `M_j`, let `W=max_j M_j`, and let `E_j` be their strict-rhombus crossing masses.  The audited orbit decomposition gives

\[
E_j\le {M_j^2\over4},
\qquad
\sum_jE_j=\Delta_2,
\qquad
\sum_jM_j=A.
\tag{US.7}

Thus

\[
4\Delta_2\le\sum_jM_j^2\le WA,
\]
so

\[
\boxed{
W\ge M_0:={4\Delta_2\over A_0}.}
\tag{US.8}

The residual orbit masses total at most `A_0-W`; their total crossing mass is at most

\[
{(A_0-W)^2\over4}.
\tag{US.9}

The exact certificate gives

\[
M_0>1.89705,
\qquad
A_0<2K.
\tag{US.10}

---

## 2. Three-phase orbit capacity when the pair theorem is in scope

Write the phase-class masses of one exact orbit as

\[
C\ge U\ge V\ge0,
\qquad
W=C+U+V.
\tag{US.11}

Let

\[
x=CU-e(C,U),
\qquad
y=CV-e(C,V),
\]

and put

\[
h:=C(U+V)-E=x+y-e(U,V).
\tag{US.12}

Triangle-freeness gives the standard weighted correlation

\[
\boxed{
\left(1-{V\over C}\right)x
+
\left(1-{U\over C}\right)y
\le h.}
\tag{US.13}

Suppose a common coefficient `alpha` is valid in

\[
x\ge\alpha(C+U-K)_+^2,
\qquad
y\ge\alpha(C+V-K)_+^2.
\tag{US.14}

The equal-leaves calculation, valid for any nonnegative common `alpha`, gives

\[
\boxed{
E\le\Phi_\alpha(W,C):=
C(W-C)
-
\alpha{3C-W\over C}
\left({W+C\over2}-K\right)_+^2.}
\tag{US.15}

This formula is used only where the relevant center and leaf families all have mass at most `K`.

---

## 3. The strong `1/10` branch contains the capacity maximizer

For one leaf `L in {U,V}`, where the excess is positive, define

\[
R_L={C+L-K\over L}.
\]

It increases with `L`.

### 3.1 `W/3 <= C <= W/2`

Here `L<=C`, so

\[
R_L\le2-{K\over C}
\le2-{2K\over W}
\le2-{2K\over A_0}.
\]

The exact certificate proves

\[
2-{2K\over A_0}<0.793<r_*.
\tag{US.16}

Also `C<=W/2<=A_0/2<K`, so the size hypothesis of the physical pair theorem holds.  Therefore both center/leaf pairs satisfy (US.2), and

\[
E\le\Phi_{1/10}(W,C)
\qquad(W/3\le C\le W/2).
\tag{US.17}

### 3.2 A short interval to the right of `W/2`

For `C>W/2`, every leaf satisfies `L<=W-C`, hence

\[
R_L\le{W-K\over W-C}.
\]

Define

\[
C_s(W):=W-{W-K\over r_*}.
\tag{US.18}

Then both center/leaf pairs satisfy the strong branch whenever `C<=C_s(W)`.  Equation (US.16) implies

\[
C_s(W)>W/2.
\tag{US.19}

Moreover `C_s` decreases with `W`.  On `M_0<=W<=A_0`, the exact certificate gives

\[
1.0000<C_s(W)<1.0032<K.
\tag{US.20}

Thus the pair theorem remains fully in scope throughout the entire strong interval.

---

## 4. Strong-region optimizer

On `W/3<=C<=W/2`, put

\[
q=3-{W\over C},
\qquad
r={W+C\over2}-K.
\]

In the relevant range `r>0`, `0<=q<=1`, and `r<C`.  Differentiating (US.15),

\[
\Phi_{\alpha,C}
=W-2C-\alpha\left({W\over C^2}r^2+qr\right),
\tag{US.21}

\[
\Phi_{\alpha,CC}
=-2-\alpha\left[
{2Wr\over C^2}\left(1-{r\over C}\right)+{q\over2}
\right]
\le-2.
\tag{US.22}

For `alpha=1/10`, the exact certificate gives

\[
\Phi_{1/10,C}(W,W/3)>0.6255
\tag{US.23}

uniformly, while

\[
\Phi_{1/10,C}(W,W/2)<0.
\]

Hence there is a unique maximizer

\[
C_*(W)\in(W/3,W/2).
\tag{US.24}

Put

\[
\Psi_1(W):=\Phi_{1/10}(W,C_*(W)).
\tag{US.25}

For `W/2<=C<=C_s(W)`, equation (US.21) is already negative, so the extra strong interval to the right cannot beat `Psi_1(W)`.

---

## 5. Corrected fallback and high-center branches

The pair theorem cannot be used once `C>K`.  Split the remainder accordingly.

### 5.1 Pair-theorem fallback: `C_s(W)<=C<=K`

Here all three phase families satisfy `C,U,V<=K`, so the unconditional coefficient

\[
\alpha_0={2\over29}
\]

is valid.  Since `C_s(W)>W/2`, equation (US.21) gives

\[
\Phi_{2/29,C}<0
\]

throughout this interval.  Therefore

\[
\boxed{
E\le B_0(W):=\Phi_{2/29}(W,C_s(W)).}
\tag{US.26}

### 5.2 High center: `C>K`

Do not use the physical pair theorem.  The generic triangle-free center bound gives

\[
E\le C(U+V)=C(W-C).
\]

Because `W<=A_0<2K`, one has `K>W/2`, so `C(W-C)` decreases for `C>=K`.  Hence

\[
\boxed{
E\le B_H(W):=K(W-K).}
\tag{US.27}

Consequently every dominant orbit of mass `W` satisfies

\[
\boxed{
E\le\max\{\Psi_1(W),B_0(W),B_H(W)\}.}
\tag{US.28}

---

## 6. Adding residual orbits

Under `A<=A_0`, equations (US.9) and (US.28) imply that for some `W in[M_0,A_0]`, at least one of the following must hold:

\[
\Delta_2
\le Q_1(W):=\Psi_1(W)+{(A_0-W)^2\over4},
\tag{US.29}

\[
\Delta_2
\le Q_0(W):=B_0(W)+{(A_0-W)^2\over4},
\tag{US.30}

\[
\Delta_2
\le Q_H(W):=B_H(W)+{(A_0-W)^2\over4}.
\tag{US.31}

All three right sides increase with `W`.

### Strong branch

At the unique optimizer, the envelope theorem gives

\[
\Psi_1'(W)=\Phi_{1/10,W}(W,C_*(W)).
\]

From (US.15),

\[
\Phi_{\alpha,W}
=C+\alpha{r^2\over C}-\alpha q r
\ge C-\alpha q r.
\]

Using `C>=W/3`, `q<=1`, and `r<=3A_0/4-K`,

\[
\Psi_1'(W)
\ge {M_0\over3}-{1\over10}\left({3A_0\over4}-K\right).
\]

After subtracting the residual derivative `(A_0-W)/2`, the exact certificate gives

\[
\boxed{Q_1'(W)>0.5968.}
\tag{US.32}

### Pair-theorem fallback

Since

\[
C_s'(W)=1-{1\over r_*}<0
\]

and `Phi_{2/29,C}<0` at `C_s(W)`, the moving-boundary term in `B_0'(W)` is positive.  The coarse bounds `C_s>W/2`, `q<2`, and `r<=A_0-K` give, after the residual derivative is subtracted,

\[
\boxed{Q_0'(W)>0.8364.}
\tag{US.33}

### High-center branch

Here

\[
Q_H'(W)=K-{A_0-W\over2}.
\]

The certificate gives

\[
\boxed{Q_H'(W)>1.147.}
\tag{US.34}

Thus every total-capacity alternative is largest at

\[
W=A_0,
\tag{US.35}

where the residual orbit mass vanishes.

---

## 7. Exact endpoint certificate

The verifier

`research/verify_target_c_uniform_strong_branch_orbit_capacity_gap_0076.py`

uses exact `Fraction` arithmetic, a Machin enclosure for `pi`, and integer-square-root enclosures for radicals.

For the strong branch, take

\[
c_0=0.935343.
\]

Since `Phi_CC<=-2`,

\[
\Psi_1(A_0)
\le
\Phi_{1/10}(A_0,c_0)
+{\Phi_{1/10,C}(A_0,c_0)^2\over4}.
\]

The exact outward calculation gives

\[
\boxed{
\Delta_2-\Psi_1(A_0)>9.84\times10^{-5}.}
\tag{US.36}

For the valid fallback interval it gives

\[
\boxed{
\Delta_2-B_0(A_0)>1.49\times10^{-3}.}
\tag{US.37}

For the scope-separated high-center branch it gives

\[
\boxed{
\Delta_2-B_H(A_0)>0.0321.}
\tag{US.38}

All three alternatives (US.29)--(US.31) are impossible.  Therefore (US.6) fails, and

\[
A\ge2\sqrt{\Delta_2}+0.0076-o(1).
\tag{US.39}

The exposed-hull comparison

\[
A\le {T-q/2\over D}+o(1)
\]
proves (US.3).

---

## 8. Strict-rhombus transfer

Rerun the proof independently on the strict-rhombus train graph, exactly as in the hostile-audited iterative-pruning matched theorem.  The graph is simple and triangle-free, its edge mass is the strict-rhombus mass, its limiting crossing atoms occur at projective separation `pi/3`, and the same physical pair theorem applies to selected families within its stated size scope.  The high-center branch again uses only the generic triangle-free bound.

Thus

\[
\liminf {T_R\over D}
\ge2\sqrt{\Delta_2}+0.0076,
\]

and the standard exact train/slack transfer gives

\[
\boxed{
\liminf {\sigma_R\over D}\ge0.0152.}
\tag{US.40}

---

## 9. Frontier effect

The current matched proof-only train-measure floors are

```text
(T-q/2)/D >= 2 sqrt(Delta_2) + 0.0076 - o(1)
T_R/D       >= 2 sqrt(Delta_2) + 0.0076 - o(1)
sigma_R/D   >= 0.0152 - o(1)
```

This supersedes the `0.0071` branch-aware minimax theorem and the corrected `0.0053` universal-coefficient orbit-capacity theorem.

The remaining scalar room in this exact capacity architecture is only about `1.1e-4`, so further tuning is low-value.  The useful next step is downstream: insert `g=0.0076` and `sigma_R/D>=0.0152` into the energy-restored complement-rhombus-incidence chain and then exploit the resulting almost-pure dominant three-phase boundary structure.

No exact equilateral triangle, KKT weight floor, or same-cardinality strict sub-`D` competitor is claimed.  C-II remains open.
