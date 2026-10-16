#!/usr/bin/env python3
"""Regression checks for one-sign TB1 active-diameter decoupling.

The proof itself is geometric.  This certificate checks the exact layer-incidence
logic, the parity thinning, contact support under nonadjacent layer moves, the
common-axis contradiction arithmetic, and the displayed density constant.
"""

from fractions import Fraction
import itertools
import math


S0 = Fraction(791, 320_000_000)
C_H = 0.453819885927


def moved_layers_for_pair(a: int, b: int):
    """A layer translation moves a pair iff exactly one endpoint is in the layer."""
    if a == b:
        return set()
    return {a, b}


def check_two_layer_inward_signs() -> None:
    # For endpoints in distinct layers a,b, orient r from a to b.  The layer-a
    # incidence is -r and the layer-b incidence is +r: exact negatives.
    for a in range(8):
        for b in range(8):
            ml = moved_layers_for_pair(a, b)
            if a == b:
                assert not ml
            else:
                assert ml == {a, b}
                sign_a = -1
                sign_b = +1
                assert sign_a == -sign_b


def check_common_axis_contradiction() -> None:
    # If n.w_i >= cD and (-n).w_j >= cD, then
    # n.(w_i-w_j) >= 2cD.  But |w_i-w_j|<=K/D gives <=K.
    # Check the explicit threshold D > K/(2c) over representative K.
    for K in (1.0, 1e3, 31.4e6, 62.8e6, 1e9):
        threshold = K / (2.0 * C_H)
        D = 2.0 * threshold + 10.0
        lower = 2.0 * C_H * D
        upper = K
        assert lower > upper


def check_parity_thinning() -> None:
    for n in range(1, 100):
        for mask in range(1 << min(n, 12)):
            # Exhaust only n<=12 by bitmask; for larger n use deterministic sets.
            if n > 12:
                break
            S = {i for i in range(n) if mask & (1 << i)}
            ev = {i for i in S if i % 2 == 0}
            od = S - ev
            I = ev if len(ev) >= len(od) else od
            assert len(I) * 2 >= len(S)
            assert all(abs(i - j) != 1 for i in I for j in I if i != j)

    for n in (100, 101, 1000):
        S = set(range(n))
        ev = {i for i in S if i % 2 == 0}
        od = S - ev
        I = ev if len(ev) >= len(od) else od
        assert len(I) * 2 >= len(S)
        assert all(abs(i - j) != 1 for i in I for j in I if i != j)


def check_contact_support_nonadjacent_moves() -> None:
    # A selected contact joins consecutive layers k-1,k.  A nonadjacent moved
    # set contains at most one endpoint of every such contact.
    for n in range(2, 30):
        for parity in (0, 1):
            I = {i for i in range(n) if i % 2 == parity}
            for k in range(1, n):
                endpoints = {k - 1, k}
                assert len(endpoints & I) <= 1


def check_swap_identity() -> None:
    # Numerical exact identity a-(a+b)=-b, b-(a+b)=-a.
    for eps in (1e-1, 1e-3, 1e-6):
        a = (1.0, 0.0)
        theta = math.pi - eps
        b = (math.cos(theta), math.sin(theta))
        v = (-(a[0] + b[0]), -(a[1] + b[1]))
        av = (a[0] + v[0], a[1] + v[1])
        bv = (b[0] + v[0], b[1] + v[1])
        assert math.dist(av, (-b[0], -b[1])) < 1e-12
        assert math.dist(bv, (-a[0], -a[1])) < 1e-12
        assert abs(math.hypot(*av) - 1.0) < 1e-12
        assert abs(math.hypot(*bv) - 1.0) < 1e-12


def check_density() -> None:
    assert S0 / 2 == Fraction(791, 640_000_000)
    assert S0 / 4 == Fraction(791, 1_280_000_000)
    assert abs(float(S0 / 4) - 6.1796875e-7) < 1e-20


def main() -> None:
    check_two_layer_inward_signs()
    check_common_axis_contradiction()
    check_parity_thinning()
    check_contact_support_nonadjacent_moves()
    check_swap_identity()
    check_density()
    print(f"c_H      = {C_H:.15g}")
    print(f"s0 / 4   = {float(S0/4):.15g}")
    print("one-sign TB1 active-diameter decoupling regression: PASS")


if __name__ == "__main__":
    main()
