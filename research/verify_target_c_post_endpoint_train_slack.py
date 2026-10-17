#!/usr/bin/env python3
"""Regression checks for the post-endpoint train-slack resolution.

The proof is symbolic.  This script checks the finite identities numerically at high
precision and the component-concentration inequality exactly with Fraction arithmetic.
It deliberately does not claim geometric realizability of the random scalar ledgers.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import random

getcontext().prec = 80
RNG = random.Random(20260914)
TOL = Decimal("1e-65")


def dec_fraction(x: Fraction) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)


def close(a: Decimal, b: Decimal) -> None:
    assert abs(a - b) < TOL, (a, b, a - b)


def check_train_identity(T: int, R: int, U: int, f: int, Q: int) -> None:
    assert T > 0 and 0 < R <= T * T // 4
    assert Q >= f >= 0
    b = 2 * U - Q
    assert b >= 0
    B4 = 2 * T
    capacity = b + 4 * f + Q
    assert B4 <= capacity

    sqrt_r = Decimal(R).sqrt()
    tau = Decimal(U + 2 * f) - 2 * sqrt_r
    rho = Decimal(capacity - B4)
    sigma = Decimal(B4) - 4 * sqrt_r

    assert tau >= 0 and rho >= 0 and sigma >= 0
    close(2 * tau, rho + sigma)

    mantel = Fraction(T * T, 4) - R
    sigma_from_mantel = (
        Decimal(8) * dec_fraction(mantel) / (Decimal(T) + 2 * sqrt_r)
    )
    close(sigma, sigma_from_mantel)

    # Check the refined PE/TS surplus identity against mu*D = U+m_B-2c_I-4.
    p = Decimal(max(0, b - RNG.randint(0, min(b, 7))))
    m_b = RNG.randint(0, 20)
    c_i = RNG.randint(0, 5)
    lhs = Decimal(U + m_b - 2 * c_i - 4)
    rhs = (
        (2 * p + 2 * sqrt_r) / 5
        + Decimal(m_b)
        + Decimal(2) * Decimal(Q - f) / 5
        + Decimal(2) * (Decimal(b) - p) / 5
        + rho / 10
        + sigma / 10
        - Decimal(2 * c_i + 4)
    )
    close(lhs, rhs)


def check_component_inequality(parts: list[int], rhombi: list[int]) -> None:
    assert len(parts) == len(rhombi) and parts
    for t_i, r_i in zip(parts, rhombi):
        assert 0 <= r_i <= t_i * t_i // 4

    T = sum(parts)
    R = sum(rhombi)
    t_max = max(parts)
    M = Fraction(T * T, 4) - R
    lower = Fraction(T * (T - t_max), 4)
    assert M >= lower, (parts, rhombi, M, lower)

    # The outside union has at most T_out^2/4 crossings.
    i_star = max(range(len(parts)), key=parts.__getitem__)
    t_out = T - parts[i_star]
    r_out = R - rhombi[i_star]
    assert r_out <= t_out * t_out // 4


for _ in range(5000):
    T = RNG.randint(2, 250)
    R = RNG.randint(1, max(1, T * T // 4))
    f = RNG.randint(0, T // 3)
    U = T + RNG.randint(0, 40)
    Q = RNG.randint(f, min(2 * U, f + 40))
    check_train_identity(T, R, U, f, Q)

for _ in range(5000):
    count = RNG.randint(1, 12)
    parts = [RNG.randint(1, 80) for _ in range(count)]
    rhombi = [RNG.randint(0, t * t // 4) for t in parts]
    check_component_inequality(parts, rhombi)

print("post-endpoint train-slack regression: PASS")
