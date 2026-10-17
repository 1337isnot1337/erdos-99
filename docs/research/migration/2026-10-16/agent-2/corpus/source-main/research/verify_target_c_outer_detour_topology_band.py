#!/usr/bin/env python3
"""Exact rational check for the outer-detour topology band."""

from fractions import Fraction as F


def main() -> None:
    s0 = F(5597, 2000)  # conservative lower bound for S_*
    pi_upper = F(22, 7)
    k_upper = pi_upper - s0
    r_lower = 2 * s0 - pi_upper

    assert k_upper < F(3444, 10000)
    assert r_lower > F(2454, 1000)
    assert k_upper == F(4821, 14000)
    assert r_lower == F(17179, 7000)

    print("outer-detour topology band: exact checks OK")
    print(f"k/D < {float(k_upper):.9f}")
    print(f"r_H/D > {float(r_lower):.9f}")


if __name__ == "__main__":
    main()
