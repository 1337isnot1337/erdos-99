<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "91dff8d1e52285b94725390869ee0a7e3802b765", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support3_orientation_symmetry_2026-09-29.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "56f0663f8d7bd0cf6cb06f6215530a7e6d96f87e7f58b87877b619bfc61133a8"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: support3 orientation symmetry reduction

Date: 2026-09-29

Status: proved support-automorphism reduction, independently checked by an exact executed finite verifier, for the third surviving support in the exact two-selected-singleton support narrowing:

`[0123]^3 [0124]^2 [0134]^2 [0234]^2`.

This note does not exclude the support. It reduces its exact orientation frontier from 27 raw assignments to 7 symmetry classes.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support3_orientation_symmetry_2026_09_29.py`

Executed verifier blob:

`b5ec9748586b87984dd705c1e9811333be84f8e7`.

## 1. Support automorphism group

Count weighted support incidences at the seven labels. They are

- vertex 0: 9;
- vertices 1,2,3: 7 each;
- vertex 4: 6;
- vertices 5,6: 0 each.

Hence any support automorphism fixes 0 and 4, preserves `{1,2,3}`, and preserves `{5,6}`. Conversely every permutation of `{1,2,3}` and every permutation of `{5,6}` preserves the weighted support multiset. Thus the full support automorphism group is exactly

`S_3({1,2,3}) x S_2({5,6})`,

of order 12. The second factor acts trivially on the orientation choices because labels 5 and 6 occur in none of these supports.

## 2. Raw orientation space

The multiplicity-three support `[0123]^3` contains all three unoriented four-cycles and therefore carries no choice. Each of `[0124]^2`, `[0134]^2`, and `[0234]^2` chooses two of the three possible unoriented four-cycles, equivalently one missing cycle. Thus there are exactly

`3^3 = 27`

raw orientation assignments.

The verifier orders the varying supports as

`[0124], [0134], [0234]`

and labels states `0,1,2` by the lexicographically ordered two-subsets of the three canonical unoriented cycles on that support.

## 3. Burnside reduction

The exact verifier enumerates all 12 support automorphisms and their induced permutations of all 27 assignments. Its fixed-assignment census is

- 2 group elements fix all 27 assignments;
- 10 group elements fix exactly 3 assignments.

The two elements fixing all 27 are the identity on the used labels, with either action on the unused pair `{5,6}`. Therefore Burnside gives

`(2*27 + 10*3)/12 = 7`

orientation classes.

The exact orbit-size census is

`1^1, 2^1, 3^2, 6^3`,

which accounts for all 27 assignments.

Canonical representatives under the state convention above are:

1. `(0,0,0)`, orbit size 6;
2. `(0,0,1)`, orbit size 3;
3. `(0,1,0)`, orbit size 6;
4. `(0,1,1)`, orbit size 6;
5. `(0,1,2)`, orbit size 3;
6. `(0,2,0)`, orbit size 2;
7. `(1,1,1)`, orbit size 1.

The verifier fail-closes on the exact 12-element automorphism set, the fixed-point census, the Burnside count, the orbit-size census, and the ordered representative list.

## 4. Consequence

After the exact support-level narrowing and the exact exclusions of supports 1, 2, and 12, the two-selected-singleton profile has ten unresolved support orbits: supports 3 through 11 and support 13 in the committed 13-orbit list.

For support 3 specifically, it is sufficient to run the exact rank-four aggregate-space/generalized-weight/structural exclusion on the seven representatives above rather than all 27 raw orientations. No exclusion of those seven representatives is claimed here.
