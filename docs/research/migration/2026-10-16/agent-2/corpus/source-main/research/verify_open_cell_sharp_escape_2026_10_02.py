#!/usr/bin/env python3
"""Exact checks for the sharp open-cell escape packet.

Encoded: singleton finite unit-vector chart, signed diameter rows, antitone
paired trees, proper cyclic layer order, and every old/new pair of an explicit
six-point source with one actual non-singleton rhombus train cut.
Arithmetic: fractions/integer combinatorics only; no numerical tolerance.
Conclusions: polynomial identities, exact barrier signs, finite tree and chord
regressions, full finite-source feasibility and a strict diameter decrease.
Omitted: theorem extraction for arbitrary global minimizers, full vertex KKT
equilibrium of the explicit source, both-shore motion, and global optimality.
The finite enumerations are checks of analytic proofs, not universal proofs.
"""

from fractions import Fraction as F
from itertools import combinations, permutations


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def norm2(x):
    return dot(x, x)


def unit(t):
    return ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


def identity_checks():
    cases = 0
    params = [F(i, j) for j in range(1, 8) for i in range(-9, 10)]
    for a, c in [(F(240, 13), F(100, 13)), (F(1), F(2)),
                 (F(-3, 2), F(1, 7)), (F(5, 3), F(-4, 9))]:
        for sign in (-1, 1):
            old = (sign * a, sign * c)
            for t in params:
                du = sub(unit(t), (F(1), F(0)))
                moved = add(old, tuple(sign * x for x in du))
                excess = norm2(moved) - norm2(old)
                expected = 4 * t * (c - (a - 1) * t) / (1 + t * t)
                assert excess == expected
                cases += 1
    # A positive sign-matching parameter is blocked for every a<=1.
    for a in (F(-4), F(0), F(1)):
        for c in (F(1, 100), F(2), F(17, 3)):
            for t in (F(1, 10000), F(1, 2), F(10)):
                assert 4 * t * (c - (a - 1) * t) > 0
                assert 4 * (-t) * (-c - (a - 1) * (-t)) > 0
                cases += 2
    for a in (F(3, 2), F(7), F(240, 13)):
        for c in (F(1, 10), F(2), F(100, 13)):
            barrier = c / (a - 1)
            for sign in (-1, 1):
                for ratio, want in [(F(1, 2), 1), (F(1), 0), (F(3, 2), -1)]:
                    t = sign * ratio * barrier
                    excess = 4 * t * (sign * c - (a - 1) * t)
                    assert (excess > 0) - (excess < 0) == want
                    cases += 1
    return cases


def antitone(edges):
    directed = [(a, b) for a, b in edges] + [(b, a) for a, b in edges]
    return all(q >= s for p, q in directed for r, s in directed if p < r)


def connected(edges, n):
    seen = {0}
    todo = [0]
    adjacency = [[] for _ in range(n)]
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    while todo:
        v = todo.pop()
        for w in adjacency[v]:
            if w not in seen:
                seen.add(w)
                todo.append(w)
    return len(seen) == n


def meets(chord, other, size):
    if set(chord) & set(other):
        return True
    a, b = sorted(chord)
    c, d = other
    return (a < c < b) != (a < d < b)


def eliminate(edges, n):
    clusters = [{i} for i in range(n)]
    coordinates = list(range(1, n))
    left_edges = set(edges)
    deleted = set()
    order = []
    while left_edges:
        where = {v: i for i, block in enumerate(clusters) for v in block}
        adjacent = [e for e in left_edges if abs(where[e[0]] - where[e[1]]) == 1]
        assert len(adjacent) == 1
        e = adjacent[0]
        k = min(where[e[0]], where[e[1]])
        coord = coordinates[k]
        assert set(range(e[0] + 1, e[1] + 1)) - deleted == {coord}
        order.append((e, coord))
        deleted.add(coord)
        clusters[k] |= clusters[k + 1]
        clusters.pop(k + 1)
        coordinates.pop(k)
        left_edges.remove(e)
    assert deleted == set(range(1, n))
    return order


