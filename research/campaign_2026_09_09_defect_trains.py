"""Exact bookkeeping checks for the September 9 exceptional-face train theorem.

Enumerate every connected induced subset of the 4 by 4 integer unit grid with
at least two points. Reconstruct oriented face walks, stop opposite-edge trains
at nonquadrilateral faces, and verify the forest, unique-crossing, Mantel, and
Euler/endpoint identities. Bridges and holes are allowed. All arithmetic is
integer or Fraction; no KKT, global optimality, or general-angle theorem is
encoded. Also check the radical pentagon family's rational squared-distance
formulas and bounds on its parameters. The general proofs are in
docs/reports/campaign_defect_train_extension_2026-09-09.md.

Run: python3 research/campaign_2026_09_09_defect_trains.py
"""

from fractions import Fraction as F
from itertools import combinations


POINTS = [(x, y) for y in range(4) for x in range(4)]
STEP_ORDER = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}
GRID_EDGES = [(i, j) for i, j in combinations(range(16), 2)
              if sum((a - b) ** 2 for a, b in zip(POINTS[i], POINTS[j])) == 1]


def case(mask):
    vertices = [i for i in range(16) if mask >> i & 1]
    if len(vertices) < 2:
        return None
    edges = [(i, j) for i, j in GRID_EDGES if mask >> i & 1 and mask >> j & 1]
    adj = {i: [] for i in vertices}
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)
    reached = {vertices[0]}
    queue = [vertices[0]]
    for i in queue:
        for j in adj[i]:
            if j not in reached:
                reached.add(j)
                queue.append(j)
    if len(reached) != len(vertices):
        return None
    for i in vertices:
        x, y = POINTS[i]
        adj[i].sort(key=lambda j: STEP_ORDER[(POINTS[j][0] - x, POINTS[j][1] - y)])

    # Turning clockwise from the incoming reverse edge keeps a face on the left.
    unseen = {(i, j) for i in vertices for j in adj[i]}
    faces = []
    while unseen:
        first = min(unseen)
        dart = first
        walk = []
        while True:
            i, j = dart
            unseen.remove(dart)
            walk.append(i)
            around = adj[j]
            k = around[(around.index(i) - 1) % len(around)]
            dart = j, k
            if dart == first:
                break
        twice_area = sum(POINTS[i][0] * POINTS[j][1] - POINTS[j][0] * POINTS[i][1]
                         for i, j in zip(walk, walk[1:] + walk[:1]))
        faces.append((twice_area, walk))
    outer = [w for a, w in faces if a <= 0]
    bounded = [w for a, w in faces if a > 0]
    assert len(outer) == 1
    b = len(outer[0])
    quads = [w for w in bounded if len(w) == 4]
    exceptional = [w for w in bounded if len(w) != 4]
    assert all(len(w) >= 5 for w in exceptional)
    assert len(bounded) == len(edges) - len(vertices) + 1

    edge_id = {edge: i for i, edge in enumerate(edges)}
    train_adj = [[] for _ in edges]
    crossings = []
    for w in quads:
        sides = [edge_id[tuple(sorted((i, j)))] for i, j in zip(w, w[1:] + w[:1])]
        for a, b_side in ((sides[0], sides[2]), (sides[1], sides[3])):
            train_adj[a].append(b_side)
            train_adj[b_side].append(a)
        crossings.append((sides[0], sides[1]))
    assert all(len(ns) <= 2 for ns in train_adj)
    train_id = {}
    train_count = 0
    for root in range(len(edges)):
        if root in train_id:
            continue
        train_id[root] = train_count
        members = [root]
        for i in members:
            for j in train_adj[i]:
                if j not in train_id:
                    train_id[j] = train_count
                    members.append(j)
        assert sum(len(train_adj[i]) for i in members) == 2 * (len(members) - 1)
        directions = {tuple(POINTS[j][a] - POINTS[i][a] for a in range(2))
                      for i, j in (edges[k] for k in members)}
        assert len(directions) == 1
        train_count += 1
    crossing_pairs = [tuple(sorted((train_id[a], train_id[b_side])))
                      for a, b_side in crossings]
    assert all(a != b_side for a, b_side in crossing_pairs)
    assert len(set(crossing_pairs)) == len(quads)
    crossing_set = set(crossing_pairs)
    assert not any(all(tuple(sorted(pair)) in crossing_set for pair in combinations(triple, 2))
                   for triple in combinations(range(train_count), 3))
    R = len(quads)
    f = len(exceptional)
    Q = sum(len(w) - 4 for w in exceptional)
    assert train_count == len(edges) - 2 * R
    assert 2 * train_count == b + Q + 4 * f
    assert R == len(vertices) + f - train_count - 1
    assert 4 * R <= train_count ** 2
    # Repeated outer vertices include bridge and articulation boundary walks.
    return int(f > 0), int(len(set(outer[0])) < b), R, train_count


