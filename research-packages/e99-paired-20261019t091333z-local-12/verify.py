from fractions import Fraction as F
from itertools import combinations


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def ledger(points):
    return {
        (i, j): sum((points[i][k] - points[j][k]) ** 2 for k in range(2))
        for i, j in combinations(range(len(points)), 2)
    }


def pinch(points, pair, t):
    points = [tuple(F(x) for x in p) for p in points]
    i, j = pair
    if len(points) < 2 or not (0 <= i < j < len(points)):
        raise ValueError("bad labels")
    if not (0 < t < F(1, 2)):
        raise ValueError("bad pinch parameter")
    before = ledger(points)
    if min(before.values()) < 1 or before[pair] != 1:
        raise ValueError("pair is not an actual contact")
    middle = tuple((points[i][k] + points[j][k]) / 2 for k in range(2))
    direction = tuple(points[j][k] - points[i][k] for k in range(2))
    moved = list(points)
    moved[i] = tuple(points[i][k] + t * direction[k] for k in range(2))
    moved[j] = tuple(points[j][k] - t * direction[k] for k in range(2))
    scale = 1 / (1 - 2 * t)
    return [tuple(middle[k] + (p[k] - middle[k]) * scale for k in range(2)) for p in moved]


def descend(points, pair, s):
    before = ledger(points)
    contacts = [edge for edge, value in before.items() if value == 1]
    if contacts != [pair]:
        raise ValueError("source does not have exactly one contact")
    i, j = pair
    middle = tuple((points[i][k] + points[j][k]) / 2 for k in range(2))
    after_points = [
        p if q in pair else tuple(middle[k] + (1 - s) * (p[k] - middle[k]) for k in range(2))
        for q, p in enumerate(points)
    ]
    after = ledger(after_points)
    require(after[pair] == 1, "fixed contact changed")
    require(all(value > 1 for edge, value in after.items() if edge != pair), "lost separation")
    require(all(after[edge] < before[edge] for edge in before if edge != pair), "nonfixed pair did not shorten")
    require(max(after.values()) < max(before.values()), "diameter did not decrease")


def expect_rejected(call, message):
    try:
        call()
    except ValueError:
        return
    raise RuntimeError(message)


square = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1)), (F(1), F(1))]
pair = (0, 1)
t = F(1, 4)
before = ledger(square)
after_points = pinch(square, pair, t)
after = ledger(after_points)
require([edge for edge, value in after.items() if value == 1] == [pair], "pinch did not leave one contact")
require(after_points[0] == square[0] and after_points[1] == square[1], "selected labels did not return")
require(max(after.values()) <= max(before.values()) / (1 - 2 * t) ** 2, "diameter bound failed")

single_contact = [(F(-1, 2), F(0)), (F(1, 2), F(0)), (F(0), F(2))]
descend(single_contact, pair, F(1, 10))

expect_rejected(lambda: pinch(square, (0, 2), F(1, 4)), "noncontact accepted")
expect_rejected(lambda: pinch(square, pair, F(1, 2)), "endpoint pinch accepted")
expect_rejected(lambda: descend(square, pair, F(1, 10)), "multiple-contact descent accepted")
print("PASS: exact Fraction pinch and one-contact descent; all pair and diameter checks; three negative controls. No Level I proof.")
