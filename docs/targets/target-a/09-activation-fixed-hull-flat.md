# Target A — activation bridge forest and fixed-hull affine flat

This module continues the audited Target A frontier after Sections 154--155. It corrects
the historical limitation stated after Lemma 144.1 and extracts finite, unweighted
geometry from the monotone activation sequence. In the very-super-boundary subbranch
it composes with Section 155 to place the activation flat and both Hall shadows in one
fixed hull, but it does not yet prove the Target A Schur inequality.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 156. Monotone activation creates a bridge forest and a fixed-hull affine flat

Use the monotone activation sequence of Theorem 142.1, but write its number of
steps as \(\ell\) to avoid conflict with the canonical response quantity
\(s=\Delta_\Lambda-d_{\rm int}\):

\[
A_0,A_1,\ldots,A_\ell.
\tag{156.1}
\]

At step \(i\), the currently strict point \(r_i\) moves, all other labels stay
fixed, and exactly one new active pair

\[
e_i=r_iq_i
\tag{156.2}
\]

is created. Put

\[
E_{\rm new}=\{e_1,\ldots,e_\ell\},
\qquad
M=\{r_1,\ldots,r_\ell\},
\tag{156.3}
\]

and let \(d_D\) be the number of created diameter pairs. Let
\(A^*=A_\ell\), \(H^*=\operatorname{conv}A^*\), and assume \(D>1\) and that
\(H^*\) is full-dimensional, as in the large-cardinality Target A setting.

## 156.1 The complete activation set is a bridge forest

> **Theorem 156.1 (activation attachment forest).** The creators \(r_i\) are
> distinct, \(|M|=|E_{\rm new}|=\ell\), and the following statements hold.
>
> 1. If \(q_i\in M\), then \(q_i=r_j\) for some \(j<i\).
> 2. \(E_{\rm new}\) is a forest. Every edge of \(E_{\rm new}\) is a bridge in
>    the full active graph of \(A^*\), including both unit and diameter pairs.
> 3. Every component of this forest meets the nonisolated part of the active
>    graph of \(A_0\) in at most one vertex.
> 4. The rigidity rows of all created pairs are linearly independent:
>    \[
>    \boxed{\operatorname{rank}R_{E_{\rm new}}=\ell.}
>    \tag{156.4}
>    \]

### Proof

Immediately before step \(i\), the creator \(r_i\) is strict and hence is an
isolated vertex of the current active graph. The new edge \(e_i\) therefore attaches
an isolated vertex to one other vertex. It makes \(r_i\) non-strict, and persistence
of active pairs prevents \(r_i\) from ever becoming strict again. Thus no creator is
moved twice.

If \(q_i\) is strict immediately before the step, the new edge also makes \(q_i\)
non-strict, so \(q_i\) cannot be a later creator. If it is already non-strict and
belongs to \(M\), it must have been moved earlier. This proves item 1.

Starting from the active graph of \(A_0\), every step adds one edge incident to a
currently isolated vertex. Such an addition creates no cycle, makes the new edge a
bridge, cannot destroy the bridge status of an earlier added edge, and cannot join
two previously nontrivial components. Induction proves items 2 and 3. It also gives
\(|M|=|E_{\rm new}|=\ell\).

Finally, a forest of nonzero Euclidean edge vectors has independent rigidity rows:
in a putative row dependence, inspect the two coordinate columns of a leaf and remove
its incident edge, then iterate. This is the leaf-elimination proof of Lemma 145.1 and
applies equally to edges of length \(1\) and \(D\). Hence (156.4) follows. \(\square\)

Theorem 156.1 supersedes the historical sentence after Lemma 144.1 saying that a
recorded activation edge might later become non-bridging. Later activation edges also
attach currently isolated vertices, so they cannot complete a cycle through an older
activation edge.

## 156.2 A same-hull affine family of global minimizers

Let

\[
b=|M\cap\partial H^*|,
\qquad
I=M\cap\operatorname{int}H^*.
\tag{156.5}
\]

Every endpoint of a diameter pair lies on \(\partial H^*\). Consequently every
created diameter pair has both endpoints fixed if velocities are supported on \(I\).

For a velocity field \(v=(v_x)_{x\in A^*}\), define

