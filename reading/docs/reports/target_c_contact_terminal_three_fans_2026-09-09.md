> Generated reading edition · [exact source](../../../docs/reports/target_c_contact_terminal_three_fans_2026-09-09.md) · source SHA-256 `5759389722a4fa767ec8f3289189e5e0573f944404034dbb61bc92e9a819b83c`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-4C0C74DF92AD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — every unloaded core vertex has a three-fan to loaded terminals

**Date:** 2026-09-09  
**Repository base:** current `research/target-c-mixed-three-connectivity-2026-09-09` after MC  
**Run type:** exact contact-topology consequence  
**Target:** Target C C-II / unloaded-component structure  
**Depends on:** MC mixed 3-connectivity and the fact that every diameter-edge endpoint lies in `B_+`  
**LEVEL I STATUS:** STILL OPEN

MC proves that the mixed support graph

```math
G_M=C\cup H
```

is 3-vertex-connected.  Since every diameter edge has both endpoints in the loaded force-hull set

```math
B:=B_+,
```

this immediately strengthens the contact-only topology in a way not captured by the old component attachment count.

### Main theorem

For every set `S subset V(C)` with `|S|<=2`, every connected component of

```math
C-S
```

contains at least one loaded terminal from `B\setminus S`.

Consequently every unloaded vertex `x in V(C)\setminus B` has three internally vertex-disjoint **contact paths** to three distinct loaded terminals.

Thus the old statement

```text
each unloaded component has at least three loaded attachments
```

upgrades to

```text
each unloaded vertex individually sees the loaded boundary through a contact three-fan.
```

No diameter edge is used in those three paths.

---

## 1. No small contact separator can hide an unloaded region

### Theorem TF.1 — loaded-terminal visibility after two contact deletions

Let

```math
S\subseteq V(C),
\qquad |S|\le2.
```

Then every connected component `K` of `C-S` satisfies

```math
\boxed{V(K)\cap(B\setminus S)\ne\varnothing.}
\tag{TF.1}
```

### Proof

Assume some component `K` contains no loaded vertex outside `S`.

Every diameter edge in `H` has both endpoints in `B`. Therefore no vertex of `K` is incident to any diameter edge of `G_M-S`: by assumption `K` contains no vertex of `B\setminus S`.

By definition of a contact component of `C-S`, there is also no contact edge from `K` to a vertex outside `K` in `V\setminus S`.

Hence `K` is a connected component of

```math
G_M-S.
```

For the sufficiently large C-II sources under consideration, `q=|B|>=3`, so after deleting at most two vertices there is a loaded terminal outside `S`. Thus `G_M-S` contains a vertex outside `K`.

Therefore `G_M-S` is disconnected, contradicting MC's 3-vertex-connectivity. `square`

For `|S|=1`, TF.1 recovers and strengthens the articulation conclusion used in C51.  The genuinely new content is the `|S|=2` case.

---

## 2. Three internally disjoint contact routes from every unloaded vertex

Fix

```math
x\in V(C)\setminus B.
```

Consider vertex-disjoint paths in the contact graph `C` from `x` to the terminal set `B`.

### Theorem TF.2 — contact three-fan theorem

There exist three contact paths

```math
P_1,P_2,P_3
```

from `x` to three distinct terminals

```math
b_1,b_2,b_3\in B
```

such that the paths are pairwise internally vertex-disjoint and intersect one another only at their common initial vertex `x`.

Equivalently,

```math
\boxed{\kappa_C(x,B)\ge3.}
\tag{TF.2}
```

### Proof

Use the vertex form of Menger's theorem for a vertex and a target set. If no three-fan existed, there would be a set

```math
S\subseteq V(C)\setminus\{x\},
\qquad |S|\le2,
```

whose deletion separates `x` from every terminal in `B\setminus S`.

Then the connected component of `C-S` containing `x` would contain no loaded terminal outside `S`, contradicting TF.1.  Hence three internally vertex-disjoint `x-B` contact paths exist.

Their terminal endpoints are distinct: if two ended at the same terminal, they would share that endpoint in addition to `x`; the standard fan form of Menger chooses distinct target vertices, equivalently one may attach a new sink adjacent to every terminal and apply the internally-disjoint path theorem. `square`

---

## 3. Componentwise version

Let `I_r` be a connected component of

```math
C[V\setminus B]
```

with loaded attachment set

```math
A_r\subseteq B.
```

Every contact path from a vertex of `I_r` to `B` must first leave `I_r` through a vertex of `A_r`. Therefore TF.2 immediately gives:

### Corollary TF.3 — three-fan to the attachment set

For every

```math
x\in I_r,
```

there are three internally vertex-disjoint contact paths from `x` to three distinct vertices of `A_r`.

In particular

```math
|A_r|\ge3,
```

recovering the old attachment lower bound, but now with vertexwise disjoint-route structure.

If

```math
|A_r|=3,
```

then every vertex of `I_r` has three disjoint contact routes to **all three** attachment terminals.

---

## 4. No one- or two-terminal internal bottleneck

A useful equivalent formulation is the following.

### Corollary TF.4

