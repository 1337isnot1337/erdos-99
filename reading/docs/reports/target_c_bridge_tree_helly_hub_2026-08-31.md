> Generated reading edition · [exact source](../../../docs/reports/target_c_bridge_tree_helly_hub_2026-08-31.md) · source SHA-256 `ad4da114952fba42685d5deb80555a6320f15cd81289e3eeaa1ca071f995f040`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-92EB3BC86337","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: a Helly hub for all positive diameter paths

**Date:** 2026-08-31  
**Repository branch:** `research/target-c-two-terminal-collapse-2026-08-31`  
**Run type:** proof / articulation and diameter-flow reduction  
**Target:** C-II  
**Depends on:** positive-support connectivity, the planar diameter-thrackle fact, the audited noncrossing-partition lemma, C20, and C22  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The positive contact bridge tree has substantially more structure than an arbitrary
loaded tree.

For every positive diameter edge, join its two endpoint blocks by the unique path in
the positive-contact bridge-block tree.  Any two such tree paths intersect.  Since
subtrees of a tree have the Helly property, **all positive diameter paths pass through
one common bridge block**.

This gives a canonical articulation hub for each normalized KKT stress.  Every branch
away from the hub contains no positive diameter edge internally: all positive diameter
load incident to that branch leaves the branch and routes through the hub in the
bridge-tree sense.

The result converts the bridge stress system into an exact scalar endpoint-mass flow
on a rooted tree, with the vector bridge force equal to the corresponding positive
diameter resultant.

---

## 1. Bridge-block tree and terminal paths

Fix a normalized KKT stress `(alpha,beta)`.  Let `G_+=(V(C_+),C_+)` be its unique
nontrivial positive-contact component and let `B_+=V(H_+)` be its positive diameter
reaction vertices.

Delete every bridge of `G_+` and contract each remaining connected component to one
node.  The result is the bridge-block tree

```math
T=T_{br}.
\tag{C23.1}
```

For `b in B_+`, write `tau(b)` for the node of `T` containing `b`.

For every positive diameter edge

```math
h=bk\in H_+,
```
let

```math
P_h
\tag{C23.2}
```

be the unique tree path in `T` from `tau(b)` to `tau(k)`.  A path is allowed to have
length zero when both endpoints lie in one bridge block.

---

## 2. Positive diameter paths are pairwise intersecting

### Lemma C23.1

For any `h_1,h_2 in H_+`,

```math
\boxed{P_{h_1}\cap P_{h_2}\ne\varnothing.}
\tag{C23.3}
```

#### Proof

If `h_1` and `h_2` share a positive diameter endpoint, their tree paths both contain
the bridge block of that endpoint.

Assume therefore that

```math
h_1=ac,
\qquad
h_2=bd
\tag{C23.4}
```

have four distinct endpoints.  Every point of `B_+` is a vertex of the convex force
hull `F`.  The classical planar diameter-graph theorem says that straight diameter
edges form a geometric thrackle: two disjoint diameter edges cross.  Thus the chords
`ac` and `bd` cross in the interior of `F`; equivalently their four endpoints occur in
alternating cyclic order on the boundary of `F`.

Suppose for contradiction that `P_{ac}` and `P_{bd}` were vertex-disjoint in `T`.
Expand each tree path back to the union of its bridge blocks and intervening contact
bridges.  The two expanded subgraphs of `G_+` are vertex-disjoint.  Each contains a
simple positive-contact path joining the corresponding pair of boundary vertices.

But `G_+` is a plane straight-line graph, while `a,b,c,d` are alternating boundary
vertices of the convex polygon `F`.  The audited noncrossing-partition lemma used in
the Target C support-connectivity theorem says that two vertex-disjoint plane paths
cannot join two alternating boundary pairs.  This is a contradiction.

Hence the two tree paths intersect. `\square`

The proof uses the special diameter geometry only to obtain alternating boundary
pairs.  It does not assert that arbitrary terminal pairs in a plane network have this
property.

---

## 3. Tree Helly gives one common diameter hub

Finite families of connected subgraphs of a tree have the Helly property: if every
two members intersect, then all members have a common vertex.  Applied to the paths
`P_h`, Lemma C23.1 gives the main theorem.

### Theorem C23 (positive-diameter Helly hub)

There exists a bridge block

```math
\boxed{X_*\in V(T)}
\tag{C23.5}
```

such that

```math
\boxed{
X_*\in P_h
\qquad\text{for every }h\in H_+.
}
\tag{C23.6}
```

Equivalently, every positive diameter pair is routed through one common node of the
positive-contact bridge-block tree.

#### Proof

By Lemma C23.1 the finite family of tree paths

```math
\{P_h:h\in H_+\}
```

is pairwise intersecting.  The tree-Helly property gives a common vertex `X_*`.
`\square`

