#!/usr/bin/env python3
"""Exact finite cut ledgers and contact-walk lifts for a candidate train bank.

Fixtures are nonglobal. Reciprocal sparsity is checked as an explicit finite
antecedent; failed antecedents are counted, never treated as canonical sources.
Fixture hull corners are bookkeeping roots, not certified diameter-loaded points.
"""

from collections import Counter, defaultdict, deque
from itertools import combinations
import json

from verify_target_c_terminal_cancellation_interior_2026_10_08 import (
    DSU, F, add, edge, faces, fixture, norm2, physical, selections,
    signed_area2, square_points, sub,
)


def components(vertices, edges):
    adjacency = {v: set() for v in vertices}
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    unseen, result = set(vertices), []
    while unseen:
        pending, comp = [min(unseen)], set()
        while pending:
            v = pending.pop()
            if v in comp:
                continue
            comp.add(v)
            pending.extend(adjacency[v] - comp)
        unseen -= comp
        result.append(comp)
    return result


def index_of(p):
    j = 13 * p[1] / 12
    i = p[0] - 5 * j / 13
    assert i.denominator == j.denominator == 1
    return int(i), int(j)


def minus_end(terminal):
    _, vector, midpoint = terminal
    if vector < (F(0), F(0)):
        vector = tuple(-x for x in vector)
    return index_of(tuple(m - v / 2 for m, v in zip(midpoint, vector)))


def physical_data(points, terminals):
    contacts = {
        edge(a, b) for a, b in combinations(sorted(points), 2)
        if norm2(sub(physical(a), physical(b))) == 1
    }
    walks = faces(points, contacts)
    quadrilaterals = [w for w in walks if signed_area2(w) > 0 and len(w) == 4]
    exceptional = [w for w in walks if signed_area2(w) > 0 and len(w) != 4]
    outer = next(w for w in walks if signed_area2(w) < 0)
    dsu = DSU(contacts)
    for w in quadrilaterals:
        es = [edge(a, b) for a, b in w]
        dsu.join(es[0], es[2])
        dsu.join(es[1], es[3])
    rails = defaultdict(set)
    degree = Counter()
    crossings = set()
    for w in quadrilaterals:
        es = [edge(a, b) for a, b in w]
        crossing = tuple(sorted((dsu.root(es[0]), dsu.root(es[1]))))
        assert crossing not in crossings
        crossings.add(crossing)
        for parity in (0, 1):
            t = dsu.root(es[parity])
            # The canonical sign chooses the same unit-edge endpoint on both
            # opposite sides; the matched endpoints are joined by a contact.
            ends = []
            for e in (es[parity], es[parity + 2]):
                ends.append(min(e, key=physical))
            rail = edge(*ends)
            assert rail in contacts
            rails[t].add(rail)
            degree[t] += 1
    for t, terminal_pair in terminals.items():
        ends = [minus_end(e) for e in terminal_pair]
        assert len(rails[t]) == degree[t]
        adjacency = defaultdict(set)
        for a, b in rails[t]:
            adjacency[a].add(b)
            adjacency[b].add(a)
        distances, todo = {ends[0]: 0}, deque([ends[0]])
        while todo:
            a = todo.popleft()
            for b in adjacency[a]:
                if b not in distances:
                    distances[b] = distances[a] + 1
                    todo.append(b)
        assert distances[ends[1]] == degree[t]
        unit = terminals[t][0][1]
        delta = sub(physical(ends[1]), physical(ends[0]))
        determinant = abs(unit[0] * delta[1] - unit[1] * delta[0])
        # These exact oblique-grid rails have normal increment 12/13 per face.
        assert determinant == F(12, 13) * degree[t]
    crossing_neighbors = defaultdict(set)
    for a, b in crossings:
        crossing_neighbors[a].add(b)
        crossing_neighbors[b].add(a)
    for a, b in crossings:
        assert not (crossing_neighbors[a] & crossing_neighbors[b])
    return contacts, outer, exceptional, rails, degree, crossings


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


