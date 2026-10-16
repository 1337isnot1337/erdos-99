<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "66f28b870cab85219282dc5d243bf04e5d0a17b1", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_two_touch3_forcing_2026-09-23.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "02dd78d15e604e4bebffab41edb57aa7d956c4831c1ce5aac72c2e571d47b281"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: force two distinct Profile B touch-three kernel witnesses

Date: 2026-09-23

Status: rigorous strengthening of the sole remaining eight-no-root `k=6,D=-1,p=9` Profile B. The previous two-rank-two closure proves that every genuine source has at most one rank-two local-empty singleton block, hence at least eight aligned singleton blocks. The touch-four-alternative closure proves that at least one dependency-active aligned block has source touch count three. This note closes every branch in which that touch-three block is unique.

Consequently every genuine remaining Profile B source has at least two distinct dependency-active aligned touch-three blocks. Each supplies a distinct clean triple deletion with `d_5=2` and an exact source-basis kernel split

```text
K_T = E_T direct-sum <q_b>.
```

Profile B and Target C-II are not yet closed.

Companion exact certificate:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_two_touch3_forcing_2026_09_23.py`

## 1. Inputs already proved

Use the following established facts.

```text
rank(P)=2,
d_1(P)>=4,
exactly nine singleton changed blocks,
at most one rank-two local-empty singleton block,
at least eight aligned singleton blocks,
dim W=3,
L=W^perp has dimension 6,
at least three source basis classes are dependency-active,
dependency-active aligned touch count is 3 or 4,
at least one dependency-active aligned touch-three block exists.
```

An aligned local direction star has four no-root cycles. Two distinct aligned stars intersect in at most one cycle. An eight-cycle source therefore contains at most two full aligned touch-four stars.

If `R` is a rank-two singleton block, its nonzero coefficient line `L_R <= P` meets every distinct aligned star in at most one source coordinate.

## 2. If the touch-three witness is unique, only two active profiles are possible

Assume for contradiction that there is exactly one dependency-active aligned touch-three block `b`.

Let

```text
h = number of dependency-active aligned touch-four blocks,
z = 1 if the unique possible rank-two singleton block is dependency-active,
    0 otherwise.