def tree_checks():
    count = 0
    chord_checks = 0
    orders = 0
    for n in range(2, 8):
        m = n - 1
        all_edges = list(combinations(range(n), 2))
        size = 2 * n
        # L_0,...,L_m,U_m,...,U_0; extreme copies lie in the cap blocks.
        lpos = {j: j for j in range(n)}
        upos = {j: 2 * n - 1 - j for j in range(n)}
        local_count = 0
        for edges in combinations(all_edges, m):
            if not antitone(edges) or not connected(edges, n):
                continue
            local_count += 1
            count += 1
            order = eliminate(edges, n)
            orders += len(order)
            r = max(a + 1 for a, _ in edges)
            assert r == min(b for _, b in edges)
            assert (r - 1, r) in edges
            assert sum(b - a for a, b in edges) == m * (m + 1) // 2
            selected = [(lpos[a], upos[b]) for a, b in edges]
            selected += [(lpos[b], upos[a]) for a, b in edges]
            assert len(set(tuple(sorted(h)) for h in selected)) == 2 * m
            for h, k in combinations(selected, 2):
                assert meets(h, k, size)
                chord_checks += 1
            possible_zero_layers = []
            for j in range(n):
                h = (lpos[j], upos[j])
                if all(meets(h, k, size) for k in selected):
                    possible_zero_layers.append(j)
                chord_checks += len(selected)
            assert possible_zero_layers == [r - 1, r]
            # Distinct same-layer chords cannot both be diameter chords.
            for j, k in combinations(range(n), 2):
                assert not meets((lpos[j], upos[j]), (lpos[k], upos[k]), size)
                chord_checks += 1
        assert local_count == 2 ** (n - 2)
    return count, orders, chord_checks


def source_checks():
    d = F(20)
    d2 = d * d
    u = (F(1), F(0))
    v = (F(8, 17), F(15, 17))
    points = {
        "z": (F(0), F(0)), "p": v, "q": u, "s": add(u, v),
        "a": (F(240, 13), F(100, 13)),
        "b": (F(240, 13), F(-100, 13)),
    }
    pairs = list(combinations(points, 2))
    old_d = {pair: norm2(sub(points[pair[0]], points[pair[1]])) for pair in pairs}
    assert min(old_d.values()) == 1
    assert max(old_d.values()) == d2
    contacts = {frozenset(pair) for pair, dist in old_d.items() if dist == 1}
    assert contacts == {frozenset(e) for e in [("z", "q"), ("p", "s"),
                                              ("z", "p"), ("q", "s")]}
    diameters = {frozenset(pair) for pair, dist in old_d.items() if dist == d2}
    assert diameters == {frozenset(("z", "a")), frozenset(("z", "b"))}
    assert all(not all(frozenset(e) in contacts for e in combinations(tri, 2))
               for tri in combinations(points, 3))
    # The actual O--O rhombus train is the line parallel to v through u/2.
    normal = (v[1], -v[0])
    threshold = dot(normal, u) / 2
    left = {name for name, p in points.items() if dot(normal, p) < threshold}
    right = set(points) - left
    assert left == {"z", "p"}
    assert right == {"q", "s", "a", "b"}
    assert all(dot(normal, p) != threshold for p in points.values())
    t = F(-1, 2)
    moved_u = unit(t)
    delta = sub(moved_u, u)
    assert moved_u == (F(3, 5), F(-4, 5))
    assert delta == (F(-2, 5), F(-4, 5))
    moved = {name: add(p, delta) if name in right else p for name, p in points.items()}
    new_d = {pair: norm2(sub(moved[pair[0]], moved[pair[1]])) for pair in pairs}
    assert min(new_d.values()) == 1
    assert max(new_d.values()) < d2
    assert {frozenset(pair) for pair, dist in new_d.items() if dist == 1} == contacts
    assert max(new_d.values()) == F(25892, 65)
    assert d2 - max(new_d.values()) == F(108, 65)
    assert dot(u, v) == F(8, 17)
    assert dot(moved_u, v) == F(-36, 85)
    assert -F(1, 2) < dot(u, v) < F(1, 2)
    assert -F(1, 2) < dot(moved_u, v) < F(1, 2)
    a = F(240, 13)
    c = F(100, 13)
    barrier = c / (a - 1)
    assert barrier == F(100, 227)
    assert abs(t) > barrier > F(5, 12)
    # Formal cut virtual work is positive/negative and balanced. Full KKT is
    # explicitly absent at a,b, which have diameter load and no contacts.
    assert F(1, 2) * c + F(1, 2) * (-c) == 0
    for isolate in ("a", "b"):
        assert not any(isolate in e for e in contacts)
        assert any(isolate in e for e in diameters)
    return len(pairs) * 2, d2 - max(new_d.values())


