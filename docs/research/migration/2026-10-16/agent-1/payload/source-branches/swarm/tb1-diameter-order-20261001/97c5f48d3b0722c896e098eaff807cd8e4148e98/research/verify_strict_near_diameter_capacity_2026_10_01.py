#!/usr/bin/env python3
"""Exact finite checks for strict near-diameter capacity; not global optimality.

Encoded: unit separation, full diameter, extreme hull vertices, segment crossings,
strict near-diameter threshold, strict Gabriel cutoff. All grid arithmetic is
integer arithmetic in coordinates scaled by 2. The analytical universal proofs
are in the accompanying report. Omitted: KKT, optimality, train embedding and
the rooted endpoint hypothesis. Passing is a regression check, not a theorem
about every global minimizer.
"""

from itertools import combinations
from fractions import Fraction


def norm2(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


def turn(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    ordered = sorted(points)
    chains = []
    for order in (ordered, ordered[::-1]):
        chain = []
        for p in order:
            while len(chain) >= 2 and turn(chain[-2], chain[-1], p) <= 0:
                chain.pop()
            chain.append(p)
        chains.append(chain)
    return set(chains[0][:-1] + chains[1][:-1])


def proper_cross(a, b, c, d):
    return turn(a, b, c) * turn(a, b, d) < 0 and turn(c, d, a) * turn(c, d, b) < 0


def check(points, unit2):
    edges = list(combinations(range(len(points)), 2))
    squared = {e: norm2(points[e[0]], points[e[1]]) for e in edges}
    assert min(squared.values()) >= unit2
    diameter2 = max(squared.values())
    extreme = hull(points)
    near_d = [e for e in edges if squared[e] > diameter2 - unit2]
    assert all(points[i] in extreme for e in near_d for i in e)
    assert len(near_d) <= len(extreme)
    for e, f in combinations(near_d, 2):
        if set(e).isdisjoint(f):
            assert proper_cross(*(points[i] for i in e + f))
    short = [e for e in edges if squared[e] < 2 * unit2]
    for e in short:
        p, q = (points[i] for i in e)
        for z in (points[i] for i in range(len(points)) if i not in e):
            assert sum((z[k] - p[k]) * (z[k] - q[k]) for k in (0, 1)) > 0
    for e, f in combinations(short, 2):
        if set(e).isdisjoint(f):
            assert not proper_cross(*(points[i] for i in e + f))
    return len(near_d) - sum(s == diameter2 for s in squared.values())


def sharp_regressions():
    points = [(0, 0), (0, 1), (0, -1), (3, 0)]
    assert max(norm2(p, q) for p, q in combinations(points, 2)) == 10
    assert (0, 0) not in hull(points)
    assert norm2(points[0], points[3]) == 9
    check(points, 1)
    rectangle = [(0, 0), (3, 0), (3, 1), (0, 1)]
    assert max(norm2(p, q) for p, q in combinations(rectangle, 2)) == 10
    assert norm2(rectangle[0], rectangle[1]) == norm2(rectangle[2], rectangle[3]) == 9
    assert not proper_cross(*rectangle)
    check(rectangle, 1)
    square = [(0, 0), (1, 0), (1, 1), (0, 1)]
    assert proper_cross(square[0], square[2], square[1], square[3])
    assert norm2(square[0], square[2]) == norm2(square[1], square[3]) == 2
    check(square, 1)
    # Linear planar near-unit witnesses, with an exact inverse-diameter margin.
    for r in (2, 3, 10, 50):
        height = 1 + Fraction(1, 10 * r)
        family = [(3 * j, y) for j in range(r) for y in (0, height)]
        diameter2 = max(norm2(p, q) for p, q in combinations(family, 2))
        assert diameter2 <= (3 * r) ** 2
        assert 2 * 3 * r * (height - 1) < 1
        assert min(norm2(p, q) for p, q in combinations(family, 2)) > 1
        check(family, 1)
    # Unit triangular rhombus, in the exact basis with Gram matrix [[1,1/2],[1/2,1]].
    rhombus = [(0, 0), (1, 0), (0, 1), (1, -1)]
    def triangular_norm(p, q):
        a, b = p[0] - q[0], p[1] - q[1]
        return a * a + a * b + b * b
    assert triangular_norm(rhombus[0], rhombus[1]) == 1
    assert triangular_norm(rhombus[2], rhombus[3]) == 3
    assert all(triangular_norm(p, q) >= 1 for p, q in combinations(rhombus, 2))


def check_blocker_trees():
    packets = rooted = 0
    for r in range(1, 5):
        arcs = [(i, j) for i in range(1, r + 1) for j in range(r + 1) if i != j]
        for mask in range(1 << len(arcs)):
            packets += 1
            selected = [e for k, e in enumerate(arcs) if mask & (1 << k)]
            distance = {0: 0}
            while True:
                new = {}
                for i, j in selected:
                    if j in distance and i not in distance:
                        new[i] = min(new.get(i, r + 1), distance[j] + 1)
                if not new:
                    break
                distance.update(new)
            reaches_root = len(distance) == r + 1
            # U is indexed by its movable-layer membership bits.
            every_cut = all(any(umask & (1 << (i - 1)) and
                                (j == 0 or not umask & (1 << (j - 1)))
                                for i, j in selected)
                            for umask in range(1, 1 << r))
            assert reaches_root == every_cut
            if not reaches_root:
                continue
            rooted += 1
            tree = [next((i, j) for i2, j in selected if i2 == i and distance[j] < distance[i])
                    for i in range(1, r + 1)]
            assert len({frozenset(e) for e in tree}) == r
            assert all(distance[j] < distance[i] for i, j in tree)
    print(f"PASS: {packets} directed blocker packets; {rooted} root-reaching arborescences")


def check_isolate_forests():
    accepted = assignments = 0
    cases = [(2, 3, {(0, 1)}),
             (3, 2, {(0, 1), (0, 2), (1, 2)}),
             (4, 2, {(0, 1), (2, 3)})]
    for q, z, old_edges in cases:
        deficiency = q - len(old_edges)
        available = [e for e in combinations(range(q + z), 2) if e not in old_edges]
        for mask in range(1 << len(available)):
            new_edges = {e for k, e in enumerate(available) if mask & (1 << k)}
            adjacency = {i: set() for i in range(q + z)}
            for i, j in new_edges:
                adjacency[i].add(j)
                adjacency[j].add(i)
            distance = {i: 0 for i in range(q)}
            while True:
                fresh = {i: 1 + min(distance[j] for j in adjacency[i] if j in distance)
                         for i in range(q, q + z) if i not in distance and adjacency[i] & distance.keys()}
                if not fresh:
                    break
                distance.update(fresh)
            attached = {e for e in new_edges if e[0] in distance and e[1] in distance}
            attached_isolates = set(distance) - set(range(q))
            if len(attached) - len(attached_isolates) > deficiency:
                continue  # The analytically proved subgraph edge budget is a hypothesis.
            accepted += 1
            parent = {i: min(j for j in adjacency[i] if distance.get(j, q + z) == distance[i] - 1)
                      for i in attached_isolates}
            forest = {tuple(sorted((i, j))) for i, j in parent.items()}
            residue = attached - forest
            assert len(forest) == len(attached_isolates)
            assert len(residue) <= deficiency
            for labels in range(1 << q):
                assignments += 1
                copied = {i: (labels >> i) & 1 for i in range(q)}
                for i in sorted(attached_isolates, key=distance.get):
                    copied[i] = copied[parent[i]]
                copied.update({i: 0 for i in range(q, q + z) if i not in copied})
                changed = {e for e in new_edges if copied[e[0]] != copied[e[1]]}
                assert changed <= residue
                assert len(changed) <= deficiency
    # Exact Q(sqrt(3)) forest residue, using certified rational bounds 1<sqrt(3)<2.
    t = Fraction(1, 10000)
    cosine, sine = (1 - t*t) / (1 + t*t), 2*t / (1 + t*t)
    assert cosine*cosine + sine*sine == 1
    assert 200 - 100*cosine - 200*sine > 99
    assert 200 - 100*cosine - 100*sine < 100
    print(f"PASS: {accepted} multi-root isolate graphs; {assignments} binary root assignments; sharp d_H=1 residue")


def main():
    sharp_regressions()
    check_blocker_trees()
    check_isolate_forests()
    grid = list(combinations([(i, j) for i in range(6) for j in range(6)], 4))
    eligible = inactive = packets_with_inactive = 0
    for points in grid:
        if any(norm2(p, q) < 4 for p, q in combinations(points, 2)):
            continue
        eligible += 1
        count = check(points, 4)
        inactive += count
        packets_with_inactive += count > 0
    print(f"PASS: {eligible} unit-separated four-point half-grid packets; "
          f"{packets_with_inactive} packets with {inactive} strict inactive near-diameter edges")
    print("PASS: sharp extremality/crossing/Gabriel regressions and four exact linear-witness families")
    print("Not encoded: KKT, train geometry, rooted endpoint, or global optimality.")


if __name__ == '__main__':
    main()
