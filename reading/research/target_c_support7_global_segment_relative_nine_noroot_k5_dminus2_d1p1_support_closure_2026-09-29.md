> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_nine_noroot_k5_dminus2_d1p1_support_closure_2026-09-29.md) · source SHA-256 `f2840478ce5529146300bee9a3968826748c7c0b2d0aa333e1d2e116989c8a08`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "5121de1ef44504baf78f3696b1d055ba2fbd301c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_nine_noroot_k5_dminus2_d1p1_support_closure_2026-09-29.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "20d1e4a0607a41e175434363ef70f47e27dcc8bfeea10f632bcb9f13aa49e8e1"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close nine-no-root k=5, D=-2, d_root=1, p=1

Date: 2026-09-29

Status: proof-level weight/touch reduction followed by an executed exact support-level relaxation with zero survivors. This closes one of the four arithmetic branches in the nine-no-root k=5 layer. It does not close the other three k=5 branches, the full nine-no-root layer, Target C-II, or Erdos Problem #99.

Companion verifier:

research/verify_target_c_support7_global_segment_relative_nine_noroot_k5_dminus2_d1p1_support_closure_2026_09_29.cpp

Persisted verifier blob:

bac9114a335c586f5e2bdc010aa6f63ea8248607

That exact source was compiled and executed before persistence and produced the fail-closed census recorded below.

## 1. Arithmetic branch

For a hypothetical nine-no-root counterexample, current main proves

D(B) in {-2,-1}

and

D(B)=9+p+3 d_root-3k.

At k=5 this becomes

D(B)=p+3 d_root-6.

Hence the entire k=5 arithmetic frontier consists of exactly four branches:

- D=-2, d_root=0, p=4;
- D=-2, d_root=1, p=1;
- D=-1, d_root=0, p=5;
- D=-1, d_root=1, p=2.

This note treats D=-2, d_root=1, p=1.

Let P <= Q^9 be the external coefficient-constraint space. Since rank(P)=9-k,

rank(P)=4.

For every nonempty coordinate deletion S of size s with puncture rank loss q_S, current main gives

D(B\S)=D(B)+2s-3q_S >= 0.

The standard generalized-weight bound initially gives

(d1,d2,d3,d4)(P) >= (3,4,6,7).

## 2. Four-coordinate punctures preserve rank

Fix any four-coordinate set S and let q be the puncture rank loss. Because d3(P)>=6, a three-dimensional subcode cannot be supported on S, so q<=2.

If q=1, the five-no-root shadow has

rank(P_S)=3,
k_S=2,
D(B\S)=-2+8-3=3.

Deleting external rows cannot increase the selected incomplete-root cost, so p_S<=1. The committed exact five-no-root k=2 slack theorem proves

D >= 8-2p

for p<=2. Hence this shadow must have D>=6, contradicting D=3.

If q=2, the five-no-root shadow has

rank(P_S)=2,
k_S=3,
D(B\S)=-2+8-6=0.

Again p_S<=1. The committed coverage-correct five-no-root k=3 containment theorem proves D>=2 for every k=3 state with p<=3. This contradicts D=0.

Thus q=0 for every four-coordinate set S. Equivalently, no nonzero word of P is supported on at most four coordinates, so

d1(P)>=5.

Generalized Hamming weights are strictly increasing. Therefore

(d1,d2,d3,d4)(P) >= (5,6,7,8).

The lower-layer inputs are:

- research/verify_target_c_support7_global_segment_relative_five_noroot_k2_slack_2026_09_20.py, blob 719870f8fa647ee5e7a50a440dbd9f41fe412d14;
- research/target_c_support7_global_segment_relative_five_noroot_k3_containment_2026-09-20.md, blob bdfedd2f4de2225c12ad83ebf2250e46e8a0b4ab.

## 3. Touched-block bound h<=16

Let T be the touched triangle-block family, C the touched actual-complete blocks, E the touched actual-empty blocks, and h=|T|, e=|E|.

The face-local identity for k=5 gives

rank H(T)-rank H(C) >= 5.

The full triangle-row space on seven labels has rank 15, hence

rank H(C) <= 10.

The branch has d_root=1. The full actual complete-root family has row nullity one, so every subset, including C, has nullity at most one. Therefore

|C|-rank H(C) <= 1

and

|C| <= 11.

The incomplete-root cost is p=1, so at most one selected singleton block can be touched. Consequently

e >= h-12.

Every actual-empty touched block contributes a nonzero local coefficient space contained in P. Its coordinate support is contained in the set of external cycles touching that block. Since d1(P)>=5, every actual-empty block is touched by at least five of the nine no-root cycles.

Every other touched block is touched at least once. Nine no-root four-cycles contribute exactly 36 triangle-block incidences. Thus

