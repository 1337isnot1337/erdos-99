#!/usr/bin/env python3
"""Constructive colored-graph alternative; outputs do not assert realizability."""

if not __debug__:
    raise RuntimeError("Certificate assertions are required; run Python without -O.")

from collections import Counter, deque
from fractions import Fraction


def graph_alternative(n, contacts, diameters):
    """Return balanced edge weights or a half-integral abstract scaling direction.

    Vertex states 2*i and 2*i+1 encode (i,+) and (i,-). The input lists are
    disjoint simple undirected edge sets from an actual source when this helper
    is used geometrically. The helper itself checks only graph data.
    """
    contacts = {tuple(sorted(e)) for e in contacts}
    diameters = {tuple(sorted(e)) for e in diameters}
    if contacts & diameters:
        raise ValueError("Contact and diameter edges must be disjoint (D>1).")
    if not contacts or not diameters:
        raise ValueError("Both active edge sets must be nonempty.")
    if any(i == j or not (0 <= i < j < n) for i, j in contacts | diameters):
        raise ValueError("Edges must have distinct valid endpoints.")
    arcs = [[] for _ in range(2 * n)]
    for color, edges in ((0, contacts), (1, diameters)):
        for i, j in sorted(edges):
            arcs[2 * i + color].append(2 * j + 1 - color)
            arcs[2 * j + color].append(2 * i + 1 - color)
    indegree = [0] * (2 * n)
    for neighbors in arcs:
        for v in neighbors:
            indegree[v] += 1
    queue = deque(i for i, degree in enumerate(indegree) if not degree)
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in arcs[u]:
            indegree[v] -= 1
            if not indegree[v]:
                queue.append(v)
    if len(order) == 2 * n:
        longest = [0] * (2 * n)
        for u in reversed(order):
            longest[u] = max((longest[v] + 1 for v in arcs[u]), default=0)
        z = [Fraction(longest[2 * i] - longest[2 * i + 1], 2) for i in range(n)]
        assert all(z[i] + z[j] >= 1 for i, j in contacts)
        assert all(z[i] + z[j] <= -1 for i, j in diameters)
        return {"kind": "abstract_improvement", "z": z}
    # The residual after source removal has positive indegree at every vertex.
    # Following predecessor arcs therefore finds a genuine directed cycle.
    residual = {i for i, degree in enumerate(indegree) if degree}
    predecessor = {}
    for u in sorted(residual):
        for v in arcs[u]:
            if v in residual:
                predecessor.setdefault(v, u)
    u = min(residual)
    path, seen = [], {}
    while u not in seen:
        seen[u] = len(path)
        path.append(u)
        u = predecessor[u]
    # Reverse the predecessor walk to put every consecutive pair in arc order.
    cycle = list(reversed(path[seen[u]:]))
    assert len(cycle) % 2 == 0
    a, b = Counter(), Counter()
    for u, v in zip(cycle, cycle[1:] + cycle[:1]):
        assert v in arcs[u]
        edge = tuple(sorted((u // 2, v // 2)))
        (a if u % 2 == 0 else b)[edge] += 1
    count = len(cycle) // 2
    a = {edge: Fraction(multiplicity, count) for edge, multiplicity in a.items()}
    b = {edge: Fraction(multiplicity, count) for edge, multiplicity in b.items()}
    assert sum(a.values()) == sum(b.values()) == 1
    for i in range(n):
        assert sum(w for edge, w in a.items() if i in edge) == sum(
            w for edge, w in b.items() if i in edge)
    return {"kind": "factorized_barrier", "cycle": cycle, "a": a, "b": b}


if __name__ == "__main__":
    square = graph_alternative(4, [(0, 1), (1, 2), (2, 3), (0, 3)], [(0, 2), (1, 3)])
    pentagon_center = graph_alternative(6, [(i, 5) for i in range(5)],
                                       [(i, (i + 2) % 5) for i in range(5)])
    print("Square:", square)
    print("Pentagon plus center:", pentagon_center)
    print("Outputs concern abstract endpoint-factor distances, not planar realization.")
