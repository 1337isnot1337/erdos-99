#!/usr/bin/env python3
"""Exact Gram-matrix fixtures; periodic area is not finite diameter optimality."""

from fractions import Fraction as F
from itertools import product


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def transpose(a):
    return list(map(list, zip(*a)))


def rank(a):
    a = [list(map(F, row)) for row in a]
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        a[r] = [x / a[r][col] for x in a[r]]
        for i in range(len(a)):
            if i != r:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def check_torus():
    n = 8
    gram = [[F(1), F(-1, 7)], [F(-1, 7), F(1)]]
    period = [[F(3), F(1)], [F(1), F(3)]]
    period_gram = matmul(matmul(transpose(period), gram), period)
    assert period_gram == [[F(64, 7), F(32, 7)], [F(32, 7), F(64, 7)]]
    assert F(64, 7) > 9
    edges = set()
    fixed_rows, free_rows = [], []
    for i in range(n):
        for direction, shift in enumerate((1, 5)):
            j = (i + shift) % n
            edge = tuple(sorted((i, j)))
            assert edge not in edges
            edges.add(edge)
            # Actual positive edge u or v is obtained by an integral image shift.
            rhs_a = i + (direction == 0) - j
            rhs_b = int(direction == 1)
            assert (3 * rhs_a - rhs_b) % 8 == 0
            assert (-rhs_a + 3 * rhs_b) % 8 == 0
            row = [F(0)] * (2 * n)
            row[direction * n + i] = -1
            row[direction * n + j] = 1
            fixed_rows.append(row)
            strain = [F(0)] * 3
            strain[direction] = 1
            free_rows.append(row + strain)
    assert len(edges) == 16
    assert all(i % 2 != j % 2 for i, j in edges)
    assert rank(fixed_rows) == 14
    assert rank(free_rows) == 16
    return gram


def check_path(gram):
    strain = [[F(1, 2), F(7, 2)], [F(7, 2), F(1, 2)]]
    gram_strain = matmul(gram, strain)
    assert gram_strain[0][0] == gram_strain[1][1] == 0
    assert gram_strain == transpose(gram_strain)
    assert strain[0][0] + strain[1][1] == 1
    assert strain[0][0] * strain[1][1] - strain[0][1] * strain[1][0] == -12
    times = (F(0), F(1, 180), F(1, 90), F(1, 36), F(1, 18))
    integer_pairs = 0
    for t in times:
        transform = [[int(i == j) - t * strain[i][j] for j in range(2)]
                     for i in range(2)]
        raw_gram = matmul(matmul(transpose(transform), gram), transform)
        scale_sq = 1 + 12 * t * t
        c = (-1 - 48 * t + 12 * t * t) / (7 * scale_sq)
        normalized = [[x / scale_sq for x in row] for row in raw_gram]
        assert normalized == [[1, c], [c, 1]]
        area_ratio = (1 - t - 12 * t * t) / scale_sq
        assert 0 < area_ratio <= 1
        assert F(-1, 2) <= c <= F(-1, 7)
        if t > 0:
            assert area_ratio < 1
            for m in (1, 2, 7, 100):
                assert 2 * m * m * (1 - c) > F(16, 7) * m * m
        contacts = []
        for a, b in product(range(-12, 13), repeat=2):
            if a == b == 0:
                continue
            squared = a * a + b * b + 2 * c * a * b
            lower = a * a + b * b - abs(a * b)
            assert squared >= lower >= 1
            if squared == 1:
                contacts.append((a, b))
            integer_pairs += 1
        if t < F(1, 18):
            assert set(contacts) == {(1, 0), (-1, 0), (0, 1), (0, -1)}
        else:
            assert c == F(-1, 2)
            assert area_ratio == F(7, 8)
            assert len(contacts) == 6
            assert 2 + 2 * c == 1  # 0, u, u+v is a unit triangle.
    return len(times), integer_pairs


def check_square():
    for t in (F(1, 1000), F(1, 10), F(1, 2)):
        scale_sq = 1 + t * t
        assert (1 - t * t) / scale_sq < 1
        assert 2 * (1 + t) * (1 + t) / scale_sq > 2


def main():
    gram = check_torus()
    times, pairs = check_path(gram)
    check_square()
    print("PASS: eight-label torus; 16 contacts; fixed rank 14; free-strain rank 16")
    print(f"PASS: {times} exact path states; {pairs} integer lattice vectors; "
          "strict cell compression and finite-crop diameter growth; square guard")
    print("Scope: periodic/crop regressions; no large-source global optimum or Level I closure")


if __name__ == "__main__":
    main()
