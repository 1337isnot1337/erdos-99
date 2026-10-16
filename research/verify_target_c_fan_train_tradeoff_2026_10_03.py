#!/usr/bin/env python3
"""Exact bounded graph audit of the fan/train matching tradeoff.

Assumes only Woodall's abstract caterpillar/odd-cycle-with-leaves types.
Exhausts every simple graph with 2..6 labeled vertices, retaining no-isolate
graphs of those types. Checks pendant-block count >= h-3nu and d_H<=nu.
Also checks exact finite ledger elimination and a rational pi lower margin.
Does not certify hull embeddings, train injection, global minimizers, C-II,
or Level I. Those are analytic hypotheses/proofs in the associated report.
"""

from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations


def graph_check(n, edge_mask, pairs):
    adj = [0] * n
    edges = []
    for i, (u, v) in enumerate(pairs):
        if edge_mask >> i & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
            edges.append((u, v))
    if any(not row for row in adj):
        return False
    deg = [row.bit_count() for row in adj]
    unseen = set(range(n))
    components = []
    while unseen:
        stack = [unseen.pop()]
        comp = set(stack)
        while stack:
            u = stack.pop()
            for v in range(n):
                if adj[u] >> v & 1 and v in unseen:
                    unseen.remove(v)
                    comp.add(v)
                    stack.append(v)
        components.append(comp)
    h = len(edges)
    forest = h == n - len(components)
    if forest:
        # Removing leaves leaves disjoint paths, possibly empty.
        core = {u for u in range(n) if deg[u] > 1}
        if any(sum(bool(adj[u] >> v & 1) for v in core) > 2 for u in core):
            return False
    else:
        if len(components) != 1 or h != n:
            return False
        core = {u for u in range(n) if deg[u] > 1}
        if len(core) % 2 != 1 or len(core) < 3:
            return False
        if any(sum(bool(adj[u] >> v & 1) for v in core) != 2 for u in core):
            return False

    @lru_cache(None)
    def matching(mask):
        if not mask:
            return 0
        bit = mask & -mask
        u = bit.bit_length() - 1
        rest = mask ^ bit
        value = matching(rest)
        neighbors = adj[u] & rest
        while neighbors:
            other = neighbors & -neighbors
            value = max(value, 1 + matching(rest ^ other))
            neighbors ^= other
        return value

    nu = matching((1 << n) - 1)
    pendant = [(u, v) for u, v in edges
               if (deg[u] == 1 and deg[v] > 1) or
               (deg[v] == 1 and deg[u] > 1)]
    carriers = {u if deg[u] > 1 else v for u, v in pendant}
    fan_adjacencies = len(pendant) - len(carriers)
    assert fan_adjacencies >= h - 3 * nu
    assert 0 <= n - h <= nu
    return True


def main():
    accepted = total = 0
    for n in range(2, 7):
        pairs = list(combinations(range(n), 2))
        count = 0
        for mask in range(1 << len(pairs)):
            total += 1
            count += bool(graph_check(n, mask, pairs))
        accepted += count
        print(f'n={n}: {count} accepted Woodall-type labeled graphs')

    # Exact ledger implication in a bounded integer universe; no embedding claim.
    ledger_cases = 0
    for q in range(2, 31):
        for x in range(0, 9):
            for k in range(0, (q - x) // 2 + 1):
                Q = q - x - 2 * k
                for d_H in range(k + 1):
                    for nu in range(d_H, q // 2 + 1):
                        s_Z = k - d_H
                        if s_Z <= 2 * Q + 3 * nu + x:
                            assert 3 * q + x <= 5 * (q - k) + 3 * nu + d_H
                            assert 3 * q + x <= 5 * (q - k) + 4 * nu
                            ledger_cases += 1
    endpoint_cases = 0
    for q in range(2, 31):
        for x in range(9):
            for k in range(max(0, (q - x) // 2 + 1)):
                Q = q - x - 2 * k
                for f in range(Q + 1):
                    trains = q - k + 2 * f
                    slack = 2 * x + 4 * f + Q - (trains - 2)
                    if slack < 0:
                        continue
                    assert 5 * (q - k) + 2 - 3 * q - x == slack + 2 * (Q - f)
                    assert 5 * (q - k) + 2 >= 3 * q + x
                    endpoint_cases += 1
    # Analytic pi>3.14 supplies an exact positive weaker asymptotic margin.
    pi_lower = F(157, 50)
    t_upper = F(93, 50)
    assert 3 * pi_lower - 5 * t_upper == F(3, 25)
    print(f'PASS: {accepted}/{total} graph types; {ledger_cases} exact ledger cases; '
          f'{endpoint_cases} good-end/slack cases; '
          'rational margin 3/25 (using pi>157/50).')


if __name__ == '__main__':
    main()
