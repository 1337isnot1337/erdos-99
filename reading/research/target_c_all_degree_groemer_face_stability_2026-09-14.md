> Generated reading edition · [exact source](../../research/target_c_all_degree_groemer_face_stability_2026-09-14.md) · source SHA-256 `bc030d4e399be76716ce4877c526bf6df4a8e6549be2104c6bd6d3282f5e95ee`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ba6f4984aa79b38a46f1fcd9b7874e550ca0a966", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_all_degree_groemer_face_stability_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "4ce2c69031526da7cd63d831ac4f1f586c5869af1bb256e0bbdd7fb17eb1f5bc"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — all-degree Groemer face stability and the Type-II near-contact fork

**Date:** 2026-09-14  
**Repository base:** active `research/c2-closure-sol-20260914-r5` branch after exact Oler-gluing audit  
**State version:** `2026-09-14.audit.51`  
**Run type:** finite packing stability / full-core structural reduction  
**Target:** Target C-II, canonical full-core Type-II branch  
**Claim class:** proof-only consequence awaiting independent audit  
**External theorem:** Thue–Groemer/Oler equality classification as restated in K. J. Böröczky and I. Z. Ruzsa, *Note on an Inequality of Wegner*, Discrete Comput. Geom. 37 (2007), 245–249, DOI `10.1007/s00454-006-1277-4`  
**Computation:** dependency-free constant regression only

## LEVEL I STATUS

`STILL OPEN`

The AG42/§171 bootstrap now forces linearly many actual bounded nonquadrilateral contact faces. Generic Oler accounting alone does not turn those faces into geometric width because near-degenerate faces can approach equality. The missing information is what Oler equality looks like.

Groemer's equality classification supplies it at every finite cardinality, not only for the pentagon/hexagon cases treated in the older low-degree report. The resulting compactness theorem says:

> at any fixed face-degree cutoff and any fixed hidden-contact margin `eta>0`, every exceptional face pays a uniform positive amount of the exact canonical fixed-boundary Oler residual.

Combining this with the new linear exceptional-face count gives a Type-II fork:

```text
linear true force-hull residual R_F
        OR
linearly many pairwise vertex-disjoint actual source pairs at distance 1+o(1).
```

No exact contact, unit triangle, or strict sub-`D` competitor is claimed.

## 1. Use the existing exact residual, not raw chamber slack

The proof-only residual-conservation note
`research/target_c_inactive_chamber_residual_conservation.md` defines, for every inactive chamber `C_j`,

```math
r_j={A_j\over a_0}+{P_j\over2}+1-z_j-k_j\ge0,
\qquad a_0={\sqrt3\over2},
\tag{GS.1}
```

where `k_j` is the number of fixed augmented boundary source vertices. It proves the exact conservation law

```math
\boxed{
\sum_j r_j
=R_F
:={A_F\over a_0}+{P_F\over2}+1-N_F-{E_4\over a_0}
\ge0.
}
\tag{GS.2}
```

For a bounded nonquadrilateral contact face `P` of degree `d` containing `z` assigned contact-isolated source points, every boundary side is a unit contact and `P_P=d`, `k_P=d`. Hence

```math
\boxed{
r(P)
={A(P)\over a_0}-{d\over2}+1-z.
}
\tag{GS.3}
```

Equivalently,

```math
\boxed{
a_0r(P)
=A(P)-a_0(z+1)-c_0(d-4),
\qquad c_0={a_0\over2}.
}
\tag{GS.4}
```

Thus `r(P)` is exactly the local slack in canonical §67.19.

The hostile-audited Oler-gluing identity gives

```math
\Sigma_F+\Sigma_{ext}=\Sigma_K+L_{cap},
```

where `Sigma_F=R_F+E_4/a_0` and `Omega_K=Sigma_K-E_4/a_0`. Therefore the residual-level global relation is

```math
\boxed{
R_F+\Sigma_{ext}=\Omega_K+L_{cap}.
}
\tag{GS.5}
```

Every term in (GS.5) is nonnegative. This is the correct gluing invariant; the much larger raw chamber slack contains mandatory boundary/train credit and is not the quantity used below.

## 2. External equality theorem at the exact normalization

Böröczky–Ruzsa restate the Thue–Groemer inequality: if a convex compact set `C` contains the centers of `N` pairwise nonoverlapping unit disks, then

```math
{A(C)\over2\sqrt3}+{P(C)\over4}+1\ge N.
\tag{GS.6}
```

They also restate Groemer's equality classification. Equality holds only when either

1. `C` is a segment of length `2(N-1)`; or
2. `C` is the convex hull of the `N` centers and can be triangulated, using those centers as vertices, into regular triangles of edge length two. In this case the hull has at most six sides.

Their perimeter convention for a segment is twice its length.

Scale coordinates by `1/2`. For a unit-separated finite point set `X` in its convex hull `K`, (GS.6) becomes exactly

