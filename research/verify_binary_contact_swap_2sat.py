#!/usr/bin/env python3
"""Exact simultaneous finite source translations compiled to 2-SAT.

Input JSON: {"points": [["x", "y"], ...], "moves": [
{"indices": [1, 2], "delta": ["dx", "dy"]}, ...]}.
All coordinate strings must be rational; moved index sets must be disjoint.
Every old contact must stay exactly unit for ALL binary move choices. The
compiler checks this requirement. It retains every source point and encodes
all old inactive lower and upper distance inequalities strictly. An escape
must strictly shorten at least one old diameter. Such an escape is either a
strict diameter competitor or a same-contact source with fewer diameters.

A negative result concerns only the supplied finite move family. It does not
prove global optimality. No KKT/source-extraction hypothesis is inferred.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import combinations, product
import json
from pathlib import Path


def squared(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def solve_2sat(variable_count, clauses, pins=()):
    """Literal node 2*i+b means x_i=b. Return model or None."""
    size = 2 * variable_count
    graph, reverse = [[] for _ in range(size)], [[] for _ in range(size)]
    all_clauses = list(clauses) + [(2 * i + b,) for i, b in pins]
    for clause in all_clauses:
        if not clause:
            return None
        a, b = clause[0], clause[-1]
        for source, target in ((a ^ 1, b), (b ^ 1, a)):
            graph[source].append(target)
            reverse[target].append(source)
    seen, order = set(), []
    for root in range(size):
        if root in seen:
            continue
        seen.add(root)
        stack = [(root, iter(graph[root]))]
        while stack:
            node, children = stack[-1]
            try:
                child = next(children)
            except StopIteration:
                stack.pop()
                order.append(node)
                continue
            if child not in seen:
                seen.add(child)
                stack.append((child, iter(graph[child])))
    components = [-1] * size
    component = 0
    for root in reversed(order):
        if components[root] >= 0:
            continue
        components[root] = component
        stack = [root]
        while stack:
            node = stack.pop()
            for child in reverse[node]:
                if components[child] < 0:
                    components[child] = component
                    stack.append(child)
        component += 1
    if any(components[2 * i] == components[2 * i + 1] for i in range(variable_count)):
        return None
    model = tuple(int(components[2 * i + 1] > components[2 * i])
                  for i in range(variable_count))
    assert all(any(model[node // 2] == node % 2 for node in clause)
               for clause in all_clauses)
    return model


def identical_translation_closure(moves, forbidden):
    """Exact return paths for equal deltas; final node len(moves) is fixed false."""
    if not moves or any(delta != moves[0][1] for _, delta in moves):
        return None
    fixed = len(moves)
    reverse = [[] for _ in range(fixed + 1)]
    for _, _, bits, _ in forbidden:
        if len(bits) == 1:
            (source, bit), = bits
            assert bit == 1
            target = fixed
        else:
            assert len(bits) == 2 and bits[0][1] != bits[1][1]
            source = next(index for index, bit in bits if bit == 1)
            target = next(index for index, bit in bits if bit == 0)
        reverse[target].append(source)
    parent = {fixed: None}
    pending = [fixed]
    while pending:
        target = pending.pop()
        for source in reverse[target]:
            if source not in parent:
                parent[source] = target
                pending.append(source)
    paths = {}
    for source in sorted(parent):
        if source == fixed:
            continue
        path, node = [source], source
        while node != fixed:
            node = parent[node]
            path.append(node)
        paths[source] = path
    return {'fixed_false_node': fixed, 'return_paths': paths,
            'maximal_closed_model': tuple(int(i not in parent) for i in range(fixed))}


def horn_zero_closure(variable_count, clauses):
    """Least positive closures and exact certificates for a zero-satisfiable 2-CNF.

    Positive node 2*i+1 means x_i=1. Every clause contains a negative literal,
    since zero is a model. The possible constraints are i->j, forced i=0,
    and not(i and j). Return a feasible nonzero model or a path/branching
    obstruction for EACH proposed positive variable. This does not assert that
    a nonzero model shortens a diameter; that is checked separately.
    """
    graph = [set() for _ in range(variable_count)]
    forced_zero, conflicts = set(), set()
    for clause in clauses:
        clause = tuple(sorted(set(clause)))
        if not clause or all(node % 2 for node in clause):
            raise ValueError('the all-zero assignment must satisfy every clause')
        if len(clause) == 1:
            forced_zero.add(clause[0] // 2)
        elif len(clause) == 2:
            negative = [node // 2 for node in clause if node % 2 == 0]
            positive = [node // 2 for node in clause if node % 2 == 1]
            if positive:
                graph[negative[0]].add(positive[0])
            else:
                conflicts.add(tuple(negative))
        else:
            raise ValueError('only clauses of size at most two are supported')

    feasible, obstructions = {}, {}
    for root in range(variable_count):
        parent, pending = {root: None}, [root]
        while pending:
            source = pending.pop()
            for target in sorted(graph[source]):
                if target not in parent:
                    parent[target] = source
                    pending.append(target)

        def path(target):
            result = [target]
            while parent[result[-1]] is not None:
                result.append(parent[result[-1]])
            return list(reversed(result))

        zero_hit = next((node for node in sorted(forced_zero) if node in parent), None)
        conflict_hit = next((pair for pair in sorted(conflicts)
                             if all(node in parent for node in pair)), None)
        if zero_hit is not None:
            obstructions[root] = {'forced_zero': zero_hit, 'path': path(zero_hit)}
        elif conflict_hit is not None:
            obstructions[root] = {'incompatible_pair': conflict_hit,
                                  'paths': [path(node) for node in conflict_hit]}
        else:
            model = tuple(int(node in parent) for node in range(variable_count))
            assert all(any(model[node // 2] == node % 2 for node in clause)
                       for clause in clauses)
            feasible[root] = model
    return {'implications': [sorted(targets) for targets in graph],
            'forced_zero': sorted(forced_zero), 'incompatible_pairs': sorted(conflicts),
            'least_nonzero_models': feasible, 'obstructions': obstructions,
            'zero_is_unique': len(obstructions) == variable_count}


def compile_source(points, moves):
    if len(points) < 2:
        raise ValueError('at least two source points are required')
    if any(len(point) != 2 for point in points):
        raise ValueError('source coordinates must be planar')
    owner = [None] * len(points)
    for move_index, (indices, delta) in enumerate(moves):
        if len(delta) != 2 or not indices:
            raise ValueError('each move needs a nonempty index set and a planar delta')
        for index in indices:
            if not 0 <= index < len(points) or owner[index] is not None:
                raise ValueError('move index sets must be valid and disjoint')
            owner[index] = move_index
    old = {(i, j): squared(points[i], points[j])
           for i, j in combinations(range(len(points)), 2)}
    if min(old.values()) < 1:
        raise ValueError('source is not unit-separated')
    diameter_squared = max(old.values())
    clauses, shortenings, forbidden = [], [], []

    def moved(index, bits):
        move = owner[index]
        if move is None or not bits[move]:
            return points[index]
        delta = moves[move][1]
        return tuple(x + y for x, y in zip(points[index], delta))

    for (i, j), distance in old.items():
        variables = sorted({owner[index] for index in (i, j) if owner[index] is not None})
        for choices in product((0, 1), repeat=len(variables)):
            bits = dict(zip(variables, choices))
            new_distance = squared(moved(i, bits), moved(j, bits))
            if distance == 1 and new_distance != 1:
                raise ValueError(f'contact {i},{j} is not preserved under pattern {bits}')
            feasible = (new_distance == 1 if distance == 1 else new_distance > 1)
            feasible &= (new_distance <= diameter_squared if distance == diameter_squared
                         else new_distance < diameter_squared)
            if not feasible:
                # Forbid a local pattern: OR_i (x_i != choices_i).
                clauses.append(tuple(2 * index + 1 - bit for index, bit in bits.items()))
                forbidden.append((i, j, tuple(bits.items()), new_distance))
            elif distance == diameter_squared and new_distance < diameter_squared:
                shortenings.append(((i, j), tuple(bits.items())))

    assert solve_2sat(len(moves), clauses, tuple((i, 0) for i in range(len(moves)))) is not None
    horn = horn_zero_closure(len(moves), clauses)
    closure = identical_translation_closure(moves, forbidden)
    if closure is not None:
        maximal = closure['maximal_closed_model']
        assert all(any(maximal[node // 2] == node % 2 for node in clause) for clause in clauses)

    def verify(model):
        new_points = [moved(index, dict(enumerate(model))) for index in range(len(points))]
        new = {(i, j): squared(new_points[i], new_points[j]) for i, j in old}
        assert min(new.values()) >= 1
        assert all(new[pair] == 1 for pair in old if old[pair] == 1)
        assert all(new[pair] > 1 for pair in old if old[pair] > 1)
        assert all(new[pair] < diameter_squared for pair in old if old[pair] < diameter_squared)
        assert all(new[pair] <= diameter_squared for pair in old)
        assert any(new[pair] < diameter_squared for pair in old if old[pair] == diameter_squared)
        return new_points, max(new.values())

    for shortened_pair, pins in shortenings:
        model = solve_2sat(len(moves), clauses, pins)
        if model is not None:
            new_points, new_diameter_squared = verify(model)
            return {'model': model, 'old_D2': diameter_squared, 'new_D2': new_diameter_squared,
                    'shortened_pair': shortened_pair, 'points': new_points,
                    'clause_count': len(clauses), 'forbidden': forbidden,
                    'identical_translation_closure': closure, 'horn_zero_closure': horn}
    return {'model': None, 'old_D2': diameter_squared, 'clause_count': len(clauses),
            'forbidden': forbidden, 'identical_translation_closure': closure,
            'horn_zero_closure': horn}


def brute_escape(points, moves):
    old = {(i, j): squared(points[i], points[j])
           for i, j in combinations(range(len(points)), 2)}
    maximum = max(old.values())
    for bits in product((0, 1), repeat=len(moves)):
        changed = list(points)
        for bit, (indices, delta) in zip(bits, moves):
            if bit:
                for index in indices:
                    changed[index] = tuple(x + y for x, y in zip(changed[index], delta))
        new = {pair: squared(changed[pair[0]], changed[pair[1]]) for pair in old}
        if all((new[pair] == 1 if value == 1 else new[pair] > 1)
               and (new[pair] <= maximum if value == maximum else new[pair] < maximum)
               for pair, value in old.items()):
            if any(new[pair] < maximum for pair, value in old.items() if value == maximum):
                return bits
    return None


def regression_suite():
    swap_points = [(Q(0), Q(0)), (Q(1), Q(0)), (Q(8, 5), Q(4, 5)),
                   (Q(-4, 5), Q(12, 5))]
    rectangle = [(Q(0), Q(0)), (Q(1), Q(0)), (Q(0), Q(3)), (Q(1), Q(3))]
    cases = [
        ('actual two-contact finite swap', swap_points, [([1], (Q(-2, 5), Q(4, 5)))]),
        ('two independent compatible moves', rectangle,
         [([0, 1], (Q(0), Q(1, 2))), ([2, 3], (Q(0), Q(-1, 2)))]),
        ('diameter compensation implication', rectangle,
         [([0, 1], (Q(0), Q(1, 2))), ([2, 3], (Q(0), Q(1, 2)))]),
        ('all nonzero patterns blocked', rectangle,
         [([0, 1], (Q(0), Q(-1, 2))), ([2, 3], (Q(0), Q(1, 2)))]),
        ('new unit contacts excluded by strict inactive policy', rectangle,
         [([0, 1], (Q(0), Q(2)))]),
    ]
    for name, points, moves in cases:
        result = compile_source(points, moves)
        brute = brute_escape(points, moves)
        assert (result['model'] is None) == (brute is None)
        if name == 'diameter compensation implication':
            assert result['identical_translation_closure']['maximal_closed_model'] == (1, 1)
        if name == 'new unit contacts excluded by strict inactive policy':
            assert result['identical_translation_closure']['return_paths'] == {0: [0, 1]}
        print(f'PASS: {name}; clauses={result["clause_count"]}; escape={result["model"]}')
    # Meaningful independent solver check: every 2-CNF over two variables
    # with up to three clauses, including units, checked by brute force.
    possible = [(node,) for node in range(4)] + list(combinations(range(4), 2))
    checked = 0
    for count in range(4):
        for clauses in combinations(possible, count):
            brute = next((bits for bits in product((0, 1), repeat=2)
                          if all(any(bits[node // 2] == node % 2 for node in clause)
                                 for clause in clauses)), None)
            model = solve_2sat(2, clauses)
            assert (model is None) == (brute is None)
            checked += 1
    print(f'PASS: {checked} independently enumerated two-variable clause systems')
    # All 4096 zero-satisfiable Horn systems on three variables; an independent
    # truth-table check tests every positive closure and its obstruction.
    horn_clauses = [(2 * i,) for i in range(3)]
    horn_clauses += [(2 * i, 2 * j + 1) for i in range(3) for j in range(3) if i != j]
    horn_clauses += [(2 * i, 2 * j) for i, j in combinations(range(3), 2)]
    checked = 0
    for selection in product((0, 1), repeat=len(horn_clauses)):
        clauses = [clause for bit, clause in zip(selection, horn_clauses) if bit]
        certificate = horn_zero_closure(3, clauses)
        models = [bits for bits in product((0, 1), repeat=3)
                  if all(any(bits[node // 2] == node % 2 for node in clause)
                         for clause in clauses)]
        assert certificate['zero_is_unique'] == (len(models) == 1)
        for root in range(3):
            positive_models = [bits for bits in models if bits[root]]
            assert (root in certificate['least_nonzero_models']) == bool(positive_models)
            if positive_models:
                least = certificate['least_nonzero_models'][root]
                assert all(all(a <= b for a, b in zip(least, bits)) for bits in positive_models)
        checked += 1
    print(f'PASS: {checked} independently enumerated three-variable Horn systems')
    try:
        compile_source(rectangle, [([0], (Q(1, 2), Q(0)))])
    except ValueError:
        print('PASS: non-contact-preserving move rejected')
    else:
        raise AssertionError('invalid contact motion accepted')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path)
    args = parser.parse_args()
    if args.source is None:
        regression_suite()
        return
    data = json.loads(args.source.read_text())
    values = [value for point in data['points'] for value in point]
    values += [value for move in data['moves'] for value in move['delta']]
    if any(type(value) not in (str, int) for value in values):
        raise ValueError('coordinates must be rational strings or integers; floats are not accepted')
    points = [tuple(Q(value) for value in point) for point in data['points']]
    moves = [(move['indices'], tuple(Q(value) for value in move['delta']))
             for move in data['moves']]
    result = compile_source(points, moves)
    print(json.dumps({key: value for key, value in result.items() if key != 'forbidden'},
                     default=str, indent=2))


if __name__ == '__main__':
    main()
