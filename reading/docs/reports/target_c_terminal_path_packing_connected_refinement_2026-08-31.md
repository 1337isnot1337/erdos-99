> Generated reading edition · [exact source](../../../docs/reports/target_c_terminal_path_packing_connected_refinement_2026-08-31.md) · source SHA-256 `470a00058e940a4ce461ad720df267a624707b6d119a50b586f27802857b53b9`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-FE58D36D5085","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: connected-quotient refinement of terminal-path packing

**Date:** 2026-08-31
**Target:** Target C-II, non-additive response branch
**Depends on:** C26, C34, C35, and the Gallai T-path formula
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

The earlier TP5 bound used only the degree capacity of a separator. The connected
quotient of the deleted graph gives a stronger exact estimate. If `G` is connected,
`T` has `q>=2` terminals, terminal degree is at most 3, and nonterminal degree is
at most 5, then

```
nu_T(G) >= (q-1)/4.
```

Thus a circular-planar realization contains at least

```
floor((q-1)/8)
```

pairwise terminal-disjoint circular two-connections and strict size-two circular
response minors. In C-II, C34 turns this into at least

```
floor(ceil(D)/16)
```

terminal-disjoint strict minors. This improves the TP5 count by a constant factor,
but still gives no numerical lower bound on any individual minor.

## 1. Theorem CR4

Let `G` be a connected finite graph and `T` a terminal set of size `q>=2`. Assume

```
degree(t) <= 3 for t in T,
degree(v) <= 5 for v outside T.
```

Let `nu_T(G)` be the maximum number of pairwise vertex-disjoint T-paths, where a
T-path has distinct terminal endpoints and no internal terminal. Then

```
nu_T(G) >= (q-1)/4.
```

Equivalently, since `nu_T(G)` is integral,
`nu_T(G) >= ceil((q-1)/4)`.

If `G` is embedded as a positive circular-planar network with all terminals on the
boundary in cyclic order, then it contains at least

```
floor((q-1)/8)
```

pairwise terminal-disjoint circular two-connections. Each gives a strict size-two
circular minor of the terminal response.

## 2. Proof of the packing bound

Gallai's exact T-path theorem gives

```
nu_T(G) = min_X ( |X| + sum_K floor(|T intersect K|/2) ),
```

where `K` ranges over the components of `G-X`.

Fix a nonempty `X`. Write

```
x0 = |X outside T|,
x1 = |X intersect T|,
x  = x0+x1,
F_X = sum_K floor(|T intersect K|/2).
```

Let `N` be the number of all components of `G-X`, including components with no
terminal. Let `c_X` be the number of connected components of the induced graph
`G[X]`, and let `e_X` be its number of internal edges. Let `e_boundary` be the
number of edges with one endpoint in `X` and one endpoint in `G-X`.

Contract every component of `G[X]` and every component of `G-X`. The resulting
quotient is connected because `G` is connected, and all its edges are represented
by crossing edges. Therefore

```
e_boundary >= c_X + N - 1.
```

On the other hand, summing degrees over `X` gives

```
2*e_X + e_boundary <= 5*x0 + 3*x1.
```

Every component of `G[X]` contains at least one spanning tree, so
`e_X >= x-c_X`. Hence

```
c_X + N - 1
    <= 5*x0 + 3*x1 - 2*x + 2*c_X,
```

and therefore

```
N <= 5*x0 + 3*x1 - 2*x + c_X + 1
  <= 4*x0 + 2*x1 + 1,
```

using `c_X<=x`.

Now let `N_T` be the number of terminal-bearing components of `G-X`, and write
`t_K=|T intersect K|` for each such component. Since

```
t_K <= 2*floor(t_K/2) + 1,
```

we obtain

```
q = x1 + sum_{K: t_K>0} t_K
  <= x1 + 2*F_X + N_T
  <= x1 + 2*F_X + N
  <= 4*x0 + 3*x1 + 2*F_X + 1
  <= 4*(x+F_X) + 1.
```

