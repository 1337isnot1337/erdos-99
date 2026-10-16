# Target C: close seven-no-root `D=-2,k=6,d=0,p=9`

Date: 2026-09-21

Status: closed. Combined with the preceding seven-no-root `k=6` reduction, this leaves only `D=-1,k=6,d=0,p=10` in the `k=6` layer.

Companion verifier:

- `research/verify_target_c_support7_global_segment_relative_seven_noroot_k6_dminus2_d0p9_closure_2026_09_21.py`

The finite part is an exact refinement of the already committed six-row rank-one virtual-canonical audit. It uses the same exact `S_7` augmentation cover and the same certified modular complete-block ranks.

## 1. Starting point

Assume a seven-no-root counterexample with

```text
D=-2, k=6, d=0, p=9.
```

The preceding `k=6` containment lift already proves that its seven-row virtual-canonical state satisfies

```text
d_v=3, q=9.
```

Therefore all nine virtual-complete incomplete blocks are singletons, and they consume the entire incomplete-root budget. There are no other selected incomplete root rows.

Let `P<=Q^7` be the rank-one coefficient space. The established all-depth bound gives

```text
|supp(P)| >= 3.
```

Every one-row deletion has six no-root rows, `k=5`, and defect `D_6=0`.

## 2. Every one-row deletion retains all nine singleton rows

For deletion `i`, the exact six-row arithmetic gives

```text
p_i in {0,3,6,9}.
```

The synchronized six-row containment theorem gives

```text
0 >= 6 + p_i + 3 d_i - 3 q_i,
```

with `d_i>=2`, `q_i<=p_i`, and `C_i subset C`.

If `p_i<=3`, then even the extremal choice `d_i=2,q_i=p_i` gives a positive right-hand side, so those cases are impossible.

If `p_i=6`, deficiency `d_i>=3` is already impossible because it would require `q_i>6`. Thus `d_i=2`, and the inequality forces `q_i=6`. Since every actual incomplete block is one of the nine global singletons, these six `q_i` blocks are singleton-compatible virtual-complete blocks. But the exact all-touch six-row audit proves that every synchronized deficiency-two state has singleton capacity at most three. Contradiction.

Hence

```text
p_i=9
```

for every one of the seven deletions. In particular no global singleton block is touched by only one no-root row.

Now `p_i=9`. If `d_i=2`, containment gives `q_i>=7`, again contradicting the exact deficiency-two capacity-three bound because all such `q_i` blocks are global singletons. Therefore

```text
d_i=3, q_i>=8
```

for every deletion.

Thus every one-row shadow belongs to the exact six-row class

```text
deficiency 3, singleton capacity at least 8.
```

## 3. Exact support-three refinement

The companion verifier scans the exact 325,955-representative six-subset augmentation cover and every obtainable synchronized rank-one coefficient line. Among deficiency-three states with singleton capacity at least eight it finds exactly

```text
324 states.
```

Their coefficient-line support census is

```text
support 2: 317
support 3:   7
```

No such state has coefficient support four or more.

The seven support-three states have capacities

```text
capacity 8: 2
capacity 9: 5.
```

Across their 61 singleton-capable virtual-complete blocks, every block has exactly one touched six-row coordinate, and that coordinate lies in the support of the coefficient line. There are zero exceptions.

The exact assertions are

```text
d3_capacity_ge8_states       324
line_support_census          {2: 317, 3: 7}
support3_capacity_census     {8: 2, 9: 5}
support3_capable_blocks      61
support3_bad_touch_blocks    0
```

## 4. The global coefficient line has support exactly three

Every deletion shadow has coefficient support at most three by the exact refinement above.

The global line has support at least three. If its support were at least four, then some one-coordinate deletion would still have support at least four: for support four through six, delete a zero coordinate; for support seven, every deletion leaves support six. This contradicts the six-row census.

Therefore

```text
|supp(P)|=3.
```

Let `S` be those three support coordinates and let `Z` be the four zero coordinates.

For each `z in Z`, deleting `z` leaves coefficient support exactly three. Its six-row shadow is therefore one of the seven support-three states from the exact audit.

## 5. Four disjoint eight-block requirements

Fix `z in Z`. We have `q_z>=8`. Each of those `q_z` blocks is one of the nine global incomplete singleton blocks and is singleton-compatible and virtual-complete in the six-row shadow.

The exact support-three refinement says that, after deleting `z`, each such block is touched by exactly one remaining coordinate `s`, and `s in S`.

Because every deletion has `p_i=9`, no global singleton is globally touched only once. The block therefore must also be touched by the deleted coordinate `z`. There are no other possible touches, because the six-row shadow had only the one touch `s`. Hence every block counted by `q_z` has global touch set exactly

```text
{z,s} with s in S.
```

For distinct zero coordinates `z,z' in Z`, these block sets are disjoint. A block with touch set `{z,s}` cannot simultaneously have touch set `{z',s'}` because `z,z'` lie outside `S` and are distinct.

Each of the four zero-coordinate deletions therefore requires at least eight distinct blocks among the same nine global singleton blocks. This would require at least

```text
4*8 = 32
```

distinct singleton blocks, but only nine exist. Contradiction.

Therefore no seven-no-root counterexample exists with

```text
D=-2, k=6, d=0, p=9.
```

## 6. Validation

The exact verifier was rerun over the previously generated exact six-subset cover from the committed augmentation routine. It reported

```text
PASS: exact support-three six-shadow refinement closes seven-no-root D=-2,k=6,d=0,p=9
six_augmentation_cover 325955
d3_capacity_ge8_states 324
line_support_census {2: 317, 3: 7}
support3_capacity_census {8: 2, 9: 5}
support3_capable_blocks_checked 61
support3_bad_touch_blocks 0
global_support_forced 3
zero_coordinate_deletions 4
disjoint_required_blocks 32
available_global_singletons 9
```

The verifier defaults to rebuilding the exact cover from the committed orbit code; the cache option only avoids repeating that cover construction during local reruns.

The only remaining seven-no-root `k=6` arithmetic case is now

```text
D=-1, k=6, d=0, p=10.
```
