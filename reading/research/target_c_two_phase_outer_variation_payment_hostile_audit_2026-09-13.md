> Generated reading edition · [exact source](../../research/target_c_two_phase_outer_variation_payment_hostile_audit_2026-09-13.md) · source SHA-256 `26fbaff6f7b0717898f291c0c9073091d0549de551cf167c3a2f5d6115b58d19`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c56d2d15cbc59b0cfdae0b4998f64f52410c005c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_two_phase_outer_variation_payment_hostile_audit_2026-09-13.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "793aae2cac5d1a2ecfa9b1dc063c58cd0caa514ac56e8b512d859f5075e45ca0"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — Target C two-phase outer-walk variation payment

**Date:** 2026-09-13  
**Artifact:** `target_c_two_phase_outer_variation_payment_2026-09-12.md`  
**State lock:** `2026-09-12.audit.46`  
**Verdict:** PASS at the stated finite/near-geodesic scope; no C-II closure.

## 1. Determinant variation

For unit vectors `u,v` with `s=sin(theta)>0`, the determinant functionals have the
following exact increments:

- a step `+/-u` changes `det(x,v)` by `+/-s` and does not change `det(u,x)`;
- a step `+/-v` changes `det(u,x)` by `+/-s` and does not change `det(x,v)`;
- every other unit step changes either determinant by absolute value at most one.

The range of `det(x,v)` on a convex set is its width in the unit normal direction
`Jv` (up to orientation), and similarly for `det(u,x)` and `Ju`. A closed walk that
visits both support lines has total variation at least twice this range. Therefore

`s N_u+N_o >= 2 width_{Jv}(P)` and
`s N_v+N_o >= 2 width_{Ju}(P)`.

The source artifact's earlier normalized-coordinate wording had the coefficients
reversed; the version audited here uses the unnormalized determinants and the displayed
inequalities are the corrected ones.

**Verdict:** pass after the stated correction.

## 2. Algebraic near-disk consequence

If both widths are `D-o(D)`, adding the two inequalities gives

`s(N_u+N_v)+2N_o >= 4D-o(D)`.

Since `b=N_u+N_v+N_o`, this is exactly

`s b+(2-s)N_o >= 4D-o(D)`.

With `b <= pi D+o(D)`, it follows that

`N_o >= (4-pi s)/(2-s) D-o(D)`.

The derivative of `(4-pi s)/(2-s)` is `(4-2pi)/(2-s)^2<0`, so on
`s in [sqrt(3)/2,1]` its minimum is `4-pi`. The numerical coefficient
`0.8584073464...` is therefore valid.

**Verdict:** pass.

## 3. Geometric scope

The argument counts edge occurrences, so bridges and repeated boundary vertices do not
invalidate the variation lower bound. It requires only that the selected closed walk's
convex hull have the two stated widths and that its length be near-geodesic. It does
not identify the walk with a simple physical boundary, and it does not identify
`N_o` with `P_exc`, `e_BB-k`, or any other canonical scalar.

For a Type-II force hull converging after scaling to the radius-`1/2` disk, every fixed
direction has width `D-o(D)`. Applying the lemma to an outer walk whose hull is that
force hull is therefore within the stated scope; applying it to an arbitrary harmonic
cell requires the width hypothesis separately.

**Verdict:** pass with the explicit near-geodesic/near-disk hypothesis.

## 4. Closure gate and regressions

The conclusion is a linear population of non-two-phase boundary occurrences, not a
positive signed-return constant. A non-two-phase edge can be a singleton train or a
bridge and need not bound a nonquadrilateral face. Charging it to the canonical
exceptional-face or loaded-side currencies would require a new planar incidence
theorem. The four-host oblique-grid regression remains compatible when the walk is not
near-geodesic around a near-disk.

Contact-isolated source points are untouched; no source-preserving descent, unit
triangle, or Level-I conclusion is claimed.

**Final classification:** audited-working proof-only bridge. The theorem state remains
unchanged and C-II remains open.
