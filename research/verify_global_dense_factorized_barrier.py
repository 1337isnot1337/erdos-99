#!/usr/bin/env python3
"""Exact finite near-dense fixtures; the report proves the unbounded construction."""

if not __debug__:
    raise RuntimeError("Certificate assertions are required; run Python without -O.")

from fractions import Fraction as F
from itertools import combinations
from math import ceil

from global_factorized_graph_alternative import graph_alternative


def sign3(a, b):
    """Sign of a+b*sqrt(3), with a,b rational."""
    if not b:
        return (a > 0) - (a < 0)
    if not a:
        return (b > 0) - (b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    delta = a * a - 3 * b * b
    return 0 if not delta else (1 if a > 0 else -1) * (1 if delta > 0 else -1)


def norm(a, b):
    return a * a + a * b + b * b


def q_distance(point, shift, scale, q, alpha=F(1)):
    a, b = point[0] + shift[0], point[1] + shift[1]
    x = scale * (a + b / 2) - q[0]
    return alpha * alpha * x * x + 3 * scale * scale * b * b / 4 + q[1] * q[1], -scale * b * q[1]


def pi_upper():
    # Machin identity pi=16*atan(1/5)-4*atan(1/239), alternating-series bounds.
    def atan_bounds(x, terms):
        partial = sum((-1) ** k * x ** (2 * k + 1) / (2 * k + 1) for k in range(terms))
        next_partial = partial + (-1) ** terms * x ** (2 * terms + 1) / (2 * terms + 1)
        return min(partial, next_partial), max(partial, next_partial)
    lo5, hi5 = atan_bounds(F(1, 5), 12)
    lo239, hi239 = atan_bounds(F(1, 239), 4)
    return 16 * hi5 - 4 * lo239


def verify(m, delta, shift):
    diameter_squared = m * m + 1
    radius = F(m, 2) + delta
    bound = ceil(2 * radius) + 2
    points = [(i, j) for i in range(-bound, bound + 1) for j in range(-bound, bound + 1)
              if norm(F(i) + shift[0], F(j) + shift[1]) < radius * radius]
    boundary = [p for p in points if norm(F(p[0]) + shift[0], F(p[1]) + shift[1]) >=
                (F(m, 2) - delta) ** 2]
    # Every possible diameter conflict has both ends in this exact boundary band.
    conflicts = [(a, b) for a, b in combinations(boundary, 2)
                 if norm(a[0] - b[0], a[1] - b[1]) >= diameter_squared]
    graph = {}
    for a, b in conflicts:
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    deleted = set()
    while graph:
        v = max(graph, key=lambda z: len(graph[z]))
        deleted.add(v)
        for u in graph[v]:
            graph[u].remove(v)
            if not graph[u]:
                del graph[u]
        del graph[v]
    assert all(a in deleted or b in deleted for a, b in conflicts)
    packet = [p for p in points if p not in deleted]
    scale = 1 + F(1, m ** 4)
    assert scale > 1 and scale * scale * m * m < diameter_squared
    quartet = [(F(-m, 2), F(-1, 2)), (F(-m, 2), F(1, 2)),
               (F(m, 2), F(-1, 2)), (F(m, 2), F(1, 2))]
    bad = set()
    for p in packet:
        for q in quartet:
            a, b = q_distance(p, shift, scale, q)
            if sign3(a - 1, b) <= 0 or sign3(a - diameter_squared, b) >= 0:
                bad.add(p)
    for p in packet:
        if len(bad) >= 4:
            break
        bad.add(p)
    interior = [p for p in packet if p not in bad]
    count = len(interior) + 4
    assert count <= len(packet)
    # All packet lower pairs follow from scale>1 and nonzero integral lattice norm.
    # All packet upper pairs follow from the certified conflict cover and norm<=m^2.
    # Explicitly check every quartet/interior lower and upper pair.
    for p in interior:
        for q in quartet:
            a, b = q_distance(p, shift, scale, q)
            assert sign3(a - 1, b) > 0
            assert sign3(a - diameter_squared, b) < 0
    c, h = [], []
    for i, j in combinations(range(4), 2):
        d = sum((quartet[i][axis] - quartet[j][axis]) ** 2 for axis in (0, 1))
        assert 1 <= d <= diameter_squared
        if d == 1:
            c.append((i, j))
        if d == diameter_squared:
            h.append((i, j))
    assert c == [(0, 1), (2, 3)] and h == [(0, 3), (1, 2)]
    # All other labels are actual contact isolates, retained in this graph input.
    cert = graph_alternative(count, c, h)
    assert cert["kind"] == "factorized_barrier"
    # A single affine contraction retains all labels and strictly shortens diameter.
    alpha = 1 - F(1, m ** 8)
    assert scale * scale - (1 - alpha * alpha) * diameter_squared > 1
    direct_pairs = 0
    if m == 32:
        # Independent bounded crosscheck of the optimized conflict-band cover.
        # Clear all denominators and inspect every retained packet pair, without
        # the boundary-band reduction or the global lower-margin estimate.
        scale_num, scale_den = m ** 4 + 1, m ** 4
        alpha_num, alpha_den = m ** 8 - 1, m ** 8
        denominator = 4 * scale_den ** 2 * alpha_den ** 2
        for p, q in combinations(interior, 2):
            a, b = p[0] - q[0], p[1] - q[1]
            unscaled = norm(a, b)
            assert 1 <= unscaled <= m * m
            numerator = scale_num ** 2 * (
                alpha_num ** 2 * (2 * a + b) ** 2 +
                3 * alpha_den ** 2 * b * b)
            assert denominator < numerator < diameter_squared * denominator
            direct_pairs += 1
    for p in interior:
        for q in quartet:
            a, b = q_distance(p, shift, scale, q, alpha)
            assert sign3(a - 1, b) > 0
    for i, j in combinations(range(4), 2):
        d = alpha * alpha * (quartet[i][0] - quartet[j][0]) ** 2 + (
            quartet[i][1] - quartet[j][1]) ** 2
        assert 1 <= d < diameter_squared
    # Rigorous population comparison, including a rational upper bound on kappa0.
    sqrt3_lower = F(989, 571)
    assert sqrt3_lower * sqrt3_lower < 3
    upper_pi = pi_upper()
    assert upper_pi < F(355, 113)
    assert 243 * upper_pi ** 3 / (16000 * sqrt3_lower) < F(13, 20) ** 3
    cube_root_upper = 1
    while cube_root_upper ** 3 <= diameter_squared:
        cube_root_upper += 1
    baseline_upper = upper_pi * diameter_squared / (2 * sqrt3_lower)
    reserve_lower = count - 1 - baseline_upper
    assert reserve_lower > F(13, 20) * cube_root_upper
    return {"M": m, "source_labels": count, "packet_labels": len(packet),
            "packet_diameter_cover": len(deleted), "quartet_deletions": len(bad),
            "all_source_pairs": count * (count - 1) // 2,
            "direct_packet_pair_crosscheck": direct_pairs,
            "explicit_quartet_pairs_per_placement": 4 * len(interior) + 6,
            "reserve_lower": float(reserve_lower),
            "kappa0_D_two_thirds_upper": float(F(13, 20) * cube_root_upper)}


def main():
    parameters = [(32, F(3, 10), (F(5, 6), F(5, 6))),
                  (64, F(3, 10), (F(1, 2), F(5, 6))),
                  (96, F(1, 4), (F(2, 3), F(0))),
                  (128, F(1, 4), (F(1, 2), F(1, 3)))]
    for args in parameters:
        print("PASS:", verify(*args), flush=True)
    print("Scope: exact finite full-source distance certificates; the unbounded "
          "population construction is analytic. These sources fail KKT and are nonglobal.")


if __name__ == "__main__":
    main()
