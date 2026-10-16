#!/usr/bin/env python3
"""Exact finite audits for the phase-gap/rhombus-blocker candidate.

Encodes: Q(sqrt(3)) source coordinates, all pair lengths, old contact
preservation, rhombus diagonals, and finite interval direction packets.
Omits: KKT, global diameter optimality, large-source extraction and any
identification of crossing omissions with a canonical defect budget.
Success certifies the displayed finite regression packets and finite
combinatorial checks; the geometric theorem has a separate human proof.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, permutations, product


@dataclass(frozen=True)
class Q3:
    a: F = F(0)
    b: F = F(0)

    def __add__(self, other):
        other = lift(other)
        return Q3(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, other):
        return self + -lift(other)

    def __rsub__(self, other):
        return lift(other) + -self

    def __mul__(self, other):
        other = lift(other)
        return Q3(self.a * other.a + 3 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def sign(self):
        if not self.b:
            return (self.a > 0) - (self.a < 0)
        if not self.a:
            return (self.b > 0) - (self.b < 0)
        if self.a > 0 and self.b > 0:
            return 1
        if self.a < 0 and self.b < 0:
            return -1
        delta = self.a * self.a - 3 * self.b * self.b
        assert delta != 0  # sqrt(3) is irrational
        return ((delta > 0) - (delta < 0)) * (1 if self.a > 0 else -1)


def lift(x):
    return x if isinstance(x, Q3) else Q3(F(x))


def add(p, q):
    return tuple(x + y for x, y in zip(p, q))


def sub(p, q):
    return tuple(x - y for x, y in zip(p, q))


def norm2(p):
    return sum(x * x for x in p)


def rotated(p, c, s):
    return c * p[0] - s * p[1], s * p[0] + c * p[1]


def source_packet(m):
    c, s = F(m * m - 1, m * m + 1), F(2 * m, m * m + 1)
    zero, a = (Q3(), Q3()), (Q3(F(1)), Q3())
    root = (Q3(F(1, 2)), Q3(F(0), F(1, 2)))
    b = rotated(rotated(a, c, s), c, s)
    v = rotated(root, c, s)
    w = rotated(rotated(v, c, s), c, s)
    source = [zero, a, add(a, b), w, add(a, w), add(add(a, b), w),
              sub(zero, v), sub(a, v), (Q3(F(-m)), Q3(F(-m)))]
    moving = {1, 4, 7}
    delta = sub(b, a)
    target = [add(p, delta) if i in moving else p for i, p in enumerate(source)]
    return source, target, a, b, v, w


def check_sources():
    pairs_checked = contacts_checked = 0
    expected_contacts = {(0, 1), (1, 2), (3, 4), (4, 5),
                         (0, 3), (1, 4), (2, 5),
                         (0, 6), (1, 7), (6, 7)}
    faces = [(0, 1, 4, 3), (1, 2, 5, 4), (0, 1, 7, 6)]
    for m in (20, 40, 100, 1000, 10000):
        old, new, a, b, v, w = source_packet(m)
        contacts = set()
        for i, j in combinations(range(len(old)), 2):
            n = norm2(sub(old[i], old[j]))
            assert (n - 1).sign() >= 0, (m, i, j, n)
            if (n - 1).sign() == 0:
                contacts.add((i, j))
            pairs_checked += 1
        assert contacts == expected_contacts, (m, contacts)
        for i, j, k in combinations(range(len(old)), 3):
            assert not {(i, j), (i, k), (j, k)} <= contacts
        for i, j in contacts:
            assert (norm2(sub(new[i], new[j])) - 1).sign() == 0
            contacts_checked += 1
        for face in faces:
            for i, j in ((face[0], face[2]), (face[1], face[3])):
                assert (norm2(sub(old[i], old[j])) - 1).sign() > 0
        for face in faces[:2]:
            for i, j in ((face[0], face[2]), (face[1], face[3])):
                assert (norm2(sub(new[i], new[j])) - 1).sign() > 0
        assert (norm2(sub(new[0], new[7])) - 1).sign() < 0
        assert (norm2(sub(b, v)) - 1).sign() < 0
        # The external and retained transverse train cannot cross in a strict rhombus.
        assert (norm2(sub(v, w)) - 1).sign() < 0
        # Full-source diameter grows with the retained isolate; all 9 points were checked.
        assert (norm2(sub(old[8], old[0])) - m * m).sign() > 0
    return pairs_checked, contacts_checked


def check_single_thresholds():
    packets = 0
    for r in range(2, 9):
        phases = list(map(F, range(r)))
        for twice_t in range(-1, 2 * r):
            t = F(twice_t, 2)
            for side in ("lower", "upper"):
                allowed = [i for i, x in enumerate(phases)
                           if (x > t if side == "lower" else x < t)]
                for bits in range(1 << len(allowed)):
                    crossing = {allowed[j] for j in range(len(allowed)) if bits >> j & 1}
                    blocked = []
                    for i in range(r - 1):
                        permits_i = (phases[i] > t if side == "lower" else phases[i] < t)
                        permits_next = (phases[i + 1] > t if side == "lower" else phases[i + 1] < t)
                        if ((i in crossing and not permits_next) or
                                (i + 1 in crossing and not permits_i)):
                            blocked.append(i + 1)
                    assert len(blocked) <= 1
                    if blocked:
                        i = blocked[0]
                        assert r - len(crossing) >= min(i, r - i)
                        # Scale L=100. B direction is in the full admissible intersection.
                        y_b = F(100) + phases[-1] + F(1, 2)
                        y_c = t + (200 if side == "lower" else 100)
                        gap = abs(y_b - y_c) % 300
                        assert min(gap, 300 - gap) < 100
                    packets += 1
    return packets


def check_weight_bound():
    subsets = 0
    for r in range(2, 14):
        weights = [min(i, r - i) for i in range(1, r)]
        minima = {}
        for bits in range(1 << (r - 1)):
            k = bits.bit_count()
            total = sum(w for i, w in enumerate(weights) if bits >> i & 1)
            bound = (k + 1) ** 2 // 4
            assert total >= bound
            minima[k] = min(minima.get(k, total), total)
            subsets += 1
        assert all(minima[k] == (k + 1) ** 2 // 4 for k in minima)
    return subsets


def check_interval_permutations():
    packets = permutations_checked = 0
    for r in range(2, 6):
        choices = [[(lo, hi) for lo in range(i + 1) for hi in range(i, r)]
                   for i in range(r)]
        perms = list(permutations(range(r)))
        for intervals in product(*choices):
            safe_pair = any(intervals[i][0] <= j <= intervals[i][1] and
                            intervals[j][0] <= i <= intervals[j][1]
                            for i, j in combinations(range(r), 2))
            nontrivial = False
            for perm in perms:
                permits = all(lo <= j <= hi for (lo, hi), j in zip(intervals, perm))
                if permits and any(i != j for i, j in enumerate(perm)):
                    nontrivial = True
                permutations_checked += 1
            assert nontrivial == safe_pair
            packets += 1
    # Adjacent swaps alone do not detect all safe permutations.
    intervals = [(0, 2), (1, 1), (0, 2)]
    assert all(not (intervals[i][0] <= i + 1 <= intervals[i][1] and
                    intervals[i + 1][0] <= i <= intervals[i + 1][1]) for i in range(2))
    assert all(lo <= j <= hi for (lo, hi), j in zip(intervals, (2, 1, 0)))
    return packets, permutations_checked


def main():
    pair_count, contact_count = check_sources()
    threshold_count = check_single_thresholds()
    subset_count = check_weight_bound()
    interval_count, permutation_count = check_interval_permutations()
    print(f"PASS: {pair_count} exact source pairs; {contact_count} old contacts preserved.")
    print(f"PASS: {threshold_count} single-threshold packets; {subset_count} gap subsets.")
    print(f"PASS: {interval_count} interval packets; {permutation_count} phase assignments.")
    print("PASS: retained-grid / external-rhombus regression and adjacent-only false-lock regression.")
    print("Not certified: KKT, canonical extraction, omission-budget globalization, or Level I optimality.")


if __name__ == "__main__":
    main()
