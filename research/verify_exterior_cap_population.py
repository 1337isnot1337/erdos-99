#!/usr/bin/env python3
"""Certify rectangle site-count lower bounds in the analytic cap regression.

This bounded rational computation certifies dimensions/cardinalities only.
The report analytically proves full-source separation, diameter and loading.
It does not certify global optimality or a full-core survivor.
"""

from fractions import Fraction as F

from verify_target_c_two_halfdisk_scalar_regression import arctan_bounds


def main():
    def multiply(a, b):
        # Pairs represent rational a_0+a_1 sqrt(3), exactly.
        return a[0]*b[0]+3*a[1]*b[1], a[0]*b[1]+a[1]*b[0]

    coefficient = F(3, 2), F(1, 2)
    cube = multiply(multiply(coefficient, coefficient), coefficient)
    assert tuple(value/9 for value in cube) == (F(3, 4), F(5, 12))
    assert multiply(coefficient, (F(1, 2), F(1, 3))) == (F(5, 4), F(3, 4))
    lo5, hi5 = arctan_bounds(F(1, 5))
    lo239, hi239 = arctan_bounds(F(1, 239))
    pi_lo, pi_hi = F(314159, 100000), F(314160, 100000)
    assert pi_lo < 16*lo5-4*hi239
    assert 16*hi5-4*lo239 < pi_hi
    for power in (3, 4):
        for p in (9, 21, 51, 101):
            diameter = p**power
            angle_lo, angle_hi = pi_lo/(2*p), pi_hi/(2*p)
            assert 0 < angle_lo < angle_hi < F(1, 5)
            # sin(theta) >= sin(angle_lo) >= angle_lo-angle_lo^3/6.
            chord_lo = 2*diameter*(angle_lo-angle_lo**3/6)
            depth_lo = 3*chord_lo**2/(32*diameter)
            assert chord_lo > 0 and depth_lo > 4
            columns = chord_lo // 4
            rows = (depth_lo-4) // 2 + 1
            assert columns >= 1 and rows >= 1
            # Coordinates 2i-(columns-1), and outward depths 2+2j.
            assert columns-1 <= chord_lo/4
            assert 2+2*(rows-1) <= depth_lo-2
            count = columns*rows
            print(f"PASS: p={p}, D=p^{power}, certified exterior sites >= {count}")
    print("Rational dimension/cardinality bounds only; geometric claims are analytic.")


if __name__ == '__main__':
    main()
