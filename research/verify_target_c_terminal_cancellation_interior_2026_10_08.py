#!/usr/bin/env python3
"""Exact finite facial-terminal checks for an unreviewed Type-II candidate.

Includes bounded nonquadrilateral faces, complete rhombus tracks, singleton
contact edges, and repeated outer-face bridge occurrences. Fixtures are
nonglobal; no source stress, circle limit, or asymptotic claim is certified.
"""

from collections import Counter, defaultdict
from itertools import combinations
import json

from verify_target_b_terminal_cancellation_2026_10_08 import (
    DSU, F, add, edge, hull, norm2, physical, selections, sub,
)


DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def faces(points, contacts):
    neighbors = defaultdict(list)
    for a, b in contacts:
        neighbors[a].append(b)
        neighbors[b].append(a)
    for p, adjacent in neighbors.items():
        adjacent.sort(key=lambda q: DIRECTIONS.index(sub(q, p)))
    unseen = {(a, b) for e in contacts for a, b in (e, tuple(reversed(e)))}
    walks = []
    while unseen:
        start = min(unseen)
        dart, walk = start, []
        while not walk or dart != start:
            assert dart in unseen
            unseen.remove(dart)
            walk.append(dart)
            a, b = dart
            adjacent = neighbors[b]
            c = adjacent[(adjacent.index(a) - 1) % len(adjacent)]
            dart = b, c
            assert len(walk) <= 2 * len(contacts)
        walks.append(walk)
    assert len(points) - len(contacts) + len(walks) == 2
    return walks


def signed_area2(walk):
    return sum(a[0] * b[1] - a[1] * b[0] for a, b in walk)


def fixture(points, separate_faces=False):
    contacts = set()
    pairs = 0
    for a, b in combinations(sorted(points), 2):
        d2 = norm2(sub(physical(a), physical(b)))
        assert d2 >= 1
        pairs += 1
        if d2 == 1:
            contacts.add(edge(a, b))
            assert sub(b, a) in DIRECTIONS or sub(a, b) in DIRECTIONS
    walks = faces(points, contacts)
    outer_faces = [w for w in walks if signed_area2(w) < 0]
    assert len(outer_faces) == 1
    outer_face = outer_faces[0]
    bounded = [w for w in walks if w is not outer_face]
    assert all(signed_area2(w) > 0 for w in bounded)
    quadrilaterals = [w for w in bounded if len(w) == 4]
    exceptional = [w for w in bounded if len(w) != 4]
    assert all(len(w) >= 5 for w in exceptional)

    dsu = DSU(contacts)
    quad_incidence = Counter()
    for walk in quadrilaterals:
        edges = [edge(a, b) for a, b in walk]
        dsu.join(edges[0], edges[2])
        dsu.join(edges[1], edges[3])
        for e in edges:
            quad_incidence[e] += 1
    tracks = sorted({dsu.root(e) for e in contacts})
    degrees = {t: 0 for t in tracks}
    crossings = set()
    for walk in quadrilaterals:
        ta, tb = (dsu.root(edge(a, b)) for a, b in walk[:2])
        assert ta != tb
        pair = tuple(sorted((ta, tb)))
        assert pair not in crossings
        crossings.add(pair)
        degrees[ta] += 1
        degrees[tb] += 1

    outer = [(b, a) for a, b in reversed(outer_face)]
    corner_set = set(hull(points))
    positions = [i for i, (a, _) in enumerate(outer) if a in corner_set]
    assert len(positions) == len(corner_set), "Fixtures use unique hull occurrences"
    shift = positions[0]
    outer = outer[shift:] + outer[:shift]
    chains, current = [], []
    for a, b in outer:
        if a in corner_set and current:
            chains.append(current)
            current = []
        current.append((a, b))
    chains.append(current)
    q = len(chains)
    assert q == len(corner_set)
    ghost = q
    terminals = defaultdict(list)
    for i, chain in enumerate(chains):
        for a, b in chain:
            midpoint = tuple((x + y) / 2 for x, y in zip(physical(a), physical(b)))
            terminals[dsu.root(edge(a, b))].append(
                (i, sub(physical(b), physical(a)), midpoint))
    for face_index, walk in enumerate(exceptional):
        for a, b in walk:
            # Reverse the exceptional facial orientation: the complex is on the left.
            midpoint = tuple((x + y) / 2 for x, y in zip(physical(a), physical(b)))
            terminals[dsu.root(edge(a, b))].append(
                (ghost + face_index if separate_faces else ghost,
                 sub(physical(a), physical(b)), midpoint))

    for t in tracks:
        ends = terminals[t]
        assert len(ends) == 2
        assert add(ends[0][1], ends[1][1]) == (0, 0)
        assert norm2(sub(ends[0][2], ends[1][2])) <= degrees[t] ** 2
    boundary_budget = len(outer) + sum(len(w) for w in exceptional)
    assert boundary_budget == 2 * len(tracks)
    singleton_count = sum(quad_incidence[e] == 0 for e in contacts)
    assert singleton_count == sum(degrees[t] == 0 for t in tracks)

    chords = []
    for chain in chains:
        chord = sub(physical(chain[-1][1]), physical(chain[0][0]))
        assert norm2(chord) >= 1
        chords.append(chord)
    outer_counts = Counter(edge(a, b) for a, b in outer)
    bridge_occurrences = sum(v for v in outer_counts.values() if v == 2)
    return tracks, chains, chords, terminals, {
        "pairs": pairs,
        "terminals": len(tracks),
        "interior_occurrences": sum(len(w) for w in exceptional),
        "singleton_trains": singleton_count,
        "bridge_occurrences": bridge_occurrences,
    }, [len(w) for w in exceptional]


