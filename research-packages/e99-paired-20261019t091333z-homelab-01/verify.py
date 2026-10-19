"""Exact checks for the finite triad fixture and the two-anchor control.

The universal direction and continuity argument live in README.md; this
finite checker is not a replacement for that proof.
"""

from fractions import Fraction
from itertools import combinations


def q(a=0, b=0):
    """Exact pair (a,b) represents a + b*sqrt(3)."""
    return Fraction(a), Fraction(b)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[0], -x[1]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return x[0] * y[0] + 3 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def dot(x, y):
    return add(mul(x[0], y[0]), mul(x[1], y[1]))


def difference(x, y):
    return sub(x[0], y[0]), sub(x[1], y[1])


def pair_squares(points):
    return [dot(difference(points[a], points[b]),
                difference(points[a], points[b]))
            for a, b in combinations(points, 2)]


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    zero = q()
    half = Fraction(1, 2)
    root3_half = q(0, half)
    points = {
        "p": (zero, zero),
        "q0": (q(1), zero),
        "q1": (q(-half), root3_half),
        "q2": (q(-half), neg(root3_half)),
    }

    distances = pair_squares(points)
    expected = sorted([q(1), q(1), q(1), q(3), q(3), q(3)])
    check(sorted(distances) == expected,
          "the complete four-label squared-distance ledger changed")

    normals = [difference(points["p"], points[name])
               for name in ("q0", "q1", "q2")]
    check(all(dot(n, n) == q(1) for n in normals),
          "an anchor normal is not unit length")
    total = (zero, zero)
    for n in normals:
        total = add(total[0], n[0]), add(total[1], n[1])
    check(total == (zero, zero), "the three normals do not sum to zero")
    check(all(dot(normals[i], normals[j]) == q(-half)
              for i, j in combinations(range(3), 2)),
          "the anchor normals are not a balanced 120-degree triad")

    moment = [[zero, zero], [zero, zero]]
    for n in normals:
        for i in range(2):
            for j in range(2):
                moment[i][j] = add(moment[i][j], mul(n[i], n[j]))
    check(moment == [[q(Fraction(3, 2)), zero],
                     [zero, q(Fraction(3, 2))]],
          "the second-moment identity is not (3/2)I")

    # With q0 removed, p_s=(s,0), 0<=s<=1/4, has both squared distances
    # 1+s+s^2. This is increasing on the interval and ranges from 1 to 21/16.
    s = Fraction(1, 4)
    moved = (q(s), zero)
    two_anchor = {
        "p": moved,
        "q1": points["q1"],
        "q2": points["q2"],
    }
    control = pair_squares(two_anchor)
    check(sorted(control) == sorted([q(Fraction(21, 16)),
                                     q(Fraction(21, 16)), q(3)]),
          "the two-anchor positive-motion control changed")
    check(all(value[1] == 0 and 1 <= value[0] <= 3 for value in control),
          "the two-anchor control violates a lower or diameter upper bound")

    print("PASS: all six exact source distances are 1 or 3 in Q(sqrt(3))")
    print("PASS: balanced triad and second-moment identities hold exactly")
    print("PASS: deleting one anchor admits the full-pair-feasible path control")
    print("LIMIT: universal direction and continuous-path claims are proved in README.md")


main()
