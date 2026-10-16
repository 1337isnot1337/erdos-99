"""Retained arithmetic provenance for the retracted post-fan regression.

The regression depended on a retracted fan density normalization. It certifies only
the displayed rational arithmetic, not a fan floor, a source, or global optimality.
"""

from fractions import Fraction as F


def main() -> None:
    t = F(13, 5)
    kappa = F(0)
    S = F(3)
    G = F(1, 2)
    mu = S + G
    m = mu - t
    e = 2 * t + kappa - mu
    u = F(1)
    Q = F(7, 10)
    f = F(7, 10)
    T = t + 2 * f
    q = t + kappa

    pi_lo = F(314159, 100000)
    pi_hi = F(314160, 100000)
    sqrt3_lo = F(173205, 100000)
    delta_hi = pi_hi / (2 * sqrt3_lo)

    assert mu == F(7, 2)
    assert m == F(9, 10)
    assert e == F(17, 10)
    assert Q == e - u
    assert T == F(4)
    assert q == t == F(13, 5)
    assert Q >= f >= 0
    assert u >= 0 and G >= 0 and kappa >= 0
    assert q < pi_lo
    assert Q < 2 * t - pi_hi

    # Two-half-disk remainder and train floors.
    sqrt2_lo = F(141421, 100000)
    assert mu > pi_hi / (2 * sqrt2_lo)
    assert T - q / 2 > F(2693, 1000)
    assert T > 1 + pi_hi / 2

    # Fan pair budget after Jensen: 20f <= T^2 - 2 Delta_2 asymptotically.
    assert T * T - 20 * f - 2 * delta_hi > 0

    # §161 and the retained §163 moment checks.
    c_star_hi = pi_hi * (2 - sqrt3_lo) / 4
    c_163_hi = F(191, 100)
    assert 5 * t > S + 2 * mu + c_star_hi
    assert 5 * t - 2 * mu > c_163_hi

    # §172 sign and §123 payment.
    assert u + mu > pi_hi
    assert 4 * f + Q < 10 * e

    print("post-fan/train/hull scalar arithmetic provenance: OK; fan claim retracted")


if __name__ == "__main__":
    main()
