<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "a7300ce99eb248b7e40b8bc61e7789453895e34c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_nine_noroot_k5_dminus1_d0p5_corrected_orientation_closure_2026-09-29.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "4b84dc0afa124a03760a9cc90273a794138d4997d8dfbf8fa32873d57ea390b2"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: corrected d0p5 closure

Exact rational enumeration with the current-main helper closes S2--S8 under the correct containment E_b <= P, dim P = 4. Together with the committed S1 closure, the nine-no-root k=5, D=-1, d_root=0, p=5 branch is closed.

For U = span(E_b), any realization needs rank(U) <= 4. The structural necessity is max(0,|R|-5) <= min(|R|, rank H(R), rank H(T)-5). The generalized-weight floor (3,4,6,7) forces restriction ranks 4,3,2,1 on zero-sets of sizes 7,6,4,3. If rank(U)=r, any extension U <= P can raise a restriction rank by at most 4-r.

Executed census (orientations, rank<=4 empty subsets, structural survivors, rank-3 survivors, rank-4 survivors, extension survivors): S2=(9,531,0,0,0,0), S3=(9,1296,189,117,72,0), S4=(9,1314,180,54,126,0), S5=(27,1593,0,0,0,0), S6=(81,4755,0,0,0,0), S7=(27,4158,621,0,621,0), S8=(9,1134,117,9,108,0).

The computation used exact Fraction arithmetic and byte-identical helper blob 867e8e583f6073c92b1f7afbf2aaf536e2567fa9. The executed standalone verifier had Git blob 6596f48f6b09b149654c6ae1fc4d2e2fa28e907a.

## Salvage provenance and current scope

Salvaged on 2026-10-04 from `target-c-k5-d0p5-corrected-closure-20260929-run11`
at tip `d043347b100fb47f16281345491e26c723a35337`. The companion verifier was
rerun with Python 3 on this fresh-main branch and reported
`PASS: corrected E_b<=P certificate closes S2--S8` with zero extension survivors
in every enumerated support family. Its exact helper is the current-main file
`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_orientation_2026_09_28.py`
(blob `867e8e583f6073c92b1f7afbf2aaf536e2567fa9`).

This closes only the `k=5, D=-1, d_root=0, p=5` support-7 branch, together with the
main-represented S1 obstruction and the stated current-main lower-layer support
reductions. It is not a proof of global optimality or Level I, does not close other
nine-no-root profiles, and does not change theorem state. Lifecycle on integration is
**unreviewed** pending mathematical review.
