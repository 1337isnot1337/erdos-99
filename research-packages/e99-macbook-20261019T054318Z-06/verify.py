"""Independent exact audit of PR #104's seven-label common-shear family."""

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations


D2 = Q(146, 25)
CSTAR = Q(21, 100)
Z = ("z",)
GRID = tuple(("v", i, j) for j in (0, 1) for i in (0, 1, 2))
LABELS = GRID + (Z,)


def label(x):
    if x == Z:
        return "z"
    _, i, j = x
    return f"v{i}{j}"


def row_index_pair(p, q):
    """Return signed top-index minus bottom-index for a cross-row pair."""
    if p[2] == 0:
        bottom, top = p, q
    else:
        bottom, top = q, p
    assert bottom[2] == 0 and top[2] == 1
    return top[1] - bottom[1]


def grid_d2(p, q, c):
    """Squared distance from vector differences, using rational c."""
    _, i, j = p
    _, k, ell = q
    if j == ell:
        return Q((i - k) ** 2)
    delta = row_index_pair(p, q)
    return Q(1 + delta * delta) + 2 * delta * c


def class_of(p, q):
    if p == Z or q == Z:
        v = q if p == Z else p
        return "z-to-bottom" if v[2] == 0 else "z-to-top"
    _, i, j = p
    _, k, ell = q
    if j == ell:
        return "same-row-adjacent" if abs(i - k) == 1 else "same-row-separated"
    delta = row_index_pair(p, q)
    if delta == 0:
        return "cross-row-same-index"
    return f"cross-row-abs-delta-{abs(delta)}"


def family_interval(p, q):
    """Closed rational enclosure valid for every |c| <= 21/100."""
    cls = class_of(p, q)
    if cls == "z-to-bottom":
        _, i, _ = q if p == Z else p
        d2 = Q((1 - i) ** 2) + Q(121, 25)
        return d2, d2
    if cls == "z-to-top":
        # If s=sqrt(1-c^2), then 97/100 < s <= 1. Thus
        # 6/5 <= 11/5-s < 123/100, and |1-i-c| <= 121/100.
        return Q(36, 25), Q(2977, 1000)
    if cls == "same-row-adjacent":
        return Q(1), Q(1)
    if cls == "same-row-separated":
        return Q(4), Q(4)
    if cls == "cross-row-same-index":
        return Q(1), Q(1)
    if cls == "cross-row-abs-delta-1":
        return Q(79, 50), Q(121, 50)
    if cls == "cross-row-abs-delta-2":
        return Q(104, 25), D2
    raise AssertionError(cls)


def source_d2(p, q):
    """Exact squared distance at c=0, including the source radical s=1."""
    if p == Z or q == Z:
        v = q if p == Z else p
        _, i, j = v
        if j == 0:
            return Q((1 - i) ** 2) + Q(121, 25)
        return Q((1 - i) ** 2) + Q(36, 25)
    return grid_d2(p, q, Q(0))


def certify_radical_enclosure():
    min_s2 = 1 - CSTAR * CSTAR
    assert min_s2 == Q(9559, 10000)
    assert min_s2 > Q(97, 100) ** 2
    assert Q(2977, 1000) < D2


def check_all_21_source_pairs():
    pairs = list(combinations(LABELS, 2))
    assert len(pairs) == 21
    counts = Counter(class_of(p, q) for p, q in pairs)
    assert counts == {
        "same-row-adjacent": 4,
        "same-row-separated": 2,
        "cross-row-same-index": 3,
        "cross-row-abs-delta-1": 4,
        "cross-row-abs-delta-2": 2,
        "z-to-bottom": 3,
        "z-to-top": 3,
    }

    contacts = set()
    diameters = set()
    for p, q in pairs:
        d2 = source_d2(p, q)
        assert Q(1) <= d2 <= D2, (label(p), label(q), d2)
        if d2 == 1:
            contacts.add(frozenset((p, q)))
        if d2 == D2:
            diameters.add(frozenset((p, q)))
        lo, hi = family_interval(p, q)
        assert lo >= 1 and hi <= D2, (label(p), label(q), lo, hi)
        print(
            f"{label(p):>3s}-{label(q):<3s} class={class_of(p, q):<25s} "
            f"source_d2={d2} family_enclosure=[{lo},{hi}]"
        )

    assert len(contacts) == 7
    assert diameters == {
        frozenset((Z, ("v", 0, 0))),
        frozenset((Z, ("v", 2, 0))),
    }
    return pairs


