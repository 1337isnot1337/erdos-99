# Target A — actual-response lock or triangle-free descent

This addendum follows Sections 159 and 165--168.  The locked-boundary theorem of
Section 159 was previously applied to a source-capacity transition in the remote source
hull `H`, so its reaction points were not identified with the actual response shore.
There is a more direct application: use the fixed-container alternative on the actual
plateau-terminalized optimum `X^*` in its own hull `K^*`.  Either this produces a
triangle-free global optimum at the smaller cardinality `m^*`, or the locked triangle
and its boundary stress already live on the actual response point set.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 169. Actual response lock-or-descent theorem

Let
\[
X^*\subset K^*=\operatorname{conv}X^*,
\qquad |X^*|=m^*,
\qquad \operatorname{diam}K^*=d=D(m^*)
\tag{169.1}
\]
be the right-endpoint optimum used by the plateau-terminalized Schur response.  No
source-hull alignment is needed for the first theorem below.

For the asymptotic branch the response hull is automatically full-dimensional.

> **Lemma 169.0 (nondegeneracy of the response hull).** If `m^*>=3`, then `K^*` is
> full-dimensional.

### Proof

If `X^*` were collinear, ordering its `m^*` unit-separated points along the line would
give
\[
d\ge m^*-1.
\tag{169.2}
\]
The canonical strict translated-lattice bound of Section 114.2 gives
\[
d^2<c(m^*-1),
\qquad c=\frac{2\sqrt3}{\pi}<2.
\tag{169.3}
\]
Combining with (169.2),
\[
(m^*-1)^2<c(m^*-1),
\]
so `m^*-1<c<2`, impossible when `m^*>=3`.  \(\square\)

Thus `K^*` is a full-dimensional convex polygon throughout the sufficiently-large
regime relevant to Problem #99.

## 169.1 Direct fixed-container alternative on `X^*`

> **Theorem 169.1 (response lock or triangle-free plateau descent).** At least one of
> the following holds.
>
> 1. **Triangle-free descent.**  There is a unit-separated set
>    \[
>    X^{\rm tf}\subset K^*,
>    \qquad |X^{\rm tf}|=m^*,
>    \tag{169.4}
>    \]
>    with no unit equilateral triangle.  It is automatically a global optimum and
>    \[
>    \boxed{\operatorname{diam}X^{\rm tf}=d.}
>    \tag{169.5}
>    \]
> 2. **Actual-response lock.**  The point set `X^*` contains a unit equilateral
>    triangle `T_*` such that
>    \[
>    \boxed{
>    a_{ij}(v)=0
>    \qquad(ij\in E(T_*),\ v\in\mathcal C_{K^*}(X^*)).
>    }
>    \tag{169.6}
>    \]
>    Thus all three sides of `T_*` are fixed to first order by every infinitesimally
>    feasible motion that remains in the actual response hull.

### Proof

If `X^*` is already triangle-free, take `X^tf=X^*` and alternative 1 holds.
Otherwise apply Theorem 138.1 with fixed container `K^*` and packing `P=X^*`.

In alternative 1 of that theorem there is a fixed-container feasible velocity that,
for every sufficiently small positive time, breaks every unit triangle while keeping
all points in `K^*` and all pair distances at least one.  Let `X^tf` be one such
perturbed configuration.  It has `m^*` points and diameter at most `d`.  Since
`D(m^*)=d`, its diameter cannot be smaller than `d`; hence it is a global optimum and
(169.5) holds.

In alternative 2 of Theorem 138.1, a unit triangle of `X^*` satisfies exactly
(169.6).  Thus at least one displayed conclusion holds.  The two displayed conclusions
are not asserted to be mutually exclusive: a locked triangle in `X^*` does not rule
out a different, nonlocal triangle-free optimum elsewhere in `K^*`.  \(\square\)

The first alternative is a genuine descent of the counterexample problem: if the
original source cardinality is larger than `m^*`, then a triangle-free optimum has
been produced at the strictly smaller diameter `d<D`.  It is not itself a contradiction
unless one has separately ruled out such a smaller counterexample.

## 169.2 The locked stress reaches actual response-boundary vertices

Assume the actual-response locked conclusion (169.6).  For `m^*>=3`, Lemma 169.0
allows Theorem 159.1 to be applied with the full-dimensional convex polygon `K^*` and
packing `X^*`.  There are nonnegative contact coefficients and facet reactions, with
strictly positive coefficients on the three edges of `T_*`, satisfying force balance
at every point of `X^*`.  Let `K_T` be the connected component of the positive-contact
graph containing `T_*`.

> **Corollary 169.2 (actual-response boundary transmission).**  The component `K_T`
> contains at least two distinct points
> \[
> u,v\in X^*\cap\partial K^*
> \tag{169.7}
> \]
> carrying nonzero facet reaction.  In particular there are positive-contact paths in
> `X^*` from the locked triangle to two distinct vertices of the actual response hull.

### Proof

This is Theorem 159.1 with `H=K^*` and `P=X^*`.  Its hypotheses are exactly
(169.6), together with the full-dimensionality supplied by Lemma 169.0.  \(\square\)

