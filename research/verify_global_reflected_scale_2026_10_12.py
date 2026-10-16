#!/usr/bin/env python3
"""Exact full-source certificate for a discontinuous reflected/scaled endpoint.

The proof of the general signed-graph decision theorem is in the paired report.
This script certifies finite fixtures, not endpoint existence for minimizers.
All coordinates, squared scales, pair costs, and checks use fractions.Fraction.
"""

if not __debug__:
    raise RuntimeError("Certificate assertions are required; run Python without -O.")

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product


@dataclass(frozen=True)
class PairCosts:
    i: int
    j: int
    same: F
    opposite: F


def decide(points, normal, offset, normal_scale_sq, tangent_scale_sq, diameter_sq):
    """Return all sign bits and exact pair costs, or an obstruction.

    Bit 0 is positive normal coordinate; bit 1 is negative. The two possible
    squared distances are ordered, so a pair contributes equality, inequality,
    both constraints, or no constraint. Positive squared scales are required.
    """
    assert sum(z * z for z in normal) == 1
    assert normal_scale_sq > 0 and tangent_scale_sq > 0
    tangent = (-normal[1], normal[0])
    x = [abs(a * normal[0] + b * normal[1] - offset) for a, b in points]
    y = [a * tangent[0] + b * tangent[1] for a, b in points]
    adjacency = [[] for _ in points]
    costs = []
    for i, j in combinations(range(len(points)), 2):
        tangent_cost = tangent_scale_sq * (y[i] - y[j]) ** 2
        same = normal_scale_sq * (x[i] - x[j]) ** 2 + tangent_cost
        opposite = normal_scale_sq * (x[i] + x[j]) ** 2 + tangent_cost
        costs.append(PairCosts(i, j, same, opposite))
        if opposite < 1:
            return None, costs, ("lower pair", i, j)
        if same >= diameter_sq:
            return None, costs, ("upper pair", i, j)
        for condition, parity in [(same < 1, 1), (opposite >= diameter_sq, 0)]:
            if condition:
                adjacency[i].append((j, parity))
                adjacency[j].append((i, parity))
    signs = [None] * len(points)
    for root in range(len(points)):
        if signs[root] is not None:
            continue
        signs[root] = 0
        queue = [root]
        for i in queue:
            for j, parity in adjacency[i]:
                required = signs[i] ^ parity
                if signs[j] is None:
                    signs[j] = required
                    queue.append(j)
                elif signs[j] != required:
                    return None, costs, ("parity inconsistency", i, j)
    return signs, costs, None


