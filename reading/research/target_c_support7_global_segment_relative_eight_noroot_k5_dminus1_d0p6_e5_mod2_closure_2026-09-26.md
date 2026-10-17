> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d0p6_e5_mod2_closure_2026-09-26.md) · source SHA-256 `eaa5cb9544d1f6d89bc96dc788a06ec31e8ebab771cbd90060d4b0aac26486bc`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "0b2a4be6b2731bf05c9f3feb5948dcbe4cb387cc", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d0p6_e5_mod2_closure_2026-09-26.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "af92559ce9b9c8547c7d95342fb27958236bc11d58b0a0c2bc731e13935356b5"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close p=6, e=5 by empty-space rank over F2

Date: 2026-09-26

This note closes the e=5 slice of the final eight-no-root k=5, D=-1, d_root=0, p=6 branch.

The committed structural reduction gives rank(P)=3, generalized weights (d1,d2,d3)>=(2,4,5), exactly six touched singleton replacements, no selected pair, and e touched actual-empty blocks. The face-local span bound gives nu(T)<=e+1, hence nu(T)<=6 for e=5.

For a touched actual-empty block b, let E_b<=P be its local constraint space and I_b the set of external cycle coordinates touching b. If some containing tetrahedral support has multiplicity at least two, then E_b has rank two. Therefore d2(P)>=4 forces |I_b|>=4. Otherwise E_b is nonzero and d1(P)>=2 forces |I_b|>=2. If a and b are both forced rank-two empty blocks, then the two planes E_a,E_b in the three-space P intersect in a nonzero line. Every vector in that intersection is supported on I_a intersect I_b, so d1(P)>=2 forces |I_a intersect I_b|>=2.

An exact S7 support census with nu(T)<=6 gives:
- m=3: 10 support orbits, all nullity 3;
- m=4: 38 support orbits, nullity distribution {4:35,5:3};
- m=5: 135 support orbits, distribution {4:1,5:107,6:27};
- m=6: 302 support orbits, distribution {5:2,6:300};
- m=7: 10 support orbits, all nullity 6;
- m=8: no support orbit with nullity at most 6.

After quotienting the eight-cycle multiplicities by each support stabilizer, there are 8077 support/multiplicity S7-orbits:
- m=3: 17;
- m=4: 399;
- m=5: 2655;
- m=6: 4967;
- m=7: 39.

The phase-independent empty-block conditions above reduce these 8077 orbits to 1058 assignments and 11775 candidate empty quintuples. Only four multiplicity profiles survive:
- m=5, (3,2,1,1,1): 24 assignments, 94 quintuples;
- m=6, (3,1,1,1,1,1): 874 assignments, 7370 quintuples;
- m=6, (2,2,1,1,1,1): 121 assignments, 414 quintuples;
- m=7, (2,1,1,1,1,1,1): 39 assignments, 3897 quintuples.

All phase choices across those retained assignments give exactly 387828 phase configurations and 10623069 phase/empty-quintuple pairs.

For an empty quintuple A, form

U(A)=sum_{b in A} E_b <= P.

The ten integer rows spanning U(A) were reduced modulo 2 for every retained phase/quintuple pair. Every one of the 10623069 cases has rank_F2 U(A)>3. Since a nonzero minor modulo 2 is a nonzero integer minor, rank_Q U(A)>=rank_F2 U(A)>3. This contradicts U(A)<=P and rank(P)=3.

Therefore the entire e=5 slice is empty. No singleton-direction enumeration, generalized-weight exactification, or external relation-rank computation is needed after the mod-2 obstruction.

The companion verifier enumerates the support/multiplicity quotient, hard-asserts all counts above, and supports bounded assignment-range shards for the phase scan. The complete phase/quintuple scan was executed in bounded shards with no rank<=3 residual case.

Together with the e=2 and e=3 closures on main and the pushed e=4 closure immediately preceding this commit chain, the final p=6 branch is reduced to e>=6. This does not close Target C or Erdos Problem #99.

END
