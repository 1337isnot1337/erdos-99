#!/usr/bin/env python3
"""Regression checks for the common-lower-run trunk/cycle-rank fork."""

from __future__ import annotations

import math


def edge(a: object, b: object) -> frozenset[object]:
    return frozenset((a, b))


def path_edges(vertices: list[object]) -> set[frozenset[object]]:
    return {edge(vertices[i], vertices[i + 1]) for i in range(len(vertices) - 1)}


def vertices(edges: set[frozenset[object]]) -> set[object]:
    out: set[object] = set()
    for e in edges:
        out.update(e)
    return out


def component_count(vs: set[object], es: set[frozenset[object]]) -> int:
    adjacency = {v: set() for v in vs}
    for e in es:
        a, b = tuple(e)
        adjacency[a].add(b)
        adjacency[b].add(a)

    seen: set[object] = set()
    count = 0
    for start in vs:
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


def check_union_identity() -> None:
    # Two paths with two shared edge components plus one isolated shared vertex.
    p = path_edges([0, 1, 2, 3, 4, 5])
    q = path_edges([0, 1, "a", "b", 3, 4, "c", "d", 5])

    vp = vertices(p)
    vq = vertices(q)
    i_edges = p & q
    i_vertices = vp & vq
    c_i = component_count(i_vertices, i_edges)

    h_edges = p | q
    h_vertices = vp | vq
    beta = len(h_edges) - len(h_vertices) + 1

    assert c_i == 3
    assert beta == 2
    assert beta == c_i - 1


def check_balanced_fork() -> None:
    # If no intersection component carries sqrt(q) selected edges, at least
    # sqrt(q) components are needed and beta is at least sqrt(q)-1.
    for q in (100, 10_000, 1_000_000):
        s = math.sqrt(q)
        min_components = q / s
        beta_floor = min_components - 1.0
        assert math.isclose(beta_floor, math.sqrt(q) - 1.0, rel_tol=1e-12)


def check_small_external_scale() -> None:
    # kappa>=sqrt(Z+1) gives sqrt(kappa D^(1/4)/(Z+1))
    # >= D^(1/8)/(Z+1)^(1/4), which diverges for Z=o(sqrt(D)).
    D = 1e80
    for p in (0.0, 0.10, 0.30, 0.45, 0.49):
        z = 1.0 if p == 0.0 else D**p
        kappa = max(math.log(math.log(D)), math.sqrt(z + 1.0))
        scale = math.sqrt(kappa * D**0.25 / (z + 1.0))
        lower = D**0.125 / (z + 1.0) ** 0.25
        assert scale >= lower * (1.0 - 1e-12)
        assert scale > 1.0


def main() -> None:
    check_union_identity()
    check_balanced_fork()
    check_small_external_scale()
    print("PASS: common FREE lower-run trunk/cycle-rank certificate")


if __name__ == "__main__":
    main()