def pentagon_checks():
    """Exact Q(sqrt(5)) checks; x coordinates share one positive factor R."""
    zero = (F(0), F(0))
    one = (F(1), F(0))

    def plus(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def minus(x, y):
        return (x[0] - y[0], x[1] - y[1])

    def times(x, y):
        a, b = x
        c, d = y
        return (a * c + 5 * b * d, a * d + b * c)

    def scale(x, s):
        return tuple(s * a for a in x)

    def sign(x):
        a, b = x
        if not b:
            return (a > 0) - (a < 0)
        if not a or (a > 0) == (b > 0):
            return (b > 0) - (b < 0)
        if a > 0:
            return (a * a > 5 * b * b) - (a * a < 5 * b * b)
        return (5 * b * b > a * a) - (5 * b * b < a * a)

    def determinant(matrix):
        result = zero
        n = len(matrix)
        for p in permutations(range(n)):
            value = one
            for i, j in enumerate(p):
                value = times(value, matrix[i][j])
            parity = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
            result = plus(result, scale(value, (-1) ** parity))
        return result

    # Actual x=R*x_coeff, where R^2=(5+sqrt(5))/10; y is unscaled.
    r2 = (F(1, 2), F(1, 10))
    diameter2 = (F(3, 2), F(1, 2))
    points = {
        "z": (zero, zero),
        "l": ((F(5, 4), F(-1, 4)), (F(-1, 4), F(-1, 4))),
        "a": ((F(5, 4), F(1, 4)), (F(-1, 2), F(0))),
        "b": ((F(5, 4), F(1, 4)), (F(1, 2), F(0))),
        "w": ((F(5, 4), F(-1, 4)), (F(1, 4), F(1, 4))),
    }
    names = list(points)
    contacts = []
    diameters = []
    for i, j in combinations(range(5), 2):
        dx = minus(points[names[i]][0], points[names[j]][0])
        dy = minus(points[names[i]][1], points[names[j]][1])
        d2 = plus(times(r2, times(dx, dx)), times(dy, dy))
        assert d2 in (one, diameter2)
        (contacts if d2 == one else diameters).append((i, j))
    assert len(contacts) == len(diameters) == 5
    # Full normalized positive KKT, PSD stress and exact core affine nullity.
    stress = [[zero for _ in range(5)] for _ in range(5)]
    for edges, weight in [(contacts, scale(diameter2, F(1, 5))),
                          (diameters, (F(-1, 5), F(0)))]:
        for i, j in edges:
            stress[i][i] = plus(stress[i][i], weight)
            stress[j][j] = plus(stress[j][j], weight)
            stress[i][j] = minus(stress[i][j], weight)
            stress[j][i] = minus(stress[j][i], weight)
    for column in ([one] * 5,
                   [points[name][0] for name in names],
                   [points[name][1] for name in names]):
        for row in stress:
            energy = zero
            for x, y in zip(row, column):
                energy = plus(energy, times(x, y))
            assert energy == zero
    minors = 0
    positive_two = False
    for size in range(1, 6):
        for subset in combinations(range(5), size):
            minor = determinant([[stress[i][j] for j in subset] for i in subset])
            assert sign(minor) >= 0
            if size >= 3:
                assert minor == zero
            if size == 2 and sign(minor) > 0:
                positive_two = True
            minors += 1
    assert positive_two
    for reverse in (False, True):
        layers = {"z": 0, "l": 1, "a": 2, "b": 2, "w": 1}
        if reverse:
            layers = {name: 2 - value for name, value in layers.items()}
        support = {}
        empty = []
        work = [zero, zero]
        for i, j in diameters:
            x, y = names[i], names[j]
            if layers[x] == layers[y]:
                empty.append(layers[x])
                continue
            if layers[x] > layers[y]:
                x, y = y, x
            a, b = layers[x], layers[y]
            support[(a, b)] = support.get((a, b), 0) + 1
            transverse = minus(points[y][1], points[x][1])
            assert transverse != zero
            for k in range(a, b):
                work[k] = plus(work[k], scale(transverse, F(1, 5)))
        assert set(support.values()) == {2}
        assert work == [zero, zero]
        r = max(a + 1 for a, b in support)
        assert r == min(b for a, b in support)
        assert empty == [r if reverse else r - 1]
    return 10, minors


def main():
    identities = identity_checks()
    trees, contractions, chords = tree_checks()
    pairs, margin = source_checks()
    pentagon_pairs, minors = pentagon_checks()
    print(f"PASS: {identities} exact singleton/barrier checks")
    print(f"PASS: {trees} paired antitone trees, {contractions} contractions, "
          f"{chords} proper-order chord checks")
    print(f"PASS: {pairs} original/moved source pairs; squared-diameter gain {margin}")
    print(f"PASS: {pentagon_pairs} quadratic-field pentagon pairs, full KKT, "
          f"{minors} PSD principal minors, rank 2 and both sharp pivot-layer cases")
    print("SCOPE: six-point move omits full KKT; neither source has a "
          "global-optimality certificate")


if __name__ == "__main__":
    main()
