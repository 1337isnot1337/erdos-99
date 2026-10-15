#!/usr/bin/env python3
"""Exact finite regressions for the good-hull train depletion candidate.

Fraction arithmetic checks full pair constraints, actual contacts/diameters,
strict hull sides, complete stopped trains and endpoint multiplicities in
small square/oblique grids. It certifies constants with alternating-series
Machin bounds. It does not prove disk convergence, the finite angular cap,
global optimality, or the infinite Type-II depletion theorem.
"""
if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from fractions import Fraction as F
from itertools import combinations, product


def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def hull(points):
    ordered = sorted(range(len(points)), key=points.__getitem__)
    chains = []
    for sequence in (ordered, list(reversed(ordered))):
        chain = []
        for i in sequence:
            while len(chain) >= 2 and cross(points[chain[-2]], points[chain[-1]], points[i]) <= 0:
                chain.pop()
            chain.append(i)
        chains.append(chain[:-1])
    return chains[0] + chains[1]


def edge(a, b):
    return tuple(sorted((a, b)))


def packet(j, v):
    labels = list(product(range(j+1), repeat=2))
    index = {label: i for i, label in enumerate(labels)}
    points = [(F(a)+b*v[0], b*v[1]) for a, b in labels]
    distances = {}
    for a, b in combinations(range(len(points)), 2):
        distances[a, b] = sum((points[a][d]-points[b][d])**2 for d in (0, 1))
    assert min(distances.values()) == 1
    contacts = {e for e, s in distances.items() if s == 1}
    expected = {edge(index[a, b], index[a+1, b]) for a in range(j) for b in range(j+1)}
    expected |= {edge(index[a, b], index[a, b+1]) for a in range(j+1) for b in range(j)}
    assert contacts == expected
    assert not any(all(edge(a, b) in contacts for a, b in combinations(triple, 2))
                   for triple in combinations(range(len(points)), 3))
    diameter2 = max(distances.values())
    diameters = {e for e, s in distances.items() if s == diameter2}
    assert diameter2 == 2*j*j*(1+v[0])
    assert len(diameters) == (2 if v[0] == 0 else 1)

    strict_hull = hull(points)
    assert len(strict_hull) == 4
    hull_sides = [edge(strict_hull[i], strict_hull[(i+1) % 4]) for i in range(4)]
    assert all(distances[s] == j*j for s in hull_sides)
    good_sides = set(hull_sides) & contacts
    assert len(good_sides) == (4 if j == 1 else 0)

    links = {e: [] for e in contacts}
    for a, b in product(range(j), repeat=2):
        cell = [index[a, b], index[a+1, b], index[a+1, b+1], index[a, b+1]]
        sides = [edge(cell[i], cell[(i+1) % 4]) for i in range(4)]
        assert all(s in contacts for s in sides)
        assert distances[edge(cell[0], cell[2])] > 1
        assert distances[edge(cell[1], cell[3])] > 1
        for first, second in ((sides[0], sides[2]), (sides[1], sides[3])):
            links[first].append(second)
            links[second].append(first)
    unseen = set(contacts)
    trains = []
    while unseen:
        pending = [min(unseen)]
        component = set()
        while pending:
            current = pending.pop()
            if current in component:
                continue
            component.add(current)
            pending.extend(links[current])
        unseen -= component
        assert sum(len(links[c]) for c in component) == 2*(len(component)-1)
        terminal = [c for c in component if len(links[c]) == 1]
        assert len(terminal) == 2
        trains.append((component, terminal))
    train_of = {c: i for i, (cs, _) in enumerate(trains) for c in cs}
    crossings = set()
    for a, b in product(range(j), repeat=2):
        cell = [index[a, b], index[a+1, b], index[a+1, b+1], index[a, b+1]]
        crossing = edge(train_of[edge(cell[0], cell[1])], train_of[edge(cell[1], cell[2])])
        assert crossing not in crossings
        crossings.add(crossing)
    assert len(crossings) == j*j
    assert not any(all(edge(a, b) in crossings for a, b in combinations(triple, 2))
                   for triple in combinations(range(len(trains)), 3))
    good_per_train = [sum(c in good_sides for c in ends) for _, ends in trains]
    G = sum(good_per_train)
    N = sum(g > 0 for g in good_per_train)
    double = sum(g == 2 for g in good_per_train)
    R = j*j
    T = len(trains)
    e, b = len(contacts), 4*j
    assert T == 2*j == e-2*R == b//2
    assert N == G-double and double <= 2 and T >= G-2
    E_G = sum(good_per_train[a] > 0 or good_per_train[b] > 0 for a, b in crossings)
    assert 4*(R-E_G) <= (T-N)**2
    if j == 1:
        assert (G, N, double, E_G, T, R) == (4, 2, 2, 1, 2, 1)
        assert (T-N)**2 < 4*R  # The proposed error-free finite bound is false.
    else:
        assert G == N == double == E_G == 0
    if v[0] > 0:
        # The same-cardinality unit square grid is a strict diameter competitor.
        assert 2*j*j < diameter2
    return len(points), len(contacts), len(diameters), T, G


def atan_interval(x, terms):
    partial = sum(((-1)**i)*x**(2*i+1)/F(2*i+1) for i in range(terms))
    following = ((-1)**terms)*x**(2*terms+1)/F(2*terms+1)
    return min(partial, partial+following), max(partial, partial+following)


def sqrt_interval(lo, hi):
    def bracket(x):
        left, right = F(0), max(F(1), x)
        for _ in range(150):
            middle = (left+right)/2
            if middle*middle < x:
                left = middle
            else:
                right = middle
        return left, right
    return bracket(lo)[0], bracket(hi)[1]


# Verify the rational tangent calculation behind Machin's identity.
t = F(1, 5)
t2 = 2*t/(1-t*t)
t4 = 2*t2/(1-t2*t2)
assert (t4-F(1, 239))/(1+t4/F(239)) == 1
al, ah = atan_interval(F(1, 5), 40)
bl, bh = atan_interval(F(1, 239), 10)
pi_lo, pi_hi = 16*al-4*bh, 16*ah-4*bl
assert F(3141592653589793238, 10**18) < pi_lo < pi_hi < F(3141592653589793239, 10**18)
r3_lo, r3_hi = sqrt_interval(F(3), F(3))
s_lo, s_hi = sqrt_interval(pi_lo/(2*r3_hi), pi_hi/(2*r3_lo))
threshold_lo = (3*pi_lo+2*s_lo)/5
threshold_hi = (3*pi_hi+2*s_hi)/5
outer_lo = (3*pi_lo+2*s_lo-5*F(186, 100))/2
outer_hi = (3*pi_hi+2*s_hi-5*F(186, 100))/2
assert F(22658, 10000) < threshold_lo < threshold_hi < F(22659, 10000)
assert F(10147, 10000) < outer_lo < outer_hi < F(10148, 10000)
assert 3*pi_lo/5 > F(186, 100)

packets = [packet(j, v) for v in ((F(0), F(1)), (F(5, 13), F(12, 13))) for j in range(1, 7)]
print(f"PASS: {len(packets)} exact full-pair source packets; actual supports, strict hulls, trains, and crossings")
print("PASS: square attains the two-double-good correction and refutes the error-free finite depletion bound")
print("PASS: wall unit-edge occurrences are not unit sides of the strict convex hull")
print("PASS: rational enclosures certify 2.2658<threshold<2.2659 and 1.0147<outer floor<1.0148")
print("SCOPE: finite regression/arithmetic only; no global minimizer or Type-II theorem is computationally certified")
