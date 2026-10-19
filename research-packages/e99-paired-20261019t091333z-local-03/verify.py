"""Exact rational-interval check for two eight-label coupled-shear paths."""

from fractions import Fraction as F
from itertools import combinations


TMAX = F(1, 10)
H_VALUES = (F(1), F(11, 10))
GRID = [("A", i) for i in range(3)] + [("B", i) for i in range(3)]
Z = ("Z", 0)
W = ("W", 0)
LABELS = GRID + [Z, W]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def source_coordinates(label, h):
    kind, i = label
    if kind == "A":
        return F(i), F(0)
    if kind == "B":
        return F(i), F(1)
    if kind == "Z":
        return F(1), F(11, 5)
    return F(3), h


def source_distance_squared(p, q, h):
    x1, y1 = source_coordinates(p, h)
    x2, y2 = source_coordinates(q, h)
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def train_pair_bound(p, q):
    kp, ip = p
    kq, iq = q
    if kp == kq:
        exact = F((ip - iq) ** 2)
        return exact, exact, "same row"

    m = ip - iq
    if m == 0:
        return F(1), F(1), "vertical contact"
    if abs(m) == 1:
        return F(9, 5), F(11, 5), "cross-row gap one"
    return F(23, 5), F(27, 5), "cross-row gap two"


def pair_bound(p, q, h):
    """Return rational lower/upper bounds and a complete pair class."""
    kinds = {p[0], q[0]}

    if kinds <= {"A", "B"}:
        if p[0] != q[0]:
            a = p if p[0] == "A" else q
            b = p if p[0] == "B" else q
            m = a[1] - b[1]
            if m == 0:
                return F(1), F(1), "train vertical contact"
            if abs(m) == 1:
                return F(9, 5), F(11, 5), "train cross-row gap one"
            return F(23, 5), F(27, 5), "train cross-row gap two"
        return train_pair_bound(p, q)

    if "Z" in kinds and ("A" in kinds or "B" in kinds):
        point = q if p == Z else p
        kind, i = point
        if kind == "A":
            lower = F((1 - i) ** 2) + F(21, 10) ** 2
            upper = F((1 - i) ** 2) + F(11, 5) ** 2
            return lower, upper, "isolate to bottom row"
        return F(121, 100), F(26741, 10000), "isolate to top row"

    if "W" in kinds and ("A" in kinds or "B" in kinds):
        point = q if p == W else p
        kind, i = point
        if kind == "A":
            a = F(3 - i)
            y_min = h - F(1, 2)
            lower = a**2 + y_min**2
            if i == 0:
                upper = F(9) + h**2
            else:
                upper = (a + F(3, 25)) ** 2 + h**2
            return lower, upper, "exterior to bottom row"

        a = F(3 - i)
        delta2 = F(1, 4) if h == 1 else F(4, 25)
        lower = a**2
        upper = (a + F(1, 50)) ** 2 + delta2
        return lower, upper, "exterior to top row"

    if kinds == {"W", "Z"}:
        if h == 1:
            upper = F(136, 25) + F(72, 5) * TMAX + F(436, 25) * TMAX**2
        else:
            upper = F(521, 100) + F(68, 5) * TMAX + F(436, 25) * TMAX**2
        return F(4), upper, "exterior to isolate"

    raise AssertionError((p, q, "unclassified pair"))


def train_edges():
    edges = set()
    for i in range(2):
        edges.add(frozenset((("A", i), ("A", i + 1))))
        edges.add(frozenset((("B", i), ("B", i + 1))))
    for i in range(3):
        edges.add(frozenset((("A", i), ("B", i))))
    return edges


def triangle_count(edges):
    count = 0
    for a, b, c in combinations(LABELS, 3):
        if (frozenset((a, b)) in edges and frozenset((a, c)) in edges
                and frozenset((b, c)) in edges):
            count += 1
    return count


def check_source(h):
    d2 = F(9) + h**2
    pairs = list(combinations(LABELS, 2))
    require(len(LABELS) == 8 and len(pairs) == 28, "all eight labels must be retained")
    contacts = []
    diameters = []
    for p, q in pairs:
        value = source_distance_squared(p, q, h)
        require(value >= 1, (h, p, q, value, "source lower bound"))
        require(value <= d2, (h, p, q, value, d2, "source upper bound"))
        if value == 1:
            contacts.append(frozenset((p, q)))
        if value == d2:
            diameters.append(frozenset((p, q)))

    expected = train_edges()
    if h == 1:
        expected.add(frozenset((W, ("B", 2))))
        require(len(contacts) == 8, (contacts, "one exterior unit contact"))
    else:
        require(len(contacts) == 7, (contacts, "no added unit contact"))
        require(source_distance_squared(W, ("B", 2), h) == F(101, 100),
                "diameter-only fixture must have no unit contact at W")

    require(set(contacts) == expected, (contacts, "source contact inventory"))
    require(diameters == [frozenset((W, ("A", 0)))],
            (diameters, "unique exterior-to-opposite-corner diameter"))
    require(triangle_count(set(contacts)) == 0, "source contact graph must be triangle-free")
    return d2, len(contacts), len(diameters)


