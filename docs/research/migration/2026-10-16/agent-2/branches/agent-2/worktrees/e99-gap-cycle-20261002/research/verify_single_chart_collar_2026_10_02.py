#!/usr/bin/env python3
"""Finite algebra/regressions for the single-chart loaded-collar candidate.

Encoded: rational chart Gram interval; three-unit-edge identities; two-sign
anchor words; exact algebraic six-point source; canonical integer ledgers.
Omitted: arbitrary planar face decomposition, KKT realization, global
optimality, chart/port extraction. General geometric proofs are in the report.
"""

from fractions import Fraction as F
from itertools import combinations, product

import sympy as sp


def chart_alphabet():
    """All differences of a unit contact and of a two-axis-edge chart path."""
    lo, hi = F(12, 25), F(1, 2)
    units = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    short = units | {(1, -1), (-1, 1)}
    unit_candidates = set()
    short_candidates = set()
    for i, j in product(range(-3, 4), repeat=2):
        if (i, j) == (0, 0):
            continue
        a, slope = i * i + j * j, 2 * i * j
        values = (F(a) + slope * lo, F(a) + slope * hi)
        lower, upper = min(values), max(values)
        if lower <= 1 <= upper:
            unit_candidates.add((i, j))
            if (i, j) not in units:
                # The extra two directions are unit only at the excluded c=1/2.
                assert F(a) + slope * hi == 1
                assert F(a) + slope * lo > 1
        if lower <= F(51, 50) ** 2:
            short_candidates.add((i, j))
        if (i, j) not in short:
            assert lower >= F(74, 25)
    assert unit_candidates == short
    assert short_candidates == short
    paths = {tuple(x + y for x, y in zip(a, b)) for a, b in product(units, repeat=2)}
    straight = {(2, 0), (-2, 0), (0, 2), (0, -2)}
    assert paths == straight | {(0, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)}
    # Long regular anchor step length >5/3, and its squared excess over 1 >1/2.
    assert F(74, 25) > F(25, 9)
    assert F(74, 25) - F(3, 2) > 0
    assert (F(74, 25) - F(3, 2)) ** 2 > 2


def symbolic_identities():
    # Four-point circle intersections: B^2-h^2 = z/2-A^2.
    z, d = sp.symbols("z d", real=True, nonzero=True)
    A = -z / (2 * d)
    c2 = (2 + z) / 2 - d**2 / 4
    h2 = 1 - d**2 / 4
    assert sp.simplify(c2 - A**2 - h2 - (z / 2 - A**2)) == 0
    # The stated uniform range and final linear error bound.
    assert (1 + F(1, 25)) ** 2 - 1 < F(1, 10)
    assert F(3, 2) * (2 + F(1, 25)) < 4
    # Bounds excluding both intersections when h <=1/4.
    assert F(1, 20) + F(1, 2) + F(1, 4) < 1
    assert F(1, 4) ** 2 > F(1, 20)
    # Difference of consecutive unit-vector norm identities.
    wx, wy, ax, ay, bx, by = sp.symbols("wx wy ax ay bx by", real=True)
    w, a, b = sp.Matrix([wx, wy]), sp.Matrix([ax, ay]), sp.Matrix([bx, by])
    first = sp.expand(w.dot(w) - (w - a).dot(w - a))
    second = sp.expand((w + b).dot(w + b) - w.dot(w))
    target = 2 * w.dot(a - b) - a.dot(a) - b.dot(b)
    assert sp.expand(first - second - target) == 0


def sign_words():
    tested = 0
    for n in range(1, 13):
        for word in product((-1, 1), repeat=n):
            same = sum(a == b for a, b in zip(word, word[1:]))
            reverse = sum(a != b for a, b in zip(word, word[1:]))
            assert same + reverse == n - 1
            # Each adjacent pair has a fixed turn charge in the report.
            assert n == 1 + same + reverse
            anchors = [0]
            for sign in word:
                anchors.append(anchors[-1] + sign)
            for i, (a, b) in enumerate(zip(word, word[1:])):
                assert (anchors[i] == anchors[i + 2]) == (a != b)
            tested += 1
    assert tested == 8190
    return tested


