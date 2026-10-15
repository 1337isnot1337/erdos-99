#!/usr/bin/env python3
"""Exact graph partition and rational geometric forest-dispatch regression.

Graph universe: all simple graphs T on 2..5 labeled vertices with total cycle
rank <=1, and every nonempty forest subgraph H. Isolated vertices are allowed.
The graph result is more general than straight-line thrackles; geometric
realizability, source contacts/KKT, and global optimality are not encoded.
All binary labels of B=V(H) check protection of every nonexceptional new edge.
The rational triangle checks necessity of an upper-distance exception even at
amplitude <1/(2D). It is not a global minimizer.
"""

from fractions import Fraction as F
from itertools import combinations, product


class Partition:
    def __init__(self, n):
        self.parent = list(range(n))
        self.mark = [None] * n

    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def join(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.parent[b] = a
        self.mark[a] = self.mark[a] if self.mark[a] is not None else self.mark[b]
        return True


def partition(n, t, h):
    t, h = set(t), set(h)
    d = Partition(n)
    for a, b in h:
        assert d.join(a, b)
    bset = {v for e in h for v in e}
    c = len(bset) - len(h)
    for v in bset:
        d.mark[d.find(v)] = d.find(v)
    exceptional = set()
    for a, b in sorted(t - h):
        x, y = d.find(a), d.find(b)
        if x == y or (d.mark[x] is not None and d.mark[y] is not None):
            exceptional.add((a, b))
        else:
            d.join(a, b)
    # A source anchor for each new vertex. Traversal never crosses an old B vertex.
    neighbors = [[] for _ in range(n)]
    for a, b in t - exceptional:
        neighbors[a].append(b)
        neighbors[b].append(a)
    anchor = {v: v for v in bset}
    queue = list(bset)
    for a in queue:
        for b in neighbors[a]:
            if b in bset:
                continue
            if b in anchor:
                assert anchor[b] == anchor[a]
            else:
                anchor[b] = anchor[a]
                queue.append(b)
    for a, b in t - h - exceptional:
        assert anchor.get(a) == anchor.get(b)
    return exceptional, anchor, bset, c


def graph_checks():
    packets = labels = 0
    for n in range(2, 6):
        possible = list(combinations(range(n), 2))
        for size in range(1, n + 1):
            for t in combinations(possible, size):
                d = Partition(n)
                cycle_rank = sum(not d.join(a, b) for a, b in t)
                if cycle_rank > 1:
                    continue
                for mask in range(1, 1 << size):
                    h = [t[i] for i in range(size) if mask >> i & 1]
                    old = Partition(n)
                    if any(not old.join(a, b) for a, b in h):
                        continue
                    exceptional, anchor, bset, c = partition(n, t, h)
                    assert exceptional <= set(t) - set(h)
                    assert len(exceptional) <= c - 1 + cycle_rank
                    for bits in product((0, 1), repeat=len(bset)):
                        core = dict(zip(sorted(bset), bits))
                        moved = {v: core[anchor[v]] if v in anchor else 0 for v in range(n)}
                        assert all(moved[a] == moved[b]
                                   for a, b in set(t) - set(h) - exceptional)
                        labels += 1
                    packets += 1
    print(f"PASS: graph_packets={packets}; binary_label_checks={labels}")


def triangle_regression():
    p = [(F(0), F(0)), (F(8), F(0)), (F(3608, 901), F(6240, 901))]
    delta = (F(-1, 1000), F(-1, 100))
    dist = lambda a, b: sum((x - y) ** 2 for x, y in zip(a, b))
    assert dist(p[0], p[1]) == dist(p[0], p[2]) == 64
    assert 63 < dist(p[1], p[2]) < 64
    s2 = sum(x * x for x in delta)
    assert s2 < F(1, 256)  # s<1/(2D)<D-sqrt(D^2-1).
    moved = (p[1][0] + delta[0], p[1][1] + delta[1])
    assert dist(p[0], moved) < 64
    assert dist(p[2], moved) > 64
    assert min(dist(a, b) for a, b in combinations(p, 2)) > 1
    ex, _, _, c = partition(3, [(0, 1), (0, 2), (1, 2)], [(0, 1), (0, 2)])
    assert c == 1 and ex == {(1, 2)}
    print("PASS: rational forest source needs its one exceptional upper pair")


def weighted_difference_checks():
    """Full finite comparison with a quarter-grid feasibility oracle.

    Universe: 1..4 variables, all orientations/subsets of unordered arcs,
    fixed cyclic-by-index costs 1/4,1/2,2, all prescriptions free/0/1.
    Quarter-grid feasibility is complete for these rational difference systems:
    shortest-path potentials are on that grid. It is a finite check, not proof
    of source contact geometry or the universal path lemma.
    """
    count = 0
    for n in range(1, 5):
        pairs = list(combinations(range(n), 2))
        for pattern in product(range(3), repeat=len(pairs)):
            edges = []
            for j, ((a, b), code) in enumerate(zip(pairs, pattern)):
                if code:
                    c = F((1, 2, 8)[j % 3], 4)
                    edges.append((a, b, c) if code == 1 else (b, a, c))
            for fixed in product((-1, 0, 1), repeat=n):
                d = [F(0) if x == 1 else None for x in fixed]
                for _ in range(n):
                    for a, b, c in edges:
                        if d[a] is not None and (d[b] is None or d[b] > d[a] + c):
                            d[b] = d[a] + c
                ok = all(x != 0 or d[i] is None or d[i] >= 1
                         for i, x in enumerate(fixed))
                lamb = [max(F(0), 1 - x) if x is not None else F(0) for x in d]
                if ok:
                    assert all(x == -1 or lamb[i] == x for i, x in enumerate(fixed))
                    assert all(lamb[a] - lamb[b] <= c for a, b, c in edges)
                free = [i for i, x in enumerate(fixed) if x == -1]
                exists = False
                for vals in product([F(j, 4) for j in range(5)], repeat=len(free)):
                    trial = list(fixed)
                    for i, x in zip(free, vals):
                        trial[i] = x
                    if all(trial[a] - trial[b] <= c for a, b, c in edges):
                        exists = True
                        break
                assert exists == ok, (n, edges, fixed)
                count += 1
    print(f"PASS: weighted_difference_packets={count}")
    for k in (2, 10, 100):
        s = F(1, 100)
        excess = s / (4 * k)
        length = 1 + excess
        total_cost = k * (length * length - 1) / (2 * length * s)
        assert total_cost < 1
        assert k * excess == s / 4 < s
        assert k * length - s < k
    print("PASS: collinear slack-path regressions k=2,10,100")


if __name__ == "__main__":
    graph_checks()
    triangle_regression()
    weighted_difference_checks()
