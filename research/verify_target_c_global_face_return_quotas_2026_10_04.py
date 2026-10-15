#!/usr/bin/env python3
"""Exact finite checks for global face-return quotas.

Uses rational Tutte frameworks with pinned contact rank and positive unloaded
equilibrium. Physical bars have arbitrary lengths: unit separation, actual
diameter loading, source optimality, and the canonical source's existence are
NOT certified. Those packets check the finite pinned/plane argument. Additional
integer checks certify the bookkeeping, bridge correction, and tail coefficient.
No external packages are required.
"""

from collections import defaultdict, deque
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import combinations


def elimination(matrix, columns):
    rows = [list(map(F, row)) for row in matrix]
    pivot_rows = []
    for col in range(columns):
        at = next((i for i in range(len(pivot_rows), len(rows)) if rows[i][col]), None)
        if at is None:
            continue
        k = len(pivot_rows)
        rows[k], rows[at] = rows[at], rows[k]
        divisor = rows[k][col]
        rows[k] = [v / divisor for v in rows[k]]
        for i in range(len(rows)):
            if i != k and rows[i][col]:
                scale = rows[i][col]
                rows[i] = [a - scale * b for a, b in zip(rows[i], rows[k])]
        pivot_rows.append(col)
    return rows, pivot_rows


def edge(a, b):
    return tuple(sorted((a, b)))


def adjacency(vertices, edges):
    adj = {v: set() for v in vertices}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def vector_order(a, b):
    ha = a[1] > 0 or (a[1] == 0 and a[0] >= 0)
    hb = b[1] > 0 or (b[1] == 0 and b[0] >= 0)
    if ha != hb:
        return -1 if ha else 1
    c = cross(a, b)
    return -1 if c > 0 else 1 if c < 0 else 0


def face_walks(vertices, edges, positions):
    adj = adjacency(vertices, edges)
    rotations = {}
    for v, neighbors in adj.items():
        compare = lambda x, y: vector_order(sub(positions[x], positions[v]), sub(positions[y], positions[v]))
        rotations[v] = sorted(neighbors, key=cmp_to_key(compare))
    seen = set()
    walks = []
    for a, b in sorted((a, b) for x, y in edges for a, b in ((x, y), (y, x))):
        if (a, b) in seen:
            continue
        start = a, b
        walk = []
        while (a, b) not in seen:
            seen.add((a, b))
            walk.append(a)
            around = rotations[b]
            a, b = b, around[(around.index(a) - 1) % len(around)]
        assert (a, b) == start
        area2 = sum(cross(positions[x], positions[y]) for x, y in zip(walk, walk[1:] + walk[:1]))
        walks.append((walk, area2))
    return walks


def components(vertices, edges):
    adj = adjacency(vertices, edges)
    unseen = set(vertices)
    out = []
    while unseen:
        root = min(unseen)
        reached = {root}
        queue = [root]
        for v in queue:
            for w in adj[v] - reached:
                reached.add(w)
                queue.append(w)
        unseen -= reached
        out.append(reached)
    return out


def integer_flow(arcs, source, sink):
    capacity = defaultdict(int)
    adj = defaultdict(set)
    for a, b, amount in arcs:
        capacity[a, b] += amount
        adj[a].add(b)
        adj[b].add(a)
    residual = dict(capacity)
    value = 0
    while True:
        parents = {source: None}
        queue = deque([source])
        while queue and sink not in parents:
            a = queue.popleft()
            for b in sorted(adj[a], key=repr):
                if b not in parents and residual.get((a, b), 0) > 0:
                    parents[b] = a
                    queue.append(b)
        if sink not in parents:
            return value, set(parents)
        amount = 10**9
        b = sink
        while b != source:
            a = parents[b]
            amount = min(amount, residual[a, b])
            b = a
        b = sink
        while b != source:
            a = parents[b]
            residual[a, b] -= amount
            residual[b, a] = residual.get((b, a), 0) + amount
            b = a
        value += amount


