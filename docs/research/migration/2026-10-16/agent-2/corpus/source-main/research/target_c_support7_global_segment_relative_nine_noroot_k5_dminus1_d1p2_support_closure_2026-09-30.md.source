# Target C: nine-no-root k=5, D=-1, d_root=1, p=2 support closure

Date: 2026-09-30

Status: exact closure of this arithmetic branch, conditional on current-main lower-layer theorems.

## 1. Weight sharpening

For this branch

    k=5, D=-1, d_root=1, p=2,

the nine-coordinate coefficient space P has rank four. Current main gives the baseline generalized weights

    (d1,d2,d3,d4)(P) >= (3,4,6,7).

Suppose d2(P)=4. Then a two-dimensional subcode is supported on a four-coordinate set J. Since d3(P)>=6, puncturing J has rank loss exactly q=2. The five-no-root shadow therefore has

    D' = -1 + 2*4 - 3*2 = 1,
    rank(P') = 2,
    k' = 3,
    p' <= 2.

After stripping any incomplete root rows in blocks that became untouched, p' is still at most two. The committed coverage-correct five-no-root k=3 theorem proves D>=2 for every k=3 state with p<=3. This contradicts D'=1.

Hence

    d2(P)>=5,

so the usable generalized-weight floor is

    (d1,d2,d3,d4)(P) >= (3,5,6,7).

The lower-layer input is

    research/target_c_support7_global_segment_relative_five_noroot_k3_containment_2026-09-20.md
    blob bdfedd2f4de2225c12ad83ebf2250e46e8a0b4ab.

## 2. Touched-block bound h<=20

Let T be the touched triangle-block family, C the touched actual-complete blocks, E the touched actual-empty blocks, and let h=|T|, e=|E|.

The face-local k=5 condition gives

    rank H(T) - rank H(C) >= 5.

The full triangle-row space has rank at most 15, so rank H(C)<=10. Since d_root=1, every subset of the actual complete-root family has nullity at most one. Thus

    |C| <= rank H(C)+1 <= 11.

The incomplete-root cost is p=2, so at most two touched nonempty incomplete blocks occur. Therefore

    e >= h-13.

Every touched actual-empty block contributes a nonzero local coefficient space. Since d1(P)>=3, each such block is touched by at least three no-root cycles. Every other touched block is touched at least once. The nine no-root four-cycles contribute exactly 36 triangle-block incidences, hence

    36 >= 3e + (h-e)
       = h + 2e
       >= h + 2(h-13)
       = 3h-26.

Therefore

    h<=20.

## 3. Sound support-level relaxation

The finite verifier enumerates all size-nine tetrahedral-support multisets up to S7 with support multiplicity at most three, using the same current-main canonical augmentation and Burnside checks as the adjacent D=-2,d_root=0,p=4 certificate.

For a touched candidate empty block, the repaired local-rank rule is used only in the safe direction:

- if a containing tetrahedral support repeats, local empty rank is forced to two, so d2>=5 requires at least five incidences;
- otherwise the verifier permits rank one from three incidences and also rank two from five incidences.

For two candidate empty local spaces, the verifier imposes only the necessary pairwise consequences of (d1,d2,d3,d4)>=(3,5,6,7). It does not require the local spaces to glue to a common rank-four P.

The selected nonempty incomplete blocks are relaxed away completely except for their count. For a proposed empty set E, put R=T\E. Any actual state has a complete subset C of R with

    |R\C| <= 2,
    |C|-rank H(C) <= 1,
    rank H(T)-rank H(C) >= 5.

Write r_R=rank H(R), r_T=rank H(T). Necessarily

    |C| >= |R|-2,

while nullity at most one and the face-local gap give

    |C| <= rank H(C)+1
         <= min(r_R,r_T-5)+1
         = min(r_R+1,r_T-4).

The verifier therefore keeps a candidate whenever

    max(0,|R|-2) <= min(|R|,r_R+1,r_T-4).

This is a strict relaxation of realizability: every actual state passes these tests, while many nonrealizable support patterns may also pass.

## 4. Exact finite certificate

The exact persisted source compiled and executed for this run is:

- research/k5_d1p2_search.hpp, blob d9ee11e8d11123cefe2567d7e46fdcba1cb2741f
- research/verify_target_c_support7_global_segment_relative_nine_noroot_k5_dminus1_d1p2_support_closure_2026_09_30.cpp, blob cdb04d6428f0eea4ca63ed9eca26e35678fa6411
- imported geometry helper research/k5_d0p4_geom.hpp, blob 407b8626686fa53b4a3dfe6cc2cdf89dced47525

The exact source blobs above were compiled with C++20 and executed before persistence. The verifier independently checks the S7 Burnside orbit counts

    1,1,4,14,61,268,1283,6032,27763,121458,

checks canonical augmentation through size nine, checks Lucas-Lehmer primality for 2^31-1, and uses the same Hadamard exact-rank bound as the adjacent current-main certificate.

Executed census:

    size9_orbits 121458
    raw_size9_extensions 966977
    h_le_20_raw_extensions 239349
    h_le_20_size9_orbits 33920
    supports_with_empty_candidate 534
    relaxed_empty_tests 1070
    relaxed_survivors 0

The program fails closed unless every persisted census constant matches.

Therefore no nine-no-root state exists with

    k=5, D=-1, d_root=1, p=2.

No unexecuted verifier code is used in this closure claim.

## 5. Remaining k=5 frontier

On current main before this commit, the other unintegrated D=-2,d_root=1,p=1 certificate remains on branch target-c-nine-k5-dminus2-d1p1-20260929. After integrating that certificate, the only remaining nine-no-root k=5 arithmetic branch is

    D=-1, d_root=0, p=5.
