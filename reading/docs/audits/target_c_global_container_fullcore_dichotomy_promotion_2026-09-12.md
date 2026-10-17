> Generated reading edition · [exact source](../../../docs/audits/target_c_global_container_fullcore_dichotomy_promotion_2026-09-12.md) · source SHA-256 `33d777f23f364096dbdc5454c2af94364e882614d58a6bc9be9996680c21d636`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C84BDE6027C2","canonical":true,"claim_ids":["C-FULLCORE-NEAR-DISK","C-INACTIVE-DICHOTOMY"],"claim_statuses":{"C-FULLCORE-NEAR-DISK":"canonical","C-INACTIVE-DICHOTOMY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C §§79–80 promotion audit

**Date:** 2026-09-12

This note records the hostile audit of the proof-only modules
`79-inactive-chamber-rhombic-saturation-dichotomy-audit.md` and
`80-global-isolate-concentration-fullcore-disk-audit.md`.

## Certified chain

1. Canonical Section 77 supplies, for all post-ZF survivors,
   `a_0 Z_ch=A_ch+O(D)`, total inactive-chamber perimeter `P_ch=O(D)`, and
   total isolate-only Oler slack `Sigma_ch=O(D)`. The exact face ledger and the
   Section-68 defect bound give `m=R_4+O(D)`; this uses
   `q,d_H,s_Z,f=O(D)`, with `s_Z=O(D)` coming from the canonical difference-body
   inequality, not from an unstated stress-weight floor.
2. Isoperimetry gives
   `sum_j sqrt(A_j) <= P_ch/(2 sqrt(pi))=O(D)`. Consequently
   `A_ch <= sqrt(A_max) O(D)`. A quadratic `Z_ch` therefore forces one actual
   chamber with `A_max=Omega(D^2)`, and its individual Oler slack and perimeter
   remain `O(D)`. Conversely `A_max=o(D^2)` implies
   `A_ch,Z_ch=o(D^2)`, hence `m=N_F-o(D^2)` and
   `A_4=A_F-o(D^2)`.
3. The same capwise Oler calculation applies to the exterior caps between the full
   source hull and the force hull. Their total area is `A_K-A_F`, total perimeter is
   at most `2 pi D`, and their summed Oler slack is `O(D)`. Thus a quadratic
   exterior population forces one macroscopic exterior cap; if every exterior cap
   is `o(D^2)`, then `Z_ext=o(D^2)`.
4. If no internal chamber and no exterior cap is macroscopic, then
   `n-m=o(D^2)`, while the full translated-lattice/Oler comparison gives
   `a_0 n=pi D^2/4+O(D)`. Section 77 gives `a_0N_F=A_F+O(D)`, so
   `A_F/D^2 -> pi/4`; the exact diameter of `F` is `D`, and compactness plus the
   planar isodiametric equality case yields convergence of `D^{-1}F` to a radius-
   `1/2` disk (up to translation). The same identities give
   `m/D^2,R_4/D^2 -> pi/(2 sqrt(3))` and `A_4/A_F ->1`.
5. The fixed-width phase cut deletes only `O_epsilon(D)` rhombi and leaves a
   finite-perimeter coherent-grain family covering `F` up to `o(D^2)` area. The
   proof uses the square-root grain budget to discard only an arbitrarily small
   area tail; it does not assert one grain, exact lattice equality, or simultaneous
   compatibility of local motions.

## Scope correction

The promoted global alternative treats exterior-cap points simply as source points
outside the positive force hull. The audit does not need, and therefore does not
promote, the stronger prose in §80 claiming that every external-cap point is
contact-isolated. Internal chamber points are the contact-isolated population covered
by canonical Section 77 and the existing `C-INACTIVE-*` modules. No KKT-positive
contact is assigned to any point by this promotion.

## Non-conclusions

This is a population/geometry reduction, not a Level-I closure. In the macroscopic
container branch it supplies no source-preserving strict sub-`D` competitor and no
simultaneous pair-closing theorem. In the full-core branch it supplies no phase
aggregation inequality, no boundary-order surplus, and no exact unit triangle. The
near-disk limit is qualitative; no rate is inferred.

## Disposition

The two exact alternatives are valid and should be promoted as
`C-INACTIVE-DICHOTOMY` and `C-FULLCORE-NEAR-DISK`, with dependencies limited to the
canonical Section-67/68/69/77 chain, `C-FS-STABILITY`, and standard convex geometry.
C-II remains open. The next proof obligation is now explicitly one of:

* couple a macroscopic isolated container to global diameter minimality, or
* extract a strict boundary/interface surplus from the asymptotic full-core near-disk
  rhombic branch.
