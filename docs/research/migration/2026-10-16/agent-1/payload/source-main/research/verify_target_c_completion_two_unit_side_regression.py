"""Check the finite even-polygon ear construction.

The script verifies the combinatorial triangulation and its number of ears.  It does
not prove global optimality, a harmonic-cell realization, or a C-II counterexample.
"""

from __future__ import annotations


def chord_crosses(a: int, b: int, c: int, d: int, n: int) -> bool:
    """Return whether two non-sharing chords have alternating endpoints."""

    def between(x: int, y: int, z: int) -> bool:
        # Strictly between y and z in the positively oriented cyclic interval.
        return (x - y) % n < (z - y) % n

    if len({a, b, c, d}) < 4:
        return False
    return between(c, a, b) != between(d, a, b) and between(a, c, d) != between(b, c, d)


def triangulation(n: int) -> tuple[list[tuple[int, int]], list[int]]:
    if n < 6 or n % 2:
        raise ValueError("n must be even and at least six")
    evens = list(range(0, n, 2))
    odds = list(range(1, n, 2))
    # One ear diagonal for each even vertex; these form the odd-vertex polygon.
    ear_diagonals = [((i - 1) % n, (i + 1) % n) for i in evens]
    # Fan-triangulate the odd polygon from its first vertex.
    cell_diagonals = [(odds[0], odds[j]) for j in range(2, len(odds) - 1)]
    return ear_diagonals + cell_diagonals, evens


def check(n: int) -> None:
    diagonals, ears = triangulation(n)
    m = n // 2
    cell_triangle_count = m - 2
    d_tile = (n - 2) - cell_triangle_count
    assert len(diagonals) == n - 3
    assert len({tuple(sorted(edge)) for edge in diagonals}) == n - 3
    for i, first in enumerate(diagonals):
        for second in diagonals[i + 1 :]:
            assert not chord_crosses(*first, *second, n)
    assert len(ears) == n // 2
    assert d_tile == m
    assert n == 2 * d_tile
    print(
        f"n={n}: diagonals={len(diagonals)}, cell_triangles={cell_triangle_count}, "
        f"d_tile={d_tile}, uncovered_unit_sides={n}=2*d_tile: OK"
    )


if __name__ == "__main__":
    for n in (6, 8, 10, 20, 100):
        check(n)
