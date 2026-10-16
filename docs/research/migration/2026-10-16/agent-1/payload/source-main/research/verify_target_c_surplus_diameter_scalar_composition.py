#!/usr/bin/env python3
"""Check the corrected algebra in the withdrawn surplus/moment composition.

This is a proof-only scalar check.  It does not construct a geometric contact
complex or establish global optimality.
"""

from fractions import Fraction as F


def main() -> None:
    z0 = F(2401, 2500)  # 0.9604
    S0 = F(5597, 2000)  # 2.7985
    c0 = F(263, 1250)   # 0.2104
    A0 = 3 * S0 + c0

    # The former 2.0585 floor treated the finite constant 2 in
    # c_I+s_C=m+k-2 as 2D. After normalization the surplus inequality is
    # 2t+kappa >= z0 (up to o(1)); it adds no new floor to the moment bound.
    assert A0 / 5 > F(172, 100)

    # Former t=1.9 witness: the corrected surplus upper bound is positive.
    assert 2 * F(19, 10) > z0

    # Corrected asymptotic scalar witness.
    t = F(19, 10)
    kappa = F(0)
    e = F(9, 10)
    c = F(0)
    s = F(1)
    q = t + kappa
    m = q - e

    assert e == t + 2 * kappa - c - s
    assert e + 2 * s - 3 * kappa > z0
    assert 5 * t - 2 * kappa > A0
    assert m == F(1)
    assert q == F(19, 10)

    print("withdrawn surplus/diameter composition: corrected checks OK")
    print(f"moment_only_t_floor={float(A0 / 5):.9f}")
    print(f"witness t={float(t):.3f} kappa={float(kappa):.3f} q={float(q):.3f}")


if __name__ == "__main__":
    main()
