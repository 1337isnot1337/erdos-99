#!/usr/bin/env python3
"""Exact Q(sqrt(3)) certificates for the seed-84 seamed-grain regression.

No floating-point geometry or external packages. This verifies finite sources,
including an explicit smaller-diameter competitor; it does not certify optimality.
"""
from collections import Counter, deque
from fractions import Fraction
from functools import cmp_to_key
import json
from math import isqrt


def sign(a, b=0):
    """Sign of a+b*sqrt(3), for integer or rational a,b."""
    if not b:
        return (a > 0) - (a < 0)
    if not a:
        return (b > 0) - (b < 0)
    if (a > 0) == (b > 0):
        return 1 if a > 0 else -1
    z = a*a - 3*b*b
    return ((z > 0) - (z < 0)) * (1 if a > 0 else -1)


def mul(a, b):
    return a[0]*b[0]+3*a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    return a[0]-b[0], a[1]-b[1]


def scale(a, k):
    return a[0]*k, a[1]*k


def delta(p, q):
    return sub(p[0], q[0]), sub(p[1], q[1])


def norm2(v):
    return add(mul(v[0], v[0]), mul(v[1], v[1]))


def det(p, q):
    return sub(mul(p[0], q[1]), mul(p[1], q[0]))


def atan_bounds(x, terms=32):
    s = sum(((-1)**k * x**(2*k+1)/ (2*k+1)
             for k in range(terms)), Fraction(0))
    next_term = (-1)**terms * x**(2*terms+1)/(2*terms+1)
    return min(s, s+next_term), max(s, s+next_term)


def pi_bounds():
    a, b = atan_bounds(Fraction(1, 5))
    c, d = atan_bounds(Fraction(1, 239))
    # Machin: pi = 16 atan(1/5) - 4 atan(1/239).
    return 16*a-4*d, 16*b-4*c


def connected(vertices, edges):
    adj = {p: [] for p in vertices}
    for p, q in edges:
        adj[p].append(q)
        adj[q].append(p)
    seen = {next(iter(vertices))}
    todo = deque(seen)
    while todo:
        p = todo.popleft()
        for q in adj[p]:
            if q not in seen:
                seen.add(q)
                todo.append(q)
    return len(seen) == len(vertices), adj


