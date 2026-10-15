#!/usr/bin/env python3
"""Exact finite checks for the hull-side train-capacity candidate.

Rational actual packings test the exterior-occurrence lemma, full contact
graphs, facial walks, complete trains and sharp capacity. The scalar checks
test only the stated identities/inequalities, not realization, KKT, global
optimality, an asymptotic theorem, C-II or Level I. The analytic proof is in
docs/reports/target_c_hull_side_exact_train_capacity_audit_2026-10-04.md.
"""

from fractions import Fraction as F
from functools import cmp_to_key
from itertools import combinations


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def norm2(a):
    return a[0] ** 2 + a[1] ** 2


def direction_cmp(a, b):
    def half(v):
        return 0 if v[1] > 0 or (v[1] == 0 and v[0] > 0) else 1
    ha, hb = half(a), half(b)
    if ha != hb:
        return -1 if ha < hb else 1
    c = cross(a, b)
    return -1 if c > 0 else 1 if c < 0 else 0


def hull(points):
    order = sorted(range(len(points)), key=points.__getitem__)
    def build(seq):
        result = []
        for i in seq:
            while len(result) > 1 and cross(
                sub(points[result[-1]], points[result[-2]]),
                sub(points[i], points[result[-1]]),
            ) <= 0:
                result.pop()
            result.append(i)
        return result
    return build(order)[:-1] + build(reversed(order))[:-1]


