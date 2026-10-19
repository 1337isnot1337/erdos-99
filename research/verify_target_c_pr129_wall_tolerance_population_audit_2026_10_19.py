#!/usr/bin/env python3
"""Independent exact check of PR #129's opened 7-by-7 endpoint ledger.

Unlike the submitted verifier, this checker builds the endpoint as a set of
retained source labels, checks the 64-to-51 deletion identity directly, and
asserts the reported exact maximum squared distance (84).
"""

from fractions import Fraction as F
from itertools import combinations


def endpoint_7():
    m = n = 7
    length = m + n
    eps = F(1, 10 * length**4)
    amplitude = F(1, 100 * length**3)
    original = {(i, j) for i in range(m + 1) for j in range(n + 1)}
    deleted = {
        (i, 0) for i in range(m)
    } | {
        (0, j) for j in range(1, n)
    }
    assert len(original) == 64
    assert len(deleted) == 13

    points = {}
    for i, j in sorted(original - deleted):
        if i == m or j == n:
            # Store rational (x,q) for physical coordinates (x,sqrt(3)*q).
            x, y = F(i) + F(j, 7), F(4 * j, 7)
            kind = "wall"
        else:
            lam = (m - i) * (n - j) * (1 + eps * (m - i))
            x = F(i) + F(j, 7) - amplitude * lam * F(8, 7)
            y = F(4 * j, 7) - amplitude * lam * F(4, 7)
            kind = "moved"
        points[(i, j)] = (kind, x, y)

    assert set(points) == original - deleted
    assert len(points) == 51
    assert sum(kind == "wall" for kind, _, _ in points.values()) == 15
    assert sum(kind == "moved" for kind, _, _ in points.values()) == 36
    return points


def main():
    points = endpoint_7()
    lower_pairs = upper_pairs = moved_pairs = contacts = 0
    max_sq = F(0)
    max_labels = None
    for label_a, label_b in combinations(sorted(points), 2):
        kind_a, xa, ya = points[label_a]
        kind_b, xb, yb = points[label_b]
        dx, dy = xa - xb, ya - yb
        sq = dx * dx + 3 * dy * dy
        assert sq >= 1, (label_a, label_b, sq, "lower bound")
        lower_pairs += 1
        if kind_a == "moved" or kind_b == "moved":
            assert sq > 1, (label_a, label_b, sq, "strict moved pair")
            moved_pairs += 1
        elif sq == 1:
            contacts += 1
        assert sq <= 112, (label_a, label_b, sq, "source diameter upper bound")
        upper_pairs += 1
        if sq > max_sq:
            max_sq, max_labels = sq, (label_a, label_b)

    assert lower_pairs == upper_pairs == 1275
    assert moved_pairs == 1170
    assert contacts == 14
    assert max_sq == 84, (max_sq, max_labels)
    assert max_labels == ((0, 7), (7, 0))
    assert 64 - len(points) == len({(i, 0) for i in range(7)} | {(0, j) for j in range(1, 7)}) == 13
    print(
        "PASS independent rational endpoint: source=64, deleted=13, endpoint=51, "
        "pairs=1275, moved-involving=1170, contacts=14, max_squared=84 < 112"
    )


if __name__ == "__main__":
    main()
