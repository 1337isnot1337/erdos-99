#!/usr/bin/env python3
"""Standalone exact checker for the shared-carrier disjoint-return regression.

The boundary set consists of artificial pins, not actual diameter endpoints.
Checks certify the stated finite geometry, positive pinned equilibrium, a
triangular pinned-rigidity minor, and two different contact flow capacities.
They do not certify full-source KKT, optimality, or a canonical C-II source.
"""

from collections import Counter, defaultdict, deque
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import json

def contact_separator(contacts, roots, loaded):
    """Integral vertex-split flow, endpoint-inclusive separator and paths."""
    vertices = sorted({v for e in contacts for v in e})
    index = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    source, sink = 2 * n, 2 * n + 1
    capacity = defaultdict(Counter)

    def arc(a, b, c):
        capacity[a][b] += c
        capacity[b][a] += 0

    for v, i in index.items():
        arc(i, i + n, 1)
        if v in roots:
            arc(source, i, n + 1)
        if v in loaded:
            arc(i + n, sink, n + 1)
    for a, b in contacts:
        arc(index[a] + n, index[b], n + 1)
        arc(index[b] + n, index[a], n + 1)
    original = {a: dict(row) for a, row in capacity.items()}
    flow = 0
    while True:
        parent, todo = {source: None}, deque([source])
        while todo and sink not in parent:
            a = todo.popleft()
            for b, c in capacity[a].items():
                if c > 0 and b not in parent:
                    parent[b] = a
                    todo.append(b)
        if sink not in parent:
            break
        b = sink
        while parent[b] is not None:
            a = parent[b]
            capacity[a][b] -= 1
            capacity[b][a] += 1
            b = a
        flow += 1
    reachable = set(parent)
    separator = {v for v, i in index.items()
                 if i in reachable and i + n not in reachable}
    assert len(separator) == flow

    positive_flow = defaultdict(Counter)
    for a, row in original.items():
        for b, c in row.items():
            if c > 0 and c > capacity[a][b]:
                positive_flow[a][b] = c - capacity[a][b]
    paths, used = [], set()
    for _ in range(flow):
        parent, todo = {source: None}, deque([source])
        while todo and sink not in parent:
            a = todo.popleft()
            for b, c in positive_flow[a].items():
                if c > 0 and b not in parent:
                    parent[b] = a
                    todo.append(b)
        assert sink in parent
        sequence, b = [], sink
        while parent[b] is not None:
            a = parent[b]
            positive_flow[a][b] -= 1
            sequence.append(b)
            b = a
        sequence.reverse()
        path = [vertices[i] for i in sequence if i < n]
        assert path[0] in roots and path[-1] in loaded
        assert not (set(path) & used)
        assert len(path) == len(set(path))
        used.update(path)
        for a, b in zip(path, path[1:]):
            assert edge(a, b) in contacts
        paths.append(path)
    assert len(paths) == flow
    return separator, paths, vertices




def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def mul(c, v):
    return c * v[0], c * v[1]


def norm2(v):
    return v[0] ** 2 + v[1] ** 2


def edge(a, b):
    return tuple(sorted((a, b)))


def rotate(v, t):
    c, s = (1 - t*t) / (1 + t*t), 2*t / (1 + t*t)
    return c*v[0] - s*v[1], s*v[0] + c*v[1]


