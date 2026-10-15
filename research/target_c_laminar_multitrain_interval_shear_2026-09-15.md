# Target C-II — exact laminar multi-train shear and interval diameter rows

**Date:** 2026-09-15
**Status:** proof-only exact finite structural theorem
**Scope:** any finite family of pairwise disjoint non-singleton outer-to-outer stopped trains whose complement-dual edges lie on one simple path
**Dependencies:** audited finite stopped-train/cutset/shear primitives; elementary topology of proper crosscuts in a disk
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current small-leaf rectangle supplies a consecutive block of pairwise disjoint
outer-to-outer leaf trains on one simple path of the complement dual tree. Section 157
uses each train separately. The missing finite statement is that all of those exact
one-train shears can be used **simultaneously**, with no contact error and with a very
rigid form for every source-pair displacement.

Let

\[
\tau_1,\ldots,\tau_m
\]

be pairwise disjoint non-singleton outer-to-outer complete stopped trains whose proper centerline
crosscuts correspond to consecutive edges of one simple path in their complement-dual
tree. Then there are shore choices and unit contact vectors `u_i` such that, for every
parameter vector

\[
\theta=(\theta_1,\ldots,\theta_m),
\]

the full source motion

\[
\boxed{
 p_v(\theta)
 =p_v+
 \sum_{i:\,v\in S_i}
 \bigl(R_{\theta_i}u_i-u_i\bigr)
}
\tag{IS.1}
\]

preserves **every old unit contact exactly**. For all sufficiently small `theta`, it
also preserves every strict old noncontact inequality.

Moreover the selected cuts admit layers `0,...,m`. If source vertices `x,y` lie in
layers `a<b`, then their exact relative displacement is

\[
\boxed{
 p_y(\theta)-p_x(\theta)
 =p_y-p_x+
 \sum_{i=a+1}^{b}
 \bigl(R_{\theta_i}u_i-u_i\bigr).
}
\tag{IS.2}
\]

Thus every source-pair row, including every active diameter row, is supported on one
**contiguous interval** of train coordinates.

This is stronger than the previously audited collection of one-train shears. It is a
finite multi-parameter contact-preserving motion, not merely an infinitesimal span.

---

## 1. The dual-path cuts have laminar shores

Represent each selected non-singleton outer-to-outer train by its audited proper centerline crosscut
of the closed topological disk bounded by the actual outer face. The selected
crosscuts are pairwise disjoint. Their complement region/crosscut dual is therefore a
tree.

By hypothesis the selected train edges form one simple dual path. Write its successive
region vertices and train edges as

\[
R_0\;\xleftrightarrow{\tau_1}\;R_1
\;\xleftrightarrow{\tau_2}\;\cdots\;
\xleftrightarrow{\tau_m}\;R_m.
\tag{IS.3}
\]

Delete one dual edge `tau_i`. The dual tree splits into two components. Let `S_i` be
the geometric shore consisting of source vertices lying in regions on the `R_m` side,
and let `T_i` be the complementary shore. Interchanging the two shore labels in the
audited cutset lemma is allowed, so this is a legitimate shore choice for every
selected train.

The `R_m`-side components are nested:

\[
S_1\supseteq S_2\supseteq\cdots\supseteq S_m.
\tag{IS.4}
\]

The audited outer-to-outer cutset lemma says that the **only contact edges** with one
endpoint in `S_i` and one endpoint in `T_i` are the physical contact edges of
`tau_i`.

Choose `u_i` so every contact of `tau_i`, oriented from `T_i` into `S_i`, has unit
contact vector `u_i`.

---

## 2. Exact simultaneous contact preservation

Put

\[
\Delta_i(\theta_i):=R_{\theta_i}u_i-u_i.
\tag{IS.5}
\]

Define the full-source placement by (IS.1). This is simply a sum of translations of
nested shores. No vertex is discarded; contact-isolated source points receive the
same shore translations as every other point in their geometric region.

Take any old unit contact `xy`.

### Case 1: `xy` belongs to selected train `tau_j`

For every `i\ne j`, the cutset lemma for `tau_i` implies that `x,y` lie on the same
side of cut `i`; otherwise `xy` would itself be an edge of `tau_i`. For cut `j`,
orient the contact from `T_j` to `S_j`, so

\[
p_y-p_x=u_j.
\]

Hence all shear increments except the `j`th cancel from the relative displacement and

\[
\begin{aligned}
p_y(\theta)-p_x(\theta)
&=u_j+\Delta_j(\theta_j)\\
&=R_{\theta_j}u_j.
\end{aligned}
\tag{IS.6}
\]

Therefore its length remains exactly one.

### Case 2: `xy` belongs to no selected train

For every selected cut `i`, the cutset lemma implies that `x,y` lie on the same shore.
Every translation in (IS.1) cancels, so

\[
p_y(\theta)-p_x(\theta)=p_y-p_x.
\tag{IS.7}
\]

Thus every old contact is preserved exactly for every parameter vector for which the
formula is evaluated.

The source is finite. Every old noncontact has strict initial distance greater than
one, and every pair distance is continuous in `theta`. Hence there is a neighborhood
of `theta=0` in which all old noncontacts remain strictly longer than one.

We have proved:

### Theorem IS.1 — exact laminar multi-train shear

For any selected dual-path family `tau_1,...,tau_m`, equation (IS.1) gives an exact
`m`-parameter contact-preserving finite motion of the full source. For all sufficiently
small parameters the moved source remains unit-separated.

