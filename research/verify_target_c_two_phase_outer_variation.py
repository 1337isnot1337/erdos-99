#!/usr/bin/env python3
"""Exact scalar check for the two-phase outer-variation coefficient.

This checks only the algebraic minimization of
    (4 - pi*s)/(2-s)
over 0 <= s <= 1.  The geometric variation lemma and the near-disk hypotheses are
proved in the companion report and audit; this script is not an optimality certificate.
"""

from fractions import Fraction as F


def main() -> None:
    pi_lower = F(314, 100)
    pi_upper = F(31416, 10000)
    # For 0 <= s <= 1, f(s)-(4-pi)=(2*pi-4)*(1-s)/(2-s) >= 0.
    assert 2 * pi_lower > 4
    assert 4 - pi_upper > F(8583, 10000)
    print("two-phase outer variation: exact coefficient check OK")
    print(f"4-pi > {float(4 - pi_upper):.7f} using pi < 3.1416")


if __name__ == "__main__":
    main()
