# Target C-II — live terminal exact-flex reservoirs force diameter-locking matchings

**Date:** 2026-09-18  
**Status:** proof-only structural refinement; theorem-state authority unchanged  
**Scope:** terminal full-core Type-II FREE subsequences just above the certified `t` floor  
**Depends on:** correlated terminal gap `0.00704`; terminal transport/fan ladder; bounded-face convexity and endpoint fan theorem; train closure coordinates; canonical mixed infinitesimal rigidity; C65 relative-interior KKT positivity  
**Certificate:** `research/verify_target_c_free_terminal_live_flex_diameter_locking_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The correlated terminal theorem raises the certified floor to

\[
\mu_*+0.00704
=1.960302849540479\ldots,
\]

so the former `0.00669` three-spoke near-orbit window is empty. The active-diameter problem is nevertheless still live immediately above the new floor. The transport/fan theorem survives there and can be combined with exact train-angle integration without the near-orbit ear hypothesis.

Fix

\[
\varepsilon_0:=0.00710.
\]

For any terminal subsequence with

\[
\limsup t_D\le \mu_*+\varepsilon_0
=1.960362849540479\ldots,
\tag{L.1}
\]

the `k=3` transport/fan inequality gives

\[
\max\left\{
S/D,\ L_O/D,\ F^{\rm full}_{5,\ge3O}/D
\right\}
\ge c_{\rm live}-o(1),
\tag{L.2}
\]

where

\[
\boxed{
c_{\rm live}
=C_3(\varepsilon_0)
=0.140711505691587\ldots .
}
\tag{L.3}
\]

The new point is that both nonsingleton alternatives in (L.2) carry a simultaneous exact contact-flex product of the same linear dimension. Mixed rigidity then forces the active diameter derivative matrix on that product to have full column rank. C65 positivity makes its rows positively span the whole product tangent space. Hence, unless the singleton branch itself has density `c_live`, the source contains a linear matching from independent exact contact-flex coordinates to distinct actual diameter bars, together with a two-sided signed incidence payment of density `2c_live`.

The finite statement below does not use any lower bound on individual KKT multipliers.

---

## 1. Exact simultaneous flexes in the outer-loop branch

Let `L_O` be the number of complete stopped trains whose two terminal occurrences are on the outer face, including the singleton-bridge convention.

In the train-angle closure representation, an O--O train occurs in no bounded nonquadrilateral face. Its column in `C_face` is therefore zero. Rotate any chosen O--O train direction by a small angle. Every strict rhombus on that train still closes because opposite sides remain equal and parallel, and no bounded exceptional-face closure equation changes.

This is finite, not merely infinitesimal. Assign independently small angles to all `L_O` O--O train variables. All bounded faces close exactly, hence all graph cycles close exactly; fixing one core vertex integrates the rotated edge vectors to a contact-preserving realization. Finite strict lower-distance slack preserves all old noncontacts for a sufficiently small parameter box.

In the present window the transport identity gives

\[
E_{BB}\ge L_O+
\left(e_*-{5\over2}\varepsilon_0-o(1)\right)D,
\]

with

\[
e_*=0.341536286933018\ldots,
\]

so

\[
E_{BB}\ge L_O+(0.323786286933018\ldots-o(1))D.
\tag{1.1}
\]

Thus for large `D` at least one non-O--O train is fixed. The O--O parameter family cannot contain the global-rotation direction. It therefore gives an exact contact-flex product of dimension exactly `L_O` modulo Euclidean motions.

---

## 2. Exact simultaneous flexes in the three-spoke fan branch

Let

\[
Y:=F^{\rm full}_{5,\ge3O}.
\]

For every counted pentagon `P`, choose three distinct incident trains whose other terminal occurrence is the outer face. These three trains are distinct, non-singleton, and terminate at no other bounded exceptional face. Different selected pentagons use disjoint train variables because a pentagon-to-outer train has only one bounded terminal face.

Write the five oriented unit side vectors of `P` as

\[
u_1+u_2+u_3+u_4+u_5=0.
\]

After relabeling, rotate the chosen three outer-reaching train directions by angles `theta_1,theta_2,theta_3` and keep the other two fixed. Define

\[
\Phi_P(\theta_1,\theta_2,\theta_3)
=R_{\theta_1}u_1+R_{\theta_2}u_2+R_{\theta_3}u_3+u_4+u_5.
\tag{2.1}
\]

Canonical bounded-face convexity makes `P` a convex unit pentagon. A convex polygon has at most two sides in one projective direction, so the three chosen side directions are not all parallel. Therefore

\[
D\Phi_P(0)
=\begin{bmatrix}Ju_1&Ju_2&Ju_3\end{bmatrix}
\]

has rank two. The implicit-function theorem gives a one-dimensional nonconstant exact local closure curve through the origin.

Because each chosen train has only `P` as a bounded exceptional endpoint, changing those three directions affects no other exceptional-face equation. Rhombi close automatically. For different pentagons the variable triples are disjoint, so the local curves multiply. After fixing a core vertex and integrating edge vectors, the result is an exact contact-preserving product manifold of dimension `Y`. At least two train directions at each pentagon remain fixed, so no nonzero product tangent is global rotation.

Unlike the superseded near-orbit result, this construction claims no preferred ear-shortening sign. It needs only convexity and three outer-reaching spokes, so it remains valid in the live larger-`t` window.

---

## 3. General diameter-locking lemma for an exact contact-flex product

Let `M` be any exact contact-preserving product manifold in the canonical positive-contact core, of dimension `m` modulo Euclidean motions. Choose a tangent basis

\[
v_1,\ldots,v_m.
\]

Let `H` be the complete actual diameter-edge set used by C65. For `h=xy in H`, write

\[
r_h=p_y-p_x,
\qquad |r_h|=D,
\]

and define the `|H| x m` squared-diameter derivative matrix, up to the harmless factor two,

\[
G_{hj}:=r_h\cdot(v_j(y)-v_j(x)).
\tag{3.1}
\]

### Theorem 3.1 — full locking rank

\[
\boxed{\operatorname{rank}G=m.}
\tag{3.2}
\]

Indeed, if `Gc=0`, then `v=sum_j c_jv_j` annihilates every contact row and every actual diameter row. Canonical mixed infinitesimal rigidity makes `v` Euclidean. The tangent basis was chosen in the quotient, so `c=0`.

Choose the C65 relative-interior normalized KKT stress. Its actual-diameter coefficients satisfy

\[
\beta_h>0,
\qquad
\sum_h\beta_h=1.
\tag{3.3}
\]

Pairing stationarity with any contact-preserving tangent kills the contact part and gives

\[
\boxed{
\sum_{h\in H}\beta_hG_{h\bullet}=0.
}
\tag{3.4}
\]

Thus the rows `g_h in R^m` of `G` span `R^m` and have a strictly positive dependence.

### Corollary 3.2 — positive spanning

\[
\boxed{
0\in\operatorname{int}\operatorname{conv}\{g_h:h\in H\}.
}
\tag{3.5}
\]

If zero were on the boundary, a nonzero supporting functional `a` could satisfy `a dot g_h>=0` for every `h`. Multiplying by the positive `beta_h` and using (3.4) forces `a dot g_h=0` for every row. Since the rows span `R^m`, `a=0`, contradiction.

Consequently every nonzero exact-product tangent has active diameter derivatives of both signs.

---

## 4. Matching and signed-incidence payment

Form the bipartite support graph

\[
\Gamma\subset\{1,\ldots,m\}\times H
\]

by joining coordinate `j` to diameter bar `h` when `G_{hj}\ne0`.

### Theorem 4.1 — a matching saturates every flex coordinate

For every subset `J` of tangent coordinates, the corresponding columns of `G` are linearly independent, so

\[
|J|
=\operatorname{rank}G_{\bullet J}
\le |N(J)|.
\]

Hall's condition holds. Therefore `Gamma` contains a matching of size `m`. In particular, there are `m` pairwise distinct actual diameter edges, one with nonzero first derivative for each flex coordinate.

The positive KKT relation gives more. Every nonzero column contains both signs: if one column were nonnegative or nonpositive, its strictly positive weighted sum could vanish only if the whole column were zero, contradicting (3.2). Hence, with

\[
I_+:=\#\{(j,h):G_{hj}>0\},
\qquad
I_-:=\#\{(j,h):G_{hj}<0\},
\]

we have

\[
\boxed{
I_+\ge m,
\qquad
I_-\ge m,
\qquad
I_++I_-\ge2m.
}
\tag{4.1}
\]

Also, since zero is an interior point of a full-dimensional convex hull in `R^m`,

\[
\boxed{|H|\ge m+1.}
\tag{4.2}
\]

These constants are algebraically sharp: the rows

\[
e_1,\ldots,e_m,-(1,\ldots,1)
\]

have rank `m`, a positive all-ones dependence, exactly `m+1` rows, and exactly `2m` nonzero signed coordinate incidences.

---

## 5. Live terminal dichotomy at `epsilon=0.00710`

Apply the transport/fan trichotomy (L.2).

If

\[
S\ge(c_{\rm live}-o(1))D,
\]

we are in the still-unresolved singleton branch.

Otherwise, either `L_O` or `Y` is at least `(c_live-o(1))D`. Sections 1--2 then construct an exact contact-flex product of dimension

\[
m\ge(c_{\rm live}-o(1))D.
\tag{5.1}
\]

The diameter-locking theorem gives

\[
\boxed{
\operatorname{rank}G
\ge(0.140711505691587\ldots-o(1))D,
}
\tag{5.2}
\]

a matching to at least

\[
\boxed{
(0.140711505691587\ldots-o(1))D
}
\tag{5.3}

pairwise distinct actual diameter bars, and signed derivative-incidence counts

\[
\boxed{
I_+,I_-
\ge(0.140711505691587\ldots-o(1))D,
}
\tag{5.4}
\]

so

\[
\boxed{
I_++I_-
\ge(0.281423011383175\ldots-o(1))D.
}
\tag{5.5}
\]

In the fan branch the same `c_live D` pentagons supply at least

\[
3c_{\rm live}D
=(0.422134517074762\ldots-o(1))D
\]

distinct pentagon-to-outer train spokes.

Thus the live interval immediately above the new scalar floor has a sharper source-level alternative:

\[
\boxed{
\text{linear singleton trains}
\quad\text{or}\quad
\text{a linear exact-flex space positively locked by a linear diameter matching}.
}
\tag{5.6}
\]

---

## 6. Flex/stress dimension complementarity

Let `d_C` be the complete non-Euclidean contact-flex dimension and let

\[
d_H:=\dim\operatorname{aff}\mathcal P_H=s_Z-\sigma_C
\]

be the projected normalized diameter-stress affine dimension. The existing exact identities give

\[
d_C=T-\operatorname{rank}C_{face}-1,
\]

\[
T=h-s_Z+2f,
\qquad
\sigma_C=2f-\operatorname{rank}C_{face}.
\]

Therefore

\[
\boxed{d_C+d_H=h-1.}
\tag{6.1}
\]

Any constructed `m`-dimensional product tangent satisfies `m<=d_C`, so

\[
\boxed{d_H\le h-m-1.}
\tag{6.2}
\]

The projected-stress transversal theorem can consequently kill all normalized inherited mixed stresses using at most

\[
\boxed{d_H+1\le h-m}
\tag{6.3}
\]

selected diameter coordinates/endpoints. This does not supply the protected reinsertion capacity by itself, but it couples every linear exact-flex reservoir to a correspondingly smaller projected-stress complexity.

---

## 7. Remaining obstruction

The previous `0.00669` near-orbit exact-flex problem is obsolete after the `0.00704` correlated scalar gap. The live problem just above that floor is now reduced differently.

Either a linear singleton-train population survives, or the source carries a linear-dimensional exact contact-flex product whose active diameter derivatives form a full-rank positive-spanning system and contain a linear matching to distinct actual diameter bars. A bounded or sublinear diameter blocker set cannot lock the latter branch.

This still does not prove a feasible diameter descent. Positive spanning is exactly the first-order KKT obstruction. The next useful theorem must therefore do one of two things:

1. control the singleton branch directly; or
2. exploit geometry not used by the rank argument, especially reuse/order of one straight-line diameter bar across many localized fan or O--O coordinates, and show that the required signed support graph cannot be realized by the planar diameter thrackle in the same terminal near-disk source.

No theorem-state file is changed.

**Disposition:** proved a live larger-`t` exact-flex/diameter-locking dichotomy, a linear active-diameter matching and signed-incidence payment, and exact flex/stress dimension complementarity; C-II remains open.
