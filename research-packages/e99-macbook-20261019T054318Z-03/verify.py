"""Exact interval certificate for a two-face shear with a moving isolate."""

from fractions import Fraction as F
from itertools import combinations


D2 = F(146, 25)
TMAX = F(1, 10)
GRID = [(i, j) for j in (0, 1) for i in range(3)]
Z = ("z",)
LABELS = GRID + [Z]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def grid_polynomial(p, q, c, s):
    """Exact squared-distance polynomial before using c^2+s^2=1."""
    i, j = p
    k, ell = q
    delta = F(i - k)
    row_step = F(j - ell)
    return (delta + row_step * c) ** 2 + (row_step * s) ** 2


def grid_reduced_polynomial(p, q, c):
    """Same polynomial reduced by c^2+s^2=1."""
    i, j = p
    k, ell = q
    delta = F(i - k)
    row_step = F(j - ell)
    return delta**2 + 2 * delta * row_step * c + row_step**2


def isolate_bottom_polynomial(i, u, v):
    return (1 + u - i) ** 2 + (F(11, 5) + v) ** 2


def isolate_top_polynomial(i, u, v, c, s):
    return (1 + u - i - c) ** 2 + (F(11, 5) + v - s) ** 2


def check_polynomial_identities():
    # A rational unit vector lets the unreduced and reduced grid polynomials
    # be compared exactly for every train pair.
    c = F(3, 5)
    s = F(4, 5)
    for p, q in combinations(GRID, 2):
        require(
            grid_polynomial(p, q, c, s) == grid_reduced_polynomial(p, q, c),
            (p, q, "grid polynomial reduction"),
        )
    for i in range(3):
        require(
            isolate_bottom_polynomial(i, F(0), F(0))
            == F((1 - i) ** 2) + F(121, 25),
            (i, "bottom isolate polynomial"),
        )
        require(
            isolate_top_polynomial(i, F(0), F(0), F(0), F(1))
            == F((1 - i) ** 2) + F(36, 25),
            (i, "top isolate polynomial at source"),
        )


def path_pair_bound(p, q):
    """Uniform rational bound for each labeled pair on 0<t<=TMAX."""
    if p == Z or q == Z:
        point = q if p == Z else p
        i, j = point
        if j == 0:
            lower = F((1 - i) ** 2) + F(21, 10) ** 2
            if i in (0, 2):
                return lower, D2, "isolate-bottom endpoint, strict for t>0"
            return lower, F(121, 25), "isolate-bottom middle"
        lower = F(121, 100)
        upper = F(26741, 10000)
        return lower, upper, "isolate-top radical interval"

    i, j = p
    k, ell = q
    delta = i - k
    row_step = j - ell
    if row_step == 0:
        exact = F(delta**2)
        return exact, exact, "same row"
    if delta == 0:
        return F(1), F(1), "vertical unit contact"
    magnitude = abs(delta)
    base = F(magnitude**2 + 1)
    variation = 2 * magnitude * TMAX
    return base - variation, base + variation, f"cross-row index gap {magnitude}"


def source_distance_squared(p, q):
    """Exact rational squared distance at the source t=0."""
    if p == Z or q == Z:
        point = q if p == Z else p
        i, j = point
        if j == 0:
            return F((1 - i) ** 2) + F(121, 25)
        return F((1 - i) ** 2) + F(36, 25)
    return grid_reduced_polynomial(p, q, F(0))


def fixed_isolate_bound(p, q, c):
    """Bounds for the PR104 control with z=(1,11/5) and rational c."""
    if p == Z or q == Z:
        point = q if p == Z else p
        i, j = point
        if j == 0:
            exact = F((1 - i) ** 2) + F(121, 25)
            return exact, exact, exact < D2
        # At c=1/10, 99/100 < s < 1, so 6/5 < 11/5-s < 121/100.
        x = F(1 - i) - c
        lower = F(36, 25)
        upper = x**2 + F(121, 100) ** 2
        return lower, upper, True

    exact = grid_reduced_polynomial(p, q, c)
    return exact, exact, exact < D2


