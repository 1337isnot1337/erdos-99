#!/usr/bin/env python3
"""Exact certificate for the five-row near-unit blocker packing lemma.

The geometric statement certified here is:

    Let S_L = ([0,L] x {0}) + B(0,1/2).  If L <= 21/20, then every
    subset X of S_L with pairwise distances at least sqrt(3)/2 has
    |X| <= 5.

The upper bound is proved by a finite rational grid cover.  Every grid-cell
containment and every compatibility test is reduced to integer squared-
distance comparisons.  Floating point is used only for human-readable
printed constants after the exact assertions have passed.
"""

from fractions import Fraction
from itertools import combinations
import math
import random

GRID = 24
L_NUM = 21
L_DEN = 20


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def build_cover_cells(n: int = GRID, p: int = L_NUM, q: int = L_DEN):
    """Return all 1/n grid squares whose closure meets S_{p/q}.

    A cell is represented by integer bounds (x0,x1,y0,y1), meaning the
    closed rectangle [x0/n,x1/n] x [y0/n,y1/n].  The intersection test is
    exact after scaling all coordinates by n*q.
    """
    assert n % 2 == 0
    x_start = -n // 2
    x_stop = ceil_div(n * (2 * p + q), 2 * q)  # ceil(n*(L+1/2))
    y_start = -n // 2
    y_stop = n // 2

    scale_radius = n * q // 2
    assert 2 * scale_radius == n * q
    segment_right = p * n

    cells = []
    for ix in range(x_start, x_stop):
        X0 = ix * q
        X1 = (ix + 1) * q
        if X1 < 0:
            dx = -X1
        elif X0 > segment_right:
            dx = X0 - segment_right
        else:
            dx = 0

        for iy in range(y_start, y_stop):
            Y0 = iy * q
            Y1 = (iy + 1) * q
            if Y1 < 0:
                dy = -Y1
            elif Y0 > 0:
                dy = Y0
            else:
                dy = 0

            if dx * dx + dy * dy <= scale_radius * scale_radius:
                cells.append((ix, ix + 1, iy, iy + 1))
    return cells


def cells_may_host_separated_points(a, b, n: int = GRID) -> bool:
    """Exact over-approximate compatibility for two closed grid cells.

    If the maximum distance between the two rectangles is < sqrt(3)/2,
    they cannot contain a valid pair.  Equality is retained as compatible.
    """
    x0, x1, y0, y1 = a
    X0, X1, Y0, Y1 = b
    dx = max(abs(x0 - X1), abs(x1 - X0))
    dy = max(abs(y0 - Y1), abs(y1 - Y0))
    # (dx^2+dy^2)/n^2 >= 3/4  <=>  4(... ) >= 3 n^2.
    return 4 * (dx * dx + dy * dy) >= 3 * n * n


def build_compatibility_graph(cells, n: int = GRID):
    """Build the compatibility graph as Python-int adjacency bitsets."""
    N = len(cells)
    adj = [0] * N
    for i, a in enumerate(cells):
        bits = 0
        for j in range(i + 1, N):
            if cells_may_host_separated_points(a, cells[j], n):
                bits |= 1 << j
        adj[i] |= bits
        q = bits
        while q:
            bit = q & -q
            j = bit.bit_length() - 1
            q -= bit
            adj[j] |= 1 << i
    return adj


def has_clique_at_least_k(adj, k: int):
    """Exact branch-and-bound clique decision with a greedy-color bound.

    Returns (answer, visited_nodes).  The coloring is only an upper bound;
    no heuristic decision is accepted as a proof of absence.
    """
    visited = 0

    def greedy_color_sort(P: int):
        # Partition P greedily into independent color classes.  Vertices are
        # appended color class by color class, so bounds[t] is a valid upper
        # bound on a clique contained in the prefix through order[t].
        order = []
        bounds = []
        remaining = P
        color = 0
        while remaining:
            color += 1
            available = remaining
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                order.append(v)
                bounds.append(color)
                remaining -= bit
                available -= bit
                # Keep only vertices nonadjacent to v in this color class.
                available &= ~adj[v]
        return order, bounds

    def expand(P: int, size: int) -> bool:
        nonlocal visited
        visited += 1
        if size >= k:
            return True
        if P.bit_count() < k - size:
            return False

        order, bounds = greedy_color_sort(P)
        for idx in range(len(order) - 1, -1, -1):
            if size + bounds[idx] < k:
                return False
            v = order[idx]
            bit = 1 << v
            if not (P & bit):
                continue
            if expand(P & adj[v], size + 1):
                return True
            P -= bit
        return False

    return expand((1 << len(adj)) - 1, 0), visited


