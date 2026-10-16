#!/usr/bin/env python3
"""Rational threshold certificate and bounded lattice-circle example audit.

The threshold arithmetic is exact. Small circle counts are only examples,
not a certificate of the general circle lemma or of global optimality.
"""

from collections import defaultdict
from fractions import Fraction as F
from functools import cmp_to_key


def arctan_bounds(x, terms=25):
    partial = sum((-1)**k * x**(2*k+1)/F(2*k+1) for k in range(terms))
    next_term = (-1)**terms * x**(2*terms+1)/F(2*terms+1)
    return min(partial, partial+next_term), max(partial, partial+next_term)


def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]


def direction_compare(a, b):
    ha = 0 if a[1] > 0 or (a[1] == 0 and a[0] > 0) else 1
    hb = 0 if b[1] > 0 or (b[1] == 0 and b[0] > 0) else 1
    if ha != hb:
        return -1 if ha < hb else 1
    determinant = cross(a, b)
    return -1 if determinant > 0 else (1 if determinant < 0 else 0)


def main():
    alo, ahi = arctan_bounds(F(1, 5))
    blo, bhi = arctan_bounds(F(1, 239))
    pi_lo, pi_hi = F(314159, 100000), F(3927, 1250)
    assert pi_lo < 16*alo-4*bhi < 16*ahi-4*blo < pi_hi
    sqrt3_lo = F(34641, 20000)
    assert sqrt3_lo**2 < 3
    assert 128*pi_hi**3/sqrt3_lo < 2292
    assert 4585**2+1 == 21022226
    print("PASS exact Machin/square certificate: "
          "128*pi^3/sqrt(3) < 2292; n threshold 21022226")
    samples = triples = 0
    # Enumerate complete circles of radius <= 12. Since covolume is
    # >= 12/13, indices outside [-16,16] cannot meet these circles:
    # |i|,|j| <= D/sin(theta) <= 13 when D <= 12.
    for cosine, sine in ((F(0), F(1)), (F(5, 13), F(12, 13))):
        groups = defaultdict(list)
        for i in range(-16, 17):
            for j in range(-16, 17):
                point = (F(i)+j*cosine, j*sine)
                radius2 = point[0]**2+point[1]**2
                if 0 < radius2 <= 144:
                    groups[radius2].append(point)
        for radius2, points in groups.items():
            count = len(points)
            # Cubed version of M <= 2*pi*s^(-1/3)*D^(2/3),
            # checked even with the rigorous lower bound on pi.
            assert count**3*sine <= 8*pi_lo**3*radius2
            ordered = sorted(points, key=cmp_to_key(direction_compare))
            if count >= 3:
                for k, a in enumerate(ordered):
                    b, c = ordered[(k+1) % count], ordered[(k+2) % count]
                    determinant = cross((b[0]-a[0], b[1]-a[1]),
                                        (c[0]-a[0], c[1]-a[1]))
                    assert determinant != 0
                    quotient = abs(determinant)/sine
                    assert quotient.denominator == 1 and quotient >= 1
                    triples += 1
            samples += 1
    print(f"PASS {samples} complete small lattice circles and {triples} "
          "consecutive triple determinant checks")
    print("Universal circle and deformation proofs are analytic in the reports.")


if __name__ == "__main__":
    main()
