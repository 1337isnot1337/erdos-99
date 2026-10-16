<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d00066b00698b2185d049ec40bc9bc3fcf984f33", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_adjacent_switching_thrackle_order_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "973d815a705b9483634f4aeabe5ae81fe0a97b24420cc39ca50d08d2906cbcef"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — adjacent switching one-arc thrackle interface

**Date:** 2026-09-15  
**Reviewed:** `research/target_c_adjacent_switching_thrackle_order_2026-09-15.md`  
**Disposition:** **PASS at its stated proof-only exact structural scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate refines the bounded switching set left by the triple-small opposite-shear theorem. Its main claim is purely topological/order-theoretic: for two consecutive laminar O-O cuts, every switching diameter has one endpoint in the unique middle layer; if both switch orientations occur, all such middle endpoints lie on one common outer-boundary arc and split into one right-switch prefix and one left-switch suffix, with at most one common hub.

The audit checks the layer indexing, the four-block boundary topology, the convex-thrackle crossing test, degeneracies from shared endpoints, and the caterpillar consequence.

---

## 1. Interval support really forces a middle-layer endpoint

For an actual diameter edge with endpoint layers `a<b`, the laminar interval theorem gives support

\[
I_h=\{a+1,\ldots,b\}.
\]

For consecutive columns `i,i+1`:

- `i in I_h`, `i+1 notin I_h` forces `b=i`; hence the edge joins a layer `<i` to layer `i`;
- `i notin I_h`, `i+1 in I_h` forces `a=i`; hence the edge joins layer `i` to a layer `>i`.

Thus the switching graph has bipartition

\[
M\quad\text{versus}\quad L\cup R.
\]

There is no fourth interval-support case hidden by the signed incidence convention: sign is constant on a row's nonzero interval, so a change between adjacent columns is exactly an interval start or stop.

**Verdict:** PASS.

---

## 2. The switching graph is a forest

The actual diameter graph is an audited convex geometric thrackle. Every cycle in such a diameter graph is odd. The switching subgraph is bipartite by the previous section, so every graph cycle would be even. Therefore it has no cycle.

This conclusion does not need the stronger caterpillar theorem and does not use a KKT-weight lower bound.

**Verdict:** PASS.

---

## 3. Two disjoint proper crosscuts give exactly the claimed four boundary blocks

Two consecutive selected O-O trains are represented by disjoint proper crosscuts of the outer-face disk. Removing the two crosscuts gives three regions in a path: left, middle, right. The left and right regions each meet the disk boundary in one open arc; the middle region meets it in the other two open arcs. Therefore, after choosing an orientation, the four outer-boundary arcs occur cyclically as

\[
B_L,\ B_M^+,\ B_R,\ B_M^-.
\]

Unselected train crosscuts may subdivide these regions internally, but they do not change this coarse four-block classification relative to the two selected crosscuts.

Every actual diameter endpoint is an extreme point of the source convex hull. If `p=lambda a+(1-lambda)b` with `0<lambda<1` and `a!=b`, strict convexity gives

\[
|p-y|^2
<\lambda|a-y|^2+(1-\lambda)|b-y|^2
\le D^2,
\]

contradicting `|p-y|=D`. Hence the diameter endpoints used in the chord argument lie on the source outer boundary, and their outer-face order agrees with convex-hull cyclic order.

**Verdict:** PASS.

---

## 4. Opposite middle arcs cannot support opposite switch orientations

Take a left-switch edge of type `B_L-B_M^+` and a right-switch edge of type `B_R-B_M^-`. Their four endpoints occur in cyclic block order

\[
l,m_+,r,m_-.
\]

The two chords pair adjacent blocks, so their endpoints do not alternate and the chords do not cross. They cannot share an endpoint because all four blocks are disjoint. This contradicts the diameter-thrackle property.

The same argument forbids `B_L-B_M^-` together with `B_M^+-B_R`.

If at least one left and one right switching edge exist, any chosen pair must therefore use the same middle arc. That chosen right edge forbids every left edge from using the other middle arc, and the chosen left edge forbids every right edge from using it. Thus all switching middle endpoints lie on one common middle arc.

**Verdict:** PASS.

---

## 5. The prefix/suffix order is the exact chord-crossing condition

Assume the common middle arc is `B_M^+`, oriented in the boundary order

\[
B_L\to B_M^+\to B_R.
\]

For a left edge `l m_L` and right edge `m_R r` with distinct middle endpoints, the exterior endpoints lie in different blocks and are distinct. Thus the edges are vertex-disjoint and must cross. Their endpoints alternate exactly when

\[
m_R<m_L
\]

on `B_M^+`.

Therefore every distinct right middle endpoint precedes every left middle endpoint. If two distinct middle vertices both belonged to the left and right incident sets, choosing a right edge at the later vertex and a left edge at the earlier vertex would reverse this mandatory order. Hence at most one middle vertex is shared by both sets.

So the participating middle vertices have one right-prefix / optional-hub / left-suffix decomposition.

**Verdict:** PASS.

---

## 6. Finite exhaustive order regression

A direct Pyroam regression enumerated all pairwise-thrackle switching chord families of up to five edges on small four-block cyclic models. It checked three block-size profiles:

```text
(2,2,2,2):  256 thrackle families,  114 mixed-orientation families
(2,3,2,3): 1246 thrackle families,  462 mixed-orientation families
(3,3,3,3): 6064 thrackle families, 2844 mixed-orientation families
```

For every mixed left/right family the program verified:

- exactly one middle arc is used;
- the left/right middle endpoint sets intersect in at most one vertex;
- on `M+`, every right endpoint precedes every distinct left endpoint;
- on `M-`, the reversed order holds.

The regression is not part of the proof, but it confirms the local cyclic-order case split and shared-hub degeneracy.

**Verdict:** PASS.

---

## 7. Caterpillar promotion is legitimate only after the one-arc collapse

Before the collapse, the middle switching vertices may occupy two disjoint boundary arcs, so the standard two-complementary-interval ordered-thrackle theorem cannot simply be cited.

After both switch orientations are present, all participating middle vertices occupy one arc `B_M^star`. There are no switching vertices on the unused middle arc. Restricted to the switching graph's participating vertices, `B_M^star` is one cyclic interval and `B_R union B_L` is the complementary cyclic interval across the wrap. The standard ordered-thrackle theorem then gives caterpillar components and the usual independent-edge order property.

The candidate applies the caterpillar statement only in this post-collapse case.

**Verdict:** PASS.

---

## 8. What the theorem does not prove

The result does **not** bound the number of switching edges below the existing `O(1)` triple-small bound. In particular, an arbitrarily large finite star centered at the unique possible transition hub remains compatible with the order theorem.

It also does not determine the signs of first diameter derivatives under the opposite two-cut shear. KKT stationarity still forces a cusp obstruction somewhere, and small multiplier mass does not make an active diameter constraint dispensable.

Thus the correct next problem is now narrower:

> classify the first-derivative signs of the one-arc prefix/hub/suffix switching forest, or exclude the transition-hub/star regression using the two Section-157 cut resultants and two-sided bracing.

No diameter-decreasing deformation is claimed here.

**Final verdict:** **PASS.** The finite adjacent switching cusp is an ordered one-arc interface forest at the stated scope. C-II and Level I remain open.
