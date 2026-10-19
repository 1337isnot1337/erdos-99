"""Exact check of a geometric full-shore extension obstruction.

This is a finite local regression. It makes no global-packing or Schur claim.
Only Python's standard-library rational arithmetic is used.
"""

from fractions import Fraction as F
from itertools import permutations


POINTS = {
    "a": (F(-3, 4), F(1, 4)),
    "b": (F(1, 2), F(3, 4)),
    "c": (F(-1, 8), F(5, 8)),
    "u": (F(5, 4), F(3, 4)),
    "o": (F(0), F(0)),
    "v": (F(1), F(0)),
}
SOURCE = ("a", "b")
X = ("c", "u")
Y = ("o", "v")
C = ("c",)
O = ("o",)


def distance_squared(p, q):
    return sum((x - y) ** 2 for x, y in zip(POINTS[p], POINTS[q]))


def neighbors(target):
    return tuple(s for s in SOURCE if distance_squared(target, s) < 1)


def saturating_matchings(targets):
    """Return all injections from a small ordered shore into SOURCE."""
    found = []
    for chosen in permutations(SOURCE, len(targets)):
        assignment = dict(zip(targets, chosen))
        if all(distance_squared(t, s) < 1 for t, s in assignment.items()):
            found.append(assignment)
    return found


def maximum_matching_size(targets):
    best = 0
    for size in range(min(len(targets), len(SOURCE)) + 1):
        for picked in permutations(targets, size):
            if saturating_matchings(picked):
                best = max(best, size)
    return best


def hall_deficiency(targets):
    best = 0
    for mask in range(1 << len(targets)):
        selected = tuple(t for i, t in enumerate(targets) if mask & (1 << i))
        image = {s for t in selected for s in neighbors(t)}
        best = max(best, len(selected) - len(image))
    return best


def min_restricted_image_overlap(left, right):
    left_matchings = saturating_matchings(left)
    right_matchings = saturating_matchings(right)
    assert left_matchings and right_matchings
    return min(
        len(set(m_left.values()) & set(m_right.values()))
        for m_left in left_matchings
        for m_right in right_matchings
    )


def assert_unit_separated(labels, *, allow_contact=True):
    for i, p in enumerate(labels):
        for q in labels[i + 1 :]:
            d2 = distance_squared(p, q)
            assert d2 >= 1, (p, q, d2)
            if not allow_contact:
                assert d2 > 1, (p, q, d2)


def assert_disjoint_x_projections(edge_pairs):
    intervals = []
    for left, right in edge_pairs:
        x1, x2 = POINTS[left][0], POINTS[right][0]
        intervals.append((min(x1, x2), max(x1, x2), left, right))
    first, second = intervals
    assert first[1] < second[0] or second[1] < first[0], intervals


def main():
    assert_unit_separated(SOURCE, allow_contact=False)
    assert_unit_separated(X, allow_contact=False)
    assert_unit_separated(Y, allow_contact=True)
    assert distance_squared("o", "v") == 1  # standard lattice vector

    expected_rows = {"c": ("a", "b"), "u": ("b",), "o": ("a", "b"), "v": ("b",)}
    actual_rows = {t: neighbors(t) for t in (*X, *Y)}
    assert actual_rows == expected_rows, actual_rows

    m_x = saturating_matchings(X)
    m_y = saturating_matchings(Y)
    assert m_x == [{"c": "a", "u": "b"}], m_x
    assert m_y == [{"o": "a", "v": "b"}], m_y
    assert_disjoint_x_projections((("c", "a"), ("u", "b")))
    assert_disjoint_x_projections((("o", "a"), ("v", "b")))

    restricted = (*C, *O)
    nu = maximum_matching_size(restricted)
    delta = len(C) + len(O) - nu
    assert nu == 2
    assert hall_deficiency(restricted) == 0
    assert delta == 0
    inherited_overlap = len({m_x[0]["c"]} & {m_y[0]["o"]})
    assert inherited_overlap == 1
    assert min_restricted_image_overlap(C, O) == 0

    print("source_squared_distance=29/16; X_squared_distance=61/32; Y_squared_distance=1")
    print("source_neighborhoods=c:{a,b},u:{b},o:{a,b},v:{b}")
    print("full_shore_saturating_matchings=unique_on_X_and_Y")
    print("restricted_hall_deficiency=0; min_free_overlap=0; inherited_overlap=1")
    print("result=PASS_LOCAL_GEOMETRIC_EXTENSION_COUNTERMODEL")
    print("limitation=no_fixed_hull_capacity_or_plateau_response_claim")


main()
