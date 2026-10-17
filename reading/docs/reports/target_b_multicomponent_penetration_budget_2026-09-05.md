> Generated reading edition · [exact source](../../../docs/reports/target_b_multicomponent_penetration_budget_2026-09-05.md) · source SHA-256 `d855c448a3daa7d09962a0e4089aeaf3d50eca15c5ea2dadc10eb6c9bd8ae843`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0341E61F348F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Erdos Problem #99 - Target B multicomponent penetration budget

**Date:** 2026-09-05  
**Run type:** exact bounded-multiplicity aggregation  
**Target:** Section-50 coherent components + PC1/PC3  
**Depends on:** PC1/PC3 penetration-charged grid cancellation; Section-50 retained-component decomposition  
**LEVEL I STATUS:** STILL OPEN

## 1. Setup

Let the pure rhombic train-crossing graph be pruned as in Theorem 50.1, producing retained connected components

`H_1,...,H_m`.

For each selected component `H_j`, choose two internally noncrossing train subfamilies

`A_j,B_j subset V(H_j)`

that form a complete crossing grid. Write

`|A_j|=M_j`, `|B_j|=b_j`.

Choose trim depths `k_j,l_j` and let

`d_j=min(k_j,l_j)-2>0`.

Let the central grid vector sums be `U_j,V_j` as in PC1.

For the selected deep diagonal of grid `j`, let `X_j` be the set of physical rhombus crossings between a separator train outside `A_j union B_j` and a train of `A_j union B_j` that are used in the PC1 penetration count. PC1 gives

`|X_j| >= d_j (|U_j+V_j|-D)_+`.                       (1.1)

The internal complete-grid crossings contribute the disjoint set

`G_j=A_j x B_j`,

with

`|G_j|=M_j b_j`.                                       (1.2)

## 2. Global multiplicity is at most two

For distinct retained components `H_i,H_j`, the internal grid sets `G_i,G_j` are disjoint because their train endpoints lie in different components.

A physical crossing edge can belong to at most two of the external penetration sets `X_j`:

- if its endpoints lie in retained components `H_i,H_j`, it can be charged only from the grid in `H_i` and/or the grid in `H_j`;
- if exactly one endpoint lies in a retained component and the other train was pruned, it can be charged only from the retained endpoint's component;
- if both endpoints lie in one retained component, it can occur only in that component's penetration set;
- an internal grid edge in `G_j` cannot also lie in `X_j`, because every train counted in `X_j` is outside `A_j union B_j`.

Therefore every physical rhombus is counted at most twice in

`sum_j (|G_j|+|X_j|)`.

If `R` is the total number of rhombi, then

### Theorem MCP1 - multicomponent PC1 budget

`boxed{
2R >= sum_j [ M_j b_j + d_j(|U_j+V_j|-D)_+ ].
}`                                                       (2.1)

This is exact and finite.

It allows the same deleted crossing between two retained components to help cancel both selected grid diagonals; the factor two is precisely the worst possible reuse.

## 3. Coherent-component interface refinement

Now use the PC3 notation for each retained component. Let

`E_del(H_j)`

be the number of deleted physical crossing edges with one endpoint in `H_j` and one endpoint outside `H_j`. Let `M'_j,b'_j` be the trimmed dimensions.

For an `o(1)`-coherent triangular phase component, PC3 gives the componentwise penetration lower bound

`P_j := [ d_j(M'_j+b'_j-2D/sqrt(3)-o(D))`

`          -(2/sqrt(3)-1)E_del(H_j) ]_+`.              (3.1)

The same multiplicity argument gives

`2R >= sum_j [M_j b_j + P_j]`.                         (3.2)

There is also a global bound on the interface terms. Every deleted crossing edge with endpoints in two retained components contributes once to each endpoint component, while an edge from a retained component to a pruned train contributes once. Hence

`sum_j E_del(H_j) <= 2 E_del`,                         (3.3)

where `E_del` is the total number of crossing edges deleted by Theorem 50.1.

