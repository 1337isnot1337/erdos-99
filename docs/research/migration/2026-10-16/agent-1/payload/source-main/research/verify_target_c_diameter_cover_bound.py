#!/usr/bin/env python3
"""Finite checks for the Woodall vertex-cover bound.

This enumerates small odd-unicyclic cycle-plus-pendant-leaf graphs and verifies by
exact subset search that their minimum vertex-cover number is at most ceil(q/2).
It checks only the finite graph arithmetic; it does not prove Woodall's geometric
classification or the inactive-chamber repacking theorem.
"""

from itertools import combinations, product


def edges_odd_unicyclic(r, leaves):
    assert r % 2 == 1 and r >= 3
    edges = {(i, (i + 1) % r) for i in range(r)}
    next_vertex = r
    for i, count in enumerate(leaves):
        for _ in range(count):
            edges.add((i, next_vertex))
            next_vertex += 1
    return next_vertex, tuple(sorted(edges))


def min_vertex_cover(n, edges):
    for size in range(n + 1):
        for chosen in combinations(range(n), size):
            cover = set(chosen)
            if all(u in cover or v in cover for u, v in edges):
                return size
    raise AssertionError("finite graph has no vertex cover")


def main():
    cases = 0
    for r in (3, 5, 7):
        for total_leaves in range(5):
            # Every weak composition of total_leaves among cycle vertices.
            for leaves in product(range(total_leaves + 1), repeat=r):
                if sum(leaves) != total_leaves:
                    continue
                n, edges = edges_odd_unicyclic(r, leaves)
                cover = min_vertex_cover(n, edges)
                assert cover <= (n + 1) // 2
                cases += 1
    assert cases > 0
    print(f"diameter-cover bound: exact checks OK ({cases} odd-unicyclic graphs)")


if __name__ == "__main__":
    main()
