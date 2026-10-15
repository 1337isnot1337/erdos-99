#!/usr/bin/env python3
"""Exact finite geometry and ledgers for loaded flat-pentagon depletion.

The pentagons are unit-separated local geometry packets, not canonical
loaded sources or global minimizers. Their diagonals remain strict.
Integer incidence/rank ledgers are not source embeddings. Compactness,
asymptotic dispersion, activation and Level I closure are not numerical
conclusions of this script.
"""
from fractions import Fraction as F


def rational(x):
    return (F(x), F(0))


def add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def neg(x):
    return (-x[0], -x[1])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y, rad):
    return (x[0]*y[0]+rad*x[1]*y[1], x[0]*y[1]+x[1]*y[0])


def sign(x, rad):
    a, b = x
    if b == 0:
        return (a > 0)-(a < 0)
    if a == 0:
        return (b > 0)-(b < 0)
    if a*b > 0:
        return (a > 0)-(a < 0)
    difference = a*a-b*b*rad
    if difference == 0:
        return 0
    return ((a > 0)-(a < 0))*((difference > 0)-(difference < 0))


def vsub(x, y):
    return (sub(x[0], y[0]), sub(x[1], y[1]))


def dot(x, y, rad):
    return add(mul(x[0], y[0], rad), mul(x[1], y[1], rad))


def cross(x, y, rad):
    return sub(mul(x[0], y[1], rad), mul(x[1], y[0], rad))


def pentagon_packet(t):
    u, v = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    cb = u-F(1, 2)
    rad = 1-cb*cb
    assert 0 < rad < 1 and u*u+v*v == 1
    root = (F(0), F(1))
    p = [(rational(0), rational(0)),
         (rational(u), rational(-v)),
         (rational(2*u), rational(0)),
         (rational(u+F(1, 2)), root),
         (rational(u-F(1, 2)), root)]
    edges = [vsub(p[(i+1) % 5], p[i]) for i in range(5)]
    for i, e in enumerate(edges):
        assert dot(e, e, rad) == rational(1)
        assert sign(cross(e, edges[(i+1) % 5], rad), rad) > 0
    assert cross(edges[0], edges[1], rad) == rational(2*u*v)
    # These are the two nonparallel singleton columns at the flat corner.
    assert 2*u*v > 0
    for i in range(5):
        for j in range(i+1, 5):
            d = vsub(p[j], p[i])
            dsq = dot(d, d, rad)
            adjacent = j == i+1 or (i == 0 and j == 4)
            if adjacent:
                assert dsq == rational(1)
            else:
                assert sign(sub(dsq, rational(1)), rad) > 0
    area2 = rational(0)
    for i in range(5):
        area2 = add(area2, cross(p[i], p[(i+1) % 5], rad))
    area = (area2[0]/2, area2[1]/2)
    assert area == (u*v, u+F(1, 2))
    # r>0 iff A^2>27/16; this avoids introducing a second radical.
    assert sign(sub(mul(area, area, rad), rational(F(27, 16))), rad) > 0
    # A three-triangle fan has every side below 3/2: the nearest vertex
    # barycentric bound is strictly below one throughout the pentagon.
    for j in (3, 4):
        d = vsub(p[j], p[1])
        dsq = dot(d, d, rad)
        assert sign(sub(rational(F(9, 4)), dsq), rad) > 0
    # The unique maximum pair in these packets is 0--2. Its other
    # endpoints are not all loaded: no canonical source claim is made.
    maximum = rational(4*u*u)
    for i in range(5):
        for j in range(i+1, 5):
            if (i, j) == (0, 2):
                continue
            d = vsub(p[j], p[i])
            assert sign(sub(maximum, dot(d, d, rad)), rad) > 0
    return 10