Let `X` be a nonempty connected set of unloaded vertices. If every contact path from `X` to `B` must pass through a set `S`, then

```math
\boxed{|S|\ge3.}
\tag{TF.3}
```

Here vertices of `S` may lie inside or outside `X`; the only requirement is that deleting `S` separates some surviving vertex of `X` from `B`.

Thus an unloaded positive-contact region cannot hang from the rest of the core through one or two articulation vertices.  This is stronger than C22's two-terminal straight-chain collapse: in the full post-ZF mixed-support regime, a genuinely **unloaded** region behind only two contact vertices cannot occur at all.

C22 remains relevant to regions whose two contact terminals are supplemented by loaded/diameter structure inside the region.

---

## 5. Contact bridges carry at least two diameter bypass edges

MC also gives a direct strengthening of the old bridge cut statement.

Let `uv` be a bridge of the contact graph `C`, and let

```math
V=A\sqcup B'
```

be the corresponding contact-edge cut, with `u in A`, `v in B'`.  The only contact edge crossing the cut is `uv`.

A 3-vertex-connected graph has edge-connectivity at least three.  Therefore every nontrivial edge cut of `G_M` contains at least three mixed edges.

The mixed edges crossing `A|B'` consist of

1. the one contact bridge `uv`;
2. actual diameter edges of `H` crossing the same cut.

Hence:

### Corollary TF.5 — double diameter bypass of every contact bridge

```math
\boxed{
|E_H(A,B')|\ge2.
}
\tag{TF.4}
```

So the old statement “every positive contact bridge is crossed by at least one positive diameter edge” improves to **at least two** actual diameter bypasses.

Because two distinct planar diameter segments cannot be collinear, the exact bridge cut law

```math
\alpha_{uv}(u-v)
=
\sum_{bk\in E_H(A,B')}
\beta_{bk}(b-k)
```

always contains at least two nonparallel positive diameter vectors. Consequently the old scalar estimate

```math
\alpha_{uv}\le D\sum_{bk\in E_H(A,B')}\beta_{bk}
```

is in fact strict for every contact bridge:

```math
\boxed{
\alpha_{uv}
<
D\sum_{bk\in E_H(A,B')}\beta_{bk}.
}
\tag{TF.5}
```

No uniform quantitative gap is claimed because one bypass weight may be arbitrarily small and distinct diameter directions may be separated by only `Theta(1/D)`.

---

## 6. Relation to the low-surplus tripod normal form

TN showed that in a hypothetical sublinear `e_BB+2s_C` phase, almost every unloaded component would be a singleton degree-three tripod attached to three loaded terminals.

TF explains why the number three is not merely a rank-count artifact.  In the full post-ZF framework, every unloaded vertex is protected by a genuine contact three-fan to the loaded boundary.

For a singleton tripod the three fan paths are exactly its three contact edges. For a larger component with three attachments, TF forces a nontrivial three-terminal internally robust network throughout the component.

This structure should be used in any future stability theorem attempting to replace a large unloaded component by a thin path or a two-terminal corridor: such a replacement would violate TF unless a third boundary route is preserved.

---

## 7. Regressions and limits

- **Unit square:** there are no unloaded vertices; TF.2 is vacuous.
- **Pure rhombic disk:** interior grid vertices naturally have several disjoint contact routes to the boundary; TF is compatible with this regression.
- **Contact bridge:** TF does not exclude bridges of `C`; it forces at least two diameter bypass edges in the mixed graph.
- **Three-fan length:** TF is purely topological. It does not bound the lengths of the three paths or give a disjoint fan simultaneously for many unloaded vertices.
- **Stress weights:** TF.4 is an edge-count statement. It gives no positive lower bound on the second-largest crossing `beta` weight.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| every component of `C-S`, `|S|<=2`, meets `B` | proved | diameter endpoints all lie in `B` + MC |
| every unloaded vertex has a contact three-fan to `B` | proved | Menger + preceding theorem |
| componentwise three-fan to `A_r` | proved | first exit from `I_r` |
| every contact bridge has at least two diameter bypasses | proved | mixed edge-connectivity >=3 |
| bridge cut inequality is strict | proved | at least two distinct nonparallel positive diameter vectors |
| uniform strict bridge gap | not proved | small weights / small angular separation remain |
| Level I | still open | need quantitative/global use of three-fan structure |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

MC: G_M=C union H is 3-vertex-connected.
All H endpoints lie in B=B_+.
Therefore for every S with |S|<=2, every component of C-S contains a terminal in B-S;
otherwise that component has no H edge and remains disconnected in G_M-S.
Menger then gives, for every unloaded x,
    three internally vertex-disjoint contact paths
    x -> b1, x -> b2, x -> b3
with distinct b_i in B.
For x in an unloaded component I_r, the three paths exit through distinct A_r terminals.

Also mixed edge-connectivity >=3. Across a contact bridge cut the only contact edge is
the bridge itself, so at least two actual diameter edges cross the cut. Their directions
are nonparallel, making the bridge cut stress inequality strictly stronger than the old
alpha_e <= D w_e, though no uniform gap follows yet.
```
