#!/usr/bin/env python3
"""Exact discovery/certificate for positive pinned high-degree face tails.

Every coordinate and stress is rational. The finite certificate checks all
source pairs, the entire actual contact and diameter sets, strict hull pins,
positive unloaded equilibrium, and an explicit pinned rigidity minor. It does
not certify global optimality or a signed contact/actual-diameter KKT stress.
The report proves the infinite construction separately.
"""
from fractions import Fraction as F
from itertools import combinations


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    return a[0]-b[0], a[1]-b[1]


def mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


def norm2(a):
    return a[0]*a[0]+a[1]*a[1]


def edge(a, b):
    return tuple(sorted((a, b)))


def hull(points):
    ordered = sorted(range(len(points)), key=points.__getitem__)
    halves = []
    for order in (ordered, list(reversed(ordered))):
        stack = []
        for i in order:
            while len(stack) > 1 and cross(sub(points[stack[-1]], points[stack[-2]]),
                                           sub(points[i], points[stack[-1]])) <= 0:
                stack.pop()
            stack.append(i)
        halves.append(stack[:-1])
    return halves[0]+halves[1]


def construction(length):
    assert length >= 12 and length % 2 == 0
    half = []
    bottom = [(F(0), F(-24, 25))]
    for i in range(1, length+1):
        t = F(2*i-length-1, 100*length*length)
        h = ((1-t*t)/(1+t*t), 2*t/(1+t*t))
        half.append(h)
        bottom.append(add(bottom[-1], mul(h, h)))
    width = bottom[-1][0]
    assert bottom[-1][1] == F(-24, 25)
    right = (width+F(7, 25), F(0))
    left = (F(-7, 25), F(0))
    inner = bottom+[right]+[(x, -y) for x, y in reversed(bottom)]+[left]
    half_edges = half+[(F(4, 5), F(3, 5)), (F(3, 5), F(4, 5))]
    half_edges += [(h[1], h[0]) for h in reversed(half)]
    half_edges += [(F(-3, 5), F(4, 5)), (F(-4, 5), F(3, 5))]
    size = len(inner)
    assert len(half_edges) == size
    tips = {length+1, size-1}
    points = list(inner)
    spokes = {}
    for i in range(size):
        previous, following = half_edges[i-1], half_edges[i]
        if cross(previous, following) < 0:
            following = (-following[0], -following[1])
        beta = 2*cross(previous, following)
        product = mul(previous, following)
        outward = (product[1], -product[0])
        assert beta > 0 and norm2(outward) == 1
        vectors = [(outward, beta)]
        if i in tips:
            sign = 1 if i == length+1 else -1
            vectors = [((F(sign*4, 5), F(3, 5)), F(7, 20)),
                       ((F(sign*4, 5), F(-3, 5)), F(7, 20))]
        equilibrium = add(sub(inner[i-1], inner[i]),
                          sub(inner[(i+1) % size], inner[i]))
        for vector, weight in vectors:
            j = len(points)
            points.append(add(inner[i], vector))
            spokes[i, j] = weight
            equilibrium = add(equilibrium, (weight*vector[0], weight*vector[1]))
        assert equilibrium == (0, 0)
    expected = {edge(i, (i+1) % size) for i in range(size)} | set(spokes)
    return points, inner, spokes, expected, width


def certificate(length):
    points, inner, spokes, expected, width = construction(length)
    size = len(inner)
    pair_count = 0
    actual = set()
    diameter2, diameters = F(0), set()
    for i, j in combinations(range(len(points)), 2):
        d2 = norm2(sub(points[i], points[j]))
        assert d2 >= 1, (length, i, j, float(d2))
        if d2 == 1:
            actual.add((i, j))
        if d2 > diameter2:
            diameter2, diameters = d2, {(i, j)}
        elif d2 == diameter2:
            diameters.add((i, j))
        pair_count += 1
    assert actual == expected, (length, actual-expected, expected-actual)
    pins = set(range(size, len(points)))
    assert set(hull(points)) == pins, (length, len(hull(points)), len(pins))
    assert len(diameters) == 2
    assert len({i for pair in diameters for i in pair}) == 4
    assert diameter2 == (width+F(54, 25))**2+F(36, 25)
    non_tip_bound = (width+F(61, 50))**2+F(99, 25)**2
    tip_to_other_bound = (width+F(169, 100))**2+F(129, 50)**2
    assert diameter2-non_tip_bound == F(47, 25)*width-F(27661, 2500) > 0
    assert diameter2-tip_to_other_bound == F(47, 50)*width-F(34069, 10000) > 0
    assert 2*len(points) < length*length < diameter2
    # A ceil(sqrt(n)) square-grid box is a strict same-cardinality competitor.
    # Its squared diameter is strictly below 2n; no global optimality is claimed.

    assert size == 2*length+4 and len(points) == 4*length+10
    assert len(actual) == len(points)
    assert all(cross(sub(inner[(i+1) % size], inner[i]),
                     sub(inner[(i+2) % size], inner[(i+1) % size])) > 0
               for i in range(size))
    area = sum(cross(inner[i], inner[(i+1) % size]) for i in range(size))/2
    assert 0 < area <= F(49, 25)*(length+F(14, 25))
    assert F(length)-F(1, 1250*length) <= width <= length
    assert diameter2 < (length+3)**2
    assert all(F(-61, 100) <= x <= width+F(61, 100) and abs(y) <= F(99, 50)
               for i, (x, y) in enumerate(points)
               if i not in {size-1, length+1} and
               not (i >= size and next(a for a, b in spokes if b == i) in {size-1, length+1}))
    adjacency = [set() for _ in points]
    for i, j in actual:
        adjacency[i].add(j)
        adjacency[j].add(i)
    assert not any(adjacency[i] & adjacency[j] for i, j in actual)
    assert all(len(adjacency[i]) == (4 if i in {length+1, size-1} else 3)
               for i in range(size))
    assert all(len(adjacency[i]) == 1 for i in pins)

    # A 2*size-row minor: two nonparallel left-tip pins fix its velocity,
    # then its incident cycle edge and one spoke fix each successive vertex.
    anchor = size-1
    anchor_vectors = [sub(points[j], inner[anchor]) for i, j in spokes if i == anchor]
    assert len(anchor_vectors) == 2 and cross(*anchor_vectors) != 0
    factors = [cross(*anchor_vectors)]
    for offset in range(1, size):
        i = (anchor+offset) % size
        incoming = sub(inner[i], inner[i-1])
        vector = next(sub(points[j], inner[i]) for a, j in spokes if a == i)
        factor = cross(incoming, vector)
        assert factor != 0
        factors.append(factor)
    determinant = F(1)
    for factor in factors:
        determinant *= factor
    assert determinant != 0
    return pair_count, size, len(pins), len(actual), len(diameters)


if __name__ == "__main__":
    results = [certificate(length) for length in (12, 16, 24, 32)]
    print(f"PASS: {sum(r[0] for r in results)} exact all-source pair checks in {len(results)} packets")
    print("PASS: rational unit contacts only; triangle-free, convex face and every pin strictly extreme")
    print("PASS: strictly positive unloaded equilibrium and four explicit full-rank pinned minors")
    print("PASS: two actual diameter edges; only four pins are actual diameter endpoints")
    print("PASS: same-cardinality square-grid competitors prove all packets nonglobal")
    print("SCOPE: regression for positive pinned hypotheses; no canonical signed stress or C-II closure")