\[
\mathcal L_{\rm act}=
\left\{
v:
\begin{array}{l}
v_x=0\quad(x\notin I),\\[2mm]
(p_x-p_y)\mathbin{\cdot}(v_x-v_y)=0\\
\hfill(xy\in E_{\rm new},\ |p_x-p_y|=1)
\end{array}
\right\}.
\tag{156.6}
\]

> **Theorem 156.2 (fixed-hull activation flat).** There is a neighborhood
> \(U\) of zero in the linear space \(\mathcal L_{\rm act}\) such that
> \[
> A^*(v)=\{p_x+v_x:x\in A^*\}
> \tag{156.7}
> \]
> is, for every \(v\in U\), a triangle-free global minimizer of the same
> cardinality and diameter \(D\), and
> \[
> A^*(v)\subseteq H^*.
> \tag{156.8}
> \]
> Moreover
> \[
> \boxed{
> \dim\mathcal L_{\rm act}
> \ge \max\{0,\ell-2b+d_D\}.
> }
> \tag{156.9}
> \]

### Proof

There are \(2|I|=2(\ell-b)\) velocity coordinates. Only the
\(\ell-d_D\) created unit pairs contribute equations in (156.6). Therefore

\[
\dim\mathcal L_{\rm act}
\ge
2(\ell-b)-(\ell-d_D)
=\ell-2b+d_D,
\tag{156.10}
\]

with the trivial lower bound zero if the displayed number is negative.

No point of \(M\) is incident to an active pair of \(A_0\): such a pair persists
through the sequence and would prevent that point from being strict when moved.
Thus every old active pair has both endpoints outside \(M\) and is fixed by every
\(v\in\mathcal L_{\rm act}\). Every created diameter pair also has both endpoints
on \(\partial H^*\) and is fixed.

For a created unit pair \(xy\), equation (156.6) gives the exact identity

\[
\begin{aligned}
|(p_x+v_x)-(p_y+v_y)|^2
&=|p_x-p_y|^2
 +2(p_x-p_y)\mathbin{\cdot}(v_x-v_y)
 +|v_x-v_y|^2\\
&=1+|v_x-v_y|^2\ge1.
\end{aligned}
\tag{156.11}
\]

Every pair that is not active in \(A^*\) has distance strictly between \(1\) and
\(D\). There are finitely many such pairs, so all of their inequalities persist in
a sufficiently small neighborhood of zero. Points in \(I\) have positive distance
from \(\partial H^*\), while every other point is fixed. After shrinking the same
neighborhood, (156.8) therefore holds.

An old diameter pair of \(A_0\) is fixed and still has length \(D\). Hence every
configuration (156.7) has diameter exactly \(D\). It is unit-separated by
(156.11) and the strict-slack argument, so global minimality follows from
\(D=D(|A^*|)\).

Finally, the unit-contact graph of \(A^*(v)\) is a subgraph of the unit-contact
graph of \(A^*\): old contacts are fixed, created contacts may open, and no inactive
pair reaches unit distance in the chosen neighborhood. Since \(A^*\) is
triangle-free, so is \(A^*(v)\). \(\square\)

The boundary loss in (156.9) is boundary-order. If
\(h=|A^*\cap\partial H^*|\), cyclic order along the convex boundary and unit
separation give

\[
h\le \operatorname{per}(H^*)\le\pi D,
\tag{156.12}
\]

so \(b\le h\le\lfloor\pi D\rfloor\).

## 156.3 Quantitative source consequence

Let \(R_0\) be a specified set of \(r_0\) strict rattlers in \(A_0\). At
termination every member of \(R_0\) is incident to a created active pair. One
created pair has at most two endpoints in \(R_0\), and therefore

\[
\ell\ge\left\lceil\frac{r_0}{2}\right\rceil.
\tag{156.13}
\]

Combining (156.9), (156.12), and (156.13) gives

\[
\boxed{
\dim\mathcal L_{\rm act}
\ge
\max\left\{0,
\left\lceil\frac{r_0}{2}\right\rceil
-2\lfloor\pi D\rfloor
\right\}.
}
\tag{156.14}
\]

