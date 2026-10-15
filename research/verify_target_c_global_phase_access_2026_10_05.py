#!/usr/bin/env python3
"""Exact finite contracts for global exceptional-face phase access.

Actual rational unit sources verify internal train columns, pinned equilibrium,
outer angular determination and all face cuts. Abstract double-tree multigraphs
exercise deep distance layers. Pins are boundary points, not actual diameter
endpoints. Neither packet class certifies global optimality, Type II, uniform
integrability, Groemer compactness or asymptotic phase depletion.
"""
from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations

from verify_target_c_global_face_return_quotas_2026_10_04 import (
    adjacency, cross, edge, elimination, face_walks, sub,
)


def rank(rows, columns):
    return len(elimination(rows, columns)[1])


def actual_packet(modules, t, *, return_data=False):
    a, b = 2*t/(1+t*t), (1-t*t)/(1+t*t)
    positions = {
        3*j+i: (F(i)+(-a if i == 0 else a) * (j % 2), j*b)
        for j in range(2*modules+1) for i in range(3)
    }
    vertices = set(positions)
    contacts, checks = set(), 0
    for x, y in combinations(sorted(vertices), 2):
        dx, dy = sub(positions[y], positions[x])
        distance2 = dx*dx+dy*dy
        assert distance2 >= 1, (modules, t, x, y, distance2)
        if distance2 == 1:
            contacts.add(edge(x, y))
        checks += 1
    expected = {
        edge(3*j+i, 3*j+i+1)
        for j in range(2*modules+1) for i in range(2)
        if not (j % 2 and i == 0)
    } | {
        edge(3*j+i, 3*(j+1)+i)
        for j in range(2*modules) for i in range(3)
    }
    assert contacts == expected and len(contacts) == 9*modules+2
    adj = adjacency(vertices, contacts)
    assert not any(adj[x] & adj[y] for x, y in contacts)

    walks = face_walks(vertices, contacts, positions)
    outer = next(w for w, area2 in walks if area2 < 0)
    bounded = [w for w, area2 in walks if area2 > 0]
    faces = [w for w in bounded if len(w) != 4]
    assert len(faces) == modules and all(len(w) == 6 for w in faces)
    assert sum(len(w) == 4 for w in bounded) == 2*modules
    for w in faces:
        assert all(cross(sub(positions[w[(i+1)%6]], positions[w[i]]),
                         sub(positions[w[(i+2)%6]], positions[w[(i+1)%6]])) > 0
                   for i in range(6))

    # All pins lie on the convex hull boundary. Some are collinear, and this
    # is deliberately not a certificate of actual diameter loading.
    pins = {3*j+i for j in (0, 2*modules) for i in range(3)} | {
        3*j+i for j in range(1, 2*modules, 2) for i in (0, 2)
    }
    free = vertices-pins
    weights = {}
    for x, y in contacts:
        jx, ix = divmod(x, 3)
        jy, iy = divmod(y, 3)
        if jx != jy:
            weights[x, y] = F(2) if ix == 0 else F(1)
        elif jx in (0, 2*modules):
            weights[x, y] = F(1)
        else:
            weights[x, y] = 4*a if ix == 0 else 2*a
    assert all(w > 0 for w in weights.values())
    for v in free:
        result = [F(0), F(0)]
        for w in adj[v]:
            r = sub(positions[w], positions[v])
            for c in range(2):
                result[c] += weights[edge(v, w)]*r[c]
        assert result == [0, 0], (modules, v, result)

    parent = {e: e for e in contacts}

    def root(e):
        while parent[e] != e:
            e = parent[e]
        return e

    def join(e, f):
        x, y = root(e), root(f)
        parent[max(x, y)] = min(x, y)

    for w in bounded:
        if len(w) == 4:
            es = [edge(w[i], w[(i+1)%4]) for i in range(4)]
            join(es[0], es[2])
            join(es[1], es[3])
    trains = sorted({root(e) for e in contacts})
    index = {tr: i for i, tr in enumerate(trains)}
    outer_edges = {edge(outer[i], outer[(i+1)%len(outer)]) for i in range(len(outer))}
    outer_trains = {root(e) for e in outer_edges}
    endpoints = {tr: [] for tr in trains}
    closure = [[F(0)]*len(trains) for _ in range(2*modules)]
    for face, w in enumerate(faces):
        for i in range(6):
            x, y = w[i], w[(i+1)%6]
            tr = root(edge(x, y))
            r = sub(positions[y], positions[x])
            endpoints[tr].append((face, r))
            closure[2*face][index[tr]] -= r[1]
            closure[2*face+1][index[tr]] += r[0]
    ff = [tr for tr in trains if len(endpoints[tr]) == 2]
    assert len(trains) == 5*modules+2
    assert len(ff) == modules-1
    assert all(tr not in outer_trains for tr in ff)
    assert all(len(endpoints[tr]) <= 2 for tr in trains)
    assert all(tr in outer_trains for tr in trains if tr not in ff)
    for tr in ff:
        (f, w), (g, z) = endpoints[tr]
        assert f != g and w == (-z[0], -z[1])
    assert rank([[row[index[tr]] for tr in ff] for row in closure], len(ff)) == len(ff)
    assert rank(closure, len(trains)) == 2*modules

    n = len(vertices)
    rows = []
    for x, y in sorted(contacts):
        r = sub(positions[y], positions[x])
        row = [F(0)]*(2*n)
        for v, sign in ((x, -1), (y, 1)):
            row[2*v], row[2*v+1] = sign*r[0], sign*r[1]
        rows.append(row)
    assert rank(rows, 2*n) == len(contacts)
    free_columns = [2*v+c for v in sorted(free) for c in range(2)]
    assert rank([[row[c] for c in free_columns] for row in rows], len(free_columns)) == len(free_columns)
    angular = []
    for tr in sorted(outer_trains):
        x, y = next(e for e in sorted(outer_edges) if root(e) == tr)
        dx, dy = sub(positions[y], positions[x])
        row = [F(0)]*(2*n)
        for v, sign in ((x, -1), (y, 1)):
            row[2*v], row[2*v+1] = -sign*dy, sign*dx
        angular.append(row)
    assert rank(rows+angular, 2*n) == 2*n-2

    subsets = 0
    for mask in range(1, 1 << modules):
        selected = {f for f in range(modules) if mask >> f & 1}
        internal = sum(all(f in selected for f, _ in endpoints[tr]) for tr in ff)
        boundary = sum(sum(f in selected for f, _ in endpoints[tr]) == 1 for tr in trains)
        assert internal <= 2*len(selected)-2
        assert boundary == 6*len(selected)-2*internal
        assert boundary >= 2*len(selected)+4
        subsets += 1
    if return_data:
        return {"positions": positions, "contacts": contacts, "trains": trains,
                "roots": {e: root(e) for e in contacts}, "pins": pins,
                "weights": weights,
                "checks": checks, "subsets": subsets}
    return checks, subsets


