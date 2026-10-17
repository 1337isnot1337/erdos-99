> Generated reading edition · [exact source](../../../docs/reports/target_c_bridge_cut_matching_event_bound_2026-09-09.md) · source SHA-256 `138b463775795cdfee44d090242d3adf1d72ddec7fb7597ab8bad1d774d215eb`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-83AB8B36E9F7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — bridge-cut matching and a `2h-2` structural-event bound

**Date:** 2026-09-09  
**Repository base:** current PR #143 branch after MC/TF  
**Run type:** exact bridge-tree sharpening  
**Target:** Target C C-II / bridge-block phase  
**Depends on:** MC mixed 3-connectivity, TF contact-terminal consequences, C22 bridge-block tree  
**LEVEL I STATUS:** STILL OPEN

MC proves that the mixed support graph

```math
G_M=C\cup H
```

is 3-vertex-connected.  TF already used edge-connectivity to show that every contact bridge is bypassed by at least two actual diameter edges.  The vertex-connectivity statement gives more: on any bridge cut with at least three source vertices on each side, the complete mixed cut contains a matching of size three.  Hence at least two **vertex-disjoint** actual diameter edges bypass the contact bridge.

At the bridge-block-tree level this yields a new exact global count.  Let `h=|E(H)|`.  After suppressing the reaction-free degree-two singleton blocks as in C22, the structural bridge tree satisfies

```math
\boxed{
|V(T_{str})|\le2h-2,
\qquad
|E(T_{str})|\le2h-3.
}
\tag{BM.1}
```

The previous bound was `2q-2` and `2q-3`, where `q=|B_+|`.  Since `h=q-d_H`, BM improves the node bound by exactly `2d_H` whenever the diameter graph has tree-component defect.

---

## 1. The mixed edge cut of a contact bridge

Let `uv` be a bridge of the contact graph `C`.  Removing it partitions the contact core vertex set as

```math
V=A\sqcup B',
\qquad u\in A,
\qquad v\in B'.
\tag{BM.2}
```

The only contact edge crossing this partition is `uv`.  Every other mixed edge crossing it is an actual diameter edge.

Let `X_{uv}` be the bipartite graph with parts `A,B'` whose edges are **all** mixed edges of `G_M` crossing the cut.  Thus

```math
E(X_{uv})
=\{uv\}\sqcup E_H(A,B').
\tag{BM.3}
```

TF gives `|E_H(A,B')|>=2`.  We first strengthen this when both sides are non-small.

---

## 2. Three independent mixed edges cross every large bridge cut

### Theorem BM.1 — bridge-cut matching theorem

If

```math
|A|\ge3,
\qquad
|B'|\ge3,
\tag{BM.4}
```

then `X_{uv}` contains a matching of size at least three:

```math
\boxed{\nu(X_{uv})\ge3.}
\tag{BM.5}
```

Consequently at least two actual diameter edges in `E_H(A,B')` are pairwise vertex-disjoint.

### Proof

Suppose the minimum vertex-cover number of `X_{uv}` were at most two.  Let

```math
S\subseteq A\cup B',
\qquad |S|\le2,
```

meet every edge of `X_{uv}`.

Because each side of the cut has at least three vertices,

```math
A\setminus S\ne\varnothing,
\qquad
B'\setminus S\ne\varnothing.
```

After deleting `S`, every mixed edge crossing `A|B'` is gone, because `S` covers the entire cut graph.  Hence `G_M-S` is disconnected, contradicting MC's 3-vertex-connectivity.

Therefore

```math
\tau(X_{uv})\ge3.
```

The cut graph is bipartite, so König's theorem gives

```math
\nu(X_{uv})=\tau(X_{uv})\ge3.
```

At most one edge of any such matching can be the unique crossing contact edge `uv`.  Hence at least two matched edges are actual diameter edges, and because they belong to one matching they are vertex-disjoint. `square`

Since vertex-disjoint planar diameter edges cross geometrically, every large contact-bridge cut therefore carries an actual crossing pair of diameter chords.

---

## 3. One-sided endpoint form

