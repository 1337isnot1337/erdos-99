#!/usr/bin/env python3
"""Exact sharpness regressions for the Profile B puncture-fan theorem.

These are abstract quotient models, not K8 four-cycle states or packings.
Fraction elimination certifies dimensions, coefficient punctures and images.
The general incidence theorem is proved in the companion Markdown note.
"""

from fractions import Fraction
from itertools import combinations


def rank(rows):
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for i in range(r + 1, len(a)):
            if a[i][c]:
                q = a[i][c] / a[r][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


E = tuple(tuple(int(i == j) for j in range(9)) for i in range(9))


def add(*vectors):
    return tuple(sum(v[j] for v in vectors) for j in range(9))


def projected_plane(plane, deleted):
    return [tuple(x for j, x in enumerate(row) if j not in deleted) for row in plane]


def clean_coordinates(plane):
    return tuple(
        i for i in range(8)
        if all(
            rank(projected_plane(plane, {i, *rest})) == 2
            for size in range(3)
            for rest in combinations([j for j in range(8) if j != i], size)
        )
    )


def check_model(name, ell, plane, basis, selected, expected_counts):
    assert rank(ell) == 6
    assert rank(plane) == 2
    assert rank(basis) == 9
    for word in plane:
        assert all(sum(word[i] * ell[i][j] for i in range(8)) == 0 for j in range(9))
    # These two independent relations are the entire coefficient plane.
    assert len(ell) - rank(ell) == len(plane)
    clean = clean_coordinates(plane)
    assert selected in clean
    counts = []
    for j in range(8):
        if j == selected:
            continue
        kernel = [ell[selected], ell[j]]
        assert rank(kernel) == 2
        surviving = [v for v in basis if rank(kernel + [v]) == 3]
        # Dimension of the images of surviving labels in V/kernel.
        assert rank(kernel + surviving) - rank(kernel) == 7
        counts.append(len(surviving))
    assert tuple(counts) == expected_counts
    center_basis = [v for v in basis if rank([ell[selected], v]) == 1]
    b = len(center_basis)
    assert b in (0, 1)
    assert sum(9 - q for q in counts) == 6 + 6 * b
    for i in clean:
        others = [j for j in range(8) if j != i]
        for j, k in combinations(others, 2):
            assert rank([ell[i], ell[j], ell[k]]) == 3
            # Intersection dimension of the two planes is exactly one.
            assert 2 + 2 - rank([ell[i], ell[j], ell[k]]) == 1
            kernel = [ell[i], ell[j], ell[k]]
            surviving = [v for v in basis if rank(kernel + [v]) == 4]
            assert rank(kernel + surviving) - rank(kernel) == 6
    print(name, 'clean', clean, 'retained', tuple(counts), 'sum', sum(counts))
    return clean


def main():
    ell = (E[0], E[1], E[2], E[3], add(E[2], E[3]), E[4], E[5], add(E[4], E[5]))
    plane = ((0, 0, -1, -1, 1, 0, 0, 0), (0, 0, 0, 0, 0, -1, -1, 1))
    clean = check_model('bound51', ell, plane, E, 0, (7, 7, 7, 8, 7, 7, 8))
    assert clean == (0, 1)
    check_model('bound51_second_clean', ell, plane, E, 1, (7, 7, 7, 8, 7, 7, 8))

    directions = E[1:6] + (add(*E[1:6]), tuple(sum(i * E[i][j] for i in range(1, 6)) for j in range(9)))
    ell = (E[0],) + directions
    plane = ((0, -1, -1, -1, -1, -1, 1, 0), (0, -1, -2, -3, -4, -5, 0, 1))
    basis = E[1:6] + (add(*E[:6]),) + E[6:]
    clean = check_model('bound57', ell, plane, basis, 0, (8, 8, 8, 8, 8, 8, 9))
    assert clean == tuple(range(8))
    print('PASS: exact sharp abstract puncture models; no geometric closure claimed')


if __name__ == '__main__':
    main()
