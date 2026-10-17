> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_seven_noroot_k5_dminus1_d0p7_all_pair_sync_2026-09-21.md) · source SHA-256 `f60530b476a7d80db9068eb7dbbdd3e2d535d4b282783baf4bf1553787b47fb6`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ccb43d72fabc5c0803df48f8f830113629325357", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_seven_noroot_k5_dminus1_d0p7_all_pair_sync_2026-09-21.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "9e135c987d125ef5c026de372fc3ea5c2a21b497cfde109dba093b1ed9409878"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: all-pair synchronization in the final seven-no-root `k=5` branch

Date: 2026-09-21

Status: rigorous strengthening of the remaining

`D=-1, k=5, d=0, p=7`

branch. The branch is not yet closed, but coefficient-rank-drop pairs are now impossible. Every one-row deletion is therefore a fully synchronized six-row `k=4` shadow, not merely the deletion of one specially chosen unmatched coordinate.

Companion arithmetic certificate:

`research/verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_sync_upgrade_2026_09_21.py`

This note composes the already committed exact p=7 functional-span audits

- `research/verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_d2_functional_2026_09_21.py`, and
- `research/verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_d3_functional_2026_09_21.py`

with the established five-row `k=4` containment theorem and the seven-row all-depth deletion identity.

## 1. Five-row `k=4,p=7` has defect at least three

For five no-root rows in the `k=4` branch, the virtual-canonical containment theorem gives

`D >= 5 + p + 3d - 3q`,

where

- `d>=2` is the complete-row deficiency of the virtual canonical complete-block set, and
- `q<=p` is the number of virtual-canonical complete blocks replaced by incomplete states.

At `p=7`, the crude bound is

`D >= 12 + 3d - 3q`.

With `d>=2` and `q<=7`, the only arithmetic points at which this crude bound is below three are

```text
d   q   crude lower bound
2   6          0
2   7         -3
3   7          0
```

Every other `(d,q)` already has `D>=3`.

### The `d=2,q=7` form is absent

Since `p=7`, seven replaced virtual-complete blocks would all have to be singletons. The exact `d=2` p=7 audit proves that a deficiency-two canonical state has at most six compatible virtual-complete singleton blocks. Hence `q=7` is impossible.

### The `d=2,q=6` forms have large positive defect

There are only two ways to spend seven incomplete root rows while replacing six virtual-complete blocks.

1. Five singleton replacements plus one pair replacement.
2. Six singleton replacements plus one singleton on a virtual-canonical empty block.

For a virtual canonical relation matrix `M`, replacing a virtual-complete block by a compatible incomplete state contributes a row-index functional. If those replacement functionals gain rank `s` modulo `Col(M)`, then the actual defect is

`D = 5 + p + 3d - 3s`.

The exact `d=2` functional audit proves:

- the span of all compatible singleton replacement functionals gains rank exactly two; and
- even after adjoining an arbitrary pair replacement functional, the gain is at most three.

Therefore the two `q=6` root-cost forms satisfy respectively

`D >= 12 + 6 - 9 = 9`,

and

`D >= 12 + 6 - 6 = 12`.

### The `d=3,q=7` form has defect at least three

Here all seven replacements are singletons. The exact `d=3` functional audit exhausts every deficiency-three canonical state with singleton capacity at least seven and proves that the entire singleton-functional span gains rank at most six modulo `Col(M)`.

Hence

`D >= 12 + 9 - 18 = 3`.

Combining the crude region with these exact residual audits gives the new five-row theorem:

> Every five-no-root `k=4,p=7` state satisfies `D>=3`.

The committed exact audits use the same `2^127-1` modular rank certificate and Hadamard bounds as the underlying containment theorem. The `d=2` audit has only nine candidate canonical bases of singleton capacity at least five; the `d=3` audit has 9,059 candidate bases of singleton capacity at least seven. Their asserted functional-rank censuses are part of the committed certificates.

## 2. Rank-drop pairs in the seven-row target are impossible

Return to a hypothetical seven-no-root state with

`D_7=-1, k=5, d=0, p=7`.

Its coefficient-constraint space

`P_7 <= Q^7`

has rank two. The previously proved all-depth bound gives

`d_1(P_7)>=2, d_2(P_7)>=4`.

For a two-coordinate deletion `J`, let `q_J` be the coefficient-rank drop. Because `d_2(P_7)>=4`, deleting two coordinates cannot lower rank by two: that would support all of `P_7` on those two coordinates. Hence

`q_J in {0,1}`.

The exact defect-transport identity gives

`D(B\J) = D(B) + 2|J| - 3q_J = -1 + 4 - 3q_J`.