def check_geometry(points):
    points = [tuple(map(F, p)) for p in points]
    adjacency = [[] for _ in points]
    edges = set()
    for i, j in combinations(range(len(points)), 2):
        d = norm2(sub(points[i], points[j]))
        assert d >= 1
        if d == 1:
            edges.add((i, j))
            adjacency[i].append(j)
            adjacency[j].append(i)
    reached = {0}
    todo = [0]
    while todo:
        v = todo.pop()
        for w in adjacency[v]:
            if w not in reached:
                reached.add(w)
                todo.append(w)
    if len(reached) != len(points):
        return None
    B = hull(points)
    if len(B) < 3:
        return None
    for i, j, k in combinations(range(len(points)), 3):
        assert not all(tuple(sorted(e)) in edges for e in ((i, j), (j, k), (k, i)))
    for v, neighbors in enumerate(adjacency):
        neighbors.sort(key=cmp_to_key(
            lambda a, b: direction_cmp(sub(points[a], points[v]), sub(points[b], points[v]))
        ))
    directed = {(a, b) for a, b in edges} | {(b, a) for a, b in edges}
    unused = set(directed)
    faces = []
    while unused:
        start = min(unused)
        a, b = start
        walk = []
        while True:
            assert (a, b) in unused
            unused.remove((a, b))
            walk.append(a)
            neighbors = adjacency[b]
            c = neighbors[(neighbors.index(a) - 1) % len(neighbors)]
            a, b = b, c
            if (a, b) == start:
                break
        area2 = sum(cross(points[walk[i]], points[walk[(i + 1) % len(walk)]] )
                    for i in range(len(walk)))
        faces.append((area2, walk))
    assert len(points) - len(edges) + len(faces) == 2
    outer_index = min(range(len(faces)), key=lambda i: faces[i][0])
    assert faces[outer_index][0] <= 0
    outer = faces[outer_index][1]
    b = len(outer)
    bounded = [w for i, (a, w) in enumerate(faces) if i != outer_index]
    assert all(len(w) >= 4 for w in bounded)
    quadrilaterals = [w for w in bounded if len(w) == 4]
    exceptions = [w for w in bounded if len(w) != 4]
    f = len(exceptions)
    Q = sum(len(w) - 4 for w in exceptions)
    q = len(B)
    x = b - q
    assert x >= 0

    # At a strict hull vertex the unique outside corner has clockwise
    # angle > pi. A degree-one vertex has a single corner of angle 2pi.
    distinguished = []
    for v in B:
        occurrences = [i for i, a in enumerate(outer) if a == v]
        eligible = [i for i in occurrences if len(adjacency[v]) == 1 or cross(
            sub(points[outer[(i - 1) % b]], points[v]),
            sub(points[outer[(i + 1) % b]], points[v]),
        ) > 0]
        assert len(eligible) == 1, (points, v, outer, eligible)
        distinguished.append(eligible[0])
    # Outer walk is clockwise; convex hull routine returns counterclockwise.
    positions = list(reversed(distinguished))
    assert sum((positions[(i + 1) % q] - positions[i]) % b for i in range(q)) == b
    lengths = [(positions[(i + 1) % q] - positions[i]) % b for i in range(q)]
    good_occurrences = set()
    m = 0
    for pos, ell in zip(positions, lengths):
        end = (pos + ell) % b
        unit = norm2(sub(points[outer[pos]], points[outer[end]])) == 1
        assert (ell == 1) == unit
        if unit:
            good_occurrences.add(pos)
        else:
            m += 1
            assert ell >= 2
    assert sum(ell for ell in lengths if ell > 1) == x + m
    assert x - m == sum(ell - 2 for ell in lengths if ell > 1)

    # Complete opposite-edge train components, including singleton edges.
    links = {e: [] for e in edges}
    for w in quadrilaterals:
        assert len(set(w)) == 4
        boundary = [tuple(sorted((w[i], w[(i + 1) % 4]))) for i in range(4)]
        for i in range(2):
            a, c = boundary[i], boundary[i + 2]
            assert cross(sub(points[a[0]], points[a[1]]), sub(points[c[0]], points[c[1]])) == 0
            links[a].append(c)
            links[c].append(a)
    assert all(len(v) <= 2 for v in links.values())
    ids = {}
    N = 0
    for edge in sorted(edges):
        if edge in ids:
            continue
        component = {edge}
        todo = [edge]
        while todo:
            e = todo.pop()
            for a in links[e]:
                if a not in component:
                    component.add(a)
                    todo.append(a)
        assert sum(len(links[e]) for e in component) == 2 * (len(component) - 1)
        for e in component:
            ids[e] = N
        N += 1
    assert N == len(edges) - 2 * len(quadrilaterals)
    assert 2 * N == b + Q + 4 * f
    good_by_train = [0] * N
    for i in good_occurrences:
        e = tuple(sorted((outer[i], outer[(i + 1) % b])))
        good_by_train[ids[e]] += 1
    assert all(a <= 2 for a in good_by_train)
    assert sum(a == 2 for a in good_by_train) <= 2
    sigma = x + m + 4 * f + Q - (N - 2)
    assert sigma >= 0
    assert q <= x + 2 * m + 4 * f + Q + 4
    # tD=(b+Q)/2 is the face-ledger value; no actual KKT is claimed here.
    tD = F(b + Q, 2)
    assert 5 * tD + x + m - 3 * b + 2 == sigma + 2 * (Q - f)
    assert 5 * tD + x + m >= 3 * b - 2
    return {
        "q": q, "b": b, "x": x, "m": m, "N": N, "f": f, "Q": Q,
        "repeated": len(outer) - len(set(outer)),
        "loaded_repeated": sum(outer.count(v) - 1 for v in B),
    }


def atan_interval(x, terms):
    partial = sum(((-1) ** j) * x ** (2 * j + 1) / (2 * j + 1)
                  for j in range(terms))
    next_term = ((-1) ** terms) * x ** (2 * terms + 1) / (2 * terms + 1)
    return min(partial, partial + next_term), max(partial, partial + next_term)


def pi_interval():
    # tan(4 atan(1/5)-atan(1/239))=1, with angle in (0,pi/2).
    a, b = atan_interval(F(1, 5), 24)
    c, d = atan_interval(F(1, 239), 8)
    return 16 * a - 4 * d, 16 * b - 4 * c


