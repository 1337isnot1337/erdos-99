#!/usr/bin/env python3
"""Exact rational full-source ear reflections and lower-bound regressions.

This certifies the specified finite fixtures and every changed pair. It
proves no fixture optimality, universal ear cover, blocker repair, or Level I
conclusion. The analytic theorem is in the accompanying dated report.
"""

from fractions import Fraction as F
from itertools import combinations


def dist2(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


def distances(points):
    return {ij: dist2(points[ij[0]], points[ij[1]])
            for ij in combinations(range(len(points)), 2)}


def contacts(ledger):
    return {ij for ij, d in ledger.items() if d == 1}


def diameter_pairs(ledger):
    maximum = max(ledger.values())
    return {ij for ij, d in ledger.items() if d == maximum}


def reflect(point, a, c):
    # Reflection in the complete chord line, using rational vector projection.
    u = tuple(y - x for x, y in zip(a, c))
    v = tuple(y - x for x, y in zip(a, point))
    coefficient = sum(x * y for x, y in zip(u, v)) / sum(x * x for x in u)
    projection = tuple(x + coefficient * y for x, y in zip(a, u))
    return tuple(2 * x - y for x, y in zip(projection, point))


def fixture(blocker=None, deep_isolate=True):
    r = F(1, 50)
    h = 2 * r / (1 + r * r)
    u = (1 - r * r) / (1 + r * r)
    length = 1 / h
    assert u * u + h * h == 1 and 0 < h < F(1, 8)
    # Counterclockwise hull order; its two outer ears have unit adjacent sides.
    points = [(length + h, F(0)), (length, u), (-length, u),
              (-length - h, F(0)), (-length, -u), (length, -u)]
    if deep_isolate:
        points.append((F(0), F(0)))
    if blocker == "strict":
        points.append((length - 1, F(0)))
    elif blocker == "tie":
        points.append((length - h - 1, F(0)))
    elif blocker is not None:
        raise ValueError("unknown blocker")
    old = distances(points)
    assert min(old.values()) == 1
    assert contacts(old) == {(0, 1), (0, 5), (2, 3), (3, 4)}
    assert diameter_pairs(old) == {(0, 3)}
    reflected = list(points)
    reflected[0] = reflect(points[0], points[5], points[1])
    reflected[3] = reflect(points[3], points[2], points[4])
    assert reflected[0] == (length - h, F(0))
    assert reflected[3] == (-length + h, F(0))
    assert dist2(points[0], points[3]) > (1 + 4 * h) ** 2
    new = distances(reflected)
    assert all(new[ij] <= value for ij, value in old.items())
    assert new[(0, 3)] < old[(0, 3)]
    assert max(new.values()) < max(old.values())
    for ij in contacts(old):
        assert new[ij] == 1
    if blocker is None:
        assert min(new.values()) == 1
        assert contacts(new) == contacts(old)
    else:
        blocker_index = len(points) - 1
        ij = (0, blocker_index)
        assert old[ij] > 1
        assert old[ij] <= (1 + 2 * h) ** 2
        assert all(old[jk] > 1 for jk in old if blocker_index in jk)
        if blocker == "strict":
            assert new[ij] == (1 - h) ** 2 < 1
            assert min(new.values()) < 1
        else:
            assert new[ij] == 1
            assert min(new.values()) == 1
            assert contacts(new) == contacts(old) | {ij}
    print(f"ear-{blocker or 'clear'}: n={len(points)}, pairs={len(old)}; "
          "all upper pairs nonincreasing, old contacts exact, "
          f"lower ledger {'feasible' if min(new.values()) >= 1 else 'blocked'}")
    return len(old)


def square_regression():
    # A familiar no-extra-contact ear still collides after reflection.
    points = [(F(0), F(0)), (F(1), F(0)), (F(1), F(1)), (F(0), F(1))]
    reflected = reflect(points[1], points[0], points[2])
    assert reflected == points[3]
    assert dist2(reflected, points[3]) == 0
    print("square regression: absence of an interior unit port does not imply a feasible ear flip")


def verify_port_order_identity():
    # Rational unit vectors within the inward 60--120 degree sector. Their
    # reversed angular order is the only feasible choice along a unit hull edge.
    r = F(1, 10)
    c = (1 - r * r) / (1 + r * r)
    s = 2 * r / (1 + r * r)
    assert c * c + s * s == 1 and s < F(1, 2)
    clockwise = ((-s, c), (s, c))
    counterclockwise = tuple(reversed(clockwise))
    origin, neighbor = (F(0), F(0)), (F(1), F(0))
    for vectors, feasible in ((clockwise, True), (counterclockwise, False)):
        p = vectors[0]
        q = tuple(a + b for a, b in zip(neighbor, vectors[1]))
        assert dist2(origin, p) == dist2(neighbor, q) == 1
        assert dist2(origin, q) > 1 and dist2(neighbor, p) > 1
        assert (dist2(p, q) >= 1) == feasible
    print("port-order regression: positive inward-port turn violates lower separation")


def octagon_cross_regression():
    # Two nonadjacent selected loaded ears share a retained neighbor. Each
    # single reflection is feasible, but their two reflected positions collide.
    c, s = F(4, 5), F(3, 5)
    edges = ((1, 0), (c, s), (0, 1), (-s, c),
             (-1, 0), (-c, -s), (0, -1), (s, -c))
    points = [(F(0), F(0))]
    for dx, dy in edges[:-1]:
        x, y = points[-1]
        points.append((x + dx, y + dy))
    assert tuple(a + b for a, b in zip(points[-1], edges[-1])) == points[0]
    old = distances(points)
    assert min(old.values()) == 1
    assert contacts(old) == {(i, i + 1) for i in range(7)} | {(0, 7)}
    assert diameter_pairs(old) == {(0, 4), (2, 6)}
    flipped = list(points)
    for i in (0, 2):
        flipped[i] = reflect(points[i], points[(i - 1) % 8], points[(i + 1) % 8])
        assert dist2(points[i], flipped[i]) < 1
        single = list(points)
        single[i] = flipped[i]
        assert min(distances(single).values()) == 1
        assert contacts(distances(single)) == contacts(old)
    new = distances(flipped)
    assert all(new[ij] <= value for ij, value in old.items())
    assert new[(0, 2)] == F(2, 5) < 1
    print("octagon regression: separately feasible loaded-ear flips fail simultaneous lower separation")
    return len(old)


def skew_ear_containment_sweep():
    checked = 0
    for r in (F(1, 50), F(1, 10), F(1, 4)):
        h = 2 * r / (1 + r * r)
        u = (1 - r * r) / (1 + r * r)
        assert 0 < h < F(1, 2)
        for extra in (F(2), F(5), F(20)):
            depth = (1 - 2 * h * h) / (2 * h) + extra
            max_x = (h * (depth + h) - F(1, 2)) / u
            for proportion in (F(-1), F(-1, 2), F(0), F(1, 2), F(1)):
                x = max_x * proportion
                a, b, c, k = (-u, F(0)), (F(0), h), (u, F(0)), (x, -depth)
                points = (a, b, c, k)
                old = distances(points)
                assert min(old.values()) == 1
                assert old[(1, 3)] == max(old.values()) > 4
                reflected = reflect(b, a, c)
                assert reflected == (F(0), -h)
                # Exact membership in triangle a,c,k at depth h.
                assert h <= depth
                assert h * abs(x) <= u * (depth - h)
                new_points = (a, reflected, c, k)
                new = distances(new_points)
                assert all(new[ij] <= value for ij, value in old.items())
                assert min(new.values()) == 1
                checked += 1
    print(f"skew-ear containment: {checked} exact loaded fixtures and all-pair upper checks")
    return 6 * checked


if __name__ == "__main__":
    total = sum(fixture(blocker) for blocker in (None, "strict", "tie"))
    square_regression()
    verify_port_order_identity()
    total += octagon_cross_regression()
    total += skew_ear_containment_sweep()
    print(f"PASS: {total} all-pair reflection checks plus exact square/port-order regressions; "
          "no global minimum or universal cover certified")
