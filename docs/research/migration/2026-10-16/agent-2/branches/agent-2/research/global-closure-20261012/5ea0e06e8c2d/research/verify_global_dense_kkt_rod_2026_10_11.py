#!/usr/bin/env python3
"""Exact full-pair nonlinear competitor; no optimal-minimizer certificate."""

from fractions import Fraction as F
from itertools import combinations
import json


def difference(p, q):
    return tuple(a - b for a, b in zip(p, q))


def norm2(p):
    return sum(a * a for a in p)


def dot(p, q):
    return sum(a * b for a, b in zip(p, q))


def ledger(points):
    return {(i, j): norm2(difference(points[i], points[j]))
            for i, j in combinations(range(len(points)), 2)}


def main():
    labels = [(0, 0), (1, 0), (0, 1), (-1, 1), (-1, 0),
              (0, -1), (1, -1), (1, 1), (2, -1), (-2, 0), (2, 0)]
    u, v = (F(1), F(0)), (F(8, 17), F(15, 17))
    points = [(F(a) + v[0] * b, v[1] * b) for a, b in labels]
    old = ledger(points)
    assert len(set(points)) == 11 and len(old) == 55
    assert min(old.values()) == 1 and max(old.values()) == 16
    contacts = {e for e, length in old.items() if length == 1}
    ends = tuple(sorted((labels.index((-2, 0)), labels.index((2, 0)))))
    assert {e for e, length in old.items() if length == 16} == {ends}
    for i, j in contacts:
        assert difference(labels[i], labels[j]) in (
            (1, 0), (-1, 0), (0, 1), (0, -1))
        assert (sum(labels[i]) - sum(labels[j])) % 2 == 1
    rod = {tuple(sorted((labels.index((a, 0)), labels.index((a + 1, 0)))))
           for a in range(-2, 2)}
    assert rod <= contacts
    alpha, beta = dict.fromkeys(rod, F(4)), {ends: F(1)}
    assert sum(alpha.values()) == 16 and sum(beta.values()) == 1
    residual = [[F(0), F(0)] for _ in points]
    tensor = [[F(0), F(0)], [F(0), F(0)]]
    for weights, sign in ((alpha, 1), (beta, -1)):
        for (i, j), weight in weights.items():
            r = difference(points[i], points[j])
            for a in range(2):
                residual[i][a] += sign * weight * r[a]
                residual[j][a] -= sign * weight * r[a]
                for b in range(2):
                    tensor[a][b] += sign * weight * r[a] * r[b]
    assert all(value == 0 for row in residual for value in row)
    assert all(value == 0 for row in tensor for value in row)

    velocities = [(F(b), (F(a * a - 4) - v[0] * b) / v[1])
                  for a, b in labels]
    assert all(velocities[i] == (0, 0) for i in ends)
    for i, (a, b) in enumerate(labels):
        assert dot(u, velocities[i]) == b
        assert dot(v, velocities[i]) == a * a - 4
    for i, j in contacts:
        r = difference(points[i], points[j])
        dv = difference(velocities[i], velocities[j])
        assert dot(r, dv) == 0 and norm2(dv) > 0
    t, contraction = F(1, 1000), F(9999999, 10000000)
    moved = [tuple(p[a] + t * velocity[a] for a in range(2))
             for p, velocity in zip(points, velocities)]
    moved_ledger = ledger(moved)
    assert min(moved_ledger.values()) > 1
    assert {e for e, length in moved_ledger.items() if length == 16} == {ends}
    assert max(moved_ledger.values()) == 16
    for i, j in contacts:
        assert moved_ledger[i, j] == 1 + t * t * norm2(
            difference(velocities[i], velocities[j]))
    final = [tuple(contraction * coordinate for coordinate in p) for p in moved]
    final_ledger = ledger(final)
    assert len(set(final)) == 11
    assert min(final_ledger.values()) > 1
    assert max(final_ledger.values()) < 16
    print(json.dumps({"status": "PASS", "arithmetic": "rational",
                      "labels_retained": len(final), "pairs_each_stage": len(old),
                      "old_diameter_squared": "16",
                      "final_min_separation_squared": str(min(final_ledger.values())),
                      "final_diameter_squared": str(max(final_ledger.values())),
                      "old_unit_contacts_opened": len(contacts),
                      "global_optimality_certified": False,
                      "asymptotic_theorem_certified_by_finite_script": False,
                      "level_i_resolved": False}, sort_keys=True))


if __name__ == "__main__":
    main()
