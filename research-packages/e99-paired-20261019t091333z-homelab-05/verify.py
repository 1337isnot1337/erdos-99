"""Exact rational endpoint checks for the fixed-frame strict capacity lower bound.

These finite fixtures check endpoint geometry only. They do not certify the
compactness, lattice equality, or displacement-gap arguments in README.md.
"""
from fractions import Fraction as F
from itertools import combinations

T = F(577351, 1_000_000)
assert T < 1 and 3 * T * T > 1  # phi = 2 atan(T) is in (pi/3, pi/2)
C = (1 - T * T) / (1 + T * T)
A = 2 * T / (1 + T * T)
DELTA = 1 - 2 * C
assert C > 0 and DELTA > 0 and A * A + C * C == 1


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def sub(x, y):
    return x[0] - y[0], x[1] - y[1]


def norm2(x):
    return x[0] * x[0] + x[1] * x[1]


def grid(i, j):
    return F(i) + F(j) * C, F(j) * A


def affine(point):
    t = point[1] / A
    s = point[0] - C * t
    return s, t


def check_frame(m, n):
    assert m >= 3 and n >= 3
    L = m + n
    s = DELTA / (100 * L**2)
    h = s**2 / (100 * L**3)
    beta = F(1, 10 * L**3)
    g = 4 * beta**2 * h**2
    r = (F(1), -C / A)

    labels = {(i, j) for i in range(m + 1) for j in range(n + 1)
              if (i, j) != (1, 0)}
    interior = {(i, j) for i in range(1, m) for j in range(1, n)}
    base = {q: grid(*q) for q in labels}
    stage1 = dict(base)
    for j in range(1, n):
        stage1[1, j] = add(base[1, j], (F(0), -s * (n - j)))

    endpoint = dict(stage1)
    for i in range(2, m):
        for j in range(1, n):
            f = F(j * (n - j)) * (1 + beta * j)
            H = h * (m - i) * f
            endpoint[i, j] = add(stage1[i, j], (-H * r[0], -H * r[1]))

    checked = 0
    for x, y in combinations(sorted(labels), 2):
        assert norm2(sub(stage1[x], stage1[y])) >= 1
        d2 = norm2(sub(endpoint[x], endpoint[y]))
        if x in interior or y in interior:
            assert d2 >= 1 + g
            checked += 1
        else:
            assert d2 >= 1

    displacement_cap = DELTA / (50 * L)
    for q in interior:
        assert 0 < affine(endpoint[q])[0] < m
        assert 0 < affine(endpoint[q])[1] < n
        assert norm2(sub(endpoint[q], base[q])) < displacement_cap**2

    # If the deleted pin were restored, its pair with the moved p_(1,1)
    # would be too close. This confirms the scope requires deleting p_(1,0).
    p10 = grid(1, 0)
    restored_pair = norm2(sub(stage1[1, 1], p10))
    assert restored_pair < 1

    K = (m - 1) * (n - 1)
    N = 2 * (m + n) - 1 + (K + 1)
    assert N == (m + 1) * (n + 1)
    oler_rhs = m * n + m + n + 1
    assert oler_rhs == N
    return checked


def main():
    frames = [(3, 3), (3, 4), (4, 3), (4, 4), (3, 6), (5, 5), (6, 3)]
    pairs = sum(check_frame(m, n) for m, n in frames)
    print(f"PASS: {len(frames)} exact rational-angle frames; {pairs} strict endpoint pair checks")
    print("PASS: every target is interior, within the displacement cap, and has squared margin >= g")
    print("PASS: restoring p_(1,0) creates a subunit pair; Oler population identity is exact")
    print("LIMIT: finite endpoint checks do not verify the analytic capacity upper bound")


main()