36 >= 5e + (h-e)
   = h+4e
   >= h+4(h-12)
   = 5h-48.

Therefore

h<=16.

## 4. Sound support-level relaxation

The finite verifier enumerates support multisets only. It deliberately forgets orientation information whenever doing so enlarges the candidate set.

The audited current-main local-rank repair shows that the old converse "no repeated containing tetrahedral support implies local empty rank one" is false. The verifier does not use it.

For a touched candidate empty block:

- if a containing tetrahedral support repeats, local empty rank is forced to two; d2>=6 then requires at least six incidences;
- if no containing support repeats, the verifier permits rank one when incidence is at least five and also permits rank two when incidence is at least six.

Thus every orientation-realizable local empty space is included.

For two local spaces with occurrence sets I,J, the verifier imposes only necessary consequences of (d1,d2,d3,d4)>=(5,6,7,8), split by the possible intersection dimension:

- line-line: |I intersect J|>=5 or |I union J|>=6;
- line-plane: |I intersect J|>=5 or |I union J|>=7;
- plane-plane: |I intersect J|>=6, or both |I intersect J|>=5 and |I union J|>=7, or |I union J|>=8.

The selected singleton is also relaxed safely. Its local coefficient line may be zero; if nonzero, the verifier treats it as an arbitrary line supported inside its occurrence set, subject only to the necessary weight tests.

Coefficient generation is relaxed to necessary conditions only:

- nominal generator dimension at least four;
- occurrence-set union of the generators has size at least eight, from d4(P)>=8.

It does not require the relaxed local spaces to glue to an actual common rank-four P.

For the touched complete set C the verifier keeps only the necessary structural conditions

|C|-rank H(C) <= 1

and

rank H(T)-rank H(C) >= 5.

Therefore a zero-survivor result for this relaxation excludes every actual oriented state.

The local-rank safety input is

research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d1p0_local_rank_repair_2026-09-27.md

blob 616d89593d3e475a5ce8105ed2f498c09b7cacd7.

## 5. Exact finite certificate

The verifier independently computes the Burnside orbit counts for tetrahedral-support multisets of sizes zero through nine, with multiplicity at most three:

1, 1, 4, 14, 61, 268, 1283, 6032, 27763, 121458.

It independently canonical-augments through size eight and verifies those counts, then obtains every size-nine orbit by one support extension and verifies the final count 121458.

The proved h<=16 bound reduces the 121458 support-multiset orbits to exactly

2634

orbits. These arise from 16189 raw size-nine extensions before canonical deduplication.

The exact executed census is:

size9_orbits 121458
h_le_16_raw_extensions 16189
h_le_16_size9_orbits 2634
relaxed_profile_tests 2178
support_level_survivors 0

The verifier fails closed unless all five counts match those persisted constants.

Triangle-row ranks are computed modulo 2^31-1. The verifier checks this Mersenne number is prime by Lucas-Lehmer. Every triangle row has squared Euclidean norm three and relevant rank is at most fifteen, while

(2^31-1)^2 > 3^15.

Hadamard's bound therefore proves that every modular triangle-row rank used by the verifier equals its rational rank.

The exact persisted verifier blob bac9114a335c586f5e2bdc010aa6f63ea8248607 matches the Git blob of the exact local source that produced the census above.

Hence the nine-no-root branch

k=5, D=-2, d_root=1, p=1

has no realizable state.

## 6. Remaining k=5 frontier

Exactly three k=5 arithmetic branches remain:

- D=-2, d_root=0, p=4;
- D=-1, d_root=0, p=5;
- D=-1, d_root=1, p=2.

The next target should derive analogous puncture-weight sharpening for these branches before attempting orientation-level searches.

## 7. Salvage provenance and current scope

Salvaged on 2026-10-04 from source branch
`target-c-integrate-k5-dminus2-d1p1-20260929-run11` at tip
`7c1baa807d389355072e62e153df50e6d3ad1dcb`; the same lineage also appears on
`target-c-nine-k5-dminus2-d1p1-20260929` at tip
`9b646a864af16353319057c9fe904790615d0307`. The exact companion verifier is retained
at the path above. Its source was recompiled with `g++ -std=c++20 -O2 -Wall -Wextra
-pedantic` and rerun during salvage; it reproduced all persisted census values and
reported zero support-level survivors.

This is an exact finite support-level closure for the single arithmetic profile
`k=5, D=-2, d_root=1, p=1`, conditional on the cited Target C support-7 reductions. It
is not a proof of the remaining nine-no-root profiles, Target C-II, or Level I, and it
does not change theorem state. Lifecycle on integration is **unreviewed** pending
mathematical review.
