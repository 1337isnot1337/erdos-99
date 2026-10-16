# Target C: close the Profile B three-rank-two singleton exception

Date: 2026-09-22

Status: rigorous finite closure of the unique exceptional source geometry left by the singleton-line sharpening. The exceptional case

```text
d_2(P)=6,
projective multiplicities=(2,2,2),
three rank-two singleton blocks in common-two-set geometry
```

is impossible. Consequently every remaining genuine eight-no-root `k=6,D=-1,p=9` Profile B source has at most two rank-two singleton blocks and therefore at least seven aligned singleton blocks.

Companion exact certificate:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_three_ranktwo_exception_closure_2026_09_22.py`

The preceding reduction is

`research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_singleton_line_sharpening_2026-09-22.md`.

## 1. Input from the singleton-line sharpening

For a genuine remaining Profile B source, the coefficient space satisfies

```text
P <= Q^8,
rank(P)=2,
d_1(P)>=4.
```

If three singleton blocks have rank-two local empty spaces, the preceding sharpening proves all of the following:

1. `d_2(P)=6`;
2. the six nonzero coordinate columns of a generator of `P` have projective multiplicities `(2,2,2)`;
3. the three singleton coefficient lines are the three distinct weight-four codeword lines corresponding to those projective classes;
4. up to `S_7`, the three root blocks are

```text
B_1=123,
B_2=124,
B_3=125;
```

5. each pairwise support intersection has size two, and the three pairwise intersections are disjoint.

The source also has `d_1(P)>=4`, so every source coordinate is three-clean. Hence the already-proved all-clean-fans statement applies to all eight source coordinates: every one- and two-coordinate puncture preserves coefficient rank two, and every two-coordinate puncture has virtual canonical deficiency three.

The present note eliminates the only three-rank-two geometry allowed by the preceding argument.

## 2. The local directions are rigid

Let `s_i` be the chosen singleton local projective direction at `B_i`. For a source no-root cycle `e`, the singleton coefficient row is, up to a nonzero scalar,

```text
L_i(e) = det(s_i, q_e(B_i)),
```

where `q_e(B_i)` is the local quotient vector of `e` at `B_i`.

For each pair of blocks, exactly three no-root cycles touch both. They are the three four-cycle orientations on the pair union:

```text
B_1,B_2: 1234,
B_1,B_3: 1235,
B_2,B_3: 1245.
```

At either incident block, those three orientations occupy the three local projective directions one each.

Because the exceptional coefficient code has multiplicities `(2,2,2)`, every pair of the three weight-four singleton coefficient lines must intersect on exactly two coordinates, and those three two-coordinate intersections must be disjoint. The companion certificate checks all

```text
3^3 = 27
```

choices of `(s_1,s_2,s_3)` against the actual local quotient vectors. Exactly one normalized choice survives:

```text
s_1=s_2=s_3=(0,1).
```

For that choice the six nonzero coordinates are forced. In the repository's canonical cycle representatives they are

```text
packet 12 on 1234:
    (1,2,3,4), (1,2,4,3)

packet 13 on 1235:
    (1,2,3,5), (1,2,5,3)

packet 23 on 1245:
    (1,2,4,5), (1,2,5,4).
