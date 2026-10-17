# Hostile audit — support-six `H5` metric boundary normal form

**Date:** 2026-09-18  
**Audited note:** `target_c_support6_h5_metric_boundary_normal_form_2026-09-18.md`  
**Certificate:** `verify_target_c_support6_h5_metric_normal_form_2026_09_18.py`  
**Disposition:** PASS at finite sign/order scope; no metric exclusion claimed  
**Theorem-state authority:** unchanged; C-II remains open.

## Scope checks

1. The script imports the preceding exact H5 verifier rather than reproducing a
   second, potentially divergent enumeration. It reruns the 370 rank-three
   extensions, 48 uniform labelled survivors, 316 simple walls, and 80 wall
   survivors before quotienting.
2. The representative count is checked before the new normal-form assertions:
   six uniform and ten simple-wall orbits.
3. The uniform assertion is only that the canonical missing matching is
   `16,25,34`, that `34` is the unique missing hull side, and that the present
   sides `01,12,23` agree while `04` has the opposite sign. It does not silently
   treat the missing edge `34` as signed.
4. The wall assertion is only for the canonical representative labeling supplied
   by the exact quotient: wall `036`, missing edge `36`, no missing hull side,
   and one common sign on all five hull sides. The two matching placements are
   checked explicitly.
5. The metric interface counts only present edges. Each vertex `1,...,5` has
   five present incident edges, giving ten scalar residual rows. No force or
   stress is assigned to a missing matching edge.
6. The note's statements about trace/tensor equations are inherited necessary
   identities. The new certificate does not evaluate them and does not claim a
   zero-free metric system.
7. The nonlinear least-squares observations are explicitly labeled exploratory;
   they are absent from the certificate and cannot be imported as an exclusion.

## Independent rerun

The following exact scripts pass consecutively:

```text
verify_target_c_support6_reciprocal_h7_exclusion_2026_09_18.py
verify_target_c_support6_reciprocal_h6_exclusion_2026_09_18.py
verify_target_c_support6_reciprocal_h5_reduction_2026_09_18.py
verify_target_c_support6_reciprocal_h5_double_wall_exclusion_2026_09_18.py
verify_target_c_support6_h5_metric_normal_form_2026_09_18.py
verify_target_c_support6_collapsed_local_realization_2026_09_18.py
```

The new script reports the exact normal forms and `18` present edges / `10`
scalar rows per representative.

## Binding limitation

The finite normal form is a proved candidate reduction, not a promoted theorem.
It does not eliminate any of the sixteen metric orbits. It also says nothing
about the all-equal collapsed support-six branch, whose local realization is a
separate certified regression. A closure still requires a metric contradiction,
a genuine reciprocal realization plus its global source test, or a global
source-preserving argument.

**Audit disposition:** PASS for the stated finite scope. C-II remains open.
