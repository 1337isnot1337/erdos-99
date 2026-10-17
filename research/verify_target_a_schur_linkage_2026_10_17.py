#!/usr/bin/env python3
"""Independent exact finite check of Sections 102/113/174/175.

No predecessor verifier is imported. Standard-library integers, signed symbolic
determinant monomials, exhaustive injections, vertex-split flow, and vertex-cut
enumeration provide distinct checks. The complete domain and nongeometric scope
are in docs/reports/target_a_independent_schur_linkage_2026-10-17.md.
Checks use explicit exceptions and also run under python -O.
"""

from collections import Counter, deque
from itertools import combinations, permutations, product
import argparse
import json
from pathlib import Path


B, C, Z, O = (0, 1), (2, 3), (4, 5), (6, 7)
FIXED = frozenset(zip(B, Z))
VERTICES = B + C + Z + O


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def subsets(items):
    items = tuple(items)
    for size in range(len(items) + 1):
        yield from combinations(items, size)


def symbolic_determinant(edges, rows, columns):
    """Return the signed polynomial in independent variables x_(left,right)."""
    coefficients = Counter()
    for order in permutations(columns):
        factors = tuple((left, right) for right, left in zip(rows, order))
        if all(edge in edges for edge in factors):
            inversions = sum(order[i] > order[j]
                             for i in range(len(order))
                             for j in range(i + 1, len(order)))
            coefficients[tuple(sorted(factors))] += (-1) ** inversions
    return {monomial: value for monomial, value in coefficients.items() if value}


def schur_rank(edges, terminals):
    # det S[I,J] = det A[Z+I,B+J] / det A[Z,B], with these block orders.
    require(symbolic_determinant(edges, Z, B), "singular symbolic basis")
    for size in range(min(len(terminals), len(O)), 0, -1):
        for selected_c in combinations(terminals, size):
            for selected_o in combinations(O, size):
                if symbolic_determinant(edges, Z + selected_o, B + selected_c):
                    return size
    return 0


def injection_rank(edges, basis, terminals, right):
    """Enumerate saturating injections; no augmenting-path algorithm."""
    for size in range(len(terminals), -1, -1):
        for chosen in combinations(terminals, size):
            left = tuple(basis) + chosen
            for images in permutations(right, len(left)):
                if all(edge in edges for edge in zip(left, images)):
                    return size
    raise ValueError("basis has no saturating injection")


def orientation(edges, matching=FIXED):
    return {(right, left) if (left, right) in matching else (left, right)
            for left, right in edges}


def contract_matching(vertices, arcs, matching=FIXED):
    partners = {z: b for b, z in matching}
    image = lambda v: partners.get(v, v)
    return (tuple(sorted({image(v) for v in vertices})),
            {(image(a), image(b)) for a, b in arcs if image(a) != image(b)})


def max_flow(vertices, arcs, starts, targets, edge_only=False):
    """Edmonds--Karp on split vertices; endpoints always have capacity one."""
    source, sink = (-1, 0), (-1, 1)
    capacity = {}
    adjacency = {}

    def add(a, b, value):
        capacity[a, b] = capacity.get((a, b), 0) + value
        capacity.setdefault((b, a), 0)
        adjacency.setdefault(a, set()).add(b)
        adjacency.setdefault(b, set()).add(a)

    for vertex in vertices:
        limit = len(vertices) if edge_only and vertex not in starts + targets else 1
        add((vertex, 0), (vertex, 1), limit)
    for a, b in sorted(arcs):
        add((a, 1), (b, 0), 1 if edge_only else len(vertices))
    for vertex in starts:
        add(source, (vertex, 0), 1)
    for vertex in targets:
        add((vertex, 1), sink, 1)

    value = 0
    while True:
        parent, queue = {source: None}, deque([source])
        while queue and sink not in parent:
            a = queue.popleft()
            for b in sorted(adjacency.get(a, ())):
                if b not in parent and capacity[a, b] > 0:
                    parent[b] = a
                    queue.append(b)
        if sink not in parent:
            return value
        b = sink
        while b != source:
            a = parent[b]
            capacity[a, b] -= 1
            capacity[b, a] += 1
            b = a
        value += 1


def separator_size(vertices, arcs, starts, targets):
    """Enumerate vertex separators directly, including terminal vertices."""
    for deleted in subsets(vertices):
        deleted = set(deleted)
        seen = set(starts) - deleted
        while True:
            expanded = seen | {b for a, b in arcs if a in seen and b not in deleted}
            if expanded == seen:
                break
            seen = expanded
        if not seen.intersection(targets):
            return len(deleted)
    raise ValueError("no separator")


