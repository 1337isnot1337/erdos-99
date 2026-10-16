# Target C: six-row `d=4` functional obstruction and eight-no-root `k=7` closures

Date: 2026-09-21

Status: exact finite obstruction. Branch A is closed completely, and the branch-C profile `(d_v,q,s)=(4,12,12)` is also closed. The eight-no-root `k=7` layer is reduced to two profiles.

Companion exact verifier:

- `research/verify_target_c_support7_global_segment_relative_six_noroot_k5_d4_capacity9_functional_2026_09_21.py`

Existing exact inputs used below:

- `research/verify_target_c_support7_global_segment_relative_seven_noroot_k6_d3_capacity7_extension_2026_09_21.py`
- `research/verify_target_c_support7_global_segment_relative_eight_noroot_k7_A_d3_pair_extension_2026_09_21.py`
- `research/verify_target_c_support7_global_segment_relative_eight_noroot_k7_pair_shadow_reduction_2026_09_21.py`

## 1. The six-row functional threshold

Consider a synchronized six-row rank-one `k=5` virtual-canonical state whose actual incomplete root rows are all singleton rows. If the virtual-complete set has deficiency `d` and the compatible singleton replacement functionals gain extra rank `s_f` modulo the canonical relation-column span, the established replacement-functional accounting gives

```text
D_6 >= 6 + p_6 + 3 d - 3 s_f.
```

For the two applications below the shadow has `d=4`.

For branch A,

```text
D_6=2, p_6=11,
```

so `s_f>=9` is necessary.

For the all-singleton branch-C profile `(4,12,12)`,

```text
D_6=3, p_6=12,
```

and again `s_f>=9` is necessary.

Thus both cases reduce to the same finite question: can a synchronized six-row rank-one virtual-canonical state of deficiency four and singleton capacity at least nine have singleton-functional extra rank at least nine?

## 2. Exact `d=4`, capacity-at-least-nine census

The exact `S_7` six-row augmentation cover has 325,955 representatives. Across it there are 1,751,870 synchronized rank-one states.

The new verifier retains every virtual-canonical state with

```text
d_6=4,
singleton capacity >=9,
```

constructs every compatible singleton replacement functional, and computes the rank of their full span modulo the canonical relation-column span.

The complete census is:

```text
capacity   states   maximum extra rank
9          13,536          8
10         12,922          8
11         11,898          8
12          8,614          8
13          3,733          8
14            762          8
---------------------------------------
total      51,465          8
```

The full `(capacity, extra-rank)` census is hard-coded in the verifier. The complete computation was run in four disjoint shards covering

```text
[0,82000)
[82000,164000)
[164000,246000)
[246000,325955).
```

Their aggregate is

```text
synchronized states:              1,751,870
d=4, capacity>=9 candidate states:   51,465
maximum singleton-functional gain:         8
maximum row norm squared:                 42
maximum functional width:                 23
```

No candidate reaches the required extra rank nine.

The modular ranks are exact over `Q`. The verifier checks Lucas-Lehmer primality for `P=2^127-1`, and the observed norm/width values satisfy the same Hadamard determinant certificate used in the preceding replacement-functional audits.

Therefore:

> No synchronized six-row rank-one `d=4` state with singleton capacity at least nine can realize either `D_6=2,p_6=11` or `D_6=3,p_6=12` when all selected incomplete rows are singleton rows.

## 3. Close branch A

The only surviving branch-A profile before this run was

```text
D=-2, d_root=0, p=11,
(d_v,q,s)=(4,11,11).
```

All eleven selected incomplete rows are singletons. The committed good-pair reduction supplies a `p=11`-retaining synchronized six-row shadow. Its deficiency satisfies `2<=d_6<=4`.

- `d_6=2` was already excluded by the exact six-row deficiency-two singleton-capacity bound.
- `d_6=3` is excluded by the committed branch-A pair-extension verifier. Starting from the 324 six-row `d=3`, capacity-at-least-eight states, that scan tests 684,270 compatible pair extensions. It finds 19,016 global deficiency-four states and zero with global singleton capacity at least eleven.
- `d_6=4` is excluded by the new functional census because the shadow would require extra rank at least nine, while the exact maximum is eight.

Hence

> `D=-2,d_root=0,p=11` is impossible.

Branch A is closed.

## 4. Close branch C profile `(4,12,12)`

Now consider the surviving branch-C profile

```text
D=-1, d_root=0, p=12,
(d_v,q,s)=(4,12,12).
```

All twelve selected incomplete rows are singletons. Choose the committed good `p=12`-retaining pair deletion. Its six-row shadow has

```text
D_6=3,
k_6=5,
p_6=12,
2<=d_6<=4.
```

### `d_6=2`

Six-row containment would require at least seven virtual-complete changed blocks. Since all changed blocks are singleton blocks, the shadow would have singleton capacity at least seven. The exact deficiency-two capacity maximum is three. Contradiction.

### `d_6=3`

Containment requires at least eight virtual-complete changed blocks, so the six-row singleton capacity is at least eight.

Add either deleted cycle back. The resulting seven-row `p=12` shadow has `D_7=1`. Deficiency two would require at least eight singleton-compatible changed blocks, contradicting the exact seven-row deficiency-two capacity maximum of five. If its deficiency were three, containment would require at least nine singleton-compatible blocks. But the committed six-to-seven extension theorem proves that no six-row `d=3`, capacity-at-least-six state extends to a seven-row `d=3`, capacity-at-least-seven state. Therefore each intermediate seven-row shadow is forced to

```text
d_7=4,
singleton capacity >=10.
```

The committed branch-A pair-extension verifier is actually a structural extension obstruction at exactly these thresholds: from every six-row `d=3`, capacity-at-least-eight state it enumerates both seven-row `d=4`, capacity-at-least-ten lifts and then the global eight-row line. It finds no global `d_8=4` state with singleton capacity at least eleven.

The present profile would have global capacity at least twelve, so it is excluded.

### `d_6=4`

The new functional census applies directly. At `D_6=3,p_6=12,d_6=4`, the shadow would need singleton-functional extra rank at least nine. The exact maximum is eight. Contradiction.

All three possible six-row deficiencies are impossible. Hence

> The branch-C profile `(d_v,q,s)=(4,12,12)` is impossible.

## 5. Remaining eight-no-root `k=7` target

Only two profiles now remain:

```text
C: D=-1, d_root=0, p=12
   (d_v,q,s)=(4,11,10)
   (d_v,q,s)=(5,12,12)
```

The new functional census also removes the `d_6=4` good-pair-shadow subcase from `(5,12,12)`, because that shadow is all-singleton and has the same `D_6=3,p_6=12` threshold. Thus the `d_v=5` profile can only survive through a selected pair shadow of deficiency three or five.

The smallest unresolved target is `(4,11,10)`: ten singleton blocks and one pair block. A good `p=12` pair shadow has `d_6` equal to three or four after deficiency two is excluded. The `d_6=3` side requires singleton capacity at least seven; the `d_6=4` side requires at least eight singleton-compatible blocks plus the contribution of the one pair replacement. A direct next scan should therefore either

1. extend the 402 six-row `d=3`, capacity-at-least-seven states through both seven-row shadows to global `d_8=4`, capacity-at-least-ten states; or
2. augment the new `d=4` functional audit with the compatible pair-replacement functional and test whether singleton-plus-pair extra rank can reach nine.
