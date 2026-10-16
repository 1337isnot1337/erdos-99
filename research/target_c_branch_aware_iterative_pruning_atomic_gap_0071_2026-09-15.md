# Target C-II — branch-aware iterative pruning raises the matched atomic gap to `0.0071`

**Date:** 2026-09-15  
**Status:** proof-only strengthening of the matched all-train/rhombic atomic gap  
**Scope:** canonical full-core Type-II train-measure branch  
**Dependencies:** hostile-audited iterative-pruning conditional pair payment; audited dominant exact `pi/3` orbit decomposition and weighted two-leaf correlation  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current matched atomic theorem uses the iterative-pruning pair estimate only through
its unconditional relaxation

\[
\rho\ge {2\over29}(a+b-K)_+^2,
\qquad K={2\over\sqrt3}.
\]

That discards the stronger branch of the same theorem.  The exact pair result is

\[
\rho\ge
\min\left\{
{(a+b-K)_+^2\over10},
{2\min(a,b)^2\over29}
\right\}.
\tag{BA.1}
\]

Whenever

\[
{(a+b-K)_+\over\min(a,b)}
\le r:=\sqrt{20\over29},
\tag{BA.2}
\]

the first term in (BA.1) is active.  In the dominant three-phase orbit, the two leaf
families satisfy (BA.2) on the entire part of the center-imbalance domain that controls
the old minimax.  Outside that region we retain the unconditional `2/29` bound.

This branch-aware use of the already-proved physical pair theorem yields

\[
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.0071,
\qquad
\Delta_2={\pi\over2\sqrt3}.
}
\tag{BA.3}
\]

The same argument on the strict-rhombus train graph gives

\[
\boxed{
\liminf {T_R\over D}
\ge2\sqrt{\Delta_2}+0.0071,
\qquad
\liminf {\sigma_R\over D}\ge0.0142.
}
\tag{BA.4}
\]

The outward-rational certificate has more than `3.66e-4` margin at `g=0.0071`.
This supersedes the safe matched gaps `0.0050` and `0.0052` at the same proof-only
scope.

---

## 1. Physical pair theorem, with both branches retained

For two exact train-phase atom families of normalized masses `a,b<=K`, whose axes are
separated projectively by `pi/3`, let `rho` be their normalized missing-pair mass and
put

\[
e=(a+b-K)_+,
\qquad
m=\min\{a,b\}.
\]

The iterative-pruning theorem proves (BA.1).  Two corollaries will be used.

First, since `e<=m`, (BA.1) always gives

\[
\boxed{
e\le\lambda_0\sqrt\rho,
\qquad
\lambda_0:=\sqrt{29/2}.}
\tag{BA.5}
\]

Second, if `e/m<=r=sqrt(20/29)`, then

\[
{e^2\over10}\le {2m^2\over29},
\]

so the stronger branch applies:

\[
\boxed{
e\le\lambda_1\sqrt\rho,
\qquad
\lambda_1:=\sqrt{10}.}
\tag{BA.6}
\]

No new train-order or common-neighbor theorem is being assumed here.  Both statements
are direct consequences of the already-audited physical pair theorem.

---

## 2. Contradiction domain for a proposed atomic gap

Put

\[
s:=\sqrt{\Delta_2},
\qquad
g:=0.0071,
\qquad
\bar A:=2s+g.
\tag{BA.7}
\]

Assume for contradiction that the total exact atomic train mass satisfies

\[
A\le\bar A.
\tag{BA.8}
\]

Let `W` be the mass of a dominant exact `pi/3` orbit and `E` its strict-rhombus crossing
mass.  The generic orbit square bound gives

\[
4\Delta_2\le\sum_r M_r^2\le WA,
\]

hence

\[
\boxed{
W\ge W_0:={4s^2\over\bar A}.}
\tag{BA.9}
\]

Write the dominant-orbit Mantel deficit as

\[
\delta={W^2\over4}-E.
\tag{BA.10}
\]

If the residual orbit masses total `R=A-W`, then their total crossing mass is at most
`R^2/4`.  Since all exact-orbit crossing masses sum to `s^2`,

\[
s^2
\le {W^2\over4}-\delta+{R^2\over4}
\le {A^2\over4}-\delta.
\]

Therefore

\[
\boxed{
0\le\delta\le d_0:=s g+{g^2\over4}.}
\tag{BA.11}
\]

At `g=0.0071`, numerically only for orientation,