def hull(points):
    def compare(p, q):
        z = sub(p[0], q[0])
        c = sign(*z)
        return c if c else sign(*sub(p[1], q[1]))
    ordered = sorted(points, key=cmp_to_key(compare))
    def chain(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and sign(*det(delta(out[-1], out[-2]),
                                            delta(p, out[-1]))) <= 0:
                out.pop()
            out.append(p)
        return out
    return chain(ordered)[:-1]+chain(ordered[::-1])[:-1]


def make_source(Q, shear_den=10**6, rotation_den=10**12, wrong_sign=False):
    bound = 2*isqrt(Q)+3
    labels = [(i, j) for i in range(-bound, bound+1)
              for j in range(-bound, bound+1) if i*i+i*j+j*j <= Q]
    label_set = set(labels)
    anchor_i = max(i for i, j in labels if j == 0 and (i, -1) in label_set)
    # Rotate v0 counterclockwise by delta=2 atan(1/shear_den).
    c, s, d = shear_den**2-1, 2*shear_den, shear_den**2+1
    # Every sheared coordinate initially has denominator L0=2d.
    L0 = 2*d
    # v=((c-s sqrt3)/2d, (s+c sqrt3)/2d).
    base = {(i, j): ((2*d*i+j*c, -j*s), (j*s, j*c)) for i, j in labels}
    cr, sr, dr = rotation_den**2-1, -2*rotation_den, rotation_den**2+1
    if wrong_sign:
        sr = -sr
    L = L0*dr
    anchor_x = anchor_i*L0
    points = {}
    for label, (x, y) in base.items():
        if label[1] < 0:
            points[label] = scale(x, dr), scale(y, dr)
        else:
            x_rel = sub(x, (anchor_x, 0))
            points[label] = (add((anchor_x*dr, 0),
                                sub(scale(x_rel, cr), scale(y, sr))),
                             add(scale(x_rel, sr), scale(y, cr)))
    return labels, points, L, (anchor_i, 0), (anchor_i, -1), (c, s, d, cr, sr, dr)


def verify(Q, independent=False):
    labels, points, L, anchor, lower_anchor, pars = make_source(Q)
    n = len(labels)
    expected = set()
    for p in labels:
        for q in ((p[0]+1, p[1]), (p[0], p[1]+1)):
            if q in points and ((p[1] < 0) == (q[1] < 0)):
                expected.add(frozenset((p, q)))
    expected.add(frozenset((anchor, lower_anchor)))
    contacts, diameters = [], []
    maximum = (0, 0)
    pair_count = 0
    for k, p in enumerate(labels):
        for q in labels[k+1:]:
            z = norm2(delta(points[p], points[q]))
            assert sign(z[0]-L*L, z[1]) >= 0, (Q, p, q, "lower pair")
            if z == (L*L, 0):
                contacts.append((p, q))
            comparison = sign(*sub(z, maximum))
            if comparison > 0:
                maximum, diameters = z, [(p, q)]
            elif comparison == 0:
                diameters.append((p, q))
            pair_count += 1
    assert {frozenset(e) for e in contacts} == expected
    is_connected, adj = connected(labels, contacts)
    assert is_connected
    for p in labels:
        for q in adj[p]:
            assert not set(adj[p]).intersection(adj[q]), "triangle"
    cross = [(p, q) for p, q in contacts if (p[1] < 0) != (q[1] < 0)]
    assert len(cross) == 1
    # Original centered lattice crop has actual diameter squared 4Q.
    assert max(i*i+i*j+j*j for i, j in labels) == Q
    assert sign(maximum[0]-4*Q*L*L, maximum[1]) > 0
    pi_lo, pi_hi = pi_bounds()
    # D^2*pi < 2sqrt3(n-1), with an upper bound for pi.
    assert sign(-pi_hi.numerator*maximum[0],
                2*(n-1)*L*L*pi_hi.denominator-pi_hi.numerator*maximum[1]) > 0
    cells = [[], []]
    for i, j in labels:
        vs = ((i, j), (i+1, j), (i+1, j+1), (i, j+1))
        if all(p in points for p in vs) and j != -1:
            cells[int(j >= 0)].append((i, j, vs))
    R = sum(map(len, cells))
    assert len(contacts)-n+1 == R, "all bounded faces accounted for"
    B, V, E, chi, trains = 0, set(), set(), 0, []
    for component in cells:
        edges = Counter()
        cv = set()
        for i, j, vs in component:
            cv.update(vs)
            for k in range(4):
                edges[frozenset((vs[k], vs[(k+1) % 4]))] += 1
        cb = sum(v == 1 for v in edges.values())
        counts = len({i for i, j, vs in component}), len({j for i, j, vs in component})
        assert cb == 2*sum(counts), "train boundary count"
        B += cb
        V.update(cv)
        E.update(edges)
        chi += len(cv)-len(edges)+len(component)
        trains.append(counts)
    t = n-len(V)
    assert n == R+B//2+chi+t
    hp = hull(list(points.values()))
    twice_area = (0, 0)
    for p, q in zip(hp, hp[1:]+hp[:1]):
        twice_area = add(twice_area, det(p, q))
    assert sign(-twice_area[0], (n-1)*L*L-twice_area[1]) > 0, "shell upper window"
    c, s, d, cr, sr, dr = pars
    # G = area(K)-R*sin(theta) >= 0; all terms use denominator 2L^2.
    sin_theta = (s, c)  # denominator 2d
    assert sign(*sub(twice_area, scale(sin_theta, R*L*L//d))) >= 0
    u = ((L, 0), (0, 0))
    v = ((c*(L//(2*d)), -s*(L//(2*d))),
         (s*(L//(2*d)), c*(L//(2*d))))
    def rot(z):
        # Coordinates share L and every numerator is divisible by dr here.
        x, y = z
        result = sub(scale(x, cr), scale(y, sr)), add(scale(x, sr), scale(y, cr))
        assert all(k % dr == 0 for field in result for k in field)
        return tuple(tuple(k//dr for k in field) for field in result)
    vectors = (u, v), (rot(u), rot(v))
    M = (0, 0)
    for i in range(2):
        for j in range(2):
            z = det(vectors[0][i], vectors[1][j])
            if sign(*z) < 0:
                z = scale(z, -1)
            M = add(M, scale(z, trains[0][i]*trains[1][j]))
    assert sign(*sub(scale(M, 2), maximum)) > 0, "quadratic virtual mass fixture"
    loaded = set(p for edge in diameters for p in edge)
    pinned_nullity_floor = 2*(n-len(loaded))-len(contacts)
    assert pinned_nullity_floor > 0, "fixture must not pass jammed scope"
    if independent:
        # Separate Fraction-based squaring and sign comparisons for every pair.
        fp = {p: tuple(tuple(Fraction(k, L) for k in z) for z in points[p]) for p in labels}
        for k, p in enumerate(labels):
            for q in labels[k+1:]:
                x, y = delta(fp[p], fp[q])
                ref = (x[0]**2+3*x[1]**2+y[0]**2+3*y[1]**2,
                       2*(x[0]*x[1]+y[0]*y[1]))
                fast = norm2(delta(points[p], points[q]))
                assert ref == tuple(Fraction(z, L*L) for z in fast)
                assert sign(ref[0]-1, ref[1]) >= 0
    # Negative control: the opposite hinge sign contracts a former seam contact.
    _, bad, badL, _, _, _ = make_source(Q, wrong_sign=True)
    k = anchor[0]-1
    assert (k, 0) in bad and (k, -1) in bad
    badz = norm2(delta(bad[(k, 0)], bad[(k, -1)]))
    assert sign(badz[0]-badL*badL, badz[1]) < 0
    # Negative control: without shear, one chart contains an exact unit triangle.
    assert all(p in points for p in ((0, 0), (1, 0), (0, 1)))
    assert all(i*i+i*j+j*j == 1 for i, j in ((1, 0), (0, 1), (1, -1)))
    return {"Q": Q, "labels": n, "all_source_pairs": pair_count,
            "contacts": len(contacts), "cross_contacts": len(cross),
            "rhombi": list(map(len, cells)), "train_counts": trains,
            "B": B, "chi": chi, "t": t, "loaded_vertices": len(loaded),
            "pinned_nullity_floor": pinned_nullity_floor,
            "D2_numerator": list(maximum), "coordinate_denominator": L,
            "M_inter_numerator": list(M), "hull_vertices": len(hp),
            "independent_fraction_replay": independent}


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run without -O: certificate assertions must execute.")
    _, pi_hi = pi_bounds()
    pi_lo, _ = pi_bounds()
    # The analytic fixed-deficit limit lies strictly between 1/8 and 1/6.
    assert sign(36-24*pi_hi, 25) > 0
    assert sign(24-18*pi_lo, 17) < 0
    records = [verify(Q, independent=(Q == 7)) for Q in (7, 19, 31, 61, 100, 217)]
    print(json.dumps({"status": "PASS", "arithmetic": "exact Q(sqrt(3))",
                      "total_pairs": sum(r["all_source_pairs"] for r in records),
                      "fixtures": records}, indent=2))
