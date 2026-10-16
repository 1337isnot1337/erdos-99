"""Exact rational checks for the post-Section-173 half-disk scalar regression.

This checks only normalized arithmetic.  It does not construct a source, verify
the inherited geometric hypotheses, or prove C-II closure.
"""

from __future__ import annotations

from fractions import Fraction
from math import pi, sqrt


def main() -> None:
    t = Fraction(21, 10)
    kappa = Fraction(0)
    S = Fraction(14, 5)
    G = Fraction(3, 10)
    mu = S + G
    f = Fraction(9, 10)
    T = t + 2 * f
    u = Fraction(1, 10)
    Q = Fraction(1)
    e = Fraction(11, 10)
    q = t + kappa
    a = Fraction(2)

    c_halfdisk = 2.0 * sqrt(pi / sqrt(3.0))
    c_boundary = 2.0 + pi * (4.0 - 2.0 * sqrt(3.0)) / 8.0
    c_detour = pi * (2.0 - sqrt(3.0)) / 2.0
    c161 = pi * (2.0 - sqrt(3.0)) / 4.0
    c163 = 2.0 * sqrt(pi / (2.0 * sqrt(3.0)))

    assert T - q / 2 > Fraction(28, 10)
    assert float(T - q / 2) > c_halfdisk
    assert float(T) > c_boundary
    assert 5.0 * float(t) - 2.0 * float(kappa) > float(S) + 2.0 * float(mu) + c161
    assert 5.0 * float(t) - 2.0 * float(mu) - 2.0 * float(kappa) > c163
    assert float(u + mu + kappa) > pi
    assert 4.0 * float(f) + float(Q) < 10.0 * float(e - kappa)
    assert 2.0 * float(f) - float(kappa) > 0.333829
    assert float(q) < pi

    detour_upper = 10.0 * float(e - kappa) + 2.0 * float(a - S)
    assert detour_upper > c_detour

    assert e == 2 * t + kappa - mu
    assert T == t + 2 * f
    print(f"half_disk_floor={c_halfdisk:.15f}")
    print(f"boundary_floor={c_boundary:.15f}")
    print(f"aggregate_detour_constant={c_detour:.15f}")
    print("post-173 two-half-disk scalar regression: OK")


if __name__ == "__main__":
    main()
