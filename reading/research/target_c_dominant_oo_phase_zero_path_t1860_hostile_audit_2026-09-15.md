> Generated reading edition · [exact source](../../research/target_c_dominant_oo_phase_zero_path_t1860_hostile_audit_2026-09-15.md) · source SHA-256 `f30bafbef7025f1d78cef3fa51e9acd89dc3987a99610b51884a14940692a28e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "2e2b498cd82916e540cb7a1813ed27aa2f20f505", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_dominant_oo_phase_zero_path_t1860_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "2c04f4330eaa22561e857be02775a32ca55dbc6c34db08258926538ad88de46b"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — high-`t` dominant O--O phase-zero path extraction

**Date:** 2026-09-15
**Reviewed:** `research/target_c_dominant_oo_phase_zero_path_t1860_2026-09-15.md`
**Disposition:** **PASS at the stated weighted/asymptotic full-core scope, after the exact-phase scope tightening in `e69269bd`.**
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate claims that the linear same-window dominant O--O family can be reduced,
losing only `o(D)` retained pair weight, to a family whose complement dual is a path.
The dangerous points are: applying Section 157 to both shores, charging deletion to
physical retained endpoint measure, moving train-dependent phase zeros to fixed
markers, and the disk nesting lemma.

All four survive audit.

---

## 1. The pair-weight endpoint measure is legitimate

The wide-window theorem defines for every dominant O--O train

```math
w_\tau=\min(a_\tau,b_\tau),
```

where `a_tau,b_tau` are the two retained outer-terminal weights.  Thus a measure which
puts weight `w_tau` at either terminal is pointwise dominated by the corresponding
retained occurrence measure.  The audited route-capacity construction bounds retained
occurrence weight on each loaded-hull side by that side's Euclidean length.

The Type-II near-disk perimeter theorem therefore gives, on the oriented normal circle,

```math
D^{-1}\mu_D(I)\le |I|/2+o(1)
```

uniformly over moving intervals.  Hence a bounded union of intervals of total width
`o(1)` carries `o(D)` pair-endpoint weight.  No train-count-to-length conversion is
used.

**Verdict:** PASS.

---

## 2. Section 157 is symmetric under swapping shores

For one shore `S`, orient each cut contact from the complementary shore into `S` by
`u`, and orient a crossing diameter vector into `S` by `r`.  Section 157 gives both
signs of

```math
r\cdot Ju.
```

If the two shores are exchanged, the canonical orientations become

```math
u'=-u,
\qquad
r'=-r.
```

Therefore

```math
r'\cdot Ju'=(-r)\cdot J(-u)=r\cdot Ju.
```

The same two-sign theorem is available on the other shore.  Thus both complementary
loaded-hull normal arcs contain a zero of `n dot J u_tau` after the near-disk radial
replacement.  Since the endpoints are later kept away from the zero neighborhoods,
the zeros lie in the interiors of the two complementary arcs and must be the two
antipodal oriented representatives.

**Verdict:** PASS.

---

## 3. The near-disk replacement is uniform enough

The hostile audit of the complement bracing theorem already proves that an actual
diameter vector oriented into a loaded shore satisfies

```math
r_h/D=n_h+o(1)
```

uniformly over actual diameter pairs.  The selected phase window has width
`epsilon_D->0`.  Hence all errors can be absorbed into one sequence `eta_D->0`, then
one may choose a slower `rho_D->0` with

```math
epsilon_D+eta_D=o(rho_D).
```

This is the correct diagonal order.  The candidate does not assume an unproved
`O(1/D)` phase width in the high-`t` window.

**Verdict:** PASS.

---

## 4. Deleting terminal neighborhoods costs only `o(D)` pair weight

A bad train has at least one terminal in the union of the two `rho_D` neighborhoods.
Its pair weight is no larger than the retained occurrence weight at that terminal.
Charging each bad train to one such terminal gives

```math
\sum_{\tau\,bad}w_\tau
\le \text{retained endpoint mass in the two neighborhoods}
=o(D).
```

Double counting a train with both terminals bad would only weaken this upper bound if
one charged both occurrences; the candidate charges at least one and uses an upper
bound by the total occurrence mass.  Therefore the linear staircase constants survive
unchanged at the `cD-o(D)` scale.

**Verdict:** PASS.

---

## 5. Fixed markers remain on opposite sides

For every surviving train, its actual train-dependent zero lies `o(rho_D)` from one
fixed marker and the antipodal zero lies `o(rho_D)` from the other.  No train terminal
lies within distance `rho_D` of either marker.  Moving each zero to its fixed marker
therefore crosses no train endpoint in cyclic order.  Since the train-dependent zeros
are in complementary shore arcs, the fixed markers are also in complementary shore
arcs.

The audited convex-pocket retraction preserves the cyclic order of outer terminal
occurrences.  The argument therefore transfers back from loaded-hull normal order to
the original proper O--O crosscuts.  No metric straightness of the train midpoint
curve is required.

**Verdict:** PASS.

---

## 6. The two-marker disk lemma really gives a path

Let `gamma,gamma'` be two disjoint proper crosscuts which both separate fixed boundary
markers `p,q`.  The interior of `gamma'` lies in one component of the disk minus
`gamma`.  If it lies in the `p` component, the `p`-shore of `gamma'` is contained in
the `p`-shore of `gamma`; if it lies in the `q` component, the reverse containment
holds.  Hence the `p`-shores of all selected crosscuts are totally ordered by
inclusion.

A totally ordered finite crosscut family has exactly one complementary region between
successive crosscuts, so its complement dual is a path.  A branch vertex would require
two incomparable shore sets and is impossible.

**Verdict:** PASS.

---

## 7. Exact-phase scope was correctly narrowed

The initial draft said the finite shrinking-window path automatically inherited the
exact-phase region-saturation factorization.  That was too strong without replaying the
companion theorem's phase-limit passage.  Commit `e69269bd` removed this inference.

The path theorem itself uses only:

- a shrinking phase window;
- pairwise noncrossing of that window;
- two-shore phase-zero pinning; and
- retained endpoint measure domination.

The Helly path-routing theorem is purely topological and remains available.  Any use of
the exact-phase rank factorization must keep its own scope separately.

**Verdict:** repaired before promotion; PASS.

---

## 8. What is genuinely new

Before this theorem the high-`t` same-phase O--O family could be a dual-tree star with
linearly many tiny branches.  After deleting `o(D)` retained pair weight, that topology
is impossible.  The surviving train counts are still

```math
>0.0700D-o(D),\quad >0.0466D-o(D),\quad >0.0246D-o(D)
```

at the `1.850`, `1.855`, and `1.860` checkpoints respectively, and their complement
dual is a path.

This does not close the high-`t` branch.  It does, however, restore interval entry/exit
counting and adjacent-cut finite-interface methods without using the low-`t` rectangle.

**Final disposition:** **PASS.** C-II and Level I remain open.