```math
\boxed{
|X|\le {A(K)\over a_0}+{P(K)\over2}+1.
}
\tag{GS.7}
```

Equality in (GS.7) occurs only when

1. `K` is a segment of length `|X|-1`; or
2. `X` triangulates `K` into unit equilateral triangles.

This is the equality theorem needed for the local §67 residual. No different packing inequality is being substituted for Oler.

## 3. Uniform fixed-degree face stability

For one exceptional face `P`, let `X(P)` be the union of

- its `d` cyclic boundary vertices; and
- its `z` assigned interior contact-isolated source points.

Call a pair in `X(P)` **hidden** if it is not one of the `d` cyclic boundary-edge pairs.

### Theorem GS.1 — fixed-degree hidden-contact stability

Fix an integer `K>=5` and `eta>0`. There exists

```math
\sigma_K(\eta)>0
```

such that every canonical bounded nonquadrilateral contact face `P` with

```math
5\le d=\deg(P)\le K
```

and

```math
|x-y|\ge1+\eta
\qquad\text{for every hidden pair }\{x,y\}\subset X(P)
\tag{GS.8}
```

satisfies

```math
\boxed{r(P)\ge\sigma_K(\eta).}
\tag{GS.9}
```

#### Proof

Suppose not. Then there is a sequence `P_j` with degrees at most `K`, hidden-pair margin at least `eta`, and `r(P_j)->0`.

There are finitely many possible degrees. Pass to a subsequence with fixed degree `d`. Canonical §67.3 says `P_j` is a convex unit-edge `d`-gon, so its perimeter is exactly `d`; isoperimetry gives

```math
A(P_j)\le {d^2\over4\pi}.
```

Oler on the `d+z_j` source points in `P_j` gives

```math
z_j\le {A(P_j)\over a_0}-{d\over2}+1,
```

so `z_j` is bounded in terms of `d`. Pass again so `z_j=z` is fixed.

Normalize the first boundary edge to join `(0,0)` to `(1,0)`. All boundary and interior points lie in a fixed compact disk depending only on `K`. Global unit separation is closed under limits. After a subsequence, all `d+z` points and the convex polygons converge. Area and convex perimeter are continuous, including degenerate limits. Since `r(P_j)->0`, the limiting convex hull `P_infty` has perimeter `d` and

```math
A(P_\infty)=a_0\left(z+{d\over2}-1\right).
\tag{GS.10}
```

Thus the `N=d+z` limiting points attain equality in (GS.7).

The segment equality case is impossible: its Groemer perimeter after scaling would be

```math
2(N-1)=2(d+z-1)>d
```

for `d>=5`, contradicting perimeter continuity.

Hence the limiting point set admits a triangulation by unit equilateral triangles. If `h` points lie on the convex hull, a triangulation using all `N` points has

```math
E=3N-h-3\ge2N-3>d
```

edges because `N>=d>=5`. Only `d` pairs are designated cyclic boundary edges, so at least one unit triangulation edge is hidden. This contradicts the closed limiting form of (GS.8), which keeps every hidden pair at distance at least `1+eta`. Therefore (GS.9) holds. `square`

### Actual faces have strict hidden distances

No hidden pair in an actual canonical exceptional face can already have distance one. Any assigned interior point is contact-isolated. If two nonconsecutive boundary vertices were at unit distance, their straight contact chord would lie in the convex face and split it, contradicting that the displayed cycle is a face boundary. Therefore every hidden pair is strictly longer than one.

## 4. Linearly many bounded-degree exceptional faces

The proof-only AG42 bootstrap gives

```math
\liminf {f\over D}
\ge
f_*:=\sqrt{\Delta_2}-{\pi\over4}+0.00021
=0.167124643466509\ldots .
\tag{GS.11}
```

There is also a finite upper bound on total excess degree. The canonical identity

```math
b+Q=2(q-k)
```

combined with `k>=0`, `q<=P_F`, and `b>=P_F` gives

```math
\boxed{Q\le P_F.}
\tag{GS.12}
```

Let `f_{<=K}` count exceptional bounded faces of degree at most `K`. Every face of degree at least `K+1` contributes at least `K-3` to `Q`, so

```math
f_{\le K}\ge f-{Q\over K-3}.
\tag{GS.13}
```

In Type II, `P_F/D->pi`. Hence

```math
\boxed{
\liminf {f_{\le K}\over D}
\ge
\ell_K:=f_*-{\pi\over K-3}.
}
\tag{GS.14}
```

Take `K=42`. Then

```math
\boxed{
\ell_{42}=0.086570985682155\ldots>0.
}
\tag{GS.15}
```

Thus at least `0.08657D-o(D)` actual exceptional faces have degree at most 42.

## 5. Small residual forces a linear near-contact matching

Fix `eta>0`. Among the degree-at-most-42 faces, call a face `eta`-clean if all of its hidden pairs are at least `1+eta`. By Theorem GS.1, every such face consumes at least `sigma_42(eta)` of residual. The exceptional-face residuals are nonnegative and sum to at most `R_F`, so