def incidence_and_rank_ledgers():
    count = 0
    for q in range(4, 15):
        for k in range(q//2+1):
            Q, b = q-2*k, q
            for f in range(Q+1):
                high_penalty = Q-f
                T = q-k+2*f
                for spokes in range(q+1):
                    low_mark = max(0, q-spokes-6*high_penalty)
                    high_mark = min(f, q-spokes)
                    if low_mark > high_mark:
                        continue
                    for marked in {low_mark, high_mark}:
                        for sigma in range(3):
                            rank_floor = q-k+sigma+2*marked
                            deleted = max(q, rank_floor)
                            if deleted > T:
                                continue
                            for single_u in {0, T-deleted}:
                                U = T-deleted-single_u
                                assert U <= 2*(f-marked)-sigma-single_u
                                assert spokes+6*high_penalty-2*k >= (F(U+sigma+single_u, 2))
                                root_r = F(q+1, 7)
                                S = single_u
                                sigma_R = 2*(T-S)-4*root_r
                                lhs = 4*S+2*sigma_R
                                rhs = (2*b-8*root_r+5*U
                                       +5*(sigma+2*marked+single_u)
                                       +2*high_penalty
                                       +5*(deleted-rank_floor))
                                assert lhs == rhs
                                count += 1
    return count


def formal_scalar_survivor():
    """Linear expressions in 1, pi, s; this is not a geometric source."""
    def la(x, y):
        return tuple(a+b for a, b in zip(x, y))

    def ls(x, factor):
        return tuple(a*F(factor) for a in x)

    def ld(x, y):
        return la(x, ls(y, -1))

    def positive(x):
        constant, pi_coefficient, s_coefficient = x
        # Use only pi>3 and 0<s<pi/2. The latter follows from pi*sqrt(3)>2.
        effective = pi_coefficient + min(s_coefficient, 0)/2
        assert effective >= 0
        lower = constant+3*effective
        assert lower >= 0
        assert lower > 0 or s_coefficient < 0 or effective > 0

    zero, pi, s = (F(0),)*3, (F(0), F(1), F(0)), (F(0), F(0), F(1))
    q, k, f = pi, ls(pi, F(1, 8)), ls(pi, F(3, 4))
    spokes, marked = ls(la(pi, s), F(1, 2)), ls(ld(pi, s), F(1, 2))
    Q = ld(q, ls(k, 2))
    assert Q == f and marked == ld(q, spokes)
    T = la(ld(q, k), ls(f, 2))
    deleted = la(ld(q, k), ls(marked, 2))
    U = ld(T, deleted)
    assert T == ls(pi, F(19, 8))
    assert deleted == ld(ls(pi, F(15, 8)), s)
    assert U == la(ls(pi, F(1, 2)), s)
    assert U == ls(ld(f, marked), 2)
    positive(ld(U, ls(s, 2)))
    positive(ld(spokes, la(s, ls(k, 2))))
    positive(ld(q, spokes))
    positive(ld(f, spokes))
    positive(ld(ls(marked, 2), k))
    positive(ld(ld(q, k), ls(la(pi, s), F(1, 2))))
    positive(ld(ld(q, k), ls(la(ls(pi, 3), ls(s, 2)), F(1, 5))))
    sigma_R = ld(ls(ld(T, q), 2), ls(s, 4))
    positive(sigma_R)
    lhs = la(ls(q, 4), ls(sigma_R, 2))
    marked_rhs = la(ls(la(pi, s), 2), ls(marked, 10))
    assert ld(lhs, marked_rhs) == ls(ld(ls(pi, F(1, 2)), s), 5)
    positive(ld(lhs, marked_rhs))
    population_margin = ld(ls(pi, F(1, 2)), (F(1, 4), F(0), F(0)))
    positive(population_margin)
    assert zero == ld(Q, f)


def main():
    pair_checks = 0
    for t in [F(1, n) for n in (5, 10, 20, 50, 100, 250, 1000, 10000)]:
        pair_checks += pentagon_packet(t)
    ledgers = incidence_and_rank_ledgers()
    formal_scalar_survivor()
    print(f"PASS: {pair_checks} exact unit-pentagon pair constraints, strict diagonals and convexity")
    print("PASS: positive residual, complete interior disk cover and rank-two marked columns")
    print(f"PASS: {ledgers} incidence, simultaneous rank and second-depletion ledgers")
    print("PASS: exact formal scalar survivor; overlapping source charges give no algebraic closure")
    print("SCOPE: local geometry and abstract ledgers; no canonical loaded source or activation certificate")


if __name__ == "__main__":
    main()
