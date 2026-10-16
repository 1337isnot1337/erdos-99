"""Arithmetic checks for the attachment-cell diameter-square budget.

The geometric inputs (full-core rhombus localization and cell disjointness) are
theorem dependencies. This script checks only the displayed coefficient conversion
and a current scalar witness showing that the combined upper budget is not a closure.
"""

from fractions import Fraction as F


def main() -> None:
    # Isodiametric conversion: area >= pi/4 D^2 implies sum d_r^2 >= D^2.
    pi_lo = F(314159, 100000)
    pi_hi = F(314160, 100000)
    area_coeff = pi_lo / 4
    square_diameter_coeff = 4 * area_coeff / pi_hi
    assert square_diameter_coeff > F(999, 1000)

    # The current high-surplus endpoint-style scalar witness remains feasible.
    t = F(29, 10)
    k = F(0)
    s = F("2.798596312209462")
    g = F("0.291043460511411")
    m = s + g - t
    e = t - m
    combined = g + e - k
    assert m > 0 and e > 0
    assert combined < 2 * t - 1

    print("attachment-cell diameter-square budget arithmetic: OK")
    print(f"certified_square_diameter_coefficient>{float(square_diameter_coeff):.6f}")
    print(f"witness_combined={float(combined):.9f} upper={float(2*t-1):.9f}")


if __name__ == "__main__":
    main()