For the bridge side `A`, define its mixed cut-boundary vertex set

```math
\partial_M A
:=
\{u\}
\cup
\{a\in A:\exists b\in B'\text{ with }ab\in H\}.
\tag{BM.6}
```

### Lemma BM.2 — every large bridge side has three mixed boundary vertices

If `|A|>=3`, then

```math
\boxed{|\partial_M A|\ge3.}
\tag{BM.7}
```

Consequently `A` contains at least two distinct loaded terminals from `B_+`.

### Proof

If `|\partial_M A|<=2`, then because `|A|>=3` there is a vertex in

```math
A\setminus\partial_M A.
```

Delete all vertices of `\partial_M A`.  Every mixed edge from `A` to `B'` is incident to this deleted set: the contact bridge uses `u`, and by definition every crossing diameter edge uses an `A`-endpoint in `\partial_M A`.  Thus a surviving vertex of `A` is disconnected from the surviving vertices of `B'`, unless every vertex of `B'` was deleted.

But `\partial_M A\subseteq A`, so no vertex of `B'` is deleted.  This contradicts 3-connectivity.

Hence BM.7 holds.

The only member of `\partial_M A` not automatically a diameter endpoint is `u`.  Therefore at least two distinct vertices of `A` are endpoints of crossing diameter edges, and hence lie in `B_+`. `square`

A slightly sharper conditional statement is immediate: if `u` itself is an endpoint of a crossing diameter edge, then the set of `A`-side diameter endpoints has cardinality at least three, because adjoining `u` adds no extra boundary vertex.

---

## 4. Leaf bridge blocks

Use C22's bridge-block tree `T_br`: delete all contact bridges and contract each remaining connected component.  A leaf block is the entire leaf side of its unique incident contact bridge.

C22 already proves every leaf block is loaded.

A bridge block cannot contain exactly two vertices.  Indeed, after all contact bridges are deleted, a two-vertex connected component would consist of one simple contact edge; that edge would itself be a contact bridge, contradiction.  Thus every bridge block is either a singleton or has at least three vertices.

Let

- `L_1` be the number of singleton leaf blocks;
- `L_+` be the number of non-singleton leaf blocks;
- `L=L_1+L_+`.

By Lemma BM.2, every non-singleton leaf block contains at least two distinct loaded terminals.  A singleton leaf block contains exactly one core vertex, which is loaded by C22.

Therefore the loaded terminals used by distinct leaf blocks are disjoint and

```math
\boxed{q\ge L_1+2L_+.}
\tag{BM.8}
```

---

## 5. Singleton leaves spend diameter branching

Let `x` be a singleton leaf block.  Its unique incident bridge is its only contact edge, so

```math
\deg_C(x)=1.
\tag{BM.9}
```

MC gives mixed minimum degree at least three.  Therefore

```math
\boxed{\deg_H(x)\ge2.}
\tag{BM.10}
```

Every vertex of `B_+` has diameter degree at least one by definition.  Hence

```math
\begin{aligned}
r_H
:=2h-q
&=\sum_{b\in B_+}(\deg_H(b)-1).
\end{aligned}
\tag{BM.11}
```

Each singleton leaf contributes at least one to the nonnegative sum on the right.  Distinct singleton leaves are distinct loaded vertices.  Thus

```math
\boxed{L_1\le r_H=2h-q.}
\tag{BM.12}
```

Combine BM.8 and BM.12:

```math
2L
=2L_1+2L_+
\le q+L_1
\le q+r_H
=2h.
```

Therefore

```math
\boxed{L\le h.}
\tag{BM.13}
```

This improves C22's general leaf count `L<=q`.

---

## 6. The structural bridge tree has at most `2h-2` events

Suppress the reaction-free degree-two singleton blocks exactly as in C22, obtaining the structural tree `T_str`.

Let

- `R` be the number of loaded nodes of `T_str`;
- `I_0` the number of reaction-free nodes;
- `L` the number of leaves.

Suppression does not change the leaves.  Every reaction-free node has degree at least three, so the standard tree identity gives