The common intersection may contain more than one tree node; the theorem only needs
one choice of hub.

---

## 4. Every branch away from the hub is diameter-edge-free internally

Root `T` at `X_*`.  Let `U` be any connected component of

```math
T-X_*.
```

### Corollary C23.2

No positive diameter edge has both endpoint blocks in `U`.

#### Proof

If `h=bk` had both `tau(b),tau(k) in U`, the unique tree path `P_h` would be contained
entirely in `U` and would not contain `X_*`, contradicting C23.6. `\square`

The same statement holds below every rooted bridge edge.  If `e` is a bridge of `T`
and `T_e` is the descendant component of `T-e` not containing `X_*`, then no positive
diameter edge has both endpoints in `T_e`.

Thus a branch can contain many positive diameter endpoints, but every positive diameter
edge incident to any of them exits that branch.

---

## 5. Exact scalar endpoint flow on the rooted bridge tree

Let `e=uv` be a positive contact bridge, oriented so that its descendant side `S_e`
does not contain the hub `X_*`.  Let

```math
B_e:=B_+\cap S_e.
\tag{C23.7}
```

For each loaded vertex put

```math
s_b:=\sum_{bk\in H_+}\beta_{bk}.
\tag{C23.8}
```

Define the scalar endpoint mass below `e` by

```math
\boxed{
w_e:=\sum_{b\in B_e}s_b.}
\tag{C23.9}
```

By Corollary C23.2 there is no positive diameter edge internal to `B_e`.  Therefore
every positive diameter incidence counted by `w_e` crosses the bridge cut exactly once.
Hence

```math
\boxed{
w_e
=
\sum_{\substack{bk\in H_+\\b\in B_e,\ k\notin B_e}}
\beta_{bk}.}
\tag{C23.10}
```

Combining this with the diameter-cut flow identity C22.5 gives

```math
\boxed{
\alpha_e(u-v)
=
\sum_{\substack{bk\in H_+\\b\in B_e,\ k\notin B_e}}
\beta_{bk}(b-k),
}
\tag{C23.11}
```

and therefore

```math
\boxed{
\alpha_e\le D w_e.
}
\tag{C23.12}
```

The scalar quantities `w_e` behave as an ordinary nonnegative rooted-tree flow.  At a
reaction-free non-root branch node the incoming endpoint mass is the sum of the
outgoing endpoint masses.  At a non-root block containing loaded vertices, the
incoming/outgoing difference is exactly the sum of their `s_b` masses.

Since

```math
\sum_{b\in B_+}s_b
=2\sum_{h\in H_+}\beta_h
=2,
\tag{C23.13}
```

any antichain of rooted bridge edges satisfies

```math
\boxed{
\sum_{e\in\mathcal A}w_e\le2.
}
\tag{C23.14}
```

Equation C23.12 then recovers the `2D` bridge-frontier stress bound, now as a direct
corollary of a scalar terminal-mass flow:

```math
\sum_{e\in\mathcal A}\alpha_e\le2D.
\tag{C23.15}
```

C20 is stronger in that it obtains the stress frontier bound directly from reciprocal
perimeter and does not need the hub theorem.  The point here is the new rooted-flow
interpretation.

---

## 6. Weighted bridge depth is forced by bridge stress

Let `d_T(tau(b),X_*)` be the number of contact bridges between the block of `b` and the
hub.  Summing C23.9 over every rooted bridge edge gives the exact layer-cake identity

```math
\boxed{
\sum_{e\in E(T)}w_e
=
\sum_{b\in B_+}s_b\,d_T(\tau(b),X_*).
}
\tag{C23.16}
```

Indeed a fixed endpoint mass `s_b` is counted once for every bridge on its unique path
to `X_*`.

Let

```math
S_{br}:=\sum_{e\text{ bridge of }G_+}\alpha_e.
\tag{C23.17}
```

Then C23.12 and C23.16 give

```math
\boxed{
S_{br}
\le
D\sum_{b\in B_+}s_b\,d_T(\tau(b),X_*).
}
\tag{C23.18}
```

Consequently, if

```math
S_{br}\ge\eta D^2,
\tag{C23.19}
```

then

```math
\boxed{
\sum_{b\in B_+}s_b\,d_T(\tau(b),X_*)
\ge\eta D.
}
\tag{C23.20}
```

Since the total `s_b` mass is two, the `s_b/2`-weighted mean bridge depth of the
positive diameter endpoints is at least

```math
\boxed{
\frac{\eta D}{2}.
}
\tag{C23.21}
```

Thus bridge-dominant stress forces the positive-diameter endpoint incidence measure to
have mean bridge depth `Omega(D)` from the common hub.  This is stronger than merely
recording the unweighted depth of one tree arm, but it does **not** imply that a fixed
positive fraction of the endpoint mass lies at depth `Omega(D)`; a sufficiently small
mass could lie much deeper.  Any later use of C23.21 must retain that distinction.

