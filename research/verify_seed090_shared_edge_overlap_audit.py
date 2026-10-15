#!/usr/bin/env python3
"""Exact five-label regression for shared-edge cell overlap in Seed 90.

Coordinates and squared distances are computed in Q(sqrt(3)); the script checks
only the finite counterexample to the unrestricted same-half-plane sentence.
The repaired propagation argument is proved analytically in the accompanying
report.
"""

from fractions import Fraction as F
from itertools import combinations


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[0], -x[1]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return x[0] * y[0] + 3 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def norm2(point_a, point_b):
    dx = sub(point_a[0], point_b[0])
    dy = sub(point_a[1], point_b[1])
    return add(mul(dx, dx), mul(dy, dy))


# A scalar (r, s) denotes r + s*sqrt(3).
zero, one = (F(0), F(0)), (F(1), F(0))
half, root3_half = (F(1, 2), F(0)), (F(0), F(1, 2))
points = {
    "A": (zero, zero),
    "B": (zero, one),
    "D": (root3_half, half),
    "C": (root3_half, (F(3, 2), F(0))),
    "E": (root3_half, (F(-1, 2), F(0))),
}

expected = {
    ("A", "B"): F(1),
    ("A", "C"): F(3),
    ("A", "D"): F(1),
    ("A", "E"): F(1),
    ("B", "C"): F(1),
    ("B", "D"): F(1),
    ("B", "E"): F(3),
    ("C", "D"): F(1),
    ("C", "E"): F(4),
    ("D", "E"): F(1),
}
observed = {}
for a, b in combinations(points, 2):
    value = norm2(points[a], points[b])
    require(value[1] == 0, f"unexpected sqrt(3) term for pair {a},{b}")
    require(value[0] >= 1, f"unit-separation failure for pair {a},{b}")
    observed[tuple(sorted((a, b)))] = value[0]
require(observed == expected, "pair-distance ledger mismatch")

cycles = (("A", "B", "C", "D"), ("A", "B", "D", "E"))
for cycle in cycles:
    sides = tuple(zip(cycle, cycle[1:] + cycle[:1]))
    require(all(observed[tuple(sorted(edge))] == 1 for edge in sides),
            f"nonunit side in cycle {cycle}")

diagonals = (
    (observed[("A", "C")], observed[("B", "D")]),
    (observed[("A", "D")], observed[("B", "E")]),
)
require(diagonals == ((F(3), F(1)), (F(1), F(3))),
        "diagonal ledger mismatch")
require(set(cycles[0]) & set(cycles[1]) == {"A", "B", "D"},
        "cycles do not have the intended overlap")
require(all(points[label][0][1] == F(1, 2) for label in ("C", "D", "E")),
        "off-edge vertices are not on the same side of AB")

print({
    "labels": len(points),
    "pair_count": len(observed),
    "minimum_squared_distance": min(observed.values()),
    "cycles": cycles,
    "shared_labels": sorted(set(cycles[0]) & set(cycles[1])),
    "same_open_half_plane": True,
    "status": "PASS: the unrestricted same-half-plane sentence needs an overlap case",
})
