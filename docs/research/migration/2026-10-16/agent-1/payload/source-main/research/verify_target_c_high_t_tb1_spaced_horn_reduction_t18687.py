#!/usr/bin/env python3
from itertools import product

# Regression checks for the directed-closure/Horn normal form on the
# 15-spaced exact-swap subsystem.


def sccs(n, arcs):
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for u, v in arcs:
        adj[u].append(v)
        radj[v].append(u)

    seen = [False] * n
    order = []

    def dfs(u):
        seen[u] = True
        for v in adj[u]:
            if not seen[v]:
                dfs(v)
        order.append(u)

    for u in range(n):
        if not seen[u]:
            dfs(u)

    comp = [-1] * n
    comps = []

    def rdfs(u, c):
        comp[u] = c
        comps[c].append(u)
        for v in radj[u]:
            if comp[v] < 0:
                rdfs(v, c)

    for u in reversed(order):
        if comp[u] < 0:
            comps.append([])
            rdfs(u, len(comps) - 1)

    return comp, comps


# 1. Exhaustively verify the local truth-table encoding.
# States are bitmasks 10=1, 01=2, 11=3.  State 00 is strict/safe initially.
# Joint-only bad {11} is the pattern removed by the previous theorem.
states = (1, 2, 3)
for bmask in range(1 << 3):
    bad = {states[k] for k in range(3) if (bmask >> k) & 1}
    if 3 in bad and 1 not in bad and 2 not in bad:
        continue

    forbidden = set()
    implications = []

    if 1 in bad:
        if 3 in bad:
            forbidden.add(0)
        else:
            implications.append((0, 1))

    if 2 in bad:
        if 3 in bad:
            forbidden.add(1)
        else:
            implications.append((1, 0))

    for state in states:
        chosen = {i for i in range(2) if (state >> i) & 1}
        graph_safe = chosen.isdisjoint(forbidden) and all(
            u not in chosen or v in chosen for u, v in implications
        )
        metric_safe = state not in bad
        assert graph_safe == metric_safe, (
            bad,
            forbidden,
            implications,
            state,
        )


# 2. Verify the global graph lemma:
# nonempty out-closed F-free set <=> F-free sink SCC.
# Full exhaustive digraph enumeration through n=3, plus a deterministic
# sample of n=4 digraphs; all forbidden sets are exhaustive.
for n in range(1, 5):
    possible = [(u, v) for u in range(n) for v in range(n) if u != v]
    masks = range(1 << len(possible)) if n <= 3 else range(0, 1 << len(possible), 97)

    for mask in masks:
        arcs = [edge for k, edge in enumerate(possible) if (mask >> k) & 1]
        comp, comps = sccs(n, arcs)

        has_out = [False] * len(comps)
        for u, v in arcs:
            if comp[u] != comp[v]:
                has_out[comp[u]] = True
        sinks = [set(comps[c]) for c in range(len(comps)) if not has_out[c]]

        for fmask in range(1 << n):
            forbidden = {i for i in range(n) if (fmask >> i) & 1}
            free_sink_exists = any(C.isdisjoint(forbidden) for C in sinks)

            closed_exists = False
            for smask in range(1, 1 << n):
                S = {i for i in range(n) if (smask >> i) & 1}
                if not S.isdisjoint(forbidden):
                    continue
                if all(u not in S or v in S for u, v in arcs):
                    closed_exists = True
                    break

            assert free_sink_exists == closed_exists

print("PASS: 15-spaced TB1 Horn/implication reduction regressions")
