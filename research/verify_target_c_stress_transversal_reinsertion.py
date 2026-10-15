#!/usr/bin/env python3
"""Exact finite tests for the stress-transversal/reinsertion proof draft.

Certifies finite stress and motion examples, hexagonal-container arithmetic, and
abstract simplex face counts. Does not prove a C-II packing reserve, global
optimality of an example, or Erdős #99. General theorems are proved in
docs/reports/target_c_stress_transversal_reinsertion_2026-09-12.md.
Only Python's standard library is required. No floating-point decisions are used.
"""

from fractions import Fraction as F
from itertools import combinations


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def distance2(a, b):
    delta = sub(a, b)
    return dot(delta, delta)


def quadratic(a, b, c, t):
    return a * t * t + b * t + c


def interval_min(a, b, c, end):
    """Exact minimum of a squared-distance quadratic on [0,end]."""
    candidates = [c, quadratic(a, b, c, end)]
    if a:
        critical = -b / (2 * a)
        if 0 < critical < end:
            candidates.append(quadratic(a, b, c, critical))
    return min(candidates)


def square_test(m):
    boundary = [
        (F(x), F(y))
        for x in range(m + 1)
        for y in range(m + 1)
        if x in (0, m) or y in (0, m)
    ]
    isolate = (F(m, 2), F(m, 2))
    source = boundary + [isolate]
    assert len(source) == 4 * m + 1
    diameter2 = F(2 * m * m)
    contacts, diameters = [], []
    for i, j in combinations(range(len(source)), 2):
        dsq = distance2(source[i], source[j])
        assert 1 <= dsq <= diameter2
        if dsq == 1:
            contacts.append((i, j))
        if dsq == diameter2:
            diameters.append((i, j))
    assert len(contacts) == 4 * m
    assert len(diameters) == 2
    assert all(len(source) - 1 not in e for e in contacts + diameters)

    # Exact normalized equilibrium, including the original isolate's zero row.
    forces = [[F(0), F(0)] for _ in source]
    for edges, weight in ((contacts, F(m, 2)), (diameters, F(-1, 2))):
        for i, j in edges:
            delta = sub(source[i], source[j])
            for axis in (0, 1):
                forces[i][axis] += weight * delta[axis]
                forces[j][axis] -= weight * delta[axis]
    assert all(f == [0, 0] for f in forces)
    assert F(1, 2) * len(diameters) == 1
    assert F(m, 2) * len(contacts) == diameter2

    retained = [p for p in boundary if p != (m, m)]
    inserted = [(F(m, 2) - 1, F(m, 2)), (F(m, 2) + 1, F(m, 2))]
    initial = retained + inserted
    velocities = [(y, x) for x, y in retained] + [(F(0), F(0))] * 2
    assert len(initial) == len(source)
    assert len(set(initial)) == len(source)
    for b in inserted:
        for r in retained:
            assert 1 < distance2(b, r) < diameter2
    assert 1 < distance2(*inserted) < diameter2

    # All contacts and all inherited diameter pairs, not a selected subgraph.
    inherited_diameters = 0
    for i, j in combinations(range(len(retained)), 2):
        delta = sub(initial[i], initial[j])
        velocity = sub(velocities[i], velocities[j])
        dsq = dot(delta, delta)
        if dsq == 1:
            assert dot(delta, velocity) == 0
        if dsq == diameter2:
            inherited_diameters += 1
            assert dot(delta, velocity) == -2 * m * m
    assert inherited_diameters == 1

    end = F(1, 10 * m)
    min_final, max_final = None, F(0)
    pairs_checked = 0
    for i, j in combinations(range(len(initial)), 2):
        delta = sub(initial[i], initial[j])
        velocity = sub(velocities[i], velocities[j])
        a, b, c = dot(velocity, velocity), 2 * dot(delta, velocity), dot(delta, delta)
        final = quadratic(a, b, c, end)
        assert interval_min(a, b, c, end) >= 1
        assert c <= diameter2
        assert 1 < final < diameter2
        # Convexity bounds the quadratic above by its endpoint chord. As the
        # right endpoint is strictly below D^2, every t>0 is strictly below D^2.
        assert a >= 0
        min_final = final if min_final is None else min(min_final, final)
        max_final = max(max_final, final)
        pairs_checked += 1
    return pairs_checked, min_final - 1, diameter2 - max_final


def hexagon_test(m):
    s, t = 1 + F(1, 100 * m * m), 1 + F(1, 200 * m * m)
    lattice = [
        (i, j)
        for i in range(-m, m + 1)
        for j in range(-m, m + 1)
        if max(abs(i), abs(j), abs(i + j)) <= m
    ]
    count = 3 * m * m + 3 * m + 1
    assert len(lattice) == count
    assert 1 < t < s
    for i, j in lattice:
        assert max(abs(t * i), abs(t * j), abs(t * (i + j))) < s * m
    # The norm of an axial lattice vector is i^2+ij+j^2, an integer.
    # Positivity of the quadratic form proves the all-m separation analytically;
    # exhaust the pair list for these finite instances as an extra check.
    for p, q in combinations(lattice, 2):
        i, j = sub(p, q)
        norm = i * i + i * j + j * j
        assert norm >= 1
        assert t * t * norm > 1
    oler_bound = 3 * m * m * s * s + 3 * m * s + 1
    expected_gap = F(3, 50) + F(3, 100 * m) + F(3, 10000 * m * m)
    assert oler_bound - count == expected_gap
    assert 0 < expected_gap <= F(903, 10000) < 1
    return count


