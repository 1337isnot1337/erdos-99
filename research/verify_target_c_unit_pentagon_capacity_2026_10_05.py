#!/usr/bin/env python3
"""Exact supporting algebra for the universal convex unit-pentagon report.

Checks a distance identity, rational Oler margin and a sharp boundary packet.
The universal perimeter/uniqueness proof is analytic, not a finite search.
No global optimality, source extraction or Level I conclusion is certified.
"""
from fractions import Fraction as F


def add(p, q):
    result = dict(p)
    for key, value in q.items():
        result[key] = result.get(key, F(0)) + value
    return {key: value for key, value in result.items() if value}


def mul(p, q):
    result = {}
    for i, a in p.items():
        for j, b in q.items():
            key = tuple(x + y for x, y in zip(i, j))
            result[key] = result.get(key, F(0)) + a*b
    return {key: value for key, value in result.items() if value}


def scale(p, a):
    return {key: a*value for key, value in p.items() if a*value}


def qadd(x, y):
    return x[0]+y[0], x[1]+y[1]


def qmul(x, y):
    return x[0]*y[0]+3*x[1]*y[1], x[0]*y[1]+x[1]*y[0]


def qneg(x):
    return -x[0], -x[1]


def distance_sq(p, q):
    delta = [qadd(x, qneg(y)) for x, y in zip(p, q)]
    return qadd(qmul(delta[0], delta[0]), qmul(delta[1], delta[1]))


def main():
    one = {(0, 0, 0): F(1)}
    r = {(1, 0, 0): F(1)}
    s = {(0, 1, 0): F(1)}
    c = {(0, 0, 1): F(1)}
    lhs = add(add(mul(r, r), mul(s, s)), scale(mul(mul(r, s), c), -2))
    lhs = add(lhs, scale(add(one, scale(c, -1)), -2))
    r_minus_s = add(r, scale(s, -1))
    rhs = add(mul(r_minus_s, r_minus_s),
              scale(mul(add(one, scale(c, -1)),
                        add(mul(r, s), scale(one, -1))), 2))
    assert lhs == rhs
    oler_bound = F(25, 18)+F(5, 2)+1
    assert oler_bound == F(44, 9)
    assert 5-oler_bound == F(1, 9)
    chord = lambda angle_over_pi: F(1, 2)+F(3, 2)*angle_over_pi
    assert chord(F(1, 3)) == 1 and chord(F(1)) == 2

    zero, unit, half, root_half = (F(0), F(0)), (F(1), F(0)), (F(1, 2), F(0)), (F(0), F(1, 2))
    vertices = [(qneg(unit), zero), (unit, zero), (half, root_half),
                (qneg(half), root_half)]
    packet = vertices + [(zero, zero)]
    for i, point in enumerate(packet):
        for other in packet[i+1:]:
            squared = distance_sq(point, other)
            assert squared[1] == 0 and squared[0] >= 1
    edge_squares = [distance_sq(vertices[i], vertices[(i+1) % 4]) for i in range(4)]
    assert edge_squares == [(F(4), F(0)), (F(1), F(0)), (F(1), F(0)), (F(1), F(0))]
    print("PASS: exact radial identity; Oler margin 1/9; chord endpoints; "
          "10 lower pairs and four edges of the sharp quadrilateral-hull packet.")


if __name__ == "__main__":
    main()
