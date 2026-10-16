#!/usr/bin/env python3
"""Exact example audit of antipode transitions, not a universal proof.

Integer/Fraction comparisons certify normal exposure, radius-vector order,
and separation-sensitive turning bounds. No floating-point angles are used.
"""

from fractions import Fraction as F
from itertools import combinations

from verify_diameter_star_contiguity import hull


def squared(a, b):
    return sum((x-y)**2 for x, y in zip(a, b))


def cosine_at_most(dot, norm_product, bound):
    """Check dot/sqrt(norm_product) <= bound by sign-aware squaring."""
    if bound >= 0:
        return dot <= 0 or dot**2 <= bound**2 * norm_product
    return dot < 0 and dot**2 >= bound**2 * norm_product


def audit(points):
    pairs = [(a, b, squared(a, b)) for a, b in combinations(points, 2)]
    diameter2 = max(d for _, _, d in pairs)
    separation2 = min(d for _, _, d in pairs)
    edges = [(a, b) for a, b, d in pairs if d == diameter2]
    loaded = {v for edge in edges for v in edge}
    boundary = hull(loaded)
    if len(boundary) < 3:
        return 0, 0, 0, 0
    partners = []
    covered = protected = 0
    for i, x in enumerate(boundary):
        y = boundary[(i+1) % len(boundary)]
        matches = [v for v in loaded if squared(v, x) == diameter2
                   and squared(v, y) == diameter2]
        assert len(matches) <= 1
        partner = matches[0] if matches else None
        partners.append(partner)
        if partner is not None:
            nx, ny = -(y[1]-x[1]), y[0]-x[0]
            for p in points:
                gap = nx*(p[0]-partner[0]) + ny*(p[1]-partner[1])
                assert gap == 0 if p == partner else gap < 0
            covered += 1
            side2 = squared(x, y)
            if side2*diameter2 <= 4*separation2*diameter2-separation2**2:
                assert all((y[0]-x[0])*(p[1]-x[1])
                           -(y[1]-x[1])*(p[0]-x[0]) >= 0 for p in points)
                protected += 1

    transitions = changed = 0
    cos_delta = 1-F(separation2)/(2*F(diameter2))
    cos_two_delta = 2*cos_delta**2-1
    for i, v in enumerate(partners):
        w = partners[(i+1) % len(partners)]
        if v is None or w is None:
            continue
        x, y, z = (boundary[(i+j) % len(boundary)] for j in range(3))
        vx, vy = v[0]-y[0], v[1]-y[1]
        wx, wy = w[0]-y[0], w[1]-y[1]
        determinant = vx*wy-vy*wx
        assert determinant == 0 if v == w else determinant > 0
        assert vx*wx+vy*wy > 0
        ax, ay = y[0]-x[0], y[1]-x[1]
        bx, by = z[0]-y[0], z[1]-y[1]
        dot = ax*bx+ay*by
        product = squared(x, y)*squared(y, z)
        assert cosine_at_most(dot, product, cos_delta)
        if v != w:
            assert cosine_at_most(dot, product, cos_two_delta)
            changed += 1
        transitions += 1
    return covered, transitions, changed, protected


def main():
    grid = [(x, y) for x in range(4) for y in range(3)]
    totals = [0, 0, 0, 0]
    samples = 0
    for size in range(3, len(grid)+1):
        for points in combinations(grid, size):
            for i, value in enumerate(audit(points)):
                totals[i] += value
            samples += 1
    fan = [(F(0), F(0)), (F(1, 5), F(-3, 5))]
    for i in range(81):
        t = F(i, 240)
        fan.append(((1-t*t)/(1+t*t), -2*t/(1+t*t)))
    fan_counts = audit(fan)
    assert fan_counts[1] > 70
    # A length-two V side need not support the full source hull.
    x, y, v = (F(-1), F(0)), (F(1), F(0)), (F(0), F(49, 10))
    w, z = (F(382, 325), F(2927, 650)), (F(0), F(-1, 20))
    sample = [x, y, v, w, z]
    pairs = [(a, b, squared(a, b)) for a, b in combinations(sample, 2)]
    assert min(d for _, _, d in pairs) > 1
    assert max(d for _, _, d in pairs) == F(2501, 100)
    diameter_pairs = {frozenset((a, b)) for a, b, d in pairs
                      if d == F(2501, 100)}
    assert diameter_pairs == {frozenset((v, x)), frozenset((v, y)),
                              frozenset((x, w))}
    assert hull({p for edge in diameter_pairs for p in edge}) == [x, y, w, v]
    assert z[1] < 0 and squared(x, y) == 4
    audit(sample)
    print(f"PASS: {samples} grid subsets; {totals[0]} covered-side instances; "
          f"{totals[1]} covered transitions; {totals[2]} changed antipodes; "
          f"{totals[3]} protected-side instances")
    print(f"PASS: rational non-star fan counts {fan_counts}")
    print("PASS: rational length-two exterior-point regression")
    print("Finite examples only; universal transition and occupancy proofs are analytic.")


if __name__ == '__main__':
    main()