\[
W_0=1.89755198257\ldots,
\qquad
d_0=0.00677402342\ldots .
\]

---

## 3. Dominant three-phase orbit and weighted two-leaf correlation

Freeze shrinking windows around the at most three atoms of the dominant exact orbit.
Write their masses as

\[
C\ge U\ge V\ge0,
\qquad
C+U+V=W.
\tag{BA.12}
\]

Same-window pairs do not cross.  The standard triangle-free dominant-orbit estimate is

\[
E\le C(U+V)=C(W-C).
\]

Put

\[
z:=C-{W\over2}.
\tag{BA.13}
\]

Then

\[
C(W-C)={W^2\over4}-z^2,
\]

so (BA.10) implies

\[
\boxed{|z|\le\sqrt\delta\le\sqrt{d_0}.}
\tag{BA.14}
\]

Let

\[
x=CU-e(C,U),
\qquad
y=CV-e(C,V),
\]

be the missing masses in the two center-leaf pairs, and let `e(U,V)` be the leaf-leaf
crossing mass.  Define

\[
h:=C(U+V)-E=x+y-e(U,V).
\tag{BA.15}
\]

The physical train-crossing graph is triangle-free.  For every actual `UV` crossing,
the two leaf endpoints have disjoint neighborhoods in the center class.  Summing the
center-degree deficits gives

\[
C e(U,V)\le Vx+Uy.
\]

With

\[
a=1-{V\over C},
\qquad
b=1-{U\over C},
\]

we obtain

\[
\boxed{a x+b y\le h.}
\tag{BA.16}
\]

Also, from (BA.10), (BA.13), and (BA.15),

\[
\boxed{h=\delta-z^2\le d_0-z^2.}
\tag{BA.17}
\]

The contradiction domain stays safely inside the pair theorem's family cap.  Indeed

\[
C={W\over2}+z
\le {\bar A\over2}+\sqrt{d_0}
<1.039<K,
\tag{BA.18}
\]

and `U,V<=C`.  The exact certificate checks this with outward bounds.

---

## 4. A new branch test depending only on the center imbalance

Consider either leaf mass `L in {U,V}`.  Since `C>=L`, the pair theorem uses

\[
m=L,
\qquad e_L=(C+L-K)_+.
\]

For fixed `C`, the ratio `e_L/L`, where positive, increases with `L`.  Since every leaf
satisfies

\[
L\le U+V=W-C,
\]

we have

\[
{e_L\over L}
\le {W-K\over W-C}.
\tag{BA.19}
\]

Thus both center-leaf pairs lie in the strong branch (BA.6) whenever

\[
{W-K\over W-C}\le r.
\]

Equivalently,

\[
(1-r)W+rC\le K.
\]

Substituting `C=W/2+z`, this is

\[
\left(1-{r\over2}\right)W+r z\le K.
\tag{BA.20}
\]

Under the contradiction hypothesis `W<=A<=bar A`, a sufficient condition depending
only on `z` is

\[
\boxed{
z\le z_*:={K-(1-r/2)\bar A\over r}.}
\tag{BA.21}
\]

At `g=0.0071`,

\[
z_*=0.04428390253\ldots .
\]

This contains the actual worst part of the minimax domain.  For `z<=z_*` we may use
`lambda_1=sqrt(10)` simultaneously for both center-leaf pairs.  For `z>z_*` we use the
unconditional `lambda_0=sqrt(29/2)`.

This is the only new idea in the proof.

---

## 5. Weighted two-leaf minimax with a branch-aware coefficient

For one coefficient `lambda` valid for both leaf pairs, define

\[
F_U=C+U-\lambda\sqrt x,
\qquad
F_V=C+V-\lambda\sqrt y.
\tag{BA.22}
\]

The corresponding pair inequalities imply

\[
F_U\le K,
\qquad F_V\le K.
\tag{BA.23}
\]

The existing weighted two-leaf argument is retained exactly.  A maximum dominates the
`a,b` weighted average, while Cauchy and (BA.16) give

\[
a\sqrt x+b\sqrt y
\le\sqrt{(a+b)h}.
\]

Writing `L=U+V=W-C` and using `UV<=L^2/4` gives

\[
{aU+bV\over a+b}\ge {L\over2}.
\]

Therefore

\[
\max(F_U,F_V)
\ge {W+C\over2}
-\lambda\sqrt{h\,{C\over3C-W}}.
\tag{BA.24}
\]

Substitute `C=W/2+z`:

