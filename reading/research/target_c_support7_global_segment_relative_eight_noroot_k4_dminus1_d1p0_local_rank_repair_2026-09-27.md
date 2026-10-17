> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d1p0_local_rank_repair_2026-09-27.md) · source SHA-256 `80496bc6a00e1c785fb4a7c281fcdc1ec9fca6488143960ef60d010d63da9ac5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "616d89593d3e475a5ce8105ed2f498c09b7cacd7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d1p0_local_rank_repair_2026-09-27.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "866b6432826462454cb08826586a19503275c4e6080cd7e044c8b2299e06bd7b"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: repair the eight-no-root k=4, D=-1, d_root=1, p=0 local-rank certificate

Date: 2026-09-27

Status: exact support-level repair of the closure recorded in
`research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d1p0_support_closure_2026-09-26.md`.
The old verifier used the false converse that a touched empty block has local rank two only when a containing tetrahedral support repeats. This note removes that converse and reruns a strictly larger support relaxation. The repaired relaxation still has zero survivors.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d1p0_local_rank_repair_2026_09_27.cpp`

## 1. Defect in the old certificate

For a touched triangle block `b`, let `E_b` be the local empty-state coefficient space and `I_b` the set of external occurrences whose tetrahedral supports contain `b`.

The old verifier classified

- `dim E_b = 2` iff one containing tetrahedral support is repeated;
- `dim E_b = 1` otherwise.

Only the implication from a repeated containing support to rank two is support-determined. The converse is false. Distinct containing tetrahedral supports can produce two independent local quotient directions; the explicit counterexample is recorded in
`research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus2_d0p2_local_rank_repair_2026-09-27.md`.

Therefore the old verifier is not a valid standalone certificate.

## 2. Sound local-rank relaxation

The branch data remain

`rank(P)=4`,

`(d1,d2,d3,d4)(P) >= (2,4,5,7)`,

and the already proved incidence bound `h<=24`.

The repaired verifier uses only support-level implications that remain valid:

- if a containing tetrahedral support repeats, then `dim E_b=2`; an actual-empty block therefore needs `|I_b|>=4` by `d2>=4`;
- if no containing support repeats and `|I_b|<2`, the block cannot be actual-empty by `d1>=2`;
- if no containing support repeats and `2<=|I_b|<=3`, an actual-empty block can only have rank one, because rank two would violate `d2>=4`;
- if no containing support repeats and `|I_b|>=4`, the verifier permits both ranks one and two.

The last case is deliberately an over-approximation. It avoids any orientation-dependent rank inference from support multiplicities.

For any chosen local dimensions, the same generalized-weight compatibility conditions remain necessary:

- line-line: `|I intersect J|>=2` or `|I union J|>=4`;
- plane-line: `|I intersect J|>=2` or `|I union J|>=5`;
- plane-plane: `|I intersect J|>=4`, or both `|I intersect J|>=2` and `|I union J|>=5`, or `|I union J|>=7`.

Because `p=0`, every touched incomplete block is actual-empty. Thus the repaired search enumerates every support-level local-dimension assignment compatible with the necessary generalized-weight constraints, including every actual oriented state.

## 3. Root-deficiency and face-local conditions

Let `T` be the touched triangle-block set, `E` the touched empty subset, and `C=T\E` the touched complete subset.

Root deficiency one implies that the full complete-root family has triangle-row nullity one, so it contains at most sixteen blocks. Hence every actual state satisfies

`|E| >= h-16`.

Every subset of that complete family has nullity at most one, so the repaired verifier requires

`|C| - rank H(C) <= 1`.

All four external relation directions survive modulo the complete-root span and lie in the touched face-row span. Replacing the full complete span by the smaller touched-complete span only enlarges the quotient, so every actual state necessarily satisfies

`rank H(T) - rank H(C) >= 4`.

Finally, the chosen local coefficient spaces must have nominal dimension sum at least four and occurrence support on at least seven of the eight external coordinates, by `rank(P)=4` and `d4(P)>=7`.

All of these are necessary conditions. The verifier does not impose orientation-specific conditions that could accidentally discard an actual state.

## 4. Exact finite certificate

Canonical augmentation reproduces the established `S_7` orbit counts for support-multiset sizes zero through eight:

`1,1,4,14,61,268,1283,6032,27763`.

Among the 27,763 size-eight orbits, exactly 26,580 have `h<=24`.

The repaired search gives the following executed census:

- size-eight support orbits: `27763`;
- orbits with `h<=24`: `26580`;
- relaxed final local-rank tests satisfying the count/dimension/support filters: `33192`;
- those also having touched-complete nullity at most one: `909`;
- those with face-local capacity at least four: `0`.

For comparison, the old false-converse search had only 32,060 final tests and 908 nullity-admissible tests. The repaired search is strictly larger and still has no survivor.

All support operations are exact integer combinatorics. Triangle-row ranks are computed modulo `2^31-1`; the verifier checks the Lucas-Lehmer condition for this Mersenne prime. Each triangle row has squared norm three and triangle-row rank is at most fifteen, so `(2^31-1)^2 > 3^15` and Hadamard imply that every modular rank used by the verifier equals the corresponding rational rank.

## 5. Result and audit consequence

The branch

`k=4, D=-1, d_root=1, p=0`

remains closed after removing the false local-rank converse.

This repairs a second dependency in the eight-no-root closure chain. It does not certify other older support-level verifiers that made the same converse. Those still require separate monotonicity audits or repaired reruns before the global eight-no-root barrier can be treated as fully re-audited.