def simplex_test(k):
    # For Delta_{k-1}, intersection beta_j=0 is nonempty precisely when at
    # least one of the k coordinates was not selected.
    unit_vertices = [tuple(int(i == j) for i in range(k)) for j in range(k)]
    cases = 0
    for size in range(k + 1):
        for selected in combinations(range(k), size):
            survivors = [v for v in unit_vertices if all(v[j] == 0 for j in selected)]
            assert bool(survivors) == (size < k)
            cases += 1
    return cases


def hexagon_center_stress_test():
    """Exact Q(sqrt(3)) geometry; store (x,y/sqrt(3)) as rational pairs."""
    points = [(F(1), F(0)), (F(1, 2), F(1, 2)), (F(-1, 2), F(1, 2)),
              (F(-1), F(0)), (F(-1, 2), F(-1, 2)), (F(1, 2), F(-1, 2)),
              (F(0), F(0))]
    ring = [tuple(sorted((i, (i + 1) % 6))) for i in range(6)]
    spokes = [(i, 6) for i in range(6)]
    diameters = [(i, i + 3) for i in range(3)]
    contacts = ring + spokes
    for i, j in combinations(range(7), 2):
        dx, dy = sub(points[i], points[j])
        dsq = dx * dx + 3 * dy * dy
        assert 1 <= dsq <= 4
        assert (dsq == 1) == ((i, j) in contacts)
        assert (dsq == 4) == ((i, j) in diameters)

    # Full stress polytope: parameter a for equal ring weights and beta_i for
    # diameter weights, with spoke weights 2 beta_{i mod 3} - a.
    def stress(a, beta):
        alpha = [a] * 6 + [2 * beta[i % 3] - a for i in range(6)]
        assert min(alpha + beta) >= 0
        assert sum(beta) == 1
        forces = [[F(0), F(0)] for _ in points]
        support = set()
        for edges, weights, sign in ((contacts, alpha, 1), (diameters, beta, -1)):
            for (i, j), weight in zip(edges, weights):
                if weight:
                    support.update((i, j))
                dx, dy = sub(points[i], points[j])
                # Dividing all y-equilibrium equations by sqrt(3) is exact.
                for axis, delta in enumerate((dx, dy)):
                    forces[i][axis] += sign * weight * delta
                    forces[j][axis] -= sign * weight * delta
        assert all(f == [0, 0] for f in forces)
        return alpha + beta, support

    extreme = [stress(F(2, 3), [F(1, 3)] * 3)]
    extreme.extend(stress(F(0), [F(int(i == j)) for i in range(3)]) for j in range(3))
    # Each single-vertex deletion leaves at least one genuine normalized stress.
    for deleted in range(7):
        assert any(deleted not in support for _, support in extreme)
    # Deleting center and one hull vertex kills every extreme stress. The
    # report proves these are all vertices, so this is an all-stress statement.
    assert not any(not ({0, 6} & support) for _, support in extreme)
    # Every pair of diameter-coordinate-zero faces leaves a straight-chain stress.
    for chosen in combinations(range(3), 2):
        assert any(all(weights[12 + j] == 0 for j in chosen) for weights, _ in extreme)
    assert not any(all(weight == 0 for weight in weights[12:]) for weights, _ in extreme)
    print("PASS hexagon-plus-center: all 7 single deletions retain stress; a 2-vertex deletion suffices")


def main():
    total_pairs = 0
    min_separation_margin, min_diameter_margin = None, None
    for m in range(6, 25, 2):
        pairs, separation_margin, diameter_margin = square_test(m)
        total_pairs += pairs
        min_separation_margin = (
            separation_margin if min_separation_margin is None
            else min(min_separation_margin, separation_margin)
        )
        min_diameter_margin = (
            diameter_margin if min_diameter_margin is None
            else min(min_diameter_margin, diameter_margin)
        )
    print(f"PASS square sources m=6,8,...,24: {total_pairs} whole-interval pair checks")
    print(f"  least final squared-separation margin above 1: {min_separation_margin}")
    print(f"  least final squared-diameter improvement: {min_diameter_margin}")
    counts = [hexagon_test(m) for m in range(1, 13)]
    print(f"PASS hexagons m=1,...,12: populations {counts[0]} through {counts[-1]}")
    print("  exact Oler increment <= 903/10000 < 1; integer reserve is zero")
    faces = sum(simplex_test(k) for k in range(1, 9))
    print(f"PASS simplex dimensions 0,...,7: {faces} coordinate-face intersections")
    hexagon_center_stress_test()
    print("SCOPE: finite certificates only; no global optimality or C-II closure.")


if __name__ == "__main__":
    main()
