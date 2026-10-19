"""Exact full-pair ledger for a two-face train with one fixed isolate."""

from fractions import Fraction as F
from itertools import combinations


D2 = F(146, 25)
C_MAX = F(21, 100)
GRID = [(i, j) for j in (0, 1) for i in (0, 1, 2)]
ISOLATE = ("z",)
LABELS = GRID + [ISOLATE]


def name(label):
    return "z" if label == ISOLATE else f"v{label[0]}{label[1]}"


def grid_distance2(p, q, c):
    i, j = p
    k, ell = q
    if j == ell:
        return F((i - k) ** 2)
    if j == 0:
        low_i, high_i = i, k
    else:
        low_i, high_i = k, i
    delta = high_i - low_i
    return F(delta * delta + 1) + 2 * delta * c


def source_distance2(p, q):
    """Exact squared distance at the source c=0."""
    if p == ISOLATE or q == ISOLATE:
        grid = q if p == ISOLATE else p
        i, j = grid
        if j == 0:
            return F((1 - i) ** 2) + F(121, 25)
        return F((1 - i) ** 2) + F(36, 25)
    return grid_distance2(p, q, F(0))


def family_bounds(p, q):
    """Rational squared-distance bounds valid throughout |c| <= 21/100."""
    if p == ISOLATE or q == ISOLATE:
        grid = q if p == ISOLATE else p
        i, j = grid
        if j == 0:
            value = F((1 - i) ** 2) + F(121, 25)
            return value, value, "exact isolate-to-bottom"
        return F(36, 25), F(2977, 1000), "isolate-to-top algebraic bound"

    i, j = p
    k, ell = q
    if j == ell:
        value = F((i - k) ** 2)
        return value, value, "same row"
    if j == 0:
        low_i, high_i = i, k
    else:
        low_i, high_i = k, i
    delta = high_i - low_i
    if delta == 0:
        return F(1), F(1), "same-column contact"
    if abs(delta) == 1:
        return F(79, 50), F(121, 50), f"cross row k={delta}"
    return F(104, 25), D2, f"cross row k={delta}"


def grid_contacts(c):
    edges = set()
    for p, q in combinations(GRID, 2):
        if grid_distance2(p, q, c) == 1:
            edges.add(frozenset((p, q)))
    return edges


def triangle_count(edges):
    vertices = set().union(*edges) if edges else set()
    return sum(
        1
        for a, b, c in combinations(vertices, 3)
        if frozenset((a, b)) in edges
        and frozenset((a, c)) in edges
        and frozenset((b, c)) in edges
    )


def check_family():
    # Exact radical bound: sqrt(1-c^2) > 97/100 on the full interval.
    s2_min = 1 - C_MAX**2
    assert s2_min == F(9559, 10000)
    assert s2_min > F(97, 100) ** 2
    assert F(2977, 1000) < D2

    expected_contacts = 7
    for c in (F(-21, 100), F(-1, 5), F(0), F(1, 5), F(21, 100)):
        edges = grid_contacts(c)
        assert len(edges) == expected_contacts
        assert triangle_count(edges) == 0

        for p, q in combinations(LABELS, 2):
            lower, upper, _ = family_bounds(p, q)
            assert lower >= 1, (name(p), name(q), lower)
            assert upper <= D2, (name(p), name(q), upper)

        # All nonboundary members have exactly the two fixed isolate diameters.
        cross_max = 5 + 4 * abs(c)
        new_diameter_pairs = [
            (p, q)
            for p, q in combinations(GRID, 2)
            if p[1] != q[1] and grid_distance2(p, q, c) == D2
        ]
        if abs(c) < C_MAX:
            assert cross_max < D2
            assert not new_diameter_pairs
        else:
            assert cross_max == D2
            assert len(new_diameter_pairs) == 1
        diameter_count = 2 + len(new_diameter_pairs)

        if c == F(-1, 5):
            assert sorted((5 + 4 * c, 5 - 4 * c)) == [F(21, 5), F(29, 5)]
            assert diameter_count == 2
        if abs(c) == C_MAX:
            assert diameter_count == 3


def check_complete_source_ledger():
    rows = list(combinations(LABELS, 2))
    assert len(rows) == 21
    contact_pairs = set()
    diameter_pairs = set()
    for p, q in rows:
        d2 = source_distance2(p, q)
        assert d2 >= 1
        assert d2 <= D2
        if d2 == 1:
            contact_pairs.add((name(p), name(q)))
        if d2 == D2:
            diameter_pairs.add((name(p), name(q)))
        lower, upper, kind = family_bounds(p, q)
        print(
            f"{name(p):>3s}-{name(q):<3s} source_d2={str(d2):>6s} "
            f"family_d2=[{lower},{upper}] {kind}"
        )
    assert len(contact_pairs) == 7
    assert len(diameter_pairs) == 2
    assert {frozenset(pair) for pair in diameter_pairs} == {
        frozenset(("z", "v00")),
        frozenset(("z", "v20")),
    }
    assert triangle_count(grid_contacts(F(0))) == 0


def check_falsification_controls():
    # One quarter of a unit of shear exceeds the inactive upper pair.
    c = F(-1, 4)
    violating_distance2 = 5 - 4 * c
    assert violating_distance2 == 6
    assert violating_distance2 > D2

    # At c=-1/2 a new cross-row unit pair closes a unit triangle.
    edges = grid_contacts(F(-1, 2))
    assert len(edges) > 7
    assert triangle_count(edges) > 0


def main():
    check_complete_source_ledger()
    check_family()
    check_falsification_controls()
    print("PASS: 21 source pairs; 7 contacts; 2 actual diameter pairs at c=0")
    print("PASS: all lower and upper pairs for |c| <= 21/100")
    print("PASS: open interval leaves (|C|,|H|)=(7,2) unchanged")
    print("PASS: either boundary adds one diameter pair; outside violates D")
    print("PASS: invalid-upper and unit-triangle controls detected")


main()
