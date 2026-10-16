#!/usr/bin/env python3
"""Exact finite regression; no global-optimality or Level I certificate."""

from fractions import Fraction as F
from itertools import combinations
import json


def difference(p, q):
    return tuple(a - b for a, b in zip(p, q))


def norm2(p):
    return sum(a * a for a in p)


def pair_ledger(points):
    return {(i, j): norm2(difference(points[i], points[j]))
            for i, j in combinations(range(len(points)), 2)}


def has_triangle(contacts, size):
    return any(all(tuple(sorted(edge)) in contacts
                   for edge in combinations(triple, 2))
               for triple in combinations(range(size), 3))


def check_square(m):
    points = [(F(i), F(j)) for i in range(m) for j in range(m)]
    ledger = pair_ledger(points)
    d2 = 2 * (m - 1) ** 2
    contacts = {e for e, length in ledger.items() if length == 1}
    diameters = {e for e, length in ledger.items() if length == d2}
    assert min(ledger.values()) == 1 and max(ledger.values()) == d2
    assert not has_triangle(contacts, len(points))
    assert len(diameters) == 2
    perimeter = {}
    for edge in contacts:
        p, q = (points[i] for i in edge)
        if ((p[0] == q[0] and p[0] in (0, m - 1))
                or (p[1] == q[1] and p[1] in (0, m - 1))):
            perimeter[edge] = F(m - 1, 2)
    assert len(perimeter) == 4 * (m - 1)
    beta = dict.fromkeys(diameters, F(1, 2))
    assert sum(perimeter.values()) == d2
    assert sum(beta.values()) == 1
    residual = [[F(0), F(0)] for _ in points]
    tensor = [[F(0), F(0)], [F(0), F(0)]]
    for stress, sign in ((perimeter, 1), (beta, -1)):
        for (i, j), weight in stress.items():
            r = difference(points[i], points[j])
            for a in range(2):
                residual[i][a] += sign * weight * r[a]
                residual[j][a] -= sign * weight * r[a]
                for b in range(2):
                    tensor[a][b] += sign * weight * r[a] * r[b]
    assert all(value == 0 for row in residual for value in row)
    assert all(value == 0 for row in tensor for value in row)
    return ledger


def main():
    old_ledger = check_square(3)
    labels = [(0, 0), (1, 0), (0, 1), (-1, 1), (-1, 0),
              (0, -1), (1, -1), (1, 1), (2, -1)]
    points = [(F(a) + F(8, 17) * b, F(15, 17) * b)
              for a, b in labels]
    assert len(set(points)) == 9
    ledger = pair_ledger(points)
    contacts = {e for e, length in ledger.items() if length == 1}
    assert min(ledger.values()) == 1
    assert max(ledger.values()) == F(125, 17)
    assert not has_triangle(contacts, 9)
    for i, j in contacts:
        r = difference(labels[i], labels[j])
        assert r in ((1, 0), (-1, 0), (0, 1), (0, -1))
        assert (sum(labels[i]) - sum(labels[j])) % 2 == 1
    margin = max(old_ledger.values()) - max(ledger.values())
    assert margin == F(11, 17)
    for m in (4, 5, 8):
        check_square(m)
    # sqrt(3)<26/15 and pi>31/10 give 2sqrt(3)/pi<104/93.
    # (104/93)*16 < 18 establishes the comparator inequality at m=4.
    assert F(26, 15) ** 2 > 3
    assert F(2449, 1000) ** 2 < 6
    assert F(1415, 1000) ** 2 > 2
    assert 3 * F(2449 - 1415, 1000) > F(31, 10)
    assert F(104, 93) * 16 < 18
    assert F(9, 8) > F(104, 93)

    # At angle pi/3 the squared distance between integer lattice labels is
    # a^2+ab+b^2, so no irrational coordinates need be approximated.
    def triangular_ledger(packet):
        return {(i, j): (r[0] ** 2 + r[0] * r[1] + r[1] ** 2)
                for i, j in combinations(range(len(packet)), 2)
                for r in [difference(packet[i], packet[j])]}

    inner = labels[:7]
    outer = [(1, 1), (-1, 2), (-2, 1), (-1, -1), (1, -2), (2, -1)]
    six = triangular_ledger(inner[:6])
    twelve = triangular_ledger((inner + outer)[:12])
    assert len(six) == 15 and min(six.values()) >= 1 and max(six.values()) == 4
    assert (len(twelve) == 66 and min(twelve.values()) >= 1
            and max(twelve.values()) == 12)
    special = {6: max(six.values()), 9: max(ledger.values()),
               12: max(twelve.values())}
    finite_factorizations = 0
    for n in range(5, 16):
        for m in range(1, n + 1):
            if n % m:
                continue
            k = n // m
            lower_bound = (m - 1) ** 2 + (k - 1) ** 2
            competitor_bound = special.get(n, F(104, 93) * n)
            assert competitor_bound < lower_bound, (n, m, k)
            finite_factorizations += 1
    print(json.dumps({"status": "PASS", "arithmetic": "rational",
                      "old_pairs": len(old_ledger), "new_pairs": len(ledger),
                      "new_contact_edges": len(contacts),
                      "new_diameter_squared": str(max(ledger.values())),
                      "squared_diameter_margin": str(margin),
                      "square_kkt_sizes": [3, 4, 5, 8],
                      "product_factorizations_checked": finite_factorizations,
                      "exceptional_competitor_pairs": len(six) + len(twelve),
                      "uniform_product_exclusion_threshold": 5,
                      "global_optimality_certified": False,
                      "level_i_resolved": False}, sort_keys=True))


if __name__ == "__main__":
    main()