No diameter monotonicity is claimed.

---

## 3. Layer index and interval support

Delete all selected dual edges from the complement tree. The remaining forest has
exactly `m+1` components. The component containing `R_j` will be called layer `j`;
all off-path branches attached to `R_j` belong to the same layer.

The audited centerline crosscuts pass through contact-edge midpoints rather than source
vertices, so every source vertex lies on a definite side of every selected cut. Define

\[
\ell(v):=\#\{i:v\in S_i\}.
\tag{IS.8}
\]

Because the shores are nested, `ell(v)` lies in `{0,...,m}` and

\[
v\in S_i\quad\Longleftrightarrow\quad i\le\ell(v).
\tag{IS.9}
\]

If `ell(x)=a<b=ell(y)`, then cut `i` separates `x,y` exactly when

\[
a<i\le b.
\tag{IS.10}
\]

Subtracting (IS.1) for the two vertices therefore gives the exact interval formula
(IS.2).

If the orientation of the pair is reversed, the same interval appears with the
opposite sign.

### Corollary IS.2 — active diameter rows are interval rows

For an actual diameter pair `h=xy`, orient it so `ell(x)<=ell(y)` and write

\[
r_h=p_y-p_x,
\qquad
I_h=\{\ell(x)+1,\ldots,\ell(y)\}.
\]

Then under the simultaneous shear

\[
\boxed{
 r_h(\theta)=r_h+\sum_{i\in I_h}\Delta_i(\theta_i).
}
\tag{IS.11}
\]

Hence the active-diameter constraint matrix restricted to these exact train
coordinates has consecutive-interval support in every row.

This is an exact finite statement. It does not use asymptotic phase purity, KKT
weights, or a response theorem.

---

## 4. Exact first and second variations

For later use, differentiate (IS.11) at `theta=0`. For `i\in I_h`,

\[
{\partial r_h\over\partial\theta_i}(0)=Ju_i,
\qquad
{\partial^2 r_h\over\partial\theta_i^2}(0)=-u_i,
\tag{IS.12}
\]

and mixed second derivatives of the vector `r_h` vanish.

For the squared length

\[
L_h(\theta):=|r_h(\theta)|^2,
\]

we get

\[
\boxed{
{\partial L_h\over\partial\theta_i}(0)
=2r_h\cdot Ju_i
\quad(i\in I_h),
}
\tag{IS.13}
\]

\[
\boxed{
{\partial^2 L_h\over\partial\theta_i^2}(0)
=2-2r_h\cdot u_i
\quad(i\in I_h),
}
\tag{IS.14}
\]

and for distinct `i,j\in I_h`,

\[
\boxed{
{\partial^2 L_h\over\partial\theta_i\partial\theta_j}(0)
=2u_i\cdot u_j.
}
\tag{IS.15}
\]

All derivatives are zero in a coordinate outside `I_h`.

Along one scalar direction `theta_i=t c_i`, put

\[
A_h=\sum_{i\in I_h}c_iJu_i,
\qquad
B_h=\sum_{i\in I_h}c_i^2u_i.
\tag{IS.16}
\]

Then

\[
r_h(t)=r_h+tA_h-{t^2\over2}B_h+O(t^3)
\tag{IS.17}
\]

and

\[
\boxed{
L_h(t)=D^2
+2t\,r_h\cdot A_h
+t^2\bigl(|A_h|^2-r_h\cdot B_h\bigr)
+O(t^3)
}
\tag{IS.18}
\]

for every active diameter row.

Thus the remaining diameter-feasibility problem on a laminar O--O block is an
interval-sum max-function problem with completely explicit finite curvature.

---

## 5. Application to the live small-leaf rectangle

The corrected small-leaf rectangle theorem constructs its leaf block as consecutive
edges of one simple complement-dual backbone path. Therefore Theorem IS.1 applies
without any additional extraction.

For the fixed rectangle point this gives more than

\[
0.003D-o(D)
\]

exact simultaneous leaf-shear coordinates. The Pareto theorem gives, for any fixed
`rho<rho_max`, a consecutive leaf block of length `rho D-o(D)`; in particular the
balanced choice supplies more than

\[
0.00779D-o(D)
\]

coordinates while retaining a linear common center family.

After the phase-collapse trimming, the selected leaf contact directions also lie in an
`O(D^{-1})` projective window. Therefore the interval rows (IS.13) are not arbitrary
consecutive-ones rows: their nonzero coefficients come from diameter vectors paired
with an almost common leaf normal.

This is the interface needed for a genuine simultaneous-shear attack. A diameter
edge may brace many nested cuts, but it can do so only through one contiguous interval,
and its first and second variations across that whole interval are linked by
(IS.13)--(IS.18).

---

## 6. Scope audit and non-conclusions

- The theorem uses a **dual-path** family, not an arbitrary pairwise noncrossing O--O
  family. Branching complement topology is retained outside the selected path.
- No claim is made that the selected cuts are equally spaced or that the rhombus
  rectangle is an affine lattice.
- The finite motion preserves all old contacts exactly and all strict old noncontacts
  for sufficiently small parameters. It does **not** automatically preserve the
  diameter bound.
- A diameter edge can still cross a macroscopic interval of selected cuts. The new
  information is the exact interval-sum formula, not a distinct-edge count.
- KKT positivity and Section 157 are not used in the proof; they can now be imposed on
  top of this exact coordinate system.

**Disposition:** proved proof-only exact laminar multi-train shear / interval-row
reduction. C-II and Level I remain open.