def build(m):
    assert m >= 12
    r = F(isqrt(3*m*m) // 3 + 2, m)
    base = ((1 - r*r) / (1 + r*r), 2*r / (1 + r*r))
    increments = {}
    partial = {}
    for side, sign in ((-1, 1), (1, -1)):
        partial[side] = [(F(0), F(0))]
        increments[side] = []
        for j in range(1, m + 1):
            t = F(sign*(m + 1 - 2*j), 100*m*m)
            v = rotate(base, t)
            assert F(1, 4) < v[0] < F(1, 2)
            assert v[1] > F(4, 5)
            increments[side].append(v)
            partial[side].append(add(partial[side][-1], v))
    assert partial[-1][-1] == partial[1][-1]
    points = {}
    for i in range(2*m + 1):
        side = -1 if i < m else 1
        rows = range(m + 1) if i != m else (0, m)
        for j in rows:
            points[i, j] = add((F(i), F(0)), partial[side][j])
    contacts = {
        edge(a, b) for a in points for b in ((a[0] + 1, a[1]), (a[0], a[1] + 1))
        if b in points
    }
    pinned = {p for p in points if p[0] in (0, 2*m) or p[1] in (0, m)}
    carrier = {
        e for e in contacts
        if all(v in pinned for v in e)
        or (e[0][0] == e[1][0] and e[0][0] in (m - 1, m + 1))
    }
    roots = {(m - 1, j) for j in range((m + 2)//3, 2*m//3 + 1)}
    return points, contacts, pinned, carrier, roots, increments


def check(m):
    points, contacts, pinned, carrier, roots, increments = build(m)
    pairs = 0
    diameter2, diameter_pairs = F(0), []
    for a, b in combinations(points, 2):
        d2 = norm2(sub(points[a], points[b]))
        assert d2 >= 1, (m, a, b, d2)
        assert (d2 == 1) == (edge(a, b) in contacts), (m, a, b, d2)
        if d2 > diameter2:
            diameter2, diameter_pairs = d2, [(a, b)]
        elif d2 == diameter2:
            diameter_pairs.append((a, b))
        pairs += 1
    actual_loaded = {v for e in diameter_pairs for v in e}
    assert not roots & actual_loaded
    assert pinned - actual_loaded
    assert (m, 0) in pinned - actual_loaded
    # All graph edges change the index parity, so no contact triangle exists.
    assert all((sum(a) - sum(b)) % 2 for a, b in contacts)
    assert len(points) == 2*m*(m + 1) + 2
    assert len(pinned) == 6*m and len(carrier) == 8*m
    assert diameter2 >= F(81, 16)*m*m > 2*len(points)
    # A square-grid crop of n points has squared diameter < 2n.
    grid_side = isqrt(len(points))
    if grid_side*grid_side < len(points):
        grid_side += 1
    assert 2*(grid_side - 1)**2 < 2*len(points) < diameter2

    weights = {}
    for a, b in contacts:
        i, j = a
        if a[0] == b[0]:
            side = -1 if i < m else 1
            weights[a, b] = 1 / increments[side][j][1]
        elif j in (0, m):
            weights[a, b] = F(1)
        else:
            side = -1 if i < m else 1
            prev, nxt = increments[side][j - 1], increments[side][j]
            beta = nxt[0] / nxt[1] - prev[0] / prev[1]
            if side == -1:
                assert beta > 0
                weights[a, b] = (m - 1 - i)*beta
            else:
                assert beta < 0
                weights[a, b] = (i - m)*(-beta)
        assert weights[a, b] > 0
    reaction = {p: (F(0), F(0)) for p in points}
    for (a, b), w in weights.items():
        force = mul(w, sub(points[b], points[a]))
        reaction[a] = add(reaction[a], force)
        reaction[b] = sub(reaction[b], force)
    free = set(points) - pinned
    assert all(reaction[p] == (0, 0) for p in free)

    # An explicit triangular full pinned-rigidity minor: horizontal rows
    # determine each free x-coordinate from its pinned outer side; vertical
    # rows then determine y-coordinates from the pinned bottom row. All
    # vertical pivot coefficients are nonzero exact rationals.
    selected = set()
    x_known = set(pinned)
    for columns in (range(1, m), range(2*m - 1, m, -1)):
        for i in columns:
            for j in range(1, m):
                prev = (i - 1, j) if i < m else (i + 1, j)
                p = i, j
                assert prev in x_known
                e = edge(p, prev)
                assert e in contacts and sub(points[p], points[prev])[1] == 0
                assert e not in selected
                selected.add(e)
                x_known.add(p)
    assert x_known == set(points)
    y_known = set(pinned)
    for j in range(1, m):
        for i in list(range(1, m)) + list(range(m + 1, 2*m)):
            p, prev = (i, j), (i, j - 1)
            assert prev in y_known
            e = edge(p, prev)
            assert e in contacts and sub(points[p], points[prev])[1] > 0
            assert e not in selected
            selected.add(e)
            y_known.add(p)
    assert y_known == set(points)
    assert len(selected) == 2*len(free)

    # Every selected terminal lies on a distinct v_j train with an actual
    # horizontal contact rail of m-1 edges, ending on the inner face.
    owner = {}
    degrees = Counter()
    for columns, side in ((range(m - 1), -1), (range(m + 1, 2*m), 1)):
        for i in columns:
            for j in range(m + 1):
                owner[edge((i, j), (i + 1, j))] = ("u", side, i)
        for i in list(columns) + [columns[-1] + 1]:
            for j in range(m):
                owner[edge((i, j), (i, j + 1))] = ("v", side, j)
    singletons = contacts - set(owner)
    assert len(singletons) == 4
    for e in singletons:
        owner[e] = ("singleton", e)
    assert set(owner) == contacts
    crossings = set()
    quad_count = 0
    for columns in (range(m - 1), range(m + 1, 2*m)):
        for i in columns:
            for j in range(m):
                w = [(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]
                es = [edge(w[k], w[(k + 1) % 4]) for k in range(4)]
                assert all(e in contacts for e in es)
                assert owner[es[0]] == owner[es[2]]
                assert owner[es[1]] == owner[es[3]]
                u = sub(points[w[1]], points[w[0]])
                v = sub(points[w[3]], points[w[0]])
                assert add(points[w[0]], add(u, v)) == points[w[2]]
                assert norm2(u) == norm2(v) == 1
                area = u[0]*v[1] - u[1]*v[0]
                assert area > 0 and area*area > F(3, 4)
                cross = owner[es[0]], owner[es[1]]
                assert cross not in crossings
                crossings.add(cross)
                degrees.update(cross)
                quad_count += 1
    assert quad_count == len(crossings) == 2*m*(m - 1)
    assert len(set(owner.values())) == 4*m + 2
    assert all(d == (m if t[0] == "u" else m - 1) for t, d in degrees.items())
    assert set(degrees) == set(owner.values()) - {owner[e] for e in singletons}
    for i, j in roots:
        owned = [edge((k, j), (k, j + 1)) for k in range(m)]
        rails = [edge((k, j), (k + 1, j)) for k in range(m - 1)]
        assert all(e in contacts for e in owned + rails)
        vectors = [sub(points[e[1]], points[e[0]]) for e in owned]
        assert len(set(vectors)) == 1
        assert len(rails) == m - 1

    sparse_cut, sparse_paths, _ = contact_separator(carrier, roots, pinned)
    full_cut, full_paths, _ = contact_separator(contacts, roots, pinned)
    assert len(sparse_cut) == len(sparse_paths) == 2
    assert len(full_cut) == len(full_paths) == len(roots)
    # Every contact changes one index by one. Any path from a central
    # root to the artificial pin set has at least floor(m/3) edges.
    floor_depth = m//3
    for i, j in roots:
        assert min(i, 2*m - i, j, m - j) >= floor_depth
    assert all(len(p) - 1 >= floor_depth for p in full_paths)
    explicit_paths = [[(i, j) for i in range(m - 1, -1, -1)] for _, j in sorted(roots)]
    assert all(all(edge(a, b) in contacts for a, b in zip(p, p[1:]))
               for p in explicit_paths)
    assert sum(map(len, explicit_paths)) == len(set(v for p in explicit_paths for v in p))

    # Exact positive excess, with a certified O(m) sum. Each grain's
    # rhombus area is v_j.y; 4/5 < sqrt(3)/2 < 7/8.
    rhombus_areas = [v[1] for side in (-1, 1) for v in increments[side]]
    assert all(y*y > F(3, 4) for y in rhombus_areas)
    # Relative to the area of the base direction, variation is O(1);
    # the base's angular departure from pi/3 is O(1/m).
    r = F(isqrt(3*m*m)//3 + 2, m)
    assert (r - F(2, m))**2 < F(1, 3) < (r - F(1, m))**2
    return {
        "m": m, "source_points": len(points), "all_pair_checks": pairs,
        "strict_rhombi": 2*m*(m - 1), "complete_trains": 4*m + 2,
        "singleton_trains": 4, "positive_contact_weights": len(weights),
        "pinned_rigidity_minor_order": 2*len(free),
        "carrier_edges": len(carrier), "selected_long_terminal_roots": len(roots),
        "carrier_disjoint_returns": len(sparse_paths),
        "full_contact_disjoint_returns": len(full_paths),
        "independent_return_step_lower_bound": len(roots)*floor_depth,
        "actual_diameter_endpoint_count": len(actual_loaded),
    }


def main():
    cases = [check(m) for m in (12, 16, 24)]
    print(json.dumps({
        "status": "PASS", "cases": cases,
        "scope": "nonglobal artificial-pin regression; no actual-loaded KKT or Level I assertion",
    }, indent=2))


if __name__ == "__main__":
    main()
