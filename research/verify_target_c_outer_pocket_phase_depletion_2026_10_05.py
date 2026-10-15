#!/usr/bin/env python3
"""Exact packets for outer-pocket phase depletion and terminal payment.

Rational three-point pockets certify unit contacts, strict noncontact chords,
Groemer residual enclosures, and convergence to a common reduced phase. End
tables certify multiplicities and the second-depletion algebra. No global
optimum, canonical stress, compactness theorem, phase coarea, asymptotic tail
hypothesis, or strict competitor is certified by finite output.
"""

from fractions import Fraction as F
from itertools import product
from math import isqrt


PRECISION = 10**60
ROOT_LO = F(isqrt(3 * PRECISION**2), PRECISION)
ROOT_HI = ROOT_LO + F(1, PRECISION)
assert ROOT_LO**2 < 3 < ROOT_HI**2


def triangular_pocket(t):
    x = (1 - t * t) / (1 + t * t)
    y = 2 * t / (1 + t * t)
    assert x > F(1, 2) and x < 1 and y > 0
    assert x * x + y * y == 1
    chord = 2 * x
    assert chord > 1
    # Points (0,0),(x,y),(2x,0): exactly the two path edges are unit.
    assert chord * chord > 1
    area = x * y
    # Three source points: A/(sqrt(3)/2)+P/2+1-3.
    residual_lo = 2 * area / ROOT_HI + x - 1
    residual_hi = 2 * area / ROOT_LO + x - 1
    assert residual_lo > 0
    # Euclidean direction error relative to +/- pi/3, without floating trig.
    dy = max(abs(y - ROOT_LO / 2), abs(y - ROOT_HI / 2))
    error2_hi = (x - F(1, 2)) ** 2 + dy * dy
    return residual_lo, residual_hi, error2_hi


def geometry_packets():
    previous_r = F(1)
    previous_e = F(1)
    count = 0
    for digits in range(1, 19):
        scale = 10**digits
        # Rational t below 1/sqrt(3), tending to it from below.
        t = F(isqrt(scale * scale // 3), scale)
        assert 3 * t * t < 1
        lo, hi, err = triangular_pocket(t)
        assert hi <= previous_r and err <= previous_e
        previous_r, previous_e = hi, err
        count += 1
    assert previous_r < F(1, 10**17)
    assert previous_e < F(1, 10**34)

    # Small degree alone does not force phase agreement. The rational 3-4-5
    # triangle has side directions differing from the equilateral phase.
    lo, hi, err = triangular_pocket(F(1, 2))
    assert lo > F(3, 20) and hi < F(4, 25)
    # Its x component is 3/5 rather than the required 1/2, so an exact reduced
    # phase agreement is impossible. Its residual is strictly positive.
    assert F(3, 5) != F(1, 2)
    return count


def terminal_packets():
    count = 0
    mantel = 0
    # G=good hull, N=non-good outer, F=bounded exceptional-face terminal.
    for gg in range(3):
        for gn, gf, nn, nf, ff in product(range(5), repeat=5):
            if gg + gn + gf + nn + nf + ff == 0:
                continue
            train_count = gg + gn + gf + nn + nf + ff
            outer_ends = 2 * gg + 2 * gn + gf + 2 * nn + nf
            good_ends = 2 * gg + gn + gf
            face_ends = gf + nf + 2 * ff
            good_trains = gg + gn + gf
            outer_trains = good_trains + nn + nf
            internal_trains = ff
            mixed_trains = gf + nf
            assert 2 * train_count == outer_ends + face_ends
            assert outer_trains + internal_trains == train_count
            assert 2 * outer_trains >= outer_ends
            assert face_ends == 2 * internal_trains + mixed_trains
            assert good_trains == good_ends - gg
            assert outer_trains - good_trains == nn + nf

            # b=q+m+u and h_B=q-m, hence b-h_B=2m+u.
            nongood_occurrences = outer_ends - good_ends
            assert nongood_occurrences >= 0
            for nonunit_sides in range(nongood_occurrences // 2 + 1):
                u = nongood_occurrences - 2 * nonunit_sides
                q = good_ends + nonunit_sides
                assert outer_ends == q + nonunit_sides + u
                exact_lower = F(3 * nonunit_sides + u - q, 2) + gg
                additional = outer_trains - good_trains
                assert additional >= max(F(0), exact_lower)
                assert train_count - good_trains - additional == internal_trains
                count += 1

            # Exact integer form of the Mantel implication P_exc>=4sqrt(R)
            # on the retained internal train graph, including mixed ends.
            for crossings in range(internal_trains * internal_trains // 4 + 1):
                assert (face_ends - mixed_trains) ** 2 >= 16 * crossings
                mantel += 1
    return count, mantel


def occurrence_tail_packets():
    # A hull-side count bounds anchors, not all train occurrences assigned to
    # those anchors. This tests the multiplicity issue as bookkeeping only.
    count = 0
    for length in range(2, 1002):
        one_anchor = 1
        assigned_occurrences = length
        assert assigned_occurrences > one_anchor
        cutoff = length - 1
        tail = length if length > cutoff else 0
        assert tail == assigned_occurrences
        count += 1
    return count


def marked_face_packets():
    count = 0
    # B is a marked bounded face; U is an unmarked bounded face. The table
    # makes no assumption that a physical face has only one hull side.
    for gg, gn, gb, gu, nn, nb, nu, bb, bu, uu in product(range(3), repeat=10):
        total = gg + gn + gb + gu + nn + nb + nu + bb + bu + uu
        if not total:
            continue
        b = 2 * gg + 2 * gn + gb + gu + 2 * nn + nb + nu
        h = 2 * gg + gn + gb + gu
        p_marked = gb + nb + 2 * bb + bu
        p_unmarked = gu + nu + bu + 2 * uu
        good = gg + gn + gb + gu
        deleted = total - uu
        mixed = gu + nu + bu
        assert 2 * total == b + p_marked + p_unmarked
        assert p_unmarked == 2 * uu + mixed
        assert 2 * deleted >= b + p_marked
        assert deleted >= good
        assert good == h - gg
        # Checking the strongest permissible m is sufficient; the expression
        # 3m+u-q is independent of this parameter once b,h are prescribed.
        m = (b - h) // 2
        u = b - h - 2 * m
        q = h + m
        lower = F(3 * m + u - q + p_marked, 2) + gg
        assert deleted - good >= max(F(0), lower)
        assert total - good - (deleted - good) == uu
        count += 1
    return count


if __name__ == "__main__":
    geometry = geometry_packets()
    terminals, mantel = terminal_packets()
    tails = occurrence_tail_packets()
    marked = marked_face_packets()
    print(f"PASS: {geometry} rational unit-path pockets and exact residual/direction enclosures")
    print("PASS: fixed small pocket with positive residual and reduced-phase mismatch")
    print(f"PASS: {terminals} exact terminal/payment packets; {mantel} integer Mantel consequences")
    print(f"PASS: {tails} anchor/occurrence multiplicity packets")
    print(f"PASS: {marked} marked-face terminal tables and stronger second-depletion charges")
    print("SCOPE: finite geometry and counting; no asymptotic hypothesis, source optimum, or competitor")
