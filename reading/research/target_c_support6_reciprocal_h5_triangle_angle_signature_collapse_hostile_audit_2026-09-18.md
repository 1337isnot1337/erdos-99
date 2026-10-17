> Generated reading edition · [exact source](../../research/target_c_support6_reciprocal_h5_triangle_angle_signature_collapse_hostile_audit_2026-09-18.md) · source SHA-256 `a5d13e49f4d1dea021f55ffb68f9da71d8e66ef9b82415d4a854fcf221e16dbd`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "65ddd7a7311f30480db38e4819fccbc2f7a91a3d", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_reciprocal_h5_triangle_angle_signature_collapse_hostile_audit_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "9aa87f1184fa0aa649f153d3b7e3b56ae07835d0795a88e8ed17b26aed756784"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — H5 triangle-angle signature collapse

**Date:** 2026-09-18  
**Audited note:** `target_c_support6_reciprocal_h5_triangle_angle_signature_collapse_2026-09-18.md`  
**Certificate:** `verify_target_c_support6_reciprocal_h5_triangle_angle_signature_collapse_2026_09_18.py`  
**Disposition:** PASS with the scope limits below. C-II remains open.

## 1. The raw-angle conversion has the correct four branches

At reciprocal vertex `i`, write the raw ray toward `a` as `r_a=y_a-y_i` and its signed force ray as `f_a=s_ia r_a`, with `s_ia=+/-1`.  Let `R` be the counterclockwise force angle from `f_a` to `f_b`, normalized by `pi`.

If the two signs agree, the force and raw angular differences agree modulo `2pi`.  Raw orientation `chi>0` means the counterclockwise raw difference lies in `(0,pi)`, giving interior angle `R`; `chi<0` means it lies in `(pi,2pi)`, giving `2-R`.

If the signs differ, exactly one ray is reversed.  For `chi>0`, the force CCW difference is the raw interior angle plus `pi`, so the raw interior angle is `R-1`.  For `chi<0`, the force CCW difference is the complement after the reversal, giving `1-R`.  Thus the four cases in equation (2.1) are correct.  No branch assumes a numerical coordinate realization.

## 2. The orientation signs really are fixed by the current exact data

At the ground vertex, the current uniform H5 reduction gives raw radial order

`1,6,5,2,3,4`

inside a cone of width `<pi/3`.  Hence every pairwise raw orientation sign is determined by linear order; there is no wraparound ambiguity because the entire cone has width below `pi`.

At each non-ground reciprocal vertex, the current exact force cycle is a strict convex five-ray order satisfying the two-turn theorem.  Hence a force ray has positive cross product with precisely the next two force rays and negative cross product with the previous two.  Multiplying by the two reciprocal edge signs recovers the raw orientation sign.  This is exactly what the certificate implements.

The certificate therefore does not import any unproved chirotope or coordinate information beyond the sign/order representatives already established in the repository.

## 3. Every triangle used is present

The missing reciprocal matching is `{16,25,34}`.  The triangle functionals used in the three sparse identities are:

- `P1`: `012,015,023,035,045,046,056`;
- `P2`: `012,013,023,045,046,056`;
- `P3`: `014,023,024,026,035,046`.

None contains a missing edge.  Thus each is an actual Euclidean triangle on three distinct noncollinear reciprocal points, so its ordinary interior angles sum exactly to `pi`.

## 4. The sparse identities are affine identities, not consequences of plugging target values

The verifier represents every exterior gap `x_i,k` as an independent formal variable.  It constructs every raw triangle angle from the four-branch formula, then compares full coefficient dictionaries and affine constants.

For each orbit it verifies the target surface-class gap functional equals the claimed integer combination of face functionals `F_i`, triangle functionals `T_ijk`, and the displayed constant **before** using `F_i=2` or `T_ijk=1`.

Only after coefficient equality is established does it substitute those universal equalities.  The resulting exact values are

- `P1`: eleven-corner target gap sum `G/pi=5`, hence cone order `(11-5)/2=3`;
- `P2`: twenty-two-corner target gap sum `G/pi=8`, hence cone order `(22-8)/2=7`;
- `P3`: fourteen-corner target gap sum `G/pi=6`, hence cone order `(14-6)/2=4`.

The certificate uses integer arithmetic only.  There is no floating point, tolerance, numerical rank test, or optimization step.

## 5. The surface cone conversion has the correct sign

If a surface vertex class contains `N` polygon corners and the associated physical/ground exterior gaps sum to `G*pi`, the glued cone angle is

`N*pi-G*pi`.

Thus `2*pi*m=N*pi-G*pi`, giving `m=(N-G)/2`.  This is consistent with the earlier surface-signature verifier and with the total cone-order sum eleven.

Consequently the final signatures are forced as follows:

- `P1`: target order three; three small order-one classes; remaining order five, so `(5,3,1,1,1)` and `H(4,2)`;
- `P2`: target order seven and four order-one classes, so `(7,1,1,1,1)` and `H(6)`;
- `P3`: target order four; small class order one; remaining order six, so `(6,4,1)` and `H(5,3)`.

The former `P1 H(3,3)` and `P3 H(4,4)` alternatives are genuinely removed.

## 6. Scope limits

This result does **not** eliminate `P1`, `P2`, or `P3`.  It proves a necessary signature for each if a metric reciprocal realization exists.  It does not solve the equilateral force-polygon closure equations, the positive reciprocal edge-length equations, or the signed trace balance.

It also says nothing about the collapsed support-six branch.  That branch has a separate certified local realization and still requires a global train/source or diameter-locking obstruction.

No theorem-state file should be changed from this result alone.

**Audit disposition:** PASS.  The two-signature elimination is an exact consequence of the already established H5 sign/order data and Euclidean triangle angle sums.  C-II remains open.