def sector_data(edges, tube, shield_c):
    """Internal components exclude sinks, so sink sharing stays visible."""
    tube, shield_c = set(tube), set(shield_c)
    require(all({r for l, r in edges if l == c} <= tube for c in shield_c),
            "shield terminal has a neighbor outside the tube")
    shield = tube | shield_c | {b for b, z in FIXED if z in tube}
    remaining = set(VERTICES) - shield
    internal = remaining - set(O)
    adjacency = {v: set() for v in internal}
    for left, right in edges:
        if left in internal and right in internal:
            adjacency[left].add(right)
            adjacency[right].add(left)
    components = []
    while internal:
        root = min(internal)
        component, queue = {root}, [root]
        while queue:
            for neighbor in sorted(adjacency[queue.pop()] - component):
                component.add(neighbor)
                queue.append(neighbor)
        internal -= component
        components.append(component)
    sectors = []
    coarse_edges = set()
    for component in components:
        require(len(component.intersection(B)) == len(component.intersection(Z)),
                "sector basis balance failed")
        terminals = component.intersection(C)
        sinks = {o for left, o in edges if left in component
                 and o in O and o in remaining}
        sectors.append((terminals, sinks))
        coarse_edges.update(product(terminals, sinks))
    sink_counts = Counter(o for _, sinks in sectors for o in sinks)
    surviving_c = tuple(c for c in C if c in remaining)
    surviving_o = tuple(o for o in O if o in remaining)
    coarse_rank = injection_rank(coarse_edges, (), surviving_c, surviving_o)
    return {
        "shield": shield,
        "sectors": sectors,
        "sink_unique": max(sink_counts.values(), default=0) <= 1,
        "isolated_sinks": len(set(surviving_o) - set(sink_counts)),
        "coarse_rank": coarse_rank,
        "surviving_sinks": len(surviving_o),
    }


def negative_controls():
    direct = FIXED | {(2, 6), (3, 7)}
    require(schur_rank(direct, C) == 2, "direct control rank")
    try:
        sector_data(direct, (), (2,))
    except ValueError as error:
        require("outside the tube" in str(error), "wrong rejection")
    else:
        raise ValueError("accepted unintercepted shield terminal")
    # If that invalid deletion were allowed: rank 2 > |tube| + remaining rank 1.
    unintercepted = {"true_rank": 2, "invalid_cut_upper": 1}

    shared = FIXED | set(product(C, O))
    data = sector_data(shared, (), ())
    rank = schur_rank(shared, C)
    naive = data["isolated_sinks"] + sum(max(0, len(o) - len(c))
                                                   for c, o in data["sectors"])
    require(not data["sink_unique"] and naive > len(O) - rank,
            "shared-sink false surplus not exposed")
    overlap = {"true_right_deficiency": len(O) - rank,
               "invalid_disjoint_sink_lower": naive,
               "coarse_hall_lower": len(O) - data["coarse_rank"]}

    # Contracting a matched pair must retain capacity one. Before contraction,
    # its unique directed matching edge already enforces that capacity.
    matching = {(0, 4)}
    edges = matching | {(c, r) for c in (1, 2, 3) for r in (4, 5)} | {(0, 6), (0, 7)}
    arcs = orientation(edges, matching)
    vertex_rank = max_flow(tuple(range(8)), arcs, (1, 2, 3), (5, 6, 7))
    vertices, contracted_arcs = contract_matching(tuple(range(8)), arcs, matching)
    contracted_rank = max_flow(vertices, contracted_arcs, (1, 2, 3), (5, 6, 7))
    edge_rank = max_flow(vertices, contracted_arcs, (1, 2, 3), (5, 6, 7), True)
    require((vertex_rank, contracted_rank, edge_rank) == (2, 2, 3),
            "contracted-pair capacity control failed")

    backwards = FIXED | {(2, 6), (3, 6), (2, 4), (3, 4), (0, 7)}
    true_rank = schur_rank(backwards, C)
    wrong_rank = max_flow(VERTICES, set(backwards), C, O)
    require((true_rank, wrong_rank) == (2, 1), "orientation control failed")

    # Here S consists of four distinct variables generically. Setting all to
    # one gives [[1,1],[1,1]] and rank one, despite unchanged flow rank two.
    specialized = ((1, 1), (1, 1))
    determinant = specialized[0][0] * specialized[1][1] - specialized[0][1] * specialized[1][0]
    require(determinant == 0 and any(map(any, specialized)), "specialization control")
    require(rank == 2, "generic specialization control rank")
    return {
        "missing_terminal_interception": unintercepted,
        "overlapping_sector_sinks": overlap,
        "lost_capacity_after_matching_contraction": {
            "original_vertex_flow": vertex_rank,
            "contracted_vertex_flow": contracted_rank, "contracted_edge_flow": edge_rank},
        "wrong_matching_orientation": {"symbolic_rank": true_rank, "wrong_flow": wrong_rank},
        "equal_weight_specialization": {"generic_rank": rank, "specialized_rank": 1},
    }


