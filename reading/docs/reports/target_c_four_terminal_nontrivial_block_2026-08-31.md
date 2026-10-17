> Generated reading edition · [exact source](../../../docs/reports/target_c_four_terminal_nontrivial_block_2026-08-31.md) · source SHA-256 `e00b97f2f025c719f8c780aa62ae6e75d3e4822097529bd62d71e472dd238521`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-588096315A95","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_four_terminal_nontrivial_block_2026-08-31.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=4c4863f5373f07349002ee3fa31ea08435c22525; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C C34: every nontrivial bridge block has four loaded-or-bridge terminals

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** C26, canonical C31 loaded-block pinned budget, Eppstein 2018 Lemmas 1–2  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Eppstein's degeneracy proof contains a local statement stronger than the edge-count inequality: every cyclic triangle-free penny graph has at least four distinct non-articulation vertices of degree at most two; in the biconnected case, at least four vertices have degree exactly two.

A nontrivial positive-contact bridge block has no internal bridges, so its internal contact graph contains a cycle and has minimum internal degree at least two. Hence it has at least four distinct internal degree-two vertices.

C26 says an unloaded contact vertex in fully force-visible C-II has full contact degree at least three. Therefore every one of those four internal degree-two vertices is either positively diameter-loaded or incident to a bridge leaving the block. Distinct vertices require distinct bridge edges. Thus, for every nontrivial bridge block `X`,

```math
\boxed{q_X+k_X\ge4,}
```

where `q_X=|B_+\cap X|` and `k_X` is bridge-tree degree.

---

## 1. Eppstein import and block application

The repository copy of Eppstein, *Edge Bounds and Degeneracy of Triangle-Free Penny Graphs and Squaregraphs* (2018), proves that a biconnected triangle-free penny graph has at least four degree-two vertices and, via its block-tree argument, that a cyclic triangle-free penny graph has at least four non-articulation vertices of degree at most two.

Let `G_X=C[V(X)]` be the internal contact graph of a nontrivial bridge block. Every internal edge is non-bridge in the full contact graph and therefore lies on a cycle contained in `G_X`; in particular `G_X` is cyclic. Its minimum internal degree is at least two: an internal degree-one edge would be a bridge.

Thus Eppstein supplies four distinct vertices

```math
Z_X=\{z_1,z_2,z_3,z_4\}
\tag{C34.1}
```

of internal degree exactly two.

If `z in Z_X\setminus B_+`, then C26 gives full contact degree at least three, so at least one unit contact at `z` leaves `X`. Such an inter-block contact is a bridge of the full contact graph. One bridge has only one endpoint in `X`, so different vertices of `Z_X\setminus B_+` require different incident bridges.

Let `l=|Z_X\cap B_+|`. Then

```math
q_X\ge l,
\qquad
k_X\ge4-l,
```

and hence:

### Theorem C34

```math
\boxed{q_X+k_X\ge4.}
\tag{C34.2}
```

---

## 2. Consequences

For a nontrivial bridge block:

```math
\begin{array}{c|c}
k_X&\text{forced }q_X\\ \hline
1&q_X\ge3\\
2&q_X\ge2\\
3&q_X\ge1\\
q_X=0&k_X\ge4
\end{array}
\tag{C34.3}
```

Thus:

- a nontrivial leaf block contains at least three loaded vertices;
- a nontrivial degree-two block contains at least two loaded vertices;
- a degree-two block with only one loaded vertex is necessarily a singleton;
- a reaction-free nontrivial block has at least four bridge directions.

C39 below will sharpen the last statement to `k_X>=5` using the positive self-stress surplus.

---

## 3. Comparison with canonical C31

Canonical C31 gives

```math
\delta_X\le2q_X+k_X-2.
```

Since a nontrivial triangle-free bridge block has `delta_X>=2`, this only implies

```math
2q_X+k_X\ge4.
```

C34 improves the coefficient of the loaded term:

```math
q_X+k_X\ge4.
```

The gain comes from four distinct low-degree vertices, not from the total edge count.

---

## 4. Regression audit

- **Unit square isolated block:** `q=4,k=0`, equality.
- **Reaction-free square with four bridge attachments:** `q=0,k=4`, allowed by C34 but later excluded by C39.
- **One-loaded square with two bridges:** `q=1,k=2`, excluded.
- **Singleton blocks:** outside the theorem and remain allowed in the C26 cases.

```text
C34:
Every nontrivial bridge block contains four distinct internal degree-two vertices by
Eppstein.  C26 forces each to be loaded or to carry a distinct outgoing bridge.  Hence
    q_X+k_X>=4.
This removes one-loaded degree-two 2D gadgets from long bridge paths.
```
