"""Arithmetic and small-incidence checks for the bridge-subtracted note.

The planar incidence proof is recorded in
target_c_bridge_subtracted_isoperimetry_2026-09-13.md.  This script checks the
displayed finite toy bounds, the endpoint constant, and the asymptotic formula.
It does not certify a global minimizer, near-disk saturation, or two-phase purity.
"""

from fractions import Fraction as F


def main() -> None:
    # Certified pi enclosure used only for strict toy inequalities.
    pi_lo = F(314159, 100000)
    pi_hi = F(314160, 100000)

    # Unit square cycle: L=4, no outer bridges, area=1.
    square_bound_lo = F(16, 4 * pi_hi)
    assert square_bound_lo > 1

    # Add one pendant outer bridge.  Its two occurrences are removed by 2 B_o,
    # leaving the same square perimeter budget.
    pendant_bound_lo = F((6 - 2 * 1) ** 2, 4 * pi_hi)
    assert pendant_bound_lo > 1

    # A pendant edge drawn into the bounded square face is an internal bridge:
    # B_o=0 and the outer walk remains L=4.  The subtraction must not be applied.
    internal_bridge_bound_lo = F(16, 4 * pi_hi)
    assert internal_bridge_bound_lo > 1

    # Near-geodesic, near-isodiametric saturation forces the normalized bridge count
    # to zero.  Use an explicit rational epsilon/rho instance of (BI.4).
    eps = F(1, 10**6)
    rho = F(1, 10**3)
    # Since sqrt(pi*(pi/4-eps)) > pi/2 - 2 eps for this tiny eps, the displayed
    # right side is below rho/2 + 2 eps.
    assert F(1, 2) * (rho + 4 * eps) < F(1, 100)

    # Full bounded-face area saturation gives the stronger endpoint payment.
    full_endpoint_floor = (4 - pi_hi) / 10
    assert full_endpoint_floor > F(85, 1000)

    # Strict-rhombus-only saturation retains one extra P_exc in the bridge
    # inequality, so the safe endpoint coefficient is half as large.
    rhombus_endpoint_floor = (4 - pi_hi) / 20
    assert rhombus_endpoint_floor > F(42, 1000)

    print("bridge-subtracted isoperimetry arithmetic: OK")
    print(f"square_area_bound_lower={float(square_bound_lo):.9f}")
    print(f"full_endpoint_payment_lower={float(full_endpoint_floor):.9f}")
    print(f"rhombus_endpoint_payment_lower={float(rhombus_endpoint_floor):.9f}")


if __name__ == "__main__":
    main()
