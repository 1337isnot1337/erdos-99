> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_five_noroot_k3_p3_reduction_2026-09-20.md) · source SHA-256 `5f7f5cb9e24b23f69c5bf6e54f459e7f009fa94f763d531e4a532eed208c2b00`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "26f06580d2701df62a1f36f7fd17e2fe0351997b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_five_noroot_k3_p3_reduction_2026-09-20.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c02b081a1df8bfcf51607c1b29d7e4f66cd4dff040d986edff4a9127bba675c2"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: five-no-root k=3, p=3 structural reduction

Date: 2026-09-20

Status: rigorous reduction of the remaining five-no-root `k=3,p=3` rank-density branch. This note does not claim that the branch is closed. It narrows the exact finite search that remains. It does not reduce the 3,874-state generic-H6 endpoint and does not change theorem-state authority files.

## Setup

Keep the notation of the `p=0,1,2` audits. For a fixed rank-two coefficient-constraint space `P`, let the canonical `p=0` state have complete-block set `C`. Write

- `c = |C|`,
- `r = rank_T(C)`,
- `d = c-r`.

A canonical `p=3` realization has exactly one of two local forms:

1. one two-row incomplete block and one singleton block (`2+1`), or
2. three singleton blocks (`1+1+1`).

Let `R subset C` be the complete blocks replaced by incomplete states, put `q=|R|`, and let

`C' = C \ R`, `c' = |C'| = c-q`.

The five no-root rows have a three-dimensional coefficient nullspace because `k=3`. Therefore

`delta(A) <= rank_T(C') + 3`.

The selected-row count is

`|A| = 5 + 3c' + 3 = 8 + 3c'`.

## A counterexample forces C' to be independent

If `C'` is dependent, then

`rank_T(C') <= c'-1`,

so

`delta(A) <= c'+2`

and hence

`|A|-3 delta(A) >= 8+3c' - 3(c'+2) = 2`.

Thus every counterexample to `3 delta(A) <= |A|` must have `C'` independent.

Consequently at least `d` complete blocks must be replaced, so

`d <= q <= 3`.

For `c<=13`, the exact `p=0` deficiency census therefore removes the entire `d=4` class. The only base states that can contribute are

```text
d=1       86
d=2   13,349
d=3  219,112
--------------
      232,547
```

canonical states.

## High-c slice: only c=14,15 can matter

Independently of complete-block rank, `delta(A) <= dim(T)=15`. Therefore if `c' >= 13`,

`|A|-3 delta(A) >= 8 + 3*13 - 45 = 2`.

A counterexample must satisfy `c'<=12`. Since `q<=3`, this immediately gives

`c <= 15`.

Hence every canonical `p=0` state with `c>=16` is irrelevant to the `p=3` branch. The exact `p=0` census removes

```text
c=16   585
c=17    57
```

states without any further rank computation.

### The c=14 slice

The exact supplement for the previously omitted `p=2,c=14` slice already computed the complete-block ranks of all 10,250 canonical `c=14` states:

```text
rank_T(C)=10   1,224 states
rank_T(C)=11   9,026 states
```

If `q<=2`, then `c'>=12` while `rank_T(C')<=11`, so `C'` is dependent and the state is safe by the preceding argument.

If `q=3` and `rank_T(C)=10`, then `c'=11` but `rank_T(C')<=10`, so again `C'` is dependent.

Therefore the only `c=14` base states that can contribute are the 9,026 rank-11 states, and they can contribute only with

- `q=3`,
- three singleton replacements,
- all three singleton blocks replacing complete blocks.

This is exactly the `d=3` deletion-minimal form.

### The c=15 slice

There are 1,802 canonical `c=15` states. Since a counterexample needs `c'<=12`, all three complete-block replacements are mandatory:

`q=3`, `c'=12`.

Thus the `2+1` local type is impossible here because it occupies only two incomplete blocks and can replace at most two complete blocks. The only possible form is again three singleton replacements, all on complete blocks.

