> Generated reading edition · [exact source](../../research/target_c_terminal_free_rhombic_corridor_t18687_2026-09-15.md) · source SHA-256 `bee745f2c4ac8edeceb0ab6b642de2b4597afb9742b6c2839cd2313d1063f34c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "997dc94566275acd0488d4ae60491e8a49465ea5", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_terminal_free_rhombic_corridor_t18687_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d36eea5fbdcdd8bd88ced722e98edf6488521f108ae5921770d9171db38d9d75"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the high-`t` joint cusp contains a macroscopic terminal-free rhombic corridor

**Date:** 2026-09-15  
**Status:** proof-only high-`t` local-structure strengthening  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** high-`t` rectangle joint cusp; proper stopped-train centerline geometry; bounded-face convexity/quadrilateral-rhombus theorem; force-hull location of actual diameter endpoints  
**Certificate:** `research/verify_target_c_terminal_free_rhombic_corridor_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The joint-cusp theorem selects adjacent O--O row trains

```math
a_0=\tau_i,
\qquad a_1=\tau_{i+1},
```

inside the high-`t` complete rectangle, together with an oriented common transverse family

```math
B_+,
\qquad |B_+|>0.1567D-o(D),
\tag{RC.1}
```

such that every column crosses both rows. The intervening strip has at most

```math
L_i\le1{,}108{,}999
\tag{RC.2}
```

complete-stopped-train terminal face-side occurrences.

Because the columns are pairwise noncrossing, their portions between the two rows are disjoint proper crosscuts of the strip. They cut it into an ordered ladder. Only `O(1)` ladder cells can contain any train terminal, while the number of cells is linear in `D`.

Consequently one obtains a **consecutive terminal-free run** of internal ladder cells of length

```math
\boxed{
>{1567\over11{,}090{,}000{,}000}D-o(D)
>1.412\times10^{-7}D-o(D).
}
\tag{RC.3}
```

Every cell in this run is disjoint from the global outer boundary. Hence the whole run contains

1. no complete-train terminal occurrence;
2. no bounded nonquadrilateral contact face;
3. no actual diameter endpoint.

Thus every bounded contact face lying wholly in the run is a strict unit rhombus, and every complete train which enters the run must leave it again rather than terminate there.

There is also a quantitative microcell consequence. Among the terminal-free cells one can choose a cell bounded by consecutive columns `b_0,b_1 in B_+` such that all four row/column corner crossings are inverse-diameter close to the triangular angle:

```math
\boxed{
0<\theta(a_r,b_s)-{\pi\over3}
<{1.57\times10^{13}\over D}+o(D^{-1})
\qquad(r,s\in\{0,1\}).
}
\tag{RC.4}
```

The two column phases themselves satisfy

```math
\boxed{
d_{\mathbb{RP}^1}(b_0,b_1)
<{1.57\times10^{13}\over D}+o(D^{-1}),}
\tag{RC.5}
```

while the already-selected row pair has

```math
d_{\mathbb{RP}^1}(a_0,a_1)
<{7.08\times10^6\over D}+o(D^{-1}).
\tag{RC.6}
```

So the finite KKT cusp contains a linearly long internal corridor with zero endpoint/face defect and, inside it, a terminal-free near-triangular `2 x 2` train cell.

---

## 1. Common columns are proper crosscuts of the selected strip

Let `R` be the complement region between the consecutive O--O rows `a_0,a_1`. Since the rows are disjoint proper crosscuts of the closed outer-face disk and are consecutive on the selected O--O path, `R` is a topological quadrilateral: two opposite boundary sides are row-centerline arcs, and the other two are subarcs of the global outer boundary.

Take `b in B_+`. It crosses each row exactly once. The portion of its simple midpoint path between those two crossings lies in `R`. It cannot leave through the global outer boundary between the crossings, because reaching the outer face there would terminate the complete train before its second row crossing. Hence this portion is a proper crosscut of `R` joining the two row sides.

Distinct columns in `B_+` are pairwise noncrossing. Their strip portions are therefore disjoint proper crosscuts. Order them as

```math
b_1,\ldots,b_M
```

by their crossing order along `a_0`. Disjointness forces the same order along `a_1`. The `M` crosscuts partition `R` into `M+1` ladder cells. Exactly the two end cells meet the two global-outer-boundary sides of `R`; every cell between consecutive columns is internal and disjoint from the global outer boundary.

---

## 2. Terminal occurrences cannot hide on a column boundary

A stopped-train centerline runs through strict-rhombus interiors and contact-edge midpoints. A source vertex never lies on such a centerline. Inside `R`, every `b in B_+` is between two crossings and therefore is not at one of its own terminal midpoints.

A terminal midpoint of a different train cannot lie on the `b` centerline. Inside a strict rhombus, the two train centerlines meet at the rhombus interior crossing; a contact-edge midpoint belongs to the unique train using that edge direction. Hence a terminal midpoint on the `b` centerline would be a terminal of `b` itself, impossible between its two row crossings. The same statement applies to the selected row-centerline interiors.

Therefore every terminal occurrence assigned to `R` lies in a unique open ladder cell, except outer-face occurrences on the two global boundary sides, which belong only to the two end zones and never to an internal cell.

Let an internal cell be **bad** when it contains at least one terminal occurrence. Then

```math
\boxed{
\#\{\text{bad internal cells}\}
\le L_i\le1{,}108{,}999.
}
\tag{RC.7}
```

