> Generated reading edition · [exact source](../../../docs/reports/target_c_negative_transfer_unbounded_forest_split_regression_2026-09-11.md) · source SHA-256 `297f61e6a5742863c27cc1691c373b8f3742c139ee3098e87dd086c1ebe0e980`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-6AC0F2EA4A29","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Unbounded negative-split support in the Woodall forest class

**Status:** regression (proved finite geometric/combinatorial obstruction; not a
global-minimality construction)

**Date:** 2026-09-11

## Purpose

The strict-negative response branch has the following tempting possible
closure: a negative transfer between the extreme diameter edges might force a
positive circular interval split with only two crossed diameter edges (or with
support bounded by an absolute constant).  Such a statement would reduce the
remaining branch to the already understood terminal normal forms.

This report gives an exact counterexample even in the forest side of the
actual-diameter topology.  It therefore rules out any proof that uses only
the following data: convex-thrackle order, the Woodall caterpillar-forest
classification, and the sign change of one circular interval split.  It does
not assert that the examples are global minimum-diameter configurations, and
it does not challenge the C53 response identities.

## The family

For every integer `n >= 5`, let the loaded vertices be ordered

```text
0,1,...,n-1
```

and define

```text
H_n = { (0,i) : 1 <= i <= n-2 } union { (1,n-1) }.
```

This graph has `n-1` edges and is a tree.  Its degree sequence is

```text
deg(0)=n-2,  deg(1)=2,  deg(n-1)=1,
deg(i)=1 for 2 <= i <= n-2.
```

Consequently it is a one-component caterpillar forest, with

```text
q=n,  h=n-1,  d_H=q-h=1.
```

Put the vertices in convex position in the displayed order.  Every pair of
star edges meets at vertex `0`.  The edge `(1,n-1)` meets `(0,1)` at a vertex,
and crosses every `(0,i)` with `2 <= i <= n-2`, since their endpoint order is
`0 < 1 < i < n-1`.  Thus `H_n` is a straight-line convex thrackle and is
exactly of the forest topology permitted by the Woodall classification.

## The interval split

Use the legal orientation from the displayed cyclic order and take the proper
circular interval

```text
A_n={1,2,...,n-2}.
```

For an oriented edge, write `z_e=+1` when its head is in `A_n` and its tail is
outside, `z_e=-1` for the reverse crossing, and `z_e=0` otherwise.  Then

```text
z_(0,1)=+1,
z_(1,n-1)=-1,
z_(0,i)=+1  (2 <= i <= n-2).
```

In particular, the two extreme edges in the projective slope order can be
chosen as `(0,1)` and `(1,n-1)`: for points on the convex parabola
`p_i=(i,i^2)`, their slopes are respectively `1` and `n`, while the star
slopes are `i`.  Hence

```text
z_(0,1) z_(1,n-1) = -1.
```

The split crosses `n-1` diameter edges, namely every edge of `H_n`.  Both
shores induce no edge: `H_n[A_n]` is empty, and the complementary shore
`{0,n-1}` is also edgeless because `(0,n-1)` is deliberately absent.  Thus
the usual shore estimate is attained at an unbounded scale:

```text
|A_n|=n-2,   k(A_n)=n-1.
```

Therefore neither the negative extreme-transfer sign nor the forest/caterpillar
topology implies `k(A)=O(1)`, a two-crossing split, or a bounded-size shore.

## Geometric realization of the diameter graph (optional strengthening)

The obstruction is already combinatorial, but it can also be realized by a
unit-separated finite configuration with this exact diameter graph.  Fix a
large `D` and place one point at the origin and the other `n-1` points on the
circle of radius `D` along an arc of central angle `pi/3`.  Put the two
endpoints of the arc at angular separation `pi/3`, and choose the intermediate
angles strictly between them with consecutive gaps at least

```text
2 asin(1/(2D)).
```

For

```text
n-2 <= (pi/3)/(2 asin(1/(2D))),
```

all pairwise distances are at least one (there are exactly `n-2` consecutive
gaps between the `n-1` arc points).  The origin is at distance `D` from every arc point; the two arc
endpoints are also at distance `D`; all other arc pairs are at distance less
than `D`.  Hence the diameter graph is exactly `H_n` (after naming the origin
`0`, the first arc endpoint `1`, and the last endpoint `n-1`).  Small generic
perturbations of the intermediate angles avoid accidental unit contacts while
preserving the diameter graph and the strict inequalities.

This configuration is not claimed to minimize diameter for its population.
Its role is to show that geometry and the Woodall graph classification alone
cannot supply the missing response bound.

## Consequence for the live C-II proof

Any successful treatment of the strict-negative branch must use information
not present in this regression, such as the actual C53 affine/PSD response
identities together with KKT force visibility, source-population accounting,
or a strict global competitor.  In particular, the already proved statement

```text
K_min<0  =>  some positive interval split has opposite signs on the extreme pair
```

cannot be strengthened to a bounded-crossing normal form without an additional
hypothesis.  The forest charge `3 d_H` is not by itself sufficient: this family
has `d_H=1` while the negative split crosses `n-1` edges.

## What this does not prove

The family does not disprove Erdős Problem #99.  It supplies neither a
triangle-free global minimizer nor a global-optimality certificate, and it does
not realize the full C53 selected-stress response.  It is a regression against
one proposed closure lemma only.