def distance_sq(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


def independent_endpoint_distances(points, signs, normal, offset, a_sq, b_sq):
    """Reconstruct endpoint axis coordinates and check every pair directly.

    Store coordinates divided by their square-root scale. This avoids floats
    while giving exactly the squared distances of actual algebraic coordinates.
    """
    if len(signs) != len(points) or any(bit not in (0, 1) for bit in signs):
        raise ValueError("Every source label requires exactly one sign bit.")
    tangent = (-normal[1], normal[0])
    endpoint = [
        ((1 - 2 * bit) * abs(p[0] * normal[0] + p[1] * normal[1] - offset),
         p[0] * tangent[0] + p[1] * tangent[1])
        for p, bit in zip(points, signs)
    ]
    return [a_sq * (p[0] - q[0]) ** 2 + b_sq * (p[1] - q[1]) ** 2
            for p, q in combinations(endpoint, 2)]


def verify_decision_oracle():
    """Compare parity decisions with exhaustive actual endpoint assignments."""
    cloud = [(F(x), F(y)) for x, y in [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)]]
    outcomes = {"feasible": 0, "lower pair": 0, "upper pair": 0,
                "parity inconsistency": 0}
    parallel_forcing = 0
    for n in (2, 3, 4):
        for points in combinations(cloud, n):
            diameter_sq = max(distance_sq(p, q) for p, q in combinations(points, 2))
            for normal, offset, scales in product(
                    [(F(1), F(0)), (F(3, 5), F(4, 5))], [F(0), F(1, 2)],
                    [(F(1, 2), F(1)), (F(1), F(1, 2)),
                     (F(1), F(1)), (F(2), F(1, 2))]):
                a_sq, b_sq = scales
                signs, costs, obstruction = decide(
                    points, normal, offset, a_sq, b_sq, diameter_sq)
                exists = any(all(1 <= d < diameter_sq for d in
                    independent_endpoint_distances(points, candidate, normal,
                                                   offset, a_sq, b_sq))
                    for candidate in product((0, 1), repeat=n))
                assert (signs is not None) == exists
                outcomes["feasible" if signs is not None else obstruction[0]] += 1
                if signs is not None:
                    assert len(costs) == n * (n - 1) // 2
                    assert all(1 <= d < diameter_sq for d in
                        independent_endpoint_distances(points, signs, normal,
                                                       offset, a_sq, b_sq))
                if any(c.same < 1 and c.opposite >= diameter_sq for c in costs):
                    parallel_forcing += 1
    assert all(outcomes.values()) and parallel_forcing > 0
    for bad_signs in ([0], [0, 2]):
        try:
            independent_endpoint_distances(cloud[:2], bad_signs,
                                           (F(1), F(0)), F(0), F(1), F(1))
        except ValueError:
            continue
        raise AssertionError("Incomplete or invalid sign certificate accepted")
    print(f"PASS: {sum(outcomes.values())} decision cases match exhaustive sign oracle; "
          f"{outcomes}; {parallel_forcing} cases exercise parallel forcing")
    print("PASS: omitted-label and invalid-bit endpoint certificates rejected")


def verify_moment_identity(points, signs, normal, offset, a_sq, b_sq):
    """Check the finite second/fourth moment identity without algebraic floats."""
    assert sum(p[0] for p in points) == sum(p[1] for p in points) == 0
    tangent = (-normal[1], normal[0])
    x = [p[0] * normal[0] + p[1] * normal[1] for p in points]
    y = [p[0] * tangent[0] + p[1] * tangent[1] for p in points]
    z = [(1 - 2 * bit) * abs(xx - offset) for bit, xx in zip(signs, x)]
    def mean(values):
        return sum(values) / F(len(points))
    z_mean = mean(z)
    z_centered = [zz - z_mean for zz in z]
    sx, sy = mean(xx * xx for xx in x), mean(yy * yy for yy in y)
    mixed = mean(xx * xx * yy * yy for xx, yy in zip(x, y))
    odd = mean(xx * yy * yy for xx, yy in zip(x, y))
    vx = a_sq * mean(zz * zz for zz in z_centered)
    vy = b_sq * sy
    w = a_sq * b_sq * mean(zz * zz * yy * yy for zz, yy in zip(z_centered, y))
    twice_m_l = 2 * a_sq * b_sq * z_mean * mean(zz * yy * yy for zz, yy in zip(z_centered, y))
    lhs = w + twice_m_l - vx * vy
    denominator = b_sq * (mixed - sx * sy - 2 * offset * odd)
    assert lhs == a_sq * denominator
    if denominator:
        assert lhs / denominator == a_sq
    return odd


