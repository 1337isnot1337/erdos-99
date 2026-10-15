#!/usr/bin/env python3
"""Exact relative-chord checks on the canonical nonglobal bent-grid family.

Checks coherent unit increments, a uniformly conditioned basis, all boundary
pair lower bounds, short-chord index bounds, and angular sine bounds over
Q(sqrt(3)). Does not prove the general normal-count theorem, actual loading,
canonical chart coverage, global optimality, C-II, or Level I.
"""

from fractions import Fraction as F
from itertools import combinations
import json

from verify_target_c_bent_grid_transport_2026_10_05 import (
    add, mul, neg, scale, sign, squared_distance,
)


ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def subtract(a, b):
    return add(a, neg(b))


def norm2(vector):
    return add(mul(vector[0], vector[0]), mul(vector[1], vector[1]))


def dot(a, b):
    return add(mul(a[0], b[0]), mul(a[1], b[1]))


def det(a, b):
    return subtract(mul(a[0], b[1]), mul(a[1], b[0]))


def fixture(m, short_length=F(4)):
    assert m >= 8 and m % 2 == 0
    eta = F(1, m)
    # K=2 and eta < 1/(2 sqrt(2) K), checked without irrational division.
    assert 8 * 4 * eta ** 2 < 1
    t = F(1, m)
    c, s = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
    v = ((c / 2, -s / 2), (s / 2, c / 2))
    assert norm2(v) == ONE
    # ||[u v]^-1||_F^2 = 2/v_y^2 < 4, hence the operator norm is < K.
    assert sign(subtract(mul(v[1], v[1]), (F(1, 2), F(0)))) > 0
    prefix = [(F(0), F(0))]
    for i in range(m):
        t = F(i, 2 * m * m)
        ux, uy = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
        assert ux * ux + uy * uy == 1
        assert (ux - 1) ** 2 + uy ** 2 < eta ** 2
        prefix.append((prefix[-1][0] + ux, prefix[-1][1] + uy))
    indices = [
        (i, j) for i in range(m + 1) for j in range(m + 1)
        if i in (0, m) or j in (0, m)
    ]
    points = {
        (i, j): (
            add((prefix[i][0], F(0)), scale(v[0], F(j))),
            add((prefix[i][1], F(0)), scale(v[1], F(j))),
        )
        for i, j in indices
    }
    bow = prefix[m][1] / 2 - prefix[m // 2][1]
    assert bow >= F(1, 8) - F(1, 4 * m * m) > F(1, 10)
    checked = short_checked = contacts = 0
    for first, second in combinations(indices, 2):
        i, j = first
        k, l = second
        p, q = points[first], points[second]
        r = tuple(subtract(a, b) for a, b in zip(p, q))
        r2 = squared_distance(p, q)
        assert sign(subtract(r2, ONE)) >= 0
        contacts += r2 == ONE
        zi, zj = i - k, j - l
        z2 = F(zi * zi + zj * zj)
        assert z2 > 0
        lattice_vector = (add((F(zi), F(0)), scale(v[0], F(zj))),
                          scale(v[1], F(zj)))
        error = tuple(subtract(a, b) for a, b in zip(r, lattice_vector))
        expected_error = ((prefix[i][0] - prefix[k][0] - zi, F(0)),
                          (prefix[i][1] - prefix[k][1], F(0)))
        assert error == expected_error
        e2 = norm2(error)
        assert sign(subtract((eta ** 2 * (abs(zi) + abs(zj)) ** 2, F(0)), e2)) >= 0
        assert sign(subtract(scale(r2, F(16)), (z2, F(0)))) > 0
        assert sign(subtract(scale(r2, 32 * eta ** 2), e2)) >= 0
        assert sign(dot(r, lattice_vector)) > 0
        sine_numerator = mul(det(r, lattice_vector), det(r, lattice_vector))
        sine_bound = scale(mul(r2, norm2(lattice_vector)), 32 * eta ** 2)
        assert sign(subtract(sine_bound, sine_numerator)) >= 0
        if sign(subtract((short_length ** 2, F(0)), r2)) >= 0:
            assert z2 < 16 * short_length ** 2
            assert abs(zi) <= 4 * short_length
            assert abs(zj) <= 4 * short_length
            short_checked += 1
        checked += 1
    assert contacts == 4 * m
    return {
        "M": m,
        "boundary_points": len(indices),
        "pair_checks": checked,
        "short_chords": short_checked,
        "exact_bow_greater_than": "1/10",
        "increment_error_bound": str(eta),
    }


if __name__ == "__main__":
    fixtures = [fixture(m) for m in (8, 12, 16)]
    print(json.dumps({
        "status": "PASS",
        "arithmetic": "Q(sqrt(3)), exact rational coefficients",
        "scope": "nonglobal bent-grid boundary fixtures; no canonical coverage",
        "total_pair_checks": sum(item["pair_checks"] for item in fixtures),
        "fixtures": fixtures,
    }, indent=2))
