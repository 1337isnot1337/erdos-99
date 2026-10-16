#!/usr/bin/env python3
"""Exhaust every loopless antitone directed relation on n=2,...,7 labels.

Assumes the exact relation: i<j implies every target of i is >= every
target of j. Checks the interval-terminal-SCC theorem, paired-tree structure
of each nontrivial SCC, and the strong-case staircase incidence identity.
Enumerates all labeled relations, without quotienting by symmetry.
Does not certify the geometric antitone lift, contacts, a finite source move,
KKT hypotheses, global optimality, C-II, or Level I. The report proves the
graph statements for all finite n and the conditional geometric/source lift.
"""

from fractions import Fraction as F
from itertools import combinations


def relations(n):
    rows = [0] * n

    def visit(i, cap):
        if i == n:
            yield tuple(rows)
            return
        universe = (1 << (cap + 1)) - 1
        subset = universe
        while True:
            if not subset >> i & 1:  # Loops never affect SCCs or cut support.
                rows[i] = subset
                next_cap = (subset & -subset).bit_length() - 1 if subset else cap
                yield from visit(i + 1, next_cap)
            if subset == 0:
                break
            subset = (subset - 1) & universe

    yield from visit(0, n - 1)


def audit(rows):
    n = len(rows)
    reach = [rows[i] | (1 << i) for i in range(n)]
    for k in range(n):
        for i in range(n):
            if reach[i] >> k & 1:
                reach[i] |= reach[k]
    components = {sum(1 << j for j in range(n)
                      if reach[i] >> j & 1 and reach[j] >> i & 1)
                  for i in range(n)}

    terminal = []
    for component in components:
        vertices = [i for i in range(n) if component >> i & 1]
        incoming = any(rows[i] & component for i in range(n)
                       if not component >> i & 1)
        outgoing = any(rows[i] & ~component for i in vertices)
        if not incoming or not outgoing:
            terminal.append(component)
        for i in vertices:
            for j in vertices:
                if rows[i] >> j & 1:
                    assert rows[j] >> i & 1  # Every internal edge is paired.
        edges = [(i, j) for i, j in combinations(vertices, 2) if rows[i] >> j & 1]
        assert len(edges) == len(vertices) - 1  # Paired underlying tree.
        # Compress the SCC's layer labels. Staircase incidence survives gaps.
        order = {v: i for i, v in enumerate(vertices)}
        compressed = sum(order[b] - order[a] for a, b in edges)
        assert compressed == len(vertices) * (len(vertices) - 1) // 2
        assert sum(b - a for a, b in edges) >= compressed

    # Every minimum-span terminal SCC is an interval, not merely one example.
    def span(component):
        return component.bit_length() - (component & -component).bit_length()

    best_span = min(map(span, terminal))
    for component in terminal:
        if span(component) == best_span:
            lo = (component & -component).bit_length() - 1
            hi = component.bit_length() - 1
            assert component == ((1 << (hi - lo + 1)) - 1) << lo
    if len(components) == 1:
        edges = [(i, j) for i, j in combinations(range(n), 2) if rows[i] >> j & 1]
        assert sum(b - a for a, b in edges) == n * (n - 1) // 2
        assert max(a for a, b in edges) < min(b for a, b in edges)
    else:
        # A minimum-span terminal component is proper in this case.
        assert best_span < n - 1
    return len(components) == 1


def main():
    total = strong = 0
    for n in range(2, 8):
        count = strong_n = 0
        for rows in relations(n):
            count += 1
            strong_n += audit(rows)
        total += count
        strong += strong_n
        print(f'n={n}: {count} complete labeled loopless antitone relations; {strong_n} strong')
    assert total == 487208
    # Exact perpendicular opening, without using a first-order rank claim.
    openings = 0
    for parameter in (F(-2), F(-1, 2), F(0), F(1, 3), F(2)):
        unit = ((1 - parameter ** 2) / (1 + parameter ** 2),
                2 * parameter / (1 + parameter ** 2))
        normal = (-unit[1], unit[0])
        for t in (F(1, 100), F(1, 10), F(1, 2)):
            for orientation in (-1, 1):
                moved = tuple(orientation * unit[i] + t * normal[i] for i in (0, 1))
                assert sum(x * x for x in moved) == 1 + t * t > 1
                openings += 1
    # Nonglobal fixture: translate the middle point of a unit three-point line.
    # The two contacts open and its only diameter stays exactly 2.
    before = ((F(0), F(0)), (F(1), F(0)), (F(2), F(0)))
    after = ((F(0), F(0)), (F(1), F(1, 10)), (F(2), F(0)))
    old = [sum((before[i][k] - before[j][k]) ** 2 for k in (0, 1))
           for i, j in combinations(range(3), 2)]
    new = [sum((after[i][k] - after[j][k]) ** 2 for k in (0, 1))
           for i, j in combinations(range(3), 2)]
    assert old.count(1) == 2 and new.count(1) == 0
    assert max(old) == max(new) == 4 and min(new) > 1
    print(f'PASS: {total} complete relations; {strong} strong; interval terminal SCCs,')
    print('paired trees, compressed staircase identities, and full-order strong incidence.')
    print(f'PASS: {openings} exact perpendicular contact openings; finite all-pair motion fixture.')
    print('Finite corroboration only; the report supplies the unrestricted analytic proofs.')


if __name__ == '__main__':
    main()
