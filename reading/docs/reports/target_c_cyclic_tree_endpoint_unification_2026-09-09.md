> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_tree_endpoint_unification_2026-09-09.md) · source SHA-256 `3823cd112352281644b0f0c38f83e5136b73c7fdc8aaaa0ede7247ac1e3376dd`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-06BF898834C2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=1` zeroed edges force four-block corner cuts

**Date:** 2026-09-09  
**Repository branch:** PR #118 after DC/D2/TC  
**Run type:** exact KKT-endpoint/topological reduction plus dependency correction  
**Target:** cyclic primitive tree phases `d_H=1,2`  
**Depends on:** DC, D2, TC, LF, CG selected scalar-rank theorem  
**External literature:** none  
**Computation:** small abstract convex-thrackle enumeration was used only as a regression check; it is not a proof dependency

## LEVEL I STATUS

`STILL OPEN`

This report originally made one unsupported identification: after a full-tree diameter edge `e` has coefficient zero at a `d_H=1` KKT endpoint, it identified the selected positive diameter support with `H-e` and called the resulting mixed graph a rigidity circuit. TC does **not** prove that no other diameter coefficient vanishes at the same endpoint, and CG proves maximal rank of the selected **scalar stress matrix**, not rank `2q-3` of the selected mixed rigidity matrix.

That circuit claim is withdrawn here.

The useful geometric theorem survives intact and is slightly cleaner when stated on the **full** diameter tree: every zeroed nonleaf edge cuts the full tree into two nontrivial mutually-crossing trees whose bipartition classes are four cyclic blocks, and the zeroed chord joins opposite block corners. Summed endpoint equilibrium still gives the reciprocal parallelogram because the zeroed full-tree edge is the only full diameter edge crossing that cut.

### Theorem EU — four-block corner-cut theorem

Let `H` be the full spanning diameter tree in the cyclic `d_H=1` phase. Let `s` be a KKT endpoint and let

```math
e=uv\in E(H),\qquad \beta_e(s)=0,
```

be any zeroed nonleaf full-tree edge. Put

```math
H-e=T_A\sqcup T_B.
```

Then:

1. `T_A,T_B` are nontrivial trees covering all `q` terminals;
2. their bipartition classes form four nonempty cyclic blocks, after relabeling,
   ```math
   \boxed{A_0\mid B_0\mid A_1\mid B_1;}
   \tag{EU.1}
   
   ```
3. the four cycle contacts crossing the `A|B` cut satisfy the endpoint reciprocal parallelogram
   ```math
   \boxed{v_i+v_k=v_j+v_\ell,\qquad v_r=\alpha_r t_r;}
   \tag{EU.2}
   
   ```
4. the zeroed actual diameter chord `e=uv` joins opposite corners of the four-block partition. In particular `u` and `v` are endpoints of their respective color blocks.

The selected positive diameter support at `s` may be a proper subgraph of

```math
H-e.
```

What CG does guarantee at the endpoint is

```math
C_s=C_q,
\qquad B_s=B_+,
\qquad \operatorname{rank}\Omega_s=q-3,
```

and C56-G. No selected mixed-rigidity rank is asserted.

---

## 1. Deleting a zeroed nonleaf full-tree edge

DC says the full `d_H=1` diameter graph is one spanning tree on `q` terminals, so

```math
|E(H)|=q-1.
```

TC/LF show that each endpoint lies on at least one diameter-coordinate facet corresponding to a nonleaf full-tree edge. Fix such an edge

```math
e=uv.
```

Deleting a tree edge gives exactly two connected components. Since `e` is nonleaf, each component contains at least one remaining diameter edge. Hence

```math
H-e=T_A\sqcup T_B
```

with two nontrivial trees.

Every A-edge is vertex-disjoint from every B-edge. Because the **full** diameter graph is a convex geometric thrackle, every A-edge crosses every B-edge.

This conclusion uses the full graph only and is unaffected if additional beta coordinates vanish at the selected endpoint.

---

## 2. Four cyclic color blocks

Write the tree bipartitions as

```math
A=A_0\sqcup A_1,
\qquad
B=B_0\sqcup B_1.
```

Fix an A-edge `xy`. Every B-edge crosses `xy`, so its endpoints lie on opposite open boundary arcs cut by `x,y`. Connectivity and bipartiteness of `T_B` imply, up to swapping colors, that all of `B_0` lies on one arc and all of `B_1` on the other.

Thus two same-color B vertices lie on the same side of every A-edge. Their joining chord crosses no A-edge. If an A-vertex separated two same-color B vertices along their boundary arc, connectedness of `T_A` would force an A-edge to cross that same-color chord, contradiction. Therefore each B-color class is one cyclic block. The same argument applies to the A-color classes.

Since each tree contains an edge, all four classes are nonempty. Cross-component crossing then forces the two B blocks to separate the two A blocks, and conversely. After cyclic rotation and color swaps,

```math
\boxed{A_0\mid B_0\mid A_1\mid B_1.}
```

This is EU.1.

---

## 3. Endpoint equilibrium gives the reciprocal parallelogram without support equality

The full tree edge `e` is the **only full diameter edge** crossing the cut `A|B`. Since

```math
\beta_e(s)=0,
```

no selected positive diameter force crosses that cut. Any additional zeroed diameter rows lie inside `A` or inside `B` and are irrelevant to the cut sum.

Sum the KKT equilibrium equations of the endpoint stress over all vertices in `A`. Internal contact and selected diameter forces cancel. Four cycle contacts cross the cut because of the four-block order. With cyclic transition indices `i<j<k<ell`, the signed contact-force resultant is

```math
v_i-v_j+v_k-v_\ell=0,
\qquad
v_r=\alpha_rt_r.
```

Hence

```math
\boxed{v_i+v_k=v_j+v_\ell.}
```

This is EU.2 and is exactly TC's reciprocal parallelogram.

---

## 4. The zeroed diameter chord is an opposite-corner chord

Let `u` lie in `T_A`, say in block `A_0`. Because `e` is nonleaf in the full tree, `u` has at least one edge of `T_A` joining it to `A_1`.

Assume first that `v` lies in `B_0`, with cyclic order

```math
A_0\mid B_0\mid A_1\mid B_1.
```

Take any `a in A_0\setminus\{u\}`. Since `T_A` is connected and nontrivial, `a` is incident to an A-edge joining `A_0` to `A_1`. Unless that edge is incident to `u`, it is vertex-disjoint from the full diameter chord `uv` and therefore crosses `uv`.

A chord from `A_0` to `A_1` crosses `uv` only if its A0 endpoint lies on the `u -> B_0` side of `u` within the A0 block. An A0 vertex on the other side would produce a nonalternating endpoint order and a noncrossing pair. Therefore no A0 vertex lies on that forbidden side, and `u` is the A0 endpoint adjacent to `B_1`.

The symmetric argument with B-edges shows that `v` is the B0 endpoint adjacent to `A_1`. Thus `uv` joins the opposite block corners

```math
(B_1|A_0)
\quad\text{and}\quad
(B_0|A_1).
```

If `v in B_1`, the other pair of opposite corners results. Singleton blocks cause no exception because their unique vertex is both block endpoints.

Therefore

```math
\boxed{\text{every zeroed nonleaf full-tree edge at a KKT endpoint is an opposite-corner chord.}}
\tag{EU.3}
```

---

## 5. Correct relation to the `d_H=2` phase

D2 proves that in the full `d_H=2` phase the actual diameter graph itself is exactly two tree components with four alternating bipartition blocks. CY gives a unique normalized stress there, and the full mixed graph is a rigidity circuit.

For a `d_H=1` KKT endpoint, EU proves only the corresponding **full-tree cut topology** and cut equilibrium:

- `H-e` is two nontrivial trees with the same four-block order;
- `e` is an opposite-corner actual diameter chord;
- the endpoint reciprocal forces satisfy the same transition parallelogram;
- the positive selected diameter support is an edge cover contained in `H-e`, but may omit further internal tree edges;
- CG keeps the selected scalar stress matrix in C56-G with affine kernel only.

So the two tree phases share a four-block geometric skeleton, not necessarily the same selected rigidity circuit.

---

## 6. Two-endpoint consequence for `d_H=1`

The normalized KKT polytope is a line segment. LF/TC show its two endpoint facets involve distinct nonleaf full-tree diameter coordinates. Therefore there exist distinct full-tree edges

```math
e_-,e_+
```

with

```math
\beta_{e_-}(s_-)=0,
\qquad
\beta_{e_+}(s_+)=0.
```

EU applies independently to each. Hence the same spanning convex-thrackle tree admits two distinct nonleaf edge cuts such that:

1. each cut has a four-block bipartition order;
2. the deleted edge is an opposite-corner chord for that cut;
3. the corresponding endpoint reciprocal polygon contains the cut parallelogram.

The endpoint reciprocal polygons and selected positive diameter supports may differ. No stronger identification is assumed.

---

## 7. Audit correction

The following claims from the first version are withdrawn:

- that the endpoint selected positive diameter support equals `H-e`;
- that the selected endpoint mixed rigidity matrix has rank `2q-3`;
- that the endpoint support has exactly one mixed row dependence;
- that every `d_H=1` endpoint is literally a D2 rigidity circuit plus one zero-weight chord.

What remains proved is the four-block/corner-cut theorem and reciprocal parallelogram above. CG's selected **scalar** rank theorem remains valid and useful.

This correction does not weaken TC, D2, DC, UFB, ID, or any `d_H=0` Reinhardt result.

---

## 8. Regression audit

### Multiple beta coordinates vanish at one endpoint

Allowed. EU uses one zeroed nonleaf full-tree edge at a time. Additional vanished edges lie inside the two components of `H-e` and do not affect the cut-equilibrium argument.

### One zeroed nonleaf edge

The four-block and corner-chord conclusions remain exact.

### `d_H=2`

Its full graph is still the genuine two-tree rigidity circuit established by CY/D2; this correction concerns only selected supports at `d_H=1` endpoints.

### Abstract double-corner trees

Allowed. EU does not claim the double-corner property alone is contradictory.

---

## 9. Next theorem

The best common tree-phase attack is now stated without an unsupported support identification.

1. **`d_H=1`:** combine two distinct EU corner cuts, their endpoint reciprocal parallelograms, WT's weighted-cycle transfer formulas, and CG/C56-G. A useful intermediate theorem would bound how many internal beta coordinates can simultaneously vanish at an endpoint of a maximal scalar-rank edge-cover stress.
2. **`d_H=2`:** exploit the genuine D2 four-block two-tree rigidity circuit and unique KKT stress directly.

The source-population route UFB/ID remains common to all cyclic phases.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

The corrected theorem is downstream of report-level CY/DC/D2/TC/LF/CG. The new corner argument is elementary and does not require selected mixed-rigidity rank.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Correction: a d_H=1 endpoint may zero more than one beta coordinate. CG proves selected
scalar-stress rank q-3, not selected mixed-rigidity rank 2q-3. Do not identify the
positive endpoint support with H-e or call it a rigidity circuit.

What is exact:
Choose any zeroed nonleaf full-tree edge e=uv. Since H is a spanning tree, H-e has two
nontrivial full-tree components T_A,T_B. Every A-edge crosses every B-edge. Their tree
bipartition classes are four nonempty cyclic blocks
  A0 | B0 | A1 | B1.
The full edge e is the only full diameter edge crossing A|B and beta_e=0, so summed
endpoint equilibrium leaves exactly four contact forces:
  v_i+v_k=v_j+v_l.
Thrackle crossing with the remaining full-tree edges forces u,v to be opposite block
corners.

The two KKT endpoints give two distinct such full-tree corner cuts. Endpoint selected
supports may omit additional internal edges but remain C56-G edge covers with scalar
rank q-3 by CG.

Next: control additional endpoint zero coordinates, or combine the two corner-cut
parallelograms with WT/C56-G. D2 remains a genuine full two-tree circuit separately.
```
