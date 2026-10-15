#!/usr/bin/env python3
"""Exact finite regressions for the source-wide cubic diameter-star report.

Encoded: explicit rational unit-separated diameter stars; exact squared radical
identities/inequalities for rational samples of the constant-width regression;
degree-packet Holder inequalities on all labelled graphs with <=5 vertices.
Omitted: arbitrary completion/support geometry, dense-source extraction, KKT,
asymptotic quantifiers, and global optimality. General proofs are in the report.
This is a finite certificate, not a test establishing the general theorem.
"""

from fractions import Fraction as F
from itertools import combinations


def squared_distance(p, q):
    return sum((x - y) ** 2 for x, y in zip(p, q))


def check_rational_stars():
    pair_count = 0
    partner_count = 0
    for size in (4, 8, 12, 16):
        diameter = size**3
        limit = size**2 // 4
        points = [(F(0), F(0))]
        for index in range(-limit, limit + 1):
            param = F(index, diameter)
            denom = 1 + param**2
            point = (
                diameter * (param**2 - 1) / denom,
                -2 * diameter * param / denom,
            )
            assert squared_distance(point, points[0]) == diameter**2
            assert 2 * abs(param) / denom < F(1, size)
            points.append(point)
        partner_count += len(points) - 1
        actual_diameter_edges = []
        for i, j in combinations(range(len(points)), 2):
            dist = squared_distance(points[i], points[j])
            assert 1 < dist <= diameter**2
            if dist == diameter**2:
                actual_diameter_edges.append((i, j))
            if i > 0:
                ti = F(i - 1 - limit, diameter)
                tj = F(j - 1 - limit, diameter)
                expected = 4 * diameter**2 * (ti - tj) ** 2
                expected /= (1 + ti**2) * (1 + tj**2)
                assert dist == expected
            pair_count += 1
        assert actual_diameter_edges == [(0, j) for j in range(1, len(points))]
    return partner_count, pair_count


def check_regression_derivative():
    # u=(1-2t^2)/sqrt(1-t^2), w=sqrt(1-4t^2).
    # All quantities checked below are rational squared identities or bounds.
    for index in range(257):
        t = F(index, 1024)
        u_squared = (1 - 2 * t**2) ** 2 / (1 - t**2)
        w_squared = 1 - 4 * t**2
        assert u_squared - w_squared == t**2 / (1 - t**2)
        assert F(7, 8) ** 2 <= u_squared <= 1
        assert F(3, 4) ** 2 <= w_squared <= 1
        # These bounds imply 2t^2 <= F'(t) <= 3t^2 for the entire interval;
        # samples additionally catch transcription mistakes in the identity.
        assert F(4) / (F(15, 16) * F(13, 8)) < 3
    return 257


def check_degree_packets():
    graph_count = 0
    packet_count = 0
    for order in range(1, 6):
        possible_edges = list(combinations(range(order), 2))
        for edge_mask in range(1 << len(possible_edges)):
            degree = [0] * order
            for index, (u, v) in enumerate(possible_edges):
                if edge_mask & (1 << index):
                    degree[u] += 1
                    degree[v] += 1
            loaded = [v for v in range(order) if degree[v] > 0]
            total_moment = sum((degree[v] - 1) ** 3 for v in loaded)
            for packet_mask in range(1, 1 << len(loaded)):
                packet = [v for i, v in enumerate(loaded) if packet_mask & (1 << i)]
                incidence = sum(degree[v] for v in packet)
                count = len(packet)
                moment = sum((degree[v] - 1) ** 3 for v in packet)
                assert (incidence - count) ** 3 <= count**2 * moment
                assert moment <= total_moment
                if count <= F(incidence, 2):
                    assert incidence**3 <= 8 * count**2 * total_moment
                packet_count += 1
            graph_count += 1
    return graph_count, packet_count


def check_square_root_forests():
    for count in (2, 4, 8, 16, 32):
        diameter = count**2
        edge_count = count**2
        vertex_count = count * (count + 1)
        degree = [count] * count + [1] * count**2
        moment = sum((d - 1) ** 3 for d in degree)
        assert edge_count == diameter
        assert sum(degree) == 2 * edge_count
        assert vertex_count - edge_count == count
        assert vertex_count <= 2 * diameter
        assert moment == count * (count - 1) ** 3 < diameter**2
        incidence = count**2
        assert (incidence - count) ** 3 == count**2 * moment
    return 5


if __name__ == "__main__":
    stars, pairs = check_rational_stars()
    samples = check_regression_derivative()
    graphs, packets = check_degree_packets()
    forests = check_square_root_forests()
    print(f"PASS: 4 exact star witnesses; {stars} partners; {pairs} source pairs")
    print(f"PASS: {samples} rational squared-identity samples")
    print(f"PASS: {graphs} finite graphs; {packets} degree packets")
    print(f"PASS: {forests} abstract square-root carrier forests (geometry omitted)")
    print("Scope: finite regressions and arithmetic; no global-optimality certificate")
