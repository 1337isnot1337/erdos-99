#!/usr/bin/env python3
"""Exact finite checks for protected simultaneous first-contact creation.

General statements and proofs are in the associated C-II closing-run report.
This script certifies finite separated near-lattice motions and a different-first-
blocker example. It does not certify a global minimum or a C-II survivor.
"""

from fractions import Fraction as F
from itertools import combinations


def norm2(p, q):
    """Integer numerator for coordinates (x, sqrt(3)*y)/denominator."""
    return (p[0] - q[0]) ** 2 + 3 * (p[1] - q[1]) ** 2


def minimum_during_motion(p, q, vp, vq):
    """Exact minimum squared numerator on the entire common time interval [0,1]."""
    dx, dy = p[0] - q[0], p[1] - q[1]
    vx, vy = vp[0] - vq[0], vp[1] - vq[1]
    aa = vx * vx + 3 * vy * vy
    bb = dx * vx + 3 * dy * vy
    cc = dx * dx + 3 * dy * dy
    if aa == 0 or bb >= 0:
        return cc
    if -bb >= aa:
        return aa + 2 * bb + cc
    return F(cc * aa - bb * bb, aa)


def near_lattice_check(size):
    denominator = 2 * size * size
    scale = size * size + 1
    labels = [(i, j) for j in range(size) for i in range(size)]
    points = [((2 * i + j) * scale, j * scale) for i, j in labels]
    index = {ij: k for k, ij in enumerate(labels)}
    unit2 = denominator * denominator

    # Four index layers imply distance >3 from every parallelogram side.
    matching = [
        (index[i, j], index[i + 1, j])
        for j in range(4, size - 4)
        for i in range(4, size - 5, 2)
    ]
    assert matching
    assert len({v for pair in matching for v in pair}) == 2 * len(matching)
    selected = []
    for pair in matching:
        if all(norm2(points[pair[0]], points[old[0]]) > 9 * unit2
               for old in selected):
            selected.append(pair)
    assert 49 * len(selected) >= len(matching)

    velocity = [(0, 0)] * len(points)
    for center, mate in selected:
        assert norm2(points[center], points[mate]) == 4 * scale * scale
        velocity[center] = (2, 0)  # Physical displacement 1/size^2.

    final = [(p[0] + v[0], p[1] + v[1]) for p, v in zip(points, velocity)]
    contacts = set()
    initial_diameter2 = 0
    final_diameter2 = 0
    pairs_checked = 0
    for i, j in combinations(range(len(points)), 2):
        old = norm2(points[i], points[j])
        new = norm2(final[i], final[j])
        assert old > unit2
        assert minimum_during_motion(points[i], points[j], velocity[i], velocity[j]) >= unit2
        if new == unit2:
            contacts.add((i, j))
        initial_diameter2 = max(initial_diameter2, old)
        final_diameter2 = max(final_diameter2, new)
        pairs_checked += 1
    assert contacts == {tuple(sorted(pair)) for pair in selected}
    assert final_diameter2 == initial_diameter2
    print(f"size={size}: points={len(points)}, candidate_pairs={len(matching)}, "
          f"simultaneous_contacts={len(selected)}, continuous_pair_checks={pairs_checked}; PASS")


def different_first_blocker():
    # All coordinates are rational. The exact stopping time is the first root
    # of f(t)=|z-(t,0)|^2-1, certified in (1/300,1/250).
    x = (F(0), F(0))
    y = (F(21, 20), F(0))
    z = (F(7007, 25000), F(24024, 25000))
    sq = lambda p, q: sum((a - b) ** 2 for a, b in zip(p, q))
    assert all(sq(p, q) > 1 for p, q in combinations((x, y, z), 2))
    f = lambda t: (t - z[0]) ** 2 + z[1] ** 2 - 1
    lo, hi = F(1, 300), F(1, 250)
    assert f(lo) > 0 > f(hi)
    assert hi < F(1, 20) < z[0]  # f is strictly decreasing up to target closing.
    assert (y[0] - hi) ** 2 > 1
    print("different first blocker: exact root in (1/300,1/250), "
          "before target time 1/20; PASS")


if __name__ == "__main__":
    for grid_size in (12, 20, 32):
        near_lattice_check(grid_size)
    different_first_blocker()
    print("Exact finite motion checks passed. No global-optimality claim.")
