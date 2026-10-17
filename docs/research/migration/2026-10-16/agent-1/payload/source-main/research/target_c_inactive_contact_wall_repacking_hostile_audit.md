# Hostile audit — inactive contact-wall repacking

**Date:** 2026-09-12  
**Audited source:** `research/target_c_inactive_contact_wall_repacking.md`  
**Verdict:** PASS at the stated proof-only internal-face scope.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

The audit rechecks the contact-wall lemma, source retention, diameter-cover replacement,
and the Oler residual. It also records the exact point at which the argument stops.

## 1. Boundary crossing geometry

The source theorem uses only the following finite Euclidean fact. If a segment of
length `<1` properly crosses a unit edge `pq`, and the endpoint on one side is at
distance at least one from both `p` and `q`, then the other endpoint is at distance
strictly below one from both edge endpoints. The proof is the exact triangle-inequality
calculation

\[
 |x-p|+|y-q|\le |x-y|+|p-q|<2
\]

and its symmetric counterpart.

For the polygon wall, an outside source point can itself be a boundary vertex. The
source file treats this case separately; its distance to a replacement point is then
one of the imposed fixed-boundary inequalities. If the outside point is not a boundary
vertex, source unit separation supplies distance `>=1` to every boundary vertex.

If a subunit segment exits the convex face at a boundary vertex, that vertex lies
strictly between the endpoints and the two imposed/source distances add to at least
two. If it exits through the relative interior of a unit edge, the crossing is proper
because an interior point of a convex polygon lies strictly on the interior side of
each supporting edge. The two-endpoint crossing lemma applies.

A distinct source point cannot lie in the relative interior of a unit boundary edge:
it would be at distance `<1` from an endpoint. Thus there is no omitted endpoint-on-edge
case.

**Result:** the wall shield is exact.

## 2. Scope of the chamber

The theorem is intentionally restricted to a bounded nonquadrilateral contact face.
Canonical face convexity supplies a simple convex polygon with actual unit contacts on
every side. Its interior is a bounded face interior, hence lies in `int F subset int K`.
The canonical Section-77 assignment puts all source points in that face interior into
the assigned contact-isolated set `Z_C`; no retained old source point remains inside
the face after `Z_C` is removed.

The theorem does **not** silently extend to a convex outer pocket. An outer pocket has
an artificial force-hull chord on its boundary, and crossing that chord is not blocked
by the unit-edge argument.

**Result:** scope is correctly limited.

## 3. Cardinality and source-point retention

The replacement deletes `Z_C` and a diameter-graph vertex cover `U`, then inserts
`z_C+|U|` new points.

There is no overlap between `Z_C` and `U`: every chamber isolate lies in `int K`, while
a point in `int K` has distance strictly below `D` from every point of `K` and hence
cannot be an endpoint of an actual diameter edge. Thus the cardinality calculation is
literal.

No isolate is discarded without replacement. No isolate coordinate is inserted into
the Section-57 affine-kernel theorem.

**Result:** source cardinality and the binding core/isolate normalization are preserved.

## 4. Unit separation of the competitor

The new set is required to be pairwise unit-separated and at distance at least one
from every original boundary vertex, including a boundary vertex which may itself lie
in the deleted cover `U`. Keeping deleted boundary vertices as geometric obstacles only
makes the capacity condition stronger.

Every retained old source point lies outside the face interior. The wall theorem then
gives distance at least one from every new point. Old-old distances were already
feasible.

**Result:** the competitor is genuinely unit-separated.

## 5. Strict diameter descent

The cover `U` meets every edge of the **complete actual diameter graph**, so no retained
old-old pair remains at distance `D`.

Every new point is in `int K`. For `x in K` and `y in int K`, one has `|x-y|<D`: since
`K subset closed B(x,D)`, an interior point of `K` cannot lie on that disk's boundary
circle. This covers new-old and new-new pairs.

All pair distances in the finite competitor are therefore strictly below `D`, so its
diameter is strictly below `D`.

The replacement is not required to be triangle-free. This is legitimate because the
contradiction is against the definition of `D(n)`, whose comparison class is all
unit-separated `n`-point sets.

**Result:** the global-minimality contradiction is valid.

## 6. Oler residual audit

For an internal face with `m` unit boundary edges, the `m` boundary vertices together
with the `z_C` assigned isolates form a unit-separated set with convex hull `C`.
Finite Oler gives

\[
 z_C+m\le A_C/a_0+m/2+1,
\]

hence

\[
 r_\partial=A_C/a_0-m/2+1-z_C=\sigma_C-m\ge0.
\]

The same inequality applied to any fixed-boundary replacement gives

\[
 M_\partial-z_C\le r_\partial.
\]

This direction is easy to misuse. It is an **upper** bound on possible spare capacity.
It does not imply that `r_partial` slots actually exist. The source file states this
explicitly.

Summing `sigma_C>=m` over exceptional faces yields

\[
 \sum_{exc}\sigma_j\ge\sum_{exc}\deg(C_j)=4f+Q,
\]

which is compatible with the existing exceptional-face Oler ledger and introduces no
new authority claim.

**Result:** the residual identity is correct and correctly interpreted.

## 7. What was attempted and rejected

Three tempting continuations do not follow from the theorem.

1. **Reverse Oler to obtain spare points.** Invalid. Oler is an upper packing bound.
2. **Use contact-isolation as a uniform density defect.** Invalid. Strictly perturbed
   near-lattice packings can make every interior gap `>1` with arbitrarily small bulk
   density loss.
3. **Apply the wall shield to outer pockets.** Invalid across the artificial chord.

These are genuine regressions, not merely missing exposition.

## 8. Exact surviving obligation

For an internal macroscopic face, closure by the new route is reduced to a finite
fixed-boundary extension theorem strong enough to give

\[
 M_\partial(C)-z_C\ge\tau(H),
\]

or to a smaller lexicographic multi-vertex exchange using the same wall shield.
The only Oler allowance which can pay such an extension is the residual
`r_partial=sigma_C-m`.

The outer-pocket branch still requires a chord-safe analogue.

**Final audit verdict:** PASS as proof-only structural progress. It removes the full
one-unit collar from internal-face repacking, but it does not close the inactive
container branch or C-II.
