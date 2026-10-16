<!-- theorem-state: {"artifact_id":"ART-F3439E9157C4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: two-terminal harmonic corridors

**Date:** 2026-08-31  
**Run type:** proof / structural reduction  
**Target:** C-II  
**Depends on:** canonical Target C equilibrium, C20 bridge reciprocals, C21 straight-chain suppression  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

A reaction-free positive-contact region attached to the rest of the stressed network
through at most two contact terminals cannot contain genuine two-dimensional
structure. KKT equilibrium makes every unloaded vertex a positive barycenter of its
neighbors, so a two-terminal region is trapped in the segment joining its terminals
and collapses to a straight series chain.

For the bridge tree this has two consequences. First, after suppressing neutral
straight degree-two nodes, there are only `O(|B_+|)=O(D)` event nodes globally.
Second, along every bridge-tree path the nested reciprocal bridge resultants have total
vector variation at most `P_*<=2D`.

The articulation branch is therefore a bounded-complexity planar force tree whose
large cardinality or stress can be hidden only in long exact straight corridors.
This is a reduction, not a Level I contradiction.

---

## 1. Harmonic convex hull for an unloaded contact domain

Fix a normalized KKT stress. Let `G=C_+` be its connected positive unit-contact graph
and let `B_+` be the positive diameter-reaction vertices. For every
`x notin B_+`, equilibrium is
\[
\sum_{xy\in E(G)}\alpha_{xy}(x-y)=0,
\qquad \alpha_{xy}>0,
\tag{C22.1}
\]
so
\[
x=
\frac{\sum_{xy}\alpha_{xy}y}
     {\sum_{xy}\alpha_{xy}}.
\tag{C22.2}
\]
For a vertex set `U`, write
\[
\partial_GU
=\{w\notin U:\exists u\in U\text{ with }uw\in E(G)\}.
\tag{C22.3}
\]

### Theorem C22.1 (unloaded-domain convex-hull principle)

Let `U` be a nonempty connected vertex set with
\[
U\cap B_+=\varnothing.
\tag{C22.4}
\]
Then `partial_G U` is nonempty and
\[
\boxed{
\{p_u:u\in U\}
\subseteq
\operatorname{conv}\{p_w:w\in\partial_GU\}.
}
\tag{C22.5}
\]

#### Proof

The connected graph `G` contains the nonempty reaction set `B_+`, so a nonempty
reaction-free `U` is proper and has nonempty graph boundary.

Let `ell` be any linear functional and put
\[
M=\max_{u\in U}\ell(p_u).
\]
If
\[
M>\max_{w\in\partial_GU}\ell(p_w),
\tag{C22.6}
\]
choose `u_0` attaining `M`. Equation (C22.2) expresses `ell(p_{u_0})` as a positive
weighted average of its neighbors' values, all at most `M`. Hence every neighbor in
`U` also has value `M` and no boundary neighbor can occur. Propagating through
connected `U` makes every vertex of `U` have value `M`. But some vertex of `U` is
adjacent to `partial_GU`, and applying (C22.2) there forces a boundary neighbor to have
value `M`, contradiction. Thus
\[
\max_U\ell\le\max_{\partial_GU}\ell.
\tag{C22.7}
\]
Apply the same argument to `-ell` and use separation from a compact convex set.
`\square`

### Corollary C22.2 (one- and two-terminal domains)

A connected reaction-free positive-contact domain cannot have one boundary vertex. If
\[
|\partial_GU|=2,
\tag{C22.8}
\]
then every vertex of `U` lies on the segment joining the two boundary vertices, and
the contact graph on `U union partial_GU` is a straight unit-spaced path.

#### Proof

For one boundary vertex, (C22.5) would put every vertex of nonempty `U` at the same
point. For two boundary vertices, (C22.5) puts all points on their joining segment.
Unit separation on a line permits unit contacts only between consecutive unit-spaced
points, so a connected subgraph is a path. `\square`

---

## 2. Degree-two bridge-tree blocks are either loaded or trivial

Delete every bridge of `G`. The remaining connected components are the nodes of the
bridge tree `mathcal T`; a node may be a singleton.

### Theorem C22.3 (no unloaded two-terminal nontrivial block)

Let `K` be a node of `mathcal T` of tree degree two. If
\[
V(K)\cap B_+=\varnothing,
\tag{C22.9}
\]
then `K` is one vertex. That vertex has contact degree two in `G` and is an exact
neutral straight-chain vertex of C21.

#### Proof

Let the two incident bridge edges join `K` to outside vertices `w_-,w_+`. Put
`U=V(K)`. These are the only positive-contact neighbors outside `U`, so
\[
\partial_GU=\{w_-,w_+\}.
\tag{C22.10}
\]
Corollary C22.2 makes the local contact graph on
`U union {w_-,w_+}` a collinear path.

Suppose `K` contained an internal contact edge `e`. Removing `e` separates that local
path into two sides. Any alternate path in the full graph `G-e` between the two sides
would have to leave `K` through one incident bridge and return through the other,
because there is no third edge leaving `K`. But the two outside sides lie in distinct
components of the bridge tree after removing node `K`; such an outside path would
create a cycle in the bridge tree, equivalently would make the incident edges
nonbridges. Therefore no alternate path exists and `e` itself is a bridge of `G`,
contradicting the definition of `K` after all bridges were deleted.

Hence `K` has no internal edge and, being connected as a bridge-tree node, is a
singleton. C21 makes it a neutral straight degree-two vertex. `\square`

### Corollary C22.4 (every bridge-tree leaf is loaded)

Every leaf node of `mathcal T` contains a vertex of `B_+`.

#### Proof

If a leaf node were reaction-free, its vertex set would be a nonempty connected
reaction-free domain with only one outside contact terminal, contradicting
Corollary C22.2. `\square`

---

## 3. Global event count and corridor normal form

Assume the bridge tree has at least one edge. Call a bridge-tree node an **event node**
if it is not a reaction-free singleton of degree two. Let

- `L` be the number of leaves;
- `Q_2` the number of degree-two event nodes;
- `Q_3` the number of nodes of degree at least three.

Corollary C22.4 says every leaf contains a reaction. Theorem C22.3 says every
degree-two event node contains a reaction. These nodes are disjoint, so
\[
\boxed{L+Q_2\le|B_+|.}
\tag{C22.11}
\]
The tree identity gives
\[
L=2+\sum_{\deg K\ge3}(\deg K-2),
\tag{C22.12}
\]
hence
\[
Q_3\le L-2.
\tag{C22.13}
\]

### Theorem C22.5 (global bridge-corridor decomposition)

The total number `Q_evt` of event nodes satisfies
\[
\boxed{
Q_{\rm evt}=L+Q_2+Q_3
\le2|B_+|-2.
}
\tag{C22.14}
\]
After suppressing every non-event node, the bridge tree has at most
`2|B_+|-2` vertices and at most `2|B_+|-3` edges. Each reduced edge corresponds to an
exact straight unit-spaced bridge corridor of constant contact stress. If its corridor
contains `L_E` unit bridges, then
\[
\boxed{L_E\in\mathbb Z_{\ge1},\qquad L_E\le D.}
\tag{C22.15}
\]
Consequently
\[
\boxed{
|E_{\rm bridge}|
\le D(2|B_+|-3)
\le D(2\pi D-3).
}
\tag{C22.16}

#### Proof

Equations (C22.11)--(C22.13) give
\[
Q_{\rm evt}
=(L+Q_2)+Q_3
\le |B_+|+L-2
\le2|B_+|-2.
\]
Every suppressed node is exactly a reaction-free degree-two singleton by definition
and Theorem C22.3. C21 therefore makes every maximal suppressed run a straight
unit-spaced constant-stress chain between its event endpoints. Its number of unit
bridges equals the Euclidean distance between its two attachment points and is at most
the source diameter `D`. Summing over the at most `Q_evt-1` reduced-tree edges gives
the first inequality in (C22.16). Finally the reaction vertices are unit-separated
points on the boundary of the two-dimensional force hull, so
`|B_+|<=per(F)<=pi D`. `\square`

Thus the bridge articulation is globally boundary-order complex. `D^2`-scale
cardinality can still be hidden in `O(D)` long straight corridors, so this is not a
packing contradiction.

---

## 4. Events on one bridge corridor inject into the reaction set

For a simple bridge-tree path
\[
K_0,e_1,K_1,e_2,\ldots,e_m,K_m,
\tag{C22.17}
\]
call an internal node an event if it contains a reaction vertex or has tree degree at
least three. Theorem C22.3 makes every other internal node neutral and straight.

### Theorem C22.6 (path event charging)

If `q` events occur on the path, then
\[
\boxed{q\le|B_+|.}
\tag{C22.18}
\]
The path therefore contains a straight constant-stress run of at least
\[
\boxed{
L_{\rm run}\ge\frac{m}{|B_+|+1}
}
\tag{C22.19}
\]
unit bridges.

#### Proof

Charge a loaded event node to one reaction vertex inside it. For a reaction-free
branching event, choose an off-path bridge. The bridge-side component in that off-path
subtree contains a reaction vertex because its nonzero bridge resultant is the sum of
the reactions on that side (C20). Off-path subtrees chosen at different branching
nodes of one tree path are disjoint, and they are disjoint from loaded nodes on the
path. Thus all charges can be chosen distinct, proving (C22.18).

The `q` event nodes divide the bridge sequence into at most `q+1` event-free subpaths.
Their internal nodes are neutral straight singletons, so C21 makes each subpath an
exact straight constant-stress chain. Their lengths sum to `m`; one has length at
least `m/(q+1)`. `\square`

---

## 5. Nested bridge resultants have bounded total variation

Orient the path (C22.17) toward `K_m`. For bridge `e_i`, let `S_i` be the forward
component of `G-e_i`, let
\[
B_i=B_+\cap S_i,
\qquad
f_i=\sum_{b\in B_i}g_b.
\tag{C22.20}
\]
Then
\[
B_1\supseteq B_2\supseteq\cdots\supseteq B_m,
\tag{C22.21}
\]
and C20 gives
\[
\boxed{|f_i|=\alpha_{e_i}.}
\tag{C22.22}
\]
Up to a fixed quarter-turn, `f_i` is the reciprocal diagonal of the bridge cut.

### Theorem C22.7 (reciprocal-diagonal bounded variation)

Along every simple bridge-tree path,
\[
\boxed{
\sum_{i=1}^{m-1}|f_i-f_{i+1}|
\le
\sum_{b\in B_+}|g_b|
=P_*
\le2D.
}
\tag{C22.23}
\]
Consequently
\[
\sum_{i=1}^{m-1}
|\alpha_{e_i}-\alpha_{e_{i+1}}|
\le2D.
\tag{C22.24}
\]
If every bridge on a subpath has stress at least `a>0`, its bridge-direction unit
vectors `u_i=f_i/|f_i|` satisfy
\[
\boxed{
\sum|u_i-u_{i+1}|
\le\frac{4D}{a}.
}
\tag{C22.25}

#### Proof

The shell sets `B_i\setminus B_{i+1}` are pairwise disjoint. Hence
\[
\begin{aligned}
\sum_i|f_i-f_{i+1}|
&=\sum_i\left|\sum_{b\in B_i\setminus B_{i+1}}g_b\right|\\
&\le\sum_i\sum_{b\in B_i\setminus B_{i+1}}|g_b|\\
&\le P_*\le2D.
\end{aligned}
\]
The reverse triangle inequality gives (C22.24). For nonzero `f,g` with norms at least
`a`,
\[
\left|\frac f{|f|}-\frac g{|g|}\right|
\le\frac{2|f-g|}{a};
\]
summing gives (C22.25). `\square`

Thus high-stress bridge corridors have bounded total turning. Low-stress corridors
remain a binding escape.

---

## 6. Bridge-mass consequence

Let
\[
S_{\rm br}=\sum_{e\text{ bridge}}\alpha_e.
\tag{C22.26}
\]
Root the bridge tree and let `H` be its maximum edge depth. At each fixed depth the
forward bridge-side components are disjoint, so C20 gives at most `2D` total bridge
stress on that frontier. Therefore
\[
\boxed{S_{\rm br}\le2DH.}
\tag{C22.27}
\]
If
\[
S_{\rm br}\ge\eta D^2,
\tag{C22.28}
\]
then
\[
\boxed{H\ge\frac{\eta D}{2}.}
\tag{C22.29}
\]
Combining with Theorem C22.6, some deep root-to-leaf path has either frequent events
or a straight run of length at least
\[
\boxed{
L_{\rm run}
\ge
\frac{\eta D}{2(|B_+|+1)}.
}
\tag{C22.30}

This remains compatible with `|B_+|=Theta(D)`, so no divergence is claimed.

---

## 7. Exact C-II frontier after C22

The bridge-heavy branch is no longer an arbitrary connected penny graph. Its bridge
tree has only `O(D)` genuine event nodes. Every long event-free interval is an exact
straight constant-stress integer chain, and every nested reciprocal-resultant sequence
has total variation `O(D)`.

The remaining exact corridor theorem is:

> **Bounded-variation corridor exclusion.** Show that a sufficiently large global
> minimum-diameter packing cannot support `D^2`-scale bridge transport through a
> boundary-order event tree whose corridors are exact straight chains and whose nested
> force resultants have total variation at most `2D`, unless the force hull becomes
> one-dimensional or a forbidden diameter configuration occurs.

The complementary C-II branch remains two-edge-connected stress bulk. C22 does not
eliminate it.

## 8. Regression audit

- A straight chain satisfies every corridor conclusion; its whole force hull would be
  one-dimensional, excluded only by the global C19 theorem.
- A sparse noncrossing tree with `Theta(D)` boundary events and `Theta(D)`-long
  straight corridors is not excluded. This is the principal surviving articulation
  regression.
- Genuine multi-terminal two-dimensional blocks are untouched.
- No lower bound on an individual reaction or contact stress is assumed.
- KKT-invisible source points remain allowed.
