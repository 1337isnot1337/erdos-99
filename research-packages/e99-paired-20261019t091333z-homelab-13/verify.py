#!/usr/bin/env python3
"""Independent exact audit controls for the supplied-parameter parity theorem."""

if not __debug__:
    raise RuntimeError("Assertions are part of this audit; do not use python -O.")

from fractions import Fraction as F
from itertools import combinations, product


def distance_sq(p, q):
    return sum((x - y) ** 2 for x, y in zip(p, q))


def source_diameter_sq(points):
    return max(distance_sq(p, q) for p, q in combinations(points, 2))


def costs(points, normal, offset, a, b):
    """Compute the two exact squared costs for each unordered label pair."""
    tangent = (-normal[1], normal[0])
    x = [abs(p[0] * normal[0] + p[1] * normal[1] - offset)
         for p in points]
    y = [p[0] * tangent[0] + p[1] * tangent[1] for p in points]
    rows = []
    for i, j in combinations(range(len(points)), 2):
        dy = y[i] - y[j]
        same = a * (x[i] - x[j]) ** 2 + b * dy ** 2
        opposite = a * (x[i] + x[j]) ** 2 + b * dy ** 2
        rows.append((i, j, same, opposite))
    return x, y, rows


def forced_system(points, normal, offset, a, b, diameter_sq):
    """Return the exact pair constraints, forbidden-pair flag, and label count."""
    _, _, pair_rows = costs(points, normal, offset, a, b)
    edges = []
    forbidden = False
    both_parities = 0
    for i, j, same, opposite in pair_rows:
        if opposite < 1 or same >= diameter_sq:
            forbidden = True
        parities = []
        if same < 1:
            parities.append(1)  # opposite signs
        if opposite >= diameter_sq:
            parities.append(0)  # equal signs
        if len(parities) == 2:
            both_parities += 1
        edges.extend((i, j, parity) for parity in parities)
    return edges, forbidden, both_parities


def enumerate_forced_assignments(n, edges):
    """Exhaust all label sign vectors instead of using cycle propagation."""
    solutions = []
    for mask in range(1 << n):
        bits = tuple((mask >> i) & 1 for i in range(n))
        if all((bits[i] ^ bits[j]) == parity for i, j, parity in edges):
            solutions.append(bits)
    return solutions


def direct_endpoint_distances(points, bits, normal, offset, a, b):
    """Measure the actual reflected coordinates, independently of s/o edges."""
    tangent = (-normal[1], normal[0])
    positions = []
    for point, bit in zip(points, bits):
        signed_normal = point[0] * normal[0] + point[1] * normal[1] - offset
        x = abs(signed_normal)
        y = point[0] * tangent[0] + point[1] * tangent[1]
        positions.append(((1 - 2 * bit) * x, y))
    return [a * (p[0] - q[0]) ** 2 + b * (p[1] - q[1]) ** 2
            for p, q in combinations(positions, 2)]


def audit_small_exact_domain():
    cloud = [(F(x), F(y)) for x, y in
             [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)]]
    normals = [(F(1), F(0)), (F(3, 5), F(4, 5))]
    offsets = [F(0), F(1, 2)]
    scale_pairs = [(F(1, 2), F(1)), (F(1), F(1, 2)),
                   (F(1), F(1)), (F(2), F(1, 2))]
    totals = {"feasible": 0, "lower-forbidden": 0,
              "upper-forbidden": 0, "parity-inconsistent": 0}
    both_constraints = 0
    cycle_only_inconsistencies = 0

    for n in (2, 3, 4):
        for points in combinations(cloud, n):
            d2 = source_diameter_sq(points)
            for normal, offset, (a, b) in product(
                    normals, offsets, scale_pairs):
                edges, forbidden, both = forced_system(
                    points, normal, offset, a, b, d2)
                both_constraints += both
                forced = enumerate_forced_assignments(n, edges)
                theorem_feasible = not forbidden and bool(forced)

                direct = []
                for bits in product((0, 1), repeat=n):
                    ds = direct_endpoint_distances(
                        points, bits, normal, offset, a, b)
                    if all(1 <= d < d2 for d in ds):
                        direct.append(bits)
                assert theorem_feasible == bool(direct)
                if theorem_feasible:
                    assert all(1 <= d < d2 for d in direct_endpoint_distances(
                        points, forced[0], normal, offset, a, b))
                    totals["feasible"] += 1
                elif any(opposite < 1 for _, _, _, opposite in
                         costs(points, normal, offset, a, b)[2]):
                    totals["lower-forbidden"] += 1
                elif any(same >= d2 for _, _, same, _ in
                         costs(points, normal, offset, a, b)[2]):
                    totals["upper-forbidden"] += 1
                else:
                    totals["parity-inconsistent"] += 1
                    if not both:
                        cycle_only_inconsistencies += 1

    assert sum(totals.values()) == 400
    assert all(totals.values())
    assert both_constraints > 0 and cycle_only_inconsistencies > 0
    print(f"PASS: {sum(totals.values())} exact small-source cases; "
          f"{totals}; {both_constraints} paired-edge cases; "
          f"{cycle_only_inconsistencies} cycle-only parity failures")


def check_boundary(points, normal, offset, a, b, expected, expected_s,
                   expected_o, name):
    d2 = source_diameter_sq(points)
    rows = costs(points, normal, offset, a, b)[2]
    assert len(rows) == 1
    _, _, same, opposite = rows[0]
    assert (same, opposite) == (expected_s, expected_o), name
    edges, forbidden, _ = forced_system(points, normal, offset, a, b, d2)
    feasible = not forbidden and bool(enumerate_forced_assignments(2, edges))
    direct = any(all(1 <= d < d2 for d in direct_endpoint_distances(
        points, bits, normal, offset, a, b)) for bits in product((0, 1), repeat=2))
    assert feasible == direct == expected, name


def audit_strict_boundary_conventions():
    n = (F(1), F(0))
    pair = [(F(0), F(0)), (F(2), F(0))]
    # Opposite cost exactly one is allowed; the lower constraint is strict.
    check_boundary(pair, n, F(1), F(1, 4), F(1), True,
                   F(0), F(1), "o = 1")
    # Same cost exactly one is allowed, while o = D^2 forces equal signs.
    check_boundary(pair, n, F(1, 2), F(1), F(1), True,
                   F(1), F(4), "s = 1 and o = D^2")
    # This pair imposes both distinct parities; the two-edge cycle is inconsistent.
    check_boundary(pair, n, F(1), F(1), F(1), False,
                   F(0), F(4), "s < 1 and o = D^2")
    # s = D^2 is already fatal because the upper endpoint is strict.
    check_boundary(pair, n, F(-10), F(1), F(1), False,
                   F(4), F(484), "s = D^2")
    # o < 1 makes even the larger of the two options too short.
    check_boundary(pair, n, F(1), F(1, 16), F(1), False,
                   F(0), F(1, 4), "o < 1")
    print("PASS: exact lower/upper boundary cases, including a contradictory "
          "parallel-edge pair")


if __name__ == "__main__":
    audit_small_exact_domain()
    audit_strict_boundary_conventions()
