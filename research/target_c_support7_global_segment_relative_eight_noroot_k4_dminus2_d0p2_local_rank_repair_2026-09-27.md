<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "9bd58ea5eb598c15419a8bc1ed30f90523548076", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus2_d0p2_local_rank_repair_2026-09-27.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e1f6796323e4c77d1ee9201139ff47689619341a8b7eb496e29ad0ffd324ab9e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: repair the eight-no-root k=4, D=-2, d_root=0, p=2 local-rank certificate

Date: 2026-09-27

Status: exact support-level repair of the closure recorded in
`research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus2_d0p2_support_closure_2026-09-26.md`.
The old support verifier used a false converse for the local empty-block rank. This note removes that converse and reruns a strictly larger support relaxation. The repaired relaxation still has zero survivors.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k4_dminus2_d0p2_local_rank_repair_2026_09_27.cpp`

## 1. Defect in the old certificate

For a touched triangle block `b`, let `E_b` be the local empty-state coefficient space and `I_b` the set of external occurrences whose tetrahedral supports contain `b`.

The old verifier classified

- `dim E_b = 2` iff one containing tetrahedral support is repeated;
- `dim E_b = 1` otherwise.

Only the forward implication is support-determined. The converse is false: distinct containing tetrahedral supports can also give two independent local quotient directions.

A concrete exact example already follows from the quotient coordinates in
`research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py`.
For `b={1,2,5}`, the no-root cycles with descriptors

`(1,2,3,5)`, `(1,2,4,5)`, `(1,2,5,6)`

have three distinct tetrahedral supports, while their local quotient vectors at `b` are

`(-1,1)`, `(-1,1)`, `(1,0)`.

The corresponding empty-state coefficient rows are independent, so `dim E_b=2` despite the absence of a repeated support.

The old verifier therefore is not a valid standalone certificate.

## 2. Sound local-rank relaxation

The branch data remain

`rank(P)=4`,

`(d1,d2,d3,d4)(P) >= (4,5,6,7)`,

and the already proved incidence bound `h<=20`.

The repaired verifier uses only support-level implications that are safe:

- if a containing tetrahedral support repeats, then `dim E_b=2`; an actual-empty block therefore needs `|I_b|>=5` by `d2>=5`;
- if no containing support repeats and `|I_b|<4`, the block cannot be actual-empty by `d1>=4`;
- if no containing support repeats and `|I_b|=4`, an actual-empty block can only have rank one, because rank two would violate `d2>=5`;
- if no containing support repeats and `|I_b|>=5`, the verifier permits both ranks one and two.

The final case is deliberately an over-approximation. It does not try to infer orientation-dependent rank from support multiplicities.

For any chosen local dimensions, the same generalized-weight compatibility conditions remain necessary:

- line-line: `|I intersect J|>=4` or `|I union J|>=5`;
- plane-line: `|I intersect J|>=4` or `|I union J|>=6`;
- plane-plane: `|I intersect J|>=5`, or both `|I intersect J|>=4` and `|I union J|>=6`, or `|I union J|>=7`.

For the one-selected-pair profile, the pair contributes no coefficient constraint. For the two-selected-singleton profile, each touched singleton is still relaxed to either a zero constraint or an arbitrary line supported in its occurrence set. Thus every actual oriented state is represented by at least one state searched by the repaired verifier.

## 3. Structural conditions retained

Let `T` be the touched triangle blocks, `I` the touched incomplete blocks, and `C=T\I` the touched complete blocks.
Because `d_root=0`, the rows indexed by `C` must be independent. The face-local relation capacity still requires

`rank H(T) - rank H(C) >= 4`.

The repaired verifier imposes these conditions exactly. It deliberately drops the old redundant tetrahedron-boundary injectivity check; removing a necessary filter only enlarges the search, so a zero-survivor result remains sufficient.

The coefficient generators must have nominal total dimension at least four and occurrence support covering at least seven of the eight external coordinates, by `rank(P)=4` and `d4(P)>=7`. These again are necessary conditions only.

## 4. Exact finite certificate

Canonical augmentation reproduces the established `S_7` orbit counts for support-multiset sizes zero through eight:

`1,1,4,14,61,268,1283,6032,27763`.

Among the 27,763 size-eight orbits, exactly 13,574 have `h<=20`.

The repaired search enumerates every admissible rank assignment in the sound relaxation above and both `p=2` root profiles. Its executed census is

- size-eight support orbits: `27763`;
- orbits with `h<=20`: `13574`;
- pair-profile relaxed final tests: `2091`;
- two-singleton-profile relaxed final tests: `775064`;
- pair-profile survivors: `0`;
- two-singleton-profile survivors: `0`.

Hence no actual state can realize this branch.

All support operations are exact integer combinatorics. Triangle-row ranks are computed modulo `2^31-1`; the verifier checks its Lucas-Lehmer primality condition. Each triangle row has squared norm three and the triangle-row rank is at most fifteen, so the checked inequality `(2^31-1)^2 > 3^15` is more than sufficient for Hadamard to make every modular rank equal the rational rank.

## 5. Result and audit consequence

The branch

`k=4, D=-2, d_root=0, p=2`

remains closed after removing the false local-rank converse.

This repairs one dependency in the eight-no-root closure chain. It does not by itself certify every other older support-level verifier that used the same converse. Those certificates still require individual monotonicity audits or analogous relaxed reruns before the global eight-no-root barrier should be treated as fully re-audited.
