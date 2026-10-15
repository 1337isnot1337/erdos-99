#!/usr/bin/env python3
"""Exact local geometry and train-ledger checks; no global-source assertion."""
from fractions import Fraction as F
from itertools import combinations
import json


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def squared(a):
    return dot(a, a)


def unit(t):
    return (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)


def local_checks():
    anchors = clauses = cones = 0
    normals = []
    for j in range(-20, 21):
        c, s = unit(F(j, 1000))
        r = (s, c)
        assert squared(r) == 1
        assert squared(sub(r, (F(0), F(1)))) < F(1, 20) ** 2
        normals.append(r)
    for j in range(1, 578):
        c, s = unit(F(j, 1000))
        assert squared((c, s)) == 1
        assert c > F(1, 2)
        a, b, z = (-c, F(0)), (c, F(0)), (F(0), -s)
        assert squared(sub(a, z)) == squared(sub(b, z)) == 1
        assert squared(sub(a, b)) > 1
        for u in ((c, s), (c, -s)):
            assert det(u, (F(0), F(1))) >= F(1, 2)
            anchors += 1
            for r in normals:
                assert det(u, r) > F(9, 20)
                cones += 1
        if 2 * c <= F(13, 12):
            # Positive cosine below 1/2 means projective angle is in
            # (pi/3,pi/2), so both directions cannot be selected narrowly.
            cosine = dot(sub(a, z), sub(b, z))
            assert 0 < cosine < F(1, 2)
            clauses += 1
    return anchors, clauses, cones


def long_pocket_regression():
    points = [(F(0), F(0)), (F(0), F(-1)),
              (F(1), F(-1)), (F(8, 5), F(-1, 5))]
    contacts = []
    for i, j in combinations(range(4), 2):
        distance = squared(sub(points[i], points[j]))
        assert distance >= 1
        if distance == 1:
            contacts.append((i, j))
    assert contacts == [(0, 1), (1, 2), (2, 3)]
    for j in range(4):
        incoming = sub(points[j], points[j - 1])
        outgoing = sub(points[(j + 1) % 4], points[j])
        assert det(incoming, outgoing) > 0
    chord = sub(points[3], points[0])
    normal = (-chord[1], chord[0])
    contact = sub(points[1], points[0])
    ratio = det(contact, normal) ** 2 / squared(normal)
    assert ratio == F(1, 65) < F(1, 4)
    return {'points': [[str(x), str(y)] for x, y in points],
            'contacts': contacts, 'normalized_determinant_squared': str(ratio)}


def ledger_checks():
    cases = 0
    for q in range(4, 15):
        for k in range(q // 2 + 1):
            for x in range(q - 2 * k + 1):
                Q = q - x - 2 * k
                for f in range(Q + 1):
                    X = Q - f
                    total = q - k + 2 * f
                    b = q + x
                    for oo in range(min(4, b // 2 + 1)):
                        ob = b - 2 * oo
                        outer = b - oo
                        bb = total - outer
                        if bb < 0:
                            continue
                        assert total == oo + ob + bb
                        assert bb == 2 * f - x - k + oo
                        for singletons in {0, bb // 2, bb}:
                            for r_bulk in (F(0), F(1, 3), F(7, 2)):
                                slack = bb - singletons - 2 * r_bulk
                                assert slack == (2 * f - x - k - singletons
                                                 - 2 * r_bulk + oo)
                                assert slack == (2 * q - 3 * x - 5 * k
                                                 - 2 * X - singletons
                                                 - 2 * r_bulk + oo)
                                cases += 1
    return cases


def leading_ledger():
    # Tuple (a,b) is the exact formal quantity a*pi+b*s. No float comparison.
    def plus(*terms):
        return tuple(sum(t[j] for t in terms) for j in range(2))

    def scale(a, term):
        return tuple(a * v for v in term)

    pi, s, zero = (F(1), F(0)), (F(0), F(1)), (F(0), F(0))
    q = b = Q = f = p5 = pi
    total = scale(3, pi)
    bb = scale(2, pi)
    sg = pi
    sbb = plus(bb, scale(-2, s))
    assert total == plus(q, scale(2, f))
    assert bb == plus(total, scale(-1, b))
    assert scale(2, f) == plus(scale(2, s), sbb)
    assert plus(scale(3, zero), scale(5, zero), scale(2, zero), sbb) == sbb
    # Singleton formula: S=total-2s; S_G+S_BB is precisely that value.
    assert plus(sg, sbb) == plus(total, scale(-2, s))
    # The good-hull singleton bound S_G<=2P_5 has slack pi>0.
    assert plus(scale(2, p5), scale(-1, sg)) == pi
    # New terminal inequality has equality; no old bank became a surplus site.
    return {'q,b,Q,f,P5': 'pi D', 'K_top,X,x_B,m_B,N_OO': 'o(D)',
            'N_OB,S_G': 'pi D', 'N_BB': '2 pi D',
            'S_BB,eta_D': '(2 pi-2 s) D', 'sigma_R': 'o(D)',
            'status': 'leading-order algebra only; no source or global optimality'}


def main():
    anchors, clauses, cones = local_checks()
    report = {'classification': 'exact finite geometry and ledger certificates',
              'anchor_checks': anchors, 'short_pocket_binary_checks': clauses,
              'positive_cone_checks': cones, 'finite_ledger_checks': ledger_checks(),
              'long_pocket_regression': long_pocket_regression(),
              'surviving_leading_ledger': leading_ledger(),
              'omitted': ['source KKT realization', 'asymptotic compactness proof',
                          'beneficial finite motion', 'global optimality']}
    print(json.dumps(report, sort_keys=True))


if __name__ == '__main__':
    main()
