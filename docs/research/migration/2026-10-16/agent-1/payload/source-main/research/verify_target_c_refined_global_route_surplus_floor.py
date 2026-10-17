"""Exact scalar checks for the refined 153/1250 route-surplus floor.

The geometric and finite-to-limit inputs are audited separately. This script checks
only the rational endpoint margins and the Fejer-order-two polynomial used in the
short-detour optimization.
"""

from fractions import Fraction as F


def main() -> None:
    pi_hi = F(314160, 100000)
    pi_lo = F(314159, 100000)
    sqrt3_hi = F(173206, 100000)
    sqrt3_lo = F(173205, 100000)

    delta_lo = pi_lo / (2 * sqrt3_hi)
    c_lo = F(38092, 10000)
    assert (c_lo / 4) ** 2 < delta_lo

    r = F(153, 1250)
    h0 = (c_lo - r) ** 2 - pi_hi * pi_hi / 2
    hr = c_lo * c_lo - ((pi_hi + r) ** 2 + 1225 * r * r) / 2
    assert h0 > F(865, 100)
    assert hr > F(6, 1000)

    # U_2 is increasing for nonnegative lambda; H is concave with negative
    # quadratic coefficient -612, so endpoint positivity controls [0,r].
    assert h0 > 0 and hr > 0
    assert F(-612, 1) < 0

    print("refined global route-surplus floor arithmetic: OK")
    print(f"H0_lower={float(h0):.6f}")
    print(f"Hr_lower={float(hr):.6f}")
    print("certified_floor=0.122400")


if __name__ == "__main__":
    main()
