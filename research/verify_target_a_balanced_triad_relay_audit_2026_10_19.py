"""Independent exact pair ledger for the balanced-triad relay audit."""

from fractions import Fraction as F
from itertools import combinations


def add(left, right):
    return left[0] + right[0], left[1] + right[1]


def sub(left, right):
    return left[0] - right[0], left[1] - right[1]


def dot(left, right):
    # Coordinates store (x, coefficient of sqrt(3) in y).
    return left[0] * right[0] + 3 * left[1] * right[1]


def squared_distance(left, right):
    delta = sub(left, right)
    return dot(delta, delta)


def ledger(points):
    return [
        (f"{first}-{second}", squared_distance(points[first], points[second]))
        for first, second in combinations(points, 2)
    ]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def check_interval(table, low=F(1), high=F(3)):
    require(all(low <= value <= high for _, value in table),
            f"pair bound failed: {table}")


def main():
    half = F(1, 2)
    base = {
        "p": (F(0), F(0)),
        "q0": (F(1), F(0)),
        "q1": (-half, half),
        "q2": (-half, -half),
    }

    base_table = ledger(base)
    check_interval(base_table)
    require([value for _, value in base_table] ==
            [F(1), F(1), F(1), F(3), F(3), F(3)],
            f"unexpected six-pair fixture: {base_table}")

    normals = [sub(base["p"], base[f"q{i}"]) for i in range(3)]
    require(all(dot(n, n) == 1 for n in normals), "nonunit contact normal")
    require(all(dot(normals[i], normals[j]) == F(-1, 2)
                for i, j in combinations(range(3), 2)),
            "contact normals are not balanced at 120 degrees")
    require(add(add(normals[0], normals[1]), normals[2]) == (0, 0),
            "contact normals do not sum to zero")

    xx = sum(n[0] ** 2 for n in normals)
    yy = 3 * sum(n[1] ** 2 for n in normals)
    xy_coefficient = sum(n[0] * n[1] for n in normals)
    require((xx, yy, xy_coefficient) == (F(3, 2), F(3, 2), F(0)),
            "second-moment matrix is not (3/2)I")

    two_anchor = {
        "p": (F(1, 10), F(0)),
        "q1": base["q1"],
        "q2": base["q2"],
    }
    two_table = ledger(two_anchor)
    check_interval(two_table)
    require([value for _, value in two_table] ==
            [F(111, 100), F(111, 100), F(3)],
            f"unexpected two-anchor boundary control: {two_table}")

    unit_endpoint = dict(base)
    unit_endpoint["p"] = (F(-1), F(0))
    endpoint_table = ledger(unit_endpoint)
    require(all(value >= 1 for _, value in endpoint_table),
            f"unit endpoint unexpectedly violates lower bound: {endpoint_table}")
    upper_failures = [(pair, value) for pair, value in endpoint_table if value > 3]
    require(upper_failures == [("p-q0", F(4))],
            f"unexpected diameter-upper failures at unit endpoint: {upper_failures}")
    require([value for _, value in endpoint_table] ==
            [F(4), F(1), F(1), F(3), F(3), F(3)],
            f"unexpected complete unit-endpoint ledger: {endpoint_table}")

    print("PASS: all six fixture pairs lie in the exact interval [1, 3]")
    print("PASS: three unit normals have zero sum and second moment (3/2)I")
    print("PASS: deleting one anchor admits the exact nonzero displacement (1/10, 0)")
    print("PASS: unit endpoint satisfies all lower bounds and only p-q0 exceeds D^2=3")


if __name__ == "__main__":
    main()
