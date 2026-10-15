#!/usr/bin/env python3
"""Exact common-angle closure and full-pair endpoint scope certificates.

A physical unit hexagon has a zero-valid non-Horn train-selection relation.
Its alternating selection has a full six-point strict competitor. A retained
contact isolate makes that same endpoint lengthen the actual global diameter.
Neither source is claimed canonical or globally optimal.
"""
from fractions import Fraction as F
from itertools import combinations, product
import json


def q(a=0, b=0):
    return F(a), F(b)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[0], -a[1]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return a[0] * b[0] + 3 * a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def scale(a, b):
    return a[0] * b, a[1] * b


def sign(a):
    if not a[1]:
        return (a[0] > 0) - (a[0] < 0)
    if not a[0]:
        return (a[1] > 0) - (a[1] < 0)
    if (a[0] > 0) == (a[1] > 0):
        return 1 if a[0] > 0 else -1
    gap = a[0] ** 2 - 3 * a[1] ** 2
    assert gap
    return ((a[0] > 0) - (a[0] < 0)) * (1 if gap > 0 else -1)


ZERO = (q(), q())


def p_add(a, b):
    return add(a[0], b[0]), add(a[1], b[1])


def p_sub(a, b):
    return sub(a[0], b[0]), sub(a[1], b[1])


def dot(a, b):
    return add(mul(a[0], b[0]), mul(a[1], b[1]))


def squared(a):
    return dot(a, a)


def turn(a):
    return neg(a[1]), a[0]


def rotate(a, t):
    c, s = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
    assert c * c + s * s == 1
    return sub(scale(a[0], c), scale(a[1], s)), add(scale(a[0], s), scale(a[1], c))


def potentials(edges, state):
    positions, selected = [ZERO], [ZERO]
    for e, bit in zip(edges[:-1], state[:-1]):
        positions.append(p_add(positions[-1], e))
        selected.append(p_add(selected[-1], e if bit else ZERO))
    return positions, selected


def endpoint(positions, selected, t):
    return [p_add(p, p_sub(rotate(y, t), y)) for p, y in zip(positions, selected)]


def main():
    edges = [(q(1), q()), (q(F(1, 2)), q(0, F(1, 2))),
             (q(F(-1, 2)), q(0, F(1, 2))), (q(-1), q()),
             (q(F(-1, 2)), q(0, F(-1, 2))), (q(F(1, 2)), q(0, F(-1, 2)))]
    valid = []
    for state in product(range(2), repeat=6):
        total = ZERO
        for e, bit in zip(edges, state):
            if bit:
                total = p_add(total, e)
        if total == ZERO:
            valid.append(state)
    assert len(valid) == 10
    pair = (1, 0, 0, 1, 0, 0)
    triple = (1, 0, 1, 0, 1, 0)
    meet = tuple(a & b for a, b in zip(pair, triple))
    assert pair in valid and triple in valid and meet not in valid
    source, selected = potentials(edges, triple)
    contacts = {tuple(sorted((i, (i + 1) % 6))) for i in range(6)}
    diameters = {(0, 3), (1, 4), (2, 5)}
    for i, j in combinations(range(6), 2):
        distance = squared(p_sub(source[i], source[j]))
        assert distance == q(1) if (i, j) in contacts else sign(sub(distance, q(1))) > 0
        assert distance == q(4) if (i, j) in diameters else sign(sub(distance, q(4))) < 0
    isolated = (q(-4), q())
    seven_source = source + [isolated]
    assert all(sign(sub(squared(p_sub(isolated, p)), q(1))) > 0 for p in source)
    assert squared(p_sub(source[2], isolated)) == q(31)
    assert all(sign(sub(squared(p_sub(seven_source[i], seven_source[j])), q(31))) < 0
               for i, j in combinations(range(7), 2) if (i, j) != (2, 6))
    formula_checks, lower_checks = 0, 0
    for state in valid:
        _, y = potentials(edges, state)
        seven_y = y + [ZERO]  # Retain the isolate at its original coordinate.
        for t in (F(1, 10), F(-1, 10)):
            points = endpoint(seven_source, seven_y, t)
            for i, j in combinations(range(7), 2):
                r = p_sub(seven_source[i], seven_source[j])
                s = p_sub(seven_y[i], seven_y[j])
                aa, bb = dot(p_sub(r, s), s), dot(r, turn(s))
                predicted = scale(sub(bb, scale(aa, t)), 4 * t / (1 + t * t))
                actual = sub(squared(p_sub(points[i], points[j])), squared(r))
                assert predicted == actual
                formula_checks += 1
                if j < 6:
                    distance = squared(p_sub(points[i], points[j]))
                    assert distance == q(1) if (i, j) in contacts else sign(sub(distance, q(1))) > 0
                    lower_checks += 1
    t = F(1, 10)
    six_target = endpoint(source, selected, t)
    for i, j in combinations(range(6), 2):
        assert sign(sub(squared(p_sub(six_target[i], six_target[j])), q(4))) < 0
    seven_target = endpoint(seven_source, selected + [ZERO], t)
    failed_excess = sub(squared(p_sub(seven_target[2], seven_target[6])), q(31))
    assert failed_excess == q(F(-18, 101), F(20, 101))
    assert sign(failed_excess) > 0
    print(json.dumps({
        'classification': 'finite closure and endpoint scope certificates',
        'hexagon_boolean_patterns': 64, 'closed_patterns': len(valid),
        'horn_meet_failure': {'first': pair, 'second': triple, 'meet': meet},
        'full_pair_quadratic_identity_checks': formula_checks,
        'contact_and_inactive_lower_checks': lower_checks,
        'six_point_strict_competitor_pair_checks': 15,
        'retained_contact_isolate': True,
        'isolate_actual_diameter_squared_increase': '(20 sqrt(3)-18)/101',
        'omitted': ['canonical-source mixed rigidity', 'global optimality',
                    'beneficial pattern for every canonical source']
    }, sort_keys=True))


if __name__ == '__main__':
    main()
