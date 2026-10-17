# Target C-II — collapsed support-six blocks pay into the full contact tangent

**Date:** 2026-09-19  
**Status:** proof-only structural strengthening; theorem-state authority unchanged  
**Scope:** canonical full-core stopped-train system after maximal two-anchor activation  
**Depends on:** audited train-angle closure matrix; one-anchor relation-component theorem; support-five reciprocal exclusion; completed noncollapsed support-six exclusion; sealed-component exact rotation theorem; activated-endpoint pair-shield manifold; exact contact-tangent dimension  
**Certificate:** `research/verify_target_c_support6_collapsed_tangent_payment_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The support-six classification has reached a sharp endpoint. A nonzero one-anchor relation component cannot have support five, and every degree-pure support-six component is now forced into the collapsed branch

\[
y_1=\cdots=y_6\ne0,
\qquad
R=K_6\setminus M,
\]

with six projectively parallel outside anchors in a `3+3` orientation split. The noncollapsed support-six branch has been excluded. The collapsed branch itself cannot be excluded by the local pentagon inequalities: the repository contains a certified regular exact local realization.

There is nevertheless a universal tangent payment. Freeze the six outside-anchor train angles of one degree-pure collapsed block. The twelve internal relation-train angle rates are constrained by twelve scalar face-closure rows. Every internal train column occurs with opposite vectors at its two endpoint faces. Consequently the internal closure matrix has a two-dimensional constant-vector left kernel, hence rank at most ten and column nullity at least two.

Thus every degree-pure collapsed support-six block contributes at least two localized, non-Euclidean infinitesimal contact-flex directions with all six anchor train rates zero. In addition, such a block is sealed, so the existing sealed-component theorem supplies its exact common-angle rotation. The internal-only tangent does not contain that common-angle direction. After the same conservative one-dimensional global-rotation allowance used in the sealed-component theorem, `c_6` collapsed blocks therefore pay at least

\[
2c_6+(c_6-1)_+
\]

contact-tangent dimensions beyond the pair-shield baseline.

Put

\[
M_0:={b-f\over2}+E_U+p_U,
\qquad
E_U:=a_F+{x_A\over2}+{n_0+n_2\over2}.
\]

Then

\[
\boxed{
 d_C\ge M_0+2c_6+(c_6-1)_+.
}
\tag{CT.1}
\]

Here `d_C` is the complete contact infinitesimal-flex dimension modulo Euclidean motions. No nonlinear integration of the new two-dimensional internal-only spaces is claimed; only the already-known common-angle coordinate is exact finite motion.

Combining (CT.1) with the completed support-five/support-six classification gives

\[
\boxed{
\sigma_C
\le
2n_0+n_2+{n_1\over7}+{x_U\over7}+{c_6\over7}.
}
\tag{CT.2}
\]

Since (CT.1) implies

\[
 c_6\le {d_C-M_0+1\over3},
\]

we obtain

\[
\boxed{
\sigma_C
\le
2n_0+n_2+{n_1\over7}+{x_U\over7}
+{d_C-M_0+1\over21}.
}
\tag{CT.3}
\]

A convenient aggregate relaxation is

\[
\boxed{
\sigma_C
\le {Q\over7}+{26\over7}E_U
+{d_C-M_0+1\over21}.
}
\tag{CT.4}
\]

The gain is structural rather than a claimed replacement for the current live scalar envelope. Support six is no longer a free combinatorial obstruction: a degree-pure support-six block either disappears or spends two localized tangent dimensions plus its already-audited sealed common-angle coordinate. Since

\[
d_H+p_D=q-d_C-1,
\]

the last collapsed mechanism is now coupled directly to the diameter-row-nullity object already isolated as the remaining C-II bottleneck.

---

## 1. Internal closure matrix of a degree-pure support-six block

Run maximal two-anchor activation. Let `K` be a nonzero one-anchor relation component with exactly six faces, all of degree five. The one-anchor minimum-degree theorem gives relation degree at least four at every face. Each degree-five one-anchor face has exactly four residual internal train occurrences, so every residual internal occurrence is a relation edge. Simplicity forces

\[
R[K]=K_6\setminus M
\]

for a perfect matching `M`. Thus `K` has exactly twelve internal complete trains and no residual train leaves `K`: it is sealed.

The completed reciprocal analysis proves that every noncollapsed degree-pure support-six block is impossible. Hence any such live `K` is collapsed. That classification is needed in the component count below; the next rank observation uses only the sealed twelve-edge internal transport structure.

For each internal train `e=FG`, choose a coherent oriented unit side vector `r_e` at `F`; its occurrence at `G` is `-r_e`. Let `omega_e` be its train angular rate. Freeze every train not internal to `K`, including the six unique outside/activated anchor trains. The linearized closure equation at `F` is

\[
\sum_{e\ni F}\epsilon_{F,e}\,\omega_e J r_e=0,
\qquad
\epsilon_{F,e}=\pm1.
\tag{1.1}
\]

Let

\[
C_K:\mathbb R^{12}\to\mathbb R^{12}
\]

be the internal-only closure matrix, with two scalar rows per face.

For any fixed `w in R^2`, put the same dual row vector at every face:

\[
y_F=w\qquad(F\in K).
\]

For an internal train `e=FG`, its column pairing with this row vector is

\[
w\cdot Jr_e+w\cdot J(-r_e)=0.
\tag{1.2}
\]

Therefore

\[
\{(w,w,w,w,w,w):w\in\mathbb R^2\}
\subseteq\ker C_K^T.
\]

Hence

\[
\operatorname{rank}C_K\le10,
\qquad
\boxed{\dim\ker C_K\ge2.}
\tag{1.3}
\]

This is exact finite linear algebra. It does not use the numerical collapsed realization and does not assume that `C_K` has rank exactly ten.

---

## 2. The internal nullity gives genuine global contact infinitesimal flexes

Take `omega in ker C_K` and extend it by zero to every complete train outside the twelve internal trains of `K`.

- Every face in `K` closes to first order by definition of `ker C_K`.
- Every bounded exceptional face outside `K` sees no changed incident train.
- Every strict rhombus closes automatically because angular rate is constant along each complete train.

The audited train-angle closure theorem therefore integrates these edge-vector derivatives to a global contact infinitesimal flex. Thus `ker C_K` injects into the global contact-flex tangent.

These flexes are non-Euclidean after quotienting. A global infinitesimal rotation has one common nonzero angular rate on every complete train. Our modes have all six anchor-train rates zero and vanish on every train outside `K`. Therefore a mode in `ker C_K` can be Euclidean only if it is zero.

So every degree-pure collapsed support-six block contributes

\[
W_K\subset V_C,
\qquad
\boxed{\dim W_K\ge2,}
\tag{2.1}
\]

supported on its twelve relation-graph train coordinates.

This is only an infinitesimal theorem. The existing certified collapsed example has `rank C_K=10` and a regular two-dimensional exact anchor-fixed local closure family, but that one exact realization does not prove a universal constant-rank statement. Equation (2.1) does not promote every collapsed block to a two-dimensional finite manifold.

---

## 3. Add the sealed exact rotation without double-counting

Different active one-anchor relation components have disjoint face sets and disjoint relation-train sets. Hence their spaces `W_K` have disjoint train-coordinate support.

The pair-shield tangent freezes every residual-internal relation-graph train. Its `n_2` parameters live on two-anchor residual faces. A `p_U` mutually-parallel one-anchor coordinate may use a residual one-anchor train, but that train is parallel to the anchor at both endpoints and is therefore not an edge of the nonparallel relation graph `R`. Thus no pair-shield tangent direction changes an `R[K]` train, while every nonzero vector in `W_K` changes at least one such train. The sum of the `W_K` is therefore direct and disjoint from the pair-shield tangent.

Because `K` is sealed, the existing sealed-component theorem also gives an exact common-angle motion: rotate every complete train incident to `K` through the same small angle and use the activated pivot system to restore activated-face closures. On the twelve `R[K]` edges, the tangent of this motion is the all-ones angular-rate vector.

That all-ones internal vector is **not** in `W_K`. At a face `F`, setting all four internal rates to one gives

\[
\sum_{e\ni F}\epsilon_{F,e}Jr_e
=J\left(\sum_{e\ni F}\epsilon_{F,e}r_e\right)
=-J a_F\ne0,
\tag{3.1}
\]

because the four internal oriented sides sum to the negative of the nonzero anchor side `a_F`. Hence the common-angle direction adds a third train-coordinate direction beyond `W_K` before quotienting Euclidean rotation.

The hostile-audited sealed-component theorem already proves that the common-angle directions of distinct sealed components are independent of the pair-shield directions, with only one conservative possible universal overlap: the global all-train rotation. Therefore, for `c_6` collapsed support-six components, the complete contact tangent contains at least

\[
M_0+2c_6+(c_6-1)_+
\]

non-Euclidean dimensions. This proves (CT.1).

Equivalently, if `g_C:=d_C-M_0>=0`, then for `c_6>=1`,

\[
g_C\ge3c_6-1.
\]

For `c_6=0` the next bound is trivial, so in all cases

\[
\boxed{c_6\le{d_C-M_0+1\over3}.}
\tag{3.2}
\]

---

## 4. Support accounting after the support-six classification

Let `d_1` be the dimension of the one-anchor fiber after projecting `ker C_face^T` away from the `n_0` and `n_2` face blocks. The one-anchor theorem gives

\[
\sigma_C\le2n_0+n_2+d_1.
\tag{4.1}
\]

Let `c_*` be the number of one-anchor relation components on which that fiber has nonzero projection. Each connected component contributes at most one scalar fiber dimension, so

\[
d_1\le c_*.
\tag{4.2}
\]

Partition the active components into

- `c_6`: support six, all six faces degree five;
- `c_6^+`: support six, with at least one face of degree at least six;
- `c_7`: all remaining active components.

Support five is impossible. Every component counted by `c_6` is collapsed by the completed noncollapsed support-six exclusion. Every component counted by `c_6^+` contains a distinct face contributing at least one unit to

\[
x_U=\sum_{F\in U}(\deg F-5),
\]

so

\[
\boxed{c_6^+\le x_U.}
\tag{4.3}
\]

Every component in `c_7` has support at least seven. Since active components have disjoint one-anchor face sets,

\[
n_1\ge6c_6+6c_6^++7c_7.
\tag{4.4}
\]

Therefore

\[
\begin{aligned}
c_*
&=c_6+c_6^++c_7\\
&\le {n_1\over7}+{c_6+c_6^+\over7}\\
&\le {n_1\over7}+{c_6+x_U\over7}.
\end{aligned}
\tag{4.5}
\]

Combining (4.1), (4.2), and (4.5) proves (CT.2). Substituting (3.2) proves (CT.3).

---

## 5. Aggregate form

Use

\[
f=a_F+n_0+n_1+n_2,
\qquad
E_U=a_F+{x_A\over2}+{n_0+n_2\over2}.
\]

Coefficient comparison gives

\[
2n_0+n_2+{n_1\over7}+{x_U\over7}
\le
{f\over7}+{26\over7}E_U+{x_U\over7}.
\tag{5.1}
\]

The right-minus-left coefficients are `27/7` on `a_F`, zero on `n_0`, zero on `n_1`, `1` on `n_2`, and `13/7` on `x_A`. Since

\[
x_A+x_U=Q-f,
\]

we have `x_U<=Q-f`, so

\[
2n_0+n_2+{n_1\over7}+{x_U\over7}
\le {Q\over7}+{26\over7}E_U.
\tag{5.2}
\]

Combining (5.2) with (CT.3) proves (CT.4).

This aggregate relaxation is not asserted to dominate the current quarter-slope or degree-weighted-seed live frontiers. Eliminating `n_0` through `E_U` can make those older scalar lines stronger. The new result instead identifies where the last support-six equality shape must pay in the exact primal tangent.

---

## 6. Handoff to diameter locking

The exact tangent/stress duality gives

\[
\boxed{d_H+p_D=q-d_C-1.}
\tag{6.1}
\]

Hence a linear population of degree-pure support-six dual blocks cannot remain merely a dual combinatorial phenomenon. The completed reciprocal classification forces those blocks to be collapsed, and (CT.1) then forces the full contact tangent upward by almost three dimensions per block: two localized internal tangent directions and one sealed exact common-angle direction, with at most one global rotation lost overall. Equation (6.1) simultaneously drives the unresolved diameter topology/stress defect downward.

If `d_C-M_0=o(D)`, then (CT.1) forces `c_6=o(D)`. Up to the residual degree-excess population charged by `x_U`, almost every active one-anchor component then has support at least seven. At the exact endpoint `d_C=M_0`, (CT.1) gives `c_6=0`; if also `x_U=0`, the sharper unrelaxed bound (CT.2) becomes

\[
\sigma_C\le2n_0+n_2+{n_1\over7}.
\]

The remaining task is therefore no longer to find another local pentagon inequality for collapsed support six. A closing theorem must either integrate enough of the two-dimensional spaces `W_K` into finite source motions, exploit global train/rhombus holonomy to rule out the collapsed blocks, or show that the actual straight-line diameter graph cannot positively lock the enlarged full contact tangent under (6.1).

No theorem-state file is changed.

**Disposition:** every degree-pure collapsed support-six one-anchor component contributes at least two localized non-Euclidean contact-tangent dimensions and is also a sealed exact common-angle mechanism; after the single global-rotation allowance, `c_6` such blocks cost at least `2c_6+(c_6-1)_+` tangent dimensions beyond the pair-shield baseline. Support-six components with degree excess charge `x_U`. The finite bounds (CT.1)--(CT.4) replace the last free support-six combinatorial escape by the exact contact-tangent/diameter-locking gap. C-II remains open.
