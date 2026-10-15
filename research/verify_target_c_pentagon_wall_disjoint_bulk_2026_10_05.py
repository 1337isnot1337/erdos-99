#!/usr/bin/env python3
"""Exact bounded-overlap thinning of terminal-wall incidence packets.

Wall rosters and crossing graphs below are abstract finite incidence data,
not embedded contact packings or optimal sources. Rational Bernoulli
enumeration checks the probabilistic argument. The analytic source train
span bound is not inferred from these abstract rosters.
"""
from fractions import Fraction as F
from itertools import combinations


def conflicts(walls, ends):
    assert all(len(w) == 5 for w in walls)
    assert all(sum(v in w for w in walls) <= 5 for v in set().union(*walls))
    assert all(sum(pair.count(f) for pair in ends) <= 5 for f in range(len(walls)))
    good = {i for i, (a, b) in enumerate(ends) if not walls[a] & walls[b]}
    supports = {i: walls[ends[i][0]] | walls[ends[i][1]] for i in good}
    neighbors = {i: set() for i in good}
    for i, j in combinations(good, 2):
        if supports[i] & supports[j]:
            neighbors[i].add(j)
            neighbors[j].add(i)
    assert all(len(ns) <= 250 for ns in neighbors.values())
    return good, supports, neighbors


def enumerate_packet(walls, ends, crossings):
    good, supports, neighbors = conflicts(walls, ends)
    eligible = {tuple(sorted((i, j))) for i, j in crossings
                if i in good and j in good and j not in neighbors[i]}
    p, bound = F(1, 251), F(250, 251)
    c = p*p*bound**500
    vertices = sorted(good)
    expectation, total_probability, best = F(0), F(0), 0
    for mask in range(1 << len(vertices)):
        chosen = {v for k, v in enumerate(vertices) if mask >> k & 1}
        retained = {v for v in chosen if not neighbors[v] & chosen}
        assert all(not supports[i] & supports[j] for i, j in combinations(retained, 2))
        bulk = sum(i in retained and j in retained for i, j in crossings)
        probability = p**len(chosen)*bound**(len(vertices)-len(chosen))
        total_probability += probability
        expectation += probability*bulk
        best = max(best, bulk)
    exact_formula = sum(p*p*bound**len(neighbors[i] | neighbors[j])
                        for i, j in eligible)
    assert total_probability == 1 and expectation == exact_formula
    assert expectation >= c*len(eligible) and best >= expectation
    return 1 << len(vertices), len(eligible)


def rosters(n, shared):
    walls = [{5*f+i for i in range(5)} for f in range(n)]
    for a, b in shared:
        # Each face participates in at most two sharing pairs below.
        used = {v for v in walls[a] if v >= 5*n}
        old_a = next(v for v in walls[a] if v < 5*n)
        old_b = next(v for v in walls[b] if v < 5*n)
        common = 5*n+len(used)+7*a+11*b
        while common in set().union(*walls):
            common += 1
        walls[a].remove(old_a)
        walls[b].remove(old_b)
        walls[a].add(common)
        walls[b].add(common)
    return walls


if __name__ == "__main__":
    checks, eligible = 0, 0
    for n in (5, 6, 7):
        for sharing in ([], [(0, 1)], [(0, 1), (2, 3)]):
            walls = rosters(n, sharing)
            ends = [(i, (i+1) % n) for i in range(n)]
            if n == 5:
                ends += [(0, 0)]  # two occurrences on the same pentagon
            if n >= 6:
                ends += [(i, i+n//2) for i in range(2)]
            if n == 6:
                ends += [(0, 1)]  # distinct trains may repeat a face pair here
            middle = len(ends)//2
            crossings = {(i, j) for i in range(middle)
                         for j in range(middle, len(ends))}
            count, e = enumerate_packet(walls, ends, crossings)
            checks += count
            eligible += e
    # A saturated abstract roster audit: many trains share an endpoint
    # face, but every wall has five vertices and at most five train ends.
    n = 100
    walls = rosters(n, [(2*i, 2*i+1) for i in range(n//2)])
    ends = [(i, (i+s) % n) for i in range(n) for s in (1, 2)]
    good, _, neighbors = conflicts(walls, ends)
    assert sum(len(ns) for ns in neighbors.values()) <= 250*len(good)
    # Unit-pentagon terminal midpoint separation <=4, while each crossed
    # unit rhombus contributes at least sqrt(3)/2 in monotone projection:
    # five crossings would already have projection >4.
    assert 5*5*3 > 4*4*4
    print(f"PASS: {checks} exact Bernoulli outcomes and {eligible} nonconflicting crossing-pair probabilities")
    print("PASS: retained families have pairwise disjoint ten-vertex terminal-wall supports")
    print("PASS: five-face vertex incidence, five train ends per face and degree-250 conflict bound")
    print("PASS: exact thinning constant (1/251)^2 (250/251)^500")
    print("PASS: integer squared check that five monotone rhombi exceed a four-unit endpoint span")
    print("SCOPE: abstract incidence and exact probability; no source embedding, load activation or optimum")
