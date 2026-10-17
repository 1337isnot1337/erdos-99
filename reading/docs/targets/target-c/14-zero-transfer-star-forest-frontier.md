> Generated reading edition · [exact source](../../../../docs/targets/target-c/14-zero-transfer-star-forest-frontier.md) · source SHA-256 `2afa8168cfd1cd5ca9e581a94225786f25f209c4564b6d7b476aad4748f66262`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C — zero-transfer star-forest frontier

**LEVEL I STATUS: STILL OPEN.**

This module records C58 from
`docs/reports/target_c_zero_transfer_star_forest_2026-08-31.md`.
It sharpens the exceptional C56-Z branch and the C57 null-body hinge phase.

## C58 structure theorem

For a selected normalized KKT stress in the C56-Z phase,

`K = Q^T Lambda^+ Q = B_H^{-1}`.

Hence the positive diameter graph `H_s` is a forest. On each connected component `T`,
for any two component vertices `u,v`,

`R_eff(u,v) = sum_{e in P_T(u,v)} 1/beta_e`.

Thus the physical contact response restricted to `V(T)` is exactly the positive
weighted tree metric of `T`.

The circular-planar response makes this tree metric Kalmanson in the induced force-hull
order. Every positive tree-edge split must therefore be circular: a noncircular split
would give four alternating vertices for which the tree four-point crossing sum is
strictly minimal, while the Kalmanson inequalities require it to be maximal.

A diameter-tree component with two disjoint edges would have a connector edge whose
circular split places the two endpoint pairs in complementary intervals. Their chords
would not cross, contradicting the geometric diameter-thrackle property. Hence every
component has matching number one and is a star.

Therefore

`H_s = disjoint union of diameter stars`.

## Uniform component bound in the triangle-free source

A star component with center `o` and leaves `v_i` has additive resistance metric

`W_xy = r_x+r_y`,

where `r_o=0` and `r_vi=1/beta_(o,vi)`.

For a component with `q>=4` terminals, the source-preserving SEPq theorem gives one
vertex whose deletion separates all of those terminals, with contact degree at least
`q` if it is not a designated terminal and at least `q-1` if it is.

Every vertex in a triangle-free unit-contact graph has degree at most five. Consequently

`q <= 6`,

so every zero-transfer diameter star has degree at most five. A six-terminal component
forces a separating terminal of positive-contact degree exactly five.

## C57 body consequence

Every extreme stress of the C54 null face is a rigid body for every strong-framework
flex. If two such bodies rotate at different angular rates, C57 makes their midpoint a
C56-Z stress. C58 therefore forces

`H_a union H_b`

to be a degree-at-most-five star forest. Every midpoint star with at least four
terminals also has a source-preserving one-vertex contact separator.

Thus the remaining body-hinge mechanism is local and bounded: it cannot use a long
zero-transfer diameter path, caterpillar, or cycle.

## Next exact target

For two differently rotating null-face bodies meeting at one source vertex `z`, prove
that the C58 bounded-star/separator structure either forces their angular rates to
agree or allows a finite same-diameter hinge rotation.

For one pair of bodies, the second route is nearly explicit. After subtracting one
body's rigid motion, the other rotates about `z`. Any cross-body strong active pair has
zero radial first variation, so its endpoints and `z` are collinear. A cross-body
strong diameter shortens at second order under finite rotation, while a cross-body
strong unit contact lengthens. The remaining obstruction is compatibility of three or
more bodies in a closed pin cycle.