def contact_edges():
    edges = set()
    for p, q in combinations(GRID, 2):
        i, j = p
        k, ell = q
        if j == ell and abs(i - k) == 1:
            edges.add(frozenset((p, q)))
        if j != ell and i == k:
            edges.add(frozenset((p, q)))
    return edges


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
    require(len(pairs) == 21, "source must have all 21 unordered pairs")
    contacts = []
    diameters = []
    for p, q in pairs:
        d2 = source_distance_squared(p, q)
        require(d2 >= 1, (p, q, d2, "source lower bound"))
        require(d2 <= D2, (p, q, d2, "source upper bound"))
        if d2 == 1:
            contacts.append((p, q))
        if d2 == D2:
            diameters.append((p, q))
    require(len(contacts) == 7, (contacts, "source contact count"))
    require(len(diameters) == 2, (diameters, "source actual diameter count"))
    return len(pairs), len(contacts), len(diameters)


def check_uniform_path():
    # For 0<=t<=1/10, s^2>=99/100>(99/100)^2 and s<=1.
    s2_min = 1 - TMAX**2
    require(s2_min == F(99, 100), "wrong minimum s squared")
    require(s2_min > F(99, 100) ** 2, "rational lower bound for s failed")
    q_lower = F(11, 5) - TMAX - 1
    q_upper = F(11, 5) - F(99, 100)
    x_max = 1 + TMAX
    require(q_lower == F(11, 10), "top isolate lower bound")
    require(q_upper == F(121, 100), "top isolate upper bound")
    require(x_max == F(11, 10), "top isolate horizontal bound")
    top_upper = x_max**2 + q_upper**2
    require(top_upper == F(26741, 10000), "top isolate squared-distance bound")
    require(top_upper < D2, "top isolate upper bound must be below D2")

    y_lower = F(11, 5) - TMAX
    y_upper = F(11, 5)
    require(y_lower == F(21, 10) and y_upper == F(11, 5), "bottom isolate interval")
    require(TMAX > 0 and y_lower < y_upper, "moving isolate creates strict endpoint slack")
    require(y_upper - TMAX == y_lower and y_lower > 0,
            "positive displacement lowers both endpoint distances")
    require(1 + y_upper**2 == D2, "old endpoint pairs set the source diameter")
    isolate_endpoint_min = 1 + y_lower**2
    train_max = F(27, 5)
    require(isolate_endpoint_min == F(541, 100), "bottom endpoint lower bound")
    require(isolate_endpoint_min < D2, "positive displacement gives strict upper slack")
    require(isolate_endpoint_min > max(train_max, F(121, 25), top_upper, F(4)),
            "isolate endpoints must set the diameter throughout the interval")

    pairs = list(combinations(LABELS, 2))
    require(len(pairs) == 21, "path must retain all source pairs")
    contacts = []
    classes = {}
    for p, q in pairs:
        lower, upper, kind = path_pair_bound(p, q)
        require(lower >= 1, (p, q, lower, kind, "path lower bound"))
        require(upper <= D2, (p, q, upper, kind, "path upper bound"))
        if upper == D2:
            require(kind == "isolate-bottom endpoint, strict for t>0",
                    (p, q, kind, "only isolate endpoint pairs may reach the D2 bound"))
            require(TMAX > 0 and isolate_endpoint_min < D2,
                    (p, q, "strict upper follows from t>0"))
        else:
            require(upper < D2, (p, q, upper, kind, "strict upper proof"))
        classes[kind] = classes.get(kind, 0) + 1
        if lower == upper == 1:
            contacts.append((p, q))

    require(len(contacts) == 7, (contacts, "path contact count"))
    edges = contact_edges()
    require(len(edges) == 7, "ladder must have seven unit edges")
    require(triangle_count(edges) == 0, "ladder must remain triangle-free")
    return len(pairs), len(contacts), classes


