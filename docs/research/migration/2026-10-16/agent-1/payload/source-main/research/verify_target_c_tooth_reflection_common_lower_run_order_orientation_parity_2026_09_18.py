#!/usr/bin/env python3
"""Regression checks for the common-run order/orientation parity refinement."""

from __future__ import annotations


def edge(a: object, b: object) -> frozenset[object]:
    return frozenset((a, b))


def path_edges(path: list[object]) -> set[frozenset[object]]:
    return {edge(path[i], path[i + 1]) for i in range(len(path) - 1)}


def component_count(vertices: set[object], edges: set[frozenset[object]]) -> int:
    adjacency = {v: set() for v in vertices}
    for e in edges:
        a, b = tuple(e)
        adjacency[a].add(b)
        adjacency[b].add(a)

    seen: set[object] = set()
    count = 0
    for start in vertices:
        if start in seen:
            continue
        count += 1
        stack = [start]
        seen.add(start)
        while stack:
            v = stack.pop()
            for w in adjacency[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
    return count


def intersection_component_count(p: list[object], q: list[object]) -> int:
    ep = path_edges(p)
    eq = path_edges(q)
    vi = set(p) & set(q)
    ei = ep & eq
    return component_count(vi, ei)


def union_cycle_rank(p: list[object], q: list[object]) -> int:
    ep = path_edges(p)
    eq = path_edges(q)
    vh = set(p) | set(q)
    eh = ep | eq
    return len(eh) - len(vh) + 1


def check_compatible_same_same() -> None:
    p = [0, 1, 2, 3, 4, 5]
    q = [0, 1, 2, 3, 4, 5]
    assert intersection_component_count(p, q) == 1
    assert union_cycle_rank(p, q) == 0


def check_compatible_opposite_reverse() -> None:
    p = [0, 1, 2, 3, 4, 5]
    q = list(reversed(p))
    assert intersection_component_count(p, q) == 1
    assert union_cycle_rank(p, q) == 0


def check_mismatch_same_reverse() -> None:
    # P sees a-b before c-d. Q sees c-d before a-b, but traverses both
    # selected common edges in the same endpoint direction as P.
    p = ["a", "b", "p", "c", "d"]
    q = ["c", "d", "q", "a", "b"]
    common = path_edges(p) & path_edges(q)
    assert edge("a", "b") in common
    assert edge("c", "d") in common
    assert intersection_component_count(p, q) == 2
    assert union_cycle_rank(p, q) == 1


def check_mismatch_opposite_same() -> None:
    # Both selected edges occur in the same order, but Q traverses each in
    # the endpoint direction opposite to P.
    p = ["a", "b", "p", "c", "d"]
    q = ["b", "a", "q", "d", "c"]
    common = path_edges(p) & path_edges(q)
    assert edge("a", "b") in common
    assert edge("c", "d") in common
    assert intersection_component_count(p, q) == 2
    assert union_cycle_rank(p, q) == 1


def check_scaling_gain() -> None:
    for q in (2, 10, 100, 10_000, 1_000_000):
        mismatch_rank = q - 1
        balanced_rank = q**0.5 - 1
        assert mismatch_rank >= balanced_rank


def main() -> None:
    check_compatible_same_same()
    check_compatible_opposite_reverse()
    check_mismatch_same_reverse()
    check_mismatch_opposite_same()
    check_scaling_gain()
    print("PASS: common-run order/orientation parity certificate")


if __name__ == "__main__":
    main()
