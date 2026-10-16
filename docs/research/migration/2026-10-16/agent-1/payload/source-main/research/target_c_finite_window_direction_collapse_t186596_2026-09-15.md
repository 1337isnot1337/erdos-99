# Target C-II — a finite-window strip and switching-direction collapse through `t<=1.86596`

**Date:** 2026-09-15  
**Status:** proof-only high-`t` structural strengthening  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.86596`  
**Dependencies:** hostile-audited paired-remainder path through `1.86596`; finite-defect strip ledgers; outer-walk identity; adjacent switching order; global minimum-diameter packing asymptotics  
**Certificate:** `research/verify_target_c_finite_window_defect_strip_t186596.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The finite-defect theorem controls switching rows, train terminals, and KKT switch mass
on one adjacent O--O layer.  A separate outer-boundary average can be added to the same
cost.  The result is one **single** nonhub strip satisfying

\[
\boxed{
N_i+L_i+D B_i+G_i<1{,}036{,}400,
}
\tag{FW.1}
\]

where `G_i` is the total occurrence-counted metric length of the two middle-layer outer
boundary windows.

Hence every switching diameter has its middle endpoint in two boundary-walk intervals
of total length below `1,036,400`, independent of `D`.  Since normalized source hulls
of global minimizers converge to the diameter-one disk, actual diameter pairs whose
middle endpoints lie in the same fixed-length window have one common limiting oriented
direction.

Therefore:

\[
\boxed{
\text{the switching diameter set has at most two asymptotic oriented-direction clusters.}
}
\tag{FW.2}
\]

If both left- and right-switch rows occur, the adjacent one-arc theorem puts all
switching middle endpoints in one of the two windows, and

\[
\boxed{
\max_{h,k\in H_{sw}}\left|{n_h\over D}-{n_k\over D}\right|\to0.
}
\tag{FW.3}
\]

In that mixed-switch case the normalized nonzero KKT layer reaction itself converges to
the same oriented diameter ray.

---

## 1. The outer windows form another additive path ledger

Use the simple path of selected O--O crosscuts

\[
\tau_1,\ldots,\tau_m,
\qquad
m>{17\over10^6}D-o(D)
\tag{FW.4}
\]

from the hostile-audited paired-remainder endpoint theorem.  For each consecutive pair
`tau_i,tau_{i+1}`, let `M_i` be the intervening complement region.  Its trace on the
occurrence-counted outer facial circle is the disjoint union of two open arcs

\[
J_i^+,\qquad J_i^-.
\]

Put

\[
G_i=\operatorname{len}_{out}(J_i^+)
+\operatorname{len}_{out}(J_i^-).
\tag{FW.5}
\]

The interiors of these arcs are disjoint from strip to strip, because pairwise disjoint
crosscuts on a simple dual path divide the disk linearly.  If `b` is the total
occurrence-counted outer contact-walk length, then

\[
\boxed{\sum_iG_i\le b.}
\tag{FW.6}
\]

Every outer contact-edge occurrence has Euclidean length one, so `G_i` is also the
ordinary path-metric length of the two boundary-walk portions, including the natural
half-edge endpoint pieces.

---

## 2. Uniform outer-walk density at the high endpoint

Write

\[
\delta={d_{out}\over D}.
\]

The distinguished-route identity gives

\[
{b\over D}=\pi+\delta+o(1).
\tag{FW.7}
\]

On the paired-remainder branch use

\[
C_{76}=2\sqrt{\pi\over2\sqrt3}+0.0076.
\]

The same residual envelope used in the `1.86596` path certificate gives

\[
2\delta+{\kappa\over2}+h
={9t\over2}-2\pi-C_{76},
\qquad \kappa,h\ge0.
\tag{FW.8}
\]

Thus at

\[
T=1.86596
\]

\[
\delta\le\delta_{max}
:={1\over2}\left({9T\over2}-2\pi-C_{76}\right)+o(1).
\tag{FW.9}
\]

The exact certificate proves

\[
\boxed{
\delta_{max}<0.100705,
\qquad
{b\over D}<3.2423+o(1).
}
\tag{FW.10}
\]

---

## 3. Joint finite-window / finite-defect averaging

For every eligible nonhub internal path region define

\[
C_i^*=N_i+L_i+D B_i+G_i.
\]

The finite-defect ledgers give

\[
\sum_iN_i\le2\pi D,
\tag{FW.11}
\]

\[
\sum_iL_i\le(10T-4\pi)D+o(D),
\tag{FW.12}
\]

and

\[
\sum_iD B_i\le2D.
\tag{FW.13}
\]

Adding (FW.6)--(FW.10),

\[
\sum_iC_i^*
\le
\bigl[10T-2\pi+2+\pi+\delta_{max}\bigr]D+o(D).
\tag{FW.14}
\]

The exact companion certificate proves

\[
\boxed{
{10T-\pi+2+\delta_{max}\over17/10^6}<1{,}036{,}395.
}
\tag{FW.15}
\]

Delete the one Helly hub region and the two end regions.  Their number is `O(1)` and is
absorbed by the `o(D)` denominator.  Hence for all sufficiently large sources one
nonhub internal strip satisfies (FW.1).

In particular,

\[
\boxed{G_i<1{,}036{,}400.}
\tag{FW.16}
\]

---

## 4. Switching middle endpoints lie in fixed-size boundary patches

For the selected adjacent pair, every switching diameter has exactly one endpoint in
the moving middle layer:

- a left switch joins the left layer to the middle layer;
- a right switch joins the middle layer to the right layer.

