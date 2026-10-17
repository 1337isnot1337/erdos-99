> Generated reading edition · [exact source](../../research/target_c_boundary_flat_reflection_dichotomy_2026-09-14.md) · source SHA-256 `6103686f099e0caff62073bbf5f8763fbe97ae89f251555a1dc4ed72860ab6aa`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "156bfcec3ae1206232807a38a4fbfcb449f050c5", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_boundary_flat_reflection_dichotomy_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "2124255084277404bce5fbe43d85adab1a49e9e6ec8d88e3e712723341575629"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — boundary flat-center reflection dichotomy

**Date:** 2026-09-14  
**Target:** C-II, canonical contact-minimal full-core Type-II branch  
**Dependencies:** double-unit corner / flat-center overlap (`66d738ba`); loaded lexicographic exchange; empty-pentagon trapezoid stability; shallow-tooth penetration; audited minimax atomic gap `g=0.0021`  
**Claim class:** proof-only source-level reduction; theorem-state authority unchanged  

## LEVEL I STATUS

`STILL OPEN`

The double-unit/flat-center overlap theorem forces, on the small-residual low-`t`
branch, a large weighted population of

1. shallow-tooth inward contacts,
2. loaded flat-pentagon centers, and
3. inward third contacts at double-unit loaded corners.

The middle currency is not a separate final escape.  A loaded flat center can be
reflected through its two almost-antipodal face contacts.  Loaded lexicographic
minimality forces that reflection to hit a separation blocker, so each loaded flat
center produces an inactive source pair of length `1+o(1)`.  A packing argument then
extracts a large endpoint-disjoint matching of such pairs.

Let `E_pen(eta)` and `E_in^(4)` have the meanings from
`target_c_double_unit_flat_center_overlap_2026-09-14.md`, and let `L_flat^bd` be its
loaded flat-center population.  On every convergent Type-II subsequence with

```math
R_F=o(D),
```

there is a subfamily `L_diag subseteq L_flat^bd` with

```math
|L_{diag}|=|L_{flat}^{bd}|-o(D)
\tag{BR.1}
```

and an endpoint-disjoint inactive-pair matching `H_ref` such that

```math
\boxed{|H_{ref}|\ge {|L_{diag}|\over13},}
\tag{BR.2}
```

```math
\boxed{\sum_{xy\in H_{ref}}(|x-y|-1)=o(D).}
\tag{BR.3}
```

For the admissible tooth threshold `eta=0.06`, the endpoint form of `66d738ba` gives

```math
4|E_{pen}(0.06)|+|L_{flat}^{bd}|+|E_{in}^{(4)}|
\ge (0.442242872369096\ldots-o(1))D.
\tag{BR.4}
```

Combining (BR.1)--(BR.4),

```math
\boxed{
4|E_{pen}(0.06)|+13|H_{ref}|+|E_{in}^{(4)}|
\ge (0.442242872369096\ldots-o(1))D.
}
\tag{BR.5}
```

Let

```math
E_{in}^*:=E_{pen}(0.06)\cup E_{in}^{(4)}.
```

Both parent families consist of actual source unit-contact edges with quantitative
inward penetration.  Since each parent family is contained in the union,

```math
4|E_{pen}(0.06)|+|E_{in}^{(4)}|\le5|E_{in}^*|.
```

Therefore

```math
\boxed{
5|E_{in}^*|+13|H_{ref}|
\ge (0.442242872369096\ldots-o(1))D,
}
\tag{BR.6}
```

and hence the current safe endpoint satisfies the two-currency source alternative

```math
\boxed{
\max\{|E_{in}^*|,|H_{ref}|\}
\ge (0.0245690484649497\ldots-o(1))D.
}
\tag{BR.7}
```

Thus a small-residual survivor near the present scalar endpoint must expose either a
linear family of actual strongly inward unit contacts or a linear endpoint-disjoint
matching of inactive source pairs with sublinear total gap to activation.

## 1. Reflection blocker lemma

Let `m` be a loaded distinguished middle vertex of a sufficiently flat pentagonal
exceptional face, with cyclic neighbors `l,r` satisfying

```math
|l-m|=|m-r|=1,
\qquad
\angle lmr=\pi-\epsilon_m.
```

Reflect `m` across the line `lr` and call the reflected point `m^*`.  Since the two
incident bars have equal length,

```math
|m^*-l|=|m^*-r|=1,
\qquad
|m-m^*|=2\sin(\epsilon_m/2).
\tag{BR.8}
```

In the flat-trapezoid limit, the midpoint of `lr` has a positive inward segment inside
the quadrilateral formed by `l,r` and the two opposite pentagon vertices.  Trapezoid
stability therefore implies that for sufficiently small `epsilon_m`,

```math
m^*\in\operatorname{int}(\operatorname{conv}A).
\tag{BR.9}
```

The loaded flat-center theorem gives `deg_C(m)=2`, so every source point
`z notin {m,l,r}` satisfies `|m-z|>1`.

Suppose every such `z` also satisfied `|m^*-z|>1`.  Replace `m` by `m^*`.  The new
source is unit-separated and has exactly the two replacement contacts to `l,r`.
Moreover `|l-r|>1`, because `|l-r|=1` would make the original triple `l,m,r` a
forbidden unit equilateral triangle.  Hence the replacement contact graph remains
triangle-free.

Now apply the committed loaded lexicographic exchange theorem with `Z` empty and
`Y={m^*}`.  The replacement lies in the interior of the old convex hull, creates no
diameter pair, and creates exactly as many unit contacts as were lost at loaded vertex
`m`.  This contradicts secondary diameter-pair minimality.