The remaining coordinate-identification step is elementary but important.

> **Lemma 169.3 (hull-boundary response points are response-boundary columns).**  Fix
> a triangular-lattice phase generic for `X^*`, and use the response notation
> \[
> Z=(\Lambda+v)\cap\operatorname{int}K^*,
> \qquad
> X^\circ=\{x\in X^*:N(x)\subseteq Z\},
> \qquad
> X^\partial=X^*\setminus X^\circ.
> \tag{169.8}
> \]
> Then
> \[
> \boxed{X^*\cap\partial K^*\subseteq X^\partial.}
> \tag{169.9}
> \]

### Proof

Let `x in X^* cap partial K^*`.  Section 79 associates to `x` the cell
\[
C_x=\operatorname{conv}N_\Lambda(x),
\tag{169.10}
\]
which is an elementary triangle or unit lozenge and contains `x` in its interior.
If `x` belonged to `X^circ`, every vertex of `C_x` would lie in `Z subset int K^*`.
The interior of a convex set is convex, so
\[
C_x\subset\operatorname{int}K^*.
\tag{169.11}
\]
But then `x in int C_x` would imply `x in int K^*`, contradicting
`x in partial K^*`.  Therefore `x in X^partial`.  \(\square\)

Combining the last two statements gives the promised scope correction.

> **Corollary 169.4 (locked-support transport to the actual response boundary).**  In
> the locked branch there are at least two distinct vertices
> \[
> \boxed{u,v\in X^\partial}
> \tag{169.12}
> \]
> that lie in the positive-contact component of the locked response triangle and carry
> nonzero `K^*`-facet reaction.

This is strictly stronger than the Section-159 source-hull statement for the present
purpose: `u` and `v` are vertices of the same point set from which the Schur boundary
columns are chosen.  They may still belong to the contracted `Z`-basis `B`, rather than
to the nonbasis terminal set `C^partial`; no claim to the contrary is made.

## 169.3 Contact-edge crossing rule and the proper-crosscut subbranch

The following exact crossing observation is unconditional in the locked branch.

> **Lemma 169.5 (response edge crossing a locked contact edge).**  Let `pq` be a unit
> contact edge of `X^*`, and let `xy` be a response radial edge with
> \[
> x\in X^*,\qquad y\in\Lambda+v,\qquad |x-y|<1,
> \tag{169.13}
> \]
> whose segment properly crosses the relative interior of `pq`.  If
> `x notin {p,q}`, then
> \[
> \boxed{|y-p|<1\quad\text{or}\quad |y-q|<1.}
> \tag{169.14}
> \]

### Proof

Because `X^*` is unit-separated and `x` is distinct from `p,q`,
\[
|x-p|\ge1,
\qquad |x-q|\ge1.
\tag{169.15}
\]
If both `|y-p|` and `|y-q|` were at least one, the unit-edge crossing barrier of
Lemma 103.1, applied to the crossing segment `xy`, would give
\[
|x-y|\ge\sqrt3,
\tag{169.16}
\]
contradicting the response-edge inequality `|x-y|<1`.  Hence (169.14) holds.
\(\square\)

Section 159 guarantees positive-contact paths from the locked triangle to at least two
distinct boundary-reaction vertices.  It does **not** by itself prove that the positive
contact component contains a proper crosscut whose polygonal arc meets
`partial K^*` only at its two endpoints; a stress component could contain substantial
boundary-supported contact structure.  Accordingly define a **locked contact
crosscut** to be any simple positive-contact subpath
\[
Q=(q_0,\ldots,q_L)
\tag{169.17}
\]
with `q_0,q_L in partial K^*` and with every other point of its polygonal arc in
`int K^*`.

Whenever such a crosscut exists, Lemma 169.5 says that a response path cannot cross it
invisibly: every proper crossing radial edge creates a lattice vertex that is already
a strict response neighbor of one of the contact-path vertices.  Section 170 converts
this fact into an exact Schur-rank inequality.

## 169.4 Exact remaining bridge

The Target A endpoint is unchanged:
\[
\boxed{
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}.
}
\tag{169.18}
\]

Section 169 changes the locked branch substantially.  The boundary-transmitting stress
no longer ends at unrelated points of the remote source hull.  It ends at actual
response-boundary vertices `X^partial`, and every proper crossing of a locked contact
edge by a response edge has the exact local shielding rule of Lemma 169.5.

There are now two nested obligations in the locked branch.  First either produce a
proper locked contact crosscut, or treat the residual case in which the relevant
positive-contact support is boundary-hugging.  Second, once a crosscut is available,
prove the quantitative side imbalance required by Section 170.  The two boundary
reaction points of Corollary 169.4 may both lie in the contracted basis rather than in
`C^partial`; this basis issue also remains live.

In the other branch, Theorem 169.1 produces a triangle-free global optimum at the
smaller plateau endpoint.  A full proof must either rule out indefinite descent of
such counterexamples or show that a sufficiently large descent eventually enters a
branch already closed by the canonical Target A/Target B machinery.
