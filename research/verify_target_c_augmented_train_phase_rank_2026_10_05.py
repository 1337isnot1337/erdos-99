#!/usr/bin/env python3
"""Exact augmented angular columns and finite phase-bank inequalities.

Source pins are boundary points, not certified actual diameter endpoints.
Abstract phase-coloured double trees are incidence ledgers, not source
embeddings. No optimality, Groemer compactness, hull convergence or asymptotic
exclusion is certified by these checks.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product

from verify_target_c_global_phase_access_2026_10_05 import actual_packet, rank
from verify_target_c_global_face_return_quotas_2026_10_04 import edge, face_walks, sub


def augmented_packet(modules, t):
    data = actual_packet(modules, t, return_data=True)
    pos, contacts = data["positions"], data["contacts"]
    trains, roots = data["trains"], data["roots"]
    added = {edge(3*j+i, 3*(j+2)+i)
             for j in range(1, 2*modules-1, 2) for i in (0, 2)}
    assert not added & contacts and len(added) == 2*(modules-1)
    walks = face_walks(set(pos), contacts | added, pos)
    outer = next(w for w, area2 in walks if area2 < 0)
    assert set(outer) == data["pins"]
    bounded = [w for w, area2 in walks if area2 > 0]
    pockets = [w for w in bounded if any(edge(w[i], w[(i+1)%len(w)]) in added
                                     for i in range(len(w)))]
    nodes = [w for w in bounded if len(w) != 4 or w in pockets]
    assert len(pockets) == len(added)
    assert all(len(w) == 3 for w in pockets)
    assert all(sum(edge(w[i], w[(i+1)%len(w)]) in added
                   for i in range(len(w))) == 1 for w in pockets)
    assert len(nodes) == 3*modules-2

    index = {tr: i for i, tr in enumerate(trains)}
    endpoints = {tr: [] for tr in trains}
    closure = [[F(0)]*len(trains) for _ in range(2*len(nodes))]
    for node, w in enumerate(nodes):
        for i in range(len(w)):
            x, y = w[i], w[(i+1)%len(w)]
            e = edge(x, y)
            if e in added:
                continue  # exact zero auxiliary-vector displacement
            tr = roots[e]
            dx, dy = sub(pos[y], pos[x])
            endpoints[tr].append((node, (dx, dy)))
            closure[2*node][index[tr]] -= dy
            closure[2*node+1][index[tr]] += dx
    outer_contacts = {edge(outer[i], outer[(i+1)%len(outer)])
                      for i in range(len(outer))} & contacts
    outside_trains = {roots[e] for e in outer_contacts}
    internal = [tr for tr in trains if tr not in outside_trains]
    assert all(len(endpoints[tr]) == 2 for tr in internal)
    for tr in internal:
        (f, w), (g, z) = endpoints[tr]
        assert f != g and w == (-z[0], -z[1])
    matrix = [[row[index[tr]] for tr in internal] for row in closure]
    assert rank(matrix, len(internal)) == len(internal)
    assert len(internal) <= 2*len(nodes)-2
    count = 0
    # All subsets for the first four packet sizes, every singleton/pair and
    # the full node set for the larger ones.
    masks = range(1, 1 << len(nodes)) if len(nodes) <= 10 else (
        [1 << i for i in range(len(nodes))]
        + [(1 << i) | (1 << j) for i in range(len(nodes)) for j in range(i)]
        + [(1 << len(nodes))-1]
    )
    for mask in masks:
        selected = {i for i in range(len(nodes)) if mask >> i & 1}
        edges = sum(all(f in selected for f, _ in endpoints[tr]) for tr in internal)
        assert edges <= 2*len(selected)-2
        count += 1
    return data["checks"], count, len(internal)


def bank_ledger():
    count = 0
    # a=good physical nodes, h=bad nodes, ea=internal good edges,
    # x=good/bad train edges, y=good-to-pocket/outside terminals.
    # These scalar packets have no asserted source realization.
    for a, h, ea, x, y in product(range(8), range(7), range(15), range(16), range(25)):
        if a == 0 or ea > 2*a-2 or ea+x > 2*(a+h)-2:
            continue
        if 2*ea+x+y < 5*a:
            continue
        assert a+x <= 4*h+y-4
        incident = ea+x+y
        assert incident <= 8*h+3*y
        for ej in (y, y+1, y+7):
            # Additional H-H edges number at most 2h; all others have an
            # outside/good-pocket occurrence charged by E_j.
            all_trains = incident+2*h+ej
            assert all_trains <= 10*h+4*ej
            count += 1
    return count


def four_sided_pocket():
    # Three unit path edges and one nonunit hull chord. These two angular
    # rows must not be discarded as automatic unit-rhombus closure.
    t = F(1, 50)
    a, b = 2*t/(1+t*t), (1-t*t)/(1+t*t)
    pos = {0: (F(0), F(0)), 1: (a, b),
           2: (a, b+1), 3: (F(0), 2*b+1)}
    contacts, added = {edge(0, 1), edge(1, 2), edge(2, 3)}, {edge(0, 3)}
    for i in range(4):
        for j in range(i):
            dx, dy = sub(pos[i], pos[j])
            assert dx*dx+dy*dy >= 1
            assert (dx*dx+dy*dy == 1) == (edge(i, j) in contacts)
    bounded = [w for w, area2 in face_walks(set(pos), contacts | added, pos)
               if area2 > 0]
    assert len(bounded) == 1 and len(bounded[0]) == 4
    pockets = [w for w in bounded if any(edge(w[i], w[(i+1)%len(w)]) in added
                                         for i in range(len(w)))]
    assert pockets == bounded
    nodes = [w for w in bounded if len(w) != 4 or w in pockets]
    assert nodes == bounded
    w = bounded[0]
    vectors = [sub(pos[w[(i+1)%4]], pos[w[i]]) for i in range(4)
               if edge(w[i], w[(i+1)%4]) in contacts]
    assert rank([[-dy for dx, dy in vectors], [dx for dx, dy in vectors]], 3) == 2
    assert (2*b+1)**2 > 1


def coloured_tree(branching, height, pattern):
    parents, branch, levels = {}, {0: 0}, [[0]]
    for level in range(height):
        new = []
        for v in levels[-1]:
            for c in range(branching):
                w = len(parents)+1
                parents[w] = v
                branch[w] = c if level == 0 else branch[v]
                new.append(w)
        levels.append(new)
    forest = [(v, p) for v, p in parents.items()]
    edges = forest+forest
    degree = Counter(v for e in edges for v in e)
    leaves = set(levels[-1])
    colours = [(branch[v]+(pattern if i % 11 == 0 else 0)) % branching
               for i, (v, _) in enumerate(edges)]
    incident_colours = {v: set() for v in range(len(parents)+1)}
    for e, colour in zip(edges, colours):
        for v in e:
            incident_colours[v].add(colour)
    bad = {v for v, cs in incident_colours.items() if len(cs) != 1}
    for colour in range(branching):
        good = {v for v, cs in incident_colours.items() if cs == {colour}}
        physical = good-leaves
        pockets = good & leaves
        assert all(degree[v] >= 5 for v in physical)
        assert all(degree[v] == 2 for v in pockets)
        assert all(not (v in physical and w not in physical | pockets | bad)
                   and not (w in physical and v not in physical | pockets | bad)
                   for v, w in edges)
        nj = sum(c == colour for c in colours)
        ej = sum(degree[v] for v in pockets)
        assert nj <= 10*len(bad)+4*ej
    return branching


if __name__ == "__main__":
    sources = [augmented_packet(n, t) for n in (1, 2, 3, 4, 6, 8)
               for t in (F(1, 50), F(1, 40))]
    four_sided_pocket()
    ledgers = bank_ledger()
    colours = sum(coloured_tree(b, h, p) for b in (2, 3, 4)
                  for h in (2, 3, 5) for p in (0, 1, 2))
    print(f"PASS: {sum(x[0] for x in sources)} rational unit-pair checks in {len(sources)} sources")
    print("PASS: hull augmentation, one added side per pocket, zero-vector auxiliary contract")
    print("PASS: independent augmented internal columns, including former outer train ends")
    print("PASS: four-sided nonunit-chord pocket retained with both angular closure rows")
    print(f"PASS: {sum(x[1] for x in sources)} augmented node-subset sparsity checks")
    print(f"PASS: {ledgers} exact phase-bank ledgers and {colours} coloured-tree bin checks")
    print("SCOPE: no actual diameter loading, global optimality, compactness or asymptotic exclusion certified")