def check_auxiliary(tracks, chains, chords, terminals, nonatomic):
    ghost = len(chains)
    adjacency = [set() for _ in range(ghost + 1)]
    for t in nonatomic:
        a, b = (e[0] for e in terminals[t])
        adjacency[a].add(b)
        adjacency[b].add(a)
    unseen = set(range(ghost + 1))
    components = []
    while unseen:
        pending, component = [min(unseen)], set()
        while pending:
            v = pending.pop()
            if v in component:
                continue
            component.add(v)
            pending.extend(adjacency[v] - component)
        unseen -= component
        components.append(component)
    assert len(nonatomic) >= ghost + 1 - len(components)
    assert sum(ghost in c for c in components) == 1
    checked = 0
    atomic = set(tracks) - nonatomic
    for component in components:
        if ghost in component:
            continue
        lhs, rhs = (F(0), F(0)), (F(0), F(0))
        for i in component:
            lhs = add(lhs, chords[i])
        for t in nonatomic:
            included = [e for e in terminals[t] if e[0] in component]
            assert len(included) in (0, 2)
            if included:
                assert add(included[0][1], included[1][1]) == (0, 0)
        for t in atomic:
            for i, vector, _ in terminals[t]:
                if i in component:
                    rhs = add(rhs, vector)
        assert lhs == rhs
        checked += 1
    return checked


