<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c90cda423b94215ab53232e50e7a8579e0829f5b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support4_orientation_symmetry_2026-09-29.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1427255c2c75a298e09bb2a813d0dfb9bc75e8121236b654cdbcdafddc54c4b8"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: support4 orientation symmetry reduction

Support: [0123]^3 [0124]^2 [0134]^2 [0234] [1234].

Companion verifier:
research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support4_burnside_2026_09_29.py

Executed verifier blob: 246b9b29337c0a5bf025dc933f58a331f06330ff.

The weighted vertex-incidence degrees are (8,8,7,7,6,0,0). Therefore every support automorphism preserves {0,1}, {2,3}, {4}, and {5,6} setwise. Conversely the swaps a=(0 1), b=(2 3), and z=(5 6) independently preserve the weighted support multiset. Hence the full support automorphism group is <a,b,z>, of order 8. The unused-label swap z acts trivially on orientations.

Write the four varying supports as A=[0124]^2, B=[0134]^2, C=[0234], D=[1234]. Each has three orientation states. The multiplicity-three support [0123]^3 has no choice, so the raw orientation space has 3^4=81 assignments.

Use the lexicographic state convention for the three unoriented-cycle choices. The effective generators act as follows.

For b=(2 3): A and B are exchanged with the same state; C and D are individually fixed as supports but their state labels are transposed 0<->2. A fixed assignment therefore has A=B (3 choices) and C=D=1, so b fixes 3 assignments.

For a=(0 1): A and B are individually fixed as supports but their state labels are transposed 1<->2; C and D are exchanged with the same state. A fixed assignment therefore has A=B=0 and C=D (3 choices), so a fixes 3 assignments.

For ab: A and B are exchanged while their state labels are transposed 1<->2, so A may be chosen freely and determines B (3 choices). C and D are exchanged while their state labels are transposed 0<->2, so C may be chosen freely and determines D (3 choices). Thus ab fixes 9 assignments.

The identity fixes all 81 assignments. Since z acts trivially, each effective element has two lifts in the full order-8 group. The fixed-point census is therefore 81^2, 9^2, 3^4. Burnside gives

(2*81 + 2*9 + 4*3)/8 = 24

orientation classes. Thus support4 is rigorously reduced from 81 raw orientation cases to 24 support-automorphism classes.

The executed verifier checks this induced effective action on all 81 assignments, the fixed-point census, the Burnside count, and the orbit-size census 1^1, 2^6, 4^17. The support-automorphism classification and the induced state-label action are proved above, so the finite script is an audit check rather than an unproved source of those facts.

This note does not exclude any of the 24 classes. Supports 1, 2, 3, and 12 are already excluded; supports 4 through 11 and 13 remain unresolved.
