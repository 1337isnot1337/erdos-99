#!/usr/bin/env python3
"""Finite exact boundary regressions for the palette-transversal equivalence."""

from fractions import Fraction as F
from itertools import combinations, product

D_SQUARED = F(4)
POINTS = (
    (F(0), F(0)),
    (F(1, 2), F(0)),
    (F(1), F(0)),
    (F(3, 2), F(0)),
    (F(2), F(0)),
    (F(5, 2), F(0)),
    (F(0), F(1)),
)


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def squared_distance(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def admissible(p, q):
    d2 = squared_distance(p, q)
    return d2 >= 1 and d2 < D_SQUARED


def conflict_edges(domains):
    vertices = [(i, option) for i, domain in enumerate(domains)
                for option in range(len(domain))]
    edges = set()
    for left, right in combinations(vertices, 2):
        i, a = left
        j, b = right
        if i == j or not admissible(POINTS[domains[i][a]], POINTS[domains[j][b]]):
            edges.add(frozenset((left, right)))
    return edges


def compare_all_transversals(domains):
    edges = conflict_edges(domains)
    assignments = 0
    for choice in product(*(range(len(domain)) for domain in domains)):
        assignments += 1
        selected_vertices = [(i, option) for i, option in enumerate(choice)]
        independent = all(frozenset(pair) not in edges
                         for pair in combinations(selected_vertices, 2))
        selected_points = [POINTS[domain[option]]
                           for domain, option in zip(domains, choice)]
        direct_endpoint = all(admissible(p, q)
                              for p, q in combinations(selected_points, 2))
        check(independent == direct_endpoint, (domains, choice))
    return assignments


def main():
    # Boundary controls for D=2: equality at 1 is allowed; equality at D is not.
    check(admissible(POINTS[0], POINTS[2]), "distance 1 must be allowed")
    check(not admissible(POINTS[0], POINTS[4]), "distance D must be rejected")
    check(not admissible(POINTS[0], POINTS[1]), "distance below 1 must be rejected")
    check(admissible(POINTS[0], POINTS[3]), "distance strictly below D must be allowed")

    domains = [tuple(c) for size in (1, 2) for c in combinations(range(len(POINTS)), size)]
    check(len(domains) == 28, "expected 28 one- or two-option domains")
    two_label_assignments = sum(compare_all_transversals((a, b))
                                for a in domains for b in domains)
    check(two_label_assignments == 2401, "unexpected two-label assignment count")

    small_domains = ((0,), (2,), (0, 2), (3, 4), (5, 6))
    three_label_assignments = sum(compare_all_transversals((a, b, c))
                                  for a, b, c in product(small_domains, repeat=3))
    check(three_label_assignments == 512, "unexpected three-label assignment count")
    check(compare_all_transversals(((0,), (), (1,))) == 0,
          "empty label class must have no full transversal")

    print("PASS exact boundary controls: d=1 allowed, d=D forbidden, below-one forbidden, below-D allowed")
    print("PASS 784 ordered two-label palettes and", two_label_assignments, "direct assignments")
    print("PASS 125 selected three-label palettes and", three_label_assignments, "direct assignments")
    print("PASS empty label class admits neither endpoint nor transversal")
    print("SCOPE: finite regression controls only; the general equivalence is proved in README.md")


main()
