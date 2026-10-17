> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_nine_noroot_k5_dminus2_d0p4_support_closure_2026-09-30.md) · source SHA-256 `60e5916892358ae5e14cb2b587e02a19195534fd267d4d350d985e1ee749fa78`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3f5d914fdf6400056ddd5378534e2906130fa6cc", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_nine_noroot_k5_dminus2_d0p4_support_closure_2026-09-30.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "fa0d8b390fe4ad3a42a7d4c4f4d7b88bac4d5dd1d9252d8bc9d309c2121bf5a7"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: nine-no-root k=5, D=-2, d_root=0, p=4

Date: 2026-09-30

Status: exact closure of this arithmetic branch, conditional on current-main lower-layer theorems.

Current main gives rank(P)=4 and generalized weights at least (3,4,6,7). If d2=4, puncturing a four-coordinate support of a two-dimensional subcode has rank loss exactly two and produces a five-no-root k=3 shadow with D=0. If all four selected rows remain touched, this contradicts the committed p=4 theorem D>=3. If any selected row becomes untouched, stripping inert rows gives p<=3 and negative defect, contradicting the committed p<=3 theorem D>=2. Hence d2>=5 and the weights are at least (3,5,6,7).

The face-local k=5 condition gives rank H(T)-rank H(C)>=5. Since d_root=0 and the full triangle-row rank is 15, |C|<=10. With p=4, at most four touched nonempty incomplete blocks occur, so e>=h-14. Empty touched blocks have at least three incidences; the nine external cycles give 36 incidences. Thus 36>=h+2e>=3h-28 and h<=21.

The exact support relaxation uses the repaired local-rank rule from current main. A repeated containing tetrahedral support forces local empty rank two, so at least five incidences are required. Without a repeated containing support, the verifier permissively allows rank one from three incidences and rank two from five. It uses only necessary pairwise consequences of weights (3,5,6,7), discards all coefficient restrictions on the at-most-four selected nonempty incomplete blocks, and does not require the local spaces to glue to a common rank-four P.

For a proposed empty set E, put R=T\E. Any actual state has an independent complete subset C of R with |R\C|<=4 and rank H(T)-|C|>=5. The verifier therefore keeps a candidate whenever

    max(0, |R|-4) <= min(|R|, rank H(R), rank H(T)-5).

This is a strict relaxation of realizability.

Executed census:

    size9_orbits 121458
    raw_size9_extensions 966977
    h_le_21_raw_extensions 368746
    h_le_21_size9_orbits 50745
    supports_with_empty_candidate 1168
    relaxed_empty_tests 2318
    relaxed_survivors 0

The verifier independently checks the S7 Burnside counts and canonical augmentation. Triangle-row ranks are certified over Q by computation modulo 2^31-1, Lucas-Lehmer, and the Hadamard bound (2^31-1)^2 > 3^15.

The exact three-file source set compiled and executed for this census is persisted on this branch:

- research/verify_target_c_support7_global_segment_relative_nine_noroot_k5_dminus2_d0p4_support_closure_2026_09_30.cpp, blob 2e21d1296c0e6e2ae8dfc9e1e2b140b5168debe5
- research/k5_d0p4_search.hpp, blob 1599772d236b631edb4ff46a153e3dacc240b632
- research/k5_d0p4_geom.hpp, blob 407b8626686fa53b4a3dfe6cc2cdf89dced47525

Those hashes exactly match the locally executed files. No unexecuted verifier code is used in the closure claim.

Conclusion: no nine-no-root state exists with k=5, D=-2, d_root=0, p=4.

Remaining k=5 arithmetic branches are D=-2,d_root=1,p=1 and the two D=-1 branches (d_root,p)=(0,5),(1,2). A separate pushed branch already contains the D=-2,d_root=1,p=1 certificate.
