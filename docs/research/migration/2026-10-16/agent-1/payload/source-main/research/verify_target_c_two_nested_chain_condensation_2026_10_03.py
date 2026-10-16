#!/usr/bin/env python3
"""Exact finite check of the two nested-chain condensation lemma.

Assumes: the positive and negative support types each form a strict chain of
nonempty intervals of cuts 1..m, both including [1,m]. An interval [a,b]
creates a->b after replacing a by a-1, with the negative edge reversed.
Proves computationally: for m<=6 every chain pair either is strongly connected
or has a proper contiguous source/sink SCC; strong pairs have identical full
unit-erosion chains. Arithmetic is integer/set/bit arithmetic only.
Does not prove: the unrestricted combinatorial lemma, geometric nesting,
physical source extraction, KKT identities, absence of inactive blockers,
global minimality, C-II, or Level I. Those require the accompanying proof.
"""

from collections import Counter
from functools import lru_cache


@lru_cache(maxsize=None)
def chains(a, b):
    result = [((a, b),)]
    for c in range(a, b + 1):
        for d in range(c, b + 1):
            if (c, d) != (a, b):
                result.extend(((a, b),) + tail for tail in chains(c, d))
    return tuple(result)


def components(m, edges):
    reach = [1 << i for i in range(m + 1)]
    for a, b in edges:
        reach[a] |= 1 << b
    for k in range(m + 1):
        for i in range(m + 1):
            if (reach[i] >> k) & 1:
                reach[i] |= reach[k]
    remaining = set(range(m + 1))
    result = []
    while remaining:
        a = min(remaining)
        comp = {i for i in remaining
                if (reach[a] >> i) & 1 and (reach[i] >> a) & 1}
        result.append(comp)
        remaining -= comp
    return result


def verify(m, positive, negative):
    edges = [(a - 1, b) for a, b in positive]
    edges += [(b, a - 1) for a, b in negative]
    scc = components(m, edges)
    if len(scc) == 1:
        assert positive == negative
        assert len(positive) == m
        assert positive[0] == (1, m)
        assert positive[-1][0] == positive[-1][1]
        assert all((b - a) - (d - c) == 1
                   for (a, b), (c, d) in zip(positive, positive[1:]))
        return "strong"
    labels = {v: i for i, comp in enumerate(scc) for v in comp}
    dag = {(labels[a], labels[b]) for a, b in edges
           if labels[a] != labels[b]}
    interval_extrema = [comp for i, comp in enumerate(scc)
                       if max(comp) - min(comp) + 1 == len(comp)
                       and (not any(b == i for a, b in dag)
                            or not any(a == i for a, b in dag))]
    assert interval_extrema, (m, positive, negative, scc, dag)
    assert all(len(comp) < m + 1 for comp in interval_extrema)
    return "interval_extremum"


def main():
    checked = 0
    for m in range(1, 7):
        chain_set = chains(1, m)
        census = Counter(verify(m, p, n) for p in chain_set for n in chain_set)
        count = len(chain_set) ** 2
        checked += count
        assert census["strong"] == 2 ** (m - 1)
        print(f"m={m}: chains={len(chain_set)}, pairs={count}, "
              f"strong={census['strong']}, "
              f"interval_extremum={census['interval_extremum']}")
    assert checked == 171538
    print(f"PASS: {checked} exact chain pairs; no geometric/global claim.")


if __name__ == "__main__":
    main()