Apply this after the maximal triangle-free source extension of Section 121. Its
retained strict set satisfies

\[
|R_B|\ge\rho-5\widehat p_H.
\tag{156.15}
\]

The terminal activated representative therefore has a fixed-terminal-hull affine
family of dimension at least

\[
\boxed{
\max\left\{0,
\left\lceil
\frac{\max\{0,\rho-5\widehat p_H\}}{2}
\right\rceil
-2\lfloor\pi D\rfloor
\right\}.
}
\tag{156.16}
\]

Since \(\widehat p_H=O(D)\), this dimension is super-boundary whenever
\(\rho=\omega(D)\). Unlike Theorem 143.1, diameter activations do not have to be
discarded: their endpoints are frozen on the terminal hull boundary, and the exact
dimension count already absorbs them.

The hull in (156.16) is \(\operatorname{conv}B^*\), the hull of the terminal
activated representative. It need not be the original source hull. Any scaffold or
capacity flag used after this normalization must be rebuilt for the new
representative and its terminal hull.

## 156.4 Composition with very-super-boundary alignment

Section 155 applies to every genuine global minimizer with the stated cardinality and
diameter data, not only to the representative used when that section was proved.
It can therefore be applied to the terminal activated representative. This gives a
precise composition in the very-super-boundary subbranch.

> **Corollary 156.3 (coembedded affine two-shadow family).** Suppose the initial
> source has a specified strict-rattler set of size \(\rho=N-m\), and suppose
> \[
> \rho\ge\frac{\pi D}{2}
> +\frac{4D}{c}\left(1+3\,3^{1/4}\sqrt D\right),
> \qquad c=\frac{2\sqrt3}{\pi}.
> \tag{156.17}
> \]
> Apply monotone activation to that source and let \(A^*\), \(H^*\), and
> \(\mathcal L_{\rm act}\) be as above. Then an independently chosen smaller
> optimum \(X_m\), its unit collar, and a prescribed-phase inner scaffold
> \(Y_{\rm in}\) can be placed inside \(H^*\). For every sufficiently small
> \(v\in\mathcal L_{\rm act}\),
> \[
> \operatorname{conv}A^*(v)=H^*,
> \tag{156.18}
> \]
> and, with \(\widehat p_{H^*}=\alpha_1(H^*)-N\),
> \[
> \boxed{
> \nu(X_m,A^*(v))\ge m-\widehat p_{H^*},
> \qquad
> \nu(Y_{\rm in},A^*(v))
> \ge |Y_{\rm in}|-\widehat p_{H^*}.
> }
> \tag{156.19}
> \]
> Thus the super-boundary affine source family and both Hall shadows coexist in
> one fixed container.

### Proof

The terminal set \(A^*\) is an \(N\)-point global minimizer of diameter \(D\), so
the Bonnesen alignment theorem of Section 155 applies to \(H^*\) with the same
\(N,m,\rho,D\). Under (156.17), it places \(X_m\), its unit collar, and hence
the prescribed-phase inner scaffold inside \(H^*\).

Every point of \(A^*\cap\partial H^*\) is fixed in Theorem 156.2. In particular
the hull vertices are fixed. Since all perturbed points remain in \(H^*\), the
perturbed hull is still \(H^*\). The exact same-source Hall theorem then applies,
for each \(v\), to the two displayed unit-separated subsets of the same hull, with
the fixed slack \(\widehat p_{H^*}\). This proves (156.19). \(\square\)

Corollary 156.3 is a genuine composition with Sections 154--155, not a coordinate
identification of arbitrary source and scaffold constructions. It still does not
make the two matchings compatible or identify their composition with the Schur
response. The Section 157 backbone obstruction is likewise compatible with this
coembedding, but its captured-rattler set still needs a compatibility/relocation
argument.

## 156.5 Exact localization of a persistent capacity transition

The fixed-hull conclusion permits a clean interaction with the capacity flag, but it
does not by itself make every transition triangle-free.

Fix a capacity endpoint \(X_{\max}\subset H^*\). Choose a relatively open chamber
\(\Omega\subset U\) on which the strict conflict graph between \(A^*(v)\) and
\(X_{\max}\) is constant, after excluding the finitely many nonidentical unit-distance
walls. Build a fixed-basis exchange flag in that chamber. For one of its exchange
sets write

