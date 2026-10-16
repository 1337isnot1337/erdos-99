#!/usr/bin/env python3
"""Exact fixtures for whole-source parallel-contact approximation.

All comparisons use Q(sqrt(3)); no floating point or optimizer is used.
This verifies the named finite fixtures, not a global optimality theorem.
"""

from fractions import Fraction as Q
from itertools import combinations


class R:
    """a+b*sqrt(3), with exact field operations and ordering."""

    def __init__(self, a=0, b=0):
        self.a, self.b = Q(a), Q(b)

    def __add__(self, other):
        other = other if isinstance(other, R) else R(other)
        return R(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return R(-self.a, -self.b)

    def __sub__(self, other):
        return self + -other if isinstance(other, R) else self + R(-other)

    def __mul__(self, other):
        other = other if isinstance(other, R) else R(other)
        return R(self.a * other.a + 3 * self.b * other.b,
                 self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def sign(self):
        a, b = self.a, self.b
        if not b:
            return (a > 0) - (a < 0)
        if not a or (a > 0) == (b > 0):
            return (b > 0) - (b < 0)
        delta = a * a - 3 * b * b
        assert delta != 0, "sqrt(3) is irrational"
        return ((a > 0) - (a < 0)) * ((delta > 0) - (delta < 0))

    def __lt__(self, other):
        return (self - other).sign() < 0

    def __eq__(self, other):
        return isinstance(other, R) and (self.a, self.b) == (other.a, other.b)

    def __hash__(self):
        return hash((self.a, self.b))


def fixtures():
    square = [(R(x), R(y)) for x, y in [(0, 0), (1, 0), (1, 1), (0, 1)]]
    wheel = [(R(0), R(0)), (R(1), R(0)), (R(Q(1, 2)), R(0, Q(1, 2))),
             (R(Q(-1, 2)), R(0, Q(1, 2))), (R(-1), R(0)),
             (R(Q(-1, 2)), R(0, Q(-1, 2))), (R(Q(1, 2)), R(0, Q(-1, 2)))]
    patch = [(R(i + Q(j, 2)), R(0, Q(j, 2))) for i in range(7) for j in range(7)]
    return [("square", square), ("wheel", wheel), ("triangular_patch_49", patch)]


def certify(name, points):
    polys = {}
    vectors = {}
    old_contacts = set()
    for i, j in combinations(range(len(points)), 2):
        dx, dy = points[i][0] - points[j][0], points[i][1] - points[j][1]
        poly = (dx * dx + dy * dy, dx * dx, 2 * dx * dy, dy * dy)
        assert not poly[0] < R(1)
        if poly[0] == R(1):
            old_contacts.add((i, j))
        polys[i, j] = poly
        if dx.sign() < 0 or (dx.sign() == 0 and dy.sign() < 0):
            dx, dy = -dx, -dy
        vectors[i, j] = (dx, dy)

    classes = {}
    for pair, vec in vectors.items():
        poly = polys[pair]
        if vec in classes:
            assert classes[vec] == poly
        else:
            classes[vec] = poly
    assert len(set(classes.values())) == len(classes)
    s = len(classes)
    bad_root_bound = 3 * s * (s - 1) // 2
    epsilon = Q(1, 100)
    for k in range(1, bad_root_bound + 2):
        t = epsilon * k / (bad_root_bound + 1)
        lengths = {pair: sum((c * t**power for power, c in enumerate(poly)), R())
                   for pair, poly in polys.items()}
        class_values = [sum((c * t**power for power, c in enumerate(poly)), R())
                        for poly in classes.values()]
        if len(set(class_values)) == s:
            break
    else:
        raise AssertionError("finite bad-root bound was exceeded")

    m2, old_d2, new_d2_raw = min(lengths.values()), max(p[0] for p in polys.values()), max(lengths.values())
    assert not m2 < R(1)
    contacts = {pair for pair, value in lengths.items() if value == m2}
    assert len({vectors[pair] for pair in contacts}) == 1
    adj = [set() for _ in points]
    for i, j in contacts:
        adj[i].add(j)
        adj[j].add(i)
    assert max(map(len, adj)) <= 2
    remaining = set(range(len(points)))
    components = 0
    while remaining:
        stack, component = [next(iter(remaining))], set()
        while stack:
            i = stack.pop()
            if i not in component:
                component.add(i)
                stack.extend(adj[i] - component)
        remaining -= component
        edges = sum(len(adj[i]) for i in component) // 2
        assert edges == len(component) - 1
        components += 1
    if len(points) >= 3:
        raw_clearance = min(max(lengths[i, j], lengths[i, k], lengths[j, k]) - m2
                            for i, j, k in combinations(range(len(points)), 3))
        assert raw_clearance.sign() > 0
    for pair, value in lengths.items():
        # Normalized value is value/m2. These are exact cross-multiplied tests.
        assert not value < m2
        assert not (m2 * R(1 + epsilon + epsilon**3) * polys[pair][0]) < value
    assert not (m2 * R(1 + epsilon + epsilon**3) * old_d2) < new_d2_raw
    # This fixture must retain the attainment distinction: diameter increases.
    if name == "wheel":
        assert old_d2 == R(4)
        assert (new_d2_raw - m2 * old_d2).sign() > 0
        assert len(old_contacts) == 12
    print(f"PASS {name}: labels={len(points)} pairs={len(polys)} "
          f"classes={s} samples={k} contacts={len(contacts)} components={components}")


if __name__ == "__main__":
    for fixture_name, fixture_points in fixtures():
        certify(fixture_name, fixture_points)
    print("PASS exact finite fixtures; no global-optimality or Level I certificate")