def scalar_checks():
    p_lo, p_hi = pi_interval()
    assert F(314159, 100000) < p_lo < p_hi < F(314160, 100000)
    threshold_lo, threshold_hi = 3 * p_lo / 5, 3 * p_hi / 5
    assert threshold_lo > F(186, 100)
    excess_lo = (3 * p_lo - 5 * F(186, 100)) / 2
    assert excess_lo > F(6238, 100000)

    # rho=cos(rho) is below .74: cos(.74) has this strict upper bound.
    r = F(74, 100)
    assert 1 - r*r/2 + r**4/24 < r
    g = F(7707, 1000000)
    # sqrt(Delta_2)<.953, certified with sqrt(3)>1.732.
    sqrt3_lo = F(433, 250)
    assert sqrt3_lo**2 < 3
    s_hi = F(953, 1000)
    assert p_hi / (2 * sqrt3_lo) < s_hi**2
    # Entire positive collar-to-pentagon coefficient window lies below 3pi/5.
    coefficient_at_threshold_hi = 3 * (r + g) + 6 * s_hi - 13 * p_lo / 5
    assert coefficient_at_threshold_hi < -F(1, 5)
    pen_threshold_hi = (10 * p_hi + 3 * (r + g) + 6 * s_hi) / 21
    assert pen_threshold_hi < threshold_lo

    # Certified intervals for the new global candidate floor. Bisection
    # takes place over exact rational bounds, never over float arithmetic.
    lower, upper = F(1), F(2)
    for _ in range(60):
        mid = (lower + upper) / 2
        if mid**2 < 3:
            lower = mid
        else:
            upper = mid
    sqrt3_fine_lo, sqrt3_fine_hi = lower, upper
    delta_lo = p_lo / (2 * sqrt3_fine_hi)
    delta_hi = p_hi / (2 * sqrt3_fine_lo)
    lower, upper = F(0), F(1)
    for _ in range(60):
        mid = (lower + upper) / 2
        if mid**2 < delta_lo:
            lower = mid
        else:
            upper = mid
    s_lo = lower
    lower, upper = F(0), F(1)
    for _ in range(60):
        mid = (lower + upper) / 2
        if mid**2 > delta_hi:
            upper = mid
        else:
            lower = mid
    s_upper = upper
    hull_floor_lo = (p_lo + s_lo) / 2
    hull_floor_hi = (p_hi + s_upper) / 2
    assert hull_floor_lo > F(2046, 1000)
    assert hull_floor_hi < F(2048, 1000)
    assert hull_floor_hi - hull_floor_lo < F(1, 10**16)
    assert (3 * p_lo + 2 * s_lo) / 5 > 2 * p_hi / 3
    assert delta_lo > F(16, 27)  # strict endpoint grid contradiction

    # Leading scalar witness after removing x=o(D). It has no assertion of
    # geometric realization. All expressions are affine in pi, so endpoint
    # checks certify the interval. Set x=m=1/5, t=93/50, f=9/20,
    # q=pi-x, b=P=pi, Q=2t-pi. nu,c_I have zero leading coefficient.
    for p in (p_lo, p_hi):
        t, x, m, f = F(93, 50), F(1, 5), F(1, 5), F(9, 20)
        q, b, P = p - x, p, p
        Q, k = 2*t - b, q - t
        eBB, sC = q - m, m + k
        mu = eBB + 2*sC - 3*k
        assert mu == F(103, 50)
        assert 0 < f <= Q and 0 <= m <= x
        assert q - x == Q + 2*k and b + Q == 2*t
        N = t + 2*f
        sigma = x + m + 4*f + Q - N
        assert sigma > 0  # finite +2 omitted in normalized leading ledger
        assert 5*t + x + m - 3*P == sigma + 2*(Q-f)
        assert 5*mu + (x-m) - 3*m >= 3*P
        I = P - 3*x
        U = 2*x + Q
        T_fan = I - U
        assert 0 < U < I <= q and 0 < T_fan <= q
        assert T_fan == 2*P - 2*t - 5*x
        # S=0 is permitted by the October finite collar floor.
        collar_floor = 4*P - 6*t - 9*x
        assert collar_floor < 0
        S = F(0)
        assert S >= collar_floor
        assert S - x - m <= 0
        assert S - x - m - 6*(Q-f) < 0
        assert S <= 2*(eBB-k)
        assert T_fan <= 3*q - 2*eBB  # available loaded-to-unloaded incidences
        # Modern train-slack lower bound is compatible: sqrt(Delta_2)<1
        # and rho<3/4 give tau > .76 > rho+g.
        assert N - 2 > F(3, 4) + g
    return threshold_lo, threshold_hi, excess_lo, hull_floor_lo, hull_floor_hi


