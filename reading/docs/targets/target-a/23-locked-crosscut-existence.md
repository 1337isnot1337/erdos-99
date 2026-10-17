> Generated reading edition · [exact source](../../../../docs/targets/target-a/23-locked-crosscut-existence.md) · source SHA-256 `7733ac57c9c8f05b641d983b2698700a57b2b4821300dbd8098b9ba69d2fd972`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — locked stress forces a proper response crosscut

Section 169 transported a universally locked response triangle to a positive-contact
stress component meeting the actual response hull boundary.  Section 170 gave an exact
Schur bound conditional on a proper contact crosscut.  The theorem below removes that
conditionality for every nontrivial response cardinality: the positive-contact stress
itself forces such a crosscut.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 171. Positive stress support contains a boundary-to-boundary crosscut

Assume the actual-response locked branch of Section 169.  Thus `m^*>=3`,
`K^*=conv X^*` is a full-dimensional convex polygon, and there is a nonnegative
contact/facet equilibrium
```math
\sum_{j:ij\in E_1(X^*)}\alpha_{ij}(p_i-p_j)
-
\sum_{f:n_f\cdot p_i=c_f}\mu_{if}n_f=0
\tag{171.1}
```
with strictly positive coefficients on the three edges of a unit equilateral triangle
`T_*`.  Let `G_+` be the graph of positive contact edges `alpha_ij>0`, and let
`K_T` be its connected component containing `T_*`.

Call a vertex a **reaction vertex** when at least one `mu_if>0`.  Every reaction
vertex belongs to `X^* cap partial K^*`.

## 171.1 Leaf blocks must carry reaction

Use the standard block-cut tree of the finite connected graph `K_T`, treating a bridge
as a block of two vertices.  A leaf block has at most one cut vertex through which it
meets the rest of `K_T`.

> **Lemma 171.1 (reaction in every leaf block).**  Let `B_0` be a leaf block of
> `K_T`.  If `w` is its unique cut vertex when one exists, then `B_0` contains a
> reaction vertex distinct from `w`.

### Proof

Suppose not.  Every vertex of `B_0\setminus{w}` then has zero facet reaction.  Since
`B_0` is a leaf block, no such vertex is incident with a positive contact edge outside
`B_0`; otherwise it would be a second cut vertex of that block.

The finite set of geometric vertices of `B_0` has a convex-hull extreme vertex
`z!=w`.  For a bridge block this is simply its non-cut endpoint.  For a block with at
least three vertices, its convex hull has at least two extreme vertices, so at most one
can be `w`.  Choose a vector `u` exposing `z` uniquely among `V(B_0)`.  Then for every
positive-contact neighbor `j` of `z`,
```math
u\cdot(p_z-p_j)>0.
\tag{171.2}
```
At `z` the reaction term in (171.1) is zero and all positive-contact neighbors lie in
`B_0`.  Dotting (171.1) with `u` gives
```math
0
=
\sum_j\alpha_{zj}\,u\cdot(p_z-p_j)
>0,
\tag{171.3}
```
a contradiction.  $`\square`$

The same exposing-direction argument also shows directly that if `K_T` consists of a
single block, its convex-hull extreme vertices must be reaction vertices.  In
particular that block has at least two distinct reaction vertices, consistent with
Theorem 159.1.

## 171.2 A reaction-to-reaction path through the locked triangle block

All three edges of `T_*` lie in one 2-connected block of `K_T`; call it `B_T`.
Choose any vertex `t` of `T_*`.

> **Lemma 171.2 (boundary path through the triangle block).**  There are two distinct
> reaction vertices `r_-,r_+` and a simple positive-contact path from `r_-` to `r_+`
> that contains `t`.

### Proof

Root the block-cut tree at `B_T`.

If the tree has only the single block `B_T`, the preceding extreme-point observation
supplies two distinct reaction vertices in `B_T`.  Since `B_T` is 2-connected, the
fan form of Menger's theorem gives internally vertex-disjoint paths from `t` to those
two reaction vertices; their union is a simple reaction-to-reaction path through `t`.

Suppose the block-cut tree has more than one block.  Every branch from `B_T` ends in a
leaf block, and Lemma 171.1 supplies a reaction vertex in that leaf away from its cut
vertex.