The componentwise little-oh term in (3.1) is summable in the Section-50 regime. Fix the pruning threshold `lambda>0` before sending `D` to infinity. Every nonempty retained component has minimum degree at least `lambda D`, hence at least `lambda D+1` train vertices. The total train count is `T=O(D)`. Therefore there are only `O_lambda(1)` retained components. Also every trim depth satisfies `d_j=O(D)`, and the selected coherent components have a uniform `o(1)` angular error. Consequently the total coherence loss contributed by the terms `d_j o(D)` is `o(D^2)` for fixed `lambda`. This quantifier order is required in the additive form below.

Using `[x-y]_+>=x-y` gives the weaker but additive form

### Theorem MCP2 - additive three-phase/interface budget

`boxed{
2R >= sum_j M_j b_j
      + sum_j d_j(M'_j+b'_j-2D/sqrt(3)-o(D))
      - 2(2/sqrt(3)-1)E_del.
}`                                                       (3.4)

Here the sum of all displayed coherence-error contributions is `o(D^2)` for fixed `lambda`, by the preceding paragraph. Terms with negative diagonal excess may simply be omitted instead of using (3.4); the positive-part form (3.2) is the sharper statement.

Theorem 50.1 supplies

`E_del <= C_delta D^(2-eta)+C_T lambda D^2`.           (3.5)

Thus for fixed lambda and large D, the total loss from arbitrary inter-component/pruned-train cancellation is explicitly of order `lambda D^2`, with coefficient

`2 C_T(2/sqrt(3)-1)`

in (3.4).

## 4. Why this still does not close from the present density theorem

PDG extracts from a phase pair of crossing density `rho` a complete grid with guaranteed shore sizes only

`rho^2 M/128`

and

`rho b/4-O(1)`.

Theorem 50.1 by itself gives retained minimum degree `lambda D`, but preserving all but `o(D^2)` of the physical rhombi requires taking `lambda` small. Consequently its bare degree floor can force only small fixed-fraction grids. For such grids

`M'_j+b'_j <= 2D/sqrt(3)`

is compatible with all current constants, so the PC3 penetration term may vanish completely.

Therefore MCP1-MCP2 do **not** close Level I from Section 50 + PDG alone.

This failure is informative: the remaining global step must use more than positive crossing density. It must force one of:

1. a component/grid whose two coherent shore populations sum above the `2D/sqrt(3)` phase-cancellation threshold;
2. many smaller grids whose geometric diameter costs combine more strongly than the factor-two crossing reuse in MCP1;
3. a new quantitative coupling of the local Theorem-51 crossing deficit to virtual noncrossing determinant mass, improving grid extraction beyond the density-only `rho^2` scale.

## 5. Interface with the current virtual-area dichotomy

**Publication scope note:** the historical GPS1/virtual-area lead is not retained
in this corpus and is not a premise of MCP1 or MCP2. No general certificate
allowing arbitrary component pruning is supplied here. The retained
[route Sections 26.4–26.5 and 51](../targets/target-b/01-jammed-rhombic-branch.md)
define zonotope/missing-pair area and the cyclic-order deficit. A new argument
would have to connect those quantities to support depth and internal virtual
noncrossing determinant mass. MCP2 supplies the complementary physical currency:
deleted train crossings that allow arbitrary external cancellation.

Thus the current Target B endpoint can be phrased without ambiguity:

- virtual missing pairs pay zonotope/support-depth area;
- deleted physical pairs pay the PC3 cancellation-interface term;
- retained physical pairs must either remain spread among subcritical grids or create a forbidden deep grid.

A closure now requires a quantitative inequality coupling these three mutually exclusive uses of train pairs.

## Handoff

```text
For complete grids selected in distinct retained Section-50 components:

  2R >= sum_j [M_j b_j + X_j],

because a physical crossing can be used in at most two component penetration counts.
PC1 gives X_j>=d_j(|U_j+V_j|-D)_+.

In the coherent PC3 form,

  2R >= sum_j [M_j b_j + P_j],

  P_j=[d_j(M'_j+b'_j-2D/sqrt(3)-o(D))
       -(2/sqrt(3)-1)E_del(H_j)]_+,

and

  sum_j E_del(H_j)<=2E_del.

For fixed Section-50 lambda, the number of retained components is O_lambda(1), so the summed phase-coherence error is o(D^2).

This closes the deleted-edge double-counting issue exactly. The remaining gap is quantitative grid size: density-only PDG can still extract grids below the 2D/sqrt(3) cancellation threshold.
```
