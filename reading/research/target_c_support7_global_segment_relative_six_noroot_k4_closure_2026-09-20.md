> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_six_noroot_k4_closure_2026-09-20.md) · source SHA-256 `cb64606a8d3be2ae2021e4c1203d03553e52b0d326b4428f7467b22c2c884021`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e657af99b1a26022523a0831395660c34aa771e0", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_six_noroot_k4_closure_2026-09-20.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "26a170953c8402055777de12165e84b1d8f4f33fdd3798591fd375d3643aa422"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: six-no-root `k=4` closure

Date: 2026-09-20

Status: exact closure of both synchronized `k=4` six-no-root counterexample cases. Together with the committed `k=5` and `k=6` closures, this closes the full six-no-root factor-three rank-density layer. It does not reduce the 3,874-cell generic-H6 endpoint and does not close C-II.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_six_noroot_k4_2026_09_20.py`

## Starting point

Let `A` be a block-reduced family with exactly six no-root four-cycles and write

`D(A)=|A|-3 delta(A)`.

Deletion-shadow synchronization and the already closed `k=5,6` branches leave only

```text
D(A)   k(A)   p(A)   deletion k   deletion p
 -2      4      4         3            4
 -1      4      5         3            5
```

For `k=4` on six external rows, the global coefficient-constraint space `P` has rank two. Every coordinate deletion `P_i` has rank two because every deletion shadow has five no-root rows and `k=3`.

The support-overlap corollary from deletion synchronization also applies:

> every nonempty incomplete root-0 block in a hypothetical six-no-root counterexample is touched by at least two of the six no-root cycles.

## Lift of the repaired five-row `k=3` theorem

Fix the six no-root rows and an obtainable rank-two space `P`. Define its virtual canonical state as in the repaired five-no-root `k=3` theorem:

- a touched root-0 block `b` is empty when its empty-state coefficient constraint `E_b` is contained in `P`;
- otherwise `b` is complete.

Let `C` be the canonical complete-block set, let `H(C)` be the span of its complete-block `T` relation rows, and put

`d=|C|-rank H(C)`.

For coordinate deletion `i`, let `P_i` be the projected rank-two plane and `C_i` the five-row virtual canonical complete set. If a block is six-row canonical-empty, then `E_b subset P`; after projection its empty constraint is contained in `P_i`, so it remains canonical-empty. Therefore

`C_i subset C`.

The repaired five-no-root `k=3` theorem gives

`|C_i|-rank H(C_i) >= 1`.

Adding rows cannot reduce row nullity, hence

`d >= 1`.

The external-containment part of the five-row theorem also lifts. Let

`N=null(P)`

and

`N_i={alpha in N: alpha_i=0}`.

Because `rank(P_i)=2`, the coordinate functional `alpha -> alpha_i` is nonzero on `N`, so each `N_i` is a hyperplane in the four-dimensional space `N`. The ambient coordinate functionals span `N*`, so not all of these hyperplanes are equal. Hence two distinct `N_i,N_j` satisfy

`N=N_i+N_j`.

For `alpha in N_i`, deletion gives a vector in `null(P_i)`, whose five-row external relation lies in `H(C_i)` by the repaired theorem. Lifting it back to six coordinates does not add demand on blocks in `C\C_i`, because their projected empty constraint is contained in `P_i`. Thus its six-row relation lies in `H(C_i) subset H(C)`. Since the `N_i` span `N`, every six-row external relation lies in `H(C)`.

The same virtual-canonical accounting therefore gives, for every compatible actual state,

`D(A) >= 6 + p + 3d - 3q`,

where `q` is the number of canonical-complete blocks changed to incomplete states. A canonical-complete block cannot become empty, so

`q<=p`.

## Reduction to one finite obstruction

For `d>=2`, the crude `q<=p` bound gives

- at `p=4`, `D(A)>=4`;
- at `p=5`, `D(A)>=2`.

For `d=1,p=4`, it still gives

`D(A)>=1`.

Thus the only possibly dangerous case is

`d=1, p=5, q=5`.

Since the total incomplete-row count is five and five canonical-complete blocks are changed, every one of those five blocks must be replaced by a singleton. There can be no additional nonempty incomplete block. By support-overlap, all five singleton blocks must also be touched by at least two no-root cycles.

So a counterexample requires a six-row `d=1` virtual canonical state with at least five canonical-complete blocks that simultaneously

1. admit a singleton whose local coefficient constraint is contained in `P`; and
2. are touched by at least two of the six no-root cycles.

## Why only the 86 five-row `d=1` parents matter

If the six-row state has `d=1`, then for every deletion

`1 <= d_i <= d = 1`,

so every five-row deletion shadow has `d_i=1`.

The coverage-repaired five-no-root `k=3` census contains exactly

`86`

`d=1` virtual canonical states. All 86 are in the empty-generated class; none of the planes requiring singleton generators has `d=1`.

Choose any deletion of a hypothetical six-row `d=1` candidate and relabel its five no-root cycles by `S_7` to the corresponding canonical five-row representative. The deleted no-root cycle then becomes one of the remaining 100 no-root cycles. Therefore every six-row `d=1` orbit is represented among the extensions of those 86 parent states.

The verifier scans all

`86 * 100 = 8,600`

parent extensions. This is an orbit cover, not a claim that all 8,600 extensions or the later candidate planes are orbit-distinct. Duplicates are harmless for the exclusion.

## Exact rank-two coefficient-space enumeration

For a fixed five-row parent plane `P5` and one added sixth no-root cycle, the verifier enumerates every realizable rank-two six-row plane `P6` projecting to `P5`.

At one touched block:

- the empty state contributes a coefficient-constraint space of rank at most two;
- a singleton contributes rank at most one;
- a pair or complete state contributes no coefficient constraint.

Any rank-two global `P6` therefore has a basis supplied either by one rank-two local constraint space, or by two independent rank-one local constraint spaces from distinct blocks. The verifier enumerates exactly those basis possibilities, forms the exact rational row space, and keeps planes whose sixth-coordinate projection is `P5`.

As an implementation cross-check, the first 100 parent extensions are also enumerated by the full repaired block-state dynamic program. The candidate sets agree exactly in all 100 cases.

Deletion synchronization then requires all six coordinate projections of `P6` to retain rank two.

Across the complete extension cover the counts are

```text
parent extensions                         8,600
rank-two P6 candidates before sync       16,781
all six projections rank two              4,684
```

Their complete-block deficiency census is

```text
d=1       31
d=2    1,877
d=3    2,171
d=4      595
d=5       10
```

Only the 31 `d=1` candidates require the singleton-capacity test. As an independent check of the deletion-lift argument, the verifier constructs all four six-row external relation lifts for every one of these 31 candidates and verifies directly that they lie in `H(C)`. All 31 pass; the maximum squared norm of a checked external row is 36.

## Singleton-capacity obstruction

For each of those 31 candidates, count canonical-complete blocks that both admit a compatible singleton and have no-root support multiplicity at least two. The exact census is

```text
eligible singleton blocks   cover candidates
0                                  1
2                                  6
3                                 24
```

Thus the maximum possible number is

`3`.

The only dangerous case requires five such singleton blocks. Therefore it does not occur.

This eliminates both synchronized `k=4` cases.

## Exactness

All coefficient-space construction, projection, row-space union, and containment operations use exact rational arithmetic inherited from the repaired five-row verifier.

Complete-block ranks use the prime

`MOD=2^127-1`.

The imported verifier checks primality by Lucas-Lehmer. The complete-block relation rows have squared Euclidean norm at most 12. The directly checked six-row external relation rows in the dangerous `d=1` states have squared norm at most 36. The verifier checks

`MOD^2 > 36^15`.

Hadamard's determinant bound therefore prevents a nonzero rational minor of order at most 15 from vanishing modulo `MOD`, so the modular rank and containment decisions used here equal the rational decisions.

## Consequence

The six-no-root density layer is now closed:

> every four-cycle family with at most six no-root four-cycles satisfies `3 delta(A) <= |A|`.

In particular, the metric-basis route can now move to seven no-root cycles. Under the established 44-cycle sufficient-family reduction, where sufficiency would require `delta=15`, a sufficient 44-cycle family must contain at least seven no-root cycles.

The direct C-II endpoint remains

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

The state-specific forced-segment-order elimination over those generic-H6 cells remains the direct endpoint computation. No theorem-state authority file is changed here.