Thus every nonempty `X` has Gallai value

```
|X|+F_X >= (q-1)/4.
```

For `X` empty, connectedness gives Gallai value `floor(q/2)`, which is also at
least `(q-1)/4`. Taking the minimum proves the first assertion.

## 3. Circular-planar consequence

Take a maximum packing of `nu_T(G)` vertex-disjoint T-paths and pair its paths
arbitrarily. For each pair, the four terminal endpoints cannot alternate around
the boundary: otherwise the two embedded paths would intersect. Each pair is
therefore a circular two-connection. The pairs are terminal-disjoint, so their
number is at least

```
floor(nu_T(G)/2) >= floor((q-1)/8).
```

The circular-minor connection theorem makes each associated size-two response
minor strict under positive circular-planar conductances.

## 4. Exact C-II implication

In fully force-visible C-II, apply the theorem to the positive contact graph with
terminal set `T=B_+`. C26 and C35 supply the degree bounds, while C34 gives

```
2*|B_+| >= ceil(D)+2.
```

Consequently

```
nu_(B_+)(C) >= (|B_+|-1)/4 >= ceil(D)/8,
```

and the circular-planar response has at least

```
floor((|B_+|-1)/8) >= floor(ceil(D)/16)
```

pairwise terminal-disjoint strict circular minors.

This rules out a bounded-size family of circular connections in the non-additive
branch. It does not rule out strict minors whose numerical values all tend to zero.

## 5. Sharpness and audit limits

The coefficient `1/4` cannot be improved from the degree and connectedness
hypotheses alone. For each `k`, take `k` nonterminal hubs, attach four terminal
leaves to each hub, and attach each hub by its fifth edge to a distinct leaf of a
connected terminal-free tree. The hubs have degree five, all terminals have degree
one, and the graph is connected. Deleting the hubs gives Gallai value `k`, while
the four terminal leaves at each hub provide one disjoint T-path, so

```
q=4*k,
nu_T(G)=k=q/4.
```

This is a graph regression only; it is not asserted to be a unit-contact KKT
framework or a global minimizer.

The theorem does not produce any lower bound for an individual circular minor. A
positive-conductance network can make the connections strict while sending their
minor values to zero. It therefore does not yet imply the C41 trace gap or a C42
global-packing contradiction.

## 6. Dependencies and literature input

- C26/C35: fully force-visible nonterminal and terminal degree bounds.
- C34: `2|B_+|>=ceil(D)+2`.
- The Gallai formula is Theorem 2 in T. Kaiser,
  [*Disjoint T-paths in tough graphs*](https://iti.mff.cuni.cz/series/2005/270.pdf).
- Strictness of a circular minor from a circular two-connection is Lemma 3.4 in
  S. Forcey, [*Kalmanson-Kron reconstruction*](https://sforcey.github.io/sf34/kron.pdf).

## 7. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| `nu_T(G)>=(q-1)/4` | proved with literature input | Connected quotient plus degree counting in Gallai's formula. |
| Paired paths give circular two-connections | proved | Disk planarity forbids alternating endpoint pairs. |
| Each connection gives a strict response minor | literature import | Forcey Lemma 3.4 under positive circular-planar conductances. |
| C-II has at least `floor(ceil(D)/16)` strict minors | proved | CR4, C26, C34, and C35. |
| The constant improves to a universal numerical minor size | not proved | No individual conductance lower bound is available. |
| Target C is closed | not proved | C-I and the remaining C-II geometric branches remain open. |

## 8. Exact next lemma

> **Weighted connected-quotient transport.** Couple the CR4 terminal-path packing
> to the positive contact-stress distribution so that a linear family of
> terminal-disjoint connections carries a quantitative aggregate response weight.

Any such statement must use more than graph degrees: the sharp hub/tree regression
shows that topology alone cannot supply the missing conductance magnitude.
