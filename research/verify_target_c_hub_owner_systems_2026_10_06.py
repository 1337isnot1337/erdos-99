#!/usr/bin/env python3
"""Exact abstract owner-tree search. No source or global-optimality assertion.

Enumerates ordered trees, acute-binary zero/moving labels, physical loaded-cycle
clauses, and terminal banks. It separately checks the general Horn criterion.
The geometry needed to realize the abstract data is deliberately not assumed.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations, permutations, product
import json
from pathlib import Path


@lru_cache(None)
def trees(edges):
    if edges == 0:
        return ((),)
    return tuple(forests(edges))


@lru_cache(None)
def forests(total):
    if total == 0:
        return ((),)
    result = []
    for first in range(1, total + 1):
        for child in trees(first - 1):
            for rest in forests(total - first):
                result.append((child,) + rest)
    return tuple(result)


def unpack(shape):
    edges, depths, children = [], [0], [[]]

    def visit(subtree, parent):
        for child in subtree:
            idx = len(depths)
            depths.append(depths[parent] + 1)
            children.append([])
            children[parent].append(idx)
            edges.append((parent, idx))
            visit(child, idx)

    visit(shape, 0)
    contour = []

    def walk(v):
        contour.append(v)
        for child in children[v]:
            walk(child)
            contour.append(v)

    walk(0)
    return edges, depths, contour[:-1]


def labelings(depths, max_owners=3):
    moving = [v for v, depth in enumerate(depths) if depth % 2]
    labels = [0] * len(depths)

    def visit(index, largest):
        if index == len(moving):
            yield tuple(labels)
            return
        for owner in range(1, min(largest + 1, max_owners) + 1):
            labels[moving[index]] = owner
            yield from visit(index + 1, max(largest, owner))

    yield from visit(0, 0)


def runs(word, owner):
    if all(x == owner for x in word):
        return 1
    return sum(x == owner and word[i - 1] != owner
               for i, x in enumerate(word))


def model(bits, implications, conflicts, unary):
    return (all(not bits[i] or bits[j] for i, j in implications)
            and all(not (bits[i] and bits[j]) for i, j in conflicts)
            and all(not bits[i] for i in unary))


def closure(k, implications, conflicts, unary, pins, false_pins=()):
    true = set(pins)
    changed = True
    while changed:
        changed = False
        for i, j in implications:
            if i in true and j not in true:
                true.add(j)
                changed = True
    if true.intersection(set(unary) | set(false_pins)):
        return None
    if any(i in true and j in true for i, j in conflicts):
        return None
    return tuple(int(i in true) for i in range(k))


def horn_checks():
    count = 0
    for k in range(4):
        possible = ([('u', i, i) for i in range(k)]
                    + [('a', i, j) for i in range(k) for j in range(k) if i != j]
                    + [('f', i, j) for i, j in combinations(range(k), 2)])
        for mask in range(1 << len(possible)):
            clauses = [c for j, c in enumerate(possible) if mask >> j & 1]
            arcs = [(i, j) for kind, i, j in clauses if kind == 'a']
            pairs = [(i, j) for kind, i, j in clauses if kind == 'f']
            unary = [i for kind, i, j in clauses if kind == 'u']
            for pinspec in product(range(3), repeat=k):
                pins = [i for i, x in enumerate(pinspec) if x == 1]
                false = [i for i, x in enumerate(pinspec) if x == 2]
                answer = closure(k, arcs, pairs, unary, pins, false)
                exists = any(model(bits, arcs, pairs, unary)
                             and all(bits[i] for i in pins)
                             and all(not bits[i] for i in false)
                             for bits in product(range(2), repeat=k))
                assert (answer is not None) == exists
                if answer is not None:
                    assert model(answer, arcs, pairs, unary)
                count += 1
    return count


def check_recurrence(max_edges):
    """Each edge has one moving owner; <=1 fully good edge in narrow scope."""
    cases = 0
    sharp = []
    for total in range(1, max_edges + 1):
        for shape in trees(total):
            edges, depths, contour = unpack(shape)
            for labels in labelings(depths):
                k = max(labels)
                component_counts = [labels.count(i) for i in range(1, k + 1)]
                rho = sum(c - 1 for c in component_counts)
                # Same nonzero labels never touch in the acute binary tree.
                assert all((labels[a] == 0) != (labels[b] == 0) for a, b in edges)
                # Choose zero or one fully-good train. Each remaining train
                # spends a distinct bad terminal occurrence; this is the
                # smallest possible bank for that abstract selected family.
                for fully_good in [None] + list(range(total)):
                    bad_bank = total - int(fully_good is not None)
                    assert k + rho <= bad_bank + 1
                    assert rho <= bad_bank
                    # Overlap-aware owner train bank: allocate every edge to
                    # its unique moving-side label. No root/tail double charge.
                    allocation = [0] * (k + 1)
                    for a, b in edges:
                        allocation[labels[a] or labels[b]] += 1
                    assert sum(allocation) == total
                    assert all(allocation[i] >= component_counts[i - 1]
                               for i in range(1, k + 1))
                    if rho == bad_bank and len(sharp) < 3:
                        sharp.append({'edges': edges, 'labels': labels,
                                      'rho': rho, 'bad_bank': bad_bank})
                    cases += 1
    return cases, sharp


def smallest_loaded_binary_sink(max_edges=4, require_long_pockets=False):
    """Enumerate the first two-owner zero-only obstruction with no unary.

    Every role has a distinct physical hull side. Zero/moving labels are
    acute-binary compatible. Fully-good count is <=1 and all other selected
    trains have distinct bad terminal tokens. A convex odd-star diameter
    graph supplies hub paths, with no diameter inside any nonhub branch.
    No directions, KKT forces, return demands, or finite moves are encoded.
    """
    candidate_count = 0
    survivors = []
    for total in range(1, max_edges + 1):
        for shape in trees(total):
            edges, depths, contour = unpack(shape)
            for labels in labelings(depths, 2):
                if max(labels) != 2:
                    continue
                for mask in range(1 << len(contour)):
                    regions = [v for j, v in enumerate(contour) if mask >> j & 1]
                    q = len(regions)
                    if q < 5 or q % 2 == 0:
                        continue
                    word = [labels[v] for v in regions]
                    if not {1, 2}.issubset(word):
                        continue
                    # A physical hull side is represented by its endpoint
                    # positions, even if those positions share region labels.
                    cross = [(j, (j + 1) % q) for j in range(q)
                             if {word[j], word[(j + 1) % q]} == {1, 2}]
                    for selected in combinations(cross, 3):
                        for roles in permutations(('12', '21', 'conflict')):
                            candidate_count += 1
                            arcs, conflicts = [], []
                            for pair, role in zip(selected, roles):
                                if role == '12':
                                    arcs.append((0, 1))
                                elif role == '21':
                                    arcs.append((1, 0))
                                else:
                                    conflicts.append((0, 1))
                            assert not any(model(bits, arcs, conflicts, ())
                                           for bits in ((1, 0), (0, 1), (1, 1)))
                            r = [runs(word, i) for i in (1, 2)]
                            assert min(r) >= 2
                            if sum(r) > total:
                                continue
                            # Tree branches below hub 0 are identified by their
                            # first ancestor. Construct the odd convex thrackle.
                            parent = {b: a for a, b in edges}

                            def branch(v):
                                if v == 0:
                                    return None
                                while parent[v] != 0:
                                    v = parent[v]
                                return v

                            star_step = (q - 1) // 2
                            diameter_pairs = [(j, (j + star_step) % q) for j in range(q)]
                            if any(branch(regions[a]) is not None
                                   and branch(regions[a]) == branch(regions[b])
                                   for a, b in diameter_pairs):
                                continue
                            # At most two loaded cycle edges leave each branch.
                            branches = {branch(v) for v in regions} - {None}
                            if any(sum((branch(regions[a]) == b) !=
                                       (branch(regions[c]) == b)
                                       for a, c in cross) > 2 for b in branches):
                                continue
                            rho = sum(labels.count(i) - 1 for i in (1, 2))
                            # Three nonunit hull sides are used. At least
                            # two outer occurrences per such side are reserved.
                            m_b = 3
                            u_b = 3 if require_long_pockets else 0
                            x_b = m_b + u_b
                            bad_bank = x_b + m_b
                            assert rho <= bad_bank
                            assert total <= bad_bank + 1
                            assert total <= (q + x_b) // 2
                            survivor = {'trains': total, 'tree_edges': edges,
                                        'region_labels': labels, 'loaded_regions': regions,
                                        'loaded_word': word, 'physical_sides': selected,
                                        'roles': roles, 'loaded_runs': r, 'rho': rho,
                                        'm_B': m_b, 'x_B': x_b,
                                        'u_B': u_b,
                                        'loaded_witnesses_require_long_pockets': require_long_pockets,
                                        'diameter_pairs': diameter_pairs,
                                        'return_demands': 0,
                                        'omitted': ['source realization', 'positive vertex KKT',
                                                    'actual finite translations',
                                                    'active upper truth tables',
                                                    'prescribed beneficial pins',
                                                    'bulk return endpoints', 'global optimality']}
                            if len(survivors) < 4:
                                survivors.append(survivor)
        if survivors:
            return candidate_count, total, survivors
    return candidate_count, None, []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    parser.add_argument('--max-tree-edges', type=int, default=6)
    args = parser.parse_args()
    horns = horn_checks()
    tree_cases, sharp = check_recurrence(args.max_tree_edges)
    sink_cases, minimum, survivors = smallest_loaded_binary_sink()
    long_cases, long_minimum, long_survivors = smallest_loaded_binary_sink(
        require_long_pockets=True)
    # The minimal unary obstruction survives all these topology/terminal
    # premises and blocks a pin. The token is shared, not counted twice.
    assert closure(1, (), (), (0,), (0,)) is None
    unary = {'trains': 1, 'tree_edges': [[0, 1]], 'region_labels': [0, 1],
             'rhombus_root': 1, 'pin': 1, 'fully_good_trains': 1,
             'bad_terminal_bank': 0, 'inactive_upper_exceptions': 0,
             'source_realization': 'not asserted'}
    output = {'classification': 'exact abstract regressions and finite identities',
              'horn_pinned_checks': horns, 'tree_bank_checks': tree_cases,
              'recurrence_sharp_cases': sharp, 'binary_packets_checked': sink_cases,
              'minimum_loaded_binary_sink_trains': minimum,
              'loaded_binary_survivors': survivors, 'unary_survivor': unary}
    output.update({'strengthened_packets_checked': long_cases,
                   'strengthened_minimum_trains': long_minimum,
                   'strengthened_loaded_survivors': long_survivors,
                   'first_packet_geometric_failure':
                   'u_B=0 makes all nonunit hull intervals two-edge paths; '
                   'their common unit neighbor forbids two moving owners '
                   'in a projective window narrower than pi/3'})
    if args.output:
        args.output.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({k: v for k, v in output.items()
                      if k not in ('loaded_binary_survivors', 'recurrence_sharp_cases',
                                   'strengthened_loaded_survivors')},
                     sort_keys=True))


if __name__ == '__main__':
    main()
