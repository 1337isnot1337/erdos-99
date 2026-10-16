#!/usr/bin/env python3
"""Finite graph/contact checks for original dirty-worktree23 preservation.

Exhaustive four-label graphs check endpoint-inclusive linkage composition.
Simple-path set packing and independent vertex-cut enumeration are separate
oracles. A seven-label unit-contact tree attains the factor two and has an
explicit smaller-diameter competitor. No canonical-source or Level I claim.
"""
if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from functools import lru_cache
from itertools import combinations, product


def reachable(graph, starts, deleted):
    seen = starts & ~deleted
    todo = [v for v in range(len(graph)) if seen & (1 << v)]
    while todo:
        v = todo.pop()
        new = graph[v] & ~seen & ~deleted
        seen |= new
        todo.extend(w for w in range(len(graph)) if new & (1 << w))
    return seen


def cut_value(graph, sources, targets):
    return min(deleted.bit_count() for deleted in range(1 << len(graph))
               if not reachable(graph, sources, deleted) & targets)


def path_packing(graph, sources, targets):
    masks = set()
    def visit(v, used):
        if targets & (1 << v):
            masks.add(used)
            return
        for w in range(len(graph)):
            if graph[v] & (1 << w) and not used & (1 << w):
                visit(w, used | (1 << w))
    for v in range(len(graph)):
        if sources & (1 << v):
            visit(v, 1 << v)
    @lru_cache(None)
    def pack(used):
        return max([0]+[1+pack(used | path) for path in masks if not path & used])
    return pack(0)


def exhaustive_four_labels():
    pairs = list(combinations(range(4), 2))
    # Roles: neither, attachment, source, target, source-and-target.
    cases = []
    for roles in product(range(5), repeat=4):
        attachment = sum(1 << v for v, role in enumerate(roles) if role == 1)
        sources = sum(1 << v for v, role in enumerate(roles) if role in (2, 4))
        targets = sum(1 << v for v, role in enumerate(roles) if role in (3, 4))
        assert not attachment & (sources | targets)
        cases.append((sources, attachment, targets))
    checked = overlaps = positive = oracle_pairs = 0
    for edge_mask in range(64):
        graph = [0]*4
        for i, (v, w) in enumerate(pairs):
            if edge_mask & (1 << i):
                graph[v] |= 1 << w
                graph[w] |= 1 << v
        table = {}
        for sources in range(16):
            for targets in range(16):
                value = path_packing(graph, sources, targets)
                assert value == cut_value(graph, sources, targets)
                table[sources, targets] = value
                oracle_pairs += 1
        for sources, attachment, targets in cases:
            r, s = table[sources, attachment], table[attachment, targets]
            actual = table[sources, targets]
            excess = r+s-attachment.bit_count()
            assert 2*actual >= excess
            assert 3*actual >= excess  # original weaker bound is preserved
            checked += 1
            overlaps += bool(sources & targets)
            positive += excess > 0
    return checked, overlaps, positive, oracle_pairs


def sharp_contact_fixture():
    # A is an abstract attachment set here, not actual diameter loading.
    points = [(-2, 0), (0, 1), (-1, 0), (1, 0), (0, -1), (2, 0), (0, 0)]
    contacts, graph, distances = set(), [0]*7, []
    for v, w in combinations(range(7), 2):
        squared = sum((a-b)**2 for a, b in zip(points[v], points[w]))
        assert squared >= 1
        distances.append(squared)
        if squared == 1:
            contacts.add((v, w))
            graph[v] |= 1 << w
            graph[w] |= 1 << v
    expected = {(0, 2), (1, 6), (2, 6), (3, 6), (3, 5), (4, 6)}
    assert contacts == expected and max(distances) == 16
    assert not any(all(tuple(sorted(e)) in contacts for e in combinations(t, 2))
                   for t in combinations(range(7), 3))
    sources, attachment, targets = (1 << 0) | (1 << 1), (1 << 2) | (1 << 3), (1 << 4) | (1 << 5)
    assert path_packing(graph, sources, attachment) == 2
    assert path_packing(graph, attachment, targets) == 2
    assert path_packing(graph, sources, targets) == cut_value(graph, sources, targets) == 1
    assert not reachable(graph, sources, 1 << 6) & targets
    # Reject dropping the factor two or composing merely from path counts.
    assert 1 < min(2, 2) and 2*1 == 2+2-attachment.bit_count()
    competitor = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2)]
    values = [sum((a-b)**2 for a, b in zip(p, q)) for p, q in combinations(competitor, 2)]
    assert len(values) == len(distances) == 21
    assert min(values) == 1 and max(values) == 8 < 16
    return len(distances), len(contacts)


if __name__ == "__main__":
    checked, overlaps, positive, oracle_pairs = exhaustive_four_labels()
    pairs, contacts = sharp_contact_fixture()
    print(f"PASS: {checked} linkage triples on all64 four-label graphs; "
          f"{overlaps} overlapping-terminal cases; {positive} positive-excess cases")
    print(f"PASS: {oracle_pairs} independent path-packing/vertex-cut comparisons")
    print(f"PASS: sharp seven-label contact fixture, {pairs} pairs/{contacts} contacts, "
          "and all21 smaller-competitor pairs")
    print("SCOPE: finite graph/contact regressions; canonical cell access, universal "
          "composition and endpoint-cut arguments require the analytic proofs")