def check_long_terminal_separator(atomic, terminals, data, loaded):
    contacts, _, _, rails, degree, _ = data
    if not atomic:
        return True, 0
    roots = {minus_end(terminals[t][0]) for t in atomic}
    separator, paths, vertices = contact_separator(contacts, roots, loaded)
    k, length = len(separator), min(degree[t] for t in atomic)
    remaining_contacts = [e for e in contacts if not (set(e) & separator)]
    remaining_components = components(set(vertices) - separator, remaining_contacts)
    unloaded_components = [c for c in remaining_components if c & (roots - separator)]
    assert all(not (c & (loaded - separator)) for c in unloaded_components)
    unloaded = set().union(*unloaded_components) if unloaded_components else set()

    rail_vertices = {}
    membership = defaultdict(set)
    for t in atomic:
        vs = {minus_end(e) for e in terminals[t]}
        vs.update(v for e in rails[t] for v in e)
        assert len(vs) == degree[t] + 1
        rail_vertices[t] = vs
        for v in vs:
            membership[v].add(t)
    assert all(len(ts) <= 5 for ts in membership.values())
    intercepted = {t for t in atomic if rail_vertices[t] & separator}
    assert len(intercepted) <= 5 * k
    retained = atomic - intercepted
    assert all(rail_vertices[t] <= unloaded for t in retained)
    assert len(retained) * (length + 1) <= 5 * len(unloaded)

    pinned_count_antecedent = all(
        sum(bool(set(e) & c) for e in contacts) >= 2 * len(c) + 1
        for c in unloaded_components)
    if pinned_count_antecedent:
        # The analytic packing bound uses pi; pi>3 gives this outward
        # rational consequence without floating-point arithmetic.
        assert len(unloaded) <= F(16, 9) * k * k + F(8, 3) * k
        assert max(0, len(atomic) - 5 * k) * (length + 1) <= (
            F(80, 9) * k * k + F(40, 3) * k)
    return pinned_count_antecedent, len(paths)


def check_selection(tracks, chains, terminals, face_degrees, data, nonatomic):
    contacts, outer, exceptional, rails, degree, crossings = data
    q, f = len(chains), len(face_degrees)
    ends = {t: tuple(e[0] for e in terminals[t]) for t in tracks}
    cs = components(range(q + f), (ends[t] for t in nonatomic))
    boundary = set().union(*(c for c in cs if any(v < q for v in c)))
    interior = set(range(q, q + f)) - boundary
    fi = len(interior)
    qi = sum(face_degrees[v - q] - 4 for v in interior)
    internal = [t for t in tracks if all(v in interior for v in ends[t])]
    cut = [t for t in tracks if sum(v in interior for v in ends[t]) == 1]
    atomic = set(tracks) - nonatomic
    assert set(cut) <= atomic
    assert 4 * fi + qi == 2 * len(internal) + len(cut)
    induced = components(interior, (ends[t] for t in internal))
    sigma = sum(2 if len(c) == 1 else 3 for c in induced)
    reciprocal_antecedent = len(internal) <= 2 * fi - sigma
    boundary_ends = sum(v in boundary for t in atomic for v in ends[t])
    bank = {t for t in atomic if any(v in boundary for v in ends[t])}
    if reciprocal_antecedent:
        assert len(cut) >= qi + 2 * sigma
        assert boundary_ends >= len(cut)
        assert 3 * boundary_ends >= len(atomic)
        assert 3 * len(bank) >= len(atomic)
        retained_crossings = sum(a in atomic and b in atomic for a, b in crossings)
        assert len(atomic) ** 2 >= 4 * retained_crossings
        retained_floor = max(0, len(crossings) - sum(degree[t] for t in nonatomic))
        assert retained_crossings >= retained_floor
        assert 9 * len(bank) ** 2 >= 4 * retained_floor

    carrier = set()
    for t in nonatomic:
        carrier.update(rails[t])
    for v in boundary:
        if v >= q:
            carrier.update(edge(a, b) for a, b in exceptional[v - q])
    carrier.update(edge(a, b) for a, b in outer)
    assert carrier <= contacts
    length_budget = sum(degree[t] for t in nonatomic)
    length_budget += sum(face_degrees[v - q] for v in boundary if v >= q)
    length_budget += len(outer)
    assert len(carrier) <= length_budget
    assert length_budget <= sum(degree[t] for t in nonatomic) + 2 * len(tracks)
    adjacency = defaultdict(set)
    for a, b in carrier:
        adjacency[a].add(b)
        adjacency[b].add(a)
    roots = {chain[0][0] for chain in chains}
    parent, todo = {r: None for r in roots}, deque(sorted(roots))
    while todo:
        a = todo.popleft()
        for b in adjacency[a]:
            if b not in parent:
                parent[b] = a
                todo.append(b)
    return_checks = 0
    for t in bank:
        chosen = next(e for e in terminals[t] if e[0] in boundary)
        a = minus_end(chosen)
        assert a in parent
        visited = set()
        while parent[a] is not None:
            assert a not in visited
            visited.add(a)
            b = parent[a]
            assert edge(a, b) in contacts
            assert norm2(sub(physical(a), physical(b))) == 1
            a = b
            return_checks += 1
        assert a in roots
    return reciprocal_antecedent, len(bank), return_checks


