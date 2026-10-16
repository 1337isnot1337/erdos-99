#!/usr/bin/env python3
"""Exact rotation-system obstruction for the certified collapsed local chamber.

The imported contraction certificate supplies a rigorous angle box and cyclic orders.
The remainder is finite integer combinatorics: enumerate every angle-eligible,
bounded-face-disjoint crossing subset, crossing order, and alternating crossing
rotation, then test its face count.  A planarization must have Euler characteristic 2.
"""

import ast
import contextlib
import importlib.util
import io
import itertools
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "research" / "verify_target_c_support6_collapsed_local_realization_2026_09_18.py"
spec = importlib.util.spec_from_file_location("collapsed_local", source)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(module)

edges = sorted(set(tuple(sorted(e)) for e in module.EDGES))
assert len(edges) == 12

# The contraction proof certifies every root angle in X0 +/- R.  Classify the
# projective gap with interval arithmetic, using the exact pi enclosure from it.
angle_box = {
    e: ((a - module.R, a + module.R) if e in module.VAR_EDGES else (a, a))
    for e, a in module.A.items()
}


def interval_gap(e, f):
    lo = angle_box[e][0] - angle_box[f][1]
    hi = angle_box[e][1] - angle_box[f][0]
    candidates = []
    for k in range(-4, 5):
        qlo = lo - k * module.PI[1] if k >= 0 else lo - k * module.PI[0]
        qhi = hi - k * module.PI[0] if k >= 0 else hi - k * module.PI[1]
        if qlo >= 0 and qhi < module.PI[0]:
            candidates.append((qlo, qhi))
    assert len(candidates) == 1
    qlo, qhi = candidates[0]
    if qhi <= module.PI[0] / 2:
        return qlo, qhi
    if qlo >= module.PI[1] / 2:
        return module.PI[0] - qhi, module.PI[1] - qlo
    raise AssertionError("projective-gap interval straddles pi/2")


eligible = []
ineligible = []
for i, e in enumerate(edges):
    for j in range(i + 1, len(edges)):
        f = edges[j]
        gap = interval_gap(e, f)
        if gap[0] > module.PI[1] / 3:
            eligible.append((i, j))
        else:
            assert gap[1] <= module.PI[0] / 3
            ineligible.append((i, j))

# The bounded-face endpoint-fan theorem removes crossings of trains with a common
# bounded endpoint.  The angle test leaves exactly seven usable pairs.
eligible = [
    pair for pair in eligible
    if not (set(edges[pair[0]]) & set(edges[pair[1]]))
]
assert len(eligible) == 7

# Parse the exact cyclic train-end rotations certified by the local verifier.
rotation = {}
for vertex, order in enumerate(module.FACE_ORDERS):
    neighbors = []
    for label in order:
        if label == "anchor":
            continue
        a, b = ast.literal_eval(label)
        neighbors.append(b if a == vertex else a)
    assert len(neighbors) == 4
    rotation[vertex] = neighbors


def triangle_free(crossings):
    crossing_graph = {i: set() for i in range(len(edges))}
    for a, b in crossings:
        crossing_graph[a].add(b)
        crossing_graph[b].add(a)
    return not any(
        b in crossing_graph[a] and c in crossing_graph[a] and c in crossing_graph[b]
        for a in crossing_graph
        for b in crossing_graph[a]
        for c in crossing_graph[a]
        if a < b < c
    )


def face_count(crossings, orders, crossing_bits):
    """Face count of the subdivided graph with the prescribed rotations."""
    crossing_count = len(crossings)
    adjacency = {v: [] for v in range(6 + crossing_count)}

    for edge_index, (a, b) in enumerate(edges):
        ids = orders.get(edge_index, [])
        chain = [a] + [6 + k for k in ids] + [b]
        for x, y in zip(chain, chain[1:]):
            adjacency[x].append(y)
            adjacency[y].append(x)

    for vertex in range(6):
        ordered = []
        for neighbor in rotation[vertex]:
            edge_index = edges.index(tuple(sorted((vertex, neighbor))))
            ids = orders.get(edge_index, [])
            if not ids:
                ordered.append(neighbor)
            elif vertex == edges[edge_index][0]:
                ordered.append(6 + ids[0])
            else:
                ordered.append(6 + ids[-1])
        assert set(ordered) == set(adjacency[vertex])
        adjacency[vertex] = ordered

    for crossing_index, (edge_a, edge_b) in enumerate(crossings):
        def neighbors_on(edge_index):
            ids = orders.get(edge_index, [])
            position = ids.index(crossing_index)
            a, b = edges[edge_index]
            previous = a if position == 0 else 6 + ids[position - 1]
            following = b if position == len(ids) - 1 else 6 + ids[position + 1]
            return previous, following

        a, b = neighbors_on(edge_a)
        c, d = neighbors_on(edge_b)
        options = ((a, c, b, d), (a, d, b, c))
        adjacency[6 + crossing_index] = list(options[crossing_bits[crossing_index]])

    darts = [(v, w) for v, neighbors in adjacency.items() for w in neighbors]
    successor = {}
    for vertex, neighbors in adjacency.items():
        for index, previous in enumerate(neighbors):
            successor[(previous, vertex)] = (vertex, neighbors[(index + 1) % len(neighbors)])

    seen = set()
    faces = 0
    for dart in darts:
        if dart in seen:
            continue
        faces += 1
        current = dart
        while current not in seen:
            seen.add(current)
            current = successor[(current[1], current[0])]
    return faces


tested_subsets = 0
tested_rotations = 0
for mask in range(1 << len(eligible)):
    crossings = [eligible[k] for k in range(len(eligible)) if mask & (1 << k)]
    if not triangle_free(crossings):
        continue
    tested_subsets += 1

    incidence = {edge_index: [] for edge_index in range(len(edges))}
    for crossing_index, (a, b) in enumerate(crossings):
        incidence[a].append(crossing_index)
        incidence[b].append(crossing_index)

    multi_edges = [e for e, ids in incidence.items() if len(ids) > 1]
    order_choices = [list(itertools.permutations(incidence[e])) for e in multi_edges]
    products = itertools.product(*order_choices) if order_choices else [()]
    for choices in products:
        orders = {e: list(ids) for e, ids in incidence.items() if ids}
        for e, choice in zip(multi_edges, choices):
            orders[e] = list(choice)
        for bits in itertools.product((0, 1), repeat=len(crossings)):
            tested_rotations += 1
            vertices = 6 + len(crossings)
            edge_count = 12 + 2 * len(crossings)
            assert face_count(crossings, orders, bits) != edge_count - vertices + 2

print("angle_eligible_disjoint_pairs", len(eligible))
print("legal_crossing_subsets", tested_subsets)
print("rotation_systems_tested", tested_rotations)
print("PASS: certified collapsed order chamber has no planar train routing")
