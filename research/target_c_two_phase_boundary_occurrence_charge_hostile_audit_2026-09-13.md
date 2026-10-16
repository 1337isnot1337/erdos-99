<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3c1978f31e52e642c6a0f702c3a1209ac00dd661", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_two_phase_boundary_occurrence_charge_hostile_audit_2026-09-13.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "54cc07a0ce3b15c640bd571734ffa126a851931b3dd49f183f5448bfac3ed064"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — Target C two-phase boundary occurrence charge

**Date:** 2026-09-13  
**Artifact:** `target_c_two_phase_boundary_occurrence_charge_2026-09-13.md`  
**State lock:** `2026-09-12.audit.46`  
**Verdict:** PASS at the stated finite incidence scope; no C-II closure.

## 1. Bridge multiplicity

The factor two is attached only to bridge edges that actually occur on the outer
face. In a connected plane graph, a bridge is incident to the same face on both sides;
if that face is the outer face, its facial boundary walk traverses the bridge once in
each direction. A bridge embedded inside a bounded face is not counted by `B_o` and
does not enter the outer-walk charge. Thus the report does not assume that every graph
bridge is outer-visible.

**Verdict:** pass.

## 2. Non-bridge face charge

For a non-bridge edge occurrence on the outer face, the opposite incident face is a
unique bounded face. If it were a quadrilateral, the phase-purity hypothesis makes all
of its edge directions `[u]` or `[v]`, so the occurrence would not be in `N_o`.
It is therefore a nonquadrilateral face edge. The map from outer edge occurrences to
their opposite face-edge incidences is injective, including when face boundary walks
repeat vertices. The total available incidence count is exactly `P_exc`.

**Verdict:** pass.

## 3. Combination with outer variation

The two-phase variation theorem supplies `N_o >= (4-pi)D-o(D)` only when the selected
outer walk has the explicit near-disk width and near-geodesic length hypotheses. The
charge lemma itself is finite and does not silently promote those hypotheses to an
arbitrary harmonic cell. Substitution gives (BC.2) with the correct sign.

The Section-123 estimate `P_exc <= 10(e_BB-k)` is invoked only for a harmonic induced
graph in the canonical Type-II scope; no global injectivity of local outer occurrences
is inferred.

**Verdict:** pass.

## 4. Remaining obstruction

The result does not bound `B_o`, does not identify a bridge with a positive KKT edge,
and does not turn a linear bridge population into a strict diameter decrease. A bounded
quadrilateral in a different phase is outside the phase-purity hypothesis and must be
charged by a separate interface theorem. Contact-isolated source points remain
untouched.

**Final classification:** proved candidate awaiting promotion; proof-only. The theorem
state remains unchanged and C-II remains open.
