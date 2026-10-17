> Generated reading edition · [exact source](../../research/target_c_aggregate_inactive_safe_lattice_repacking_hostile_audit.md) · source SHA-256 `e5fc5c90025165c81805193e41e9dd41d814b1b40127fc7e3ae5763185f7f11f`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "dec1f8d64782f42f77c85c93e9579fe0f126bac2", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_aggregate_inactive_safe_lattice_repacking_hostile_audit.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b2d8cb91340e28d58348b4541ec4c68af91850a10fee92f4dbafc54290eea18a"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — aggregate inactive safe-lattice repacking

**Date:** 2026-09-12  
**Audited source:** `research/target_c_aggregate_inactive_safe_lattice_repacking.md`  
**Verdict:** PASS at the stated Section-77 chamber scope.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## 1. Chamber assignment and diameter-cover disjointness

Canonical Section 77 partitions every source point in `F` outside the nonisolated
positive-contact core among the inactive chambers and gives

```math
 Z_{ch}=N_F-m.
```

The chamber population consists of contact-isolated source points. The complete actual
diameter endpoints are the loaded force-hull vertices in the positive core. Therefore
`Z_ch` is disjoint from every vertex cover of the actual diameter graph.

An isolated point assigned to a hull-augmentation pocket may lie on an added hull side.
It is still outside the positive core and is not a force-hull vertex. Removing it is
allowed; the pocket safe region keeps distance one from the whole added side.

**Verdict:** deleting `Z_ch` and a diameter cover removes exactly the sum of their
cardinalities.

## 2. One common lattice and cross-chamber separation

The chamber interiors are pairwise disjoint. The safe regions are subsets of those
interiors. A single translate of the unit triangular lattice is globally
unit-separated, so selected lattice points in different chambers need no additional
cross-chamber argument.

For a new point in chamber `C_j`, every retained old source point lies outside
`int C_j`: all assigned chamber points were removed, while positive-core source points
are on or outside the chamber boundary. The internal contact-wall or hull-outer-pocket
mixed-wall shield therefore supplies new-old unit separation.

Boundary vertices may themselves belong to the deleted diameter cover. Keeping their
original locations as guard obstacles only strengthens the safe-region definition and
does not require them to remain in the competitor.

**Verdict:** the union replacement is genuinely unit-separated.

## 3. Translation averaging and the single floor

Let `S` be the measurable union of all safe regions. For the unit triangular lattice
`Lambda` with covolume `a_0=sqrt(3)/2`, averaging
`|(Lambda+t) cap S|` over a fundamental cell gives `area(S)/a_0`. Hence one translate
has at least

```math
 floor(area(S)/a_0)
```

points. This is one integer floor for the full union, not one floor per chamber.

If there are more points than needed, taking a subset preserves unit separation.
Because `Z_ch` is an integer,

```math
 floor(area(S)/a_0)-Z_{ch}
 =floor(area(S)/a_0-Z_{ch}).
```

Thus a real lower bound `area(S)/a_0-Z_ch >= Xi` implies at least `floor(Xi)` realized
extra slots.

**Verdict:** the integer accounting is exact.

## 4. Safe-area sum

For exceptional faces,

```math
 area(S_j)\ge A_j-m_jc_*-h_*.
```

For Section-67 hull-augmentation outer pockets,

```math
 area(S_j)\ge A_j-s_j-ell_jc_*-h_*.
```

Canonical incidence identities give

```math
 sum_{exc}m_j=4f+Q,
```

```math
 sum_{out}(ell_j+1)=b+2a-q,
 \qquad sum_{out}ell_j=b+a-q,
```

and

```math
 sum_{out}s_j=L_{add}.
```

Therefore the stated total safe-area bound follows with

```math
 L_c=(4f+Q)+(b+a-q)=4f+q-2k+a,
```

using canonical `b+Q=2(q-k)`.

**Verdict:** no boundary occurrence is charged twice beyond the deliberate chamber
perimeter decomposition.

## 5. Residual algebra

For an exceptional face,

```math
 area(S_j)/a_0-z_j
 \ge r_j-kappa_*m_j-C_*.
```

For an outer pocket,

```math
 area(S_j)/a_0-z_j
 \ge r_j-kappa_*ell_j-lambda_*s_j-eta_*.
```

The companion exact conservation theorem gives `sum r_j=R_F`. Summation therefore
yields

```math
 Xi=R_F-kappa_*L_c-lambda_*L_{add}-C_*f-eta_*a.
```

No asymptotic term or hidden per-chamber floor is present.

## 6. Strict diameter descent

The diameter cover removes every old-old pair at distance exactly `D`. Every new point
lies in the interior of a chamber inside `F`; hence it lies in `int F subset int K`.
For any `x in K` and `y in int K`, `|x-y|<D`, because `K` lies in the closed
radius-`D` disk centered at `x` and an interior point of `K` cannot lie on its boundary
circle. Thus every pair involving a new point is strictly subdiametral.

The finite replacement therefore has diameter `<D` whenever the lattice supplies
`Z_ch+tau(H)` points.

The replacement may create unit triangles; this is irrelevant to the definition of
`D(n)`.

**Verdict:** the contradiction is with global diameter minimality at the correct
cardinality.

## 7. Scope boundary

The theorem aggregates only the inactive chambers **inside the force hull** from
Section 77.4: exceptional contact faces and Section-67 hull-augmentation outer
pockets. It does not aggregate the exterior caps in `K\setminus int F` from Sections
77.2/80/162. Those retain the audited-working full-collar Section-165 criterion unless
a separate source-hull boundary shield is proved.

No contact isolate is placed under the Section-57 affine-kernel theorem.

**Final verdict:** PASS. Every survivor must satisfy the finite source-level inequality

```math
 Xi<tau(H)\le ceil(q/2).
```

The remaining mathematical task is to contradict this inequality in the Type-I
internal-chamber regime, or separately close the Section-162 exterior-cap regime.
