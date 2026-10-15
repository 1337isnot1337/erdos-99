#!/usr/bin/env python3
"""Exact reciprocal integration and rigidity cuts on unit-contact packets.

The rational packets have positive unloaded contact equilibrium and pinned
boundary rigidity. Pins are not certified diameter loads. The checks prove
only the displayed finite integration, train signs, matrix identities and
subset counts, not global optimality or an asymptotic source's existence.
"""
from collections import defaultdict, deque
from fractions import Fraction as F
from itertools import combinations

from verify_target_c_global_phase_access_2026_10_05 import actual_packet, rank
from verify_target_c_global_face_return_quotas_2026_10_04 import edge, face_walks, sub


def plus(a, b):
    return a[0]+b[0], a[1]+b[1]


def packet(modules, t):
    data = actual_packet(modules, t, return_data=True)
    pos, contacts, weights = data["positions"], data["contacts"], data["weights"]
    trains, roots = data["trains"], data["roots"]
    added = {edge(3*j+i, 3*(j+2)+i)
             for j in range(1, 2*modules-1, 2) for i in (0, 2)}
    walks = face_walks(set(pos), contacts | added, pos)
    bounded = [w for w, area2 in walks if area2 > 0]
    outer = next(w for w, area2 in walks if area2 < 0)
    assert set(outer) == data["pins"]
    side_face = {(w[i], w[(i+1) % len(w)]): f
                 for f, w in enumerate(bounded) for i in range(len(w))}
    dual = defaultdict(list)
    internal_contact_count = 0
    for a, b in contacts:
        if (a, b) not in side_face or (b, a) not in side_face:
            continue
        left, right = side_face[a, b], side_face[b, a]
        dx, dy = sub(pos[b], pos[a])
        jump = (-weights[a, b]*dy, weights[a, b]*dx)
        dual[right].append((left, jump))
        dual[left].append((right, (-jump[0], -jump[1])))
        internal_contact_count += 1
    reciprocal = {0: (F(0), F(0))}
    queue = deque([0])
    cycle_checks = 0
    while queue:
        f = queue.popleft()
        for g, jump in dual[f]:
            candidate = plus(reciprocal[f], jump)
            if g in reciprocal:
                assert reciprocal[g] == candidate
                cycle_checks += 1
            else:
                reciprocal[g] = candidate
                queue.append(g)
    assert len(reciprocal) == len(bounded)
    assert internal_contact_count-len(bounded)+1 == len(pos)-len(data["pins"])

    nodes = [f for f, w in enumerate(bounded)
             if len(w) != 4 or any(edge(w[i], w[(i+1) % len(w)]) in added
                                   for i in range(len(w)))]
    node_index = {f: i for i, f in enumerate(nodes)}
    endpoints = {tr: [] for tr in trains}
    for f in nodes:
        w = bounded[f]
        for i in range(len(w)):
            a, b = w[i], w[(i+1) % len(w)]
            e = edge(a, b)
            if e not in added:
                endpoints[roots[e]].append((f, sub(pos[b], pos[a])))
    outside = {roots[edge(outer[i], outer[(i+1) % len(outer)])]
               for i in range(len(outer))
               if edge(outer[i], outer[(i+1) % len(outer)]) in contacts}
    internal = [tr for tr in trains if tr not in outside]
    angular = [[F(0)]*len(internal) for _ in range(2*len(nodes))]
    bar_transpose = [[F(0)]*len(internal) for _ in range(2*len(nodes))]
    pairs = set()
    adjacency = {f: set() for f in nodes}
    for column, tr in enumerate(internal):
        assert len(endpoints[tr]) == 2
        (f, w), (g, z) = endpoints[tr]
        assert f != g and w == (-z[0], -z[1])
        assert edge(f, g) not in pairs
        pairs.add(edge(f, g))
        adjacency[f].add(g)
        adjacency[g].add(f)
        mass = sum(weights[e] for e in contacts if roots[e] == tr)
        assert mass > 0
        difference = sub(reciprocal[g], reciprocal[f])
        assert difference == (mass*w[1], -mass*w[0])
        for face, vector in ((f, w), (g, z)):
            row = 2*node_index[face]
            angular[row][column], angular[row+1][column] = -vector[1], vector[0]
            bar_transpose[row][column] = mass*angular[row][column]
            bar_transpose[row+1][column] = mass*angular[row+1][column]
        assert (bar_transpose[2*node_index[f]][column],
                bar_transpose[2*node_index[f]+1][column]) == sub(reciprocal[f], reciprocal[g])
    assert rank(angular, len(internal)) == len(internal)
    assert rank(bar_transpose, len(internal)) == len(internal)

    # The two translations and rotation Jq annihilate the angular columns.
    dependencies = [[F(int(i % 2 == c)) for i in range(2*len(nodes))]
                    for c in range(2)]
    dependencies.append([v for f in nodes
                         for v in (-reciprocal[f][1], reciprocal[f][0])])
    assert all(sum(dependency[r]*angular[r][c] for r in range(2*len(nodes))) == 0
               for dependency in dependencies for c in range(len(internal)))
    if internal:
        assert rank(dependencies, 2*len(nodes)) == 3

    masks = range(1, 1 << len(nodes)) if len(nodes) <= 10 else (
        [1 << i for i in range(len(nodes))]
        + [(1 << i) | (1 << j) for i, j in combinations(range(len(nodes)), 2)]
        + [(1 << len(nodes))-1]
    )
    subset_checks = 0
    for mask in masks:
        selected = {f for i, f in enumerate(nodes) if mask >> i & 1}
        edges = sum(pair[0] in selected and pair[1] in selected for pair in pairs)
        if len(selected) >= 2:
            assert edges <= 2*len(selected)-3
        else:
            assert edges == 0
        remaining, bound = set(selected), 0
        while remaining:
            start = next(iter(remaining))
            component, pending = set(), [start]
            while pending:
                f = pending.pop()
                if f not in component:
                    component.add(f)
                    pending.extend((adjacency[f] & selected)-component)
            remaining -= component
            if len(component) >= 2:
                bound += 2*len(component)-3
        assert edges <= bound
        subset_checks += 1
    return data["checks"], cycle_checks, subset_checks, len(internal)


if __name__ == "__main__":
    results = [packet(n, t) for n in (1, 2, 3, 4, 6)
               for t in (F(1, 50), F(1, 40))]
    print(f"PASS: {sum(r[0] for r in results)} exact unit-pair checks in {len(results)} packets")
    print(f"PASS: {sum(r[1] for r in results)} exact reciprocal dual-cycle checks")
    print(f"PASS: {sum(r[3] for r in results)} positive train masses and signed straight-segment identities")
    print("PASS: simple internal endpoint graphs and exact normalized reciprocal rigidity matrices")
    print("PASS: two translation dependencies and the additional reciprocal rotation dependency")
    print(f"PASS: {sum(r[2] for r in results)} (2,3) and componentwise subset bounds")
    print("SCOPE: positive unloaded equilibrium and boundary pins; no actual diameter loads or global optimum")