def tree_packet(branching, height, exhaustive=False):
    # Two parallel copies of one tree form a union of two forests. The
    # abstract face valence is raised to five by outside terminal stubs.
    # This is not asserted to embed as an actual source train graph.
    levels, parents = [[0]], {}
    for _ in range(height):
        level = []
        for v in levels[-1]:
            for _ in range(branching):
                child = len(parents)+1
                parents[child] = v
                level.append(child)
        levels.append(level)
    size = len(parents)+1
    forest = [(v, p) for v, p in parents.items()]
    degree = Counter(v for e in forest for v in e)
    internal = forest+forest
    outside = {v: max(0, 5-2*degree[v]) for v in range(size)}
    valence = {v: 2*degree[v]+outside[v] for v in range(size)}
    adj = {v: set() for v in range(size)}
    for v, w in forest:
        adj[v].add(w)
        adj[w].add(v)
    distance = {v: 1 for v in range(size) if outside[v]}
    queue = deque(distance)
    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if w not in distance:
                distance[w] = distance[v]+1
                queue.append(w)
    assert len(distance) == size

    def check(selected):
        e = sum(v in selected and w in selected for v, w in internal)
        cut = sum((v in selected) != (w in selected) for v, w in internal)
        cut += sum(outside[v] for v in selected)
        q = sum(valence[v]-4 for v in selected)
        assert e <= 2*len(selected)-2
        assert cut == sum(valence[v] for v in selected)-2*e
        assert cut >= q+4 >= len(selected)+4
        return cut

    count = 0
    if exhaustive:
        for mask in range(1, 1 << size):
            check({v for v in range(size) if mask >> v & 1})
            count += 1
    layer_cuts, layer_mass = 0, 0
    used_edges = set()
    for r in range(2, max(distance.values())+1):
        selected = {v for v in range(size) if distance[v] >= r}
        cut = check(selected)
        cut_edges = {i for i, (v, w) in enumerate(internal) if (v in selected) != (w in selected)}
        assert not used_edges & cut_edges
        assert len(cut_edges) == cut
        used_edges |= cut_edges
        layer_cuts += cut
        layer_mass += len(selected)
        assert len(selected)*(r-1) <= 2*size-2
        count += 1
    assert layer_mass <= layer_cuts <= len(internal) == 2*size-2
    return count, max(distance.values()), size


if __name__ == "__main__":
    sources = [actual_packet(n, t) for n in (1, 2, 3, 5, 8)
               for t in (F(1, 50), F(1, 40))]
    trees = [tree_packet(b, h, exhaustive=(b, h) in ((2, 2), (3, 2)))
             for b, h in ((2, 2), (3, 2), (2, 5), (2, 8), (3, 5), (3, 6))]
    print(f"PASS: {sum(p[0] for p in sources)} rational unit-pair checks in {len(sources)} actual sources")
    print("PASS: positive boundary-pinned equilibrium and full pinned/contact ranks")
    print("PASS: outer angular determination and independent opposite-sign internal train columns")
    print(f"PASS: {sum(p[1] for p in sources)} exact actual-source face-subset cuts")
    print(f"PASS: {sum(p[0] for p in trees)} abstract sparse-multigraph cuts/layers; max depth {max(p[1] for p in trees)}")
    print("SCOPE: no global optimality, actual diameter loading, UI tails or asymptotic closure certified")