def run():
    optional = tuple(sorted(set(product(B + C, Z + O)) - FIXED))
    counts = Counter()
    rank_counts = Counter()
    for mask in range(1 << len(optional)):
        edges = FIXED | {edge for i, edge in enumerate(optional) if mask & (1 << i)}
        if not all(any((c, o) in edges for o in O) for c in C):
            continue
        counts["supports"] += 1
        arcs = orientation(edges)
        rank = schur_rank(edges, C)
        rank_counts[str(rank)] += 1
        for terminals in subsets(C):
            symbolic = schur_rank(edges, terminals)
            flow = max_flow(VERTICES, arcs, terminals, O)
            injections = injection_rank(edges, B, terminals, Z + O)
            require(symbolic == flow == injections,
                    ("rank/linkage/injection disagreement", mask, terminals,
                     symbolic, flow, injections))
            counts["terminal_subset_checks"] += 1
        require(separator_size(VERTICES, arcs, C, O) == rank,
                ("minimum vertex separator disagreement", mask))
        counts["separator_checks"] += 1
        contracted_vertices, contracted_arcs = contract_matching(VERTICES, arcs)
        require(max_flow(contracted_vertices, contracted_arcs, C, O) == rank,
                ("unit-capacity matching contraction changed linkage", mask))
        counts["matching_contraction_checks"] += 1
        if (0, 5) in edges and (1, 4) in edges:
            counts["supports_with_basis_alternating_cycle"] += 1
        for tube in subsets(Z + O):
            eligible = tuple(c for c in C
                             if all(r in tube for l, r in edges if l == c))
            for shield_c in subsets(eligible):
                data = sector_data(edges, tube, shield_c)
                coarse = data["coarse_rank"]
                require(rank <= len(tube) + coarse,
                        ("overlap-safe tube cut failed", mask, tube, shield_c))
                # Cancellation of tube sinks needs no disjointness if coarse
                # matching, rather than a sum of separate surpluses, is used.
                require(len(O) - rank >= data["surviving_sinks"]
                        - len(set(tube).intersection(Z)) - coarse,
                        ("overlap-safe right deficiency failed", mask, tube, shield_c))
                counts["tube_shield_cases"] += 1
                if not data["sink_unique"]:
                    counts["overlapping_sink_cases"] += 1
                    continue
                sectors = data["sectors"]
                bound = len(tube) + sum(min(len(c), len(o)) for c, o in sectors)
                p = sum(max(0, len(c) - len(o)) for c, o in sectors)
                q = sum(max(0, len(o) - len(c)) for c, o in sectors)
                zeta_lower = len(shield_c) + p - len(tube)
                h_lower = data["isolated_sinks"] + q - len(set(tube).intersection(Z))
                require(rank <= bound and len(C) - rank >= zeta_lower
                        and len(O) - rank >= h_lower,
                        ("disjoint-sector inequality failed", mask, tube, shield_c))
                old_lower = p - len(data["shield"] - set(C))
                require(zeta_lower >= old_lower, "tube charge worse than old shield charge")
                counts["disjoint_sink_cases"] += 1
                counts["strict_charge_improvements"] += zeta_lower > old_lower
    require(counts["supports"] == 9216, "enumeration domain changed")
    return {
        "classification": "unreviewed exact finite verification; no geometric or global claim",
        "arithmetic": "integer flow/cuts/injections and signed polynomials in independent edge variables",
        "domain": {"basis": list(B), "terminals": list(C), "interior": list(Z),
                   "sinks": list(O), "fixed_edges": [list(e) for e in sorted(FIXED)],
                   "optional_edges": [list(e) for e in optional],
                   "condition": "each terminal has at least one direct exterior-sink neighbor"},
        "counts": dict(sorted(counts.items())),
        "generic_schur_rank_counts": dict(sorted(rank_counts.items())),
        "negative_controls": negative_controls(),
        "status": "PASS",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write deterministic JSON evidence")
    parser.add_argument("--check", type=Path, help="compare with committed JSON evidence")
    args = parser.parse_args()
    result = run()
    if args.check:
        require(result == json.loads(args.check.read_text()), "saved evidence differs")
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end="")
