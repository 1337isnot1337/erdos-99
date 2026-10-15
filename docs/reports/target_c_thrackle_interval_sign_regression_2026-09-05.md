<!-- theorem-state: {"artifact_id":"ART-9F51A35CD025","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — regression against the arbitrary-thrackle PSD lemma

**Date:** 2026-09-05\
**Status:** WITHDRAWN — incompatible projective order and orientation

**Correction (2026-09-09):** The argument below is preserved as rejected history.
Its order uses the upper-half-plane cut but its covector orients into the right
half-plane. Consistent normalization satisfies both inequalities. See the complete
[orientation and C-I restoration audit](target_c_c53_orientation_and_ci_restoration_2026-09-09.md).
The reproduction script now checks the corrected normalization exactly.

The report `target_c_arbitrary_thrackle_response_contraction_2026-08-31.md`
uses Lemma C53.T to extend the weighted Robinson argument from a matching to an
arbitrary geometric thrackle. The following claimed refutation was incorrect.

Take a strictly convex regular pentagon with vertices `0,1,2,3,4` in cyclic
order and chords `e=(0,2), f=(0,3), g=(1,3)`. Every pair intersects: the first
two pairs share endpoints and `e,g` cross in the interior. Their projective
directions are ordered `f,g,e`. Choose the common covector `ell=(1,0)`; this
reverses all three displayed edges. For interval `A={0}`, the C53.T signs are
`z_f=-1,z_g=0,z_e=-1`, so its first inequality becomes
`z_e*(z_f-z_g)=(-1)*(-1)=1>0`, contradicting the claimed nonpositive sign.

All three chords are equal-length pentagon diagonals, of length
`sqrt((5+sqrt(5))/2)`, and the shared-endpoint angle is 36 degrees. Thus this
is an equal-diameter geometric thrackle regression, not an arbitrary-chord
artifact. C53.4--C53.6 are conditional until a shared-endpoint coupling theorem
is supplied.

## Matching-decomposition repair (rejected)

Decomposing the bounded-degree diameter graph into finitely many matchings does
not restore C53. The matching inequalities use different edge-space inverses;
they cannot be summed because cross-matching response entries remain. A valid
repair requires a new shared-endpoint coupling theorem.

An enumeration of regular n-gons for 5 <= n <= 12, over every equal-step
diagonal family and every pairwise-intersecting triple, finds the same failure
for every nontrivial step tested. This is computational corroboration only; the
five-gon certificate above is the proof-level regression.