If at least two branches leave `B_T`, choose reaction vertices `r_-` and `r_+` in leaf
blocks of two different branches.  Let `c_-,c_+` be the corresponding cut vertices of
`B_T`.  Because `B_T` is 2-connected, there is a simple `c_-`--`c_+` path inside
`B_T` passing through `t`: equivalently, apply the two-fan theorem at `t` to the set
`{c_-,c_+}`.  Concatenate it with the unique block-tree paths from `r_-` to `c_-` and
from `c_+` to `r_+`.  Choosing simple paths inside each traversed block gives a simple
positive-contact path through `t`.

If exactly one branch leaves `B_T`, then `B_T` is itself a leaf block of the unrooted
block-cut tree.  Let `c` be its unique cut vertex.  Lemma 171.1 supplies a reaction
vertex `r_- in B_T\setminus{c}`, while the unique external branch ends in another leaf
block containing a reaction vertex `r_+`.  Two-connectivity of `B_T` gives a simple
`r_-`--`c` path through `t`, and concatenating with a simple path along the external
block-tree branch to `r_+` proves the claim.  $`\square`$

## 171.3 Proper crosscut existence

The straight-line unit-contact graph on the unit-separated set `X^*` is plane.  Indeed,
if two disjoint unit edges crossed properly, applying the unit-edge crossing barrier
of Lemma 103.1 to either edge would force the other to have length at least `sqrt(3)`,
contradicting its unit length.  Thus every simple contact path is a simple polygonal
arc.

> **Theorem 171.3 (locked contact crosscut exists).**  If `m^*>3`, the positive-
> contact component `K_T` contains a locked contact crosscut in the sense of Section
> 169: a simple positive-contact path
> 

```math
> Q=(q_0,\ldots,q_L)
> \tag{171.4}
> 
```
> with
> 

```math
> q_0,q_L\in\partial K^*,
> \qquad
> |Q|\setminus\{q_0,q_L\}\subset\operatorname{int}K^*.
> \tag{171.5}
> 
```

### Proof

Take the reaction-to-reaction simple path `P` through a chosen triangle vertex `t`
from Lemma 171.2.  Its endpoints are boundary reaction vertices.

First suppose `T_*` has at least one vertex in `int K^*`.  Choose `t` to be such an
interior vertex.  Along `P`, let `q_0` be the last boundary vertex occurring before
`t`, and `q_L` the first boundary vertex occurring after `t`.  They are distinct and
the subpath between them has no other boundary vertex.  In a full-dimensional convex
body, a segment joining an interior point to any point of the body has open segment in
the interior; likewise a segment between two interior points lies in the interior.
Therefore the polygonal subarc between `q_0` and `q_L`, except for its endpoints, lies
in `int K^*`.  It is the required crosscut.

It remains to consider the case in which all three vertices of `T_*` lie on
`partial K^*`.  If every one of the three unit sides of `T_*` were contained in
`partial K^*`, convexity would force
```math
K^*=\operatorname{conv}T_*.
\tag{171.6}
```
That unit equilateral triangle has diameter one, so any fourth point in it is at
distance strictly below one from at least one triangle vertex; hence it cannot contain
four unit-separated points.  This would give `m^*=3`, contrary to hypothesis.
Therefore at least one triangle side `q_0q_1` is not contained in the hull boundary.
For two boundary points of a convex body, if their joining segment is not a boundary
segment, its relative interior lies in `int K^*`.  The one-edge path
```math
Q=(q_0,q_1)
\tag{171.7}
```
is therefore a proper positive-contact crosscut.  $`\square`$

The exceptional case `m^*=3` is irrelevant to the eventual-large-cardinality problem;
it is also already an equilateral-triangle optimum rather than a triangle-free
counterexample.

## 171.4 Immediate Schur consequence

Combining Theorem 171.3 with Section 170 gives an unconditional exact inequality in
the actual-response locked branch for every `m^*>3`.

> **Corollary 171.4 (locked-branch crosscut bound).**  There is a positive-contact
> crosscut `Q` for which
> 

```math
> \boxed{
> \zeta
> \ge
> \max\{0,|C_L|-|O_L|\}
> +\max\{0,|C_R|-|O_R|\}
> -|W_Q|,
> }
> \tag{171.8}
> 
```
> with
> 

```math
> \boxed{|W_Q|\le5|V(Q)|.}
> \tag{171.9}
> 
```

The remaining locked-branch obligation is now purely quantitative.  Proper-crosscut
existence is no longer open.  One must derive enough side imbalance relative to the
crosscut shielding cost to reach
```math
s=\Delta_\Lambda-d_{\rm int},
\tag{171.10}
```
or combine several stress-generated crosscuts with a sharper union-cost estimate.
