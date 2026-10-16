#!/usr/bin/env python3
"""Exact checks for the global convex-bank defect candidate.

Encoded: every simple tripartite graph with part sizes at most two, retaining
only triangle-free graphs; rational bounds used in the cubic capacity and the
1/26000 aggregate defect floor. No Euclidean source, stress, phase extraction,
bank geometry, asymptotic limit, or global optimality is encoded.
"""

from fractions import Fraction as F
from itertools import combinations, product


def finite_tripartite_check():
    checked = 0
    sharp = 0
    for sizes in product(range(3), repeat=3):
        parts = []
        offset = 0
        for size in sizes:
            parts.append(list(range(offset, offset + size)))
            offset += size
        possible = [
            (x, y)
            for i, j in combinations(range(3), 2)
            for x in parts[i]
            for y in parts[j]
        ]
        for mask in range(1 << len(possible)):
            edges = {
                frozenset(edge)
                for index, edge in enumerate(possible)
                if mask & (1 << index)
            }
            if any(
                frozenset((x, y)) in edges
                and frozenset((y, z)) in edges
                and frozenset((x, z)) in edges
                for x in parts[0]
                for y in parts[1]
                for z in parts[2]
            ):
                continue
            checked += 1
            a, b, c = sizes
            exact_bound = max(a * b + a * c, a * b + b * c, a * c + b * c)
            assert len(edges) <= exact_bound
            maximum = max(sizes)
            assert 3 * len(edges) <= 2 * maximum * sum(sizes)
            if maximum and 3 * len(edges) == 2 * maximum * sum(sizes):
                sharp += 1
    return checked, sharp


def capacity_constants():
    # For 0 <= epsilon <= 1/3:
    # cos(epsilon) >= 1-epsilon^2/2 >= 17/18;
    # 1-cos(epsilon) >= epsilon^2/2-epsilon^4/24
    #                   >= (107/216) epsilon^2.
    assert F(1, 2) - F(1, 9 * 24) == F(107, 216)
    # Put epsilon=gamma/3 and z=gamma^3/66, 0<gamma<=1.
    coefficient = F(2051, 107 * 66) + F(12, 17)
    assert coefficient < 1
    print("cubic capacity rational margin:", 1 - coefficient)


def aggregate_floor():
    # Under u<=1/26000, z,q<=u and gamma=(66z)^(1/3)<=137/1000.
    u = F(1, 26000)
    gamma_upper = F(137, 1000)
    assert gamma_upper**3 > 66 * u
    # Alternating rational arctangent series, with Machin's identity,
    # certifies the pi bounds; the square certificate checks sqrt(3).
    def atan_partial(inverse, terms):
        return sum(
            (F(1 if k % 2 == 0 else -1, (2 * k + 1) * inverse**(2 * k + 1))
             for k in range(terms)),
            F(0),
        )

    pi_lower = 16 * atan_partial(5, 8) - 4 * atan_partial(239, 9)
    pi_upper = 16 * atan_partial(5, 9) - 4 * atan_partial(239, 8)
    assert F(157, 50) < pi_lower < pi_upper < F(22, 7)
    assert F(26, 15)**2 > 3
    rhs_upper = 5 * u + F(13, 45) * (2 * F(22, 7)**2 + 6 * u) * gamma_upper
    lhs_lower = F(157, 200)
    assert rhs_upper < lhs_lower
    print("cube upper certificate margin:", gamma_upper**3 - 66 * u)
    print("aggregate area certificate margin:", lhs_lower - rhs_upper)


def nonclosure_check():
    # The new cubic area inequality alone admits positive defect.
    # q=0,z=1/100 gives gamma^3=33/50, hence gamma>4/5.
    z = F(1, 100)
    assert F(4, 5)**3 < 66 * z
    # sqrt(3)>17/10 and pi>3 give a coarse lower bound on the RHS.
    assert F(17, 10)**2 < 3
    rhs_lower = F(17, 60) * (2 * 3**2 + z) * F(4, 5)
    assert rhs_lower > F(22, 28)
    print("positive-defect scalar compatibility certified (not a source)")


if __name__ == "__main__":
    count, sharp = finite_tripartite_check()
    print(f"triangle-free tripartite graphs checked: {count}; sharp cases: {sharp}")
    capacity_constants()
    aggregate_floor()
    nonclosure_check()
    print("PASS: finite graph checks and rational constants only")
