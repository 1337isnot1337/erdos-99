> Generated reading edition · [exact source](../../research/target_c_attachment_cell_diameter_square_budget_2026-09-13.md) · source SHA-256 `f43a53ff5aa5e249e31f2e9942534bf88cf1cb06cb8c6fd5f25d06b66f264c5d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "182d699e5af4328ebc3be053138b1065362d721c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_attachment_cell_diameter_square_budget_2026-09-13.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "5c4e6f2a8445d80024e0a21f84481290f44797d5c3e875182fcb7e98f0265b54"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — attachment-cell diameter-square budget

**Date:** 2026-09-13
**Status:** proof-only full-core consequence; theorem-state authority unchanged.
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note extracts a source-level quadratic budget from the disjoint harmonic
attachment cells. It applies only in the canonical no-container full-core branch,
where the strict-rhombus area is asymptotically `(pi/4) D^2` and local
harmonic-face fidelity has been audited.

For an unloaded positive-contact component `I_r`, write

    P_r = conv(A_r),       d_r = diam(P_r).

Then

    sum_r d_r^2 >= D^2 - o(D^2).                         (CSB.1)

and therefore

    sum_r d_r >= D - o(D).                               (CSB.2)

Substitution into the exact Type-II five-currency identity gives

    G_D + Q + u_B + k <= 2(q-k) - D + o(D),              (CSB.3)

or, using `e_BB = Q + 2k + u_B`,

    G_D + e_BB - k <= 2(q-k) - D + o(D).                 (CSB.4)

This is an upper bound on the same global currencies that pay the canonical aggregate
detour. It is not a contradiction: the right side remains positive throughout the
currently allowed high-surplus region.

## 1. Full-core area is carried by the attachment cells

Let `A_4` be the total area of strict-rhombus bounded faces in the full positive-
contact core, and let `A_{4,r}` be the area of local strict-rhombus faces in cell `r`.
The audited full-core localization and face fidelity give

    sum_r A_{4,r} = A_4 - o(D^2).                         (CSB.5)

Every local rhombus lies in its attachment polygon `P_r`, and the interiors of the
`P_r` are pairwise disjoint. Hence

    sum_r area(P_r) >= sum_r A_{4,r} = A_4 - o(D^2).     (CSB.6)

In the no-container full-core branch,

    A_4 = (pi/4 - o(1)) D^2.                             (CSB.7)

The full-core fidelity hypothesis is essential. An arbitrary selected harmonic carrier
need not carry the global near-disk area, so (CSB.6) is not asserted for one carrier.

## 2. Isodiametric conversion

For every planar convex body, the isodiametric inequality gives

    area(P_r) <= (pi/4) d_r^2.                          (CSB.8)

Summing (CSB.8) and inserting (CSB.6)--(CSB.7) gives (CSB.1). Since the diameters are
nonnegative, `sum d_r >= sqrt(sum d_r^2)`, which gives (CSB.2).

No claim is made that the cells tile the force hull as sets. Only the audited local
rhombus inclusion and cell interior disjointness are used.

## 3. Exact currency consequence

The finite Type-II five-currency identity is

    2(q-k) + 2 = sum_r d_r + G_D + Q + u_B + k.          (CSB.9)

Insert (CSB.2) into (CSB.9) and absorb the fixed `2` into `o(D)` to obtain (CSB.3).
The Type-II loaded-hull identity `e_BB = Q + 2k + u_B` gives
`Q + u_B + k = e_BB - k`, proving (CSB.4).

On the Section-118 common-cap profile the stronger audited moment bound
`sum_r d_r >= 2.7985963122 D - o(D)` is available and supersedes (CSB.2). The present
budget is useful outside that profile because it uses only full-core area saturation.

## 4. What this does not settle

The budget does not upper-bound `G_D`, `e_BB`, or the aggregate outer detour separately.
It also does not supply a lower realization of inactive-container packing capacity. In
particular, it leaves the high-detour full-core scalar region feasible and does not
force an exact unit equilateral triangle or a source-preserving strict diameter descent.

All source points, including contact-isolated points, remain retained. No extension of
the ZR/ZF affine-kernel theorem and no KKT coefficient floor is used.

**Classification:** proved candidate awaiting independent audit; proof-only and scoped
as stated. C-II remains open.
