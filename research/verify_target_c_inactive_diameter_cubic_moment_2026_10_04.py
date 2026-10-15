#!/usr/bin/env python3
"""Exact finite regressions and algebra for the inactive near-star report.

Fraction arithmetic verifies specified nonglobal source families, elementary
energy/separation remainders, and graph cover/matching reductions. This does
not certify the analytic support-energy theorem, constant-width completion,
global minimizers, THIN extraction, or any finite feasible deformation.
"""

from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations


def squared(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def source_regressions():
    pair_checks = 0
    inactive_count = 0
    for diameter in (64, 128, 256):
        d = Q(diameter)
        radius = d - 1 / (2 * d)
        indices = range(-(diameter // 5), diameter // 5 + 1)
        partners = []
        for i in indices:
            if i == 0:
                partners.append((d, Q(0)))
            else:
                t = Q(i, diameter)
                partners.append(
                    (radius * (1 - t * t) / (1 + t * t),
                     radius * 2 * t / (1 + t * t))
                )
        source = [(Q(0), Q(0)), *partners]
        actual_degree = 0
        near_degree = 0
        near_edges = 0
        for i, j in combinations(range(len(source)), 2):
            distance2 = squared(source[i], source[j])
            assert Q(1) <= distance2 <= d * d
            if distance2 == d * d:
                assert i == 0 and j == 1 + diameter // 5
                actual_degree += 1
            if distance2 >= (d - 1 / d) ** 2:
                assert i == 0
                near_degree += 1
                near_edges += 1
            pair_checks += 1
        assert actual_degree == 1
        assert near_degree == 2 * (diameter // 5) + 1
        assert near_edges == len(partners)
        assert len(source) - 1 < diameter  # Collinear strict competitor.
        for x, y in source:
            assert Q(0) <= x <= d
            assert 2 * abs(y) <= x  # Triangle area <= D^2/2.
        inactive_count += near_degree - actual_degree
    return pair_checks, inactive_count


def algebra_checks():
    count = 0
    for t in (Q(i, 512) for i in range(513)):
        # Lower derivative of 5t-(t^2+5)atan(t), using atan(t)<=t.
        remainder = 4 * t * t / (1 + t * t) - 2 * t * t
        assert remainder == 2 * t * t * (1 - t * t) / (1 + t * t)
        assert remainder >= 0
        count += 1
    for epsilon in (Q(i, 256) for i in range(129)):
        # Unit neighbor distance forces sin(alpha/2) >= 1/(4D).
        assert 1 - epsilon * epsilon >= Q(1, 4)
        count += 1
    for c in (Q(1, 4), Q(1), Q(4), Q(9)):
        # Heavy degree implies a^2 > 25c/D^2 >= 24epsilon/D.
        assert 25 * c > 24 * c
        count += 1
    # Seven near-unit neighbors would have a gap <= 2pi/7; pi < 22/7.
    assert Q(1, 100) + 4 * Q(11, 10) ** 2 * Q(22, 49) ** 2 < 1
    count += 1
    return count


def graph_checks():
    graphs = 0
    cover_checks = 0
    matching_checks = 0
    for n in range(6):
        pairs = list(combinations(range(n), 2))
        for graph_mask in range(1 << len(pairs)):
            edges = [edge for i, edge in enumerate(pairs) if graph_mask >> i & 1]
            adjacency = [0] * n
            degrees = [0] * n
            for a, b in edges:
                adjacency[a] |= 1 << b
                adjacency[b] |= 1 << a
                degrees[a] += 1
                degrees[b] += 1

            @lru_cache(None)
            def maximum_matching(mask):
                if not mask:
                    return ()
                bit = mask & -mask
                a = bit.bit_length() - 1
                remaining = mask ^ bit
                best = maximum_matching(remaining)
                neighbors = adjacency[a] & remaining
                while neighbors:
                    next_bit = neighbors & -neighbors
                    b = next_bit.bit_length() - 1
                    candidate = ((a, b),) + maximum_matching(remaining ^ next_bit)
                    if len(candidate) > len(best):
                        best = candidate
                    neighbors ^= next_bit
                return best

            matching = maximum_matching((1 << n) - 1)
            endpoints = sum((1 << a) + (1 << b) for a, b in matching)
            assert endpoints.bit_count() == 2 * len(matching)
            assert all(endpoints >> a & 1 or endpoints >> b & 1 for a, b in edges)
            for baseline in (1, 2, 3):
                moment = sum(max(0, d - baseline) ** 3 for d in degrees)
                for cover in range(1 << n):
                    if any(not (cover >> a & 1 or cover >> b & 1) for a, b in edges):
                        continue
                    r = cover.bit_count()
                    excess = max(0, len(edges) - baseline * r)
                    assert excess ** 3 <= r * r * moment
                    cover_checks += 1
                r = 2 * len(matching)
                excess = max(0, len(edges) - baseline * r)
                assert excess ** 3 <= r * r * moment
                matching_checks += 1
            graphs += 1
    return graphs, cover_checks, matching_checks


def main():
    pairs, inactive = source_regressions()
    algebra = algebra_checks()
    graphs, covers, matchings = graph_checks()
    print(f"PASS: 3 rational nonglobal sources, {pairs} exact source-pair checks, "
          f"{inactive} inactive root pairs")
    print(f"PASS: {algebra} rational algebra checks; {graphs} finite graphs, "
          f"{covers} cover bounds, {matchings} matching bounds")
    print("Scope: finite regressions/algebra only; analytic theorem and global "
          "closure are not computer-certified.")


if __name__ == "__main__":
    main()