---

## 7. Combination with C22

C22 says that every reaction-free degree-two bridge block collapses to a single neutral
vertex and every nontrivial reaction-free block has bridge-tree degree at least three.
C23 now roots that entire articulation structure at one block common to all positive
diameter paths.

Therefore every branch away from `X_*` has the following exact form:

1. it contains no positive diameter edge internally;
2. all positive diameter incidence carried by the branch exits toward another branch
   or the hub;
3. its scalar endpoint mass flows monotonically toward the hub;
4. between loaded or branching blocks, the contact bridges form exact straight
   constant-stress unit corridors; and
5. any nontrivial reaction-free two-dimensional block has total bridge-tree degree at
   least three; away from the hub this means at least two loaded descendant branches.

This is a stricter C-II normal form than the previous unrooted bridge-tree picture.

---

## 8. What is still missing

C23 does not itself bound the number of loaded endpoints by `o(D)`, nor does it give a
uniform lower bound on the individual `s_b`, `beta_h`, or bridge stresses.  The
following configuration pattern is therefore not yet excluded abstractly:

- `Theta(D)` loaded boundary vertices, each carrying `Theta(1/D)` endpoint mass;
- `Theta(D)` rooted branches of bridge depth `Theta(D)` after recursive branching;
- small force changes at many loaded/branching events; and
- total bridge stress of order `D^2`.

That is the exact surviving bridge regression.

The next useful theorem should exploit the **geometric** fact that all diameter edges
whose tree paths route through `X_*` are actual diameter chords of one convex force
hull, with the explicit shared-endpoint angle gap and diameter-cycle girth.  Pure tree
flow cannot exclude the displayed pattern.

A plausible exact target is:

> **Hub transport cost theorem.**  In a sufficiently large global minimizer, a rooted
> Target C bridge tree satisfying C22-C23 cannot have `s_b/2`-weighted mean depth
> `Omega(D)` unless either a branch contains an `Omega(D)` straight corridor or the
> positive diameter chords force a forbidden global angle/cycle/packing configuration.

C23 reduces the bridge problem to that statement.  The two-edge-connected stress-bulk
branch remains separate.

---

## 9. Regression audit

- **Matching diameter phase:** allowed.  Many pairwise crossing diameter chords can all
  route through one central bridge block.
- **Odd diameter cycle:** allowed.  Its tree paths have a common hub; C17 still only
  forces the cycle length to grow.
- **Y-shaped contact tree:** allowed and illustrates a reaction-free branching hub.
- **Straight chain:** its bridge tree itself is a path; if all positive diameter paths
  traverse the same central segment, C23 is automatic.  The whole-source one-dimensional
  phase remains excluded separately by C19.
- **Bridge-free positive contact graph:** `T` has one node, which is trivially the hub;
  C23 adds nothing to the two-edge-connected stress-bulk branch.
- **KKT-invisible source points:** absent from the positive bridge tree and untouched.

No lower bound on individual KKT weights and no generic rigidity or PSD statement is
used.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Theorem C23 (positive-diameter Helly hub):
Contract the positive contact graph along its bridges to a tree T.  For each positive
diameter edge h=bk, let P_h be the T-path between the blocks containing b and k.
Any two P_h intersect:
- shared diameter endpoint => shared terminal block;
- disjoint diameter edges cross as geometric-thrackle chords, so their endpoints
  alternate on the convex force-hull boundary; two vertex-disjoint plane contact paths
  cannot connect alternating boundary pairs.
Tree paths have the Helly property, hence all P_h contain one common bridge block X_*.

Consequences after rooting T at X_*:
- no positive diameter edge lies internally in any branch of T-X_*;
- for a descendant bridge e, w_e=sum_{b below e}s_b equals exactly the beta-mass of
  positive diameter edges crossing that cut;
- alpha_e(u-v) is the vector resultant of those crossing diameter chords and
  alpha_e<=D w_e;
- sum_e w_e=sum_b s_b d_T(tau(b),X_*).
Thus S_bridge>=eta D^2 forces s_b/2-weighted mean endpoint depth >=eta D/2, but does
not by itself force a fixed positive mass fraction to be deep.

Combined C22-C23 bridge normal form:
one common diameter-routing hub, no internal diameter edges inside a branch,
reaction-free two-terminal regions collapse to straight chains, and every remaining
reaction-free 2D event has bridge-tree degree at least three (at least two loaded
children away from the hub).

Remaining exact bridge problem:
exclude Omega(D) weighted hub depth using the actual diameter-chord geometry, not pure
tree flow.  Linear many tiny endpoint weights remain a live regression.
```
