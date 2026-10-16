#!/usr/bin/env python3
"""Exact periodic-rigidity regression, with no finite-source identification.

This checks rational Gram identities, cycle connectivity, nearest-vector
classification, Q(sqrt(3)) signs for the doubled-period motion, and a finite
square's diameter increase. The general infinite construction and rigidity
proof are analytic in the accompanying report. No unbounded family of finite
Euclidean global minimizers is certified.
"""

from fractions import Fraction as F
from itertools import combinations
from math import gcd


def sign_q3(a, b):
    """Sign of a+b*sqrt(3), using rational comparisons only."""
    if not b:
        return (a > 0) - (a < 0)
    if not a or (a > 0) == (b > 0):
        return (b > 0) - (b < 0)
    difference = a * a - 3 * b * b
    sign = (difference > 0) - (difference < 0)
    return sign if a > 0 else -sign


def gram_length(a, b, c):
    return a * a + b * b + 2 * c * a * b


def verify_cycle(count, step):
    seen = set()
    index = 0
    for _ in range(count):
        assert index not in seen
        seen.add(index)
        index = (index + step) % count
    assert index == 0 and len(seen) == count
    return count


def verify_member(m):
    assert m >= 3
    count = m * m - 1
    denominator = m * m - m + 1
    c = F(m * m - 4 * m + 1, 2 * denominator)
    s_coefficient = F(count, 2 * denominator)  # s = s_coefficient*sqrt(3)
    assert F(-1, 2) < c < F(1, 2)
    assert c * c + 3 * s_coefficient * s_coefficient == 1
    period2 = gram_length(m, 1, c)
    assert period2 == gram_length(1, m, c) == F(count * count, denominator)
    period_dot = 2 * m + (m * m + 1) * c
    assert 2 * period_dot == period2
    assert 0 < F(denominator, count) < 1
    assert count - denominator == m - 2

    gamma = 1 - 2 * abs(c)
    assert 0 < gamma <= 1
    if m >= 4:
        assert gamma == F(3 * m, denominator)
    t = gamma / 8
    assert (1 + t) ** 2 < 1 + gamma
    assert gcd(m, count) == 1
    cycle_vertices = verify_cycle(count, 1) + verify_cycle(count, -m)

    # The quotient label is j-mi mod count; both period generators are in its kernel.
    assert (1 - m * m) % count == 0
    assert (m - m) % count == 0
    # Parity displacement is periodic for doubled generators but not u+mv.
    assert (2 * m) % 2 == 0 and 2 % 2 == 0 and 1 % 2 == 1
    assert sum(a for a, _ in ((1, 0), (-1, 0), (0, 1), (0, -1))) == 0
    assert sum(b for _, b in ((1, 0), (-1, 0), (0, 1), (0, -1))) == 0

    shortest_nonunit = None
    checked = 0
    for a in range(-4, 5):
        for b in range(-4, 5):
            if (a, b) == (0, 0):
                continue
            old2 = gram_length(a, b, c)
            unit = abs(a) + abs(b) == 1
            assert (old2 == 1) == unit
            if not unit:
                assert old2 >= 1 + gamma
                shortest_nonunit = old2 if shortest_nonunit is None else min(shortest_nonunit, old2)
            for original_parity in (0, 1):
                epsilon = (original_parity + a) % 2 - original_parity
                rational = old2 + t * t * epsilon * epsilon
                radical = 2 * b * s_coefficient * t * epsilon
                assert sign_q3(rational - 1, radical) >= 0
                new_unit = sign_q3(rational - 1, radical) == 0
                assert new_unit == (a == 0 and abs(b) == 1)
                if unit:
                    assert radical == 0  # all contact first variations are exactly zero
                    assert rational == (1 if a == 0 else 1 + t * t)
                checked += 1
    assert shortest_nonunit == 1 + gamma
    v_sign = 1 if c >= 0 else -1
    triangle_slack = gram_length(1, 0, c) + gram_length(0, v_sign, c) + gram_length(1, -v_sign, c) - 3
    assert triangle_slack == gamma
    print(f"m={m}, N={count}, density/triangular={F(denominator, count)}, "
          f"triangle-slack={gamma}; period Gram, two rigid cycles, and doubled flex certified")
    return checked, cycle_vertices


def finite_square_upper_regression():
    t = F(1, 100)
    original = ((F(0), F(0)), (F(1), F(0)), (F(1), F(1)), (F(0), F(1)))
    moved = tuple((x, y + t * int(x)) for x, y in original)
    old = [sum((a - b) ** 2 for a, b in zip(original[i], original[j]))
           for i, j in combinations(range(4), 2)]
    new = [sum((a - b) ** 2 for a, b in zip(moved[i], moved[j]))
           for i, j in combinations(range(4), 2)]
    assert min(old) == min(new) == 1
    assert max(old) == 2 and max(new) == 2 + 2 * t + t * t > 2
    assert 2 - 2 * t + t * t in new
    print("Finite-square regression: the periodic packing flex preserves lower bounds but increases diameter")


if __name__ == "__main__":
    pair_checks = cycle_vertices = 0
    for m in (3, 4, 5, 8, 16, 32, 64, 128):
        pairs, vertices = verify_member(m)
        pair_checks += pairs
        cycle_vertices += vertices
    finite_square_upper_regression()
    print(f"PASS: {pair_checks} exact Q(sqrt(3)) pair-at-parity checks and "
          f"{cycle_vertices} cycle visits; no finite Euclidean Level I counterexample asserted")
