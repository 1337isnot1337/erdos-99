> Generated reading edition · [exact source](../../../docs/reports/target_a_right_deficiency_geometric_tube_2026-09-05.md) · source SHA-256 `139262981fff8d24a9b0a54b54ebc6e1ce96e5b5381b51e9c79ac769fd65dd33`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "696ca60a1fee6daef291bcde473f4068ab789d0f", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_a_right_deficiency_geometric_tube_2026-09-05.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "5dd4cac3001b2dcfa6827ed172f1321a889a58043faeaee83ae79355503738cc"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — Target A right-deficiency geometric-tube bound

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** exact Schur/gammoid consequence plus translation average  
**Target:** Section 114 response-corrected collar endpoint  
**Status:** LEVEL I STILL OPEN

## 1. Purpose

Section 114 writes Target A in the shortest right-deficiency form

`Phi(v)=|Y_0(v)|+h(G_v)`,

with

`J(v):=rho^dagger-|Y_0(v)|`.

Thus the desired inequality is exactly

`h(G_v)>=J(v)`

for at least one admissible generic lattice translate.  A survivor satisfies the
pointwise integer inequality

`h(G_v)<=J(v)-1`.

The geometric-tube separator from the companion Steiner report was initially written
as a Schur-nullity estimate and charged every right-shore tube vertex.  For the right
deficiency `h=|O|-rank S`, every exterior tube sink cancels.  Only **interior** tube
sites remain as a penalty.  This is substantially sharper and is compatible with full
translation averaging in Section 114.

## 2. Geometric separator

Let `K` be the plateau response hull.  Let `Gamma subset K` be a finite embedded tree
whose leaves lie on `partial K`, whose open edges lie in `int K`, and which avoids the
finite response point set `X^*`.  Write

`D_1,...,D_k`

for the components of `K\Gamma`.

For a generic triangular-lattice translate define

`T_Gamma={y in Z sqcup O : dist(y,Gamma)<1}`,

`T_Z=T_Gamma cap Z`,

`T_O=T_Gamma cap O`.

As in the Steiner-tube proof, every response radial edge whose right endpoint is
outside `T_Gamma` avoids `Gamma`: if `xy` met `Gamma` at `z`, then

`dist(y,Gamma)<=|y-z|<=|y-x|<1`.

Hence every surviving internal response path stays in one `D_i`.

For each sector put

`C_i=C^partial cap D_i`.

For `o in O\T_O`, put `o in O_i` if it has a surviving response neighbor in `D_i`.
The `O_i` are pairwise disjoint.  Indeed, if one surviving sink had neighbors
`x_i,x_j` in distinct sectors, the chord `x_ix_j` meets `Gamma`; the open unit disk
centered at `o` is convex and contains both endpoints, so it contains that intersection
point, contradicting `o notin T_Gamma`.

Let

`O_0=(O\T_O)\setminus union_i O_i`.

These are surviving exterior lattice sites with no surviving response neighbor.

## 3. Right-deficiency separator theorem

Take a maximum vertex-disjoint directed Schur linkage from `C^partial` to `O`.  At
most `|T_Gamma|=|T_Z|+|T_O|` paths meet a tube right vertex.  Every remaining path is
sector-local and ends in a distinct member of the corresponding `O_i`.  Therefore

`rank S <= |T_Z|+|T_O|+sum_i min(|C_i|,|O_i|)`.

On the other hand

`|O|=|T_O|+|O_0|+sum_i|O_i|`.

Subtracting gives the exact cancellation:

### Theorem RD1 — only interior tube sites cost right deficiency

`h(G)=|O|-rank S`

`>= |O_0| + sum_i (|O_i|-|C_i|)_+ - |T_Z|`.

Define the geometric right-surplus quantity

`Xi_Gamma(v):=|O_0|+sum_i(|O_i|-|C_i|)_+`.

Then simply

`h(G_v)>=Xi_Gamma(v)-|T_Z(v)|`.

The tube sites in the exterior collar `O` have disappeared completely from the loss.
This is the right-deficiency analogue of terminal cancellation in the left-nullity
bound.

## 4. Exact Target A closing criterion

Since Target A is `h>=J`, it closes for a phase `v` whenever

`Xi_Gamma(v) >= J(v)+|T_Z(v)|`.

Conversely every surviving counterexample must satisfy, for every admissible generic
translate,

### Corollary RD2 — pointwise survivor inequality

`Xi_Gamma(v) <= J(v)+|T_Z(v)|-1`.

No source/contact assumption on `Gamma` is used.  Stress geometry may be used later to
choose a particularly informative tree, but Schur sectorization itself is purely
metric.

## 5. Translation average of the interior tube penalty

Section 114 already averages over one full triangular-lattice fundamental cell, with
area

`a_0=sqrt(3)/2`.

For any fixed measurable region `E`, translation averaging gives

`average_v |(Lambda+v) cap E| = area(E)/a_0`.

Apply this to

`E=K cap N_1(Gamma)`,

where `N_1` is the open Euclidean unit neighborhood.  Generic exceptional phases have
measure zero.  Hence

`average |T_Z| = area(K cap N_1(Gamma))/a_0`

`              <= area(N_1(Gamma))/a_0`.

If `Gamma` is a finite Euclidean tree of total edge length `L`, then

`area(N_1(Gamma)) <= pi+2L`.

To see this, start with one edge, whose unit neighborhood is a stadium of area
`pi+2ell`.  Attach the remaining tree edges one at a time at an existing vertex.  The
unit disk about the attachment vertex is already present, so an attached segment of
length `ell` increases the union area by at most `2ell`.  Summation gives the claim.

Thus:

### Theorem RD3 — averaged tube cost

`average |T_Z| <= (pi+2L(Gamma))/a_0`.

For a straight geometric crosscut of length at most `d=diam K`,

`average |T_Z| <= (pi+2d)/a_0`

`= (4/sqrt(3))d + 2pi/sqrt(3)`.

The leading coefficient is

`4/sqrt(3)=2.3094010767...`.

For the three-leaf Steiner tree of the companion report, `L<=sqrt(3)d`, giving

`average |T_Z| <= 4d+2pi/sqrt(3)`.

## 6. Joint averaged survivor inequality

Average Corollary RD2 over the full lattice torus.  Section 114 gives

`average J = J_av`.

Therefore every survivor necessarily satisfies

### Corollary RD4 — joint collar/separator average

`average Xi_Gamma`

`<= J_av + area(K cap N_1(Gamma))/a_0 - 1`.

In particular a straight crosscut of length at most `d` gives

`average Xi_Gamma`

`<= J_av + (4/sqrt(3))d + 2pi/sqrt(3) - 1`.

This is the correct use of translation averaging.  It does not choose a phase by
minimizing the shield independently of the collar reward; both terms are averaged in
the same Section-114 phase variable.

## 7. Frontier

The remaining problem can now be phrased without Schur-rank algebra:

> Find a geometrically meaningful crosscut/tree `Gamma` for which the average right
> sector surplus `Xi_Gamma` exceeds the explicit right-hand side of RD4, or derive a
> strict-diameter competitor.

A stress-generated pair of boundary reaction points is a natural way to choose a
straight crosscut of length at most `d`, while the three-reaction fan may motivate a
three-leaf tree.  The important quantitative improvement is that the right-deficiency
penalty is boundary order with leading coefficient `2.3094` for one chord, not the
pointwise full-tube constants from Sections 173–174.