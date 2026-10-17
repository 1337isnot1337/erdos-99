> Generated reading edition · [exact source](../../../../docs/targets/target-c/56-ci-restored-frontier.md) · source SHA-256 `7289f07ee1afbf24584c8c6a7d8c7df20a63598e86f5aa106eb657f530c1d551`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — C-I restored; C-II remains the global gate

**LEVEL I STATUS: STILL OPEN.**

The [2026-09-09 dependency audit](../../reports/target_c_c53_orientation_and_ci_restoration_2026-09-09.md)
is promoted for precisely the following statements:

1. The September 5 pentagon C53.T regression is invalid: its projective order
   and common-half-plane orientation use different cuts.
2. With consistent normalization, C53.T holds for shared endpoints as well as
   disjoint crossing chords. The audit supplies a complete convex-deformation
   reduction and the exhaustive exact finite certificate.
3. For every normalized source KKT stress,
   `Omega=L_C(alpha)-L_H(beta)>=0` on all displacement coordinates. This uses
   the actual circular-planar response, its affine equilibrium identity, and
   the weighted Robinson lemma, not generic planar statics.
4. C63's fixed-matrix Newton–Hoffman corrections converge, releasing every weak
   active row while preserving feasibility. Contact minimality gives `C=C_*`.
   **Gate C-I is closed.**
5. Minimizing diameter-pair count second gives `H=H_*`. Every critical velocity
   then has actual nearby realizations preserving all active lengths exactly.
6. If Omega_bar is a relative-interior stress matrix, every mixed critical
   velocity, and every sufficiently small fixed-diameter feasible displacement,
   has both coordinate fields in `ker Omega_bar = intersection_s ker Omega_s`.
   This common-kernel conclusion uses finite lexicographic minimality, not generic
   PSD face selection. Isolated vertices retain free coordinates.

The existence of this lexicographically normalized representative suffices for
contradiction if any triangle-free global minimizer exists. Full diameter support
is not asserted for every unnormalized minimizer. Do not silently combine this
secondary minimization with contact-preserving hull saturation: the latter can
increase the number of diameter pairs.

## Exact remaining endpoint

Exclude, for every sufficiently large n, a triangle-free global minimizer chosen
to minimize contacts and then diameter pairs, whose actual active constraints all
have positive coefficients in a relative-interior normalized KKT stress.
Its contact-isolated points must be retained in the source population.

The [force-bulk audit](../../reports/target_c_force_bulk_and_correction_audit_2026-09-08.md)
still rejects the assertion that every isolated source point is diametral.
Its *different* acceptance of the pentagon PSD regression is withdrawn by the new
audit. These two corrections must not be conflated.

No other later C-II theorem is promoted by association. In particular this module
does not establish pure rhombic topology, a quantitative conductance floor,
dominant-diameter stress concentration for all sources, or the required global
contradiction. The near-chain degree-three and degree-five regressions remain valid.