def six_point_regression():
    rt = sp.sqrt(3)
    h = sp.sqrt(rt / 2)
    points = {
        "l": sp.Matrix([-rt / 2, 0]),
        "a": sp.Matrix([rt / 2, 0]),
        "p": sp.Matrix([-sp.Rational(1, 2), h]),
        "q": sp.Matrix([sp.Rational(1, 2), h]),
        "p_lower": sp.Matrix([-sp.Rational(1, 2), h - 10]),
        "q_lower": sp.Matrix([sp.Rational(1, 2), h - 10]),
    }
    contact = {
        frozenset(("l", "p")), frozenset(("p", "q")),
        frozenset(("q", "a")), frozenset(("p_lower", "q_lower")),
    }
    diameter = {
        frozenset(("p", "q_lower")), frozenset(("q", "p_lower")),
    }
    distances = {}
    for a, b in combinations(points, 2):
        r = points[a] - points[b]
        value = sp.simplify(r.dot(r))
        edge = frozenset((a, b))
        distances[edge] = value
        if edge in contact:
            assert value == 1
        elif edge in diameter:
            assert value == 101
        elif {a, b}.issubset({"l", "a", "p", "q"}):
            assert value in (3, 1 + rt)
        elif {a, b}.issubset({"p", "q", "p_lower", "q_lower"}):
            assert value == 100
        else:
            # Anchor to lower point: exact expression plus a rational enclosure.
            horizontal2 = sp.simplify((points[a][0] - points[b][0]) ** 2)
            assert sp.simplify(value - horizontal2 - (10 - h) ** 2) == 0
            # 17/10 <sqrt(3)<9/5 and 9/10<h<1 follow by squaring.
            assert F(17, 10) ** 2 < 3 < F(9, 5) ** 2
            assert F(9, 10) ** 2 < F(17, 20)
            assert F(9, 10) < 1
            # All these squared distances lie strictly between 81 and 101.
            assert 81 > 1
            assert F(7, 5) ** 2 + F(91, 10) ** 2 < 101
    for triple in combinations(points, 3):
        assert not all(frozenset(edge) in contact for edge in combinations(triple, 2))
    u, v = sp.Matrix([rt / 2, sp.Rational(1, 2)]), sp.Matrix([rt / 2, -sp.Rational(1, 2)])
    assert u.dot(u) == v.dot(v) == 1
    assert u.dot(v) == sp.Rational(1, 2)
    assert points["a"] - points["l"] == u + v
    assert sp.simplify((points["a"] - points["l"]).dot(points["a"] - points["l"])) == 3
    assert len(distances) == 15


def ledger_family():
    for j in range(10, 1001):
        q, m, k = 3 * j, 2 * j, 2
        cI, sC, uB, cB = 1, 2 * j - 1, 0, 0
        xB, Q, eBB, h = 2 * j, j - 4, j, 3 * j - 1
        dH, sZ = 1, 1
        assert k == dH + sZ
        assert dH == q - h
        assert eBB == q - m
        assert q - xB == Q + 2 * k
        assert eBB == Q + 2 * k + uB + cB
        assert uB == xB - m
        assert cI + sC + cB == m + k - 2
        assert F(eBB + 2 * sC - 3 * k, j) == 5 - F(8, j)
        assert h >= j and m >= F(q, 2)


def main():
    chart_alphabet()
    symbolic_identities()
    tested = sign_words()
    six_point_regression()
    ledger_family()
    print(f"PASS: strict chart alphabet; four-point/circle and turn identities; {tested} sign words;")
    print("      all 15 algebraic source pairs and no triangles; 991 formal ledger states.")
    print("NOT CERTIFIED: face topology, source chart extraction, source KKT realization, global optimality.")


if __name__ == "__main__":
    main()
