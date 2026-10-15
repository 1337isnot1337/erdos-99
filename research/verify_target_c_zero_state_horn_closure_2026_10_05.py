#!/usr/bin/env python3
"""Exhaustive zero-valid 2-CNF closure certificates, n<=3.

Certifies finite Boolean logic only. No source geometry, motion extraction,
KKT, feasibility of a particular C-II source, or Level I closure is encoded.
"""
from itertools import product


def reachability(n, implications):
    reach = [{i} for i in range(n)]
    for i, j in implications:
        reach[i].add(j)
    for k in range(n):
        for i in range(n):
            if k in reach[i]:
                reach[i].update(reach[k])
    return reach


def models(n, forbidden, implications, conflicts):
    return [bits for bits in product((0, 1), repeat=n)
            if not any(bits[i] for i in forbidden)
            and not any(bits[i] and not bits[j] for i, j in implications)
            and not any(bits[i] and bits[j] for i, j in conflicts)]


def closure_test(reach, forbidden, conflicts, true, false):
    closure = set().union(*(reach[i] for i in true)) if true else set()
    valid = not closure.intersection(set(forbidden) | set(false))
    valid &= not any(i in closure and j in closure for i, j in conflicts)
    return valid, closure


def sink_test(n, reach, forbidden, conflicts):
    classes = []
    pending = set(range(n))
    while pending:
        i = min(pending)
        block = {j for j in pending if j in reach[i] and i in reach[j]}
        classes.append(block)
        pending.difference_update(block)
    for block in classes:
        if not all(reach[i] <= block for i in block):
            continue
        if block.intersection(forbidden):
            continue
        if any(i in block and j in block for i, j in conflicts):
            continue
        return True
    return False


def main():
    formula_count = pin_count = 0
    for n in range(4):
        clauses = ([('z', i, i) for i in range(n)]
                   + [('i', i, j) for i in range(n) for j in range(n) if i != j]
                   + [('c', i, j) for i in range(n) for j in range(i + 1, n)])
        for mask in range(1 << len(clauses)):
            chosen = [c for k, c in enumerate(clauses) if mask & (1 << k)]
            forbidden = {i for kind, i, j in chosen if kind == 'z'}
            implications = [(i, j) for kind, i, j in chosen if kind == 'i']
            conflicts = [(i, j) for kind, i, j in chosen if kind == 'c']
            reach = reachability(n, implications)
            exact_models = models(n, forbidden, implications, conflicts)
            assert (0,) * n in exact_models
            assert sink_test(n, reach, forbidden, conflicts) == any(any(b) for b in exact_models)
            for pins in product((-1, 0, 1), repeat=n):
                true = {i for i, v in enumerate(pins) if v == 1}
                false = {i for i, v in enumerate(pins) if v == 0}
                valid, closure = closure_test(reach, forbidden, conflicts, true, false)
                brute = any(all(pins[i] == -1 or pins[i] == bits[i] for i in range(n))
                            for bits in exact_models)
                assert valid == brute
                if valid:
                    assert tuple(int(i in closure) for i in range(n)) in exact_models
                pin_count += 1
            formula_count += 1
    cycle = [(0, 1), (1, 2), (2, 0)]
    assert models(3, set(), cycle, []) == [(0, 0, 0), (1, 1, 1)]
    assert len(models(3, set(), [], [(0, 1), (1, 2), (0, 2)])) == 4
    assert not closure_test(reachability(3, [(0, 1), (0, 2)]), set(), [(1, 2)], {0}, set())[0]
    print(f'PASS: {formula_count} zero-valid formulas; {pin_count} exact pinned closure comparisons; sink tests; harmless cycles and blocking fork')
    print('OMITTED: source geometry, owner extraction, old diameter shortening, C-II and Level I closure')


if __name__ == '__main__':
    main()
