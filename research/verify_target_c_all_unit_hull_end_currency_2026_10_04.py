#!/usr/bin/env python3
"""Exact finite regressions, not global-optimality or asymptotic certificates.

Field: Q(sqrt(5), z), z>0, z^2=(5+sqrt(5))/8. Every comparison below
uses rational arithmetic and sign-preserving squaring, never floats.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import combinations


def rat_sign(x):
    return (x > 0) - (x < 0)


@dataclass(frozen=True)
class Q5:
    a: F = F(0)
    b: F = F(0)

    def __add__(self, other):
        return Q5(self.a + other.a, self.b + other.b)

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Q5(self.a * other.a + 5 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    def sign(self):
        sa, sb = rat_sign(self.a), rat_sign(self.b)
        if not sa:
            return sb
        if not sb or sa == sb:
            return sa
        return sa * rat_sign(self.a * self.a - 5 * self.b * self.b)


Z2 = Q5(F(5, 8), F(1, 8))


@dataclass(frozen=True)
class K:
    a: Q5 = Q5()
    b: Q5 = Q5()

    def __add__(self, other):
        return K(self.a + other.a, self.b + other.b)

    def __neg__(self):
        return K(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return K(self.a * other.a + self.b * other.b * Z2,
                 self.a * other.b + self.b * other.a)

    def sign(self):
        sa, sb = self.a.sign(), self.b.sign()
        if not sa:
            return sb
        if not sb or sa == sb:
            return sa
        return sa * (self.a * self.a - self.b * self.b * Z2).sign()


def k(x):
    return K(Q5(F(x)))


ZERO, ONE = k(0), k(1)
C = K(Q5(F(-1, 4), F(1, 4)))
Z = K(Q5(), Q5(F(1)))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def norm2(a):
    return a[0] * a[0] + a[1] * a[1]


def edge(a, b):
    return tuple(sorted((a, b)))


def point_cmp(a, b):
    return (a[0] - b[0]).sign() or (a[1] - b[1]).sign()


def hull(points, indices):
    order = sorted(indices, key=cmp_to_key(lambda i, j: point_cmp(points[i], points[j])))

    def chain(seq):
        out = []
        for i in seq:
            while len(out) >= 2 and cross(sub(points[out[-1]], points[out[-2]]),
                                         sub(points[i], points[out[-1]])).sign() <= 0:
                out.pop()
            out.append(i)
        return out

    return chain(order)[:-1] + chain(order[::-1])[:-1]


def direction_cmp(a, b):
    def half(v):
        return 0 if v[1].sign() > 0 or (v[1] == ZERO and v[0].sign() > 0) else 1
    ha, hb = half(a), half(b)
    return rat_sign(ha - hb) if ha != hb else -cross(a, b).sign()


def face_walks(points, contacts, vertices):
    neighbors = {i: [] for i in vertices}
    for a, b in contacts:
        neighbors[a].append(b)
        neighbors[b].append(a)
    for i in vertices:
        neighbors[i].sort(key=cmp_to_key(lambda a, b: direction_cmp(
            sub(points[a], points[i]), sub(points[b], points[i]))))
    seen, faces = set(), []
    for a, b in sorted(contacts):
        for start in ((a, b), (b, a)):
            if start in seen:
                continue
            current, walk = start, []
            while current not in seen:
                seen.add(current)
                x, y = current
                walk.append(x)
                around = neighbors[y]
                current = (y, around[(around.index(x) - 1) % len(around)])
            assert current == start
            area2 = ZERO
            for i, x in enumerate(walk):
                area2 += cross(points[x], points[walk[(i + 1) % len(walk)]])
            faces.append((walk, area2.sign()))
    outer = [w for w, sign in faces if sign <= 0]
    assert len(outer) == 1, "fixtures must have one connected contact core"
    return [w for w, sign in faces if sign > 0], outer[0]


def pentagon():
    vectors, points = [(ONE, ZERO)], [(ZERO, ZERO)]
    for _ in range(4):
        x, y = vectors[-1]
        vectors.append((C * x - Z * y, Z * x + C * y))
    for v in vectors:
        assert norm2(v) == ONE
        points.append(add(points[-1], v))
    assert points[-1] == points[0]
    return points[:-1], vectors


def analyze(name, points, expect, flower=False):
    contacts, pair_count = set(), 0
    for a, b in combinations(range(len(points)), 2):
        d2 = norm2(sub(points[a], points[b]))
        assert (d2 - ONE).sign() >= 0, (name, a, b)
        pair_count += 1
        if d2 == ONE:
            contacts.add((a, b))
    core = sorted({i for e in contacts for i in e})
    for a, b, c in combinations(core, 3):
        assert not all(e in contacts for e in (edge(a, b), edge(a, c), edge(b, c)))
    h = hull(points, core)
    bounded, outer = face_walks(points, contacts, core)
    assert len(core) - len(contacts) + len(bounded) == 1
    rhombi = [w for w in bounded if len(w) == 4]
    exceptional = [w for w in bounded if len(w) != 4]
    assert all(len(w) >= 5 for w in exceptional)
    links = {e: set() for e in contacts}
    for w in rhombi:
        assert add(points[w[0]], points[w[2]]) == add(points[w[1]], points[w[3]])
        assert norm2(sub(points[w[0]], points[w[2]])) != ONE
        assert norm2(sub(points[w[1]], points[w[3]])) != ONE
        sides = [edge(w[i], w[(i + 1) % 4]) for i in range(4)]
        for i in range(2):
            a, b = sides[i], sides[i + 2]
            links[a].add(b)
            links[b].add(a)
    assert all(len(v) <= 2 for v in links.values())
    trains, owner = [], {}
    for e in sorted(contacts):
        if e in owner:
            continue
        stack, component = [e], set()
        while stack:
            f = stack.pop()
            if f in component:
                continue
            component.add(f)
            stack.extend(links[f] - component)
        assert sum(len(links[f]) for f in component) == 2 * (len(component) - 1)
        tid = len(trains)
        for f in component:
            owner[f] = tid
        trains.append(component)
    selected, m = [], 0
    outer_occ = [(outer[i], outer[(i + 1) % len(outer)]) for i in range(len(outer))]
    for i, a in enumerate(h):
        b = h[(i + 1) % len(h)]
        # Check the claimed hull side really supports every core point.
        assert all(cross(sub(points[b], points[a]), sub(points[v], points[a])).sign() >= 0
                   for v in core)
        if edge(a, b) in contacts:
            assert (b, a) in outer_occ
            selected.append(edge(a, b))
        else:
            m += 1
    selected_counts = [sum(e in component for e in selected) for component in trains]
    assert max(selected_counts) <= 2
    d = selected_counts.count(2)
    n0 = selected_counts.count(0)
    assert d <= 2
    crossings = set()
    for w in rhombi:
        pair = edge(owner[edge(w[0], w[1])], owner[edge(w[1], w[2])])
        assert pair[0] != pair[1] and pair not in crossings
        crossings.add(pair)
    for a, b, c in combinations(range(len(trains)), 3):
        assert not all(e in crossings for e in (edge(a, b), edge(a, c), edge(b, c)))
    r0 = sum(selected_counts[a] == selected_counts[b] == 0 for a, b in crossings)
    assert n0 * n0 >= 4 * r0
    q, b, f = len(h), len(outer), len(exceptional)
    Q = sum(len(w) - 4 for w in exceptional)
    x, gF = b - q, Q - f
    assert 0 <= m <= x
    L = F(b + Q, 2)  # Equals t_D D in a canonical source; no KKT claim for fixtures.
    assert len(trains) == len(contacts) - 2 * len(rhombi) == L + 2 * f
    assert len(trains) == q - m - d + n0
    assert 5 * L + x + m + d == 3 * b + 2 * gF + n0
    actual = (len(core), len(contacts), len(rhombi), f, q, b, m, d, n0)
    assert actual == expect, (name, actual, expect)
    if flower:
        center = [w for w in exceptional if set(w) == set(range(5))]
        assert len(center) == 1 and len(center[0]) == 5
        ends = {owner[edge(i, (i + 1) % 5)] for i in range(5)}
        assert len(ends) == 5
        assert all(selected_counts[tid] == 1 for tid in ends)
    print(f"{name}: {pair_count} exact pairs; core/e/R/f/q/b/m/d/N0={actual}; PASS")


def main():
    square = [(k(0), k(0)), (k(1), k(0)), (k(1), k(1)), (k(0), k(1))]
    analyze("square/additive-two-sharp", square, (4, 4, 1, 0, 4, 4, 0, 2, 0))
    p, vectors = pentagon()
    analyze("unit pentagon", p, (5, 5, 0, 1, 5, 5, 0, 0, 0))
    path = [(ZERO, ZERO), (ONE, ZERO), (ONE + C, Z)]
    analyze("two singleton bridges", path, (3, 2, 0, 0, 3, 4, 1, 0, 0))
    grid = [(k(i), k(j)) for i in range(3) for j in range(3)]
    analyze("nine-point grid/Mantel-sharp", grid, (9, 12, 4, 0, 4, 8, 4, 0, 4))
    flower = p[:]
    for i, v in enumerate(vectors):
        outward = (v[1], -v[0])
        flower.extend([add(p[i], outward), add(p[(i + 1) % 5], outward)])
    expected = (15, 20, 5, 1, 10, 15, 5, 0, 5)
    analyze("five-hull-end pentagonal flower", flower, expected, flower=True)
    analyze("flower plus retained isolate", flower + [(k(100), k(100))], expected,
            flower=True)
    print("PASS: local two-end pentagon capacity is false; finite identities checked.")
    print("No fixture is asserted globally optimal; asymptotic theorems need the analytic proof.")


if __name__ == "__main__":
    main()