---

## 3. A linearly long consecutive clean run

There are `M-1` internal cells between consecutive columns. At most

```math
L_0:=1{,}108{,}999
```

are bad. Deleting the bad cells leaves at most `L_0+1` consecutive runs of clean cells. Hence the longest run has length at least

```math
{M-1-L_0\over L_0+1}.
\tag{RC.8}
```

Using

```math
M>0.1567D-o(D)
={1567\over10000}D-o(D),
```

we obtain

```math
{M-1-L_0\over L_0+1}
>
{1567\over10000(1{,}109{,}000)}D-o(D),
```

which is (RC.3).

Let `C` be the union of the cells in this longest run. It is bounded by subarcs of the two selected rows and by two columns of `B_+`, with possibly many additional `B_+` columns running through its interior.

---

## 4. Clean means no exceptional contact face

Selected train centerlines pass through strict rhombi and do not enter the interior of a bounded nonquadrilateral face. Therefore every bounded nonquadrilateral contact face contained in `R` lies wholly in one ladder cell.

Every side occurrence of a bounded nonquadrilateral face is a complete-train terminal occurrence under the canonical stopped-train decomposition; in particular such a face contributes at least five terminal occurrences. Thus a clean cell cannot contain a bounded nonquadrilateral face.

Canonical bounded-face geometry says every bounded quadrilateral contact face is a strict unit rhombus, while a bounded triangular face would be a forbidden unit equilateral triangle. Hence

```math
\boxed{
\text{every bounded contact face wholly contained in }C
\text{ is a strict unit rhombus.}
}
\tag{RC.9}
```

No stopped train terminates in `C` by construction.

---

## 5. Internal ladder cells contain no actual diameter endpoint

Every actual diameter endpoint is an extreme source-hull/force-hull vertex and lies on the global outer boundary used by the O--O Jordan-crosscut model. Source vertices do not lie on train centerlines.

Every cell of `C` is internal between two common transverse crosscuts and is disjoint from both global-outer-boundary sides of `R`. Therefore

```math
\boxed{
C\text{ contains no endpoint of an actual diameter edge.}
}
\tag{RC.10}
```

This is stronger than an average endpoint-count bound: it is exact topology. Active diameter chords may geometrically pass across the corridor, but none has a source endpoint in it.

---

## 6. A terminal-free near-triangular microcell

Use the joint-cusp oriented phases. For `b in B_+` define

```math
x_b:=
\left(\theta(a_0,b)-{\pi\over3}\right)
+
\left(\theta(a_1,b)-{\pi\over3}\right)>0.
\tag{RC.11}
```

The selected joint cusp has

```math
\sum_{b\in B_+}x_b
=S_i+S_{i+1}<J,
\qquad J:=1{,}109{,}000.
\tag{RC.12}
```

Suppose the longest clean run has `k` cells, with boundary columns

```math
c_0,c_1,\ldots,c_k.
```

Then

```math
\sum_{j=0}^{k-1}(x_{c_j}+x_{c_{j+1}})
\le2\sum_{b\in B_+}x_b
<2J.
\tag{RC.13}
```

Hence one clean cell between consecutive columns `b_0,b_1` satisfies

```math
x_{b_0}+x_{b_1}<{2J\over k}.
\tag{RC.14}
```

By (RC.3),

```math
{2J\over k}
<
{2(1{,}109{,}000)^2\over0.1567}\,{1\over D}
+o(D^{-1}).
```

The exact certificate verifies

```math
{2(1{,}109{,}000)^2\over0.1567}
<1.57\times10^{13}.
\tag{RC.15}
```

All four angular-excess summands are nonnegative, so (RC.4) follows.

On the common oriented branch,

```math
\theta(a_0,b)-{\pi\over3}
=\beta_b-\alpha_0-{\pi\over3}.
```

Therefore

```math
|\beta_{b_1}-\beta_{b_0}|
\le
\left(\theta(a_0,b_0)-{\pi\over3}\right)
+
\left(\theta(a_0,b_1)-{\pi\over3}\right),
```

which is bounded by the left side of (RC.14). This proves (RC.5).

---

## 7. Frontier effect

At the full live high-`t` endpoint the obstruction now contains

```text
one adjacent O-O row pair with bounded KKT/terminal cusp
+ >0.1567 D consistently oriented common transverse columns
+ a consecutive terminal-free internal column run of >1.412e-7 D cells
+ no bounded nonquadrilateral face anywhere in that run
+ no stopped-train endpoint anywhere in that run
+ no actual diameter endpoint anywhere in that run
+ one clean microcell whose four row/column angles are pi/3+O(1/D).
```

This does **not** by itself give a compactly supported flex. Train-angle motions propagate along complete trains, and active diameter constraints can have endpoints outside the corridor. The theorem instead removes all local endpoint/face defect from a macroscopic portion of the scaffold, leaving only through-going rhombic transport and external locking.

The next closing target is to prove that the one/two-bar external reaction at the row interface cannot lock every source-preserving multishear through such a terminal-free rhombic corridor, or to derive a forbidden diameter-chord order from the same geometry.

**Disposition:** proved a macroscopic terminal-free pure-rhombic corridor and a terminal-free near-triangular microcell inside the high-`t` joint cusp through `t<=1.8687`. C-II and Level I remain open.
