#!/usr/bin/env python3
"""Exact finite audit of the contiguity and hull-side-cover candidate.

This checks examples; the analytic report proves the universal statement.
All geometry and direction sorting use integers or Fraction, never floats.
"""

from fractions import Fraction
from functools import cmp_to_key
from itertools import combinations


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    chain = []
    for p in sorted(points):
        while len(chain) > 1 and cross(chain[-2], chain[-1], p) <= 0:
            chain.pop()
        chain.append(p)
    other = []
    for p in reversed(sorted(points)):
        while len(other) > 1 and cross(other[-2], other[-1], p) <= 0:
            other.pop()
        other.append(p)
    return chain[:-1] + other[:-1]


def audit(points):
    pairs = [(a, b, (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
             for a, b in combinations(points, 2)]
    max_squared = max(s for _, _, s in pairs)
    edges = [frozenset((a, b)) for a, b, s in pairs if s == max_squared]
    vertices = set().union(*edges)
    boundary = hull(vertices)
    if len(boundary) < 3:
        return False, 0
    assert set(boundary) == vertices

    def direction(edge):
        a, b = sorted(edge)
        dx, dy = b[0] - a[0], b[1] - a[1]
        if dy < 0 or (dy == 0 and dx < 0):
            dx, dy = -dx, -dy
        return dx, dy

    def compare(a, b):
        ax, ay = direction(a)
        bx, by = direction(b)
        product = ax * by - ay * bx
        assert product != 0, "Distinct diameter pairs cannot be parallel"
        return -1 if product > 0 else 1

    edges.sort(key=cmp_to_key(compare))
    star = any(all(v in e for e in edges) for v in vertices)
    for v in vertices:
        bits = [v in e for e in edges]
        if all(bits):
            assert star
        else:
            runs = sum(bits[i] and not bits[i - 1] for i in range(len(bits)))
            assert runs == 1
    if star:
        return True, max(sum(v in e for e in edges) for v in vertices)

    sides = {frozenset((boundary[i - 1], boundary[i])) for i in range(len(boundary))}
    generated = set()
    disjoint = 0
    for i, current in enumerate(edges):
        following = edges[(i + 1) % len(edges)]
        shared = current & following
        if not shared:
            disjoint += 1
            continue
        assert len(shared) == 1
        side = current ^ following
        assert side in sides, "A shared consecutive diameter pair must generate a hull side"
        assert side not in generated
        generated.add(side)
    q, h = len(vertices), len(edges)
    assert disjoint == q - h
    assert len(generated) == 2 * h - q
    assert len(sides - generated) == 2 * (q - h)
    return True, max(sum(v in e for e in edges) for v in vertices)


def main():
    grid = [(x, y) for x in range(4) for y in range(3)]
    checked = full_dimensional = max_degree = 0
    for size in range(3, len(grid) + 1):
        for sample in combinations(grid, size):
            okay, degree = audit(sample)
            checked += 1
            full_dimensional += okay
            max_degree = max(max_degree, degree)

    # A large proper star run in a non-star diameter graph, with exact rational data.
    # The extra edge joins (1,0) to (1/5,-3/5).
    fan = [(Fraction(0), Fraction(0)), (Fraction(1, 5), Fraction(-3, 5))]
    for i in range(81):
        t = Fraction(i, 240)
        fan.append(((1 - t * t) / (1 + t * t), -2 * t / (1 + t * t)))
    okay, degree = audit(fan)
    assert okay and degree == 81
    print(f"PASS: {checked} grid subsets; {full_dimensional} with a two-dimensional loaded hull")
    print(f"PASS: rational non-star fan with maximum diameter degree {degree}")
    print("Universal claims are proved analytically; this enumeration is a finite regression audit.")


if __name__ == '__main__':
    main()
