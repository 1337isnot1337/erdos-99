#!/usr/bin/env python3
"""Exact regression: two stressed unit chains plus a near-dense isolate disk.

Squared distances lie in Q(sqrt(7)); signs are decided with rational squares.
This verifies feasibility, the full contact/diameter sets, normalized KKT,
and an explicit smaller-diameter competitor for each requested finite m.
It does not certify a global minimizer or the analytic cone theorem.
"""
from fractions import Fraction as F
from itertools import combinations
import argparse
import json


def sign_rational(x):
    return (x > 0) - (x < 0)


def sign_q7(a, b=F(0)):
    """Exact sign of a + b sqrt(7), for rational a,b."""
    a, b = F(a), F(b)
    sa, sb = sign_rational(a), sign_rational(b)
    if not sa:
        return sb
    if not sb or sa == sb:
        return sa
    return sa * sign_rational(a*a - 7*b*b)


def sub(p, q):
    return tuple(x-y for x, y in zip(p, q))


def norm_squared(p):
    # Point coordinates are (x, y3, y21), representing (x,y3 sqrt(3)+y21 sqrt(21)).
    x, a, b = p
    return x*x + 3*a*a + 21*b*b, 6*a*b


def compare_squared(p, q, value):
    a, b = norm_squared(sub(p, q))
    return sign_q7(a-value, b)


def verify(m):
    assert m >= 4
    zero = (F(0), F(0), F(0))
    u = (F(1), F(0), F(0))
    v = (F(2, 5), F(0), F(1, 5))
    mul = lambda k, p: tuple(k*x for x in p)
    points = [mul(F(i), u) for i in range(-m, m+1)]
    index = {p: i for i, p in enumerate(points)}
    for i in range(-m, m+1):
        p = mul(F(i), v)
        if p not in index:
            index[p] = len(points)
            points.append(p)
    core_size = len(points)
    assert core_size == 4*m+1
    contacts_expected = set()
    for direction in (u, v):
        for i in range(-m, m):
            contacts_expected.add(tuple(sorted((index[mul(F(i), direction)],
                                                index[mul(F(i+1), direction)]))))
    diameters_expected = {
        tuple(sorted((index[mul(F(-m), direction)], index[mul(F(m), direction)])))
        for direction in (u, v)
    }
    scale = F(m*m+1, m*m)
    for a in range(-2*m, 2*m+1):
        for b in range(-2*m, 2*m+1):
            if scale*scale*(a*a+a*b+b*b) > (m-2)**2:
                continue
            p = (scale*(F(a)+F(b, 2)), scale*F(b, 2), F(0))
            if all(compare_squared(p, q, F(1)) > 0 for q in points[:core_size]):
                assert p not in index
                index[p] = len(points)
                points.append(p)
    contacts, diameters = set(), set()
    for i, j in combinations(range(len(points)), 2):
        contact = compare_squared(points[i], points[j], F(1))
        diameter = compare_squared(points[i], points[j], F(4*m*m))
        assert contact >= 0 and diameter <= 0
        if contact == 0:
            contacts.add((i, j))
        if diameter == 0:
            diameters.add((i, j))
    assert contacts == contacts_expected
    assert diameters == diameters_expected
    forces = [[F(0), F(0), F(0)] for _ in points]
    for edge_set, weight in ((contacts, F(m)), (diameters, F(-1, 2))):
        for i, j in edge_set:
            delta = sub(points[i], points[j])
            for k in range(3):
                forces[i][k] += weight*delta[k]
                forces[j][k] -= weight*delta[k]
    assert all(force == [F(0), F(0), F(0)] for force in forces)
    assert len(diameters)*F(1, 2) == 1
    assert len(contacts)*m == 4*m*m
    # A strict same-cardinality competitor, independently checked in Q(sqrt(3)).
    competitor = []
    for a in range(-2*m, 2*m+1):
        for b in range(-2*m, 2*m+1):
            if a*a+a*b+b*b <= (m-1)**2:
                competitor.append((F(a)+F(b, 2), F(b, 2), F(0)))
    assert len(competitor) >= len(points)
    competitor = competitor[:len(points)]
    competitor_diameter = F(0)
    for p, q in combinations(competitor, 2):
        value, radical = norm_squared(sub(p, q))
        assert radical == 0 and value >= 1
        competitor_diameter = max(competitor_diameter, value)
    assert competitor_diameter < 4*m*m
    outside = 0
    for p in points:
        # Lattice coefficients x_c,y_c in p = x_c u + y_c v are in Q(sqrt(7)).
        x, y3, y21 = p
        cy = (5*y21, F(5, 7)*y3)
        cx = (x-F(2, 5)*cy[0], -F(2, 5)*cy[1])
        ax = tuple(sign_q7(*cx)*z for z in cx)
        ay = tuple(sign_q7(*cy)*z for z in cy)
        if sign_q7(ax[0]+ay[0]-m, ax[1]+ay[1]) > 0:
            outside += 1
    return dict(m=m, n=len(points), positive_core=core_size,
                contacts=len(contacts), diameter_pairs=len(diameters),
                isolates=len(points)-core_size, outside_force_hull=outside,
                diameter_squared=4*m*m,
                competitor_diameter_squared=str(competitor_diameter),
                verified="exact Q(sqrt(7)) pair constraints and rational KKT")


def verify_analytic_row_bounds():
    """Independently check actual candidate sites used by the all-m proof."""
    for m in (4, 8, 12, 16, 64, 100):
        scale = F(m*m+1, m*m)
        for b in (-1, 1):
            deleted = []
            for a in range(-2*m, 2*m+1):
                q = F(a)+F(b, 2)
                x, y3 = scale*q, scale*F(b, 2)
                if abs(x) > m-3 or abs(q) < F(5, 2):
                    continue
                assert x*x+3*y3*y3 <= (m-2)**2
                floor_x = x.numerator // x.denominator
                assert min((x-i)**2+3*y3*y3 for i in (floor_x, floor_x+1)
                           if -m <= i <= m) < 1
                deleted.append(a)
            assert len(deleted) >= 2*m-12
        row0 = [a for a in range(-2*m, 2*m+1) if abs(scale*a) <= m-2]
        assert len(row0) >= 2*m-6
        for a in row0:
            x = scale*a
            floor_x = x.numerator // x.denominator
            assert min((x-i)**2 for i in (floor_x, floor_x+1)
                       if -m <= i <= m) < 1
        assert 1-F(1,m*m)+F(7,m**4) < 1
    assert F(86*64-5029,175) > 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--m", nargs="+", type=int, default=[8, 12])
    args = parser.parse_args()
    # Check all branches of the exact sign routine, including cancellation cases.
    assert sign_q7(8, -3) == 1 and sign_q7(7, -3) == -1
    assert sign_q7(-8, 3) == -1 and sign_q7(-7, 3) == 1
    assert sign_q7(0, -1) == -1 and sign_q7(0, 1) == 1
    verify_analytic_row_bounds()
    for m in args.m:
        print(json.dumps(verify(m), sort_keys=True))


if __name__ == "__main__":
    main()
