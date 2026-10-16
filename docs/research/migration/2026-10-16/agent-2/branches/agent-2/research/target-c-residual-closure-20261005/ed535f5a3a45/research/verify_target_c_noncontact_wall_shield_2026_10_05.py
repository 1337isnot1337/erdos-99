#!/usr/bin/env python3
"""Exact finite checks for the noncontact-wall shield candidate.

Analytic statements are in the associated report. These rational examples
certify a sharpness regression and finite identities, not canonical-source
realizability, universal shielding by enumeration, motion, or optimality.
"""
from fractions import Fraction as F
from itertools import combinations


def distance2(p, q):
    return sum((a-b)**2 for a, b in zip(p, q))


def point(x, y):
    return F(x), F(y)


def main():
    wall = [point(F(-7, 8), 0), point(F(7, 8), 0),
            point(F(7, 8), F(-3, 2)), point(F(-7, 8), F(-3, 2))]
    old = point(0, F(49, 100))
    new = point(0, F(-49, 100))
    source = wall + [old]
    assert all(distance2(p, q) >= 1 for p, q in combinations(source, 2))
    assert all(distance2(new, p) > 1 for p in wall)
    assert max(distance2(wall[i], wall[(i+1) % 4]) for i in range(4)) == F(49, 16)
    assert min(distance2(new, p) for p in wall) == F(40229, 40000)
    assert min(distance2(old, p) for p in wall) == F(40229, 40000)
    assert distance2(new, old) == F(2401, 2500) < 1
    # Coordinate signs put new inside and old outside this axis-aligned rectangle.
    assert F(-3, 2) < new[1] < 0 < old[1]
    assert F(49, 16) > 3

    # A source polygon with four noncontact edges <= sqrt(3) can have capacity.
    square = [point(F(-3, 4), F(-3, 4)), point(F(3, 4), F(-3, 4)),
              point(F(3, 4), F(3, 4)), point(F(-3, 4), F(3, 4))]
    center = point(0, 0)
    assert all(distance2(p, q) >= 1 for p, q in combinations(square, 2))
    assert all(distance2(center, p) == F(9, 8) > 1 for p in square)
    assert all(distance2(square[i], square[(i+1) % 4]) == F(9, 4) < 3
               for i in range(4))

    identities = 0
    for numerator in range(1, 17):
        t = F(numerator, 17)
        for width in [F(1), F(6, 5), F(3, 2), F(12, 7), F(7, 4)]:
            a, b = point(0, 0), point(width, 0)
            z = point(t*width, 0)
            for x in [point(F(1, 3), F(7, 5)), point(F(-2, 5), F(-3, 2))]:
                rhs = (1-t)*distance2(x, a) + t*distance2(x, b) - t*(1-t)*distance2(a, b)
                assert distance2(x, z) == rhs
                assert t*(1-t) <= F(1, 4)
                identities += 1
    print(f'PASS: sharpness source and cross-pair regression; four-edge capacity packet; {identities} exact weighted-square identities')
    print('No global minimizer, contact-breaking motion, universal theorem by enumeration, or Level I closure is certified.')


if __name__ == '__main__':
    main()
