"""Exact finite verification of a two-shore source-image overlap identity.

Standalone standard-library script. This checks finite incidence assertions,
not source extraction, Schur rank, or global packing optimality.
"""

from functools import lru_cache
from fractions import Fraction
from itertools import product


@lru_cache(maxsize=None)
def image_masks(rows: tuple[int, ...], n_sources: int) -> frozenset[int]:
    """All source-image masks of injections saturating these ordered rows."""
    states = {0}
    for options in rows:
        nxt = set()
        for state in states:
            free = options & ~state
            while free:
                bit = free & -free
                nxt.add(state | bit)
                free ^= bit
        states = nxt
    return frozenset(states)


def max_matching(rows: tuple[int, ...], n_sources: int) -> int:
    """Independent DP allowing unmatched left vertices."""
    states = {0}
    for options in rows:
        nxt = set(states)
        for state in states:
            free = options & ~state
            while free:
                bit = free & -free
                nxt.add(state | bit)
                free ^= bit
        states = nxt
    return max(map(int.bit_count, states), default=0)


def hall_defect(rows: tuple[int, ...]) -> int:
    """Direct enumeration of all left-vertex subsets."""
    best = 0
    for pick in range(1 << len(rows)):
        union = 0
        for i, options in enumerate(rows):
            if pick & (1 << i):
                union |= options
        best = max(best, pick.bit_count() - union.bit_count())
    return best


def min_image_overlap(c_rows: tuple[int, ...], o_rows: tuple[int, ...], n: int) -> int:
    c_images = image_masks(c_rows, n)
    o_images = image_masks(o_rows, n)
    if not c_images or not o_images:
        raise ValueError('both shores must be independently saturable')
    return min((c & o).bit_count() for c in c_images for o in o_images)


def verify_exhaustive() -> tuple[int, int]:
    # Deliberately include cases with fewer source labels than combined demands.
    shapes = ((1, 1, 2), (1, 1, 3), (1, 2, 3),
              (2, 2, 3), (2, 2, 4), (1, 3, 4))
    checked = 0
    positive = 0
    for c, o, n in shapes:
        row_options = range(1 << n)
        for matrix in product(row_options, repeat=c + o):
            c_rows, o_rows = tuple(matrix[:c]), tuple(matrix[c:])
            if not image_masks(c_rows, n) or not image_masks(o_rows, n):
                continue
            checked += 1
            target = c + o - max_matching(tuple(matrix), n)
            actual = min_image_overlap(c_rows, o_rows, n)
            via_hall = hall_defect(tuple(matrix))
            assert target == actual == via_hall, (c, o, n, matrix, target, actual, via_hall)
            if target:
                positive += 1
    return checked, positive


def full_assignments(rows: tuple[int, ...], n: int) -> tuple[tuple[int, ...], ...]:
    """Independent enumeration retaining the actual source assigned to each row."""
    current = [()]
    for options in rows:
        current = [assignment + (j,) for assignment in current
                   for j in range(n) if options & (1 << j) and j not in assignment]
    return tuple(current)


def verify_extension_countermodel() -> tuple[int, int]:
    # Full shores U=(c,u), V=(o,v), sources (a,b).
    # c,o -> {a,b}; u,v -> {b}. Each full shore independently saturable.
    full_u = (0b11, 0b10)
    full_v = (0b11, 0b10)
    u_assignments = full_assignments(full_u, 2)
    v_assignments = full_assignments(full_v, 2)
    assert u_assignments == ((0, 1),), u_assignments
    assert v_assignments == ((0, 1),), v_assignments
    restricted = min_image_overlap(full_u[:1], full_v[:1], 2)
    full_min_restricted = min(
        len(set(u_assignment[:1]) & set(v_assignment[:1]))
        for u_assignment in u_assignments
        for v_assignment in v_assignments
    )
    assert restricted == 0 and full_min_restricted == 1
    assert max_matching((full_u[0], full_v[0]), 2) == 2
    return restricted, full_min_restricted


def squared_distance(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def pt(x, y):
    return (Fraction(x), Fraction(y))


def verify_rational_geometry() -> tuple[int, int, int]:
    # Coordinates from the earlier five-source PR #98 fixture, checked independently.
    c = (pt('-1/5', '-1/5'), pt('16/5', '-1/5'), pt('3/2', '2'))
    o = (pt('0', '0'), pt('3', '0'))
    a = (pt('-1/2', '-1/5'), pt('7/2', '-1/5'), pt('3/2', '29/10'),
         pt('6', '0'), pt('9', '-1/5'))
    for points in (c, o, a):
        assert all(squared_distance(points[i], points[j]) >= 1
                   for i in range(len(points)) for j in range(i + 1, len(points)))
    c_rows = tuple(sum(1 << j for j, src in enumerate(a) if squared_distance(x, src) < 1)
                   for x in c)
    o_rows = tuple(sum(1 << j for j, src in enumerate(a) if squared_distance(x, src) < 1)
                   for x in o)
    assert c_rows == (1, 2, 4), c_rows
    assert o_rows == (1, 2), o_rows
    assert image_masks(c_rows, len(a)) == frozenset({0b00111})
    assert image_masks(o_rows, len(a)) == frozenset({0b00011})
    matching = max_matching(c_rows + o_rows, len(a))
    forced_overlap = len(c) + len(o) - matching
    assert matching == 3 and forced_overlap == 2
    assert min_image_overlap(c_rows, o_rows, len(a)) == forced_overlap
    assert hall_defect(c_rows + o_rows) == forced_overlap
    return len(c), len(o), forced_overlap


if __name__ == '__main__':
    checked, positive = verify_exhaustive()
    before, after = verify_extension_countermodel()
    c, o, forced = verify_rational_geometry()
    print(f'PASS: {checked} independently saturable finite incidence graphs; '
          f'{positive} with positive unavoidable overlap')
    print(f'PASS: full-shore extension control has free-shore overlap {before} '
          f'but forced full-shore overlap {after}')
    print(f'PASS: rational source fixture C={c}, O={o}, unavoidable overlap={forced}')