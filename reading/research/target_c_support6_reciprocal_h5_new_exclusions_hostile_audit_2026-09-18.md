> Generated reading edition · [exact source](../../research/target_c_support6_reciprocal_h5_new_exclusions_hostile_audit_2026-09-18.md) · source SHA-256 `d9c54a5e08b6686de0adbaafcd124965887ff4103b000145a927ba51ae340fd2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "30339efce4fe8d798db86ecdd3ee21b587dc7ec4", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_reciprocal_h5_new_exclusions_hostile_audit_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e9efc4424692245d2f952019b5602a2b51f700a579ab7a401ee7db5ee4932130"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — simple-wall and uniform-angle reciprocal `H5` exclusions

**Date:** 2026-09-18  
**Audited notes:** `target_c_support6_reciprocal_h5_simple_wall_exclusion_2026-09-18.md`; `target_c_support6_reciprocal_h5_uniform_angle_exclusion_2026-09-18.md`  
**Disposition:** PASS with the scope limits below. C-II remains open.

## 1. Simple-wall ground reduction

The simple-wall proof does not assume six distinct ground rays. It explicitly merges the unique coincident pair and uses its signed multiplicity `+/-2`. The preceding same-sign duplicate-ray lemma is required here; if the tied rays had opposite signs the multiplicity argument would be invalid, but that case was already excluded independently.

After merging, the five ray classes are distinct. The ground cone has width `<pi/3`, so the forward unit-circle chords have strictly increasing arguments in one open halfplane. The two coefficient words certified by exact enumeration have prefix sums `(1,-1,0,-1)` and `(1,0,1,-1)`. Summation by parts gives exactly `Delta_1=Delta_2+Delta_4` and `Delta_4=Delta_1+Delta_3`. In each equation the right-hand side is a positive sum whose argument lies strictly between the arguments of its summands, so it cannot equal the extreme chord on the left. No length comparison or floating-point estimate is hidden in the argument.

The certificate imports the previous exact H5 enumerator rather than reimplementing it. It reproduces all `80` simple-wall labelled survivors and partitions them `40+40` between the two words.

## 2. Concave-pentagon identity

For the uniform-angle proof, the reciprocal polygon `0-1-2-3-6` is simple. Edges `01,12,23` are convex-hull boundary edges. Because `6` is an interior reciprocal point, segments `36` and `60` lie in the convex hull and cannot cross its boundary except at `3` and `0`; they meet each other only at `6`.

The exact turn pattern `(+,+,+,+,-)` therefore has its ordinary simple-polygon meaning: vertex `6` is the unique reflex vertex. If `C=angle 360` is the smaller raw angle, the polygon interior angle there is `2pi-C`, giving `A+B-C+D+E=pi` from the pentagon angle sum. This identity is geometric and does not assume reciprocal equilibrium.

At vertex `3`, the certificate checks that edges `32` and `36` are consecutive in the exact regular force tournament and have opposite reciprocal signs. Reversing exactly one raw ray changes the smaller raw angle `B` to the consecutive force gap `pi-B`; the strict source one-turn bound therefore gives `B>pi/3`. At vertex `6`, edges `63` and `60` are force-consecutive with equal signs, giving `C<2pi/3`. The hull bounds `D,E>2pi/3` are already proved for the non-ground H5 hull vertices. Uniformity gives `A>0`. The resulting strict lower bound on `A+B-C+D+E` is strictly greater than `pi`, so there is no endpoint-equality loophole.

The finite certificate groups all `48` labelled uniform survivors into the existing six symmetry orbits and finds a valid obstructed representative in exactly three orbits. Eliminating one representative eliminates its whole orbit because the symmetries are relabeling/reflection/global-sign symmetries of the reciprocal equations and source angle conditions.

## 3. What remains

These notes do not eliminate the other three uniform H5 sign/order orbits. Numerical experiments are not used as proof and are not committed as theorem claims. The collapsed support-six branch is also untouched; the repository now contains an exact local realization showing that branch cannot be removed using only the existing six local pentagon closures and local turn inequalities.

After these two exclusions, the noncollapsed degree-pure support-six branch has exactly three uniform H5 sign/order candidates. Proving those three metrically impossible would eliminate the noncollapsed support-six endpoint. Eliminating support six globally would still additionally require a genuinely global obstruction to the collapsed branch.

**Audit disposition:** both new exclusions are supportable as stated; theorem-state authority remains unchanged.
