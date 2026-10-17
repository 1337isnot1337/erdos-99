> Generated reading edition · [exact source](../../../docs/reports/target_c_circuit_attachment_subfamily_sparsity_2026-09-11.md) · source SHA-256 `1eec657c1f9e4db2f83673e26f4af3783f78a6e7f35dafbd8c69f3d0c9bcd83b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-22159F2156D2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — circuit sparsity for unions of unloaded attachment components

**Date:** 2026-09-11  
**Repository base:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** exact circuit-combinatorial sharpening / attachment-overlap theorem  
**Target:** Target C C-II, post-ZF `s_Z=0` circuit phase  
**Depends on:** ZF circuit property, C35-C37 attachment decomposition, ZK component stress slack  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

The current `s_Z=0` frontier has a local sparsity inequality for one unloaded component,

```math
s_r+m_r\le2|A_r|-4,
```

with a whole-circuit exception. Summing that inequality loses exactly the information that matters when attachment sets overlap: it counts `sum |A_r|` instead of the size of their union, and it does not charge loaded-loaded mixed edges joining different attachment sets.

This report applies the **full mixed-circuit sparsity directly to unions of unloaded components**. For every nonempty subfamily `S` of unloaded components, define

```math
A(S):=\bigcup_{r\in S}A_r,
\qquad a(S):=|A(S)|,
\qquad s(S):=\sum_{r\in S}s_r,
```

and let `m(S)` be the number of loaded-loaded mixed edges of `C cup H` whose two endpoints both lie in `A(S)`. Thus `m(S)` includes both loaded-loaded unit contacts and actual diameter edges induced by the attachment union, including edges whose endpoints belong to different individual attachment sets.

Whenever

```math
W(S):=\left(\bigcup_{r\in S}I_r\right)\cup A(S)
```

is a proper vertex subset of the full mixed circuit,

```math
\boxed{
s(S)+m(S)\le2a(S)-|S|-3.
}
\tag{AS.1}
```

Equivalently,

```math
\boxed{
s(S)+|S|+m(S)+3\le2|A(S)|.
}
\tag{AS.2}
```

This is a genuine overlap-sensitive inequality. It is not uniformly stronger than summing the one-component inequalities when the attachment sets are disjoint, but it becomes stronger precisely when overlap or cross-attachment loaded edges are substantial.

Two useful consequences are proved below.

1. The demands `s_r+1` admit a capacity-two Hall assignment to the loaded attachment vertices: every unloaded component can charge one base token plus all of its pinned-contact surplus to its attachments, with no loaded vertex receiving more than two tokens.
2. If the C37 attachment-incidence graph has `s` connected components and `u_0` unused loaded vertices, then, outside the single-block/no-unused exceptional case, the number `m_cross` of loaded-loaded mixed edges crossing between incidence blocks or touching unused loaded vertices satisfies the exact identity

```math
\boxed{
m_{cross}=2u_0+3s-2+\sum_{j=1}^s\delta_j,
}
\tag{AS.3}
```

where each `delta_j>=0` is the Laman deficit of the induced mixed graph on that incidence block. In particular

```math
\boxed{m_{cross}\ge2u_0+3s-2.}
\tag{AS.4}
```

This replaces a naive component-by-component sparsity sum by an exact quotient-edge ledger. It still does not close C-II because actual diameter edges may pay the cross-block requirement; a new geometric or response constraint is needed to limit that payment.

---

## 1. Setup and the exact induced-edge count

Work in the post-ZF exact circuit phase `s_Z=0`. Let the nonisolated contact core have mixed graph

```math
G_M=C\cup H.
```

The post-ZF circuit theorem says `G_M` is a planar-realized two-dimensional rigidity circuit in the row-matroid sense:

```math
|E(G_M)|=2v-2,
\tag{1.1}
```

and every proper edge subset is independent. Consequently every proper induced vertex subgraph on `W` satisfies

```math
\boxed{|E(G_M[W])|\le2|W|-3.}
\tag{1.2}
```

Let `I_1,...,I_{c_I}` be the unloaded components. For one component write

- `n_r=|I_r|`;
- `e_r` for internal contact edges;
- `t_r` for contacts from `I_r` to the loaded set;
- `A_r` for its distinct loaded attachment vertices;
- `s_r=e_r+t_r-2n_r-1>=0` for its pinned-contact surplus.

Thus ZK gives the exact identity

```math
\boxed{e_r+t_r=2n_r+1+s_r.}
\tag{1.3}
```

Fix a nonempty subfamily `S`. Put

```math
N(S):=\sum_{r\in S}n_r.
```

There are no contact edges between two different unloaded components, by definition of the components, and diameter edges have loaded endpoints. Therefore the mixed edges induced by

```math
W(S)=I(S)\cup A(S)
```
are exactly

1. all `e_r+t_r` edges belonging to `r in S`, and
2. the `m(S)` loaded-loaded mixed edges induced by `A(S)`.

Hence, using (1.3),

```math
\begin{aligned}
|E(G_M[W(S)])|
&=\sum_{r\in S}(e_r+t_r)+m(S)\\
&=2N(S)+|S|+s(S)+m(S).
\end{aligned}
\tag{1.4}
```

Also

```math
|W(S)|=N(S)+a(S).
\tag{1.5}
```

If `W(S)` is proper, insert (1.4)-(1.5) into circuit sparsity (1.2):

```math
2N(S)+|S|+s(S)+m(S)
\le2N(S)+2a(S)-3.
```

Cancel `2N(S)` to obtain AS.1:

```math
\boxed{s(S)+m(S)\le2a(S)-|S|-3.}
```

No planarity or noncrossing relaxation is used in this step; attachment overlap is retained exactly through `A(S)`.

---

## 2. Scope and the whole-circuit exception

If `S` omits at least one unloaded component, then `W(S)` omits all vertices of that component and is automatically proper. Thus AS.1 applies to every nonempty proper subfamily of unloaded components.

If `S` is the full component family but some loaded vertex is unused by all attachments, then `W(S)` is still proper and AS.1 also applies.

The unique exceptional case is

```math
S=\{1,\ldots,c_I\},
\qquad
A(S)=B_+.
\tag{2.1}
```

Then `W(S)=V(G_M)` and one must use the full circuit equality (1.1) instead of the proper-subset bound. Equation (1.4) becomes

```math
2(v-q)+c_I+s_C+e_{BB}+h=2v-2,
```
so

```math
\boxed{
s_C+e_{BB}+h=2q-c_I-2.}
\tag{2.2}
```

This is exactly one unit above the formal proper-subset right side
`2q-c_I-3`, as required for a rigidity circuit.

Thus AS.1 has the correct whole-circuit exception and does not silently apply proper-subset sparsity to the full graph.

---

## 3. Relation to the one-component inequality

For a singleton family `S={r}`, AS.1 reads

```math
\boxed{s_r+m(A_r)\le2|A_r|-4.}
\tag{3.1}
```

This is the current local circuit inequality, with `m(A_r)` explicitly interpreted as **all** loaded mixed edges induced by the attachment set.

For larger `S`, naively summing (3.1) would give

```math
s(S)+\sum_{r\in S}m(A_r)
\le2\sum_{r\in S}|A_r|-4|S|.
\tag{3.2}
```

AS.1 instead gives

```math
s(S)+m(S)
\le2\left|\bigcup_{r\in S}A_r\right|-|S|-3.
\tag{3.3}
```

The two bounds are genuinely different:

- (3.2) can be better for many disjoint attachment sets because it receives `4` units of local circuit slack per component;
- (3.3) is better under enough attachment overlap and additionally charges every loaded mixed edge joining different attachment sets inside the union.

Thus the correct next use is not to discard the old local inequalities, but to intersect the local and union-family constraints.

---

## 4. Capacity-two Hall assignment for pinned surplus

Drop the nonnegative term `m(S)` from AS.2. For every proper-family case,

```math
\sum_{r\in S}(s_r+1)
\le2|A(S)|-3
<2|A(S)|.
\tag{4.1}
```

For the full family with `A(S)=B_+`, use (2.2):

```math
\begin{aligned}
s_C+c_I
&=2q-2-(e_{BB}+h)\\
&\le2q.
\end{aligned}
\tag{4.2}
```

If the full family does not use every loaded vertex, AS.1 already gives the stronger version of (4.1).

Therefore every subfamily `S` satisfies

```math
\boxed{
\sum_{r\in S}(s_r+1)\le2|A(S)|.
}
\tag{4.3}
```

Replace every loaded vertex `b` by two identical capacity slots. The standard capacitated Hall theorem applied to the bipartite incidence graph between components and loaded attachment slots now gives:

### Corollary AS.2 — surplus-token assignment

There is an assignment of `s_r+1` distinct tokens from every unloaded component `I_r` to slots belonging to vertices of `A_r` such that no loaded vertex receives more than two tokens in total.

This converts the scalar pinned surplus `s_C` into actual boundary incidence capacity without choosing components independently. It does **not** assign KKT weight, train endpoints, or geometric angles; those remain separate proof obligations.

---

## 5. Exact quotient-edge identity for incidence components

Let `J` be the C37 attachment-incidence graph: one node for every unloaded component, one node for every used loaded vertex, and one incidence edge for membership `b in A_r`.

Let its connected components containing an unloaded node be

```math
J_1,\ldots,J_s.
```

For `J_j`, let

- `R_j` be its unloaded-component set;
- `B_j=A(R_j)` be its loaded-vertex set;
- `W_j=I(R_j) cup B_j`.

The sets `W_j` are pairwise vertex-disjoint. Let

```math
u_0:=q-\left|\bigcup_jB_j\right|
```

be the number of loaded vertices unused by every unloaded component.

Assume we are not in the single-block/no-unused case `s=1,u_0=0`. Then every `W_j` is a proper vertex subset of the full mixed circuit. Define its exact nonnegative Laman deficit

```math
\boxed{
\delta_j:=2|W_j|-3-|E(G_M[W_j])|\ge0.
}
\tag{5.1}
```

Let `m_cross` count loaded-loaded mixed edges that are not internal to any one `B_j`. Equivalently, these are mixed loaded-loaded edges

- joining two distinct incidence blocks;
- joining an incidence block to an unused loaded vertex; or
- joining two unused loaded vertices.

There are no unloaded-to-unloaded or unloaded-to-loaded edges between distinct `W_j` blocks: any such contact attachment would connect the corresponding incidence components, and diameter edges have loaded endpoints. Hence the full mixed edge set decomposes exactly into the induced edge sets on the `W_j` plus these `m_cross` loaded-loaded edges.

Using the full circuit count,

```math
\begin{aligned}
m_{cross}
&=(2v-2)-\sum_{j=1}^s|E(G_M[W_j])|\\
&=(2v-2)-\sum_j(2|W_j|-3-\delta_j).
\end{aligned}
\tag{5.2}
```

Since

```math
v=u_0+\sum_j|W_j|,
```
we obtain the exact identity

```math
\boxed{
m_{cross}=2u_0+3s-2+\sum_j\delta_j.}
\tag{5.3}
```

In particular

```math
\boxed{m_{cross}\ge2u_0+3s-2.}
```

This is AS.3-AS.4.

### Exceptional case

If `s=1,u_0=0`, then `W_1=V(G_M)` and `m_cross=0`. Formula (5.3) must not be used because `delta_1` was defined through proper-subset sparsity. This is the same whole-circuit exception already isolated in Section 2.

---

## 6. What the quotient identity adds to C37/C38

C37 gives the planar incidence bound

```math
\sum_r|A_r|\le q_{used}+2c_I-2s,
```

and C38 gives a lower bound on **loaded-loaded contact edges** needed to connect the quotient. AS.3 is different: it counts all loaded-loaded **mixed** edges, including actual diameter edges, and its coefficient comes from full Laman-circuit tightness rather than planar Euler counting.

In particular, each additional attachment-incidence component costs three cross-block mixed edges, up to the global `-2` normalization, while each unused loaded vertex costs two. Any internal Laman deficit `delta_j` must be paid by another cross-block edge exactly.

This is the correct overlap-preserving ledger for attempts to couple attachment geometry to Woodall's diameter topology. It identifies the remaining missing theorem sharply:

> bound how much of `m_cross` can be paid by the convex-thrackle diameter graph without forcing either loaded contact surplus, a response obstruction, or a forbidden source geometry.

No such bound is proved here.

---

## 7. Regression audit

- **One unloaded component attached to all loaded vertices:** this is the whole-circuit exception when there are no unused terminals. AS.1 is not applied to the full graph.
- **Two components sharing loaded attachments:** AS.1 uses the union `A(S)` and therefore retains the overlap rather than counting the shared vertices twice.
- **Cross edges between attachment sets:** loaded contacts and diameter edges inside `A(S)` are both included in `m(S)`; they are not lost from the count.
- **Whole-circuit attachment exception:** isolated explicitly in Section 2; the right side gains exactly one edge there.
- **Contact-isolated source points:** the theorem is about the post-ZF nonisolated mixed core, exactly as ZF/ZK. It does not claim the omitted source population is absent.
- **Regular odd shell:** the report assumes `s_Z=0`; regular odd shells have `s_Z=2` and are outside scope.
- **`s_Z>0`:** no extension is asserted. The proper-subset circuit sparsity used in (1.2) is specific to the exact circuit phase.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| induced-edge identity (1.4) | proved | component decomposition + ZK |
| subfamily sparsity AS.1 | proved in `s_Z=0` | proper-subset circuit sparsity |
| whole-family exception (2.2) | proved | full circuit equality |
| capacity-two Hall assignment | proved | AS.1 plus whole-family equality |
| quotient identity AS.3 | proved | exact decomposition of the mixed circuit |
| attachment-overlap contradiction | not proved | H can still pay cross-block edges |
| Level I | still open | geometric/response conversion remains missing |

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

In the s_Z=0 mixed circuit let S be a nonempty family of unloaded components,
A(S)=union A_r, s(S)=sum s_r, and m(S) the number of loaded-loaded mixed edges
induced by A(S). For W(S)=union I_r union A(S),
    |E_M(W(S))| = sum_r(e_r+t_r)+m(S)
                = 2N(S)+|S|+s(S)+m(S).
If W(S) is proper, circuit sparsity gives
    s(S)+m(S) <= 2|A(S)|-|S|-3.
The only exception is the full component family with A(S)=B_+, where
    s_C+e_BB+h = 2q-c_I-2.

Dropping m(S) gives the capacitated Hall conditions
    sum_{r in S}(s_r+1) <= 2|A(S)|,
so the base component token plus all pinned surplus can be assigned to attachment
vertices with capacity two per loaded vertex.

If the C37 attachment incidence graph has s connected blocks and u_0 unused loaded
vertices, and not (s,u_0)=(1,0), define
    delta_j=2|W_j|-3-|E_M(W_j)| >=0.
Then exactly
    m_cross = 2u_0+3s-2+sum_j delta_j.
Thus every incidence split or internal Laman deficit is paid by explicit cross-block
loaded mixed edges. The missing closure is to limit how much of that payment can be
made by H rather than by loaded contact/response currency.
```
