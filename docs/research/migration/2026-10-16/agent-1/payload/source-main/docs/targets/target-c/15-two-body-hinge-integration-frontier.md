# Target C — two-body hinge-integration frontier

**LEVEL I STATUS: STILL OPEN.**

Full proof: [target_c_two_body_hinge_integration_2026-08-31.md](../../reports/target_c_two_body_hinge_integration_2026-08-31.md).

## C59 — two null bodies cannot form a higher-order lock

Let a relative-interior fixed-diameter critical velocity be rigid on two source bodies `P,Q` with `P cap Q={x}` and different angular rates. After subtracting the rigid motion of `Q`, the relative motion is rotation of `P` about the shared source point `x`.

For an exclusive cross pair, zero first variation makes the two endpoint rays collinear with `x`.

- If the pair is an active unit contact, opposite rays are impossible because both endpoints are at least unit distance from `x`; they lie on the same ray, and finite relative rotation lengthens the pair quadratically.
- If the pair is an active diameter pair, same-ray placement is impossible because both endpoint radii lie in `[1,D]`; they lie on opposite rays, and finite relative rotation shortens the pair quadratically.

Strict first-order active rows remain strict for the chosen sign; inactive rows retain slack; internal distances of each rigid body are constant. An internal positive diameter remains exactly `D`.

Therefore, when all active vertices are covered by the two bodies, the hinge integrates to a finite same-diameter motion that releases every weak row. Contact minimality is contradicted.

## Effect after C58

C58 proves every different-motion pair of null-face extreme bodies has a zero-transfer midpoint whose positive diameter graph is a degree-at-most-five star forest. C59 shows that this electrical structure does not create a two-body higher-order lock.

A surviving C-I obstruction must now involve:

1. at least three genuinely distinct rigid-body motion classes; or
2. active vertices outside the relevant null-face body cover.

## Three-body reduction

For three distinct rigid motion classes `A,B,C`, let their pairwise shared source hinges be `x_AB,x_BC,x_CA`. Equality of rigid velocities at those vertices gives

`(omega_A-omega_B)x_AB + (omega_B-omega_C)x_BC + (omega_C-omega_A)x_CA = 0`.

The coefficients sum to zero and are nontrivial, so the three hinge vertices are collinear.

Thus the next branch is a collinear multi-body pin mechanism, not an arbitrary pin triangle.

## Next target

Combine the collinear-hinge identity with C58's bounded zero-transfer star forests and source separation to eliminate or finitely integrate three distinct body motions. Then address any residual null-face coverage defect.