No complete-rank census for the 1,802 `c=15` states has yet been committed. A state is automatically safe if `rank_T(C)<=11`; only rank at least 12 could leave an independent 12-row `C'` after three deletions.

Combining the certified low- and high-`c` information, at most

`232,547 + 9,026 + 1,802 = 243,375`

canonical base states can reach the deletion-minimal `p=3` search before local singleton compatibility and deletion-rank pruning. This is an upper bound on base states, not a count of surviving `p=3` states.

## Stronger type restrictions inherited from p=1 and p=2

The preceding `p=1` and `p=2` audits eliminate several deletion patterns before any new full relation rank is computed.

### d=3

Independence of `C'` requires at least three complete-block deletions. Since `q<=3`, necessarily

`q=3`.

The `2+1` local type has only two incomplete blocks, so it cannot occur. Every surviving `d=3` state is therefore three singleton replacements on three complete blocks.

This applies in particular to the 9,026 `c=14, rank=11` states.

### d=2

At least two complete blocks must be replaced.

For the `2+1` type, both incomplete blocks must replace complete blocks.

For the three-singleton type, either two or three singleton blocks replace complete blocks. In the `q=2` case, the two complete-block singleton replacements already form a `p=2` state with the same remaining complete set `C'`. The exact `p=2` audit found exactly 3,534 admissible two-singleton states with independent `C'`, all from `d=2`. Therefore every `d=2,q=2` three-singleton candidate must extend one of those 3,534 certified `p=2` states by a compatible singleton in a canonical-empty block.

### d=1

The `p=1` audit proved that every admissible single complete-block singleton replacement leaves the remaining complete set dependent. Therefore a three-singleton `d=1` state cannot have `q=1`.

The `p=2` audit found no `d=1` state in which two complete-block singleton replacements leave the remaining complete set independent. Therefore a three-singleton `d=1` state cannot have `q=2` either.

Hence every `d=1` three-singleton candidate must have

`q=3`,

with all three singleton blocks replacing complete blocks.

For the `2+1` type with `d=1` and `q=1`, the sole complete-block replacement cannot be the singleton: the `p=1` result would make `C'` dependent. Thus the only possible `q=1` form has the two-row pair replacing a complete block and the singleton lying in a canonical-empty block. The `p=2` audit found exactly 346 one-block pair deletions from `d=1` bases for which the remaining complete set is independent, so every such `p=3,q=1` candidate must extend one of those 346 deletion states.

The `d=1,q=2` `2+1` form and the `d=1,q=3` three-singleton form still require a new exact scan.

## Resulting p=3 search plan

A complete verifier for the remaining `k=3,p=3` branch does not need to enumerate the unrestricted local-state product. It is enough to enumerate the following deletion-minimal classes and exactify only states whose post-replacement complete set is independent:

1. `d=1`, `2+1` with `q=1` extending one of the 346 certified independent pair deletions;
2. `d=1`, `2+1` with `q=2`;
3. `d=1`, three singletons with `q=3`;
4. `d=2`, `2+1` with `q=2`;
5. `d=2`, three singletons with `q=2`, extending one of the 3,534 certified independent `p=2` two-singleton states;
6. `d=2`, three singletons with `q=3`;
7. `d=3`, three singletons with `q=3`;
8. `c=14, rank=11`, which is already a subset of the same `d=3,q=3` form but was outside the original `c<=13` deficiency census;
9. `c=15`, three singletons with `q=3`, with an initial complete-rank filter `rank_T(C)>=12`.

For every enumerated state, dependence of `C'` certifies defect at least 2. Only independent `C'` states need the three external relation rows constructed and reranked. A negative state can occur only if those three rows raise the rank from `c'` all the way to `c'+3`; any increase of at most two gives

`|A|-3 delta(A) >= 2`.

This is the exact next finite target. After `k=3,p=3`, the five-no-root density problem remains only in `k=4,p<=6`.

For C-II itself, the explicit generic-H6 endpoint remains

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

The state-specific forced-segment-order scan remains the direct endpoint computation. No theorem-state authority file is changed by this reduction.
