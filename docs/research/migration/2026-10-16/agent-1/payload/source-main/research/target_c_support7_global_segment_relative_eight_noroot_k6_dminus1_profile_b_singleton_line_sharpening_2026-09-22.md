# Target C: sharpen Profile B singleton-line intersections

Date: 2026-09-22

Status: rigorous strengthening of the remaining eight-no-root `k=6,D=-1,p=9` Profile B. The preceding singleton-line note bounded pairwise coefficient-line support intersections by three. The local singleton direction removes one of the three common four-cycle orientations, so the correct bound is two. This reduces the number of rank-two local-empty singleton blocks to at most three globally, with three possible only for the unique coefficient-column profile `d_2(P)=6`, projective multiplicities `(2,2,2)`. Consequently every Profile B source has at least six aligned singleton blocks, and every nonexceptional source has at least seven. This does not close Profile B or Target C-II.

Companion arithmetic certificate:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_singleton_line_geometry_2026_09_22.py`

The inputs are the already-proved source facts

```text
rank(P)=2,
d_1(P)>=4,
```

and the exact local root-block geometry:

1. a root block is a three-subset of `{1,...,7}`;
2. two distinct root blocks are touched by a common no-root four-cycle iff the triples share two vertices;
3. in that case their union is a four-set and the only common no-root cycles are its three orientations; and
4. at either root block those three orientations occupy the three different local projective directions, one each.

The preceding note is

`research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_singleton_line_geometry_2026-09-22.md`.

## 1. Rank-two singleton coefficient lines omit one common orientation

Let `b` be a compatible singleton block with rank-two empty local coefficient space. Its chosen singleton state has one local projective direction `s_b`, and its nonzero coefficient line

```text
L_b <= P
```

has the following support rule:

```text
coordinate e belongs to supp(L_b)
iff
e touches b and the local quotient direction of e at b is not s_b.
```

Now let `b,c` be distinct rank-two singleton blocks.

If their root triples do not share two vertices, no no-root cycle touches both, so

```text
supp(L_b) intersect supp(L_c) = empty.
```

Suppose instead that the triples share two vertices. Exactly three global no-root cycles touch both blocks: the three four-cycle orientations on their common four-set. At `b` those three cycles have the three different local projective directions. Exactly one of them therefore has direction `s_b`, so that cycle is absent from `supp(L_b)`.

Hence `L_b` is supported on at most two of the three cycles that can possibly touch both blocks. Intersecting with `supp(L_c)` cannot increase this number. Therefore

```text
|supp(L_b) intersect supp(L_c)| <= 2.              (1.1)
```

This is a strict improvement over the previous bound `<=3`.

It also immediately re-proves that distinct rank-two singleton blocks give distinct coefficient lines: if `L_b=L_c`, their common support would have size at least `d_1(P)>=4`, contradicting (1.1).

## 2. Projective-column consequence

Choose a `2 x 8` generator matrix for `P`. Let

```text
z = number of zero coordinate columns,
n = 8-z = d_2(P),
```

and let

```text
m_1,...,m_h
```

be the multiplicities of the distinct nonzero projective column classes. Then

```text
sum_i m_i = n,
max_i m_i <= n-4
```

because

```text
d_1(P)=n-max_i m_i >=4.
```

A nonzero codeword line whose kernel direction is projective class `i` has support size

```text
n-m_i.
```

For two such distinct classes `i,j`, the two supports intersect in exactly

```text
n-m_i-m_j.
```

Combining this with (1.1) gives the stronger pair inequality

```text
m_i+m_j >= n-2.                                  (2.1)
```

A generic codeword line, whose kernel direction is absent from the column configuration, has support all `n` nonzero columns. Its intersection with any other nonzero codeword support has size at least `d_1(P)>=4`, so a generic line cannot coexist with a second rank-two singleton coefficient line.

Thus whenever there are at least two rank-two singleton blocks, their coefficient lines come from distinct actual projective column classes satisfying (2.1).

## 3. Exact count by `d_2(P)`

The arithmetic is now small enough to do by hand.

### `n=5`

The minimum-distance condition forces every nonzero projective class to have multiplicity one:

```text
(m_i)=(1,1,1,1,1).
```

But two used classes would have

```text
m_i+m_j=2 < n-2=3.
```

Therefore at most one singleton block can have rank-two local empty space.

### `n=6`

Every multiplicity is at most two, and two used classes must satisfy

```text
m_i+m_j>=4.
```

Hence every class used by a rank-two singleton line must have multiplicity two. There can be at most three such classes. Equality occurs only for

```text
(m_i)=(2,2,2),
z=2,
d_1(P)=4.                                         (3.1)
```

### `n=7`

Every multiplicity is at most three. If three classes were used, write their multiplicities in increasing order

```text
a<=b<=c.
```

The pair condition gives `a+b>=5`. Since `a<=b<=3`, either `a=1`, which would force `b>=4` and is impossible, or `a>=2`, which forces `b,c>=3` and hence

```text
a+b+c >= 2+3+3 = 8 > 7.
```

Therefore at most two rank-two singleton blocks exist.

### `n=8`

Every multiplicity is at most four. If three classes were used, again write `a<=b<=c`. The pair condition is

```text
a+b>=6.
```

If `a<=2`, then `b,c>=4`, so the total is at least ten. If `a=3`, all three are at least three, so the total is at least nine. If `a=4`, the total is at least twelve. Every case exceeds eight.

Therefore at most two rank-two singleton blocks exist.

The companion script exhausts every integer projective multiplicity profile with `d_1>=4` and independently checks exactly

```text
max rank-two singleton blocks by d_2:

d_2=5: 1
d_2=6: 3
d_2=7: 2
d_2=8: 2.
```

Moreover, the only profile allowing three is (3.1).

## 4. Geometry of the unique three-rank-two exception

Suppose three rank-two singleton blocks occur. Section 3 forces

```text
d_2(P)=6,
(m_i)=(2,2,2).
```

Call the three coefficient lines `L_1,L_2,L_3`. Each has weight four. Their pairwise support intersections are the three projective column classes, each of size two. In particular:

```text
|supp(L_i) intersect supp(L_j)|=2
```

for every pair, and the three pairwise intersections are mutually disjoint.

Since each pair has nonempty support intersection, the corresponding root triples must pairwise share two vertices. Up to `S_7`, three distinct triples with pairwise two-vertex intersection have two forms:

```text
123,124,134
```

(three faces of one four-set), or

```text
123,124,125
```

(a common two-set with three distinct third vertices).

The first form is impossible. All three block pairs are then co-touched only by the same three four-cycle orientations on `1234`. But the three pairwise coefficient-support intersections must be disjoint two-element sets. Three disjoint two-element subsets cannot all lie inside the same three-element orientation set.

Therefore the only possible three-rank-two root-block geometry is

```text
123,124,125
```

up to relabeling. The three two-element coefficient-support intersections lie on the three distinct four-sets

```text
1234,
1235,
1245,
```

respectively. Thus the six nonzero coefficient coordinates split into three disjoint two-cycle packets, one packet for each pair of rank-two singleton blocks. The remaining two source coordinates are precisely the two zero columns of `P`.

This does not exclude the exceptional configuration, but it replaces an unrestricted three-block possibility by one exact root-block incidence type and one exact projective multiplicity profile.

## 5. Consequence for the nine singleton blocks

Profile B has exactly nine actual singleton changed blocks. Every one is either aligned rank one or rank-two local-empty. The count above gives

```text
d_2=5:  aligned blocks >=8;
d_2=6:  aligned blocks >=6;
d_2=7:  aligned blocks >=7;
d_2=8:  aligned blocks >=7.
```

Therefore every genuine Profile B source has at least six aligned singleton blocks.

The only way to have fewer than seven aligned blocks is the exceptional case

```text
d_2(P)=6,
z=2,
projective multiplicities=(2,2,2),
three rank-two singleton blocks in common-two-set geometry.
```

Outside that case at most two singleton blocks are rank two, so at least seven are aligned.

This supersedes the weaker earlier dichotomy that allowed up to five rank-two singleton blocks when `d_2=5`.

## 6. Bridge to the pure-dependency space

Reuse the source dependency-dual notation from the external-kernel note:

```text
W <= Q^C,
dim W=3,
L=W^perp <= V.
```

The nine actual singleton replacement classes form a basis of `V`. Their restrictions to `W` span `W^*`, so at least three of the nine changed blocks are dependency-active, meaning the corresponding coordinate functional on `W` is nonzero.

A dependency-active block cannot disappear in any rank-preserving descendant whose virtual deficiency remains three. Indeed the source pure dependency space `W` is contained in every such descendant dependency space; if block `b` ceased to be virtual-complete there, the embedded descendant dependency vectors would have zero `b` coordinate, forcing every vector of `W` to have zero `b` coordinate.

All one- and two-coordinate punctures of the source preserve coefficient rank and have deficiency three. Therefore every dependency-active aligned block is touched by at least three source cycles. Alignment bounds the touch count by four, so

```text
dependency-active aligned block => touch count in {3,4}.   (6.1)
```

In every nonexceptional source there are at most two rank-two singleton blocks, while at least three changed blocks are dependency-active. Hence:

> every nonexceptional Profile B source has at least one dependency-active aligned singleton block.

There is one further sharp consequence. Let such a block `b` have exactly three touching coordinates, and delete precisely those three coordinates. The coefficient rank remains two because `d_1(P)>=4`. The block becomes untouched and therefore disappears from the punctured virtual-complete set. If that five-row descendant still had deficiency three, the preceding persistence argument would force `b` to remain present, a contradiction. Hence

```text
active aligned block with exactly 3 touches
=> its three-coordinate puncture has d_5=2.                (6.2)
```

Thus every nonexceptional source is forced into one of two narrower subcases:

1. it has a dependency-active aligned block of touch size three, which identifies a specific `d_5=2` clean triple puncture; or
2. every dependency-active aligned block has touch size four.

The exceptional `d_2=6,(2,2,2)` source remains separate because its three dependency-active blocks could, in principle, be exactly the three rank-two singleton blocks.

## 7. Remaining bottleneck

The remaining Profile B audit can now be split before any heavy descendant construction:

1. exceptional coefficient geometry: `d_2=6`, multiplicities `(2,2,2)`, with the three rank-two singleton blocks in common-two-set geometry;
2. nonexceptional geometry: at least seven aligned singleton blocks and at least one dependency-active aligned block satisfying (6.1), with the touch-three subcase forcing a specific `d_5=2` puncture by (6.2).

The next high-value finite filter is to impose this split directly on the source candidates before the fixed-nine/kernel-lattice fan. A zero-survivor result there would close Profile B; until then no closure is claimed.