\[
\boxed{
\max(F_U,F_V)
\ge
{3W\over4}+{z\over2}
-\lambda
\sqrt{h\,{W+2z\over W+6z}}.
}
\tag{BA.25}
\]

Use

\[
\lambda(z)=
\begin{cases}
\sqrt{10},&z\le z_*,\\
\sqrt{29/2},&z>z_*.
\end{cases}
\tag{BA.26}
\]

Every hypothetical survivor of (BA.8) must therefore satisfy

\[
K\ge
{3W\over4}+{z\over2}
-\lambda(z)
\sqrt{(d_0-z^2){W+2z\over W+6z}}
\tag{BA.27}
\]

throughout its actual `z` value.

---

## 6. Reduction to a one-dimensional outward certificate

The right side of (BA.27) is bounded from below uniformly in the remaining variables.

The raw term

\[
{3W\over4}+{z\over2}
\]

is increasing in `W`, so use `W=W_0` for a lower bound.

For `z<0`,

\[
R(W,z):={W+2z\over W+6z}
\]

satisfies

\[
{\partial R\over\partial W}={4z\over(W+6z)^2}<0,
\qquad
{\partial R\over\partial z}={-4W\over(W+6z)^2}<0.
\]

Hence the loss term is maximized by the smallest allowed `W` and the smallest `z` in
an interval.  For `z>=0`, simply use `R<=1`.  Equation (BA.17) gives
`h<=d_0-z^2`, whose interval maximum occurs at the point nearest zero.

The exact verifier

`research/verify_target_c_branch_aware_atomic_gap_0071.py`

uses only rational arithmetic for all assertions.  It covers

\[
-0.083\le z\le0.083
\]

in steps of `10^{-5}`; this interval strictly contains (BA.14).  It computes an outward
lower bound for `z_*`, so the strong coefficient is used only on intervals lying wholly
inside the certified strong branch.  Any interval touching or lying above that
threshold uses the weaker coefficient `sqrt(29/2)`.

The certificate obtains

\[
W_0>1.89755198257,
\qquad
d_0<0.00677402343,
\]

\[
z_*>0.04428390253,
\]

and its worst interval is

\[
[-0.01970,-0.01969].
\]

There the outward lower bound for the right side of (BA.27) is

\[
1.15506699565\ldots,
\]

while

\[
K<1.15470053838.
\]

Thus the certified contradiction margin is

\[
\boxed{>3.66\times10^{-4}.}
\tag{BA.28}
\]

This contradicts (BA.23), so (BA.8) is impossible.

Consequently the exact atomic mass has the matched floor

\[
A\ge2s+0.0071-o(1).
\]

The exposed-hull comparison `A<=C=(T-q/2)/D` then proves (BA.3).

---

## 7. Strict-rhombus transfer

The hostile audits of the previous minimax and iterative-pruning routes already verify
that the same proof can be run independently on the strict-rhombus train graph:

- its vertices are the non-singleton complete rhombic trains;
- the graph is simple and triangle-free;
- its limiting crossings are supported at exact projective separation `pi/3`;
- the iterative-pruning physical pair theorem applies to selected phase families; and
- its edge mass is the strict-rhombus density `Delta_2`.

Nothing in Sections 1--6 uses singleton trains, loaded-hull energy, or a feature absent
from that rhombic graph.  Repeating the argument gives

\[
\liminf {T_R\over D}\ge2s+0.0071.
\]

The standard rhombic train/slack identity then gives

\[
\boxed{
\liminf {\sigma_R\over D}\ge2(0.0071)=0.0142.
}
\tag{BA.29}

---

## 8. Frontier effect and scope

At proof-only full-core Type-II scope, the matched train-measure floors are now

```text
(T-q/2)/D >= 2 sqrt(Delta_2) + 0.0071 - o(1)
T_R/D       >= 2 sqrt(Delta_2) + 0.0071 - o(1)
sigma_R/D   >= 0.0142 - o(1)
```

This is a real structural gain over the `0.0052` orbit-capacity theorem: it uses the
same physical pair theorem but stops replacing its two branches by the weaker universal
`2/29` coefficient in the part of phase space where the `1/10` branch is forced.

It still does **not** close C-II.  The next work should propagate `g=0.0071` and
`sigma_R/D>=0.0142` through the current Section-171/outer-energy and complement-rhombus
incidence chains, then attack the surviving diameter-bracing/outer-order structure.

No exact equilateral triangle, KKT weight floor, or same-cardinality strict sub-`D`
competitor is claimed.
