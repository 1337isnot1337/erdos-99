> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_seven_noroot_k3_dminus1_depth2_2026-09-20.md) · source SHA-256 `15db8538fa47a8fbeeeaafceebbf4661b6f6c05a3bd5ec6e823633a53a5a6b12`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "62fe36d6ae122318e5dc783713a866384f4e6981", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_seven_noroot_k3_dminus1_depth2_2026-09-20.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1b5800eb62af6a2b6f4479b5b0810cd6d47e6fb0d070ac7678df0912a27ea0b7"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: five-no-root `k=2,p=1` slack and seven-no-root `D=-1,k=3` depth-two synchronization

Date: 2026-09-20

Status: exact five-no-root slack theorem, with a structural consequence for the remaining seven-no-root `D=-1,k=3` branch. This does not close the whole seven-no-root layer and does not change the direct 3,874-cell generic-H6 endpoint.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_five_noroot_k2_p1_slack_2026_09_20.py`

## Five-no-root theorem

Let `A` have exactly five no-root four-cycles and suppose its quotient-nullity parameter is

`k=2`

and the selected root rows in incomplete root blocks satisfy

`p=1`.

Then

> `D(A)=|A|-3 delta(A) >= 3`.

In particular there is no sharp `D=0` five-no-root state with `k=2,p=1`.

This strengthens the previously committed `k=2,p=0` result in exactly the slice needed by the next seven-no-root deletion argument.

## Canonical reduction

For five no-root cycles and `k=2`, the global coefficient-constraint space `P` has rank three in the five external coefficients.

Because `p=1`, exactly one incomplete touched root block is a singleton. Every other incomplete touched block is empty. Fix `P` and fix the singleton block and singleton state. The canonical least-row realization is obtained by

- retaining the fixed singleton;
- leaving every other touched block empty when its empty-block coefficient constraint lies in `P`;
- completing every other touched block.

Any other realization with the same `P` and singleton choice is obtained by completing some of those canonical-empty blocks. One such completion adds three selected rows and can increase the relative `T`-relation rank by at most one. Therefore it cannot decrease

`D=|A|-3 delta(A)`.

It is enough to prove the bound on canonical realizations.

## Deficiency bound

Let `C` be the canonical complete-block set, let `c=|C|`, and let

`d = c - rank H(C)`,

where `H(C)` is the complete-block `T`-relation span.

Since `rank(P)=3`, `null(P)` has dimension two. Thus the complete relations together with the two possible external relation lifts have total rank at most

`(c-d)+2`.

The canonical family has

`5 + 1 + 3c = 6+3c`

selected rows. Hence

`D >= 6+3c - 3((c-d)+2) = 3d`.

Every state with `d>=1` is therefore already safe with `D>=3`. Only `d=0` requires exact reranking.

## Exhaustive coefficient-space census

The verifier scans the exact 20,451 `S_7` orbit representatives of five-subsets of the 105 no-root four-cycles and enumerates every realizable rank-three coefficient space with one singleton block.

The full census is

```text
coefficient spaces                         503,112
canonical p=1 states                     8,590,316

d=0                                          3,492
d=1                                      2,325,470
d=2                                      6,239,198
d=3                                         22,040
d=4                                            108
d=5                                              8
```

Thus only 3,492 canonical states require the external `T` relations to be formed.

For those 3,492 states, exact reranking gives

```text
complete blocks c   complete rank   total relation rank   states
3                    3               3                     840
5                    5               5                     698
6                    6               6                   1,616
7                    7               7                      90
8                    8               8                     248
```

In every `d=0` state the two external lifts lie in the complete-block relation span. Therefore

`delta=c`

and every one of the 3,492 residual states has

`D = 6+3c-3c = 6`.

Combining this with the `d>=1` bound proves the theorem `D>=3` for the entire five-no-root `k=2,p=1` branch.

## Exactness of the finite computation

The coefficient-space dynamic program uses the prime

`2^31-1`.

The repository's local quotient coordinates have entries in `{-1,0,1}`, and the singleton constraint rows are `2x2` determinants against the local directions `(1,0)`, `(0,1)`, `(1,-1)`. Hence every raw length-five coefficient row has squared Euclidean norm at most 20.

Any rank decision on these length-five coefficient matrices is witnessed by a square minor of order at most five. Hadamard gives

`det^2 <= 20^5`.

The verifier checks primality of `2^31-1` by Lucas-Lehmer and checks

`(2^31-1)^2 > 20^5`.

Therefore reduction modulo `2^31-1` cannot destroy any nonzero rational minor used by the coefficient-space enumeration. The coefficient-space ranks, spans, and containment tests agree with those over `Q`.

Complete-block and residual `T`-space ranks use the existing prime

`2^127-1`.

The maximum squared norm of any residual relation row in the 3,492 exact states is 44. The verifier checks the existing Lucas-Lehmer condition and

`(2^127-1)^2 > 44^15`.

Thus the final `T`-rank decisions also agree with rational rank.

## Consequence for seven no-root cycles

Now let `B` be a hypothetical seven-no-root counterexample in the remaining branch

`D(B)=-1, k(B)=3, d=0, p=1`.

The preceding seven-no-root deletion theorem already proves that deleting any one no-root row leaves quotient constraint rank four and gives a six-no-root shadow with

`D=1, k=2`.

Delete a second no-root row. Let `s` be the quotient-rank drop on this second deletion. The established defect calculation gives exactly

```text
s=0: D=3, k=1
s=1: D=0, k=2
```

The root rows do not change, so both pair-deletion shadows retain `d=0,p=1`.

The `s=1` alternative would therefore be a five-no-root state with

`D=0, k=2, p=1`,

which the theorem above rules out. Consequently

> every two-row deletion in the seven-no-root `D=-1,k=3,d=0,p=1` branch preserves quotient constraint rank four.

Equivalently, if `P_7` is the rank-four coefficient-constraint space of a hypothetical counterexample, then projection after deleting any one or any two external coordinates is injective. Hence

`minimum support(P_7) >= 3`.

Every five-row pair-deletion shadow is forced into the single synchronized boundary type

`D=3, k=1, d=0, p=1`.

This removes all support-two coefficient constraints from the `D=-1,k=3` branch. In particular, every nonzero local coefficient constraint in such a hypothetical seven-row state must involve at least three of the seven no-root cycles.

## Remaining bottleneck

The `D=-1,k=3,d=0,p=1` branch is not closed by this note. Its next finite target is now sharply specified: classify the five-no-root

`D=3, k=1, d=0, p=1`

pair-deletion shadows and extend only those states through the synchronized six- and seven-row projection conditions. This is the direct analogue of the deletion-shadow computation that closed the `D=-2,k=3,d=0,p=0` branch.

The other smallest remaining seven-no-root cases are still

```text
D=-2, k=4: (d,p) = (0,3) or (1,0).
```

The direct C-II endpoint is unchanged:

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

No theorem-state authority file is changed by this result.