def main():
    patches = [square_points(2), square_points(3)]
    for m in (4, 6):
        patches.append(square_points(m) - {(m // 2, m // 2)})
    patches.extend([
        square_points(8) - {(2, 2), (6, 6)},
        square_points(6) - {(3, j) for j in (2, 3, 4)},
        square_points(4) | {(5, 2), (6, 2)},
        (square_points(6) - {(3, 3)}) | {(7, 3), (8, 3)},
        square_points(8) - {(2, 2), (6, 2)},
        square_points(8) - {(2, 2), (6, 2), (2, 6), (6, 6)},
    ])
    counts = Counter()
    for points in patches:
        tracks, chains, _, terminals, stats, face_degrees = fixture(
            points, separate_faces=True)
        counts["source_lower_pairs"] += stats["pairs"]
        data = physical_data(points, terminals)
        counts["physical_train_rails"] += len(tracks)
        chosen = {frozenset(n) for n in selections(tracks)}
        degrees = data[4]
        for threshold in {0, 1} | {degrees[t] + 1 for t in tracks}:
            chosen.add(frozenset(t for t in tracks if degrees[t] < threshold))
        for nonatomic in sorted(chosen, key=lambda n: (len(n), tuple(sorted(n)))):
            valid, bank, returns = check_selection(
                tracks, chains, terminals, face_degrees, data, nonatomic)
            counts["selections"] += 1
            counts["reciprocal_antecedent_pass" if valid else
                   "reciprocal_antecedent_fail"] += 1
            counts["bank_end_contact_returns"] += bank
            counts["return_walk_unit_steps"] += returns
        loaded = {chain[0][0] for chain in chains}
        for threshold in sorted({1} | {degrees[t] for t in tracks if degrees[t]}):
            atomic = {t for t in tracks if degrees[t] >= threshold}
            valid, path_count = check_long_terminal_separator(
                atomic, terminals, data, loaded)
            counts["long_terminal_flow_checks"] += 1
            counts["pinned_count_antecedent_pass" if valid else
                   "pinned_count_antecedent_fail"] += 1
            counts["vertex_disjoint_full_contact_returns"] += path_count
    assert counts["reciprocal_antecedent_fail"] > 0
    print(json.dumps({
        "status": "PASS",
        "arithmetic": "Fraction",
        "nonglobal_fixtures": len(patches),
        **counts,
        "scope": "finite conditional cut/packing bounds and physical contact flows; "
                 "fixture hull roots are not certified diameter-loaded; "
                 "no KKT, optimality, asymptotic or Level I certificate",
    }, indent=2))


if __name__ == "__main__":
    main()
