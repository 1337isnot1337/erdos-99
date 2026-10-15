#!/usr/bin/env python3
"""Exact crossing-train versus independent-owner scope regression."""
from fractions import Fraction as F
from itertools import combinations, product
import json


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def squared(a):
    return dot(a, a)


def main():
    cosine, sine = F(999999, 1000001), F(2000, 1000001)
    assert cosine * cosine + sine * sine == 1

    def rotate(p):
        return cosine * p[0] - sine * p[1], sine * p[0] + cosine * p[1]

    u, w, zero = (F(1), F(0)), (F(5, 13), F(12, 13)), (F(0), F(0))
    ru, rw = rotate(u), rotate(w)
    du, dw = sub(ru, u), sub(rw, w)
    cloud = [du, dw, add(du, dw)]
    assert all(squared(d) < F(1, 100) ** 2 for d in cloud)
    assert all(dot(a, b) > 0 for a, b in combinations(cloud, 2))
    original = [zero, u, w, add(u, w)]
    contacts = {(0, 1), (0, 2), (1, 3), (2, 3)}
    assert squared(sub(u, w)) == F(16, 13)
    assert squared(add(u, w)) == F(36, 13)
    train_pairs = 0
    for a, b in product(range(2), repeat=2):
        ua, wb = (u, ru)[a], (w, rw)[b]
        points = [zero, ua, wb, add(ua, wb)]
        for i, j in combinations(range(4), 2):
            distance = squared(sub(points[i], points[j]))
            if (i, j) in contacts:
                assert distance == 1
            else:
                assert distance > 1
            train_pairs += 1
    owner_pairs = 0
    preserved = []
    for state in product(range(2), repeat=3):
        points = [zero] + [add(original[j + 1], cloud[j]) if state[j]
                           else original[j + 1] for j in range(3)]
        contact_valid = True
        for i, j in combinations(range(4), 2):
            distance = squared(sub(points[i], points[j]))
            if (i, j) in contacts and distance != 1:
                contact_valid = False
            owner_pairs += 1
        if contact_valid:
            preserved.append(state)
    # Selecting u independently leaves u+w fixed and shortens their contact.
    violation = squared(sub(add(u, du), add(u, w))) - 1
    assert violation < 0
    assert (1, 0, 0) not in preserved
    assert preserved == [(0, 0, 0), (1, 1, 1)]
    print(json.dumps({'classification': 'exact finite scope regression',
                      'train_pair_checks': train_pairs, 'owner_pair_checks': owner_pairs,
                      'contact_preserving_owner_states': preserved,
                      'failed_owner_contact_squared_excess': str(violation),
                      'omitted': ['canonical KKT', 'beneficial old-diameter state',
                                  'global optimality']}, sort_keys=True))


if __name__ == '__main__':
    main()
