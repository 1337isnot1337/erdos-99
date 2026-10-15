#!/usr/bin/env python3
"""Exact finite checks for the unreviewed terminal-cancellation candidate.

Physical fixtures are nonglobal unit-rhombic disks in a rational oblique
lattice. Check all lower pairs, actual contact edges, complete train ends,
hull-chain components, paired-vector cancellation, and the graph edge bound.
This does not certify any asymptotic statement or global optimality.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
import json


U = (F(1), F(0))
V = (F(5, 13), F(12, 13))  # Acute angle strictly between 60 and 90 degrees.


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def norm2(a):
    return a[0] ** 2 + a[1] ** 2


def physical(p):
    return F(p[0]) + V[0] * p[1], V[1] * p[1]


def edge(a, b):
    return tuple(sorted((a, b)))


def cross(o, a, b):
    ax, ay = sub(a, o)
    bx, by = sub(b, o)
    return ax * by - ay * bx


def hull(points):
    pts = sorted(points)
    lower, upper = [], []
    for out, ordered in ((lower, pts), (upper, reversed(pts))):
        for p in ordered:
            while len(out) >= 2 and cross(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
    return lower[:-1] + upper[:-1]


class DSU:
    def __init__(self, items):
        self.parent = {x: x for x in items}

    def root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def join(self, x, y):
        a, b = self.root(x), self.root(y)
        if a != b:
            self.parent[max(a, b)] = min(a, b)


def fixture(cells):
    incidences = defaultdict(list)
    opposite_pairs, cell_crossings = [], []
    points = set()
    for i, j in sorted(cells):
        a, b, c, d = (i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)
        points.update((a, b, c, d))
        for x, y in ((a, b), (b, c), (c, d), (d, a)):
            incidences[edge(x, y)].append((x, y))
        ab, bc, cd, da = edge(a, b), edge(b, c), edge(c, d), edge(d, a)
        opposite_pairs.extend(((ab, cd), (bc, da)))
        cell_crossings.append((ab, bc))

    assert all(len(v) in (1, 2) for v in incidences.values())
    for occurrences in incidences.values():
        if len(occurrences) == 2:
            assert occurrences[0] == tuple(reversed(occurrences[1]))
    assert len(points) - len(incidences) + len(cells) == 1

    pair_count = 0
    actual_contacts = set()
    for a, b in combinations(sorted(points), 2):
        d2 = norm2(sub(physical(a), physical(b)))
        assert d2 >= 1
        pair_count += 1
        if d2 == 1:
            actual_contacts.add(edge(a, b))
    assert actual_contacts == set(incidences)

    dsu = DSU(incidences)
    for a, b in opposite_pairs:
        dsu.join(a, b)
    tracks = sorted({dsu.root(e) for e in incidences})
    degrees = {t: 0 for t in tracks}
    crossing_pairs = set()
    for a, b in cell_crossings:
        ta, tb = dsu.root(a), dsu.root(b)
        assert ta != tb
        pair = tuple(sorted((ta, tb)))
        assert pair not in crossing_pairs
        crossing_pairs.add(pair)
        degrees[ta] += 1
        degrees[tb] += 1
    assert sum(degrees.values()) == 2 * len(cells)

    outer = [v[0] for v in incidences.values() if len(v) == 1]
    outgoing = {}
    for a, b in outer:
        assert a not in outgoing
        outgoing[a] = b
    start = min(outgoing)
    walk = []
    p = start
    while not walk or p != start:
        q = outgoing[p]
        walk.append((p, q))
        p = q
        assert len(walk) <= len(outer)
    assert len(walk) == len(outer) == 2 * len(tracks)

    corners = hull(points)
    corner_set = set(corners)
    starts = [k for k, (a, _) in enumerate(walk) if a in corner_set]
    assert len(starts) == len(corners)
    shift = starts[0]
    walk = walk[shift:] + walk[:shift]
    chains, current = [], []
    for a, b in walk:
        if a in corner_set and current:
            chains.append(current)
            current = []
        current.append((a, b))
    chains.append(current)
    assert len(chains) == len(corners)

    terminals = defaultdict(list)
    for i, chain in enumerate(chains):
        for a, b in chain:
            vec = sub(physical(b), physical(a))
            midpoint = tuple((x + y) / 2 for x, y in zip(physical(a), physical(b)))
            terminals[dsu.root(edge(a, b))].append((i, vec, midpoint))
    for t in tracks:
        ends = terminals[t]
        assert len(ends) == 2
        assert add(ends[0][1], ends[1][1]) == (0, 0)
        assert norm2(sub(ends[1][2], ends[0][2])) <= degrees[t] ** 2

    chords = []
    for chain in chains:
        chord = sub(physical(chain[-1][1]), physical(chain[0][0]))
        assert norm2(chord) >= 1
        vecsum = (F(0), F(0))
        for a, b in chain:
            vecsum = add(vecsum, sub(physical(b), physical(a)))
        assert vecsum == chord
        chords.append(chord)
    return tracks, chains, chords, terminals, pair_count


def selections(tracks):
    count = len(tracks)
    if count <= 8:
        return [{t for j, t in enumerate(tracks) if mask & (1 << j)}
                for mask in range(1 << count)]
    options = [set(), set(tracks)]
    options.extend({t} for t in tracks)
    options.extend(set(tracks) - {t} for t in tracks)
    options.extend(set(tracks[k::step]) for step in (2, 3, 4) for k in range(step))
    options.extend({t for t in tracks if t[0][axis] == t[1][axis]}
                   for axis in (0, 1))
    return options


def check_graph(tracks, chains, chords, terminals, nonatomic):
    adjacency = [set() for _ in chains]
    for t in nonatomic:
        a, b = (v[0] for v in terminals[t])
        adjacency[a].add(b)
        adjacency[b].add(a)
    unseen = set(range(len(chains)))
    components = []
    while unseen:
        root = min(unseen)
        pending, component = [root], set()
        while pending:
            v = pending.pop()
            if v in component:
                continue
            component.add(v)
            pending.extend(adjacency[v] - component)
        unseen -= component
        components.append(component)
    assert len(nonatomic) >= len(chains) - len(components)

    atomic = set(tracks) - nonatomic
    for component in components:
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
    return len(components)


def main():
    assert norm2(U) == norm2(V) == 1
    assert 0 < V[0] < F(1, 2)
    patches = []
    for m in (2, 3, 4, 6):
        patches.append({(i, j) for i in range(m) for j in range(m + 1)})
        patches.append({(i, j) for j in range(m) for i in range(m - j)})
        patches.append({(i, j) for i in range(-m, m) for j in range(-m, m)
                        if abs(2 * i + 1) + abs(2 * j + 1) <= 2 * m})

    pair_count = graph_count = component_count = terminal_pair_count = 0
    for cells in patches:
        tracks, chains, chords, terminals, pairs = fixture(cells)
        pair_count += pairs
        terminal_pair_count += len(tracks)
        for nonatomic in selections(tracks):
            component_count += check_graph(tracks, chains, chords, terminals, nonatomic)
            graph_count += 1

    # Dropping one of a train's terminal occurrences destroys exact cancellation.
    tracks, chains, chords, terminals, _ = fixture({(0, 0)})
    for t in tracks:
        assert terminals[t][0][1] != (0, 0)
        assert add(terminals[t][0][1], terminals[t][1][1]) == (0, 0)
    # Atomic-only finite rectangles can have isolated chain-graph vertices:
    # the circle-limit proof, not the edge count alone, must rule them out.
    assert check_graph(tracks, chains, chords, terminals, set()) == len(chains)
    print(json.dumps({
        "status": "PASS",
        "arithmetic": "Fraction",
        "nonglobal_disk_fixtures": len(patches),
        "all_source_lower_pair_checks": pair_count,
        "physical_terminal_pair_checks": terminal_pair_count,
        "boundary_graph_selections": graph_count,
        "component_cancellation_checks": component_count,
        "scope": "finite identities only; no asymptotic or global-optimality certificate",
    }, indent=2))


if __name__ == "__main__":
    main()
