#!/usr/bin/env python3
"""Exact regression certificates for finite diameter rotation barriers.

Encodes actual unit-separated planar sources, all old/new pair constraints,
an actual three-diameter cut, and exact contact-preserving rotation endpoints.
Also checks equality sources for the vertex-disjoint diameter-angle bound.
Uses Fraction only. Does not encode global optimality, positive full KKT,
canonical O--O trains, or a linear complete transverse shore. The rotation
sources have explicit smaller square-grid competitors.
"""

from fractions import Fraction as F
from itertools import combinations
from math import isqrt


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def dot(p, q):
    return p[0] * q[0] + p[1] * q[1]


def norm(p):
    return dot(p, p)


def distances(points):
    return {(i, j): norm(sub(points[i], points[j]))
            for i, j in combinations(range(len(points)), 2)}


def contacts(ds):
    return {e for e, d in ds.items() if d == 1}


def triangle_free(edges, count):
    return not any({(i, j), (i, k), (j, k)} <= edges
                   for i, j, k in combinations(range(count), 3))


def rotation_packet(n):
    """An actual m=1 cut with three moving endpoints and no source isolates."""
    d = F(n)
    t = F(1, 2 * n - 1)
    cp, sp = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
    b = d * cp, d * sp
    c = d * cp, -d * sp
    u = F(1), F(0)
    source = [(F(k), F(0)) for k in range(n)]
    source += [(d, F(0)), b, c, sub(b, u), sub(c, u)]
    moving = {n, n + 1, n + 2}
    wx, wy = sub(b, u)
    denominator = wx * wx + wy * wy
    v = ((wx * wx - wy * wy) / denominator,
         2 * wx * wy / denominator)
    delta = sub(v, u)
    endpoint = [add(p, delta) if i in moving else p
                for i, p in enumerate(source)]
    old, new = distances(source), distances(endpoint)
    assert min(old.values()) == min(new.values()) == 1
    assert max(old.values()) == max(new.values()) == d * d
    old_c = contacts(old)
    assert old_c == contacts(new)
    assert len(old_c) == n + 2
    assert triangle_free(old_c, len(source))
    assert {i for e in old_c for i in e} == set(range(len(source)))
    old_h = {e for e, s in old.items() if s == d * d}
    new_h = {e for e, s in new.items() if s == d * d}
    assert old_h == {(0, n), (0, n + 1), (0, n + 2)}
    assert new_h == {(0, n + 1)}
    crossing_contacts = {e for e in old_c if len(set(e) & moving) == 1}
    assert crossing_contacts == {(n - 1, n), (n + 1, n + 3),
                                  (n + 2, n + 4)}
    for i, j in crossing_contacts:
        if i not in moving:
            i, j = j, i
        assert sub(source[i], source[j]) == u
        assert sub(endpoint[i], endpoint[j]) == v

    # Every unselected source pair is checked, including the narrow old lower
    # slacks between the fixed dimer partners and the end of the long chain.
    assert d * d - new[(0, n)] > 0
    assert d * d - new[(0, n + 2)] > 0
    assert norm(v) == 1

    # The angular boundary has tan(theta/2)=wy/wx. Check both sides exactly.
    threshold = wy / wx
    for multiple, sign in [(F(1, 2), 1), (F(1), 0), (F(3, 2), -1)]:
        q = multiple * threshold
        test_v = ((1 - q * q) / (1 + q * q), 2 * q / (1 + q * q))
        gain = norm(add(b, sub(test_v, u))) - d * d
        assert (gain > 0) - (gain < 0) == sign

    # Actual cardinality-preserving strict diameter competitor; no appeal to
    # asymptotic density or an independently chosen unknown optimum.
    count = len(source)
    side = isqrt(count)
    if side * side < count:
        side += 1
    grid = [(F(i), F(j)) for i in range(side) for j in range(side)][:count]
    gd = distances(grid)
    assert min(gd.values()) >= 1
    assert max(gd.values()) <= 2 * (side - 1) ** 2 < d * d
    return len(old) + len(new) + len(gd), len(crossing_contacts)


def disjoint_lens_equality(k):
    s = F(2 * k, k * k + 1)
    h = F(k * k - 1, k * k + 1)
    d = F(1, 2) / s
    points = [(F(0), F(0)), (d, F(0)), (s, h), (d - s, h)]
    ds = distances(points)
    assert min(ds.values()) == 1
    assert max(ds.values()) == d * d
    assert {e for e, value in ds.items() if value == d * d} == {
        (0, 1), (0, 3), (1, 2)}
    assert triangle_free(contacts(ds), len(points))
    r, rr = sub(points[3], points[0]), sub(points[1], points[2])
    # cos(phi)=2(1-1/(2D^2))^2-1 is equivalent to
    # phi=4 asin(1/(2D)); the selected bars are vertex-disjoint.
    assert dot(r, rr) / (d * d) == 2 * (1 - F(1, 2) / (d * d)) ** 2 - 1
    assert ds[(0, 2)] == ds[(1, 3)] == 1
    return len(ds)


def strict_cross_pair_packet(k):
    """Both O(1/D)-near cross pairs are strict, with squared deficit one."""
    d = F(k * k + 1, 2 * k)
    length = F(k * k - 1, 2 * k)
    points = [(F(0), F(0)), (length, F(0)),
              (F(0), F(1)), (length, F(1))]
    ds = distances(points)
    assert min(ds.values()) == 1
    assert max(ds.values()) == d * d
    assert {e for e, value in ds.items() if value == d * d} == {(0, 3), (1, 2)}
    assert d * d - ds[(0, 1)] == d * d - ds[(2, 3)] == 1
    assert triangle_free(contacts(ds), len(points))
    # In the centered lens coordinates, b=1 and z=0. The deficit sum
    # is two and the two strict pairs cannot be made exact by a label change.
    assert 2 * d * d - ds[(0, 1)] - ds[(2, 3)] == 2
    return len(ds)


def main():
    checks = cut_contacts = 0
    for n in [10, 16, 32, 64, 128]:
        checked, cut = rotation_packet(n)
        checks += checked
        cut_contacts += cut
    lens_checks = sum(disjoint_lens_equality(k) for k in [9, 17, 33, 65, 129])
    strict_checks = sum(strict_cross_pair_packet(k) for k in [9, 17, 33, 65, 129])
    print(f"PASS: 5 actual rotation packets; {checks} full-source/competitor "
          f"pair checks; {cut_contacts} preserved cut contacts")
    print(f"PASS: 5 disjoint-lens equality packets; {lens_checks} exact pair checks")
    print(f"PASS: 5 strict-cross-pair packets; {strict_checks} exact pair checks; "
          "both near-diameter squared deficits exactly one")
    print("SCOPE: regression/identity certificates only; no global-minimizer "
          "or complete-train closure certificate")


if __name__ == "__main__":
    main()
