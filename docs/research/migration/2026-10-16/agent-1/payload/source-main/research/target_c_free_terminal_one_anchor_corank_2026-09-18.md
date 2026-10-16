# Target C-II — one-anchor residual cores have small closure corank or extra exact flex

**Date:** 2026-09-18  
**Status:** proof-only structural strengthening; theorem-state authority unchanged  
**Scope:** canonical full-core stopped-train system after maximal two-anchor activation  
**Depends on:** audited train-angle closure matrix and transpose-kernel equations; strict convexity of bounded nonquadrilateral contact faces; bounded-face endpoint-pair simplicity; maximal two-anchor peeling; activated-endpoint parallel-pair flex theorem  
**Certificate:** `research/verify_target_c_free_terminal_one_anchor_corank_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The latest two-anchor/pair theorem leaves a sharp low-flex normal form: after a maximal
activation stalls, almost every residual exceptional face has exactly one train to the
outer/activated side and at least four residual B--B train incidences.  This note uses
the *transpose* face-closure equations on that normal form.

The key point is local.  A nonzero transpose-kernel vector on a one-anchor residual
face is forced to be parallel to that face's unique outside anchor.  All but at most
one residual internal train then have a nonzero dual coefficient.  If only three such
internal trains remained, face closure would force their three unit side vectors to
sum to zero.  They would be separated by exactly 120 degrees, and one pair would be
consecutive on the strictly convex unit face.  That creates an interior unit chord,
contradicting that the polygon is a face of the complete unit-contact graph.  Hence a
nonzero one-anchor dual mode has at least four nonparallel residual neighbors.

This changes the residual self-stress bookkeeping from a generic one-anchor network to
five-face blocks.  With the notation of the pair-shield theorem,

\[
\boxed{
 \sigma_C\le 2n_0+n_2+{n_1\over5}.
}
\tag{OC.1}
\]

Here `sigma_C=dim ker(C_face^T)`, and `n_j` counts residual faces with exactly `j`
trains to the outer/activated side.  The factor `1/5` is exact and finite; it is not an
asymptotic rank estimate.

There is also a primal counterpart.  If two one-anchor residual faces are joined by a
train parallel to the unique outside train at both endpoints, those three trains have
an exact common-angle flex.  Such mutually parallel links form a matching.  If `p_U`
is their number, the latest pair-shield flex bound strengthens to

\[
\boxed{
 m_D\ge {b-f\over2}
 +a_F+{x_A\over2}+{n_0+n_2\over2}+p_U.
}
\tag{OC.2}
\]

Thus the one-anchor endpoint has two independent restrictions: mutual parallel links
produce additional exact finite flexes, while the remaining dual closure modes require
components of at least five one-anchor faces.

---

## 1. Maximal activation notation

Run the audited two-anchor activation process to maximality.  Let `A` be the activated
bounded nonquadrilateral faces and `U` the residual faces.  Put

\[
 a_F=|A|,
 \qquad
 n_j=\#\{F\in U:b_U(F)=j\},\qquad j=0,1,2,
\]

where `b_U(F)` counts trains from `F` to the actual outer face `O` or to a face in `A`.
Maximality and strict convexity give

\[
 b_U(F)\in\{0,1,2\},
\]

and when `b_U(F)=2` the two outside train directions at `F` are projectively parallel.
Let

\[
 x_A=\sum_{F\in A}(\deg F-5),
 \qquad
 f=a_F+n_0+n_1+n_2.
\]

The activated-endpoint pair theorem already gives

\[
 m_D\ge {b-f\over2}
 +a_F+{x_A\over2}+{n_0+n_2\over2}.
\tag{1.1}
\]

The purpose here is to use the same decomposition on the transpose closure kernel.

---

## 2. Every transpose-kernel vector vanishes on the activated faces

Let

\[
 C_{face}:\mathbb R^T\to\mathbb R^{2f}
\]

be the audited train-angle face-closure matrix.  A vector

\[
 y=(y_F)_{F},\qquad y_F\in\mathbb R^2,
\]

lies in `ker(C_face^T)` exactly when, for every bounded--bounded train `tau=FG` with
coherent projective direction `u_tau`,

\[
 (y_F-y_G)\cdot Ju_\tau=0,
\tag{2.1}
\]

and, for every bounded--outer train `tau=FO`,

\[
 y_F\cdot Ju_\tau=0.
\tag{2.2}
\]

Let `P` be the `2a_F` pivot train columns selected by the activation order.  No pivot
train is incident to final `U`: when its activated endpoint entered, the other endpoint
was `O` or an earlier activated face.  The submatrix

\[
 C_{face}[A,P]
\]

is the same block-upper-triangular matrix used in the primal elimination theorem, with
invertible `2x2` diagonal blocks.  It is therefore invertible.

For `y in ker(C_face^T)`, restrict the transpose equations to the pivot columns `P`.
There are no residual-row entries in those columns, hence

\[
 C_{face}[A,P]^T y_A=0.
\]

Invertibility gives

\[
\boxed{y_F=0\quad(F\in A).}
\tag{2.3}
\]

This is the dual counterpart of the triangular primal elimination.

---

## 3. Residual coordinate dimensions before using internal trains

Fix `F in U`.

If `b_U(F)=2`, the two outside/activated train directions are projectively parallel.
Because `y_A=0`, either outside train imposes one nonzero linear condition on `y_F`.
Thus the possible `y_F` lie in a one-dimensional line.

If `b_U(F)=1`, let `a_F` denote a unit vector in the unique outside train direction.
Equations (2.1)--(2.3) give

\[
 y_F\cdot Ja_F=0,
\]

so

\[
\boxed{y_F=c_Fa_F}
\tag{3.1}
\]

for one scalar `c_F`.

If `b_U(F)=0`, there is no outside condition and the a priori coordinate space is two
dimensional.

Let `B` be the set of residual `n_0` and `n_2` faces.  Project
`ker(C_face^T)` onto the `B` face blocks.  The image has dimension at most

\[
 2n_0+n_2.
\tag{3.2}
\]

It remains to bound the kernel of this projection, where all `B` blocks vanish and only
one-anchor (`n_1`) face variables remain.

---

## 4. The one-anchor relation graph

On the `n_1` faces define a graph `R` as follows.  Join distinct one-anchor residual
faces `F,G` when their common residual train `tau=FG` is projectively nonparallel to
both unique outside anchor directions `a_F,a_G`.

The B--B endpoint transport graph is simple by the audited endpoint-pair theorem, so
`R` is simple.

For an edge `FG` of `R`, substitute (3.1) into (2.1):

\[
 c_F(a_F\cdot Ju_{FG})
 -c_G(a_G\cdot Ju_{FG})=0.
\tag{4.1}
\]

Both displayed coefficients are nonzero by definition of `R`.  Thus an `R` edge
determines either endpoint scalar from the other.  Consequently, on each connected
component of `R`, the solution space has dimension at most one.

Some components in fact contribute zero because of trains to a zero face block.  We
only need to bound components which support a nonzero solution.

---

## 5. A nonzero one-anchor component has minimum `R`-degree four

Take a connected component `K` of `R` which supports a nonzero solution of the fiber
system.  Equation (4.1) propagates nonzeroness along `K`, so

\[
 c_F\ne0\qquad(F\in K).
\tag{5.1}
\]

Fix `F in K`.  Since `F` has exactly one outside incidence and total degree at least
five, it has at least four residual internal train incidences.

Any residual internal train at `F` whose direction is nonparallel to `a_F` must lead
to another nonzero one-anchor block and must also be nonparallel to that neighbor's
anchor.  Otherwise its transpose equation has only one nonzero term and forces
`c_F=0`, contradicting (5.1).  Hence every such train is an edge of `R` within `K`.

Strict convexity permits at most two polygon sides in one projective direction.  One
of them is the unique outside anchor side, so at most one residual internal side can
be projectively parallel to `a_F`.  Therefore

\[
 \deg_R(F)\ge3.
\tag{5.2}
\]

The apparent degree-three endpoint is impossible.

Assume `deg_R(F)=3`.  Then `F` must have exactly four residual internal sides, exactly
one of them projectively parallel to the outside anchor.  Hence `deg(F)=5`: `F` is a
strictly convex unit pentagon.  Let the oriented unit outside-anchor side vector be
`a`.  The unique parallel internal side has oriented vector `-a`; equal orientation is
impossible on a strictly convex polygon.  Let the remaining three oriented unit side
vectors be `v_1,v_2,v_3`.  Face closure gives

\[
 a-a+v_1+v_2+v_3=0,
\]

so

\[
 v_1+v_2+v_3=0.
\tag{5.3}
\]

Three unit vectors summing to zero are separated by exactly `2pi/3` in oriented angle.
Their directions partition the circle into three open arcs of length `2pi/3`.  The two
additional directions `a` and `-a` can occupy at most two of those arcs; strict
convexity prevents either from coinciding with a `v_i`.  Thus at least one pair of the
`v_i` is consecutive in the cyclic edge-direction order of the pentagon and has
exterior turning angle exactly `2pi/3`.

The corresponding interior angle is `pi/3`.  Its two incident sides both have length
one, so the segment joining their other endpoints also has length one.  Strict
convexity places that segment in the interior of the pentagon.  But the contact graph
contains every unit-distance pair, so this segment would be a contact chord cutting
`F`, contradicting that `F` is a face.

Therefore

\[
\boxed{\deg_R(F)\ge4\qquad(F\in K).}
\tag{5.4}
\]

Since `R` is simple, every nonzero component contains at least five one-anchor faces.
Since each such component contributes at most one scalar dimension,

\[
\boxed{
 \dim\ker(P|_{\ker C_{face}^T})\le {n_1\over5}.
}
\tag{5.5}
\]

Combining (3.2) and (5.5) proves

\[
\boxed{
 \sigma_C=\dim\ker C_{face}^T
 \le2n_0+n_2+{n_1\over5}.
}
\tag{5.6}
\]

This is (OC.1).

A useful equality-shape consequence is that any five-face component attaining the
support-size minimum has `R=K_5`.  The next obstruction is therefore much more rigid
than a generic internally 4-valent transport core: a minimal pure-contact dual mode is
a five-face complete nonparallel relation block.

---

## 6. Mutually parallel one-anchor links give exact primal flexes

Call an internal train `tau=FG` a **mutually parallel one-anchor link** when

1. `F,G` are both `n_1` residual faces; and
2. `tau` is projectively parallel at `F` to `F`'s unique outside train and
   projectively parallel at `G` to `G`'s unique outside train.

At a one-anchor face there is at most one residual side parallel to the anchor side, so
these links form a matching.  Let their number be `p_U`.

For one such link, let `alpha_F` and `alpha_G` be the unique outside trains.  On `F`,
the oriented side vectors of `tau` and `alpha_F` are exact negatives; the same holds on
`G`.  Give all three complete train angles the same small increment `theta`.  Their
pair contributions cancel identically at both residual faces for every `theta`.

If an outside train terminates on `O`, no second bounded closure equation is created.
If it terminates on an activated face, treat `theta` as an additional free parameter in
the already invertible activated pivot system.  No selected U--A train is itself an
active pivot.  The implicit-function theorem therefore adjusts the old pivots and
restores all activated-face closures.  Strict rhombi close identically.

Different mutually parallel links use disjoint residual faces and disjoint selected
train variables.  Their parameters are independent and are disjoint from the `n_2`
pair parameters already used in the pair-shield theorem.  Hence (1.1) strengthens to

\[
\boxed{
 m_D\ge {b-f\over2}
 +a_F+{x_A\over2}+{n_0+n_2\over2}+p_U.
}
\tag{6.1}
\]

This is (OC.2).

---

## 7. Flex/corank tradeoff

Define the already exposed structural flex excess

\[
 E_U:=a_F+{x_A\over2}+{n_0+n_2\over2}.
\tag{7.1}
\]

From `f=a_F+n_0+n_1+n_2` and (5.6), direct coefficient comparison gives

\[
\boxed{
 \sigma_C\le {f\over5}+{18\over5}E_U.
}
\tag{7.2}
\]

Indeed the right side minus `2n_0+n_2+n_1/5` is exactly

\[
 {19\over5}a_F+{9\over5}x_A+n_2\ge0.
\tag{7.3}
\]

Combining (6.1) and (7.2) gives the finite alternative

\[
\boxed{
 m_D\ge {b-f\over2}+p_U
 +{5\over18}\left(\sigma_C-{f\over5}\right)_+.
}
\tag{7.4}
\]

Thus a large pure-contact self-stress space cannot be used to hide the one-anchor
residual core without paying additional exact finite flex dimension.

---

## 8. Terminal FREE consequence

In the current live terminal window

\[
 \limsup t_D\le\mu_*+0.00710,
\]

the terminal ledger used by the pair-shield theorem gives

\[
 {f\over D}
 ={M_*+2\xi-\delta-r\over5}+o(1),
\]

where

\[
 M_*=4\sqrt{\frac\pi{2\sqrt3}}+2(0.007707),
\]

and

\[
 \xi+2(r+\delta)\le5(0.00710),
 \qquad \xi,r,\delta\ge0.
\]

Therefore

\[
 \limsup {f\over D}
 \le {M_*\over5}+2(0.00710)
 =0.7791330454\ldots .
\tag{8.1}
\]

Equation (7.2) yields

\[
\boxed{
 \limsup{\sigma_C\over D}
 \le0.1558266091\ldots
 +{18\over5}\limsup{E_U\over D}.
}
\tag{8.2}
\]

The exact-rational certificate proves the safe decimal bound

\[
 {1\over5}\left({M_*\over5}+2(0.00710)\right)
 <0.1558266092.
\]

In particular, any stalled sequence approaching the exact pair-shield counting floor,
so `E_U=o(D)`, has

\[
\boxed{
 \limsup{\sigma_C\over D}\le0.1558266092.
}
\tag{8.3}
\]

This is a new restriction on the low-flex endpoint.  The endpoint can no longer hide
inside a large closure-row corank: its pure-contact dual modes must be sparse in
dimension and each nonzero one-anchor mode occupies at least five residual faces.

---

## 9. Remaining obstruction

This still does not close C-II.  It removes two escapes from the one-anchor 4-core:

1. mutually parallel internal links are not passive; each gives an additional exact
   finite contact flex; and
2. the remaining transpose-kernel space has density at most one mode per five clean
   one-anchor faces, up to the explicitly charged `n_0,n_2` defects.

A minimal surviving dual block is now a `K_5` nonparallel relation component.  A useful
next theorem should attack that five-face block geometrically, or combine (7.4) with
the straight-line diameter-thrackle locking system to show that the required positive
span cannot simultaneously lock the primal pair coordinates and the sparse dual
blocks.

No theorem-state file is changed.

**Disposition:** proved the exact one-anchor closure-corank bound (OC.1), excluded the
four-face dual block by a unit-chord argument, extracted mutually parallel residual
links as exact finite flexes, and derived the terminal `0.1558266092D` corank endpoint
bound. C-II remains open.
