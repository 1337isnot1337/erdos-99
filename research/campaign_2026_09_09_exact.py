"""Exact regressions for the 2026-09-09 campaign; standard library only.

Checks interval signs for triples of pairwise intersecting chords of integer
convex polygons, all projective cuts, and all circular intervals; checks the
all-gap equality combinatorics; and verifies the sharp 15-degree path examples
over Q(sqrt(3)). These are finite regression checks, not a proof of the general
chord theorem, local optimality, or global diameter optimality.
Run: python3 research/campaign_2026_09_09_exact.py
"""

from fractions import Fraction as F
from itertools import combinations, product


def chord_checks():
    counts = {}
    for n in range(3, 9):
        edges = list(combinations(range(n), 2))
        count = 0
        for triple in combinations(edges, 3):
            def meet(e, f):
                a, b = e
                c, d = f
                return bool(set(e) & set(f)) or a < c < b < d or c < a < d < b
            if not all(meet(e, f) for e, f in combinations(triple, 2)):
                continue
            # Points (i,i*i). The oriented chord slope is i+j, exactly.
            ordered = sorted(triple, key=sum)
            assert len({sum(e) for e in ordered}) == 3
            for cut in range(3):
                oriented = ordered[cut:] + [(b, a) for a, b in ordered[:cut]]
                for start in range(n):
                    for size in range(1, n):
                        interval = {(start + j) % n for j in range(size)}
                        z = [int(b in interval) - int(a in interval) for a, b in oriented]
                        e, f, g = z
                        assert g * (e - f) <= 0, (n, triple, oriented, interval, z)
                        assert e * (g - f) <= 0, (n, triple, oriented, interval, z)
                        count += 1
        counts[n] = count
    return counts


def all_gap_checks():
    counts = {}
    for m in range(3, 9):
        surviving = []
        for z in product((-1, 0, 1), repeat=m):
            support = {i for i, v in enumerate(z) if v}
            if all(z[i] == z[i + 1] or support <= {i, i + 1} for i in range(m - 1)):
                assert len(support) <= 1 or len(set(z)) == 1, z
                surviving.append(z)
        assert len(surviving) == 2 * m + 3
        counts[m] = len(surviving)
    return counts


def tree_response_checks():
    """All labeled trees on six circular terminals, with unit resistances."""
    n = 6
    planar_count = diagonal_count = 0
    selected = [(0, 3), (1, 4), (2, 5)]
    for word in product(range(n), repeat=n - 2):
        degree = [1 + word.count(i) for i in range(n)]
        edges = []
        for x in word:
            leaf = next(i for i, d in enumerate(degree) if d == 1)
            edges.append(tuple(sorted((leaf, x))))
            degree[leaf] -= 1
            degree[x] -= 1
        edges.append(tuple(i for i, d in enumerate(degree) if d == 1))
        if any(a < c < b < d or c < a < d < b for (a, b), (c, d) in combinations(edges, 2)):
            continue
        planar_count += 1
        adjacency = [[] for _ in range(n)]
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)
        W = []
        for root in range(n):
            distance = [None] * n
            distance[root] = 0
            queue = [root]
            for vertex in queue:
                for neighbor in adjacency[vertex]:
                    if distance[neighbor] is None:
                        distance[neighbor] = distance[vertex] + 1
                        queue.append(neighbor)
            W.append(distance)
        # Tree effective resistances equal path lengths. Transfer polarization.
        if all(W[a][c] - W[a][d] - W[b][c] + W[b][d] == 0
               for (a, b), (c, d) in combinations(selected, 2)):
            diagonal_count += 1
            assert max(map(len, adjacency)) == 5
            hub = next(i for i in range(n) if len(adjacency[i]) == 5)
            r = [int(i != hub) for i in range(n)]
            assert all(W[i][j] == r[i] + r[j] for i, j in combinations(range(n), 2))
    assert (planar_count, diagonal_count) == (273, 6)
    # Two selected crossing pairs on a unit-resistance 4-cycle: the m=2 limit.
    W4 = [[F(0) if i == j else F(1) if (i - j) % 4 == 2 else F(3, 4)
           for j in range(4)] for i in range(4)]
    assert W4[0][1] - W4[0][3] - W4[2][1] + W4[2][3] == 0
    assert W4[0][2] + W4[1][3] != W4[0][1] + W4[2][3]
    return planar_count, diagonal_count


# Elements a+b sqrt(3), with exact sign comparisons.
def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[0], -x[1]


def mul(x, y):
    return x[0] * y[0] + 3 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def scale(k, x):
    return k * x[0], k * x[1]


def sign(x):
    a, b = x
    if not b:
        return (a > 0) - (a < 0)
    if not a:
        return (b > 0) - (b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    t = a * a - 3 * b * b
    return ((t > 0) - (t < 0)) * (1 if a > 0 else -1)


def sharp_path_checks():
    one = (F(1), F(0))
    r = (F(2), F(-1))
    c_squared = (F(1, 2), F(1, 4))
    assert add(mul(r, r), scale(2, mul((0, 1), r))) == one
    counts = {}
    for m in range(2, 26):
        # Coordinates divided by c=cos(pi/12); c^2=(2+sqrt(3))/4.
        points = [((F(j), F(0)), scale(min(j, 2 * m - j), r)) for j in range(2 * m + 1)]
        points.append(((F(m), F(0)), (F(0), F(-m))))
        diameter_squared = scale(4 * m * m, c_squared)
        contacts = set()
        diameters = set()
        for i, j in combinations(range(len(points)), 2):
            dx = add(points[i][0], neg(points[j][0]))
            dy = add(points[i][1], neg(points[j][1]))
            d2 = mul(c_squared, add(mul(dx, dx), mul(dy, dy)))
            assert sign(add(d2, neg(one))) >= 0, (m, i, j, d2)
            assert sign(add(diameter_squared, neg(d2))) >= 0, (m, i, j, d2)
            if d2 == one:
                contacts.add((i, j))
            if d2 == diameter_squared:
                diameters.add((i, j))
        assert contacts == {(i, i + 1) for i in range(2 * m)}
        assert (m, 2 * m + 1) in diameters
        assert (0, 2 * m) in diameters
        counts[m] = (len(points), len(contacts), len(diameters))
    return counts


if __name__ == "__main__":
    print("Exact chord/interval checks:", chord_checks())
    print("All-gap equality signatures (zero, singletons, constants):", all_gap_checks())
    print("Six-terminal noncrossing trees / diagonal-transfer stars:", tree_response_checks())
    results = sharp_path_checks()
    print("Sharp path families: m=2..25; all pair distances certified; contact graph is a path.")
    print("Endpoint cases (vertices, unit contacts, diameters):", results[2], results[25])
