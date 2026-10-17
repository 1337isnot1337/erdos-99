#!/usr/bin/env python3
"""Exact rational certificate for the scoped common-cap t floor.

The certificate checks the arithmetic implication from audited §161 after inserting
the Section-118 common-cap lower bounds for the diameter moment and component
remainder. It also checks a rational point above the floor. It does not prove the
geometric profile hypotheses or global optimality.
"""

from fractions import Fraction as F


def main() -> None:
    # Conservative lower enclosures for the audited profile constants.
    s_lo = F(2798596, 1_000_000)
    g_lo = F(291043, 1_000_000)
    pi_lo = F(314159, 100_000)
    sqrt3_hi = F(173206, 100_000)
    c_lo = pi_lo * (2 - sqrt3_hi) / 4

    floor_lo = (3 * s_lo + 2 * g_lo + c_lo) / 5
    assert floor_lo > F(18376, 10_000)

    # The scoped floor is not a scalar closure: this point remains feasible.
    t = F(37, 20)
    kappa = F(0)
    s = F(14, 5)
    g = F(3, 10)
    c = pi_lo * (2 - sqrt3_hi) / 4
    assert 5 * t - 2 * kappa > 3 * s + 2 * g + c
    assert t > floor_lo

    print(f"scoped_floor_lower_bound={float(floor_lo):.12f}")
    print("common-cap t-floor arithmetic: OK; scope remains proof-only")


if __name__ == "__main__":
    main()
