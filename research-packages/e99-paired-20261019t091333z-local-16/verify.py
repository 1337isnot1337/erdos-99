"""Independent exact pair-ledger audit for the finite PR #142 path."""

from fractions import Fraction as F
from itertools import combinations


D2 = F(146, 25)
TMAX = F(1, 10)
GRID = tuple(("g", i, j) for j in (0, 1) for i in range(3))
Z = ("z",)
LABELS = GRID + (Z,)


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def is_z(p):
    return p == Z


def grid_distance2(p, q, c):
    """Use b=(c,s), c^2+s^2=1, to eliminate the radical exactly."""
    _, i, j = p
    _, k, ell = q
    delta = F(i - k)
    row = F(j - ell)
    return delta * delta + 2 * delta * row * c + row * row


def source_distance2(p, q):
    if is_z(p) or is_z(q):
        point = q if is_z(p) else p
        _, i, j = point
        vertical2 = F(121, 25) if j == 0 else F(36, 25)
        return F((1 - i) ** 2) + vertical2
    return grid_distance2(p, q, F(0))


def path_bound(p, q):
    """Closed rational enclosure, plus whether a strict endpoint needs t>0."""
    if is_z(p) or is_z(q):
        point = q if is_z(p) else p
        _, i, j = point
        if j == 0:
            if i == 1:
                return F(441, 100), F(121, 25), "bottom-middle", False
            return F(541, 100), D2, "bottom-endpoint", True
        return F(121, 100), F(26741, 10000), "top", False

    _, i, j = p
    _, k, ell = q
    delta = i - k
    row = j - ell
    if row == 0:
        d2 = F(delta * delta)
        return d2, d2, "same-row", False
    if delta == 0:
        return F(1), F(1), "vertical", False
    gap = abs(delta)
    center = F(gap * gap + 1)
    spread = 2 * gap * TMAX
    return center - spread, center + spread, "cross-row", False


def edge_set_from_exact_distances(distance):
    return {
        frozenset((p, q))
        for p, q in combinations(LABELS, 2)
        if distance(p, q) == 1
    }


def triangle_count(edges):
    return sum(
        1
        for a, b, c in combinations(LABELS, 3)
        if frozenset((a, b)) in edges
        and frozenset((a, c)) in edges
        and frozenset((b, c)) in edges
    )


def check_source():
    pairs = list(combinations(LABELS, 2))
    require(len(pairs) == 21, "source must retain all 21 pairs")
    contacts = []
    diameters = []
    for p, q in pairs:
        d2 = source_distance2(p, q)
        require(d2 >= 1, (p, q, d2, "source lower bound"))
        require(d2 <= D2, (p, q, d2, "source upper bound"))
        if d2 == 1:
            contacts.append((p, q))
        if d2 == D2:
            diameters.append((p, q))
    edges = edge_set_from_exact_distances(source_distance2)
    require(len(contacts) == len(edges) == 7, "source must have seven unit edges")
    require(len(diameters) == 2, (diameters, "source diameter-pair count"))
    require(triangle_count(edges) == 0, "source contact ladder must be triangle-free")
    return len(pairs), len(contacts), len(diameters)