def split_arcs(vertices, contacts, pins, big):
    arcs = [(('i', v), ('o', v), 1) for v in vertices]
    for a, b in contacts:
        arcs.extend(((('o', a), ('i', b), big), (('o', b), ('i', a), big)))
    arcs.extend((('o', v), 'sink', big) for v in pins)
    return arcs


def separator(vertices, contacts, pins, starts):
    big = len(vertices) + 1
    arcs = split_arcs(vertices, contacts, pins, big)
    arcs.extend(('source', ('i', v), big) for v in starts)
    value, reachable = integer_flow(arcs, 'source', 'sink')
    cut = {v for v in vertices if ('i', v) in reachable and ('o', v) not in reachable}
    assert len(cut) == value
    return cut


def grid_packet(side, removed, corner_chords):
    vertices = {(i, j) for i in range(side) for j in range(side)}
    contacts = {edge(v, w) for v in vertices for w in ((v[0] + 1, v[1]), (v[0], v[1] + 1)) if w in vertices}
    contacts -= {edge(*pair) for pair in removed}
    boundary = ([(i, 0) for i in range(side)] + [(side - 1, j) for j in range(1, side)]
                + [(i, side - 1) for i in range(side - 2, -1, -1)] + [(0, j) for j in range(side - 2, 0, -1)])
    pins = set(boundary)
    positions = {}
    count = len(boundary)
    for v, index in zip(boundary[:-1], range(count - 1)):
        t = F(index - (count - 2) // 2)
        positions[v] = (F(1 - t*t, 1 + t*t), F(2*t, 1 + t*t))
    positions[boundary[-1]] = F(-1), F(0)
    interior = sorted(vertices - pins)
    lookup = {v: i for i, v in enumerate(interior)}
    adj = adjacency(vertices, contacts)
    system = []
    for v in interior:
        row = [F(0)] * (len(interior) + 2)
        row[lookup[v]] = len(adj[v])
        for w in adj[v]:
            if w in lookup:
                row[lookup[w]] -= 1
            else:
                row[-2] += positions[w][0]
                row[-1] += positions[w][1]
        system.append(row)
    solved, pivots = elimination(system, len(interior))
    assert len(pivots) == len(interior)
    for v, row in zip(interior, solved):
        positions[v] = row[-2], row[-1]
    assert len(set(positions.values())) == len(vertices)
    for v in interior:
        assert tuple(sum(positions[w][i] - positions[v][i] for w in adj[v]) for i in range(2)) == (0, 0)
    rigidity = []
    for a, b in contacts:
        row = [F(0)] * (2 * len(interior))
        for v, w in ((a, b), (b, a)):
            if v in lookup:
                row[2*lookup[v]:2*lookup[v]+2] = sub(positions[v], positions[w])
        if any(row):
            rigidity.append(row)
    assert len(elimination(rigidity, 2 * len(interior))[1]) == 2 * len(interior), 'pinned-rank prerequisite fails'
    assert all(not (adj[a] & adj[b]) for a, b in contacts), 'physical triangle'
    aux = set()
    if corner_chords:
        for v in ((0, 0), (side - 1, 0), (side - 1, side - 1), (0, side - 1)):
            neighbors = sorted(adj[v])
            assert len(neighbors) == 2 and set(neighbors) <= pins
            aux.add(edge(*neighbors))
    augmented = contacts | aux
    for (a, b), (c, d) in combinations(augmented, 2):
        if len({a, b, c, d}) < 4:
            continue
        orient = lambda x, y, z: cross(sub(positions[y], positions[x]), sub(positions[z], positions[x]))
        assert not (orient(a, b, c)*orient(a, b, d) < 0 and orient(c, d, a)*orient(c, d, b) < 0), 'crossing edges'
    walks = face_walks(vertices, augmented, positions)
    faces = [walk for walk, area in walks if area > 0 and len(walk) >= 5]
    assert faces
    assert all(len(set(walk)) == len(walk) for walk in faces)
    return vertices, contacts, aux, pins, positions, faces, walks


def packet_checks():
    packets = [
        (5, [((2, 2), (3, 2))]),
        (6, [((2, 2), (3, 2)), ((2, 3), (3, 3))]),
        (6, [((2, 2), (3, 2)), ((3, 3), (4, 3))]),
    ]
    checked = 0
    quotas = 0
    triangle_packets = 0
    for side, removed in packets:
        for chord_flag in (False, True):
            vertices, contacts, aux, pins, positions, faces, all_walks = grid_packet(side, removed, chord_flag)
            if chord_flag:
                assert sum(area > 0 and len(walk) == 3 for walk, area in all_walks) == 2 * len(aux)
                triangle_packets += 1
            for mask in range(1, 1 << len(faces)):
                selected = [face for i, face in enumerate(faces) if mask & (1 << i)]
                starts = set().union(*map(set, selected))
                defect = sum(len(face) - 4 for face in selected)
                cut = separator(vertices, contacts, pins, starts)
                left = vertices - cut
                leftover_edges = {e for e in contacts if set(e) <= left}
                unpinned = [comp for comp in components(left, leftover_edges) if comp & (starts - cut)]
                assert all(not (comp & pins) for comp in unpinned)
                bulk = set().union(*unpinned) if unpinned else set()
                retained = bulk | cut
                physical_k = {e for e in contacts if set(e) <= retained}
                aux_k = {e for e in aux if set(e) <= retained}
                k_walks = face_walks(retained, physical_k | aux_k, positions)
                outer = [walk for walk, area in k_walks if area <= 0]
                assert cut <= set().union(*map(set, outer))
                b = sum(map(len, outer))
                out_aux = sum(edge(x, y) in aux_k for walk in outer for x, y in zip(walk, walk[1:] + walk[:1]))
                e_s = sum(set(e) <= cut for e in physical_k)
                f3 = sum(area > 0 and len(walk) == 3 for walk, area in k_walks)
                qpos = sum(len(walk) - 4 for walk, area in k_walks if area > 0 and len(walk) >= 5)
                c_k = len(components(retained, physical_k | aux_k))
                assert b >= 2*len(cut) - 2*e_s - out_aux
                assert f3 <= 2*len(aux_k) - out_aux
                assert b - f3 + qpos == 4*len(retained) - 2*len(physical_k | aux_k) - 4*c_k
                assert defect <= qpos <= 2*len(cut) - 2*len(unpinned) - 4*c_k
                if len(selected) == 1:
                    assert len(cut) >= (len(selected[0]) + 3)//2
                requests = [max(0, (len(face) - 4)//2 - len(set(face) & pins)) for face in selected]
                big = len(vertices) + sum(requests) + 1
                arcs = split_arcs(vertices, contacts, pins, big)
                for i, (face, request) in enumerate(zip(selected, requests)):
                    arcs.append(('source', ('f', i), request))
                    arcs.extend((('f', i), ('i', v), big) for v in set(face) - pins)
                assert integer_flow(arcs, 'source', 'sink')[0] == sum(requests)
                quotas += sum(requests)
                checked += 1
    return checked, quotas, triangle_packets


def bookkeeping_checks():
    cases = 0
    for k in range(1, 16):
        for cu in range(5):
            for ck in range(1, 5):
                for es in range(8):
                    for a in range(8):
                        for ao in range(2*a + 1):
                            b = max(0, 2*k - 2*es - ao)
                            f3 = 2*a - ao
                            upper = 4*k - 2*cu - 2*es - 2*a - 4*ck - b + f3
                            assert upper <= 2*k - 2*cu - 4*ck
                            cases += 1
    # A physical bridge has two outer occurrences. The false one-copy bound fails.
    assert 2 < 2*2 - 1
    for degree in range(6, 100):
        for loaded in range(3):
            request = max(0, (degree - 4)//2 - loaded)
            assert request >= F(degree - 4, 2) - F(1, 2) - loaded
    return cases


if __name__ == '__main__':
    ledger_count = bookkeeping_checks()
    face_count, quota_count, two_sided = packet_checks()
    print(f'PASS: {ledger_count} integer cancellation ledgers; {face_count} exact face-family/separator packets')
    print(f'PASS: {quota_count} simultaneous face demands; {two_sided} packets with two triangles per auxiliary chord')
    print('Scope: rational pinned frameworks with arbitrary bar lengths; not unit-separated global minimizers or Level I closure.')
