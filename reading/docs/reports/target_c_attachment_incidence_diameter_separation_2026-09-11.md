> Generated reading edition · [exact source](../../../docs/reports/target_c_attachment_incidence_diameter_separation_2026-09-11.md) · source SHA-256 `250e577f8fd0a32e38bd73ca5c3e523e8c2345e1b7ed1ac328f00ca9916e357e`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E931780DF08E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — only one attachment-incidence block can contain diameter edges

**Date:** 2026-09-11  
**Repository base:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** planar attachment/diameter-topology coupling theorem  
**Target:** Target C C-II  
**Depends on:** C36-C37 planar attachment incidence, full actual convex-thrackle diameter graph  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

The C37 attachment-incidence graph and the actual diameter graph have so far mostly been counted separately. They cannot be arranged independently.

Let `J` be the planar bipartite attachment-incidence graph obtained by contracting every unloaded contact component and retaining one edge from that component node to each distinct loaded attachment. Let

```math
J_1,\ldots,J_s
```

be its connected components containing an unloaded node, and let `B_j` be the loaded boundary vertices belonging to `J_j`.

### Theorem AD.1

At most one `J_j` can contain both endpoints of an actual diameter edge. Equivalently,

```math
\boxed{
\#\{j:E(H[B_j])\ne\varnothing\}\le1.
}
\tag{AD.1}
```

Thus, except for one possible distinguished attachment-incidence block, every actual diameter edge incident to a terminal used by an unloaded component must leave that incidence block.

The theorem is topological. It uses neither `s_Z=0` nor stress weights. It therefore applies before the circuit specialization, whenever the C36-C37 attachment decomposition and full actual diameter visibility are available.

Combined with the `s_Z=0` quotient ledger of the companion attachment-sparsity report, this localizes all internal diameter payment to one incidence block. It does not yet force loaded-contact payment, because a convex-thrackle forest can still place many diameter edges between distinct incidence blocks.

---

## 1. Boundary nonalternation for distinct incidence components

C37 constructs `J` as a planar embedded graph in the force hull `F`, with every loaded vertex on the outer face in the same cyclic order as on `partial F`. Distinct connected components `J_i,J_j` are vertex-disjoint and edge-disjoint.

We use the following standard disk-topology fact.

### Lemma AD.1 — disjoint connected planar pieces do not link on the boundary

Let `X,Y` be two disjoint connected finite plane graphs embedded in a closed disk, with all their boundary vertices lying on the boundary circle. There do not exist distinct boundary vertices

```math
a,b\in X,
\qquad c,d\in Y
```

occurring in alternating cyclic order

```math
a,c,b,d.
```

#### Proof

Choose a simple path `P` in `X` from `a` to `b`. If `P` meets the boundary circle at intermediate vertices, perturb arbitrarily small neighborhoods of those intermediate boundary contacts into the open disk. Because `X` and `Y` are finite disjoint embedded graphs, the perturbation can be chosen disjoint from `Y` and from itself. We obtain a simple arc `P'` from `a` to `b` whose interior lies in the open disk and is disjoint from `Y`.

The arc `P'` separates the disk into two components after adjoining either boundary arc from `a` to `b`. Since `c` and `d` lie on opposite boundary arcs by alternation, every connected subset of the disk containing both `c` and `d` must meet `P'`. But `Y` is connected and contains `c,d`, contradicting `P' cap Y=emptyset`. `square`

The same statement can be phrased as the familiar noncrossing-partition property of the boundary vertex sets of disjoint connected plane subgraphs.

---

## 2. Proof of AD.1

Assume for contradiction that two distinct incidence components `J_i` and `J_j` each contain the endpoints of an actual diameter edge:

```math
ab\in E(H),\qquad a,b\in B_i,
```

```math
cd\in E(H),\qquad c,d\in B_j.
```

The loaded sets `B_i` and `B_j` are disjoint because `J_i,J_j` are distinct connected components of the incidence graph. Hence the two diameter edges have four distinct endpoints.

The full actual diameter graph of a planar point set is a straight-line convex geometric thrackle: any two diameter edges with disjoint endpoints cross. Therefore the chords `ab` and `cd` cross in the interior of the force hull. Their four endpoints consequently occur in alternating cyclic order on `partial F`, say

```math
a,c,b,d.
```

But `J_i` and `J_j` are disjoint connected plane subgraphs containing `a,b` and `c,d`, respectively. Lemma AD.1 forbids such alternating boundary pairs. Contradiction.

Thus at most one incidence component contains an internal diameter edge. `square`

---

## 3. Immediate counting consequences

If a distinguished incidence block exists, denote it by `J_*` and its loaded set by `B_*`; otherwise put `B_*=emptyset`.

Every loaded terminal is incident to at least one actual diameter edge. Hence every terminal in

```math
\left(\bigcup_jB_j\right)\setminus B_*
```

is incident to a diameter edge that leaves its incidence block. In particular, if `h_cross` counts diameter edges whose endpoints do not lie in one common incidence block, then

```math
\boxed{
2h_{cross}\ge q_{used}-|B_*|.
}
\tag{3.1}
```

This inequality is deliberately weak but unconditional: a cross-block diameter edge can serve two terminals from two different nondistinguished blocks.

In the Woodall forest branch, the internal diameter graph `H[B_*]` is a forest, so

```math
|E(H[B_*])|\le |B_*|-1
```
whenever `B_*` is nonempty. Thus

```math
\boxed{
h_{cross}\ge h-|B_*|+1.}
\tag{3.2}
```

Neither (3.1) nor (3.2) is by itself a contradiction; their role is to prevent diameter edges from being distributed independently inside many attachment cells.

---

