"""Exact rational witness for the post-perimeter two-half-disk scalar system.

This certifies arithmetic compatibility only. It does not construct a source, prove
global optimality, or resolve Target C-II.
"""

from __future__ import annotations

from fractions import Fraction as F


def arctan_bounds(x: F, terms: int = 8) -> tuple[F, F]:
    """Even alternating partial sum and its next-term upper bound."""
    assert terms % 2 == 0 and 0 < x < 1
    lower = sum(((-1) ** i * x ** (2 * i + 1) / (2 * i + 1)
                 for i in range(terms)), F(0))
    return lower, lower + x ** (2 * terms + 1) / (2 * terms + 1)


def main() -> None:
    t = F(21, 10)
    kappa = F(0)
    S = F(14, 5)
    G = F(3, 10)
    mu = S + G
    m = mu - t
    e = 2 * t + kappa - mu
    u = F(1, 10)
    Q = F(1)
    f = F(9, 10)
    T = t + 2 * f

    pi_lo = F(314159, 100000)
    pi_hi = F(314160, 100000)
    sqrt3_lo = F(173205, 100000)
    atan5_lo, atan5_hi = arctan_bounds(F(1, 5))
    atan239_lo, atan239_hi = arctan_bounds(F(1, 239))
    # Machin's identity pi = 16 atan(1/5) - 4 atan(1/239).
    assert pi_lo < 16 * atan5_lo - 4 * atan239_hi
    assert 16 * atan5_hi - 4 * atan239_lo < pi_hi
    assert sqrt3_lo > 0 and sqrt3_lo ** 2 < 3
    assert mu == F(31, 10)
    assert m == F(1)
    assert e == F(11, 10)
    assert Q + u == e - 2 * kappa
    assert T == F(39, 10)
    assert t + kappa == m + e
    assert Q >= f >= 0
    assert u >= 0 and G >= 0 and kappa >= 0
    assert t + kappa < pi_lo
    assert u + mu + kappa > pi_hi

    # Half-disk remainder floor S+G >= pi/sqrt(2): upper-bound the RHS.
    sqrt2_lo = F(141421, 100000)
    assert sqrt2_lo > 0 and sqrt2_lo ** 2 < 2
    assert mu > pi_hi / sqrt2_lo

    # §161 retained remainder, with c_* = pi(2-sqrt(3))/4.
    c_star_hi = pi_hi * (F(2) - sqrt3_lo) / 4
    assert 5 * t > S + 2 * mu + c_star_hi

    # Half-disk stopped-train floor T-q/2 >= 2 sqrt(2 Delta_2)
    # = 2 sqrt(pi/sqrt(3)). Positive squaring and an upper bound certify it.
    train_margin = T - (t + kappa) / 2
    assert train_margin > 0
    assert train_margin ** 2 > 4 * pi_hi / sqrt3_lo

    # Strict stopped-train phase floor 2f-kappa > 2sqrt(Delta_2)-pi/2.
    phase_radical_hi = F(1905, 1000)
    assert phase_radical_hi > 0
    assert phase_radical_hi ** 2 > 2 * pi_hi / sqrt3_lo
    phase_rhs_hi = phase_radical_hi - pi_lo / 2
    assert 2 * f - kappa > phase_rhs_hi

    # New half-disk perimeter-rigidity floor T >= 1+pi/2.
    assert T > F(1) + pi_hi / 2

    # §123 payment and global nonquadrilateral-face constraints.
    assert 4 * f + Q < 10 * (e - kappa)
    assert 2 * f - kappa > F(3338, 10000)

    print("two-half-disk post-perimeter scalar regression: OK")


if __name__ == "__main__":
    main()