Consequently there is a blocker

```math
z(m)\notin\{m,l,r\},
\qquad |m^*-z(m)|\le1.
```

Using (BR.8),

```math
\boxed{
1<|m-z(m)|
\le1+2\sin(\epsilon_m/2).
}
\tag{BR.10}
```

This is an inactive near-contact in the original source.

## 2. One blocker serves at most six diagonal flat centers

Consider a family for which all `epsilon_m<=epsilon_D` and `epsilon_D->0`.  Fix a
source point `z` and suppose it blocks seven distinct centers.  Their rays about `z`
have two consecutive angular directions separated by at most `2pi/7`, while their
radii lie in `(1,1+eta_D]`, where

```math
\eta_D:=2\sin(\epsilon_D/2)\to0.
```

For a completely finite bound, once `eta_D<=1/20`, two such adjacent centers at radii
`r,s` and radial unit vectors `u,v` satisfy

```math
|ru-sv|
\le |r-s|+s|u-v|
\le {1\over20}+{21\over20}\,2\sin(\pi/7)
<0.962<1.
\tag{BR.11}
```

This contradicts source unit separation.  Thus every blocker is assigned to at most
six centers.

Form the assignment edge `{m,z(m)}` for each center.  A source vertex is a distinguished
center at most once and a blocker at most six times, so this assignment multigraph has
maximum degree at most seven.  Greedy edge matching deletes at most `2*7-1=13`
assignment edges per chosen edge, proving

```math
|H_{ref}|\ge |L_{diag}|/13.
```

The matching is endpoint-disjoint by construction.

## 3. Diagonalize the boundary flat-center population

The flat-center population in `66d738ba` was obtained with a fixed positive pentagon
residual threshold.  For reflection activation we need the geometric error to tend to
zero, but the small-residual branch supplies this without losing first-order mass.

For each fixed `j`, trapezoid stability gives a positive residual threshold
`theta_j` guaranteeing middle-angle error at most `1/j`.  Because `R_F/D->0`, choose
an integer `j(D)->infinity` slowly enough that

```math
{R_F\over D\,\theta_{j(D)}}\to0.
\tag{BR.12}
```

Delete from `L_flat^bd` every center whose incident pentagon has residual at least
`theta_{j(D)}`.  At most `R_F/theta_{j(D)}=o(D)` centers are deleted, because the
centers are distinct and each retained center is attached to its one classified
pentagon.  The surviving family is `L_diag`, establishing (BR.1), with a common
`epsilon_D=1/j(D)->0`.

By (BR.10), every edge of the matching then has gap at most
`2 sin(epsilon_D/2)`.  Also `|L_diag|=O(D)`; for instance it is a subset of the loaded
force-hull vertices, whose unit separation and convex-hull perimeter bound give
`O(D)` vertices.  Therefore

```math
\sum_{xy\in H_{ref}}(|x-y|-1)
\le |H_{ref}|\,2\sin(\epsilon_D/2)
=o(D),
```

proving (BR.3).

## 4. Composition with the boundary overlap theorem

The contact-converted form of `66d738ba`, at `eta=0.06`, is

```math
4|E_{pen}(0.06)|+|L_{flat}^{bd}|+|E_{in}^{(4)}|
\ge (0.442242872369096\ldots-o(1))D.
```

Replace `|L_flat^bd|` by `|L_diag|+o(D)` and then use
`|L_diag|<=13|H_ref|`.  This gives (BR.5).  Passing to the union `E_in^*` gives
(BR.6).  Finally the two coefficients on the left sum to eighteen, so (BR.7) follows.

The numerical division is

```math
{0.442242872369096\ldots\over18}
=0.0245690484649497\ldots .
```

## 5. Frontier effect

This removes the loaded-flat-center term from the boundary endpoint as a qualitatively
independent obstruction.  Near the current audited `g=0.0021` endpoint, the remaining
boundary geometry is forced into two concrete source-level currencies:

```text
(A) Omega(D) actual strongly inward unit contacts,

or

(B) Omega(D) endpoint-disjoint inactive near-pairs
    with total gap o(D).
```

The next closing step is therefore variational.  Route (B) asks for a simultaneous
first-contact / lexicographic exchange theorem for a disjoint matching with sublinear
total activation gap.  Route (A) asks for a global capacity or stress theorem showing
that the near-extremal diameter system cannot support that many strongly inward
contact bars together with the already-forced train/pentagon structure.

## 6. Scope audit

- The reflection is a hypothetical replacement used through the already-audited
  loaded lexicographic exchange theorem; `m` and `m^*` are never kept simultaneously.
- The replacement creates exactly two contacts because the no-blocker hypothesis uses
  strict distance `>1` from every source other than `l,r`.
- `|l-r|>1` is forced by the triangle-free hypothesis, so the replacement itself does
  not create a unit triangle.
- The blocker multiplicity bound is finite once the common gap is below the explicit
  `1/20` annulus threshold.
- The diagonalization in Section 3 is essential: a fixed flatness threshold alone
  would not imply the total matching gap is `o(D)`.
- The two inward-contact parent families may overlap; using their union in (BR.6)
  loses nothing invalid because `4|E_pen|+|E_in^(4)|<=5|E_in^*|`.
- All asymptotic constants inherit the proof-only `g=0.0021` lifecycle used by
  `66d738ba`.
- No exact unit triangle or strict same-cardinality sub-`D` competitor is produced.

**Disposition:** new proof-only structural reduction.  C-II and Level I remain open.
