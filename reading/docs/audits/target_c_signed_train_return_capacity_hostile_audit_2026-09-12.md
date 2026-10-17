> Generated reading edition · [exact source](../../../docs/audits/target_c_signed_train_return_capacity_hostile_audit_2026-09-12.md) · source SHA-256 `eb37f917899cfd19007ed347d4a64f85691f85a88774ea1c554c56f545c80afe`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B3E815D5E7CF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C signed train-return capacity

**Date:** 2026-09-12  
**Audited artifact:** `docs/reports/target_c_signed_train_return_capacity_2026-09-12.md`  
**Disposition:** PASS for the finite oriented-return lemmas; the all-regime route application remains conditional.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This audit checks the finite endpoint orientation, host-width, and area-transport
claims. It does not promote them to theorem-state authority and does not supply the
missing source-specific three-route budget.

## 1. Endpoint orientation and signed projection

For a complete straight train, choose its unit edge direction `u` from one end to the
other. The incident rhombus lies on opposite sides of the train at its two physical
ends. Orienting a boundary edge with its incident rhombus on the left therefore gives
the two endpoint vectors `u` and `-u`. This is an oriented statement, not a
projective one; a square with opposite horizontal sides is the required sanity check.

For a directed walk `W_j`, with unit edge steps `v_{j,r}` and displacement direction
`q_j`,

`ell_j-|z_j| = sum_r (1-q_j dot v_{j,r})`.

If a train's two good endpoints are injected into occurrences on walks `i,j`, their
combined contribution is

`(1-q_i dot u)+(1+q_j dot u) = 2-(q_i-q_j) dot u`.

Since this is at least `2-|q_i-q_j|`, summing over the injective assignments proves
the stated two-good-end bound. A train that is not two-good consumes at least one
bad endpoint, so the count of two-good trains is at least `(k-b)_+`. No train-end
occurrence is reused in this summation.

## 2. Three-host optimization

The width of a host set in direction `u` is

`w_Q(u)=h_Q(u)+h_Q(-u)`.

For two crossing train directions `u,v` and positive weights `a,b`, the four support
vectors are `au,-au,bv,-bv`. With at most three hosts, two of these four support
requests use the same host. The loss from merging a cross pair is at least

`a+b-sqrt(a^2+b^2+2ab cos(phi))`

after choosing the acute representative of the projective angle `phi`; merging an
opposite pair costs `2a` or `2b`, which is no smaller. The cross-pair loss is the
minimum by the triangle inequality. At `a=b` and `phi=pi/3` it is `2-sqrt(3)`.
Thus two crossing trains with projective angle strictly above `pi/3` incur the
positive return charge claimed in (TW.1). The construction in the source shows the
constant is sharp as a host-set relaxation; it is not asserted to be a realizable
global minimizer.

## 3. Area transport

At a retained-retained rhombus crossing, the two train charges sum to at least
`2-sqrt(3)`. Along one complete train, the sum of strict-rhombus areas is its
transverse displacement, up to the fixed unit-edge normalization, and is at most
the diameter `d` of the convex container. Summing each rhombus through its two
trains therefore gives

`d E >= (2-sqrt(3)) A_gg`.

If a train has a bad endpoint, it is excluded from the two-good family. There are at
most `b` such trains, and each train carries at most `d` total rhombus area. The
union of rhombi incident to excluded trains has area at most `bd`; every remaining
rhombus is retained-retained. This proves

`A_gg >= (A_4-bd)_+`

and the displayed all-train area bound. The argument counts train incidences rather
than boundary vertices, so holes, disconnected components, and bridge occurrences
do not create an uncharged endpoint.

## 4. Diffuse bad-end estimate

For a fixed other train, bad trains whose crossing angle lies in an `epsilon`
neighborhood of `pi/3` occupy two projective direction intervals of length
`epsilon`; there are at most `2 M_bad(epsilon)` of them. Summing over at most `T`
other trains gives `2 T M_bad(epsilon)`. Crossings with angular excess greater than
`epsilon` number at most `Delta/epsilon`, because each contributes more than
`epsilon` to the total angular defect. Since each train pair crosses at most once,
these counts are valid even with repeated boundary occurrences. Hence (DP.1) and
(DP.2) follow.

The order of limits in the source is essential: first fix epsilon and let `D` grow,
then let epsilon decrease. The condition that the bad-end profile is diffuse is not
deduced from linear endpoint abundance and must remain an explicit hypothesis.

## 5. Scope and classification

The finite SR/TW/AT/DP statements are audited-working candidate lemmas under the
canonical complete-train and strict-rhombus scopes. The Section-101/102 application
is only conditional on a simultaneous injective assignment to at most three actual
boundary walks, with all bad endpoints and route excess accounted for. No arbitrary
phase cut is treated as a physical boundary, and no contact-isolated source point is
deleted.

**Final audit verdict:** PASS for the stated finite oriented-return package. The
missing all-regime route/excess comparison and the Type-I branch remain open.