def pair_state(p, q, c):
    """Return exact rational d^2 or a certified strict interval for z/top."""
    if p == Z or q == Z:
        v = q if p == Z else p
        _, i, j = v
        if j == 0:
            d2 = Q((1 - i) ** 2) + Q(121, 25)
            return d2, d2, d2
        lo, _ = family_interval(p, q)
        if abs(c) <= CSTAR:
            _, hi = family_interval(p, q)
            return None, lo, hi
        return None, lo, None
    d2 = grid_d2(p, q, c)
    return d2, d2, d2


def triangle_count(edges):
    return sum(
        1
        for a, b, c in combinations(LABELS, 3)
        if frozenset((a, b)) in edges
        and frozenset((a, c)) in edges
        and frozenset((b, c)) in edges
    )


def counts_at(c):
    edges = set()
    diameters = set()
    for p, q in combinations(LABELS, 2):
        d2, lo, hi = pair_state(p, q, c)
        if d2 is None:
            assert lo > 1
            if abs(c) <= CSTAR:
                assert hi < D2
            continue
        if d2 == 1:
            edges.add(frozenset((p, q)))
        if d2 == D2:
            diameters.add(frozenset((p, q)))
    return len(edges), len(diameters), triangle_count(edges), edges, diameters


def check_interval_and_endpoints():
    certify_radical_enclosure()
    # All seven pair classes obey 1 <= d^2 <= D^2 throughout this interval.
    pairs = list(combinations(LABELS, 2))
    for p, q in pairs:
        lo, hi = family_interval(p, q)
        assert lo >= 1 and hi <= D2

    # A cross-row pair with signed index gap delta has d^2=1+delta^2+2*delta*c.
    # The two |delta|=2 values have maximum 5+4|c|, so the upper bound is
    # equivalent to 5+4|c| <= 146/25, namely |c| <= 21/100.
    assert D2 - 5 == Q(21, 25)
    assert (D2 - 5) / 4 == CSTAR

    for c in (Q(-1, 5), Q(0), Q(1, 5)):
        n_contacts, n_diameters, n_triangles, _, _ = counts_at(c)
        assert (n_contacts, n_diameters, n_triangles) == (7, 2, 0)

    plus = Q(21, 100)
    minus = -plus
    for c in (minus, plus):
        n_contacts, n_diameters, n_triangles, _, _ = counts_at(c)
        assert (n_contacts, n_diameters, n_triangles) == (7, 3, 0)

    plus_state = counts_at(plus)
    minus_state = counts_at(minus)
    assert frozenset((("v", 0, 0), ("v", 2, 1))) in plus_state[4]
    assert frozenset((("v", 2, 0), ("v", 0, 1))) in minus_state[4]

    # Outside either endpoint, the pair whose signed gap has the sign of c
    # violates the fixed D upper bound. Check exact witnesses on both sides.
    for c, bottom_i, top_i in (
        (Q(1, 4), 0, 2),
        (Q(-1, 4), 2, 0),
    ):
        witness = grid_d2(("v", bottom_i, 0), ("v", top_i, 1), c)
        assert witness == 6 and witness > D2

    # At c=+/-1/2, the two extra cross-row unit edges close four triangles:
    # each lies in one triangle with each of its two adjacent ladder edges.
    for c in (Q(-1, 2), Q(1, 2)):
        n_contacts, _, n_triangles, _, _ = counts_at(c)
        assert (n_contacts, n_triangles) == (9, 4)

    print("PASS: all 21 pair classes and source distances independently reconstructed")
    print("PASS: exact radical enclosure proves all full-source lower/upper bounds")
    print("PASS: feasible interval is exactly |c| <= 21/100")
    print("PASS: interior counts are (|C|, |H|, triangles) = (7, 2, 0)")
    print("PASS: both activation endpoints have counts (7, 3, 0)")
    print("PASS: both outside-upper controls have d^2=6 > D^2")
    print("PASS: both unit-triangle controls have (9 contacts, 4 triangles)")


def main():
    check_all_21_source_pairs()
    check_interval_and_endpoints()


main()