def verify_affine_obstruction_fixture():
    points = [(F(i), F(j)) for i, j in product(range(-15, 16), range(-2, 3))]
    points.extend([(F(0), F(16, 5)), (F(0), F(-16, 5))])
    original = [distance_sq(p, q) for p, q in combinations(points, 2)]
    assert min(original) == 1 and max(original) == 916
    contacts = {(i, j) for i, j in combinations(range(len(points)), 2)
                if distance_sq(points[i], points[j]) == 1}
    for i in range(len(points)):
        neighbors = {j for a, b in contacts for j in ([b] if a == i else [a] if b == i else [])}
        assert not any((min(j, k), max(j, k)) in contacts for j, k in combinations(neighbors, 2))
    assert all(not any(i in edge for edge in contacts) for i in [155, 156])

    normal = (F(351, 449), F(280, 449))
    a_sq, b_sq = F(1, 2), F(9, 5)
    signs, _, obstruction = decide(points, normal, F(0), a_sq, b_sq, F(916))
    assert obstruction is None
    actual = independent_endpoint_distances(points, signs, normal, F(0), a_sq, b_sq)
    assert len(actual) == 12246
    assert min(actual) == F(405441, 403202) > 1
    assert max(actual) == F(865065744, 1008005) < 916
    verify_moment_identity(points, signs, normal, F(0), a_sq, b_sq)

    # Explicit normalized stress: each side chain has conductance lambda
    # after eliminating its degree-two interior labels.
    lam = F(1, 1832)
    contact_mass = 60 * 30 * lam + 8 * 4 * lam
    diameter_mass = 2 * 916 * lam
    assert contact_mass == diameter_mass == 1
    weights = {}
    for i, j in contacts:
        p, q = points[i], points[j]
        if p[1] == q[1] and abs(p[1]) == 2:
            weights[i, j] = 30 * lam
        elif p[0] == q[0] and abs(p[0]) == 15:
            weights[i, j] = 4 * lam
    diameter_pairs = {(i, j) for i, j in combinations(range(len(points)), 2)
                      if distance_sq(points[i], points[j]) == 916}
    assert len(diameter_pairs) == 2
    for i, p in enumerate(points):
        force = [F(0), F(0)]
        for edges, sign in [(weights.items(), 1), ([(e, lam) for e in diameter_pairs], -1)]:
            for (j, k), weight in edges:
                if i not in [j, k]:
                    continue
                other = k if i == j else j
                for d in [0, 1]:
                    force[d] += sign * weight * (p[d] - points[other][d])
        assert force == [0, 0]
    print(f"157 labels, {len(actual)} full-source pairs, two contact isolates retained")
    print(f"old diameter squared = 916; endpoint range = [{min(actual)}, {max(actual)}]")
    print(f"strict diameter-squared gain = {F(916) - max(actual)}")
    print("normalized nonnegative equilibrium checked at every source label")

    # The nonzero odd moment exercises the line-offset term independently of
    # the symmetric packing fixture. This is an algebraic identity fixture.
    asymmetric = [(F(x), F(y)) for x, y in [(0, 0), (2, 0), (0, 3), (4, 1), (1, 5)]]
    center = [sum(p[d] for p in asymmetric) / 5 for d in [0, 1]]
    asymmetric = [(p[0] - center[0], p[1] - center[1]) for p in asymmetric]
    assert verify_moment_identity(asymmetric, [0, 1, 0, 1, 1], normal,
                                  F(3, 7), a_sq, b_sq) != 0
    s, t = F(1, 16), F(1, 384)
    assert t - s * s == F(-1, 768)
    print("finite moment identity checked, including a nonzero offset/odd-moment term")


def verify_rectangle_family():
    normal = (F(351, 449), F(280, 449))
    a_sq, b_sq = F(1, 2), F(9, 5)
    # The analytical family is infinite; these checks also exercise the explicit
    # formula without relying on the signed-graph solver to choose an endpoint.
    for m, k in [(40, 1), (60, 2)]:
        points = [(F(i), F(j)) for i, j in product(range(-m, m + 1), range(-k, k + 1))]
        central = 4 * k + 2
        signs = [int(p[0] * normal[0] + p[1] * normal[1] < 0) if abs(p[0]) <= central else 0
                 for p in points]
        actual = independent_endpoint_distances(points, signs, normal, F(0), a_sq, b_sq)
        assert min(actual) > 1
        assert max(actual) < 4 * (m * m + k * k)
        print(f"family fixture M={m}, K={k}: {len(points)} labels, {len(actual)} pairs verified")


if __name__ == "__main__":
    verify_decision_oracle()
    verify_affine_obstruction_fixture()
    verify_rectangle_family()
    print("PASS: exact endpoint fixtures only; no global-minimizer extraction or Level I closure")
