# Hostile audit — two-anchor peeling and parallel outside-pair flexes

**Date:** 2026-09-18  
**Status:** proof-only audit; theorem-state authority unchanged  
**Audited source:** `target_c_free_terminal_two_anchor_pair_shield_flex_2026-09-18.md`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

## Verdict

PASS at the stated proof-only scope.

The strengthened argument does not require the two parallel trains at a residual face
to terminate on the actual outer face.  They may terminate on already activated bounded
faces.  Their common rotation preserves the residual closure exactly, and the original
block-triangular pivot system absorbs the induced closure changes on the activated
faces.  This raises the exact stalled-case dimension floor from the preliminary
`b/2-5f/8` count to

\[
\boxed{m_D\ge(b-f)/2.}
\]

The finite bookkeeping also isolates the true low-flex endpoint: almost every residual
face must have exactly one train to the outer/activated side, so the residual transport
graph is internally at least 4-valent at almost every face.

---

## 1. Residual train accounting

Let `A` be the activated bounded exceptional faces and `U` the nonempty residual set.
For `F in U`, maximality of the two-anchor process means all train ends from `F` to
`O union A` lie in one projective direction.  Strict convexity permits at most two
sides in one projective direction, hence

\[
 b_U(F)\in\{0,1,2\}.
\]

Write

\[
 n_j=\#\{F\in U:b_U(F)=j\},
 \qquad
 d_U=2n_0+n_1,
 \qquad
 u=n_0+n_1+n_2.
\]

If `x_U=sum_{F in U}(deg F-5)`, the residual degree sum is

\[
2E(U)+B_U=5u+x_U,
\qquad B_U=2u-d_U.
\]

Therefore the number of complete train variables incident to `U` is exactly

\[
 I_U=E(U)+B_U={5u+x_U+B_U\over2}.
\]

An internal U--U train contributes two degree incidences but one frozen variable; a
U--outside train contributes one of each.  No endpoint multiplicity is lost.

---

## 2. Peeling manifold and Euclidean quotient

Every pivot selected when a face entered `A` had other endpoint `O` or an earlier
activated face.  Hence no pivot is incident to final `U`.  Freezing all U-incident
trains leaves the same `2|A|` pivot columns and the same block upper triangular Jacobian
with invertible `2x2` diagonal blocks.  The implicit-function theorem therefore solves
the active closures exactly as before.

Residual closures are unchanged because all their incident trains are initially frozen.
Strict rhombi close identically in train-angle coordinates.  Thus

\[
 m_{peel}=T-I_U-2|A|.
\]

Using `T=(q-k)+2f`, `f=u+|A|`, `b+Q=2(q-k)`, and
`x_A+x_U=Q-f` gives

\[
\boxed{
 m_{peel}
 ={b-2f\over2}+{3|A|+x_A+d_U\over2}.
}
\]

Because every residual face has degree at least five and at most two outside incidences,
`U` has at least one internal U--U train.  That train angle is frozen, so the all-train
constant angular-rate vector for global rotation is absent.  No further `-1` quotient
is missing in the stalled case.

---

## 3. Two-outside pair flex with activated endpoints

Take `F in U` with `b_U(F)=2`.  Its two outside terminal side vectors `v_1,v_2` are
projectively parallel by maximality.  A cyclically oriented strictly convex polygon
cannot contain two sides with the same oriented direction, so the two unit vectors are
exact opposites:

\[
 v_2=-v_1.
\]

Give the two complete trains the same angle change `theta`.  Their residual-face
contribution remains

\[
R_\theta v_1+R_\theta v_2=0
\]

identically.  The other endpoint of a selected train is either `O` or a face in `A`.
An O endpoint creates no bounded closure equation.  At an A endpoint the changed angle
is simply an additional free parameter in the already invertible active pivot system.
The implicit-function theorem adjusts the active pivots to restore every A-face closure.

A U--A train cannot itself be an active pivot: when its A endpoint was activated, its
U endpoint was neither outer nor previously activated.  Hence introducing these pair
parameters never steals a pivot column.

Different residual faces use disjoint outside train variables.  The `n_2` common-angle
parameters therefore add `n_2` exact dimensions to the peeling manifold.  Singleton
selected trains are harmless because they have no rhombus equations; nonsingleton
trains preserve every crossed strict rhombus by opposite-side cancellation.

---

## 4. Exact finite identity

Adding the `n_2` pair parameters gives

\[
\begin{aligned}
 m_D
 &\ge {b-2f\over2}
 +{3|A|+x_A\over2}
 +n_0+{n_1\over2}+n_2.
\end{aligned}
\]

Since

\[
f=|A|+n_0+n_1+n_2,
\]

this is exactly

\[
\boxed{
 m_D\ge {b-f\over2}
 +|A|+{x_A\over2}+{n_0+n_2\over2}.
}
\]

Thus `m_D>=(b-f)/2` with no asymptotic step.  The correction terms identify the
counting endpoint: small excess above `(b-f)/2` forces few activated faces, little
degree excess on those faces, and few residual faces with zero or two outside trains.
Almost all residual faces then have exactly one outside train and therefore at least
four internal U--U train incidences.

The exact-rational certificate checks this finite algebra on an exhaustive integer box;
the displayed identity is the load-bearing proof.

---

## 5. Terminal scalar check

The inherited terminal identities are

\[
 {b\over D}=\pi+\delta+o(1),
\]

\[
 {f\over D}={M_*+2\xi-\delta-r\over5}+o(1),
\]

with

\[
 \xi+2(r+\delta)\le5\varepsilon,
 \qquad \xi,r,\delta\ge0.
\]

Substitution into `(b-f)/2` gives

\[
 {\pi\over2}-{M_*\over10}
 +{3\over5}\delta
 +{1\over10}r
 -{1\over5}\xi.
\]

Only `xi` has negative coefficient.  At `epsilon=0.00710` the minimum is attained on
the closed defect simplex at `xi=5epsilon`, `r=delta=0`.  The exact-rational certificate
proves

\[
 m_D/D>1.1812298040-o(1).
\]

In the small-complement branch, `delta>0.01725` and `xi+2r<=0.001`; the closed
relaxation is minimized at `delta=0.01725`, `r=0`, `xi=0.001`, giving

\[
 m_D/D>1.1984798040-o(1).
\]

No floating-point value is load-bearing.

---

## 6. Limits

- The result does not prove that a `1.1812D`-dimensional exact contact-flex manifold is
  incompatible with the actual diameter graph.  KKT positive locking remains possible.
- It does not bound how many explicit pair coordinates one diameter bar may couple to.
- It does not give a simultaneous strict diameter-decreasing tangent or a second-order
  descent.
- The one-anchor internal 4-core is a necessary near-endpoint normal form, not yet an
  excluded object.
- The separate macroscopic-container branch is untouched.
- No theorem-state file is promoted or changed.

**Claim classification:** audited-working proof-only structural strengthening. C-II
remains open.