def check_positive_parameter_path():
    pairs = list(combinations(LABELS, 2))
    require(len(pairs) == 21, "path must check every retained source pair")

    y_top = F(11, 5)
    y_bottom = y_top - TMAX
    require(0 < y_bottom < y_top, "bottom isolate coordinate stays positive")
    require(1 + y_bottom**2 < 1 + y_top**2 == D2,
            "strict endpoint decrease at the far end of the interval")
    # For every 0<t<=TMAX, y_bottom<=y_top-t<y_top. Squaring is
    # strictly increasing on this positive interval, so 1+y^2<D2.

    s2_min = 1 - TMAX**2
    require(s2_min == F(99, 100), "minimum s squared")
    require(s2_min > F(99, 100) ** 2, "s is strictly above 99/100")
    q_low = y_top - TMAX - 1
    q_high = y_top - F(99, 100)
    x_abs_max = 1 + TMAX
    top_upper = x_abs_max**2 + q_high**2
    require(q_low == F(11, 10), "top-isolate lower bound")
    require(q_high == F(121, 100), "top-isolate upper bound")
    require(top_upper == F(26741, 10000) < D2, "top-isolate strict upper bound")
    require(q_low**2 > 1, "top-isolate strict lower bound")

    contacts = []
    kinds = {}
    for p, q in pairs:
        lo, hi, kind, strict_at_positive_t = path_bound(p, q)
        require(lo >= 1, (p, q, lo, kind, "path lower bound"))
        require(hi <= D2, (p, q, hi, kind, "old diameter upper bound"))
        if strict_at_positive_t:
            require(kind == "bottom-endpoint", (p, q, kind))
            require(1 + y_bottom**2 < D2, "positive motion gives strict old-D slack")
        else:
            require(hi < D2, (p, q, hi, kind, "strict old-D slack"))
        kinds[kind] = kinds.get(kind, 0) + 1
        if lo == hi == 1:
            contacts.append((p, q))

    require(len(contacts) == 7, (contacts, "path unit-contact count"))
    edges = edge_set_from_exact_distances(
        lambda p, q: F(1) if path_bound(p, q)[:2] == (F(1), F(1)) else F(-1)
    )
    require(len(edges) == 7 and triangle_count(edges) == 0,
            "path contact graph is the triangle-free ladder")

    endpoint_min = 1 + y_bottom**2
    other_max = max(F(27, 5), F(121, 25), top_upper, F(4))
    require(endpoint_min == F(541, 100), "endpoint lower diameter value")
    require(endpoint_min > other_max, "bottom endpoints dominate every other pair")
    require(1 + y_top**2 == D2, "old source diameter is set by bottom endpoints")
    return len(pairs), len(contacts), kinds


def fixed_isolate_distance_bounds(p, q, c):
    if is_z(p) or is_z(q):
        point = q if is_z(p) else p
        _, i, j = point
        if j == 0:
            d2 = F((1 - i) ** 2) + F(121, 25)
            return d2, d2
        x_abs = abs(F(1 - i) - c)
        # At c=1/10, s^2=99/100 and 99/100<s<1, hence
        # 6/5 < 11/5-s < 121/100.
        return F(36, 25), x_abs**2 + F(121, 100) ** 2
    d2 = grid_distance2(p, q, c)
    return d2, d2


def check_fixed_isolate_control():
    c = F(1, 10)
    contacts = []
    diameter_pairs = []
    for p, q in combinations(LABELS, 2):
        lo, hi = fixed_isolate_distance_bounds(p, q, c)
        require(lo >= 1, (p, q, lo, "fixed-isolate lower bound"))
        require(hi <= D2, (p, q, hi, "fixed-isolate upper bound"))
        if hi == lo == 1:
            contacts.append((p, q))
        if (is_z(p) or is_z(q)):
            point = q if is_z(p) else p
            if point[2] == 0 and point[1] in (0, 2):
                diameter_pairs.append((p, q))
    require(len(contacts) == 7, "fixed-isolate control retains seven contacts")
    require(len(diameter_pairs) == 2, "fixed-isolate control retains two D pairs")


def check_falsifiers():
    upper_bad = grid_distance2(("g", 0, 0), ("g", 2, 1), F(1, 4))
    require(upper_bad == 6 and upper_bad > D2,
            "c=1/4 must violate an inactive upper pair")

    lower_bad = grid_distance2(("g", 1, 0), ("g", 0, 1), F(3, 5))
    require(lower_bad == F(4, 5) < 1, "c=3/5 must violate lower separation")

    triangle = (("g", 0, 0), ("g", 1, 0), ("g", 0, 1))
    c = F(1, 2)
    side_values = [
        grid_distance2(triangle[0], triangle[1], c),
        grid_distance2(triangle[0], triangle[2], c),
        grid_distance2(triangle[1], triangle[2], c),
    ]
    require(side_values == [F(1), F(1), F(1)],
            "c=1/2 control must create a unit triangle")


source_result = check_source()
path_result = check_positive_parameter_path()
check_fixed_isolate_control()
check_falsifiers()

print(f"PASS: all {source_result[0]} source pairs; contacts={source_result[1]}, D-pairs={source_result[2]}")
print(f"PASS: all {path_result[0]} retained path pairs; contacts={path_result[1]}, classes={path_result[2]}")
print("PASS: strict path diameter is 1+(11/5-t)^2; at t=1/10 it is 541/100")
print("PASS: fixed-isolate, inactive-upper, lower-separation and unit-triangle controls")
