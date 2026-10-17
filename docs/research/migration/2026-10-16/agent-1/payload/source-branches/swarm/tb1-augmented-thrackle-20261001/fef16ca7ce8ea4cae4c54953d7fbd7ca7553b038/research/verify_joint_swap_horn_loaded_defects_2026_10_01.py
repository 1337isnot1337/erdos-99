#!/usr/bin/env python3
"""Exact finite certificates for joint small-swap lower constraints.

Encodes rational source unit separation, pair-local binary translations, strict
preservation of old noncontacts, prime Horn reductions, closure feasibility,
quadratic conflict bounds, and three exact geometric/KKT regressions.
Uses Fraction and Q(sqrt(3)); there are no floating-point tolerances.

The general geometry and KKT results are proved in the accompanying report.
Random packets have no train embedding, all-topology upper-feasibility theorem,
full positive source stress, or global-optimality certificate. KKT regression
packets explicitly fail global optimality. This script cannot close C-II.
"""

from collections import deque
from fractions import Fraction as F
from itertools import combinations, product
from random import Random

from verify_ultrasmall_swap_isolate_dispatch_2026_10_01 import Q3, distance2


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(a, s):
    return tuple(x * s for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def unit(parameter):
    return (2 * parameter / (1 + parameter ** 2),
            (1 - parameter ** 2) / (1 + parameter ** 2))


def local_bad(r, di, dj):
    states = {(0, 0): r, (1, 0): add(r, di),
              (0, 1): sub(r, dj), (1, 1): sub(add(r, di), dj)}
    assert dot(r, r) > 1
    return {bits for bits, vector in states.items() if dot(vector, vector) <= 1}


def prime_constraints(bad, i, j):
    """Return implications, unary zeros, conflicts with the exact same models."""
    assert (0, 0) not in bad
    unary = set()
    if {(1, 0), (1, 1)} <= bad:
        unary.add(i)
    if {(0, 1), (1, 1)} <= bad:
        unary.add(j)
    arrows = []
    conflicts = []
    if (1, 0) in bad and i not in unary:
        arrows.append((i, j))
    if (0, 1) in bad and j not in unary:
        arrows.append((j, i))
    if (1, 1) in bad and not unary:
        conflicts.append((i, j))
    for xi, xj in product((0, 1), repeat=2):
        values = {i: xi, j: xj}
        passes = (all(not values[v] for v in unary) and
                  all(not values[a] or values[b] for a, b in arrows) and
                  all(not values[a] or not values[b] for a, b in conflicts))
        assert passes == ((xi, xj) not in bad)
    return arrows, unary, conflicts


def closure_models(k, arrows, unary, conflicts):
    outgoing = [[] for _ in range(k)]
    for i, j in arrows:
        outgoing[i].append(j)
    survivors = []
    for seed in range(k):
        closed = {seed}
        queue = deque([seed])
        while queue:
            for j in outgoing[queue.popleft()]:
                if j not in closed:
                    closed.add(j)
                    queue.append(j)
        if closed.isdisjoint(unary) and not any(i in closed and j in closed for i, j in conflicts):
            survivors.append(closed)
    return survivors


def check_source_compiler(points, owners, moves):
    k = len(moves)
    assert min(distance2(a, b) for a, b in combinations(points, 2)) > 1
    arrows, unary, conflicts = [], set(), []
    zero = (F(0), F(0))
    for p, q in combinations(range(len(points)), 2):
        i, j = owners[p], owners[q]
        if i == j:
            continue
        r = sub(points[p], points[q])
        if i is None or j is None:
            owner = j if i is None else i
            delta = scale(moves[owner], -1 if i is None else 1)
            if dot(add(r, delta), add(r, delta)) <= 1:
                unary.add(owner)
            continue
        bad = local_bad(r, moves[i], moves[j])
        a, u, c = prime_constraints(bad, i, j)
        arrows.extend(a)
        unary.update(u)
        conflicts.extend(c)
    feasible_nonzero = False
    for bits in product((0, 1), repeat=k):
        moved = [add(p, moves[i] if i is not None and bits[i] else zero)
                 for p, i in zip(points, owners)]
        geometry = min(distance2(p, q) for p, q in combinations(moved, 2)) > 1
        formula = (all(not bits[i] for i in unary) and
                   all(not bits[i] or bits[j] for i, j in arrows) and
                   all(not bits[i] or not bits[j] for i, j in conflicts))
        assert geometry == formula
        feasible_nonzero |= geometry and any(bits)
    assert bool(closure_models(k, arrows, unary, conflicts)) == feasible_nonzero
    return len(arrows), len(unary), len(conflicts)


def local_packets(rng):
    pure, double, all_tables = 0, 0, set()
    for _ in range(6000):
        a = F(1, rng.randrange(6, 70))
        b = a * F(rng.randrange(1, 100), 100)
        vi, vj = unit(F(rng.randrange(-2, 3), rng.randrange(100, 1000))), \
                 unit(F(rng.randrange(-2, 3), rng.randrange(100, 1000)))
        di, dj = scale(vi, a), scale(vj, b)
        r = (1 - a * a * F(rng.randrange(1, 80), 1000),
             -a * F(rng.randrange(1, 100), 100))
        if dot(r, r) <= 1:
            continue
        bad = local_bad(r, di, dj)
        all_tables.add(tuple(sorted(bad)))
        prime_constraints(bad, 0, 1)
        assert dot(di, dj) > 0
        if {(1, 0), (0, 1)} <= bad:
            assert (1, 1) in bad
            double += 1
        if bad == {(1, 1)}:
            pure += 1
            kappa = sum(abs(x - y) for x, y in zip(vi, vj))
            slack = dot(r, r) - 1
            assert slack < a * a + 2 * a * kappa + a * a * kappa * kappa
            kappa0 = max(sum(abs(x - y) for x, y in zip(v, (F(0), F(1))))
                         for v in (vi, vj))
            assert abs(r[1]) < a + (1 + a) * kappa0
    # Deliberately make both singleton states bad in a very small acute cone.
    r = (F(1000001, 1000000), F(0))
    vi, vj = unit(F(-1, 100)), unit(F(1, 100))
    di, dj = scale(vi, F(1, 10000)), scale(vj, F(1, 10000))
    bad = local_bad(r, di, dj)
    assert bad == {(1, 0), (0, 1), (1, 1)}
    prime_constraints(bad, 0, 1)
    double += 1
    assert pure > 0 and double > 0
    return pure, double, len(all_tables)


def source_packets(rng):
    arrows = zeros = conflicts = 0
    for _ in range(120):
        points = []
        for _ in range(200):
            p = (F(rng.randrange(-250, 251), 100), F(rng.randrange(-250, 251), 100))
            if all(distance2(p, q) > 1 for q in points):
                points.append(p)
            if len(points) == 8:
                break
        k = 4
        owners = [rng.choice([None, *range(k)]) for _ in points]
        moves = [scale(unit(F(rng.randrange(-2, 3), 100)), F(rng.randrange(1, 10), 100))
                 for _ in range(k)]
        a, z, c = check_source_compiler(points, owners, moves)
        arrows += a
        zeros += z
        conflicts += c
    assert arrows + zeros > 0
    return arrows, zeros, conflicts


def regressions():
    for denominator in (10, 100, 1000, 10000):
        a = F(1, denominator)
        r = (1 - a * a / 16, -a / 2)
        bad = local_bad(r, (F(0), a), (F(0), a / 2))
        assert bad == {(1, 1)}
        assert 0 < dot(r, r) - 1 < a * a
    d = F(41, 18)
    p, x = (F(0), F(0)), (-d, F(0))
    a, b = (F(9, 41), F(40, 41)), (F(9, 41), -F(40, 41))
    points = [p, x, scale(a, -1), scale(b, -1)]
    lengths = [distance2(q, r) for q, r in combinations(points, 2)]
    assert min(lengths) >= 1 and max(lengths) == d * d
    assert distance2(x, scale(a, -1)) == distance2(x, scale(b, -1)) == d * d
    assert d * d * dot(add(a, b), add(a, b)) == 1
    # Full positive KKT packet, three unit-contact leaves and outer H triangle.
    zero = (Q3(), Q3())
    outer = [(Q3(F(1)), Q3()),
             (Q3(F(-1, 2)), Q3(F(0), F(1, 2))),
             (Q3(F(-1, 2)), Q3(F(0), F(-1, 2)))]
    assert all(distance2(p, zero) == Q3(F(1)) for p in outer)
    assert all(distance2(p, q) == Q3(F(3)) for p, q in combinations(outer, 2))
    for p in outer:
        force = zero
        for q in outer:
            if q != p:
                force = add(force, scale(sub(p, q), F(1, 3)))
        assert force == p
        cross_signs = [p[0] * (p[1] - q[1]) - p[1] * (p[0] - q[0])
                       for q in outer if q != p]
        assert cross_signs[0] * cross_signs[1] < 0
    assert add(add(outer[0], outer[1]), outer[2]) == zero
    # Full positive contact-path / single-diameter threshold packet.
    chain = [(F(i), F(0)) for i in range(4)]
    for i, p in enumerate(chain):
        contact_force = (F(0), F(0))
        for j in (i - 1, i + 1):
            if 0 <= j < 4:
                contact_force = add(contact_force, scale(sub(p, chain[j]), 3))
        diameter_force = sub(p, chain[3 - i]) if i in (0, 3) else (F(0), F(0))
        assert contact_force == diameter_force
    # A unit square gives a strict smaller diameter at the same cardinality
    # for both KKT packets; neither regression is a global minimizer.
    square = [(F(0), F(0)), (F(1), F(0)), (F(1), F(1)), (F(0), F(1))]
    assert min(distance2(p, q) for p, q in combinations(square, 2)) == 1
    assert max(distance2(p, q) for p, q in combinations(square, 2)) == 2


def main():
    rng = Random(991001601)
    regressions()
    pure, double, tables = local_packets(rng)
    arrows, zeros, conflicts = source_packets(rng)
    print(f"PASS: {pure} rational pure conflicts; {double} double-singleton blockers; {tables} truth tables")
    print(f"PASS: 120 unit-separated source packets and all binary patterns; "
          f"{arrows} arrows, {zeros} unary zeros, {conflicts} pure conflicts")
    print("PASS: unequal-parallel conflict at four scales; sharp loaded-contact geometry")
    print("PASS: full positive KKT hub/threshold packets, with strict same-cardinality competitors")
    print("Scope: exact finite lower geometry and stress regressions; no global-optimality or train certificate")


if __name__ == "__main__":
    main()
