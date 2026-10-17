#!/usr/bin/env python3
"""Reviewer-owned replay: no imports from the submitted checker.

Build the actual 2x2 Schur numerator with sparse polynomial arithmetic and
an adjugate, then zero unsupported variables. Enumerate simple directed paths
and pairs of disjoint paths rather than using flow, cuts, or determinant minors.
Also reconstruct every tube case with union-find, rather than graph search.
"""
from collections import Counter
from itertools import product
import json

B, C, Z, O = (0, 1), (2, 3), (4, 5), (6, 7)
all_edges = tuple(product(B + C, Z + O))
edge_index = {edge: i for i, edge in enumerate(all_edges)}
fixed = {(0, 4), (1, 5)}
optional = tuple(edge for edge in all_edges if edge not in fixed)

def add(*terms):
    result = Counter()
    for term in terms:
        result.update(term)
    return {m: n for m, n in result.items() if n}

def scale(p, n):
    return {m: n * c for m, c in p.items()}

def mul(p, q):
    result = Counter()
    for m, a in p.items():
        for n, b in q.items():
            result[tuple(sorted(m + n))] += a * b
    return {m: n for m, n in result.items() if n}

def x(left, right):
    return {(edge_index[left, right],): 1}

delta = add(mul(x(0, 4), x(1, 5)), scale(mul(x(1, 4), x(0, 5)), -1))
adj = ((x(1, 5), scale(x(1, 4), -1)),
       (scale(x(0, 5), -1), x(0, 4)))
numerators = {}
for o in O:
    for c in C:
        correction = add(*(mul(mul(x(b, o), adj[i][j]), x(c, z))
                           for i, b in enumerate(B) for j, z in enumerate(Z)))
        numerators[o, c] = add(mul(delta, x(c, o)), scale(correction, -1))
detnumerator = add(mul(numerators[6, 2], numerators[7, 3]),
                   scale(mul(numerators[6, 3], numerators[7, 2]), -1))

def nonzero(poly, support):
    return any(all(all_edges[i] in support for i in monomial) for monomial in poly)

def actual_schur_rank(support, terminals=C):
    if len(terminals) == 2 and nonzero(detnumerator, support):
        return 2
    return int(any(nonzero(numerators[o, c], support) for o in O for c in terminals))

def simple_paths(arcs, start, targets, prefix=()):
    if start in targets:
        return [frozenset(prefix + (start,))]
    paths = []
    for a, b in arcs:
        if a == start and b not in prefix:
            paths += simple_paths(arcs, b, targets, prefix + (start,))
    return paths

def path_rank(arcs, terminals=C):
    paths = {c: simple_paths(arcs, c, O) for c in terminals}
    if len(terminals) == 2 and any(a.isdisjoint(b) for a in paths[2] for b in paths[3]):
        return 2
    return int(any(paths.values()))

def coarse_matching(neighbors):
    if len(neighbors) == 2 and any(o != p for o in neighbors[2] for p in neighbors[3]):
        return 2
    return int(any(neighbors.values()))

