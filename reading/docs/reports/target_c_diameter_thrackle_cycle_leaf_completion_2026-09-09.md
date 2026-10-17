> Generated reading edition · [exact source](../../../docs/reports/target_c_diameter_thrackle_cycle_leaf_completion_2026-09-09.md) · source SHA-256 `5a086c6c35786c0c79b0b063c6b3a94e0e22ccf1dca23d1e5278db12d1ae99b4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 4 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-A32292559208","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — the loaded diameter graph is a deleted odd-cycle spine with pendant leaves

**Date:** 2026-09-09  
**Repository branch:** `research/fullcore-interface-perimeter-2026-09-09`  
**Run type:** exact convex-thrackle structural import and endpoint application  
**Target:** full actual diameter graph on the loaded convex terminals  
**Depends on:** C65 loaded-terminal setup; standard maximal convex-thrackle classification; EP only for the final quantitative corollary  
**External source:** R. Fabila-Monroy and D. R. Wood, *The Chromatic Number of the Convex Segment Disjointness Graph*, LNCS 7579 (2012), 79–84, Section 2. The source states that every maximal convex thrackle on a set of points in convex position consists of an odd cycle together with degree-one vertices adjacent to cycle vertices, and hence has exactly `q` edges.  
**Computation:** displayed decimals only

## LEVEL I STATUS

`STILL OPEN`

Let `H` be the complete actual diameter graph on the `q` loaded force-hull terminals `B_+`. Because the terminals are in strictly convex position and any two disjoint diameter segments cross, `H` is a convex thrackle.

Every loaded terminal is an endpoint of at least one actual diameter edge, so

```math
\boxed{\delta(H)\ge1.}
\tag{TC.1}
```

Extend `H` greedily, on the same vertex set, to an edge-maximal convex thrackle `T`. The classical convex-thrackle classification gives an odd cycle `C` such that every vertex outside `C` is a leaf adjacent to one cycle vertex, and

```math
|E(T)|=q.
```

Write

```math
d_H:=q-h,
\qquad h=|E(H)|.
```

Then `T\setminus H` has exactly `d_H` edges. None of those deleted edges can be a pendant leaf edge of `T`: deleting the unique edge incident to a leaf of `T` would make that vertex isolated in `H`, contradicting TC.1.

Therefore every missing edge lies on the odd cycle `C`.

### Theorem TC — cycle-leaf completion

There exists a maximal convex thrackle `T` on the loaded terminals with odd-cycle spine `C` such that

```math
\boxed{
H=T-F,
\qquad
F\subseteq E(C),
\qquad
|F|=d_H.
}
\tag{TC.2}
```

Equivalently:

- every vertex outside `C` has degree exactly one in the **actual diameter graph** and its unique diameter edge joins it to a vertex of `C`;
- all missing edges relative to the maximal convex thrackle are cycle edges;
- if `d_H=0`, the actual diameter graph itself is one odd cycle with pendant leaves;
- if `d_H>0`, deleting the `d_H` cycle edges cuts the spine into `d_H` path pieces, with the same pendant leaves attached to their spine vertices.

Thus the earlier statement that the diameter graph is merely a pseudoforest can be sharpened: all tree components are pieces of one common cyclic spine, not arbitrary trees.

At the minimal-interface endpoint, EP gives

```math
d_H+s_Z\le0.07571193869\ldots D+o(D),
```

hence

```math
\boxed{|F|=d_H\le0.07571193869\ldots D+o(D).}
\tag{TC.3}
```

Since `q=(pi+o(1))D`, at most about `2.41%` as many spine edges as loaded terminals are deleted.

This is a genuine structural reduction, but it does not yet imply that most loaded terminals lie on the cycle spine: the maximal convex thrackle may have many pendant leaves. The next metric question is therefore to control the pendant population using the near-circle diameter geometry.

---

## 1. Why the actual diameter graph is a convex thrackle

Take two distinct diameter edges `ab` and `cd` with no common endpoint. All four endpoints lie on the boundary of the convex force hull. If the two chords did not cross, one endpoint pair would lie in the same boundary arc determined by the other chord. The standard diameter-chord lemma for a planar set then gives a pair at distance strictly greater than the common diameter, a contradiction. Equivalently, this is the familiar fact already used throughout Target C that disjoint actual diameter chords of a convex point set cross.

Thus every pair of edges of `H` either shares an endpoint or crosses, exactly the definition of a convex thrackle.

C65/relative-interior support uses `B_+` as the loaded terminals. Every `b in B_+` is an endpoint of a positive diameter reaction and hence of an actual diameter edge. Therefore `H` has no isolated vertices, proving TC.1.

---

## 2. Maximal convex-thrackle completion

The vertex set is finite. Add any chord between loaded terminals whose addition preserves the convex-thrackle property, and repeat until no such chord remains. The resulting `T` is a maximal convex thrackle and contains `H` as a spanning subgraph.

The standard classification of maximal convex thrackles on points in convex position states:

1. `T` contains one odd cycle `C`;
2. every vertex outside `C` has degree one;
3. every such leaf is adjacent to a vertex of `C` determined by its convex wedge;
4. `|E(T)|=|V(T)|=q`.

No metric statement is imported: edges added in `T\setminus H` need not be diameter edges.

Since `H` has `h=q-d_H` edges,

```math
|E(T)\setminus E(H)|=q-h=d_H.
\tag{2.1}
```

---

## 3. Deleted leaf edges are impossible

Let `u` be a leaf of `T`, with unique incident edge `uv`. Suppose `uv` were absent from `H`.

Because `H\subseteq T`, `u` would then have degree zero in `H`. But every loaded terminal is an actual diameter endpoint, so `deg_H(u)>=1`. Contradiction.

Hence every pendant edge of `T` is present in `H`.

Therefore

```math
E(T)\setminus E(H)\subseteq E(C).
```

Together with (2.1), this proves TC.2.

A useful exact consequence is that every off-spine vertex has **exactly one** actual diameter partner. This is stronger than merely saying it is a leaf in some maximal completion: its unique maximal-thrackle edge is already an actual diameter edge.

---

## 4. Component structure after deleting cycle edges

If `d_H=0`, no cycle edge is deleted and `H=T`: one odd cycle plus pendant leaves.

Suppose `d_H>0`. Deleting `d_H` edges from the single cycle `C` breaks it into exactly `d_H` vertex-disjoint path segments, allowing a zero-edge segment only if two deleted cycle edges are adjacent. Every pendant leaf stays attached to its original spine vertex.

Thus each connected component of `H` is a caterpillar whose non-leaf core is a path segment of `C`, except that a one-spine-vertex component may be a star.

The number of tree components is exactly `d_H`, recovering the existing pseudoforest interpretation but now with a common cyclic completion.

Since `H` has no isolates, a spine vertex isolated by two adjacent deleted cycle edges must carry at least one pendant leaf. This gives a small local restriction on clusters of missing cycle edges.

---

## 5. Minimal-interface quantitative corollary

EP proves in the sharp full-core near-circle interface branch

```math
d_H+s_Z
\le c_*D+o(D),
\qquad
c_*:=\frac25(\pi-2-\sqrt\Delta)
=0.07571193869\ldots .
```

Since both currencies are nonnegative,

```math
|F|=d_H\le c_*D+o(D).
```

With `q=(pi+o(1))D`,

```math
\frac{|F|}{q}
\le
\frac{c_*}{\pi}+o(1)
=0.0240998586\ldots+o(1).
```

Thus the actual diameter graph is obtained from one maximal odd-cycle-plus-leaves convex thrackle by deleting at most about `2.41%` as many cycle edges as there are terminals.

The conclusion is stronger than the edge-density statement `h/q>=0.9759...`: it identifies **where every missing edge must occur**.

---

## 6. What this does not prove

The maximal spine `C` may have sublinear, linear, or nearly full cardinality. TC alone does not show that most terminals are cycle vertices.

A large pendant population is compatible with abstract maximal convex-thrackle structure. The metric diameter condition adds more information:

- every retained pendant edge is an exact diameter;
- every retained cycle edge is an exact diameter;
- in the near-circle regime all diameter partners of one center lie in an `o(1)` angular neighborhood of its antipode;
- the loaded shell has unit spacing at all but `o(D)` consecutive intervals.

The next theorem should use those metric facts to bound the number or total angular width of pendant blocks attached to a spine vertex. No such bound is assumed here.

---

## 7. Literature source and scope

The maximal convex-thrackle classification is stated in Section 2 of:

Ruy Fabila-Monroy and David R. Wood, *The Chromatic Number of the Convex Segment Disjointness Graph*, in *Computational Geometry*, LNCS 7579, Springer, 2012, pp. 79–84, DOI `10.1007/978-3-642-34191-5_7`.

Their statement is combinatorial/geometric for points in convex position. It does not concern diameter graphs or Erdős Problem #99. The new deduction here is the no-deleted-leaf-edge observation from the source-specific fact that every loaded terminal has positive actual diameter degree.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| actual diameter graph is a convex thrackle | established repository geometry |
| maximal completion is odd cycle plus pendant leaves | external classical convex-thrackle theorem |
| every completion leaf edge already lies in `H` | proved | otherwise loaded vertex is isolated in `H` |
| all `d_H` missing edges are cycle edges | proved | edge count + previous row |
| every H component is a path-spine caterpillar/star | proved | delete cycle edges from one completed spine |
| `d_H<=0.075712D+o(D)` at minimal interface | proved conditional on EP endpoint |
| most terminals lie on the cycle spine | not proved | pendant population remains a metric obstruction |
| Level I | still open | need near-circle control of pendant blocks |

---

## 9. Next target

For a spine vertex `v`, all of its actual diameter partners — its retained cycle neighbors and every pendant leaf assigned to `v` — lie on one exact radius-`D` circle centered at `v`. In the near-circle limit they occupy one shrinking boundary arc near the antipode of `v`.

The maximal convex-thrackle wedge structure makes the pendant leaves assigned to `v` a contiguous boundary block between the two spine-neighbor rays. The loaded shell has asymptotically unit spacing.

A useful metric lemma would compare the length of that pendant block with the deficit of the two adjacent spine diameter directions from exact antipodality. Summing over the odd spine could then turn a large pendant population into either

- a positive force-hull perimeter deficit, contradicting the `q~pi D` near-circle endpoint at the relevant rate; or
- additional missing cycle edges/diameter branching beyond the EP budget.

Until that metric step is proved, TC should remain a report-level structural import.
