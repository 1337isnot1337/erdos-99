> Generated reading edition · [exact source](../../../docs/reports/target_b_balanced_phase_stability_exclusion_2026-09-05.md) · source SHA-256 `e97160e75d88c5639f589460dc7b92aecae7856647e63c0cad9d1cd5dcf94e26`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-BA27A63D6904","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Erdős Problem #99 — Target B balanced phase stability exclusion

**Date:** 2026-09-05  
**Run type:** robust equality classification + ordered train extraction  
**Target:** balanced coherent three-phase endpoint  
**Depends on:** trimmed-grid phase-star exclusion  
**LEVEL I STATUS:** STILL OPEN

## 1. Balanced tripartite stability

Let `G` be a tripartite graph with classes `A,B,C`, each of size `m`, and no transversal triangle. Suppose

`E >= (2-epsilon)m^2`.

For a triple `(a,b,c)` define

`d(a,b,c)=2-[1_(ab)+1_(bc)+1_(ca)]`.

Triangle-freeness gives `d>=0`. Summing over all triples,

`D_3:=sum_(a,b,c)d(a,b,c)=2m^3-mE<=epsilon m^3`.

We show that one phase pair has only `O(sqrt(epsilon))m^2` missing edges.

## 2. Find a low-defect nonedge anchor

If the `A`–`B` pair already has at most `4sqrt(epsilon)m^2` nonedges, we are done.

Otherwise call `a in A` slice-bad if

`sum_(b,c)d(a,b,c)>sqrt(epsilon)m^2`,

and define slice-bad `b in B` analogously. There are at most `sqrt(epsilon)m` bad vertices on each shore.

At most `2sqrt(epsilon)m^2` `A`–`B` nonedges touch a bad vertex. Hence more than `2sqrt(epsilon)m^2` nonedges have both endpoints slice-good.

For an `A`–`B` pair put

`d(ab)=sum_c d(a,b,c)`.

Since the total over all pairs is `D_3`, some slice-good nonedge `a_0b_0` satisfies

`d(a_0b_0)<=sqrt(epsilon)m/2`.

Because `a_0b_0` is absent,

`d(a_0,b_0,c)=2-1_(a_0c)-1_(b_0c)`.

Therefore all but at most `sqrt(epsilon)m/2` vertices of `C` are adjacent to both `a_0` and `b_0`. Let this common-neighbor set be `C_*`; then

`|C_*| >= (1-sqrt(epsilon)/2)m`.

## 3. Approximate two-colouring

Split

`A=A_0 sqcup A_1`, where `A_1=N(b_0) cap A`,

`B=B_0 sqcup B_1`, where `B_1=N(a_0) cap B`.

For `c in C_*`:

- every `A_1`–`C_*` edge is absent, otherwise `a b_0 c` is a transversal triangle;
- every missing `A_0`–`C_*` edge contributes at least one defect to the slice through `b_0`.

Because `b_0` is slice-good, at most `sqrt(epsilon)m^2` `A_0`–`C_*` edges are missing. Symmetrically, all `B_1`–`C_*` edges are absent and at most `sqrt(epsilon)m^2` `B_0`–`C_*` edges are missing.

For `a in A_1`, `b in B_1`, `c in C_*`, both `ac` and `bc` are absent, so

`d(a,b,c)>=1`.

Hence

`|A_1||B_1||C_*|<=D_3<=epsilon m^3`.

For small `epsilon`, `|C_*|>=m/2`, so

`min(|A_1|,|B_1|)<=sqrt(2epsilon)m`.

If `A_1` is smaller, the missing `A`–`C` edges are contained in:

1. all pairs incident with `A_1`;
2. all pairs incident with `C\C_*`;
3. the at most `sqrt(epsilon)m^2` missing `A_0`–`C_*` pairs.

Thus `A`–`C` has only `O(sqrt(epsilon))m^2` missing edges. If `B_1` is smaller, the same conclusion holds for `B`–`C`.

### Theorem BS1 — balanced tripartite stability

If a transversal-triangle-free tripartite graph with three classes of size `m` has

`E >= (2-epsilon)m^2`,

then some pair of classes has at most

`O(sqrt(epsilon))m^2`

missing edges.

In particular, if `E=(2-o(1))m^2`, one phase pair is `1-o(1)` complete.

## 4. Ordered train extraction

In a coherent phase class, train tracks are pairwise noncrossing. For a second class, every train has a consecutive crossing interval in the first class.

Apply the dense interval-bigraph extraction from the unique-max stability theorem. From a phase pair with `o(m^2)` missing crossings, obtain subfamilies

`A'`, `B'`

with

`|A'|=m-o(m)`,

`|B'|=m-o(m)`

and complete mutual crossing.

Assume the standard dense-core pruning leaves only `o(m^2)` crossings outside the coherent three-phase core.

## 5. Diameter contradiction

Use the retained complete grid in the trimmed-grid theorem. The third phase has at most `m+o(m)` trains and may contribute its worst coherent linear cancellation.

After normalization,

`t=1-o(1)`, `0<=s<=1+o(1)`.

At `t=1`, the exact constrained minimum is

`F(s,1)=3`

for every `0<=s<=1`.

Therefore

`D^2 >= (3-o(1))m^2`.

But a balanced near-extremal core has

`R=(2-o(1))m^2`

and `T=O(m)`, hence

`n=(2-o(1))m^2`.

The strict translated-lattice comparison gives

`D(n)^2 < (2c+o(1))m^2`,

where

`2c=4sqrt(3)/pi=2.2053155817...<3`.

Contradiction.

### Theorem BS2 — balanced near-extremal coherent phase cores are impossible

No sufficiently large pure-rhombic global-minimizer sequence can contain a balanced coherent phase core carrying all but `o(m^2)` of its quadratic crossings and satisfying

`E=(2-o(1))m^2`.

## 6. Scope

This theorem handles the exactly balanced/equal-size stability model. The asymptotically balanced and two-largest-tie regimes require a small additional reduction; they are not asserted here without that reduction.
