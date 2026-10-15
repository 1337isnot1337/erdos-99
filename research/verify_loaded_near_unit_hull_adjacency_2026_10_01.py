#!/usr/bin/env python3
"""Exact geometry certificates for loaded short-pair hull adjacency.

Encodes unit-separated sources, all actual diameter endpoints, convex hull
order, the exact cap-threshold polynomial, and short-pair adjacency. Rational
stars, antipodal matchings, and Q(sqrt(3)) odd-cycle-plus-leaf packets are used.
The two-leaf corner family certifies asymptotic sharpness of sqrt(3).

No positive KKT, stopped-train, near-disk sequence, global-optimality, or Level I
certificate is asserted. Universal conclusions have proofs in the report.
"""

from fractions import Fraction as F
from itertools import combinations
from random import Random

from verify_ultrasmall_swap_isolate_dispatch_2026_10_01 import Q3, cross, distance2


def unit(t):
    return ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


def hull_order(points):
    ordered = sorted(set(points))
    halves = []
    for order in (ordered, ordered[::-1]):
        half = []
        for p in order:
            while len(half) >= 2 and cross(half[-2], half[-1], p) <= 0:
                half.pop()
            half.append(p)
        halves.append(half[:-1])
    return halves[0] + halves[1]


def packet(points):
    lengths = {ij: distance2(points[ij[0]], points[ij[1]])
               for ij in combinations(range(len(points)), 2)}
    assert min(lengths.values()) >= 1
    diameter_value = max(lengths.values())
    diameter2 = diameter_value
    if isinstance(diameter2, Q3):
        assert not diameter2.b
        diameter2 = diameter2.a
    assert diameter2 >= 36
    actual = {ij for ij, value in lengths.items() if value == diameter_value}
    loaded = {v for ij in actual for v in ij}
    index = {p: i for i, p in enumerate(points)}
    order = [index[p] for p in hull_order([points[i] for i in loaded])]
    assert set(order) == loaded and len(order) >= 3
    neighbors = {frozenset((order[i], order[(i + 1) % len(order)]))
                 for i in range(len(order))}
    short = nonadjacent = 0
    for i, j in combinations(loaded, 2):
        value = lengths[min(i, j), max(i, j)]
        if value <= F(13, 12) ** 2:
            assert frozenset((i, j)) in neighbors
            short += 1
        if frozenset((i, j)) not in neighbors and value < diameter2:
            # Exact elimination of the positive square root in
            # (1+1/D^2) ell^2 + 2 ell/D >= 3.
            remainder = 3 - (1 + 1 / diameter2) * value
            if remainder > 0:
                assert value * (4 / diameter2) >= remainder ** 2
            nonadjacent += 1
    return short, nonadjacent


def two_leaf_corner(d):
    t = (1 + F(1, 4 * d * d)) / (2 * d)
    cosine, sine = unit(t)
    c = (Q3(), Q3())
    x = (Q3(F(d)), Q3())
    y = (Q3(F(d, 2)), Q3(F(0), F(d, 2)))
    p = (Q3(d * (1 - cosine)), Q3(d * sine))
    q = (Q3(d * (1 - cosine) / 2, d * sine / 2),
         Q3(-d * sine / 2, d * (1 - cosine) / 2))
    points = [c, x, y, p, q]
    lengths = {ij: distance2(points[ij[0]], points[ij[1]])
               for ij in combinations(range(5), 2)}
    assert min(lengths.values()) > 1
    assert max(lengths.values()) == Q3(F(d * d))
    actual = {ij for ij, value in lengths.items() if value == Q3(F(d * d))}
    assert actual == {(0, 1), (0, 2), (1, 2), (1, 3), (2, 4)}
    assert 1 < lengths[3, 4] < 3
    assert lengths[0, 3] == lengths[0, 4]
    assert lengths[3, 4] == Q3(d * d * ((1 - cosine) ** 2 + 3 * sine ** 2),
                              -2 * d * d * (1 - cosine) * sine)
    assert lengths[0, 3] == Q3(4 * d * d * t * t / (1 + t * t))
    short, nonadjacent = packet(points)
    assert nonadjacent > 0
    return short, nonadjacent


def regressions():
    # Removing both loaded-endpoint hypotheses makes hull adjacency false.
    points = [(F(0), F(0)), (F(4), F(0)), (F(4), F(4)), (F(0), F(4)),
              (F(3, 2), F(2)), (F(251, 100), F(2))]
    assert min(distance2(p, q) for p, q in combinations(points, 2)) > 1
    assert distance2(points[-2], points[-1]) == F(101, 100) ** 2
    assert points[-2] not in hull_order(points) and points[-1] not in hull_order(points)
    # The same pairs can be put in a source with D>=6; they stay unloaded.
    points[:4] = [(F(0), F(0)), (F(5), F(0)), (F(5), F(5)), (F(0), F(5))]
    assert max(distance2(p, q) for p, q in combinations(points, 2)) == 50
    packet(points)


def main():
    rng = Random(991002)
    packets = short = nonadjacent = 0
    regressions()
    for _ in range(800):
        d = F(rng.randrange(6, 40))
        points = [(F(0), F(0))]
        for _ in range(100):
            u = unit(F(rng.randrange(0, 501), 1000))
            p = (d * u[0], d * u[1])
            if all(distance2(p, q) >= 1 for q in points):
                points.append(p)
            if len(points) >= 10:
                break
        if len(points) >= 4:
            a, b = packet(points)
            packets += 1
            short += a
            nonadjacent += b
    for _ in range(800):
        radius = F(rng.randrange(3, 20))
        points = []
        for _ in range(100):
            u = unit(F(rng.randrange(-1000, 1001), 500))
            p = (radius * u[0], radius * u[1])
            antipode = (-p[0], -p[1])
            if all(distance2(a, q) >= 1 for a in (p, antipode) for q in points):
                points.extend([p, antipode])
            if len(points) >= 10:
                break
        if len(points) >= 4:
            a, b = packet(points)
            packets += 1
            short += a
            nonadjacent += b
    for d in (6, 7, 10, 20, 100, 1000, 10000):
        a, b = two_leaf_corner(d)
        packets += 1
        short += a
        nonadjacent += b
    assert short > 0 and nonadjacent > 0
    print(f"PASS: {packets} rational/quadratic-field loaded hull packets")
    print(f"PASS: {short} loaded pairs at length <=13/12 are hull sides; "
          f"{nonadjacent} nonadjacent loaded pairs satisfy the exact cap polynomial")
    print("PASS: seven odd-cycle/two-leaf corner packets below sqrt(3), with exact asymptotic formula")
    print("PASS: unloaded near-unit interior-pair regression")
    print("Scope: exact finite source geometry; no KKT, train, asymptotic, or global-optimality certificate")


if __name__ == "__main__":
    main()
