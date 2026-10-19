"""Exact finite audit for the balanced-triad source-interface lemma."""

from fractions import Fraction as F
from itertools import combinations


def q3(a=0, b=0):
    """Represent a + b*sqrt(3) as a pair of exact rational coefficients."""
    return F(a), F(b)


def qadd(left, right):
    return left[0] + right[0], left[1] + right[1]


def qneg(value):
    return -value[0], -value[1]


def qsub(left, right):
    return qadd(left, qneg(right))


def qmul(left, right):
    return (left[0] * right[0] + 3 * left[1] * right[1],
            left[0] * right[1] + left[1] * right[0])


def qsign(value):
    a, b = value
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    gap = a * a - 3 * b * b
    if gap == 0:
        raise ValueError("nonzero rational square cannot equal three times a rational square")
    if a > 0:
        return (gap > 0) - (gap < 0)
    return (-gap > 0) - (-gap < 0)


def vadd(left, right):
    return qadd(left[0], right[0]), qadd(left[1], right[1])


def vsub(left, right):
    return qsub(left[0], right[0]), qsub(left[1], right[1])


def dot(left, right):
    return qadd(qmul(left[0], right[0]), qmul(left[1], right[1]))


def norm_sq(vector):
    return dot(vector, vector)


def pair_sq(points, first, second):
    return norm_sq(vsub(points[first], points[second]))


def pair_values(points):
    return [pair_sq(points, first, second)
            for first, second in combinations(points, 2)]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check_bounds(points, lower_sq=1, upper_sq=3):
    lower_sq = q3(lower_sq)
    upper_sq = q3(upper_sq)
    values = pair_values(points)
    require(all(qsign(qsub(value, lower_sq)) >= 0 for value in values),
            "a source pair violates its lower bound")
    require(all(qsign(qsub(upper_sq, value)) >= 0 for value in values),
            "a source pair violates its diameter upper bound")
    return values


def main():
    zero = q3()
    half = F(1, 2)
    root3_half = q3(0, half)
    base = {
        "p": (zero, zero),
        "q0": (q3(1), zero),
        "q1": (q3(-half), root3_half),
        "q2": (q3(-half), qneg(root3_half)),
    }

    base_values = check_bounds(base)
    require(sorted(value[0] for value in base_values) ==
            [F(1), F(1), F(1), F(3), F(3), F(3)] and
            all(value[1] == 0 for value in base_values),
            "the four-label fixture does not have the stated six distances")

    normals = [vsub(base["p"], base[name]) for name in ("q0", "q1", "q2")]
    total = (zero, zero)
    for normal in normals:
        total = vadd(total, normal)
        require(norm_sq(normal) == q3(1), "an exterior normal is not unit")
    require(total == (zero, zero), "the three normals are not balanced")
    require(all(dot(normals[i], normals[j]) == q3(F(-1, 2))
                for i, j in combinations(range(3), 2)),
            "the three normals are not pairwise 120 degrees apart")

    covariance = [[zero, zero], [zero, zero]]
    for normal in normals:
        for i in range(2):
            for j in range(2):
                covariance[i][j] = qadd(
                    covariance[i][j], qmul(normal[i], normal[j]))
    require(covariance == [[q3(F(3, 2)), zero],
                           [zero, q3(F(3, 2))]],
            "the normal second-moment identity failed")

    two_anchor = {"p": (q3(F(1, 10)), zero),
                  "q1": base["q1"], "q2": base["q2"]}
    two_values = check_bounds(two_anchor)
    require(all(qsign(value) > 0 for value in two_values[:2]),
            "the two-anchor control did not open both retained contacts")

    boundary = dict(base)
    boundary["p"] = (q3(-1), zero)
    boundary_values = pair_values(boundary)
    require(all(qsign(qsub(value, q3(1))) >= 0 for value in boundary_values),
            "the boundary control unexpectedly violates a lower pair bound")
    require(max(value[0] for value in boundary_values) == 4 and
            any(qsign(qsub(value, q3(3))) > 0 for value in boundary_values),
            "the boundary control did not violate the actual diameter upper bound")

    print("PASS: exact four-label fixture has three unit contacts and three diameter pairs")
    print("PASS: balanced normals and isotropic second moment verified in Q(sqrt(3))")
    print("PASS: two-anchor control admits a nonzero full-pair-feasible displacement")
    print("PASS: three-anchor boundary control meets lower bounds but violates diameter")
    print("PASS: checked fixture identities match the hypotheses of the all-direction proof")


main()
