# Scope erratum — superseded `0.0052` phase-star orbit-capacity draft

**Date:** 2026-09-15  
**Affected:**
- `research/target_c_phase_star_orbit_capacity_gap_0052_2026-09-15.md`
- `research/verify_target_c_phase_star_orbit_capacity_gap_0052.py`

**Disposition:** **DO NOT CITE THE `0.0052` NOTE AS A PROOF.**  
**Replacement:** `research/target_c_phase_star_orbit_capacity_gap_0053_2026-09-15.md`.

The `0.0052` draft correctly identifies the phase-star crossing-capacity mechanism and
its low-center optimizer, but its displayed definition of the capacity function lets
the formal center phase mass `C` range above

\[
K={2\over\sqrt3}.
\]

The physical two-family missing-pair theorem used to derive the penalty term assumes
each selected phase family has mass at most `K`.  Therefore the draft's application of
that penalty on the formal `C>K` portion is outside the stated scope of its dependency.
The accompanying arithmetic certificate does not repair a hypothesis mismatch.

The corrected `0.0053` theorem splits the optimization before invoking the pair theorem:

- for `C<=K`, it uses the physical phase-star penalty and proves the optimizer lies in
  `(W/3,W/2) subset (0,K)`;
- for `C>K`, it uses only the generic valid bound `E<=C(W-C)`, which is decreasing in
  `C` because the relevant orbit mass satisfies `W<2K`.  The exact certificate shows
  this high-center branch lies more than `0.0348` below the required crossing density.

With that scope repair, the exact certificate safely proves the stronger matched gap
`g=0.0053`.

This erratum changes no canonical theorem-state file.  It exists to prevent the stale
proof-only draft from being propagated by later research workers.
