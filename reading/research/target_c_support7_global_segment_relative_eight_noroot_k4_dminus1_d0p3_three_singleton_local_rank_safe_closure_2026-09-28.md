> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_three_singleton_local_rank_safe_closure_2026-09-28.md) · source SHA-256 `d8655e0f197490b3604990771e1d20e1dc920b455fa1d06972268debf734a94a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "301e309ce6cc154ec0928b776db216c74e2f05a0", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_three_singleton_local_rank_safe_closure_2026-09-28.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c34ba1726125b65697f642d22173b4abef755e8955fcb7443dc6bec205351d7e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: three-singleton local-rank-safe closure

Date: 2026-09-28

Scope: eight-no-root `k=4, D=-1, d_root=0, p=3`, three-singleton profile.

Current main gives a rank-four coefficient space `P<=Q^8` with generalized weights at least `(2,4,5,7)`. Distinct projective weight-two lines have disjoint supports, so their number `r` is one of `0,1,2,3,4`. These five cases are exhaustive.

The known local-rank defect was the invalid converse that nonrepeated containing supports force local rank one. The repaired certificates do not use that converse to exclude states.

- `r=0`: the integrated monotonicity audit shows that the old support tag only enlarges the virtual-empty family. The existing exact census over 27,763 support orbits remains valid.
- `r=1`: the current-main repaired verifier was recompiled and rerun in this audit: 777,364 pair tests, 2,393,667 singleton triples, zero structural passes.
- `r=2`: the integrated repaired verifier was rerun: 210 disjoint pairsets, 5,830,230 orbit/pairset tests, 2,437,069 singleton triples, zero structural passes.
- `r=3`: the repaired verifier was hardened to fail unless the expected census is reproduced, then rerun: 13,574 `h<=20` orbits, 420 matchings, 5,701,080 tests, 676,371 singleton triples, zero structural passes.
- `r=4`: the integrated perfect-matching repair was rerun: 13,574 `h<=20` orbits, 105 perfect matchings, 1,425,270 tests, 47,546 singleton triples, zero structural passes.

For `r>=1`, each repaired search forms supersets `E*` and `S*` containing every actual empty block and selected singleton. For an actual singleton triple `S`, `C*=T\(E* union S)` is contained in the actual complete family. Since `d_root=0`, `H(C*)` is independent, and face-local capacity requires `rank H(T)-rank H(C*)>=4`. Thus zero survivors in the relaxed searches exclude all actual states.

The modular triangle-row rank tests are exact over the rationals by the checked `2^31-1` primality and Hadamard bound used by the verifiers.

Therefore the three-singleton profile has no realizable state. This does not by itself re-audit the separate mixed singleton-plus-pair profile or close the global problem.