```math
\boxed{I_0\le L-2.}
\tag{BM.14}
```

C22 used only `R<=q`.  We can retain the extra terminal cost of the non-singleton leaf blocks.  Every loaded node contains at least one distinct loaded terminal, and every one of the `L_+` non-singleton leaf nodes contains at least one **additional** loaded terminal. Therefore

```math
\boxed{R+L_+\le q.}
\tag{BM.15}
```

Now

```math
\begin{aligned}
|V(T_{str})|
&=R+I_0\\
&\le R+L-2\\
&=R+L_1+L_+-2\\
&\le q+L_1-2\\
&\le q+r_H-2\\
&=2h-2.
\end{aligned}
```

This proves the node bound in BM.1.  Since a tree has one fewer edge,

```math
\boxed{|E(T_{str})|\le2h-3.}
\tag{BM.16}
```

Each edge of `T_str` represents one maximal exact straight constant-stress bridge corridor by C22.

---

## 7. Comparison with the previous event budget

C22 proved

```math
|V(T_{str})|\le2q-2.
```

Since

```math
h=q-d_H,
```

BM gives

```math
2h-2
=2q-2d_H-2.
```

Thus every unit of diameter-graph tree-component defect removes **two** possible structural bridge events from the old worst-case count.

The new estimate is exact and finite.  It is strongest in the high-`d_H` branch.  It does not by itself close the bridge phase because `h=Theta(D)` remains possible.

---

## 8. Relation to diameter-thrackle geometry

On every bridge cut satisfying BM.4, choose the two vertex-disjoint crossing diameter edges supplied by BM.1.  Their four loaded endpoints lie on the two complementary cyclic terminal intervals associated with the contact bridge, and the two diameter chords cross geometrically.

Therefore a large bridge side cannot be supplied by a diameter star through one loaded endpoint.  It has at least two independent diameter channels across the cut.

This is a useful regression against future scalar bridge-flow arguments: the cut force

```math
\alpha_{uv}(u-v)
=
\sum_{h\text{ crossing}}\beta_h d_h
```

is generated by a set of diameter vectors whose support contains at least two vertex-disjoint chords when both sides are large.  No uniform lower bound on their weights follows.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| large bridge cut has mixed matching number >=3 | proved | 3-connectivity + König |
| at least two vertex-disjoint H bypasses | proved | only one crossing contact edge |
| every >=3-vertex bridge side contains >=2 loaded terminals | proved | one-sided separator argument |
| singleton leaf has diameter degree >=2 | proved | mixed minimum degree 3 |
| singleton leaf count `L_1<=r_H` | proved | degree-excess identity |
| total leaf count `L<=h` | proved | terminal cost + preceding bound |
| structural event bound `2h-2` | proved | C22 tree identity + refined loaded-node accounting |
| sublinear bridge event count | not proved | `h=Theta(D)` remains possible |
| Level I | still open | must exploit independent diameter channels quantitatively or close bridgeless phase |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For a contact bridge uv with cut A|B, let X be the bipartite graph of all mixed
(C union H) edges crossing the cut. If |A|,|B|>=3, any <=2 vertex cover of X would
disconnect G_M after deleting those vertices. MC 3-connectivity therefore gives
    tau(X)>=3.
By Konig,
    nu(X)>=3.
Only uv is a contact edge, so at least two matched crossing edges are vertex-disjoint
actual diameter edges.

One-sided: every bridge side A with |A|>=3 has at least three mixed boundary vertices,
hence at least two distinct loaded terminals.

For bridge-block leaves:
- non-singleton leaves have >=2 loaded terminals;
- singleton leaves have contact degree 1, hence by mixed min degree 3 have H-degree>=2.
If L1=#singleton leaves, L+=#other leaves, then
    q>=L1+2L+,
    L1<=sum_B(deg_H-1)=2h-q=r_H,
so total leaves L<=h.
Keeping the extra terminal used by each non-singleton leaf in C22's tree count gives
    |V(T_str)|<=2h-2,
    |E(T_str)|<=2h-3.
```
