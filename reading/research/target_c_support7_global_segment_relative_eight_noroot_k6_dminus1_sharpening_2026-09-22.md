> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_sharpening_2026-09-22.md) · source SHA-256 `afa8ba3e3a2d368aaaaeddd7205732acfeda7be648b221659fc315385d4ba048`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "75d4d246f0737ee04ac19fba4e33348d38ff7af7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_sharpening_2026-09-22.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1918e5e3dee21812c71e7d126f994af155ee3c8b6f57b0ba9bc667fba5468a37"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: sharpen the eight-no-root `k=6`, `D=-1,p=9` residual

Date: 2026-09-22

Status: rigorous structural sharpening of the remaining eight-no-root `k=6` branch after closure of the `D=-2` side. This note proves a new zero-capacity theorem for seven-row synchronized rank-two deficiency-one states, eliminates both remaining global deficiency-one profiles, eliminates the all-singleton part of global deficiency two (including `(d_v,q)=(2,9)`), and reduces the entire `D=-1,p=9` branch to two explicit residual patterns.

Companion arithmetic/support checker:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_sharpening_2026_09_22.py`

The exact inputs reused are:

- `research/verify_target_c_support7_global_segment_relative_seven_noroot_k5_dminus1_d1p4_2026_09_21.py`, which proves synchronized six-row rank-two deficiency-one singleton capacity at most three and, more strongly, touch support exactly three for every compatible singleton block;
- `research/verify_target_c_support7_global_segment_relative_five_noroot_k3_p5_sharp_2026_09_21.py`, which proves the repaired five-row rank-two deficiency-one singleton-capacity maximum three; and
- `research/verify_target_c_support7_global_segment_relative_six_noroot_k4_d2_singleton_capacity_2026_09_21.py`, whose exact synchronized deficiency-two audit has zero singleton-capacity-at-least-six states with all six five-row projections of deficiency two.

The unstripped containment convention is used throughout: `p` counts all selected rows in incomplete root blocks, including rows in blocks that become untouched after deleting no-root rows. As already proved in the committed sharp-shadow arguments, such untouched incomplete rows impose no external coefficient constraint and no relative `T` relation, so keeping them increases the row count without changing the relative relation rank. Thus the same containment inequality holds with the original total incomplete-root cost.

For the current branch that total cost is always

```text
p=9.
```

## 1. A stronger seven-row deficiency-one theorem

The previous eight-no-root reduction proved only that a synchronized seven-row rank-two virtual state of deficiency one has singleton capacity at most four. The exact six-row support census improves this to zero.

### Lemma 1

Let `Q<=Q^7` have rank two. Assume every one- and two-coordinate puncture of `Q` still has rank two. If the seven-row virtual-canonical complete set has deficiency one, then it admits no compatible singleton block at all.

Equivalently,

```text
seven-row synchronized rank-two d=1 singleton capacity = 0.
```

### Proof

Fix a seven-row compatible singleton block `b` that is virtual-canonical complete, and suppose for contradiction that one exists.

For every coordinate deletion `j`, the resulting six-row coefficient plane is synchronized. Its virtual-complete set is contained in the seven-row one, so its deficiency is at most one; the six-row containment theorem gives deficiency at least one. Therefore every six-row deletion has deficiency exactly one.

The previous capacity-lifting argument already proves that `b` can disappear from the compatible singleton-complete set for at most two deletion coordinates:

1. at most one deletion can make the block untouched;
2. at most one deletion can leave it touched but make it virtual-canonical empty.

The second statement follows from the rank-two puncture condition. If two distinct deletions `j,k` both made the block canonical-empty, its empty-state constraint space would lie in both `Q+span(e_j)` and `Q+span(e_k)`. Either their intersection is `Q`, contradicting that `b` was seven-row virtual-complete, or the two spaces coincide, which would put a nonzero vector supported on `{j,k}` in `Q`, contradicting preservation of rank under the two-coordinate puncture.

Hence `b` survives as a compatible singleton-complete block in at least five of the seven six-row deletions.

Now use the stronger exact six-row census. Every compatible singleton block in every synchronized six-row rank-two deficiency-one state is touched by exactly three of the six no-root rows.

Let `m` be the number of the seven no-root rows touching `b` before deletion. After deleting one coordinate, the projected touch support has size

- `m-1` for each of the `m` touching-coordinate deletions;
- `m` for each of the `7-m` nontouching-coordinate deletions.

For a projected support to equal three:

- if `m=3`, only the four nontouching deletions work;
- if `m=4`, only the four touching deletions work;
- for every other `m`, no deletion leaves support three.

Thus at most four of the seven deletions can produce a six-row singleton block of touch support exactly three.

But `b` must survive in at least five deletions, and every survivor must have support exactly three. Contradiction. `□`

This zero-capacity statement is strictly stronger than the previous bound `S<=4`.

## 2. Clean-shadow arithmetic for `D=-1,p=9`

The current global coefficient-constraint space `P<=Q^8` has rank two and generalized weight `d_2(P)>=4`. The committed projective-column argument gives at least two three-clean coordinates. Fix one such coordinate `i`.

Every puncture of at most three coordinates containing `i` preserves coefficient rank two. Therefore the one-, two-, and three-row deletion shadows containing `i` have defects

```text
D_7 = -1+2 = 1,
D_6 = -1+4 = 3,
D_5 = -1+6 = 5.
```

With unstripped total cost `p=9`, the containment inequality

```text
D_t >= t+p+3d_t-3q_t
```

forces the following minimum numbers of virtual-complete changed blocks:

```text
seven rows:  d=1 -> q>=6, d=2 -> q>=7, d=3 -> q>=8;
six rows:    d=1 -> q>=5, d=2 -> q>=6, d=3 -> q>=7;
five rows:   d=1 -> q>=4, d=2 -> q>=5, d=3 -> q>=6.
```

These thresholds will be used repeatedly below.

## 3. All global deficiency-one profiles are impossible

The remaining global deficiency-one profiles were

```text
(d_v,q,singleton_min)=(1,7,5),(1,8,7).
```

The already-eliminated `(1,9,9)` profile is not needed here.

For a three-clean deletion `i`, virtual-complete sets shrink under projection, so `d_7<=d_v=1`. The seven-row containment theorem gives `d_7>=1`. Hence

```text
d_7=1.
```

Lemma 1 says this seven-row state has singleton capacity zero.

But the seven-row containment threshold requires `q_7>=6`.

For global `(d_v,q)=(1,7)`, at least five of the seven global changed blocks are singletons, so there are at most two pair blocks. Any six retained changed blocks therefore contain at least four singleton blocks.

For global `(d_v,q)=(1,8)`, at least seven of the eight changed blocks are singletons, so any six retained changed blocks contain at least five singleton blocks.

Because the deletion virtual-complete set is a subset of the global one, every block counted by `q_7` is one of the global changed blocks. Therefore either profile would force positive, in fact at least four, singleton capacity in a seven-row `d_7=1` state.

That contradicts Lemma 1.

Hence both global deficiency-one profiles are impossible.

## 4. Global deficiency two: the all-singleton form is impossible

The remaining global deficiency-two profiles were

```text
(d_v,q)=(2,8),(2,9).
```

At `q=9`, all nine changed blocks are singletons.

At `q=8`, the incomplete-root cost `p=9` and the minimum singleton count seven give exactly two root-pattern possibilities:

1. seven singleton changed blocks plus one pair changed block, using all nine rows;
2. eight singleton changed blocks, plus one additional singleton row on a virtual-canonical empty block.

This section excludes the second, all-singleton-changed form. It also excludes all of `(2,9)`.

Assume therefore that every globally changed virtual-complete block is a singleton. There are either eight or nine such blocks.

Take a three-clean deletion `i`. We have `d_7<=2` and `d_7>=1`.

If `d_7=1`, the seven-row threshold gives `q_7>=6`. Every one of those changed blocks is a singleton, contradicting Lemma 1. Hence

```text
d_7=2.
```

Now delete any second coordinate `j`. The resulting six-row state is synchronized because every further one-coordinate puncture deletes a three-set containing `i`. Its deficiency satisfies

```text
1<=d_6<=d_7=2.
```

If `d_6=1`, the six-row threshold gives `q_6>=5`. All five changed blocks would be singleton-compatible, contradicting the exact synchronized six-row deficiency-one capacity maximum three. Thus

```text
d_6=2,
q_6>=6,
singleton capacity >=6.
```

Delete any one of the six remaining coordinates. The five-row state has

```text
1<=d_5<=2.
```

If `d_5=1`, the five-row threshold gives `q_5>=4`. Again all changed blocks are singletons, contradicting the exact five-row deficiency-one capacity maximum three. Therefore every one of the six five-row projections has

```text
d_5=2,
q_5>=5,
singleton capacity >=5.
```

We have reached exactly the structural class exhaustively covered by the committed synchronized six-row deficiency-two audit:

```text
synchronized six-row rank-two,
d_6=2,
singleton capacity >=6,
all six five-row projections d_5=2.
```

The exact full-cover survivor count for that class is zero.

Contradiction.

Therefore:

- `(d_v,q)=(2,9)` is impossible;
- the eight-singleton-changed subcase of `(d_v,q)=(2,8)` is impossible.

The only global deficiency-two residual is

```text
d_v=2,
q=8,
root pattern = 7 singleton changed blocks + 1 pair changed block.
```

## 5. The pair residual is synchronized more strongly

Fix the remaining deficiency-two pair pattern and a three-clean coordinate `i`.

As above, `d_7=1` is impossible: `q_7>=6`, and with only one pair block among the eight changed blocks this would force at least five compatible singleton blocks, contradicting Lemma 1. Hence

```text
d_7=2,
q_7>=7,
singleton capacity >=6.
```

Now delete any second coordinate `j`. We again have `1<=d_6<=2`.

If `d_6=1`, then `q_6>=5`; with at most one pair among those changed blocks, at least four are singletons, contradicting the exact six-row deficiency-one singleton-capacity maximum three. Therefore every such double-deletion shadow has

```text
d_6=2,
q_6>=6,
singleton capacity >=5.
```

There is one more forced condition.

### Lemma 2

The unique pair block must be virtual-canonical complete in every six-row double-deletion shadow containing the chosen three-clean coordinate `i`.

### Proof

Suppose some double-deletion shadow `B\{i,j}` made the pair block virtual-canonical empty or untouched. Since virtual-complete sets only shrink under further puncturing, that pair block would be absent from every five-row projection of this six-row state.

The six-row threshold gives `q_6>=6`. With the pair absent, all `q_6` changed virtual-complete blocks are singleton blocks, so the six-row singleton capacity is at least six.

For any five-row projection, if `d_5=1`, then `q_5>=4`. The pair is still absent, so all four changed blocks would be singletons, contradicting the exact five-row deficiency-one capacity maximum three. Hence all six five-row projections must have `d_5=2`.

This is again the exact zero-survivor class of the committed synchronized six-row `d_6=2`, capacity-at-least-six audit. Contradiction. `□`

Thus the pair block survives as virtual-complete through every double deletion containing a three-clean coordinate.

For a five-row projection of one of these six-row shadows:

- if `d_5=1`, then `q_5>=4`; the deficiency-one singleton-capacity maximum three forces the pair block to remain virtual-complete and forces exactly three singleton changed blocks alongside it;
- if `d_5=2`, then `q_5>=5`.

So the deficiency-two residual is no longer an arbitrary seven-singleton/one-pair configuration. The pair block must persist through the whole clean depth-two deletion fan.

## 6. Global deficiency three is forced to stay deficiency three down two levels

The last global profile is

```text
d_v=3,
q=9,
nine singleton changed blocks.
```

Take a three-clean coordinate `i`.

The seven-row deficiency lies in `{1,2,3}`.

- `d_7=1` is impossible by Lemma 1, because `q_7>=6` and all changed blocks are singletons.
- Suppose `d_7=2`. Delete any second coordinate `j`. If `d_6=1`, then `q_6>=5`, contradicting the six-row deficiency-one singleton-capacity maximum three. Hence `d_6=2` and `q_6>=6`. Every five-row projection then has `d_5 in {1,2}`; `d_5=1` would require four singleton blocks, above the exact capacity-three bound, so all six projections have `d_5=2`. The committed six-row deficiency-two zero-survivor audit gives a contradiction.

Therefore

```text
d_7=3
```

for every three-clean deletion.

Now fix any second deletion `j`. Its six-row deficiency lies in `{1,2,3}`.

- `d_6=1` is impossible because `q_6>=5` singleton blocks would be required.
- `d_6=2` is impossible by the same five-row cascade and zero-survivor audit just used above.

Hence every such synchronized double-deletion shadow has

```text
d_6=3,
q_6>=7,
singleton capacity >=7.
```

Every five-row projection has `d_5<=3`. The `d_5=1` option is impossible because it would require four compatible singleton blocks, above the exact capacity-three bound. Thus

```text
d_5 in {2,3}
```

throughout the clean depth-three fan.

This is now the exact all-singleton higher-deficiency residual.

## 7. Exact remaining `D=-1,p=9` target

After these exclusions, the previous five global virtual profiles collapse to exactly two root patterns.

### Pair residual

```text
global:
    d_v=2,
    q=8,
    7 singleton changed blocks + 1 pair changed block;
for every three-clean i:
    d_7=2,
    q_7>=7,
    singleton capacity >=6;
for every j!=i:
    d_6=2,
    q_6>=6,
    singleton capacity >=5,
    the pair block remains virtual-complete;
five-row children:
    d_5=1 => pair + exactly 3 singleton changed blocks,
    d_5=2 => q_5>=5.
```

The global maximal-functional-rank theorem requires the eight global replacement functionals to be independent. Each clean seven-row shadow must also fill its seven-dimensional replacement-functional quotient, and each clean six-row `d_6=2` shadow must fill its six-dimensional quotient.

### All-singleton residual

```text
global:
    d_v=3,
    q=9,
    9 singleton changed blocks;
for every three-clean i:
    d_7=3,
    q_7>=8;
for every j!=i:
    d_6=3,
    q_6>=7,
    singleton capacity >=7;
five-row children:
    d_5 in {2,3}.
```

The global maximal-functional-rank theorem requires all nine replacement functionals to be independent. Every clean seven-row shadow must fill an eight-dimensional quotient and every clean six-row `d_6=3` shadow must fill a seven-dimensional quotient.

These two classes are the only remaining eight-no-root `k=6` targets after the `D=-2` closure and the present sharpening.