def check_endpoint():
    t = TMAX
    y = F(11, 5) - t
    endpoint_d2 = 1 + y**2
    require(endpoint_d2 == F(541, 100), (endpoint_d2, "endpoint diameter"))
    require(endpoint_d2 < D2, "endpoint must be strictly below source D")
    require(endpoint_d2 - F(27, 5) == F(1, 100), "endpoint exceeds every train pair")

    # At t=1/10, s=sqrt(99/100), so 99/100 < s < 1.
    s2 = 1 - t**2
    require(s2 == F(99, 100), "endpoint shear norm")
    require(s2 < 1, "nonzero shear makes s strictly below one")
    q_low = F(11, 10)
    q_high = F(121, 100)
    require(q_low == F(21, 10) - F(1), "endpoint radical lower bound")
    require(F(21, 10) - F(99, 100) < q_high, "endpoint radical upper bound")
    for i in range(3):
        x = abs(F(1 - i) - t)
        require(x <= F(11, 10), (i, x, "top horizontal bound"))
        require(q_low**2 > 1, "top isolate lower bound")
        require(x**2 + q_high**2 < endpoint_d2, "top isolate is below the endpoint diameter")
    for i in (0, 2):
        require(isolate_bottom_polynomial(i, F(0), -t) == endpoint_d2,
                (i, "endpoint diameter pair"))
    require(isolate_bottom_polynomial(1, F(0), -t) < endpoint_d2,
            "middle bottom pair is below the endpoint diameter")


def check_fixed_isolate_control():
    c = F(1, 10)
    pairs = list(combinations(LABELS, 2))
    contacts = []
    diameters = []
    for p, q in pairs:
        lower, upper, strict_upper = fixed_isolate_bound(p, q, c)
        require(lower >= 1, (p, q, lower, "fixed-isolate lower bound"))
        require(upper <= D2, (p, q, upper, "fixed-isolate upper bound"))
        if p == Z or q == Z:
            point = q if p == Z else p
            i, j = point
            if j == 0:
                exact = F((1 - i) ** 2) + F(121, 25)
                if exact == D2:
                    diameters.append((p, q))
        elif lower == upper == 1:
            contacts.append((p, q))
    require(len(contacts) == 7, (contacts, "fixed-isolate contacts"))
    require(len(diameters) == 2, (diameters, "fixed-isolate diameter pairs"))


def check_falsification_controls():
    # The all-pair upper constraint is decisive beyond the selected interval.
    upper_break = grid_reduced_polynomial((0, 0), (2, 1), F(1, 4))
    require(upper_break == 6, (upper_break, "upper-bound control value"))
    require(upper_break > D2, "upper-bound control must fail")

    # A larger displacement makes a cross-row lower pair violate separation.
    lower_break = grid_reduced_polynomial((1, 0), (0, 1), F(3, 5))
    require(lower_break == F(4, 5), (lower_break, "lower-bound control value"))
    require(lower_break < 1, "lower-bound control must fail")

    # At c=1/2, v00, v10 and v01 are a unit triangle.
    c = F(1, 2)
    triangle = ((0, 0), (1, 0), (0, 1))
    d2s = [
        grid_reduced_polynomial(triangle[0], triangle[1], c),
        grid_reduced_polynomial(triangle[0], triangle[2], c),
        grid_reduced_polynomial(triangle[1], triangle[2], c),
    ]
    require(d2s == [F(1), F(1), F(1)], (d2s, "unit-triangle control"))


check_polynomial_identities()
source = check_source()
path = check_uniform_path()
check_endpoint()
check_fixed_isolate_control()
check_falsification_controls()

print(f"PASS: source census has {source[0]} pairs, {source[1]} contacts, {source[2]} actual D-pairs")
print(f"PASS: coupled path checks all {path[0]} pairs for 0<t<=1/10 with {path[1]} contacts")
print("PASS: every path pair is >=1 and <146/25; D_t^2=1+(11/5-t)^2")
print("PASS: t=1/10 gives D_t^2=541/100, set by the two isolate-bottom endpoints")
print("PASS: fixed-isolate c=1/10 control retains the old two diameter pairs")
print("PASS: inactive-upper, lower-separation, and unit-triangle controls fail as expected")