\[
P(v)=(A^*(v)\setminus W)\cup X',
\qquad v\in\Omega,
\tag{156.20}
\]

where \(X'\subseteq X_{\max}\) and \(W=N_{A^*(v)}(X')\) are constant on the
chamber. Every \(P(v)\) is a same-hull global optimum of its flag cardinality.

Call a source label \(x\) **\(\mathcal L_{\rm act}\)-frozen** if
\(v_x=0\) for every \(v\in\mathcal L_{\rm act}\).

> **Proposition 156.4 (persistent-triangle localization).** If every \(P(v)\),
> \(v\in\Omega\), contains a unit equilateral triangle, then one fixed labeled
> triangle persists throughout \(\Omega\). That triangle either lies entirely in
> \(X'\), or every one of its retained source vertices is
> \(\mathcal L_{\rm act}\)-frozen.

### Proof

There are only finitely many labeled triples. For each triple, the condition that all
three squared distances equal one is an algebraic condition on the affine space
\(\mathcal L_{\rm act}\). If the finite union of these triangle loci covers the
relatively open set \(\Omega\), one locus has relative interior. Its three distance
polynomials therefore vanish identically on \(\mathcal L_{\rm act}\), giving one
fixed labeled triangle throughout the chamber.

The triangle cannot consist only of retained source points because every
\(A^*(v)\) is triangle-free. Let \(x\) be a retained source vertex of the persistent
triangle and let \(z\in X'\) be one of its inserted vertices. For any
\(v_0\in\Omega\), direction \(w\in\mathcal L_{\rm act}\), and sufficiently small
\(t\), persistence gives

\[
|p_x+(v_0)_x+t w_x-z|^2=1.
\tag{156.21}
\]

The coefficient of \(t^2\) is \(|w_x|^2\), so \(w_x=0\). Since \(w\) was
arbitrary, \(x\) is frozen. Apply this to every retained source vertex in the
triangle. \(\square\)

Thus the activation flat breaks every transition obstruction except one supported
entirely on inserted capacity points and source labels invisible to the flat. Exact
two-leaf cages can occur in that frozen support, so Proposition 156.4 is a
localization theorem, not an elimination theorem.

## 156.6 Target A implication and binding regressions

Section 156 supplies finite global-optimum motion in one fixed hull, not merely KKT
or infinitesimal data. It also strengthens the activation-rank statement from a
recorded unit subforest to all created active pairs. Nevertheless it does not imply

\[
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}.
\tag{156.22}
\]

The plateau scaffold is built from an independent smaller optimum. No canonical map
from \(\mathcal L_{\rm act}\) to the boundary source space \(\mathbb F^{C^\partial}\)
has been constructed, and Proposition 156.4 permits a first triangle to remain on
the frozen/inserted support.

The existing regressions remain consistent:

- Section 152 realizes the same attachment geometry without global
  minimum-diameter optimality and still has zero monomer-scaffold nullity. It rules
  out a local flat-to-Schur implication.
- Section 153 forces every activation multiplier to be zero. This is compatible with,
  and now geometrically explained by, the affine feasible family.
- Sections 154--155 are compatible and, under (156.17), give the genuine coembedding
  in Corollary 156.3. Section 157 supplies a backbone Hall witness in that same
  subbranch, but the captured rattlers are not yet a Schur certificate.
- Straight activation chains are not a counterexample: first-order-orthogonal linear
  motions increase their unit lengths by the nonnegative quadratic term in
  (156.11).
- Exact two-leaf cages, full-rank planar responses, overlapping circuits, and annular
  full-linkage networks remain possible on support not controlled by the affine
  family.

The exact remaining bridge is therefore a genuinely global two-shadow/backbone
compatibility theorem. In the aligned subbranch it must use the common source/capacity
history, the affine family, and the captured rattlers of Section 157 to send at least
\(s=\Delta_\Lambda-d_{\rm int}\) independent directions or obstructions into
\(\ker S\), or else turn the frozen/inserted support into a strict smaller-diameter
source replacement. Outside that subbranch the coordinate transport itself is still
also required. Neither implication is proved here.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**
