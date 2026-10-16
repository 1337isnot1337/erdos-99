"""Checks for the 2026-09-11 endpoint-gap / cyclic-force-hull report.

Exact component: exhaust all ordered subsets of at least two distinct K_4
edges and check I <= 2h-q+1, with cyclic multiplicity for h=2. Geometry is
intentionally omitted in this stronger finite combinatorial test.

Floating components: crossing diameter quadrilaterals, regular odd shells,
two antipodal unit-step arcs, and gap simplexes with the two lower bounds.
They test explicit formulas,
not global optimality, KKT support, arbitrary configurations, or Level I.
The general theorems are proved in the report, independently of these checks.
Run: python3 research/diameter_endpoint_gap_audit.py
"""

from itertools import combinations, permutations
from math import asin, atan2, cos, hypot, pi, sin
from random import Random


def incidence_count(order):
    return sum(bool(set(e) & set(order[(i + 1) % len(order)]))
               for i, e in enumerate(order))


def exact_incidence_checks():
    edges = tuple(combinations(range(4), 2))
    cases = 0
    for h in range(2, len(edges) + 1):
        for order in permutations(edges, h):
            q = len({v for e in order for v in e})
            assert incidence_count(order) <= 2 * h - q + 1, order
            cases += 1
    star = ((0, 1), (0, 2), (0, 3))
    assert incidence_count(star) == 3  # The +1 cannot be dropped.
    assert incidence_count(((0, 1), (0, 2))) == 2
    return cases


def perimeter_area(points):
    pairs = tuple(zip(points, points[1:] + points[:1]))
    perimeter = sum(hypot(b[0] - a[0], b[1] - a[1]) for a, b in pairs)
    area = abs(sum(a[0] * b[1] - a[1] * b[0] for a, b in pairs)) / 2
    return perimeter, area


def close(a, b):
    assert abs(a - b) <= 1e-9 * max(1.0, abs(a), abs(b)), (a, b)


def two_arc_checks():
    cases = 0
    for diameter in (10.0, 30.0, 100.0):
        delta = 2 * asin(1 / diameter)
        for density in (0.4, 0.8, 1.5, 2.5, 3.0):
            m = max(2, int(density * diameter / 2))
            span = (m - 1) * delta
            if pi - span < delta:
                continue
            angles = [i * delta + shift for shift in (0.0, pi) for i in range(m)]
            points = [(diameter * cos(a) / 2, diameter * sin(a) / 2) for a in angles]
            for i, j in combinations(range(len(points)), 2):
                distance = hypot(points[i][0] - points[j][0], points[i][1] - points[j][1])
                assert 1 - 1e-9 <= distance <= diameter + 1e-9
            perimeter, area = perimeter_area(points)
            close(perimeter, 2 * (m - 1) + 2 * diameter * cos(span / 2))
            close(area, diameter**2 * ((m - 1) * sin(delta) + sin(span)) / 4)
            q = 2 * m
            t = max(0.0, (q - 3) / diameter - 8 * pi / diameter**2)
            assert perimeter + 1e-8 >= diameter * (t + 2 * cos(t / 2)) - pi / (6 * diameter)
            assert area + 1e-8 >= diameter**2 * (t + sin(t)) / 4 - pi / 6
            cases += 1
    return cases


def disjoint_chord_checks():
    rng = Random(990912)
    accepted = 0
    for _ in range(10000):
        diameter = rng.uniform(3, 200)
        phi = rng.uniform(0.5, 5) / diameter
        a = diameter * (1 - cos(phi))
        x = rng.random() * a
        u = rng.random() * diameter * sin(phi)
        points = [(0.0, 0.0), (diameter, 0.0),
                  (x, -u), (x + diameter * cos(phi), diameter * sin(phi) - u)]
        # Only the four cross-pairs need filtering; both long chords are D.
        distances = [hypot(points[i][0] - points[j][0], points[i][1] - points[j][1])
                     for i in (0, 1) for j in (2, 3)]
        if min(distances) < 1 or max(distances) > diameter:
            continue
        assert phi + 1e-12 >= 2 / diameter - 8 / diameter**3
        accepted += 1
    assert accepted > 100
    return accepted


def shell_checks():
    cases = 0
    for h in (11, 15, 31, 51, 101):
        radius = 1 / (2 * sin(pi / h))
        diameter = 1 / (2 * sin(pi / (2 * h)))
        points = [(radius * cos(2 * pi * i / h), radius * sin(2 * pi * i / h))
                  for i in range(h)]
        step = (h - 1) // 2
        angles = []
        for i in range(h):
            j = (i + step) % h
            angles.append(atan2(points[j][1] - points[i][1], points[j][0] - points[i][0]) % pi)
        angles.sort()
        gaps = [(angles[(i + 1) % h] - angles[i]) % pi for i in range(h)]
        close(max(gaps), pi / h)  # CY.1 equality threshold.
        perimeter, area = perimeter_area(points)
        t = max(0.0, (h - 3) / diameter - 8 * pi / diameter**2)
        assert perimeter >= diameter * (t + 2 * cos(t / 2)) - pi / (6 * diameter)
        ell = max(0.0, radius**2 - diameter**2 / 4)**0.5
        lower = diameter**2 * (t + sin(t)) / 4 - pi / 6 - pi * diameter * ell - pi * ell**2
        assert area >= lower
        cases += 1
    return cases


def gap_checks():
    rng = Random(990911)
    cases = 0
    for _ in range(2000):
        diameter = rng.uniform(3, 300)
        h = rng.randint(2, max(2, int(pi * diameter / 2)))
        floors = [1 / diameter if rng.randrange(2) else 2 / diameter - 8 / diameter**3
                  for _ in range(h)]
        leftover = pi - sum(floors)
        if leftover < 0:
            continue
        weights = [rng.random() for _ in range(h)]
        total = sum(weights)
        gaps = [b + leftover * w / total for b, w in zip(floors, weights)]
        lower_sine = min(sum(sin(floors[i]) for i in range(h) if i != j)
                         + sin(sum(floors[i] for i in range(h) if i != j))
                         for j in range(h))
        lower_half = min(sum(sin(floors[i] / 2) for i in range(h) if i != j)
                         + cos(sum(floors[i] for i in range(h) if i != j) / 2)
                         for j in range(h))
        assert sum(map(sin, gaps)) + 1e-9 >= lower_sine
        assert sum(sin(g / 2) for g in gaps) + 1e-9 >= lower_half
        cases += 1
    return cases


def root(f, a, b):
    for _ in range(80):
        midpoint = (a + b) / 2
        if f(midpoint) > 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2


if __name__ == "__main__":
    print(f"Exact ordered K4 incidence checks: {exact_incidence_checks()} PASS")
    print(f"Floating admissible crossing quadrilateral checks: {disjoint_chord_checks()} PASS")
    print(f"Floating two-arc geometry checks: {two_arc_checks()} PASS")
    print(f"Floating regular-shell checks: {shell_checks()} PASS")
    print(f"Floating concave gap-simplex checks: {gap_checks()} PASS")
    x0 = root(lambda x: 3 * x - 2 * cos(x / 2), 0, pi)
    rho = root(lambda x: x - cos(x), 0, 1)
    print(f"Illustrative x0={x0:.12f}, canonical-input area floor={(x0 + sin(x0)) / 4:.12f}")
    print(f"Conditional post-ZF area floor={(2 * rho + sin(2 * rho)) / 4:.12f}")
    print("No computation certifies global optimality or a solution of Erdős #99.")
