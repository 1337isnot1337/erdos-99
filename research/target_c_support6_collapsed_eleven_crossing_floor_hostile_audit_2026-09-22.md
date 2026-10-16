<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "63ede82aa50f8dc81141ca585d1d4c837a5259a7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_collapsed_eleven_crossing_floor_hostile_audit_2026-09-22.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "401ea5622d3bae4627ce1240c451639dd87dfd7ea8e91fed3cea06bd3d6b6eab"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — collapsed support-six eleven-crossing floor

**Audited note:** `target_c_support6_collapsed_eleven_crossing_floor_2026-09-22.md`  
**Certificate:** `verify_target_c_support6_collapsed_eleven_crossing_floor_2026_09_22.cpp`  
**Disposition:** PASS at exact finite/global train-topology scope; theorem-state authority unchanged; C-II remains open.

## Claim audited

For every globally realizable degree-pure collapsed support-six block, the number
(X_K) of strict-rhombus crossings between its twelve internal relation trains
satisfies

\[
X_K\ge11.
\]

The earlier independently audited certificate excluded weights (0,ldots,9). The
new certificate therefore has to exclude exactly weight (10).

## Completeness of the finite search

The verifier reconstructs the same 388 exact rational rotation cells and 42
conservative sign-preserving symmetry representatives as the preceding certificate.
For each representative it enumerates every affine MI.1 solution of weight ten. The
printed `parity` count is the total MI.1 survivor count; `tri` applies the necessary
triangle-free condition; `metric` counts assignments with at least one simultaneous
orientation of all strict crossing windows; and `planar` counts assignments for which
some crossing-order permutation has genus zero.

The aggregate output is

```text
TOTAL k=10 parity=58377 tri=40324 metric=20349 planar=0
```

The 66 possible train pairs are all represented before the filters. Enumerating the
42 representatives is complete in the excluding direction because relabeling and
reflection transport the rotation cell, parity equations, angle windows, forced
crossing rotations, and Euler genus.

## Simultaneous metric test

Each selected pair is assigned either

\[
1<x_e-x_f<2
\quad\text{or}\quad
1<x_f-x_e<2.
\]

All ten selected inequalities are appended to one common copy of the cell constraints.
Thus independently compatible pairs are not silently combined from different angle
vectors. The transformed integer difference constraints use strict bounds of the form
(14c-1), so the feasibility decision is exact. Unselected pairs are left
unconstrained, enlarging the candidate set and making the exclusion safe.

## Crossing rotations and planarization

For every metric orientation, the cyclic order at each crossing is forced by the sign
of the determinant of the two upper-half-plane train directions and the coherent train
orientations. The code does not choose either alternating crossing rotation freely.

If a train participates in several selected crossings, their order along that complete
train is not fixed by the projective cell. The verifier recursively enumerates every
permutation of those crossings independently. Therefore the actual order in any global
drawing is included. At each resulting degree-four rotation system it computes the
face permutation and Euler genus. Positive genus for every permutation is a valid
necessary-condition obstruction; genus zero would only be a survivor, not a
realization.

Deleting external trains from a hypothetical global drawing leaves the twelve internal
train paths, their mutual crossing vertices, and the six exceptional terminal disks in
a planar drawing. External crossings cannot repair a positive-genus planarization of
the retained subdrawing. Thus the certificate applies to the internal crossing set
even when additional global trains exist.

## Global summation check

Internal train sets of distinct collapsed components are disjoint. A rhombus has
exactly two complete train tracks, so a rhombus counted in (X_K) cannot also be
counted in (X_{K'}) for (K\ne K'). Therefore (TC.2) follows by summation, with
no double counting. The tangent-payment inequality is used only as a separate upper
bound on (c_6); no independence assumption between the two currencies is needed.

## Audit conclusion

The exact weight-ten certificate passes and, together with the audited weights through
nine, proves the scoped structural floor (X_K\ge11) for any global degree-pure
collapsed support-six block. It does not eliminate the collapsed branch, prove an
eleven-crossing realization, or change canonical theorem state.