## 4. Combination with circuit attachment sparsity

In the `s_Z=0` circuit phase, the companion report proves the exact quotient ledger

```math
m_{cross}=2u_0+3s-2+\sum_{j=1}^s\delta_j,
\tag{4.1}
```

outside the single-block/no-unused whole-circuit exception. Here `u_0=q-q_used`, `delta_j>=0`, and `m_cross` counts loaded-loaded mixed edges not internal to an incidence block.

Split

```math
m_{cross}=h_{cross}+c_{cross},
\tag{4.2}
```

where `c_cross` counts loaded-loaded unit contacts crossing the incidence-block partition or touching unused loaded vertices.

AD.1 says every internal diameter edge is contained in the single possible block `B_*`. Therefore

```math
\boxed{
c_{cross}
=2u_0+3s-2+\sum_j\delta_j-h+h_*}
\tag{4.3}
```

where

```math
h_*:=|E(H[B_*])|
```
(with `h_*=0` if no distinguished block exists).

Since `c_cross>=0`, this records the exact feasibility condition

```math
\boxed{
h-h_*
\le2u_0+3s-2+\sum_j\delta_j.}
\tag{4.4}
```

Conversely, if the right side of (4.3) has a positive linear lower bound after subtracting the maximum possible diameter payment, that lower bound is automatically loaded-contact currency `e_{BB}`.

The current structure does not provide such a maximum strong enough to close C-II. A Woodall caterpillar forest can still place linearly many diameter edges between distinct noncrossing incidence blocks. AD.1 localizes the failure to those cross-block edges rather than eliminating it.

---

## 5. Why a stronger naive claim is false or unproved

AD.1 does **not** say that each incidence block is a single cyclic interval. C36/C37 give the required planar nonalternation between distinct connected incidence pieces, but one block can have many boundary attachment vertices and nested internal structure.

AD.1 also does **not** bound the number of diameter edges between two different incidence blocks by one. Two disjoint boundary blocks can support many mutually crossing chords with reversed endpoint order. Such a family is compatible with the thrackle crossing condition and with a forest if the endpoint incidences do not create a cycle.

Therefore the tempting implication

```math
\text{many incidence blocks}
\Longrightarrow
\text{many loaded-loaded contacts}
```

is not established by topology alone. The missing ingredient must constrain the cross-block diameter family by metric direction gaps, response transport, or the common contact-route block.

---

## 6. Interaction with the new doubled-gap theorem

The companion forest report proves that vertex-disjoint diameter edges have projective direction separation at least

```math
4\arcsin\frac1{2D},
```

twice the generic shared-endpoint separation. Since AD.1 forces almost every diameter edge, in a multi-block attachment decomposition, to run between blocks rather than remain internal, this supplies a natural next coupling:

1. use incidence-block order to extract many **vertex-disjoint consecutive** cross-block diameter edges;
2. charge their doubled direction gaps through the difference-body perimeter;
3. convert the resulting perimeter loss into either outer-walk excess or loaded-contact/response mass through the exact circuit ledger.

Step 1 at the required linear scale is not proved here. A large star-like family of cross-block diameter edges can reuse terminals and evade a naive matching count; the full-source shared-endpoint angle theorem allows sublinear but growing degrees. Any future extraction must retain those degree concentrations rather than assume bounded degree.

---

## 7. Regression audit

- **One incidence block:** AD.1 is vacuous and does not disturb the whole-circuit exception.
- **Two components with alternating attachment pairs:** excluded already by planar incidence topology; AD.1 is exactly this obstruction triggered by two disjoint crossing diameter chords.
- **Many chords between two blocks:** allowed; AD.1 does not claim a one-edge bound.
- **Shared diameter endpoints:** internal diameter edges in different blocks cannot share a terminal because the loaded block sets are disjoint. The thrackle crossing theorem therefore applies with four distinct endpoints.
- **Cyclic diameter topology:** AD.1 itself remains valid; the forest-only bound (3.2) is not imported into the cyclic branch.
- **Contact-isolated source points:** untouched. The incidence graph belongs to the nonisolated core; no full-source saturation is assumed.
- **`s_Z>0`:** AD.1 remains topological; only Section 4's exact circuit ledger assumes `s_Z=0`.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| boundary nonalternation lemma | proved | disk separation |
| at most one incidence block with internal H edge | proved | convex-thrackle crossing + nonalternation |
| forest internal-edge bound | proved | forest sparsity |
| circuit quotient formula (4.3) | proved conditional on companion AS ledger | exact edge partition |
| linear loaded-contact consequence | not proved | H may pay cross-block ledger linearly |
| Level I | still open | cross-block diameter payment remains |

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let J_1,...,J_s be the connected components of the planar C37 attachment-incidence
graph, with loaded boundary sets B_j. If two distinct blocks each contained an
actual diameter edge ab and cd, the four endpoints would be distinct. Actual
diameter edges form a convex geometric thrackle, so ab and cd cross and their
endpoints alternate on the force-hull boundary. But disjoint connected planar
subgraphs cannot connect two alternating boundary pairs. Contradiction.

Hence at most one B_* has E(H[B_*]) nonempty.

In s_Z=0, combine this with the exact companion quotient ledger
    m_cross=2u_0+3s-2+sum delta_j
and write m_cross=h_cross+c_cross. Since all internal H edges lie in B_*,
    c_cross=2u_0+3s-2+sum delta_j-h+h_*,
where h_*=|E(H[B_*])|.

This localizes the remaining failure: C-II can survive only if a sufficiently large
cross-block diameter family pays the quotient ledger. Topology alone does not bound
that family strongly enough; a metric-direction, response, or common-block theorem
is still needed.
```