```

In this coordinate order the three singleton coefficient rows are exactly

```text
L_1 = (-1, 1, -1, 1,  0, 0),
L_2 = ( 1,-1,  0, 0, -1, 1),
L_3 = ( 0, 0,  1,-1,  1,-1),
```

with

```text
L_1+L_2+L_3=0.
```

They span a rank-two code whose three nonzero projective column classes each occur twice, as required.

Thus the support-level exception is in fact coefficient-rigid: after the `S_7` normalization, both the six nonzero source coordinates and the coefficient plane on them are fixed.

## 3. Only 87 cycles can occupy a zero coefficient column

The source has length eight and `d_2(P)=6`, so exactly two source coordinate columns of `P` are zero.

A zero-column source cycle `e` must satisfy

```text
L_1(e)=L_2(e)=L_3(e)=0.
```

Equivalently, at each of the three exceptional blocks, `e` either does not touch the block or its local quotient vector is parallel to the chosen singleton direction.

After excluding the six forced nonzero cycles, exactly

```text
87
```

of the 105 no-root cycles satisfy this condition. Therefore the complete zero-column search has only

```text
C(87,2)=3741
```

unordered pairs.

No projective or finite-field heuristic is used below. Complete-block ranks and coefficient row spaces are computed exactly over `Q` using the existing rational row-space machinery.

## 4. Exact source-deficiency census

For each of the 3741 zero-column pairs, append the pair to the six forced nonzero coordinates, form the fixed rank-two coefficient plane, and construct the virtual canonical complete set:

```text
block b is empty  iff  E_b <= P,
block b is complete otherwise.
```

The exact complete-block deficiency histogram is

```text
d_8=3:    3
d_8=4:  315
d_8=5: 2982
d_8=6:  441
```

so only three zero-column pairs can even have the required Profile B source deficiency `d_8=3`.

For the fixed directions above, each pair-union four-set has one omitted orientation, namely the unique common cycle killed at both corresponding rank-two singleton blocks. Write these three cycles as

```text
z_12 = (1,3,2,4),
z_13 = (1,3,2,5),
z_23 = (1,4,2,5).
```

The three source-deficiency-three pairs are exactly

```text
{z_12,z_13},
{z_12,z_23},
{z_13,z_23}.
```

For all three candidates the virtual canonical complete root blocks are the same nine triples:

```text
123,124,125,
134,135,145,
234,235,245.
```

This already reduces the exceptional source to three explicit states.

## 5. Every one of the three states violates the two-puncture theorem

Consider a source candidate containing two of `z_12,z_13,z_23`. Exactly one omitted orientation `z_ij` is absent from the source.

Delete the two nonzero coordinates in packet `ij`.

For example, if the source zero columns are `{z_12,z_13}`, then `z_23` is the missing omitted orientation. Delete the two packet-23 coordinates

```text
(1,2,4,5), (1,2,5,4).
```

The projected coefficient plane still has rank two, but the exact virtual canonical deficiency is

```text
d_6=2.
```

The other two candidates behave cyclically:

```text
zeros {z_12,z_23}: delete packet 13 -> d_6=2,
zeros {z_13,z_23}: delete packet 12 -> d_6=2.
```

This is impossible. Since the source has `d_1(P)>=4`, all eight coordinates are three-clean. The committed all-clean-fans theorem therefore requires every two-coordinate source puncture to have

```text
rank(P_6)=2,
d_6=3.
```

Each of the only three source-deficiency-three exceptional candidates instead has an explicit rank-preserving two-coordinate puncture with `d_6=2`.

Therefore the three-rank-two exception is empty.

## 6. Consequence for the remaining Profile B

The previous projective-column argument gave at most two rank-two singleton blocks except for the unique three-rank-two exception closed here. Hence the exception is gone and the universal bound is now

```text
number of rank-two singleton blocks <= 2.
```

Profile B has nine singleton changed blocks, so every remaining source has

```text
aligned singleton blocks >= 7.
```

The pure dependency space still has dimension three, so at least three changed blocks are dependency-active. With at most two rank-two singleton blocks, at least one dependency-active block is aligned in every remaining source, with touch count three or four. The prior sharpening already proves that touch count three forces its designated three-coordinate puncture to have `d_5=2`.

Thus the remaining branch has no exceptional coefficient geometry. It is now uniformly:

```text
at least seven aligned singleton blocks,
at least one dependency-active aligned singleton block,
active aligned touch count in {3,4},
touch count 3 => a specified d_5=2 puncture.
```

The next bottleneck is the all-active-aligned-touch-four subcase, together with the source-level finite filter for the touch-three alternative. Profile B, Target C-II, and Erdős Problem #99 are not yet closed.