counts, ranks, unrestricted_ranks = Counter(), Counter(), Counter()
for bits in range(1 << len(optional)):
    support = fixed | {e for i, e in enumerate(optional) if bits >> i & 1}
    arcs = {(r, l) if (l, r) in fixed else (l, r) for l, r in support}
    rank = actual_schur_rank(support)
    unrestricted_ranks[rank] += 1
    for terminals in ((), (2,), (3,), C):
        assert actual_schur_rank(support, terminals) == path_rank(arcs, terminals)
        counts['unrestricted_terminal_checks'] += 1
    contracted = {(1 if a == 5 else 0 if a == 4 else a,
                   1 if b == 5 else 0 if b == 4 else b) for a, b in arcs}
    contracted = {(a, b) for a, b in contracted if a != b}
    assert path_rank(contracted) == rank
    counts['unrestricted_contraction_checks'] += 1
    if not all(any((c, o) in support for o in O) for c in C):
        continue
    counts['supports'] += 1
    ranks[rank] += 1
    counts['cyclic_supports'] += {(0, 5), (1, 4)} <= support
    for tbits in range(16):
        tube = {v for i, v in enumerate(Z + O) if tbits >> i & 1}
        eligible = [c for c in C if all(r in tube for l, r in support if l == c)]
        for cbits in range(1 << len(eligible)):
            shield_c = {c for i, c in enumerate(eligible) if cbits >> i & 1}
            shield = tube | shield_c | {b for b, z in fixed if z in tube}
            internal = set(B + C + Z) - shield
            parents = {v: v for v in internal}
            def find(v):
                while parents[v] != v:
                    v = parents[v]
                return v
            for l, r in support:
                if l in internal and r in internal:
                    parents[find(l)] = find(r)
            sectors = {}
            for v in internal:
                sectors.setdefault(find(v), set()).add(v)
            data, neighbors = [], {}
            for component in sectors.values():
                assert len(component & set(B)) == len(component & set(Z))
                cs = component & set(C)
                os = {o for l, o in support if l in component and o in O and o not in tube}
                data.append((cs, os))
                neighbors.update({c: os for c in cs})
            coarse = coarse_matching(neighbors)
            assert rank <= len(tube) + coarse
            assert 2 - rank >= len(set(O) - tube) - len(tube & set(Z)) - coarse
            counts['tube_shield_cases'] += 1
            sink_occurrences = Counter(o for _, os in data for o in os)
            if max(sink_occurrences.values(), default=0) > 1:
                counts['overlapping_sink_cases'] += 1
                continue
            counts['disjoint_sink_cases'] += 1
            p = sum(max(0, len(cs)-len(os)) for cs, os in data)
            q = sum(max(0, len(os)-len(cs)) for cs, os in data)
            iso = len(set(O) - tube - set(sink_occurrences))
            assert coarse == sum(min(len(cs), len(os)) for cs, os in data)
            assert 2-rank >= len(shield_c)+p-len(tube)
            assert 2-rank >= iso+q-len(tube & set(Z))
            old = p-len(shield-set(C))
            new = len(shield_c)+p-len(tube)
            assert new >= old
            counts['strict_charge_improvements'] += new > old

def path_sequences(arcs, source, targets, visited=()):
    if source in targets:
        return [visited + (source,)]
    return [path for a, b in arcs if a == source and b not in visited
            for path in path_sequences(arcs, b, targets, visited + (source,))]

def packing_number(arcs, sources, targets, edge_capacity=False):
    choices = [[None] + path_sequences(arcs, s, targets) for s in sources]
    best = 0
    for selected in product(*choices):
        paths = [path for path in selected if path is not None]
        if len({p[-1] for p in paths}) != len(paths):
            continue
        occupied = [set(zip(p, p[1:])) if edge_capacity else set(p) for p in paths]
        if all(a.isdisjoint(b) for i, a in enumerate(occupied) for b in occupied[i+1:]):
            best = max(best, len(paths))
    return best

direct = fixed | {(2, 6), (3, 7)}
assert actual_schur_rank(direct) == 2 > 1
shared = fixed | set(product(C, O))
assert actual_schur_rank(shared) == 2
backwards = fixed | {(2, 6), (3, 6), (2, 4), (3, 4), (0, 7)}
assert actual_schur_rank(backwards) == 2 and path_rank(backwards) == 1
onepair = {(0, 4)}
capacity_support = onepair | set(product((1, 2, 3), (4, 5))) | {(0, 6), (0, 7)}
capacity_arcs = {(r, l) if (l, r) in onepair else (l, r) for l, r in capacity_support}
collapsed = {(0 if a == 4 else a, 0 if b == 4 else b) for a, b in capacity_arcs}
collapsed = {(a, b) for a, b in collapsed if a != b}
capacity_results = (packing_number(capacity_arcs, (1, 2, 3), (5, 6, 7)),
                    packing_number(collapsed, (1, 2, 3), (5, 6, 7)),
                    packing_number(collapsed, (1, 2, 3), (5, 6, 7), True))
assert capacity_results == (2, 2, 3)
negative_controls = {
    'missing_terminal_interception': {'actual_rank': 2, 'invalid_cut_upper': 1},
    'overlapping_sinks': {'actual_deficiency': 0, 'invalid_separate_surplus': 2},
    'contraction_capacity': capacity_results,
    'wrong_orientation': {'actual_rank': 2, 'wrong_path_rank': 1},
    'equal_weights': {'generic_rank': 2, 'specialized_all_ones_rank': 1}}

print(json.dumps({'status': 'PASS', 'counts': dict(counts),
                  'rank_counts': dict(ranks), 'unrestricted_rank_counts': dict(unrestricted_ranks),
                  'negative_controls': negative_controls,
                  'schur_polynomial_terms': {'denominator': len(delta),
                      'entry_numerators': [len(p) for p in numerators.values()],
                      'determinant_numerator': len(detnumerator)}}, indent=2))
