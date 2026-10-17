# Hostile audit — one-anchor closure-corank and mutual-link flex theorem

**Date:** 2026-09-18  
**Audited source:** `research/target_c_free_terminal_one_anchor_corank_2026-09-18.md`  
**Status:** proof-only audit; theorem-state authority unchanged

## Verdict

PASS at the stated proof-only scope.

The two load-bearing claims survive the obvious failure modes:

1. the activated-face dual variables really vanish because the selected pivot columns
   have no residual entries and the activated pivot block is invertible;
2. the residual `n_0,n_2` projection costs at most `2n_0+n_2` dimensions;
3. one-anchor scalar relations propagate on a fixed simple graph with at most one
   scalar degree of freedom per connected component;
4. a nonzero component cannot have relation degree three: that endpoint would force a
   convex unit pentagon with an interior unit chord;
5. therefore every nonzero one-anchor component contains at least five faces;
6. mutually parallel one-anchor links use disjoint train variables and their exact
   common-angle rotations are absorbed by the already invertible activated pivot
   system; and
7. the terminal decimal uses only an upper enclosure for `M_*` and the exact defect
   simplex, so its inequality direction is safe.

The result does not close C-II.  Its sharp remaining dual object is a five-face
complete relation component (`K_5`) and its sharp primal obstruction is the possibility
that the diameter thrackle positively locks the exposed exact-flex coordinates.

---

## 1. Pivot-dual elimination

Let `P` be the two pivot columns per activated face.  A pivot chosen for an activated
face has other endpoint `O` or an earlier activated face; it can never have an endpoint
in final residual `U`.  Thus the `U x P` row block is zero.

The `A x P` block is exactly the block-upper-triangular pivot matrix from the existing
two-anchor theorem.  Its diagonal `2x2` blocks consist of two nonparallel side
directions and are invertible.  Hence for `y in ker(C_face^T)`, the equations on the
columns `P` are

\[
 C[A,P]^T y_A=0,
\]

and force `y_A=0`.  There is no hidden cancellation with residual rows.

This step is finite and exact.

---

## 2. Residual projection dimension

With `y_A=0`, an `n_2` face sees at least one outside/activated train column.  Maximality
makes its two such directions projectively parallel, so the outside equations impose
one nonzero scalar condition on its two-vector `y_F`; the allowed space is at most one
dimensional.  An `n_0` face has at most two free dual coordinates.  Therefore the
projection to all `n_0,n_2` face blocks has image dimension at most

\[
2n_0+n_2.
\]

No independence between different projected blocks is assumed; this is an upper bound,
so additional equations only help.

In the projection kernel every `n_1` block has the form `y_F=c_F a_F` for its unique
outside direction `a_F`.

---

## 3. Relation-component dimension

For an internal train `FG` nonparallel to both anchors, the transpose equation is

\[
 c_F(a_F\cdot Ju)-c_G(a_G\cdot Ju)=0
\]

with both coefficients nonzero.  It determines one scalar from the other.  A connected
component of the relation graph therefore has solution dimension at most one.

If a component supports a nonzero solution, every scalar in it is nonzero.  An internal
train nonparallel to the anchor at such an `F` cannot terminate at a zero block, nor be
parallel to the neighbor's anchor: either situation would leave one nonzero term and
force `c_F=0`.  Hence every nonparallel internal train of a live vertex belongs to the
same live relation component.

This checks the main support-propagation step.  No sign assumption on the scalars is
used.

---

## 4. Why relation degree three is impossible

A one-anchor residual face has at least four internal train incidences.  Strict
convexity allows only one of those internal sides to be projectively parallel to the
outside anchor side.  Thus a live relation vertex has degree at least three.

Suppose equality holds.  Then there are exactly four internal sides, exactly one
parallel side, and no degree excess: the face is a unit pentagon.  The outside anchor
and the parallel internal side have opposite oriented unit vectors and cancel.  The
remaining three oriented unit side vectors sum to zero.

For unit vectors, `v_1+v_2+v_3=0` implies the three directions are separated by 120
degrees.  The two canceled directions `a,-a` cannot coincide with any of these three
(strict convexity), and two directions cannot occupy all three open 120-degree arcs.
One triad pair is therefore consecutive in the pentagon's cyclic tangent order.  The
turn there is 120 degrees, so the interior angle is 60 degrees.  The chord joining the
other endpoints of the two unit sides has length one.

