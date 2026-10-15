<!-- theorem-state: {"artifact_id":"ART-E84BC68D64B9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Target A — tube-only cut capacity

**Date:** 2026-09-08
**Repository base:** `7838f6c0aabe0e3d63369bda804643c3c7833426`, with pre-existing working-tree changes
**Run type:** proof and finite-model audit
**Status:** proved refinement; not promoted; Level I still open

## 1. Endpoint and dependencies

The intended implication is

`smaller exact shield charge -> weaker required sector surplus -> zeta >= s`.

Use the exact alternating orientation and linkage/rank equality of
[Section 113](../targets/target-a/03-source-response.md), and all definitions and
the geometric separation lemmas of
[Section 174](../targets/target-a/26-tube-shield-sector-balance.md).
In particular, the left shore is `B disjoint-union C^circ disjoint-union C^partial`,
the right shore is `Z disjoint-union O`, and `mu_0:B -> Z` is a perfect matching.
Matching edges are directed right to left; other edges left to right.

Write `T=T_Sigma`, `W=widehat W_Sigma`, and

`t_Sigma=|C^partial intersect V(Sigma)|`,

`delta_Sigma=sum_i max(0, |X_i|-|Z_i|-|O_i|-|C_i^circ|)`.

## 2. Theorem: only tube rows need be charged

In exactly the setting of Section 174,

\[
\operatorname{rank}S\le |T_\Sigma|
  +\sum_i\min\{|C_i^\partial|,|O_i|\},
\]

and therefore

\[
\boxed{\zeta\ge t_\Sigma+\delta_\Sigma-|T_\Sigma|.}
\]

Compared with (174.20), this improves the lower bound by exactly

\[
|V(\Sigma)\cap C^\partial|
+|V(\Sigma)\cap C^\circ|
+|T_\Sigma\cap Z|.
\]

### Proof

If `b in B intersect V(Sigma)`, its matched row `mu_0(b)` has distance less
than one from `b`, hence belongs to `T`. Consequently basis closure adds no
right vertex beyond `T`, and

\[
W=T\ \sqcup\ \mu_0^{-1}(T\cap Z)
  \ \sqcup\ (V(\Sigma)\cap C^\circ)
  \ \sqcup\ (V(\Sigma)\cap C^\partial).
\tag{1}
\]

Consider a directed path from `C^partial` to `O` that meets `W`.

* If it meets a right vertex of `W`, it meets `T` by (1).
* If it meets a basis vertex of `W`, that vertex has exactly one incoming
  edge, from its matched row in `T`. A path cannot start at a basis vertex.
* A nonbasis vertex has no incoming edge. Thus such a path cannot visit
  `C^circ`, and can visit `C^partial` only at its initial terminal.
* If this initial terminal belongs to `V(Sigma)`, its next vertex is a strict
  lattice neighbor of a point of the shield and therefore belongs to `T`.

So every path meeting `W` meets `T`. A vertex-disjoint path family contains at
most `|T|` such paths. Delete them. The remaining paths avoid `W`; Section 174
puts each in one sector, with distinct terminals and distinct sinks. At most
`min(|C_i^partial|,|O_i|)` survive in sector `i`. This proves the rank bound.

By (1), the shielded terminal count is exactly `t_Sigma`. All other terminals
belong to the sector terminal sets. Subtracting the rank bound from

`|C^partial|=t_Sigma+sum_i |C_i^partial|`

and using (174.17) proves the nullity bound. Finally (1) gives

`|W minus C^partial|=|T|+|T intersect Z|+|V(Sigma) intersect C^circ|`.

Subtracting the old lower bound gives the stated exact improvement. QED.

## 3. Exact remaining population theorem

For `s=Delta_Lambda-d_int>0`, it now suffices to find an admissible
stress-generated shield with

\[
\boxed{t_\Sigma+\delta_\Sigma\ge s+|T_\Sigma|.}
\tag{2}
\]

Section 174.1 also gives the coarser sufficient condition
`t_Sigma+delta_Sigma >= s+11|E(Sigma)|`.
For the three-channel unicyclic fan, `|E(Sigma)|=|V(Sigma)|`.
These are exact sufficient conditions, not assertions that any available fan
satisfies them. The zero-slack descent branch is not eliminated by this result.

## 4. Audit and failed stronger variants

No source/scaffold identification, geometric rank cancellation, local SDR, or
extra source Hall deficiency is used. The theorem works for the actual directed
response graph and its fixed matching. It neither moves points nor creates a
competitor. Cycles in the directed graph are harmless: linkage paths can be simple.
Deep nonbasis vertices cannot be internal path vertices because their indegree is
zero, independently of their loop status after contraction.

The tube charge cannot simply be dropped. The graph with arcs
`c -> z -> b -> o`, basis edge `z -> b`, and tube `{z}` has rank one and nullity
zero. After deleting the matched pair `{z,b}`, its terminal sector has surplus
one. Charging no tube capacity would incorrectly assert nullity at least one.
This is an abstract finite regression, not a locked unit-contact realization.

Annular full-rank responses and the Section-166 SDR collision remain compatible:
this theorem does not force a positive value of its right-hand side. The
activation/monomer regression is also unaffected. Stress-sector population
transport, not cut bookkeeping alone, is still necessary.

## 5. Computation

[tube_shield_cut_audit.py](../../research/tube_shield_cut_audit.py) enumerates all
1,024 bipartite edge sets with two basis vertices, two terminals, two interior
rows, one exterior sink, and a prescribed perfect basis matching. It checks every
right-shore tube and every admissible shield-terminal subset, using integer
matching and connected-component computations.

The experiment omits geometric realization, stress, source labels, and global
optimality. It is a finite audit of the combinatorial argument, not its proof.

## 6. Promotion recommendation

Hold as a scoped proof report pending independent review. If promoted, add the
tube-only bound to the Target A route map and Section 174, and update the active
Target A prompt, whose Section-167 endpoint is already stale. No other route is
closed by this refinement.
