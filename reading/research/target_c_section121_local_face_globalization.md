> Generated reading edition · [exact source](../../research/target_c_section121_local_face_globalization.md) · source SHA-256 `e67b97b3c3399819ea6324b062751811254252de4a06ec11dbba897c502f7f2b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c2b5751b11eb230a831de3438825120dafeac7d0", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section121_local_face_globalization.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7bf8f1fd7987df97a0ee62e5b1cbd3ca086a1756b0a87c3aa9ed35440403a8d7"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — Section 121: harmonic defect faces are actual global inactive chambers

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate.  
**Dependencies:** canonical Sections 62, 67, 77, 82, 83, and 84 under theorem-state audit.44.

The Section-116 zero-host theorem is local to one harmonic induced graph. Section 84,
by contrast, classifies the actual inactive chambers of the full positive-contact
core. Before these two tools can be composed, one must rule out a scope mismatch: a
bounded nonquadrilateral face of the harmonic induced graph could a priori be split by
positive-core vertices or contacts omitted from that induced graph.

That mismatch does not occur.

For every unloaded positive-contact component `I_r`, every bounded face of its induced
harmonic graph `H_r` is also a bounded face of the full positive-contact core. Hence
every bounded nonquadrilateral face used by Section 116 is one of the actual internal
inactive chambers of Section 77. In Type II, Section 84 therefore applies directly to
macroscopic local defect faces of the Section-116 carrier.

This is a source-retaining statement. Contact-isolated source points may lie inside the
face; they remain present and are exactly the inactive population assigned to that
chamber.

---

## 121.1 Setup

Let `G` be the full nonisolated positive-contact core of the canonical post-ZF
representative. Its loaded vertex set is

```math
B=\operatorname{Vert}(F),
```

where `F` is the force hull. Let `I_1,...,I_{c_I}` be the connected components of the
unloaded positive-contact graph.

Fix `I_r`. Let

```math
A_r\subset B,
\qquad
P_r:=\operatorname{conv}(A_r),
```

be its distinct loaded attachment set and harmonic attachment cell. Let `H_r` be the
induced positive-contact graph on

```math
I_r\cup A_r,
```

including every loaded-loaded positive contact whose two endpoints lie in `A_r`.
Canonical Section 62 gives harmonic trapping

```math
I_r\subset P_r.
```

Canonical Section 82 strengthens this to

```math
\boxed{I_r\subset\operatorname{int}P_r,}
\tag{121.1}
```

and proves that every bounded face of `H_r` is a simple convex polygon.

Canonical Section 83 gives pairwise interior-disjointness of harmonic cells:

```math
\boxed{
\operatorname{int}P_r\cap\operatorname{int}P_s=\varnothing
\quad(r\ne s).
}
\tag{121.2}
```

---

## 121.2 No omitted positive-core vertex lies in the cell interior

### Lemma 121.1 — cell-interior vertex fidelity

```math
\boxed{
V(G)\cap\operatorname{int}P_r=I_r.
}
\tag{121.3}
```

### Proof

The inclusion `I_r subset int(P_r)` is (121.1).

First consider an unloaded vertex `x in I_s` with `s ne r`. Applying (121.1) to its
own harmonic component gives

```math
x\in\operatorname{int}P_s.
```

If also `x in int(P_r)`, then the two cell interiors meet, contradicting (121.2).
Thus no unloaded vertex outside `I_r` lies in `int(P_r)`.

Now let `b in B\setminus A_r`. Since `B=Vert(F)`, the point `b` is an extreme point of
`F=conv(B)`. Hence

```math
b\notin\operatorname{conv}(B\setminus\{b\}).
```

But `A_r subset B\setminus\{b\}`, so

```math
P_r=\operatorname{conv}(A_r)
\subset
\operatorname{conv}(B\setminus\{b\}).
```

Therefore `b notin P_r`. The loaded vertices in `A_r` are vertices of `P_r` and hence
lie on its boundary, not in its interior.

These two cases exhaust `V(G)`. This proves (121.3). `square`

---

## 121.3 A bounded harmonic face cannot be cut by an omitted positive contact

### Theorem 121.2 — local-to-global face fidelity

Let `f` be any bounded face of `H_r`. Then `f` is also a bounded face of the full
positive-contact core `G`.

### Proof

By Section 82, the boundary of `f` is a simple convex contact polygon contained in
`P_r`, and its open interior satisfies

```math
\operatorname{int}f\subset\operatorname{int}P_r.
\tag{121.4}
```

Because `f` is a face of `H_r`, no vertex of `I_r union A_r` lies in `int(f)`. Lemma
121.1 says there is no other positive-core vertex in `int(P_r)`. Hence

```math
\boxed{V(G)\cap\operatorname{int}f=\varnothing.}
\tag{121.5}
```

Suppose nevertheless that an edge `xy` of `G` not belonging to `H_r` has relative
interior meeting `int(f)`. Since neither endpoint lies in `int(f)`, the straight
segment `xy` must enter and leave the Jordan domain `int(f)`. Every entry or exit is an
intersection with the simple polygon `partial f`.

The positive-contact graph is straight-line planar. Therefore an intersection between
`xy` and an edge of `partial f` can occur only at a common endpoint. It follows that
any connected portion of `xy` lying in `cl(f)` must have its endpoints among the
vertices of `partial f`.

If the whole edge segment inside the face joins two boundary vertices, both endpoints
belong to `I_r union A_r`. But `H_r` is the **induced** positive-contact graph on this
vertex set, so the contact `xy` would already be an edge of `H_r`. Such an edge cannot
run through the interior of one of its faces. This is a contradiction.

If instead `xy` had only one endpoint on `partial f` and the other endpoint outside
`cl(f)`, then after entering `int(f)` from the boundary endpoint it would have to leave
through a second boundary point which is not its endpoint, producing a forbidden
proper intersection with `partial f`. This is also impossible.

Thus no edge of `G\setminus H_r` meets `int(f)`. Together with (121.5), the region
`int(f)` contains neither a vertex nor an edge of `G`. Therefore `f` is a face of `G`.
It is bounded because it is bounded in `H_r`. `square`

The argument uses occurrence-free planar geometry only; no KKT weight is transferred
and no source point is deleted.

---

## 121.4 Nonquadrilateral local faces are exactly actual inactive chambers

Canonical Section 67 classifies bounded faces of the full positive-contact core.
Every bounded four-face is a strict unit rhombus. Every other bounded face is a convex
nonquadrilateral contact polygon, and any full-source points in its interior are
contact-isolated.

Combining that classification with Theorem 121.2 gives:

### Corollary 121.3 — defect-face globalization

Every bounded nonquadrilateral face of `H_r` is an actual internal inactive chamber of
the full source in the sense of Section 77.

In particular, if its degree is `k_f`, then its chamber perimeter is exactly

```math
\boxed{\operatorname{per}(f)=k_f,}
\tag{121.6}
```

because every boundary edge is a unit contact. All source points in its interior are
retained contact isolates.

This is the exact scope bridge needed to compose Sections 116 and 84.

---

## 121.5 Type-II macroscopic local defect faces are doubled near-geodesic corridors

Now work along a Type-II full-core sequence. Let `r=r(D)` be any chosen harmonic
component sequence and let `f_D` be a bounded nonquadrilateral face of `H_{r(D)}`.
Write

```math
k_D:=\deg(f_D).
```

Assume along a subsequence

```math
{k_D\over D}\longrightarrow\lambda>0.
\tag{121.7}
```

Corollary 121.3 makes `f_D` an actual internal inactive chamber. Canonical Section 84
therefore applies. Choose a farthest pair of boundary vertices `x_D,y_D` and let the
two boundary arcs between them have unit-edge lengths `ell_D^+` and `ell_D^-`.
Section 84 gives

```math
\boxed{
{|x_D-y_D|\over D}\longrightarrow{\lambda\over2},
}
\tag{121.8}
```

and

```math
\boxed{
{\ell_D^+\over D},
{\ell_D^-\over D}
\longrightarrow{\lambda\over2}.
}
\tag{121.9}
```

Since `ell_D^+ + ell_D^- = k_D`, the total excess of these two open face-boundary
routes over their common chord is

```math
\boxed{
k_D-2|x_D-y_D|=o(D).}
\tag{121.10}
```

Thus a macroscopic local defect-face cycle need not be paid as a zero-displacement
route of excess `k_D=Theta(D)`. It can be cut at a diameter pair into two oppositely
directed near-geodesic routes whose **combined** excess is `o(D)`.

The physical train-end assignment remains valid after the cut: orient the original
face cycle with the defect face on its right, exactly as in Section 116. Cutting the
cycle changes no edge occurrence or orientation. Every physical rhombus-boundary end
formerly assigned to the closed face cycle is assigned to the same occurrence on one
of the two open arcs. Hence endpoint assignment remains injective.

The price is geometric rather than combinatorial: the zero host `0` is replaced by an
antipodal pair of unit chord hosts

```math
q_f,
\qquad -q_f.
\tag{121.11}
```

This host-diversity cost must be retained; it cannot be silently ignored in a
signed-return inequality.

---

## 121.6 Fixed-scale corridor splitting inside one Section-116 carrier

Fix `eta>0` and one harmonic carrier `H_r`. Call a bounded nonquadrilateral face
`eta`-macroscopic when

```math
\deg f\ge\eta D.
```

The local Section-82 boundary budget gives

```math
P_{{\rm exc},r}=O(D),
```

so the number of `eta`-macroscopic defect faces is bounded by a constant depending
only on `eta` and the carrier boundary constant.

Along any Type-II subsequence, pass to a further subsequence and label these finitely
many faces by decreasing degree, padding the list when necessary. For every persistent
face whose normalized degree has a positive limit, apply (121.10). The sum of the
resulting two-arc excesses is then

```math
\boxed{o(D)}
\tag{121.12}
```

for fixed `eta`.

Consequently the Section-116 route system on one carrier can be replaced, at fixed
macroscopic scale, by the following occurrence-injective route family:

1. the two outer-walk arcs cut at a diameter pair of the attachment cell;
2. two near-geodesic boundary arcs for each macroscopic defect face; and
3. the unsplit zero-displacement cycles for all remaining defect faces.

Every physical end of every complete rhombus train is still assigned to exactly one
matching boundary occurrence. The total route excess is

```math
\boxed{
E_{\eta}
=
L_r-2d_r
+
\sum_{f\in\mathcal F_{\ge\eta D}}
\bigl(\deg f-2\operatorname{diam}f\bigr)
+
\sum_{f\in\mathcal F_{<\eta D}}\deg f.
}
\tag{121.13}
```

For fixed `eta`, the middle sum is `o(D)` along the selected Type-II subsequence.

This is a genuine strengthening of the physical-route description. Linear defect-face
perimeter cannot automatically be treated as linear route **excess** when it is
concentrated in macroscopic faces.

---

## 121.7 Exact remaining obstruction after globalization

Section 121 does **not** close C-II. It exposes the next obstruction more sharply.

After macroscopic defect corridors are split, the signed-return host set contains

- the antipodal outer diameter hosts `q,-q`;
- one antipodal pair `q_f,-q_f` for each macroscopic local defect corridor; and
- the common zero host for the residual submacroscopic defect cycles.

The Section-116 constant `4-2sqrt(3)` is special to the three-host set
`{q,-q,0}`. Adding the corridor hosts can reduce the directional return loss and can
make it vanish on selected train directions. Therefore one may **not** combine
(121.12) with the Section-116 area lower bound while keeping its old return constant.

The resulting all-regime closing target is now:

> prove that the finite family of antipodal corridor hosts cannot simultaneously
> shadow enough of the two train directions across the quadratic rhombic area to
> annihilate the signed-return cost, unless their physical corridors consume more
> boundary/interface currency than Type II permits.

The diffuse remainder, consisting of defect faces of `o(D)` individual perimeter,
remains a separate route-excess population and must also be charged without repeated
use of physical occurrences.

This reduction is stronger than treating all bounded defect faces as a single zero
host, because it distinguishes true path excess from mere doubled corridor length and
uses the actual global inactive-chamber geometry.

---

## 121.8 Dependency and scope audit

- **Section 62:** defines the induced harmonic graph and harmonic attachment cell.
- **Section 82:** gives `I_r subset int(P_r)` and simple convex bounded local faces.
- **Section 83:** supplies pairwise interior-disjoint harmonic cells.
- **Sections 67 and 77:** classify full-core bounded nonquadrilateral faces as actual
  inactive chambers containing only contact-isolated extra source points.
- **Section 84:** supplies Type-II collapse and doubled near-geodesic structure for a
  linear-perimeter internal inactive chamber.
- **Planarity:** the full positive-contact graph is straight-line planar. The proof of
  Theorem 121.2 uses it only to forbid an omitted edge from entering and leaving the
  local face without a vertex or proper crossing.
- **Inducedness:** if an omitted global contact joined two vertices on the local face
  boundary, it would already be an edge of `H_r`.
- **Contact isolates:** retained throughout. They may lie in the chamber interior but
  have no contact edges and do not split the positive-contact face.
- **ZR/ZF scope:** no affine-kernel assertion is made about isolated coordinates.
- **Theorem authority:** this file is proof-only. It does not alter audit.44 or promote
  Sections 116--121.

**Disposition:** new structural reduction; C-II remains open.