def check_separate_faces(tracks, chains, chords, terminals, nonatomic, face_degrees):
    """Check the finite refinement with every exceptional face kept separate."""
    q, f = len(chains), len(face_degrees)
    adjacency = [set() for _ in range(q + f)]
    for t in nonatomic:
        a, b = (e[0] for e in terminals[t])
        adjacency[a].add(b)
        adjacency[b].add(a)
    unseen = set(range(q + f))
    components = []
    while unseen:
        pending, component = [min(unseen)], set()
        while pending:
            v = pending.pop()
            if v in component:
                continue
            component.add(v)
            pending.extend(adjacency[v] - component)
        unseen -= component
        components.append(component)
    boundary_components = [c for c in components if any(v < q for v in c)]
    boundary_vertices = set().union(*boundary_components)
    face_boundary = {v - q for v in boundary_vertices if v >= q}
    fb, cb = len(face_boundary), len(boundary_components)
    ni = sum(terminals[t][0][0] not in boundary_vertices for t in nonatomic)
    nb = len(nonatomic) - ni
    assert nb >= q + fb - cb
    atomic = set(tracks) - nonatomic
    atomic_boundary_ends = sum(e[0] in boundary_vertices for t in atomic for e in terminals[t])
    boundary_occurrences = sum(map(len, chains)) + sum(face_degrees[i] for i in face_boundary)
    assert atomic_boundary_ends == boundary_occurrences - 2 * nb

    # This counting k need not be a source KKT defect in a nonglobal fixture.
    # The exact handshake makes the algebra identical to the source ledger.
    k = q - len(tracks) + 2 * f
    qi = sum(d - 4 for i, d in enumerate(face_degrees) if i not in face_boundary)
    assert atomic_boundary_ends <= 2 * fb - qi - 2 * k + 2 * cb
    assert 3 * fb >= f + 2 * k - 2 * cb
    assert len(atomic) + ni <= 2 * f - fb - k + cb
    assert 3 * (len(atomic) + ni) <= 5 * (f - k + cb)

    for component in components:
        lhs, rhs = (F(0), F(0)), (F(0), F(0))
        for i in component:
            if i < q:
                lhs = add(lhs, chords[i])
        for t in nonatomic:
            included = [e for e in terminals[t] if e[0] in component]
            assert len(included) in (0, 2)
        for t in atomic:
            for i, vector, _ in terminals[t]:
                if i in component:
                    rhs = add(rhs, vector)
        assert lhs == rhs
    return len(components)


def square_points(m):
    return {(i, j) for i in range(m + 1) for j in range(m + 1)}


def main():
    patches = [square_points(2), square_points(3)]
    for m in (4, 6):
        patches.append(square_points(m) - {(m // 2, m // 2)})
    patches.append(square_points(8) - {(2, 2), (6, 6)})
    patches.append(square_points(6) - {(3, j) for j in (2, 3, 4)})
    patches.append(square_points(4) | {(5, 2), (6, 2)})
    patches.append((square_points(6) - {(3, 3)}) | {(7, 3), (8, 3)})
    totals = Counter()
    graph_count = components = separate_graphs = separate_components = 0
    for points in patches:
        tracks, chains, chords, terminals, stats, _ = fixture(points)
        totals.update(stats)
        for nonatomic in selections(tracks):
            components += check_auxiliary(tracks, chains, chords, terminals, nonatomic)
            graph_count += 1
        tracks, chains, chords, terminals, _, face_degrees = fixture(points, separate_faces=True)
        for nonatomic in selections(tracks):
            separate_components += check_separate_faces(
                tracks, chains, chords, terminals, nonatomic, face_degrees)
            separate_graphs += 1

    # A train joining outer and interior recipients has just one outer vector.
    # Dropping its interior recipient would invalidate paired cancellation.
    tracks, chains, chords, terminals, _, _ = fixture(square_points(4) - {(2, 2)})
    ghost = len(chains)
    mixed = [t for t in tracks if sum(e[0] == ghost for e in terminals[t]) == 1]
    assert mixed
    for t in mixed:
        outer_vector = next(e[1] for e in terminals[t] if e[0] != ghost)
        assert outer_vector != (0, 0)
    print(json.dumps({
        "status": "PASS",
        "arithmetic": "Fraction",
        "nonglobal_contact_fixtures": len(patches),
        "all_source_lower_pair_checks": totals["pairs"],
        "physical_terminal_pair_checks": totals["terminals"],
        "interior_terminal_occurrences": totals["interior_occurrences"],
        "singleton_trains": totals["singleton_trains"],
        "repeated_outer_bridge_occurrences": totals["bridge_occurrences"],
        "auxiliary_graph_selections": graph_count,
        "components_checked_outside_interior_vertex": components,
        "separate_face_graph_selections": separate_graphs,
        "separate_face_component_cancellation_checks": separate_components,
        "scope": "finite facial identities only; no Type-II or optimality certificate",
    }, indent=2))


if __name__ == "__main__":
    main()