That chord lies in the interior of a strictly convex face and is itself a unit contact.
Since the contact graph contains every unit-distance pair, the chord would subdivide
the supposed face.  Contradiction.

Thus a live relation component has minimum degree at least four.  Simplicity of the
bounded B--B transport graph then gives at least five vertices.  This proves the
`n_1/5` fiber bound.

Regression checks:

- The argument does not assume a generic angle gap.
- It does not assume the face is regular.
- It uses equality of contact length one, so no limiting approximation is hidden.
- A repeated B--B endpoint pair would break the simple-graph support-size conclusion,
  but that case is already excluded by the audited endpoint-pair theorem explicitly
  listed as a dependency.

---

## 5. Mutual-link exact flex

For a mutually parallel link `tau=FG`, the unique outside train at each endpoint is
projectively parallel to `tau`.  On a strictly convex face the two corresponding
oriented unit side vectors are exact negatives.  A common train-angle increment
therefore preserves each residual face closure identically, not only to first order.

The outside train at `F` or `G` may terminate on an activated bounded face.  This does
not invalidate the flex: a U--A train is never one of the old pivots, so it can be used
as a new free parameter; the unchanged invertible pivot block solves the activated
closures as smooth functions of all such free parameters simultaneously.

A one-anchor face has at most one internal side parallel to its anchor, so mutually
parallel links form a matching.  Different links consequently use disjoint residual
faces and distinct internal/outside train variables.  Their differentials are
independent because each parameter changes its own internal U--U train angle while no
active pivot touches U.

The dimensions therefore add to the existing peel plus `n_2` pair manifold.  No global
rotation quotient is lost: the stalled residual system still contains frozen train
coordinates outside any single matching parameter, and the inherited pair-shield
manifold was already counted modulo Euclidean motions.

---

## 6. Algebra and terminal constant

The exact corank bound is

\[
\sigma_C\le2n_0+n_2+n_1/5.
\]

With

\[
E_U=a_F+x_A/2+(n_0+n_2)/2,
\qquad
f=a_F+n_0+n_1+n_2,
\]

one has the exact identity

\[
{f\over5}+{18\over5}E_U-
\left(2n_0+n_2+{n_1\over5}\right)
={19a_F+9x_A+5n_2\over5}\ge0.
\]

The local certificate exhausts a finite integer box as a regression and separately
checks this coefficient identity exactly.

For the live terminal constant, the inherited ledger is

\[
f/D=(M_*+2\xi-\delta-r)/5+o(1),
\qquad
\xi+2(r+\delta)\le5\varepsilon.
\]

The upper bound on `f` is attained in the closed relaxation at
`xi=5epsilon`, `r=delta=0`, giving

\[
f/D\le M_*/5+2\varepsilon+o(1).
\]

At `epsilon=0.00710`, exact rational enclosures for pi and
`sqrt(pi/(2sqrt(3)))` prove

\[
{1\over5}(M_*/5+2\varepsilon)<0.1558266092.
\]

The certificate uses the upper enclosure of `M_*`, which is the correct direction for
this corank upper bound.

---

## 7. Limits and next target

The theorem does not show that the `K_5` relation block is impossible.  It also does
not turn the corank bound into an upper bound on the actual diameter-locking rank.
Positive KKT locking can still occur.

What has changed is the exact endpoint object.  A low-flex stalled survivor now has:

- almost all residual faces one-anchored;
- mutual parallel links charged directly as exact flexes;
- pure-contact dual modes supported on at least five one-anchor faces; and
- a minimal dual support graph equal to `K_5`.

The most direct next attack is the `K_5` block.  Its five dual vectors satisfy the
train-direction difference equations on all ten relation edges, while each physical
face must simultaneously close as a strict unit contact polygon.  Excluding that
configuration, or forcing an additional exact flex from it, would improve `1/5` to a
smaller corank density and further tighten the terminal endpoint.

**Audit disposition:** PASS. C-II remains open; no theorem-state file is changed.
