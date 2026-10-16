from fractions import Fraction

# Exact density arithmetic from the 15-spaced Horn subsystem.
s0 = Fraction(791, 320_000_000)
gamma = s0 / 30
assert gamma == Fraction(791, 9_600_000_000)
assert gamma / 2 == Fraction(791, 19_200_000_000)
assert gamma / 4 == Fraction(791, 38_400_000_000)
assert gamma / 8 == Fraction(791, 76_800_000_000)


def reachable(adj, s):
    seen = {s}
    stack = [s]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen


def sccs(adj):
    n = len(adj)
    reach = [reachable(adj, i) for i in range(n)]
    remaining = set(range(n))
    out = []
    while remaining:
        u = min(remaining)
        C = {v for v in remaining if v in reach[u] and u in reach[v]}
        out.append(C)
        remaining -= C
    return out


def every_sink_meets_F(adj, F):
    for C in sccs(adj):
        has_out = any(v not in C for u in C for v in adj[u])
        if not has_out and C.isdisjoint(F):
            return False
    return True


def shortest_dist_to_F(adj, F):
    n = len(adj)
    INF = 10**9
    dist = [0 if v in F else INF for v in range(n)]
    for _ in range(n):
        changed = False
        for v in range(n):
            if v in F:
                continue
            best = min((dist[w] for w in adj[v]), default=INF)
            nd = best + 1 if best < INF else INF
            if nd < dist[v]:
                dist[v] = nd
                changed = True
        if not changed:
            break
    return dist


# Exhaustively verify the finite graph lemma through four vertices.
# Under the sink-SCC poisoning condition every vertex reaches F, and choosing
# one shortest-path successor for every non-F vertex gives exactly n-|F|
# arcs with a strictly decreasing distance potential, hence an acyclic forest.
for n in range(1, 5):
    arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    for mask in range(1 << len(arcs)):
        adj = [set() for _ in range(n)]
        for k, (i, j) in enumerate(arcs):
            if (mask >> k) & 1:
                adj[i].add(j)

        for fmask in range(1, 1 << n):
            F = {i for i in range(n) if (fmask >> i) & 1}
            if not every_sink_meets_F(adj, F):
                continue

            assert all(reachable(adj, v) & F for v in range(n))
            d = shortest_dist_to_F(adj, F)
            assert all(x < 10**9 for x in d)

            parent = {}
            for v in range(n):
                if v in F:
                    continue
                options = [w for w in adj[v] if d[w] == d[v] - 1]
                assert options
                parent[v] = min(options)

            assert len(parent) == n - len(F)
            assert all(d[parent[v]] == d[v] - 1 for v in parent)

print("PASS: Horn poisoning forces a shortest-path forest")
print("gamma=", float(gamma))
print("implication_forest_density=", float(gamma / 2))
print("lower_permanent_density=", float(gamma / 4))
print("upper_permanent_density=", float(gamma / 8))
