<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "022c74d44e90b7a1dfd3184526517d2fc2b299ef", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_h5_uniform_projection_potential_hostile_audit_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "802383d693886143ad55d134375a7e9f733d157d4d1fb788e5b0daf3020de909"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — uniform `H5` projection-potential exclusion

**Date:** 2026-09-18  
**Audited artifact:** `verify_target_c_support6_h5_uniform_projection_potential_2026_09_18.py`  
**Disposition:** passes finite certificate and scope audit; promotion still requires the repository review process

## Audit checks

1. The script imports the existing exact H5 reduction and obtains exactly six
   canonical uniform representatives. It does not enumerate or silently drop a
   metric case.
2. Each stored coordinate array is integer-valued and is checked against every
   target triple sign. No floating-point predicate is used in the coordinate
   sanity check.
3. The authoritative certificate adjoins a formal point at infinity and checks
   all rank-three Grassmann--Pluecker tests on every eight-element extension
   induced by each of the `7!` projection orders. This is an overapproximation
   of realizable metric projections, so failure of every acyclic extension is
   sufficient.
4. The signed constraint graph contains precisely the present edges from the
   H5 representative; missing matching edges are not reintroduced.
5. The graph test is an exact topological-sort test. Acyclicity would provide a
   scalar potential whose every term in the summed equilibrium identity is
   positive.
6. The identity uses all six non-ground face closures. It does not infer a
   closure equation merely from the five independent rows displayed in the
   metric-interface note: the sixth face closure is part of the reciprocal
   construction, and the ground row follows by endpoint cancellation.

An independent full-permutation recomputation of the rank-three tests agrees with
the reduced verifier for all six representatives: the extension counts are
`140,140,146,152,152,156`, with no reduced-test false positives.

## Potential scope issue

The coordinate realization is not used as the proof of completeness. The
formal-infinity extension test is the finite overapproximation used for that
purpose. The argument is not a claim that one sampled coordinate realization
represents arbitrary metric lengths or a physical source configuration.

The certificate therefore proves a uniform-order-type obstruction to the full
signed reciprocal equilibrium. It does not cover a simple ground-collinearity
wall, a higher-codimension wall, or the collapsed support-six branch. It also
does not promote the result into `docs/state/theorem-state.yaml`.

**Audit result:** the six uniform H5 cases are rigorously excluded subject to
the stated allowable-sequence lemma; the ten simple-wall cases remain the
smallest noncollapsed finite obstruction.