def brute_has_k(adj, k: int) -> bool:
    """Slow reference implementation used only in small self-tests."""
    n = len(adj)
    for S in combinations(range(n), k):
        if all((adj[i] >> j) & 1 for i, j in combinations(S, 2)):
            return True
    return False


def self_test_clique_solver():
    # Fixed complete and incomplete sanity checks.
    K6 = [(1 << 6) - 1 - (1 << i) for i in range(6)]
    assert has_clique_at_least_k(K6, 6)[0]
    K5_plus_isolate = [(1 << 5) - 1 - (1 << i) for i in range(5)] + [0]
    assert not has_clique_at_least_k(K5_plus_isolate, 6)[0]

    # Compare the branch-and-bound routine against brute force on deterministic
    # small random graphs.  This tests both positive and negative instances.
    rng = random.Random(20260917)
    for n in range(5, 10):
        for _ in range(12):
            adj = [0] * n
            for i in range(n):
                for j in range(i + 1, n):
                    if rng.randrange(2):
                        adj[i] |= 1 << j
                        adj[j] |= 1 << i
            for k in range(2, min(6, n) + 1):
                got = has_clique_at_least_k(adj, k)[0]
                want = brute_has_k(adj, k)
                assert got == want, (n, k, got, want)


def stadium_contains(x: Fraction, y: Fraction, L: Fraction) -> bool:
    if x < 0:
        dx = -x
    elif x > L:
        dx = x - L
    else:
        dx = Fraction(0)
    return dx * dx + y * y <= Fraction(1, 4)


def check_sharp_five_point_construction():
    # A completely rational five-point packing already fits in S_1.
    pts = [
        (Fraction(-1, 2), Fraction(0)),
        (Fraction(1, 4), Fraction(1, 2)),
        (Fraction(1, 4), Fraction(-1, 2)),
        (Fraction(6, 5), Fraction(9, 20)),
        (Fraction(6, 5), Fraction(-9, 20)),
    ]
    L = Fraction(1)
    assert all(stadium_contains(x, y, L) for x, y in pts)
    for (x, y), (X, Y) in combinations(pts, 2):
        assert (x - X) ** 2 + (y - Y) ** 2 >= Fraction(3, 4)
    return pts


def check_propagated_constants():
    s0 = Fraction(791, 320_000_000)
    gamma6 = s0 / 12
    gamma7 = Fraction(113, 640_000_000)
    assert gamma6 == Fraction(791, 3_840_000_000)
    assert gamma6 / gamma7 == Fraction(7, 6)

    Tstar = Fraction(6121, 2000)
    pure = Fraction(1609, 2500)  # 0.6436
    threaded = gamma6 * pure / (16 * Tstar)
    assert threaded == Fraction(1_272_719, 470_092_800_000_000)

    # With A*=14/(3 sqrt(3)), gamma6/(48 A*) equals
    # (113/122880000000)*sqrt(3).
    coeff = Fraction(113, 122_880_000_000)
    return gamma6, threaded, coeff


def main():
    self_test_clique_solver()

    # One cell cannot contain two valid points.
    assert Fraction(2, GRID * GRID) < Fraction(3, 4)

    cells = build_cover_cells()
    assert len(cells) == 1096
    adj = build_compatibility_graph(cells)
    has6, nodes = has_clique_at_least_k(adj, 6)
    assert not has6

    check_sharp_five_point_construction()
    gamma6, threaded, coeff = check_propagated_constants()

    print("five-row capsule packing certificate: PASS")
    print("stadium length cap = 21/20")
    print("grid = 1/24; retained cover cells =", len(cells))
    print("K6 search nodes =", nodes)
    print("packing number = 5 (upper certificate + exact rational construction)")
    print("gamma6 =", gamma6, "=", float(gamma6))
    print("threaded-lower coefficient =", threaded, "=", float(threaded))
    print("Oler-path upper coefficient =", coeff, "* sqrt(3) =", float(coeff) * math.sqrt(3.0))


if __name__ == "__main__":
    main()
