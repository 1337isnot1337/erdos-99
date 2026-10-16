<!-- theorem-state: {"artifact_id":"ART-4EED4FDCBA78","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_inactive_chamber_near_contact_regression_2026-09-12.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=b0d0f9e70c240f4b8aea844c1bde8753c5499378; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C inactive-chamber near-contact regression

Status: **unreviewed candidate / regression certificate**.  This artifact is
proof-only research.  It is not a theorem about global minimizers and does not
change canonical Target C state.

## Exact construction

For an integer m >= 8, take the finite set

    C_m = { i s u + j s v : 0 <= i,j <= m },

where u and v make an angle of pi/3 and

    s = 1 + 1/m.

The squared distance between two distinct lattice points with index
difference (a,b) is

    s^2 (a^2 + ab + b^2).

The integer quadratic form in parentheses is at least one for every
nonzero integer pair.  Consequently every pair in C_m is at distance
strictly greater than one.  The unit-contact graph is empty, so every point is
contact-isolated and the construction contains no unit equilateral triangle.

The convex hull is the side-m s rhombus.  After normalizing area by the area
of a unit equilateral triangle, its area is

    (m s)^2 = (m+1)^2 = |C_m|.

Thus this chamber saturates the leading Oler area term exactly while its
perimeter contribution is only

    (4 m s)/2 + 1 = 2(m+1)+1.

## Deep near-unit population

For every row index 2 <= j <= m-2, pair consecutive points with even
indices

    (2,j),(3,j); (4,j),(5,j); ...

These pairs are vertex-disjoint, have distance s = 1+1/m, and have both
endpoints at least two lattice steps from every chamber side.  Their number
is

    floor((m-3)/2)(m-3),

which is quadratic in m.  Therefore a quadratic population of
contact-isolated points and a quadratic population of deep, near-unit
inverse-diameter pairs coexist with exact chamber saturation and linear
boundary slack.

The script
target_c_inactive_chamber_near_contact_regression.py checks all of these
assertions with exact rational arithmetic.

## What this kills

This is a direct counterexample to the following local closure implication:

    near-capacity chamber + hull saturation + quadratic deep near-unit matching
    => exact unit contact, unit triangle, or a positive KKT activation that
       necessarily changes the active geometry.

The construction has no positive contact at all, so it also exhibits the
strongest form of the contact-activation failure recorded in proof-only
Section 95: first-contact motions can add contacts without providing a
source-level strict-diameter competitor.

## What it does not kill

C_m is only an inactive chamber.  It is not co-embedded with a diameter-carrying
positive-contact core, and it is not asserted to be a global
minimum-diameter configuration.  Shrinking this chamber alone leaves the
diameter of an external core unchanged.  Hence the certificate supplies no
global contradiction and cannot close the macroscopic-container branch.

The surviving bridge must therefore use information coupling the chamber to the
full source: a strict source-preserving diameter decrease, a theorem that the
chamber cannot coexist with the diameter-carrying core, or an exact triangle
forced by the coupled boundary/contact geometry.