```math
N_{clean}(\eta)\le {R_F\over\sigma_{42}(\eta)}.
\tag{GS.16}
```

Suppose along a Type-II subsequence

```math
\boxed{R_F=o(D).}
\tag{GS.17}
```

Then for each fixed `eta>0`, (GS.16) is `o(D)`. Therefore at least

```math
(\ell_{42}-o(1))D
```

degree-at-most-42 exceptional faces contain a hidden actual source pair satisfying

```math
1<|x-y|<1+\eta.
\tag{GS.18}
```

Every vertex of a triangle-free unit-contact graph has contact degree at most five. A degree-at-most-42 bounded face therefore shares a boundary vertex with at most

```math
4\cdot42=168
```

other bounded faces: at each of its boundary vertices there are at most four other incident face sectors. The conflict graph on these faces has maximum degree at most 168, so a greedy independent set contains at least a `1/169` fraction of them. Assigned interior isolates belong to only one face. Hidden pairs chosen from the independent faces are therefore pairwise vertex-disjoint.

For every fixed `eta>0`,

```math
\boxed{
\liminf {\nu_\eta\over D}
\ge {\ell_{42}\over169}
=0.000512254353148\ldots,
}
\tag{GS.19}
```

where `nu_eta` is the maximum number of pairwise vertex-disjoint actual source pairs, contained in distinct bounded exceptional faces, with distance in `(1,1+eta)`.

A diagonal subsequence makes the scale vanish. Set `eta_j=1/j`. Since `R_F/D->0`, for each fixed `j` the clean-face loss is eventually less than `ell_42 D/2`. Choosing these thresholds successively produces `eta_D->0` such that

```math
\boxed{
\nu_{\eta_D}
\ge c_{near}D-o(D),
\qquad
c_{near}:={\ell_{42}\over2\cdot169}
=0.000256127176574\ldots .
}
\tag{GS.20}
```

Thus the small-residual branch contains a linear matching of genuine noncontacts whose gaps tend to zero.

## 6. The Type-II residual/near-contact fork

Every Type-II survivor sequence has a subsequence in one of two forms.

### Branch A — true force-hull residual remains linear

For some `c>0`,

```math
\boxed{R_F\ge cD}
\tag{GS.21}
```

along the subsequence. This is genuine Oler spare after the entire rhombus-area term and all mandatory fixed-boundary credits have been removed. By (GS.5), it must be balanced by the full-source punctured slack, exterior-cap residual, and cap-chord correction.

### Branch B — force-hull residual vanishes at first order

```math
\boxed{R_F=o(D).}
\tag{GS.22}
```

Then (GS.20) gives `Omega(D)` pairwise vertex-disjoint actual source pairs in bounded exceptional faces with

```math
\boxed{1<|x-y|\le1+o(1).}
\tag{GS.23}
```

This is a Type-II analogue of the canonical Type-I near-contact matching theorem, but its mechanism is different: here the matching is forced by linearly many low-degree contact faces approaching Groemer equality, not by a quadratic cloud of contact-isolated points.

## 7. What this changes and what remains

The old warning “thin exceptional faces can pay the interface at arbitrarily small width” is now exact rather than qualitative. A linear population of cheap bounded-degree faces can do so only by producing a linear population of hidden near-unit pairs.

The remaining source-level problem is narrower:

```text
Branch A:
  R_F = Omega(D)
  -> exploit residual-level gluing, not raw chamber slack

Branch B:
  Omega(D) pairwise-disjoint hidden near-contacts inside positive-core defect faces
  -> prove one exact activation or a same-cardinality strict diameter decrease.
```

The compactness theorem gives no explicit modulus `sigma_K(eta)`, so it does not by itself reach the inverse-diameter scale `1+O(1/D)`. Claiming such a rate would be unsupported. The next useful theorem on Branch B should use KKT/global minimality or a quantitative stability version of Groemer.

The macroscopic-container branch is untouched.

## 8. Scope audit

- Every source point is retained.
- The equality classification is used only for finite unit-separated point sets in a convex hull, exactly matching canonical §67.5.
- Assigned interior points are retained in `X(P)` and are contact-isolated by the canonical representative.
- No degree-5/6 restriction is used; the cutoff 42 is only for obtaining a uniform compact family with an explicit linear population.
- The hidden pair need not be a boundary diagonal; it may involve an assigned interior isolate.
- `Q` and `f` are the global canonical exceptional-face currencies, not Section-123 local induced-cell quantities.
- `R_F` is the already-defined exact force-hull residual, not the raw chamber Oler-slack sum.
- AG42 and the §171 bootstrap remain proof-only, so the Type-II asymptotic constants here inherit proof-only status.

**Disposition:** new proof-only finite stability theorem and Type-II structural fork. C-II and Level I remain open.