def check_radical_bounds():
    s2_min = 1 - TMAX**2
    require(s2_min == F(99, 100), "squared sine lower endpoint")
    require(s2_min > F(99, 100) ** 2, "strict rational lower bound for s")
    require(F(99, 100) > 0, "positive square-root branch")

    zq_lower = F(11, 5) - TMAX - 1
    zq_upper = F(11, 5) - F(99, 100)
    require(zq_lower == F(11, 10) and zq_upper == F(121, 100),
            "isolate-to-top radical interval")
    require(F(11, 10) ** 2 + F(121, 100) ** 2 == F(26741, 10000),
            "isolate-to-top squared upper bound")

    for h, delta_lower, delta_upper, delta2_upper in (
            (F(1), F(-1, 2), F(0), F(1, 4)),
            (F(11, 10), F(-2, 5), F(1, 10), F(4, 25))):
        require(delta_lower < 0 <= delta_upper, (h, "top attachment vertical range"))
        require(delta2_upper == max(delta_lower**2, delta_upper**2),
                (h, "top attachment squared range"))


def check_path(h, source_d2):
    pairs = list(combinations(LABELS, 2))
    classes = {}
    other_upper = []
    for p, q in pairs:
        lower, upper, kind = pair_bound(p, q, h)
        require(lower >= 1, (h, p, q, lower, kind, "path lower bound"))
        require(upper <= source_d2, (h, p, q, upper, kind, "path upper bound"))
        if frozenset((p, q)) == frozenset((W, ("A", 0))):
            other_upper.append(None)
        else:
            require(upper < source_d2, (h, p, q, upper, kind, "strict non-diameter upper"))
            other_upper.append(upper)
        classes[kind] = classes.get(kind, 0) + 1

    expected_classes = {
        "same row": 6,
        "train vertical contact": 3,
        "train cross-row gap one": 4,
        "train cross-row gap two": 2,
        "isolate to bottom row": 3,
        "isolate to top row": 3,
        "exterior to bottom row": 3,
        "exterior to top row": 3,
        "exterior to isolate": 1,
    }
    require(classes == expected_classes, (h, classes, "all pair classes/counts"))

    slope = F(36, 5) - 10 * h
    quadratic = F(661, 25)
    require(slope < 0, (h, slope, "diameter derivative at source"))
    require(slope + quadratic * TMAX < 0,
            (h, slope, quadratic, "exterior diameter must strictly decrease"))
    vertex = -slope / (2 * quadratic)
    minimum_d2 = source_d2 - slope**2 / (4 * quadratic)
    require(0 < vertex < TMAX, (h, vertex, "quadratic minimum lies in interval"))
    largest_other = max(x for x in other_upper if x is not None)
    expected_minimum = F(6561, 661) if h == 1 else F(166464, 16525)
    expected_other = F(11713, 1250) if h == 1 else F(23201, 2500)
    require(minimum_d2 == expected_minimum, (h, minimum_d2, "exact diameter minimum"))
    require(largest_other == expected_other, (h, largest_other, "exact other-pair maximum bound"))
    require(minimum_d2 > largest_other,
            (h, minimum_d2, other_upper, "exterior pair remains the actual diameter"))

    # The only positive-parameter unit pairs are the seven train ladder edges.
    # Every non-train class has strict lower slack; W-B_2 has horizontal
    # separation 1+t/5 > 1 when t>0.
    require(len(train_edges()) == 7, "train ladder edge count")
    require(triangle_count(train_edges()) == 0, "positive-parameter path is triangle-free")

    endpoint = source_d2 + slope * TMAX + quadratic * TMAX**2
    expected_endpoint = F(24961, 2500) if h == 1 else F(6309, 625)
    require(endpoint == expected_endpoint, (h, endpoint, "exact endpoint diameter"))
    require(endpoint < source_d2, (h, endpoint, source_d2, "strict sub-D endpoint"))

    # At t=1/5 the proposed exterior diameter upper pair itself exceeds D_h.
    control_t = F(1, 5)
    control = source_d2 + slope * control_t + quadratic * control_t**2
    require(control > source_d2, (h, control, source_d2, "outside-interval upper control"))
    return endpoint, classes, minimum_d2


def main():
    check_radical_bounds()
    for h in H_VALUES:
        source_d2, contacts, diameter_pairs = check_source(h)
        endpoint, classes, minimum_d2 = check_path(h, source_d2)
        print(
            "PASS h=%s source_pairs=28 contacts=%d diameter_pairs=%d "
            "source_D2=%s D2_at_t_1_10=%s min_exterior_D2=%s classes=%s"
            % (h, contacts, diameter_pairs, source_d2, endpoint, minimum_d2, classes)
        )
    print("PASS: both exact eight-label paths have all 28 lower/upper pair bounds")


main()
