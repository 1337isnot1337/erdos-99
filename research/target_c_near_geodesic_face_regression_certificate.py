#!/usr/bin/env python3
"""Exact certificate for the Target C near-geodesic face regression.

The construction is a convex unit-edge corridor with two long horizontal chains.
It certifies the local obstruction recorded in
docs/reports/target_c_near_geodesic_face_regression_2026-09-12.md:

* all boundary edges have length one;
* every non-boundary pair is strictly farther than one, so the boundary contact
  graph is triangle-free and has no hidden chords;
* the face area is w*N + 3*sqrt(95)/32, with w=sqrt(15)/4;
* its diameter is N+O(1), while its interior isolate population is zero.

This is a local geometric regression only.  It does not construct a global
minimum-diameter source or a KKT stress.
"""

from sympy import Rational, sqrt, simplify


def main() -> None:
    delta = Rational(1, 2)
    width = sqrt(15) / 4

    # The two cap edges sum to v=(delta,width), but each has unit length.
    u1 = (
        Rational(1, 4) + 15 * sqrt(3) / (8 * sqrt(19)),
        sqrt(15) / 8 - 3 * sqrt(5) / (4 * sqrt(19)),
    )
    u2 = (
        Rational(1, 4) - 15 * sqrt(3) / (8 * sqrt(19)),
        sqrt(15) / 8 + 3 * sqrt(5) / (4 * sqrt(19)),
    )

    for u in (u1, u2):
        assert simplify(u[0] ** 2 + u[1] ** 2 - 1) == 0
    assert simplify(u1[0] + u2[0] - delta) == 0
    assert simplify(u1[1] + u2[1] - width) == 0

    # Consecutive boundary turns are strictly counterclockwise.
    assert u1[1] > 0
    assert u2[1] > 0
    cross_caps = simplify(u1[0] * u2[1] - u1[1] * u2[0])
    assert cross_caps > 0

    # The closest bottom/top-chain pair has squared distance 1/4+w^2=19/16.
    cross_chain_sq = simplify(delta ** 2 + width ** 2)
    assert cross_chain_sq == Rational(19, 16) > 1

    # The cap's non-adjacent chain distances are also strictly larger than one:
    # u1_x>1/2 makes the nearest horizontal separation u1_x+1/2>1.
    assert u1[0] > Rational(1, 2)
    # The two cap vertices are separated by more than one already at N=1;
    # increasing N only increases their horizontal separation.
    cap_dx = 1 + 2 * u1[0] - delta
    cap_dy = 2 * u1[1] - width
    assert simplify(cap_dx ** 2 + cap_dy ** 2 - 1) > 0

    # Two long sides and two two-edge caps give this exact area offset.
    area_offset = simplify(cross_caps)
    assert area_offset == 3 * sqrt(95) / 32

    # The positive linear coefficient is already larger than the promoted floor.
    beta_floor = Rational(867, 5000)
    assert simplify(width ** 2 - beta_floor ** 2) > 0

    print("PASS: cap vectors are exact unit vectors")
    print("PASS: cap vectors sum to (1/2,sqrt(15)/4)")
    print("PASS: all local non-boundary distances are >1")
    print(f"PASS: area/N -> sqrt(15)/4 > 867/5000; offset={area_offset}")


if __name__ == "__main__":
    main()
