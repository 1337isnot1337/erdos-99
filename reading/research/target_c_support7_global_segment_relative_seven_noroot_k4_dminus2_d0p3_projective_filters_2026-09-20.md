> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_seven_noroot_k4_dminus2_d0p3_projective_filters_2026-09-20.md) · source SHA-256 `b70f69af255615ce46f2bef26f31f131fb41b81e7953b8740322c41d02da4daf`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "98e54a8e17a88a2dab66554fdc06897652f29ddb", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_seven_noroot_k4_dminus2_d0p3_projective_filters_2026-09-20.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "815e45fc876f0b7714cc0c01094e06e0c4a961135572623be98ad420e22c5782"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: projective-system filters for the seven-no-root `D=-2,k=4,d=0,p=3` branch

Date: 2026-09-20

Status: exact structural strengthening of the remaining seven-no-root `D=-2,k=4,d=0,p=3` branch. This does not close the branch and does not change the direct 3,874-cell generic-H6 endpoint.

Companion arithmetic checker:

`research/verify_target_c_support7_global_segment_relative_seven_noroot_k4_dminus2_d0p3_projective_filters_2026_09_20.py`

## Starting point

The preceding all-depth deletion theorem gives, for this branch, a rank-three coefficient-constraint space

`P <= Q^7`

with generalized Hamming weights

`d_1(P) >= 3, d_2(P) >= 4, d_3(P) >= 6`.

The same branch has

`D=-2, k=4, d=0, p=3`.

The purpose of this note is to turn the generalized-weight statement into filters that can be applied directly to a `3 x 7` generator matrix and to the local block spaces used by the finite search.

## Generator-column formulation

Choose a full-rank `3 x 7` generator matrix `G` for `P`, with columns

`g_1,...,g_7 in Q^3`.

For a rank-three linear code the generalized weights have the standard projective-system interpretation

`d_r(P) = 7 - max |I|`,

where the maximum is over coordinate sets `I` whose columns span a space of rank at most `3-r`.

Therefore the established bounds imply all three of the following.

1. Any rank-at-most-two linear subspace of `Q^3` contains at most four of the seven columns, counted with multiplicity.
2. Any rank-at-most-one linear subspace contains at most three columns, counted with multiplicity.
3. At most one column is zero.

Equivalently, after projectivizing the nonzero columns, no projective line carries more than four columns and no projective point has multiplicity greater than three; if one zero column is present, it counts toward every linear flat in the unprojectivized formulation.

These are exact restatements of the already proved generalized-weight bounds, not heuristic coding-theory analogies.

## Local block consequence

Let `L_b <= P` be the coefficient-constraint subspace contributed by a touched root block `b`, and let `S_b` be the coordinate support of `L_b`.

If `dim L_b = r`, every column `g_i` with `i notin S_b` is annihilated by every vector in the corresponding `r`-dimensional row subspace. Hence the columns outside `S_b` lie in a linear flat of rank at most `3-r`.

For `r=1`, the complement lies in a rank-at-most-two flat. Since such a flat contains at most four columns,

`|S_b| >= 3`.

For `r=2`, the complement lies in a rank-at-most-one flat. Since such a flat contains at most three columns,

`|S_b| >= 4`.

The support inequalities were already visible from the generalized weights. The additional useful information is the equality structure:

- a rank-one local constraint with support exactly three forces the other four generator columns into one rank-two flat;
- a rank-two local constraint with support exactly four forces the other three generator columns to be proportional, allowing zero columns only in the sense covered by the rank-one-flat count.

This makes the low-support cases recognizable from the column matroid of `P` before any `T`-space reranking.

## Complete-block cap

Let `c` be the number of complete root blocks. Since `d=0`, their complete-block relation rows are independent and span a `c`-dimensional subspace of the 15-dimensional ground-root space `T`.

The branch contains

`7 + p + 3c = 10 + 3c`

selected rows. The condition `D=-2` therefore forces

`delta = (|A|+2)/3 = c+4`.

Thus the complete-block relations together with the four external relation lifts have rank exactly `c+4` inside `T`. Since `dim T=15`,

`c+4 <= 15`,

so every hypothetical state in this branch satisfies

`c <= 11`.

This is an immediate exact rejection rule for the finite search. A canonical candidate with twelve or more mandatory complete blocks cannot extend to a counterexample, even if its coefficient space satisfies every deletion-rank condition.

The same equality also shows that the four-dimensional external relation space injects modulo the complete-block span. Consequently every deletion shadow inherits independence of the surviving external relation subspace; this is consistent with the sharp six- and five-row shadows and introduces no extra assumption.

## Search use

A finite verifier for the remaining branch should now reject a rank-three `P` as soon as any of the following occurs:

- five generator columns lie in a rank-at-most-two flat;
- four generator columns are proportional;
- two generator columns are zero;
- a local rank-one constraint has support below three;
- a local rank-two constraint has support below four;
- a support-three rank-one local constraint does not have the complementary four columns in one rank-two flat;
- a support-four rank-two local constraint does not have the complementary three columns in one rank-one flat;
- the canonical mandatory complete-block count exceeds eleven.

The flat tests are equivalent to the generalized-weight constraints but are cheaper to evaluate from a generator matrix and expose the equality cases needed for a branch-specific classifier.

## Remaining bottleneck

The branch remains

`D=-2, k=4, d=0, p=3`.

The next useful computation is still the exact five-row `D=2,k=2,d=0,p=3` shadow classification, followed by extension to seven rows. The new projective filters should be imposed during rank-three coefficient-space generation rather than after a complete candidate has been built. In particular, rank-two local spaces of support four can be indexed by the proportionality class of the three complementary generator columns, and rank-one support-three spaces by the rank-two flat containing the four complementary columns.

The direct C-II endpoint remains unchanged:

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

No theorem-state authority file is changed by this note.
