#!/usr/bin/env python3
"""Exact leaf-attachment witness for the Audit 124 outer-walk correction.

Checks the four-point rational positive-equilibrium star, all six distances,
directed outer-face traversal, single leaf occurrences, double bridge use and
the three augmented pockets. The preservation report proves the general plane
graph lemma analytically. No global optimality is asserted for this fixture.
"""

if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from collections import Counter
from fractions import Fraction as F
from itertools import combinations

from verify_target_c_monotone_cap_routes_2026_10_04 import face_walks


def main():
    points = {0: (F(0), F(0)), 1: (F(99, 101), F(20, 101)),
              2: (F(-99, 101), F(20, 101)), 3: (F(0), F(-1))}
    contacts = set()
    for a, b in combinations(points, 2):
        squared = sum((points[a][d]-points[b][d])**2 for d in (0, 1))
        assert squared >= 1
        if squared == 1:
            contacts.add((a, b))
    assert contacts == {(0, 1), (0, 2), (0, 3)}
    weights = {1: F(101, 40), 2: F(101, 40), 3: F(1)}
    assert all(sum(weights[a]*points[a][d] for a in weights) == 0 for d in (0, 1))
    # Exact counterclockwise rotations: the two upper rays precede the lower ray.
    assert points[1][0]*points[2][1]-points[1][1]*points[2][0] > 0
    rotation = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0]}
    current, visited, outer = (0, 1), set(), []
    while current not in visited:
        visited.add(current)
        a, b = current
        outer.append(a)
        around = rotation[b]
        current = b, around[(around.index(a)-1) % len(around)]
    assert current == (0, 1)
    assert visited == {(a, b) for a, b in contacts} | {(b, a) for a, b in contacts}
    occurrences = Counter(outer)
    assert occurrences[0] == 3
    assert all(occurrences[a] == 1 for a in (1, 2, 3))
    for a in (1, 2, 3):
        # Deleting any leaf leaves the center joined to every remaining vertex.
        assert set(rotation[0])-{a} == {1, 2, 3}-{a}
    augmented = {a: set(ns) for a, ns in rotation.items()}
    for a, b in ((1, 2), (2, 3), (3, 1)):
        augmented[a].add(b)
        augmented[b].add(a)
    pockets = face_walks(points, augmented)
    assert len(pockets) == 3 and all(len(p) == 3 for p in pockets)
    print("PASS: six rational source pairs and positive equilibrium; each leaf occurs once")
    print("PASS: six directed bridge incidences and three triangular augmented pockets")
    print("SCOPE: finite witness; no general graph theorem or global-optimality certificate")


if __name__ == "__main__":
    main()