```

Every dependency-active aligned block has touch count three or four. Since at least three of the nine source basis classes are dependency-active,

```text
1+h+z >= 3.                                      (2.1)
```

Also `h<=2` and `z<=1`.

There is one additional global exclusion. A rank-two singleton coefficient line cannot coexist with two aligned touch-four stars. If the two full stars are `S_1,S_2`, then

```text
|S_1 union S_2| >= 7.
```

The coefficient line meets each star in at most one coordinate, and there is at most one source coordinate outside their union. Hence its weight is at most three, contradicting `d_1(P)>=4`.

Therefore a source containing two aligned touch-four blocks has no rank-two singleton block at all.

Combining this with (2.1), the unique-touch-three hypothesis leaves exactly two cases.

### Case A: two active touch-four blocks, no rank-two block

All nine singleton blocks are aligned. Besides the unique active touch-three block `b`, there are exactly two active touch-four blocks `c,d`.

### Case B: one active touch-four block and one active rank-two block

There are exactly eight aligned singleton blocks and one rank-two singleton block `r`. The three active source classes are exactly

```text
b: aligned touch three,
c: aligned touch four,
r: rank two.
```

The remaining six aligned source classes lie in `L`.

Sections 3 and 4 exclude these two cases.

## 3. Exclude Case A

Let `T` be the three source cycles touching `b`, and let `S_c,S_d` be the two full four-stars of `c,d`.

The stars `S_c,S_d` cannot be disjoint. If they were, they would already use all eight source coordinates. The three-set `T` meets each distinct star in at most one coordinate, so it would contain a source coordinate outside their union, impossible.

Thus

```text
|S_c intersect S_d|=1,
|S_c union S_d|=7.
```

To fit into eight source coordinates, `T` must meet `S_c union S_d` in exactly two coordinates and contribute exactly one new coordinate. Since `T` meets each star in at most one coordinate, those two intersections are distinct: one lies in `S_c-S_d`, the other in `S_d-S_c`. In particular all three root triples `b,c,d` are pairwise two-intersecting.

Three distinct three-subsets that pairwise share two vertices have two incidence types up to `S_7`:

```text
123,124,134
```

or

```text
123,124,125.
```

The tetrahedral-face type is impossible. All three pair unions are then the same four-set, while one aligned star of `b` contains only one orientation on that four-set. But `T` requires two distinct intersections, one with `S_c` and one with `S_d`.

Hence the only geometry is, up to `S_7`,

```text
b=123,
c=124,
d=125.                                         (3.1)
```

The exact certificate enumerates all local direction choices and the omitted member of the touch-three star. Exactly two labeled source cycle sets survive; they are exchanged by `6<->7`. For each source cycle set the certificate then considers every incomplete-block pattern induced by an arbitrary rank-two coefficient plane `P`, without imposing `d_1(P)>=4`.

This incidence enumeration is exhaustive. For each touched block let `E_x` be its local empty space.

- If `dim E_x=2` and `x` is incomplete, then `P=E_x`.
- If two distinct rank-one local empty lines are incomplete, they determine `P` as their span.
- If exactly one rank-one local line class is contained in `P`, a generic rational plane through that line realizes precisely that line class.
- A generic rational rank-two plane can contain none of the finitely many local empty spaces.

Thus it is enough to test every local rank-two empty plane, every span of two distinct local rank-one lines, every one-line generic incidence class, and the no-line generic class.

Each of the two normalized source sets has exactly 90 such incidence patterns. Their exact virtual-canonical deficiency histogram is

```text
d_8=6: 76
d_8=7: 13
d_8=8:  1.
```

There is no `d_8=3` pattern, even before the coefficient minimum-distance condition or the nine chosen-block completeness conditions are imposed. Hence Case A is impossible.

## 4. Exclude Case B

Let `T` again be the three source touches of `b`, let `S` be the full touch-four star of `c`, and let `L_r<=P` be the nonzero coefficient line supplied by the rank-two singleton block `r`.

The line-star bound gives

```text
|supp(L_r) intersect T| <= 1,
|supp(L_r) intersect S| <= 1.                    (4.1)
```

If `T` and `S` were disjoint, their union would contain seven source coordinates, leaving only one outside coordinate. Equation (4.1) would give `wt(L_r)<=3`, contradicting `d_1(P)>=4`.

Therefore

```text
|T intersect S|=1.                               (4.2)
```

Now `|T union S|=6`, so two source coordinates lie outside the union. To reach weight at least four under (4.1), all inequalities are forced to equality in the only possible way:

```text
wt(L_r)=4,
exactly one support coordinate lies in T-S,
exactly one support coordinate lies in S-T,
both coordinates outside T union S lie in supp(L_r),
the shared coordinate T intersect S is not in supp(L_r). (4.3)
```

The shared coordinate in (4.2) shows that `b,c` share two root vertices. The support coordinate in `T-S` touches both `b,r`, and the support coordinate in `S-T` touches both `c,r`. Thus `b,c,r` are pairwise two-intersecting root triples.

Again the tetrahedral-face type is impossible. In that type the shared `b,c` coordinate is the unique member of the aligned star `S` on the common four-set, but (4.3) requires a distinct member of `S` touching both `c,r`.

Hence, up to `S_7`,

```text
b=123,
c=124,
r=125.                                           (4.4)
```

The exact certificate enumerates every local direction choice, every omitted touch-three star member, and every pair of outside cycles consistent with (4.3), exact touch counts, and rank-two local empty space at `r`. After deduplication there are exactly

```text
44
```

normalized `(source cycle set, rank-two local direction)` cases.

For each case it then enumerates every incomplete-block incidence pattern induced by an arbitrary rank-two plane `P` containing the forced line `L_r`. Again the enumeration is exhaustive: such a plane is either a local rank-two empty plane containing `L_r`, the span of `L_r` with some independent local rank-one empty line, or a generic plane through `L_r` containing no additional local empty line.

The number of incidence patterns per normalized case is distributed as

```text
10 patterns: 12 cases
11 patterns:  8 cases
12 patterns: 20 cases
13 patterns:  4 cases.
```

Across all 500 incidence patterns, the exact virtual-canonical deficiency histogram is

```text
d_8=6: 164
d_8=7: 308
d_8=8:  28.
```

There is no `d_8=3` pattern. This is again a strict superset census: it does not impose `d_1(P)>=4`, does not require the chosen aligned blocks to remain complete, and does not require the nine chosen source classes to realize the source basis. Therefore Case B is impossible.

## 5. Consequence: at least two distinguished touch-three punctures

Cases A and B exhaust the hypothesis that there is exactly one dependency-active aligned touch-three block. Both are impossible.

Every genuine remaining Profile B source therefore contains at least two distinct dependency-active aligned touch-three singleton blocks.

By the previously proved touch-three kernel witness theorem, each such block `b=q_j` with touch set `T` gives

```text
d_5(T)=2,
K_T = E_T direct-sum <q_j>.
```

Distinct aligned touch-three blocks have distinct touch triples, and their aligned stars intersect in at most one cycle. Thus the remaining source has at least two distinct distinguished `d_5=2` triple punctures `T,U` satisfying

```text
|T intersect U| <= 1,
K_T = E_T direct-sum <q_b>,
K_U = E_U direct-sum <q_c>.
```

The next bottleneck is the interaction of these two coordinate-split four-dimensional puncture kernels inside the same nine-dimensional source basis and six-dimensional external space `L`. A direct double-witness kernel-lattice filter is now strictly stronger than the previous single-witness audit.

## 6. Computational status

The finite counts in Sections 3 and 4 were independently reproduced offline from the repository's exact K8 four-cycle normal form using rational row-space arithmetic. The reconstruction regenerates the 210 global four-cycle rows, 105 no-root cycles, 35 root blocks, local quotient components, complete-block `T` rows, local empty spaces, and exact complete-set dependency ranks.

The Case A census checks a superset of all rank-two coefficient planes through local-space incidence classes. The Case B census checks a superset of all rank-two coefficient planes containing the forced rank-two singleton line. Therefore the zero `d_8=3` result is a rigorous finite exclusion if the companion verifier reproduces these deterministic counts.

No GitHub Actions or external CI result is used.