def grid_checks():
    counts = dict(connected=0, with_exceptional_faces=0, repeated_outer_walk=0)
    maximum_trains = 0
    for mask in range(1 << 16):
        result = case(mask)
        if result is None:
            continue
        exceptional, repeated, _, trains = result
        counts['connected'] += 1
        counts['with_exceptional_faces'] += exceptional
        counts['repeated_outer_walk'] += repeated
        maximum_trains = max(maximum_trains, trains)
    assert counts['with_exceptional_faces'] > 0
    assert counts['repeated_outer_walk'] > 0
    counts['maximum_trains'] = maximum_trains
    return counts


def pentagon_checks():
    # h = sqrt(h2). It is enough to retain h2 exactly and use its positive root.
    for m in range(4, 1001):
        u = F(1, m)
        c = (1 - u * u) / (1 + u * u)
        s = 2 * u / (1 + u * u)
        h2 = 1 - (c - F(1, 2)) ** 2
        assert c * c + s * s == 1
        assert c >= F(15, 17) and s > 0
        assert h2 > F(3, 4)
        assert (c - F(1, 2)) ** 2 + h2 == 1
        assert 4 * c * c > 1
        # The other two diagonal types have squared lengths 1+2c and
        # 1/4+h2+s^2+2s sqrt(h2). Both inequalities are exact.
        assert (c + F(1, 2)) ** 2 + h2 == 1 + 2 * c > 1
        assert F(1, 4) + h2 + s * s > 1
        # Positive coefficients certify each strict turn and the area bounds.
        assert 2 * c * s > 0 and c > F(1, 2)
        assert c > u and c * (1 - c) == h2 - F(3, 4)
        assert F(3, 2) * (1 - c) + s <= 3 * u * u + 2 * u < 3 * u
        # Independently construct all coordinates in Q(sqrt(h2)), represented
        # as (a,b). Do not infer the contact graph from the displayed formulas.
        def plus(x, y):
            return x[0] + y[0], x[1] + y[1]

        def minus(x, y):
            return x[0] - y[0], x[1] - y[1]

        def times(x, y):
            return x[0] * y[0] + h2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]

        def sign(x):
            a, b = x
            if b == 0:
                return (a > 0) - (a < 0)
            if a == 0:
                return (b > 0) - (b < 0)
            if a > 0 and b > 0:
                return 1
            if a < 0 and b < 0:
                return -1
            diff = a * a - b * b * h2
            return ((diff > 0) - (diff < 0)) * (1 if a > 0 else -1)

        zero = (F(0), F(0))
        one = (F(1), F(0))
        points = [((-c, F(0)), zero), (zero, (-s, F(0))),
                  ((c, F(0)), zero), ((F(1, 2), F(0)), (F(0), F(1))),
                  ((F(-1, 2), F(0)), (F(0), F(1)))]

        def difference(p, q):
            return minus(p[0], q[0]), minus(p[1], q[1])

        for i, j in combinations(range(5), 2):
            dx, dy = difference(points[j], points[i])
            d2 = plus(times(dx, dx), times(dy, dy))
            expected = 0 if (j - i) in (1, 4) else 1
            assert sign(minus(d2, one)) == expected
            assert sign(minus((4 * c * c, F(0)), d2)) == (0 if (i, j) == (0, 2) else 1)
        for i in range(5):
            x = difference(points[(i + 1) % 5], points[i])
            y = difference(points[(i + 2) % 5], points[(i + 1) % 5])
            assert sign(minus(times(x[0], y[1]), times(x[1], y[0]))) == 1
        assert F(1, 4) + F(25, 17) ** 2 < F(900, 289)
        assert F(5, 3) < F(30, 17) <= 2 * c
    return 997


if __name__ == '__main__':
    print('Exact connected-grid train checks:', grid_checks())
    print('Exact pentagon parameter checks:', pentagon_checks())
