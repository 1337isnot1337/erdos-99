#!/usr/bin/env python3
"""Exact adversarial certificates for the convex-bank train-capacity packet.

This is not a certificate of the geometric bank theorem or global optimality.
It certifies its unstressed-grid regression, the absence of a positive force
floor at a strictly turning bank, the opposed-order finite obstruction, and
the conservative rational constant in the human proof. Only Fraction/integer
arithmetic is used. Run from the repository root; no third-party packages.
"""

from fractions import Fraction as F
from itertools import combinations, product


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(c, a):
    return c * a[0], c * a[1]


def norm2(a):
    return a[0] * a[0] + a[1] * a[1]


def distance2(a, b):
    return norm2((a[0] - b[0], a[1] - b[1]))


def certify_unstressed_grid():
    u, v = (F(1), F(0)), (F(5, 13), F(12, 13))
    side = 4
    pts = {(i, j): add(scale(i, u), scale(j, v))
           for i in range(side + 1) for j in range(side + 1)}
    contacts = set()
    checked = 0
    for ij, kl in combinations(pts, 2):
        sq = distance2(pts[ij], pts[kl])
        assert sq >= 1
        di, dj = ij[0] - kl[0], ij[1] - kl[1]
        assert sq == F(di * di + dj * dj) + F(10, 13) * di * dj
        if di and dj:
            # This proves all off-axis pairs strict, rather than rounding them.
            assert sq >= F(8, 13) * (di * di + dj * dj) >= F(16, 13)
        if sq == 1:
            assert abs(di) + abs(dj) == 1
            contacts.add(frozenset((ij, kl)))
        checked += 1
    assert checked == 300 and len(contacts) == 40
    for tri in combinations(pts, 3):
        assert not all(frozenset(pair) in contacts for pair in combinations(tri, 2))
    assert norm2(u) == norm2(v) == 1
    assert distance2(u, v) == F(16, 13) > 1
    assert norm2(add(u, v)) == F(36, 13) > 1
    # The four u-trains have distinct, disjoint centerlines, and all have ends
    # on the same two flat banks. Their end midpoints are actual unit-edge mids.
    for i in range(side):
        bottom = scale(F(2 * i + 1, 2), u)
        top = add(bottom, scale(side, v))
        assert top[1] - bottom[1] == F(48, 13)
        assert distance2(bottom, top) == 16
    # At a non-corner bottom vertex the three contact neighbors have directions
    # -u, u, v. Positive equilibrium is impossible: only v has nonzero y.
    x = pts[(2, 0)]
    neighbors = [pts[(1, 0)], pts[(3, 0)], pts[(2, 1)]]
    ys = [q[1] - x[1] for q in neighbors]
    assert ys == [0, 0, F(12, 13)]
    print("PASS: 25-point unstressed grid; 300 exact pair distances; 40 contacts;")
    print("      four trains share two banks, but flat-bank equilibrium fails.")


def certify_small_positive_turn():
    u, v, origin = (F(1), F(0)), (F(5, 13), F(12, 13)), (F(0), F(0))
    for n in (2, 3, 10, 100, 10000, 1000000):
        t = F(1, n)
        c, s = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
        outgoing = c, -s
        incoming_neighbor = scale(-1, u)
        alpha, beta, gamma = c + F(5, 12) * s, F(1), F(13, 12) * s
        assert alpha > 0 and beta > 0 and gamma > 0
        force = add(add(scale(alpha, incoming_neighbor), scale(beta, outgoing)),
                    scale(gamma, v))
        assert force == (0, 0)
        pts = [origin, incoming_neighbor, outgoing, v]
        assert all(distance2(a, b) >= 1 for a, b in combinations(pts, 2))
        assert all(distance2(a, b) > 1 for a, b in combinations(pts[1:], 2))
        assert norm2(outgoing) == 1
        # Strict clockwise bank turn; no positive lower bound on transverse mass.
        assert outgoing[1] < 0
        assert gamma < F(13, 6 * n)
    print("PASS: six rational unit force stars, through turn parameter 1/1000000;")
    print("      strictly positive transverse force has no uniform lower bound.")


def certify_opposed_order():
    checked = 0
    for k in range(2, 9):
        # Bank 1's boundary order is fixed. Noncrossing forces the reverse order
        # on bank 2. Subtracting the opposite pi orientation offset leaves the
        # same phase labels. Equal phases are included as a hostile case.
        for phases in product(range(3), repeat=k):
            bank1_strict = all(a > b for a, b in zip(phases, phases[1:]))
            rev = phases[::-1]
            bank2_strict = all(a > b for a, b in zip(rev, rev[1:]))
            assert not (bank1_strict and bank2_strict)
            checked += 1
    # If one bank turns the other way the abstract obstruction disappears.
    phases = (2, 1, 0)
    assert all(a > b for a, b in zip(phases, phases[1:]))
    assert all(a < b for a, b in zip(phases[::-1], phases[-2::-1]))
    print(f"PASS: {checked} opposed-order phase assignments, including repetitions.")


def certify_safe_constant():
    # gamma <= 1, epsilon=eta=gamma/100, w+rho<=eta, R<=D.
    # sin(a)<=a and cos(a+rho)>=1-(a+rho)^2/2 give this uniform bound.
    short_bound_per_gamma = F(1, 100) + F(24, 100) / (1 - F(49, 20000))
    assert short_bound_per_gamma < F(26, 100)
    remaining_per_gamma = 1 - F(26, 100) - F(1, 10)
    assert remaining_per_gamma == F(64, 100)
    z_coefficient = remaining_per_gamma / (4 * 10000)
    assert z_coefficient == F(1, 62500) > F(1, 100000)
    # 1-cos(x)>=x^2/2-x^4/24>=x^2/3 for 0<=x<=1.
    assert F(1, 2) - F(1, 24) > F(1, 3)
    print("PASS: conservative gamma^3/100000 route-excess constant.")


if __name__ == "__main__":
    certify_unstressed_grid()
    certify_small_positive_turn()
    certify_opposed_order()
    certify_safe_constant()
    print("All exact checks passed. No global optimality or Level I certificate.")
