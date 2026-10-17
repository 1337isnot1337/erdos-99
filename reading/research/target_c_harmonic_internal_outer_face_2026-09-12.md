> Generated reading edition · [exact source](../../research/target_c_harmonic_internal_outer_face_2026-09-12.md) · source SHA-256 `2a7526794df193143b387d52e498738ccda227b91cbb863a37eb67306649ac16`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e6533b8cc4f1d478e3df8e9cb65a978ce6d73167", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_harmonic_internal_outer_face_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "8321cfd26aa2f6602361f20d5d380786c965c517fb657a17988f44ec12ee29ef"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — attachment contacts lie in the internal harmonic outer face

**Date:** 2026-09-12  
**Base:** current `main` at `6a5067c505b6b1331ce3abf01717daeb102b632e`  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only exact lemma pending independent audit.

## 1. Statement

Fix one unloaded positive-contact component `I_r`. Put

```math
G_r:=C[I_r],
\qquad
A_r\subset B,
\qquad
P_r:=\operatorname{conv}(A_r),
\qquad
K_r:=\operatorname{conv}(I_r).
```

Canonical Section 82 gives the strict harmonic trapping

```math
I_r\subset\operatorname{int}P_r.
\tag{1.1}
```

### Lemma HOF

For every contact edge of the induced harmonic graph on `I_r union A_r` that is not
an internal edge of `G_r`, its relative interior lies in the outer face of `G_r`.
In particular, for every attachment contact `au`, with `a in A_r` and `u in I_r`,

```math
\boxed{
\operatorname{relint}[a,u]
\subset \text{the outer face of }G_r.
}
\tag{HOF.1}
```

The same conclusion holds for every loaded-loaded contact with both endpoints in
`A_r`.

Consequently, the whole added loaded-vertex/contact subgraph is embedded in the
closure of the **original** outer face of `G_r`. It can subdivide that outer-face
region, but it cannot alter any original bounded face. Hence the bounded faces of
`G_r` are exactly the all-unloaded bounded faces of the canonical induced harmonic
graph on `I_r union A_r`. In particular,

```math
\boxed{
\text{bounded four-faces of }G_r
=
\text{unloaded-only strict rhombi assigned to }I_r.
}
\tag{HOF.2}
```

This is the face-preservation fact needed to localize the Section-85 train-boundary
count inside one response-selected harmonic component.

## 2. Attachment vertices are outside the internal convex hull

Because `I_r` is finite, (1.1) implies

```math
K_r=\operatorname{conv}(I_r)
\subset\operatorname{int}P_r.
\tag{2.1}
```

Every member of `A_r` is an extreme vertex of `P_r`, since every attachment is a
loaded force-hull vertex. Therefore

```math
\boxed{A_r\cap K_r=\varnothing.}
\tag{2.2}
```

## 3. Proof of HOF.1 and the loaded-loaded variant

Fix first an attachment contact `e=[a,u]`. By (2.2), `a` lies outside `K_r` and hence
outside the embedded graph `G_r`. The straight-line positive-contact graph is planar,
so `relint(e)` meets no vertex or edge of `G_r`.

Points of `e` sufficiently close to `a` lie outside `K_r`, hence in the unbounded
component of `R^2\setminus G_r`. Suppose a later relative-interior point of `e`
lay in a bounded face `F` of `G_r`. Along the connected open segment from `a` to that
point one would pass from the unbounded complementary component to `F`. The boundary
of `F` is contained in `G_r`, so this transition would force `relint(e)` to meet an
edge or vertex of `G_r`, contradicting planarity.

Thus the whole relative interior of `e` stays in the outer face, proving HOF.1.

If `e=[a,b]` is instead a loaded-loaded contact with `a,b in A_r`, both endpoints lie
outside `K_r` by (2.2). Starting from either endpoint gives the identical argument:
`relint(e)` cannot leave the unbounded complementary component without crossing
`G_r`. Hence its relative interior also lies in the outer face of `G_r`.

## 4. Bounded-face preservation

Every vertex and every relative edge interior added when passing from `G_r` to the
induced harmonic graph lies in the closure of the original outer-face region of
`G_r`. Several added edges may subdivide that original outer-face region into new
bounded faces, so it would be too strong to claim that every later edge stays in the
*current* outer face after earlier insertions. The only fact needed here is that no
added edge enters any bounded face that already belonged to `G_r`.

Therefore each original bounded face of `G_r` survives unchanged in the induced
harmonic graph. Conversely, deleting the loaded vertices and all incident contact
edges can destroy only faces created inside the original outer-face region; it cannot
merge two original bounded faces into a new bounded face of `G_r`.

A bounded face of the induced harmonic graph whose boundary is all-unloaded uses only
vertices and edges of `G_r`, so it is one of these original bounded faces. Hence the
bounded faces of `G_r` are exactly the all-unloaded bounded faces of the induced
harmonic graph.

Canonical Section 82 proves that every bounded face of the induced harmonic graph is
convex and every bounded degree-four face is a strict unit rhombus. Since all vertices
of `G_r` are unloaded, every bounded four-face of `G_r` is an unloaded-only rhombus
assigned to `I_r`.

Conversely, any unloaded-only strict-rhombus face assigned to `I_r` uses only vertices
and internal contact edges of `I_r`; all are retained in `G_r`, and the original
empty face interior remains empty. Hence it is a bounded four-face of `G_r`. This
proves HOF.2.

## 5. Exact internal face currency

Let

- `k_r` be the outer-face edge-incidence count of `G_r`, bridges counted twice;
- `Q_r=sum_F(deg F-4)` over bounded faces of `G_r`;
- `delta_r` be the graph diameter of `G_r`; and
- `r_r=2|I_r|-delta_r-2-|E(G_r)|` be its Eppstein slack.

The exact Eppstein component identity gives

```math
\boxed{k_r+Q_r=2(\delta_r+r_r).}
\tag{5.1}
```

Every edge of the outer-face walk has Euclidean length one, so

```math
\operatorname{per}(K_r)\le k_r.
\tag{5.2}
```

Harmonic trapping gives `K_r subset P_r`. Conversely every attachment vertex has a
unit contact to `I_r`, so

```math
P_r\subset K_r+B(0,1).
\tag{5.3}
```

Cauchy's width formula then yields

```math
\boxed{
\operatorname{per}(P_r)\le k_r+2\pi.
}
\tag{5.4}
```

Equations (5.1) and (5.4) are the exact local analogue of the global loaded-hull
identities used in the new Type-II `q-k` train/hull floor on `main`.

## 6. Scope audit

- No source point is deleted; the lemma concerns a subgraph used for face accounting.
- `G_r` need not be 2-connected; bridges are allowed and are counted twice on its
  outer-face walk.
- No KKT coefficient lower bound is used.
- Loaded-loaded contacts among `A_r` are included explicitly in the outer-face
  preservation argument.
- The proof uses only straight-line planarity, loaded extremality, and canonical strict
  harmonic trapping.
