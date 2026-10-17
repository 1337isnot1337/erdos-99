#!/usr/bin/env python3
"""Exact finite isolate activations; stress support is not physical contact support."""

from fractions import Fraction as F
from itertools import combinations
from math import isqrt

from verify_periodic_release_diameter_transfer import rank


def d2(p, q):
    return sum((a - b) * (a - b) for a, b in zip(p, q))


def ledger(points, diameter_sq):
    contacts, diameters = set(), set()
    count = 0
    for i, j in combinations(range(len(points)), 2):
        squared = d2(points[i], points[j])
        assert 1 <= squared <= diameter_sq
        if squared == 1:
            contacts.add((i, j))
        if squared == diameter_sq:
            diameters.add((i, j))
        count += 1
    return contacts, diameters, count


def rigidity(points, edges):
    rows = []
    for i, j in sorted(edges):
        row = [F(0)] * (2 * len(points))
        for axis in range(2):
            delta = points[i][axis] - points[j][axis]
            row[2 * i + axis] = delta
            row[2 * j + axis] = -delta
        rows.append(row)
    return rows


def psd_rank(matrix):
    a = [list(map(F, row)) for row in matrix]
    answer = 0
    while a:
        assert all(a[i][i] >= 0 for i in range(len(a)))
        pivot = next((i for i in range(len(a)) if a[i][i] > 0), None)
        if pivot is None:
            assert all(x == 0 for row in a for x in row)
            break
        indices = [i for i in range(len(a)) if i != pivot]
        a = [[a[i][j] - a[i][pivot] * a[pivot][j] / a[pivot][pivot]
              for j in indices] for i in indices]
        answer += 1
    return answer


def check_square_forest(m):
    assert m >= 4 and m % 2 == 0
    wall = ([(i, 0) for i in range(m)] + [(m, j) for j in range(m)]
            + [(m - i, m) for i in range(m)] + [(0, m - j) for j in range(m)])
    width = m // 2 - 1
    tags = [(i, j) for j in range(1, width + 1) for i in range(1, width + 1)]
    points = wall + [(2 * i, 2 * j) for i, j in tags]
    old, old_diameters, total_pairs = ledger(points, 2 * m * m)
    assert len(old) == 4 * m and len(old_diameters) == 2
    assert all(i < 4 * m and j < 4 * m for i, j in old | old_diameters)
    old_rank = rank(rigidity(points, old | old_diameters))
    assert old_rank == 4 * m + 1
    contacts = old
    for offset, (i, j) in enumerate(tags):
        label = 4 * m + offset
        start = points[label]
        target = (i, 2 * j)
        points[label] = target
        updated, diameters, checks = ledger(points, 2 * m * m)
        total_pairs += checks
        assert contacts < updated and len(updated - contacts) == 1
        assert old_diameters == diameters
        assert all(d2(points[label], p) < 2 * m * m
                   for k, p in enumerate(points) if k != label)
        # The complete horizontal path stays separated: all its lower-distance
        # quadratics are nonnegative at their exact minimum on t in [0,1].
        velocity = (target[0] - start[0], target[1] - start[1])
        aa = sum(x * x for x in velocity)
        for k, p in enumerate(points):
            if k == label:
                continue
            delta = (start[0] - p[0], start[1] - p[1])
            bb = 2 * sum(a * b for a, b in zip(delta, velocity))
            cc = sum(x * x for x in delta) - 1
            t = max(F(0), min(F(1), F(-bb, 2 * aa)))
            minimum = aa * t * t + bb * t + cc
            assert minimum >= 0
            if minimum == 0:
                assert t == 1
                assert tuple(sorted((label, k))) in updated - contacts
        contacts = updated
    z = len(tags)
    assert len(contacts) == len(points)
    assert all(any(i == k or j == k for i, j in contacts) for k in range(len(points)))
    neighbors = {i: set() for i in range(len(points))}
    for i, j in contacts:
        neighbors[i].add(j)
        neighbors[j].add(i)
    assert all(not (neighbors[i] & neighbors[j]) for i, j in contacts)
    assert rank(rigidity(points, contacts | old_diameters)) == old_rank + z
    omega = [[F(0)] * len(points) for _ in points]
    for edges, coefficient in ((old, F(1)), (old_diameters, F(-1, m))):
        for i, j in edges:
            omega[i][i] += coefficient
            omega[j][j] += coefficient
            omega[i][j] -= coefficient
            omega[j][i] -= coefficient
    for vector in ([1] * len(points), [p[0] for p in points], [p[1] for p in points]):
        assert all(sum(a * b for a, b in zip(row, vector)) == 0 for row in omega)
    assert psd_rank(omega) == 4 * m - 3
    assert len(points) - (4 * m - 3) == z + 3
    assert all(x == 0 for row in omega[4 * m:] for x in row)
    # Leaf peeling forces every added edge coefficient to vanish, independently
    # of the particular original stress selected above.
    new_edges = contacts - old
    while new_edges:
        leaf = next(k for k in range(4 * m, len(points))
                    if sum(k in edge for edge in new_edges) == 1)
        new_edges = {edge for edge in new_edges if leaf not in edge}
    n = len(points)
    w = isqrt(n - 1) + 1
    h = (n + w - 1) // w
    assert (w - 1) * (w - 1) + (h - 1) * (h - 1) < 2 * m * m
    return z, total_pairs


def check_generic_first_hit():
    moving = (F(0), F(2))
    right, left, bottom = (F(1, 2), F(0)), (F(-1, 2), F(0)), (F(0), F(-3))
    endpoint = (F(1, 34), F(15, 17))
    assert d2(right, left) == 1
    assert d2(endpoint, right) == 1
    assert d2(endpoint, left) == F(18, 17) > 1
    assert 1 < d2(endpoint, bottom) < 25
    velocity = (endpoint[0] - moving[0], endpoint[1] - moving[1])
    aa = sum(x * x for x in velocity)
    for fixed in (right, left, bottom):
        delta = (moving[0] - fixed[0], moving[1] - fixed[1])
        bb = 2 * sum(a * b for a, b in zip(delta, velocity))
        cc = sum(x * x for x in delta) - 1
        t = max(F(0), min(F(1), -bb / (2 * aa)))
        assert aa * t * t + bb * t + cc >= 0
        if fixed == right:
            assert 2 * aa + bb < 0  # strictly decreasing through the first hit
        else:
            assert aa * t * t + bb * t + cc > 0
    # A point slightly beyond the first hit is inside the chosen neighbor's
    # disk and the interior upper lens, as required by the generic-target proof.
    target = tuple(a + F(101, 100) * b for a, b in zip(moving, velocity))
    assert d2(target, right) < 1
    assert all(d2(target, fixed) < 25 for fixed in (right, left, bottom))


def main():
    activations, pairs = 0, 0
    for m in (4, 6, 8, 12):
        z, checks = check_square_forest(m)
        activations += z
        pairs += checks
    check_generic_first_hit()
    print(f"PASS: four exact square-wall fixtures; {activations} activations; "
          f"{pairs} full-source pair checks")
    print("PASS: contact/diameter ledgers, finite paths, zero-stress forests, PSD/rank, "
          "rigidity increments, strict nonglobality, generic first-hit guard")
    print("Scope: global normalization proof is analytic; fixtures do not settle Level I")


if __name__ == "__main__":
    main()