Thus

```text
q_J=0  =>  D_5=3
q_J=1  =>  D_5=0
```

If `q_J=1`, the five-row shadow has coefficient rank one, hence lies in the five-row `k=4,p=7` branch just closed above. But that branch has `D>=3`, contradicting `D_5=0`.

Therefore

> every one of the 21 two-coordinate punctures preserves coefficient rank two.

Equivalently, `P_7` contains no nonzero vector supported on at most two coordinates. The generalized-weight bound improves to

`(d_1,d_2) >= (3,4)`.

## 3. Every six-row deletion is now fully synchronized

Single-coordinate punctures already preserve rank because the old all-depth bound had `d_1(P_7)>=2`. The new pair result says that every further one-coordinate puncture also preserves rank.

Therefore, for every coordinate `i`, the six-row deletion `B\{i}` has

- coefficient rank two;
- defect `D_6=-1+2=1`;
- incomplete-root cost `p=7`; and
- all six of its five-row coordinate deletions still of coefficient rank two and defect three.

So every one-row deletion, not only one deletion chosen outside the old rank-drop matching, is a synchronized six-row `k=4` shadow.

This upgrades the previous reduction substantially.

## 4. The two surviving root patterns become global all-shadow conditions

The previous `d0p7` reduction proved that one fully synchronized six-row shadow leaves only two possible global root patterns:

```text
B: five singleton incomplete blocks + one pair incomplete block
C: seven singleton incomplete blocks
```

It also proved:

- synchronized six-row `d_6=1` is impossible;
- an all-singleton synchronized `d_6=2` shadow is impossible.

Because every one-row deletion is now synchronized, these conclusions apply simultaneously to all seven six-row shadows.

### Pattern B

The global root state has exactly six nonempty incomplete blocks, five singletons and one pair. Since `d_6=1` is excluded and `q_6<=6`, every one of the seven six-row deletions must satisfy

`d_6=2, q_6=6`.

Thus all six actual incomplete blocks are virtual-canonical complete in every one-row deletion.

Every two-row deletion has five-row coefficient rank two and defect three. Row-nullity monotonicity gives

`d_5 in {1,2}`.

The five-row containment arithmetic sharpens this to

```text
d_5=1  =>  q_5=4 exactly,
             with the pair block and exactly three singleton blocks virtual-complete;

d_5=2  =>  q_5>=5.
```

These conditions now hold for all 21 pair shadows, not merely the six pair shadows containing one specially chosen coordinate.

### Pattern C

The global root state has seven singleton incomplete blocks. The all-singleton synchronized `d_6=2` layer is already excluded, so every one of the seven six-row deletions must satisfy

`d_6=3, q_6=7`.

Thus all seven singleton blocks are virtual-canonical complete in every one-row deletion.

Every pair shadow has

`d_5 in {2,3}`,

with the containment thresholds

```text
d_5=2  =>  q_5>=5,
d_5=3  =>  q_5>=6.
```

Again these restrictions now hold on all 21 pair shadows.

## 5. Projective prefilter on the global rank-two code

Choose a `2 x 7` generator matrix for `P_7`. Let `z` be the number of zero columns and let `m_max` be the largest multiplicity of one projective nonzero column direction.

For a rank-two code, a nonzero codeword vanishes on every zero column and on all columns lying in one projective direction. Hence

`d_1(P_7) = 7 - z - m_max`.

The new `d_1>=3` bound gives

`z + m_max <= 4`.

The existing `d_2>=4` bound is simply

`7-z >=4`,

so `z<=3`.

Any exact seven-row coefficient-space generator can impose these projective filters before local-state or `T`-space work.

## 6. Remaining bottleneck

The final seven-no-root `k=5` branch is still open, but its finite target is narrower than in the previous reduction.

Pattern B must realize seven different synchronized six-row shadows, all of type

`d_6=2,q_6=6`,

and all 21 pair shadows must obey the `d_5=1/2` thresholds above.

Pattern C must realize seven synchronized six-row shadows, all of type

`d_6=3,q_6=7`,

and all 21 pair shadows must obey the `d_5=2/3` thresholds above.

The next exact search should exploit the all-seven deletion requirement rather than extend one arbitrary six-row parent in isolation. A particularly direct alternative is a six-row replacement-functional audit: pattern B would need six replacement functionals to gain the full six-dimensional quotient rank, while pattern C would need seven singleton replacement functionals to gain the full seven-dimensional quotient rank. Any strict upper bound on either functional span closes the corresponding pattern before seven-row assembly.

The direct C-II endpoint remains

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.