def depletion_ledger_checks():
    count = 0
    for q in range(3, 25):
        for x in range(q + 1):
            b = q + x
            for k in range((q - x) // 2 + 1):
                Q = q - x - 2*k
                for f in range(Q + 1):
                    tD = q - k
                    T = tD + 2*f
                    for m in range(x + 1):
                        good_ends = q - m
                        for d in range(min(2, good_ends // 2) + 1):
                            good_trains = good_ends - d
                            M = T - good_trains
                            if M < 0:
                                continue
                            cI = 3  # cancels exactly; no source realization asserted
                            muD = q + m - k - 2*cI - 4
                            slack = 4*muD + 8*cI + 18 - 2*b - M - k - 3*m
                            assert slack == 2*(Q-f) + 2-d >= 0
                            assert M <= 5*tD - 3*b + x + m + 2
                            count += 1
    return count


def main():
    counts = {"sources": 0, "repeated_walks": 0, "loaded_repeated": 0}
    for u, v in (((F(1), F(0)), (F(0), F(1))),
                 ((F(1), F(0)), (F(5, 13), F(12, 13)))):
        lattice = [(i*u[0] + j*v[0], i*u[1] + j*v[1])
                   for i in range(3) for j in range(3)]
        for mask in range(1, 1 << 9):
            points = [p for i, p in enumerate(lattice) if mask & (1 << i)]
            result = check_geometry(points)
            if result is not None:
                counts["sources"] += 1
                counts["repeated_walks"] += result["repeated"] > 0
                counts["loaded_repeated"] += result["loaded_repeated"] > 0
    star = [(0, 0), (F(5, 13), F(12, 13)), (1, 0),
            (F(5, 13), -F(12, 13))]
    result = check_geometry(star)
    assert result is not None and result["loaded_repeated"] == 2
    assert (result["x"], result["m"]) == (2, 2)
    counts["sources"] += 1
    counts["loaded_repeated"] += 1
    square = check_geometry([(0, 0), (1, 0), (1, 1), (0, 1)])
    assert square is not None
    assert (square["q"], square["b"], square["N"], square["x"], square["m"]) == (4, 4, 2, 0, 0)
    assert 5 * F(square["b"] + square["Q"], 2) == 3*4 - 2
    lo, hi, excess, mu_lo, mu_hi = scalar_checks()
    ledgers = depletion_ledger_checks()
    print("PASS:", counts)
    print("Certified 3pi/5 interval:", float(lo), float(hi))
    print("Certified x/D lower bound at t<=1.860:", float(excess))
    print("Certified new full-core floor interval:", float(mu_lo), float(mu_hi))
    print("PASS: square sharpness, repeated loaded occurrences, exact capacity/slack")
    print("PASS: positive pentagon window lies below the excluded low-excess threshold")
    print("PASS: linear-excess scalar witness allows S=I5=0; no source realization claimed")
    print("PASS: exact depletion/slack ledgers:", ledgers)


if __name__ == "__main__":
    main()
