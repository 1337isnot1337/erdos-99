> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k5_final_order2_execution_dminus2_transfer_closure_2026-09-25.md) · source SHA-256 `fa0adf384645add8c3dd82ff0d0fa1e3e3960fd10b32716b798df3476a1f3db9`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f88c7206419a11f8ad8d40b94eb17c7e567835da", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k5_final_order2_execution_dminus2_transfer_closure_2026-09-25.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "54ef1a0d349edbe393969407c9fd7f179f37aaa5b131ea16bd993cb8b3e5aa19"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: final order-2 execution and D=-2 transfer closure

Date: 2026-09-25

This run executed an independent exact reconstruction of the current-main verifier for the last touched-nullity-four (3,2,2,1) support orbit {1234,1235,1267,1467} in the eight-no-root k=5,D=-1,d_root=1,p=3 branch.

The support stabilizer has order 2. There are 198 cycle-set representatives, 816480 fully labeled cycle sets, 14 touched root blocks, touched-root rank 10/nullity 4, and 210 admissible singleton triples per representative.

Exact shard results:

[0,66): 13860 374220 295074 19791 {0:19791} maxnorm2=36
[66,132): 13860 374220 295032 19842 {0:19842} maxnorm2=36
[132,198): 13860 374220 294990 19731 {0:19731} maxnorm2=36

Totals are 41580,1122660,885096,59364 with external increment census {0:59364}. Lucas-Lehmer for 2^127-1 passed and (2^127-1)^2 > 36^15, so the repository Hadamard argument certifies the modular rank decisions over Q. This is executed computational evidence, not an unexecuted-verifier claim.

Therefore this support orbit is empty in the D=-1,d_root=1,p=3,m=4,(3,2,2,1) branch, whose states require external increment 5. This closes the last (3,2,2,1) support orbit left by the current-main p=3 certificate chain.

For D=-2,d_root=0,p=5,(s,t)=(3,1), current main reduces every residual state to this same support orbit. Promoting the touched pair to complete gives r_pair <= r_prom+1. The promoted state has complete-root nullity one and satisfies the stronger generalized-weight floor (3,4,6), so the exact p=3 certificate gives r_prom=0. Hence r_pair<=1<5, contradicting the D=-2 saturation requirement. Thus the three-singleton-plus-pair profile is closed.

For the five-singleton profile, current main reduces h=4 to the same support orbit. Promoting the redundant fourth touched singleton to complete gives r_old<=r_prom+1, hence r_old<=1<5. Thus h=4 is impossible. Together with the existing h=3 exclusion, only h=5 remains in D=-2,d_root=0,p=5.

The separate branch D=-1,(d_root,p)=(0,6) remains open.
