#!/usr/bin/env python3
"""Exact graph certificate for the collapsed support-six corridor reduction.

Scope: contract each of the twelve internal K6-minus-a-perfect-matching trains
and six one-anchor trains to internally disjoint edges in a planar cellulation.
The resulting train-incidence graph has seven vertices (six exceptional faces
and the outer/activated host) and eighteen distinct edges.  A simple planar
graph on seven vertices has at most fifteen edges, so this disjoint-corridor
model is impossible.  The same Euler bound gives a lower bound of three edge
crossing events in any general-position drawing of the contracted skeleton.

This is not a global exclusion: stopped trains may share rhombi or otherwise
interact, and the certificate deliberately does not assume that they contract
to internally disjoint edges.  It identifies the exact global condition that a
future collapsed-branch exclusion must supply.
"""

from itertools import combinations, permutations


HOSTS = tuple(range(6))
OUTER = 6
MISSING = {tuple(sorted(e)) for e in ((0, 3), (1, 4), (2, 5))}
INTERNAL = {
    (i, j)
    for i, j in combinations(HOSTS, 2)
    if (i, j) not in MISSING
}
ANCHORS = {(i, OUTER) for i in HOSTS}
SKELETON = INTERNAL | ANCHORS


def main():
    assert len(INTERNAL) == 12
    assert len(ANCHORS) == 6
    assert len(SKELETON) == 18
    assert len({tuple(sorted(e)) for e in SKELETON}) == 18
    # Euler's planar simple-graph bound E <= 3V-6, with V=7.
    vertices = set(HOSTS) | {OUTER}
    assert len(vertices) == 7
    planar_simple_max = 3 * len(vertices) - 6
    excess = len(SKELETON) - planar_simple_max
    assert excess == 3
    assert len(SKELETON) > planar_simple_max
    # Removing one edge per crossing event planarizes a general-position
    # drawing; hence at least E-(3V-6) crossing events are necessary.
    crossing_lower_bound = excess
    assert crossing_lower_bound == 3

    # In the stronger all-outer subcase, pairwise noncrossing parallel anchor
    # corridors put the six hosts in one cyclic boundary order.  Count the
    # forced chord crossings of the internal graph for every such order.
    def alternates(a, b, order):
        if set(a) & set(b):
            return False
        pos = {vertex: index for index, vertex in enumerate(order)}
        i, j = sorted((pos[x] for x in a))
        k, ell = sorted((pos[x] for x in b))
        return (i < k < j) != (i < ell < j)

    convex_crossings = []
    convex_crossing_graphs = []
    for order in permutations(HOSTS):
        crossing_pairs = {
            (a, b)
            for a, b in combinations(sorted(INTERNAL), 2)
            if alternates(a, b, order)
        }
        convex_crossings.append(len(crossing_pairs))
        convex_crossing_graphs.append(crossing_pairs)
    convex_minimum = min(convex_crossings)
    assert len(convex_crossings) == 720
    assert convex_minimum == 6
    minimum_graphs = [
        crossing_pairs
        for count, crossing_pairs in zip(convex_crossings, convex_crossing_graphs)
        if count == convex_minimum
    ]

    # The minimum interaction graph is sharper than triangle-free: each of the
    # twelve internal train vertices has crossing degree two and the graph is
    # connected, hence it is one 6-cycle (the remaining six internal trains are
    # isolated).  Also record the sign-transition split for the fixed collapsed
    # 3+3 anchor word.
    cycle_count = 0
    transition_counts = {2: 0, 4: 0, 6: 0}
    crossing_colour_counts = {}
    for order, crossing_pairs in zip(
        (order for order in permutations(HOSTS) if len({
            (a, b) for a, b in combinations(sorted(INTERNAL), 2)
            if alternates(a, b, order)
        }) == convex_minimum),
        minimum_graphs,
    ):
        degree = {e: 0 for e in INTERNAL}
        adjacency = {e: set() for e in INTERNAL}
        for a, b in crossing_pairs:
            degree[a] += 1
            degree[b] += 1
            adjacency[a].add(b)
            adjacency[b].add(a)
        assert set(degree.values()) == {0, 2}
        active = [e for e, d in degree.items() if d]
        assert len(active) == 6
        assert len(set(INTERNAL) - set(active)) == 6
        seen = set()
        stack = [active[0]]
        while stack:
            e = stack.pop()
            if e in seen:
                continue
            seen.add(e)
            stack.extend(adjacency[e] - seen)
        assert len(seen) == 6
        cycle_count += 1
        signs = [1 if vertex in (0, 1, 2) else -1 for vertex in order]
        transitions = sum(signs[i] != signs[(i + 1) % 6] for i in range(6))
        transition_counts[transitions] += 1
        coloured = {
            e for e in INTERNAL if (e[0] in (0, 1, 2)) != (e[1] in (0, 1, 2))
        }
        cc = sum(a in coloured and b in coloured for a, b in crossing_pairs)
        ss = sum(a not in coloured and b not in coloured for a, b in crossing_pairs)
        mixed = sum((a in coloured) != (b in coloured) for a, b in crossing_pairs)
        old = crossing_colour_counts.get(transitions)
        current = (cc, ss, mixed)
        assert old is None or old == current
        crossing_colour_counts[transitions] = current
    assert cycle_count == len(minimum_graphs) == 48
    assert transition_counts == {2: 36, 4: 0, 6: 12}
    assert crossing_colour_counts == {2: (2, 0, 4), 6: (0, 6, 0)}

    def crossing_graph_has_triangle(crossing_pairs):
        for a, b, c in combinations(INTERNAL, 3):
            if all(
                tuple(sorted((x, y))) in crossing_pairs
                for x, y in ((a, b), (a, c), (b, c))
            ):
                return True
        return False

    # The triangle-free train-crossing condition alone does not exclude this
    # minimum pattern: every minimum convex order has a triangle-free crossing
    # graph.  This is a deliberate finite regression against an easy overreach.
    assert minimum_graphs
    assert all(not crossing_graph_has_triangle(graph) for graph in minimum_graphs)
    print("collapsed_internal_trains", len(INTERNAL))
    print("collapsed_anchor_trains", len(ANCHORS))
    print("contracted_vertices", len(vertices))
    print("contracted_edges", len(SKELETON))
    print("planar_simple_edge_bound", planar_simple_max)
    print("disjoint_corridor_edge_excess", excess)
    print("minimum_general_position_crossing_events", crossing_lower_bound)
    print("all_outer_convex_order_count", len(convex_crossings))
    print("all_outer_minimum_internal_chord_crossings", convex_minimum)
    print("all_outer_minimum_patterns", len(minimum_graphs))
    print("all_outer_minimum_crossing_graph", "C6_plus_6_isolated")
    print("all_outer_minimum_anchor_sign_transition_counts", transition_counts)
    print("all_outer_minimum_crossing_colour_counts", crossing_colour_counts)
    print("all_outer_minimum_crossing_graphs_triangle_free", True)
    print("PASS: internally-disjoint collapsed corridor model is nonplanar")
    print("PASS: all-outer parallel-anchor convex model needs six crossings")
    print("SCOPE: shared-rhombus/corridor interactions remain live")


if __name__ == "__main__":
    main()