Every actual diameter endpoint is an extreme point of the full source convex hull, hence
appears on the actual outer boundary.  The middle endpoint must therefore lie in

\[
J_i^+\cup J_i^-.
\]

Equation (FW.16) gives

\[
\boxed{
\operatorname{len}_{out}(J_i^+)
+\operatorname{len}_{out}(J_i^-)
<1{,}036{,}400.
}
\tag{FW.17}
\]

For two source vertices on one such interval, Euclidean distance is no larger than the
intervening outer-walk length.  Thus the set of switching middle endpoints in each
window has Euclidean diameter `O(1)=o(D)`.

If both switch orientations occur, the hostile-audited one-arc theorem places every
participating middle endpoint on one common middle arc.  Thus in the mixed case **all**
switching middle endpoints lie in one set of Euclidean diameter `O(1)`.

---

## 5. Global source hulls converge to the disk

Let `K_D=conv(A_D)` for any sequence of global minimum-diameter sources with
`D->infinity`.  The standard packing asymptotic is

\[
{n_D\over D^2}\to\Delta_2={\pi\over2\sqrt3}.
\tag{FW.18}
\]

Finite Oler gives

\[
{\sqrt3\over2}(n_D-1)
\le \operatorname{area}K_D
+{\sqrt3\over4}\operatorname{per}K_D.
\tag{FW.19}
\]

Since a planar convex body of diameter `D` has perimeter at most `pi D`, dividing by
`D^2` and using (FW.18) yields

\[
\liminf {\operatorname{area}K_D\over D^2}\ge{\pi\over4}.
\]

The isodiametric inequality gives the reverse bound. Therefore

\[
{\operatorname{area}K_D\over D^2}\to{\pi\over4}.
\tag{FW.20}
\]

By Blaschke compactness, every translated Hausdorff limit of `D^{-1}K_D` has diameter
at most one and area `pi/4`. Equality in the planar isodiametric theorem forces every
such limit to be the radius-`1/2` disk. Hence, after suitable translations,

\[
\boxed{D^{-1}K_D\to B_{1/2}}
\tag{FW.21}
\]

in Hausdorff distance.

---

## 6. Fixed endpoint patches force diameter-direction collapse

### Lemma FW.1

Let

\[
x_Dy_D,\qquad x'_Dy'_D
\]

be actual diameter pairs, both oriented toward the first endpoint:

\[
|x_D-y_D|=|x'_D-y'_D|=D.
\]

If

\[
|x_D-x'_D|=o(D),
\]

then

\[
\boxed{
\left|{x_D-y_D\over D}-{x'_D-y'_D\over D}\right|\to0.
}
\tag{FW.22}
\]

### Proof

If not, pass to a subsequence with a fixed positive direction separation.  Use the
translations in (FW.21) and compactness to obtain

\[
{x_D\over D},{x'_D\over D}\to x,
\qquad
{y_D\over D}\to y,
\qquad
{y'_D\over D}\to y'.
\]

The endpoint hypothesis gives the same limit `x` for the two first endpoints.  All
limits lie in `B_{1/2}`, while the diameter equalities give

\[
|x-y|=|x-y'|=1.
\]

A point of the radius-`1/2` disk has at most one other disk point at distance one: the
antipodal boundary point.  Thus `y=y'`, contradicting the assumed direction separation.
`\square`

The same compactness proof is uniform over any family whose oriented first endpoints
have diameter `o(D)`.

---

## 7. Apply the lemma to the finite windows

Orient every switching diameter from its exterior endpoint toward its middle-layer
endpoint and write

\[
n_h=Dd_h,
\qquad |d_h|=1.
\]

For each nonempty window `J_i^sigma`, Lemma FW.1 gives a unit vector `nu_D^sigma` such
that

\[
\boxed{
\max_{h:\,m_h\in J_i^\sigma}|d_h-\nu_D^\sigma|=o(1).
}
\tag{FW.23}
\]

Thus there are at most two asymptotic oriented switching-diameter clusters, proving
(FW.2).

If both left and right switch orientations occur, all middle endpoints lie in one common
window, so there is one unit vector `nu_D` with

\[
\boxed{
\max_{h\in H_{sw}}|d_h-\nu_D|=o(1),
}
\tag{FW.24}
\]

which proves (FW.3).

---

## 8. The mixed-switch KKT reaction shares the same limiting ray

In the mixed case the exact layer reaction is

\[
G=\sum_{h\in H_{sw}}\beta_hn_h
=D\sum_h\beta_hd_h,
\qquad \beta_h>0.
\tag{FW.25}
\]

Put

\[
B=\sum_{h\in H_{sw}}\beta_h>0.
\]

From (FW.24),

\[
\left|{G\over DB}-\nu_D\right|
\le
{1\over B}\sum_h\beta_h|d_h-\nu_D|
=o(1).
\tag{FW.26}
\]

Hence `|G|/(DB)->1` and

\[
\boxed{
{G\over|G|}-\nu_D\to0.
}
\tag{FW.27}
\]

So in the mixed-switch branch the exact nonzero reaction, its angular-extreme
one/two-bar representation, and every actual switching diameter all collapse to one
oriented diameter direction.

This is still qualitative.  No rate is claimed and no finite deformation amplitude is
inferred from `o(1)` direction collapse.

**Disposition:** proved one finite-window, finite-defect, low-KKT strip through
`t<=1.86596`, with at most two limiting switching-diameter rays and one ray in the
mixed-switch case.  The remaining local obstruction is a degenerate one-/two-ray finite
jam, not a macroscopically multi-directional diameter interface. C-II and Level I remain
open.
