#!/usr/bin/env python3
"""Exact certificates for finite translation lens domination/exposure.

Checks rational four-point actual sources under all sampled translations
preserving their two old crossing diameters. Certifies the two opposite cross
upper constraints and strictness if one old bar shortens. Lower constraints
are not asserted for arbitrary lens translations. A separate rational source
family preserves every contact/lower bound and shortens every moving old
diameter, but an unexposed contact vertex creates the sole upper violation.
No packet is asserted to be a canonical global minimizer.
"""

from fractions import Fraction as F
from itertools import product

from verify_target_c_rotation_cell_barriers_2026_10_02 import (
    add, sub, norm, distances, contacts, triangle_free,
)


def lens_census():
    a, b, d2 = F(4), F(3), F(25)
    vectors = []
    for i, j in product(range(-4, 5), range(-12, 13)):
        z = F(i, 4), F(j, 4)
        if (a + abs(z[0])) ** 2 + z[1] ** 2 > d2:
            continue
        source = [((z[0] - a) / 2, (z[1] - b) / 2),
                  ((z[0] + a) / 2, (z[1] + b) / 2),
                  ((-z[0] - a) / 2, (-z[1] + b) / 2),
                  ((-z[0] + a) / 2, (-z[1] - b) / 2)]
        old = distances(source)
        if min(old.values()) < 1 or max(old.values()) > d2:
            continue
        assert old[(0, 1)] == old[(2, 3)] == d2
        vectors.append((z, source))
    translations = []
    for i, j in product(range(-8, 9), range(-4, 5)):
        p = F(i, 2), F(j, 2)
        if p[0] ** 2 + (abs(p[1]) + b) ** 2 <= d2:
            translations.append(p)
    upper_checks = strict_checks = 0
    for z, source in vectors:
        for p in translations:
            delta = p[0] - a, p[1]
            target = [add(point, delta) if i in {1, 3} else point
                      for i, point in enumerate(source)]
            new = distances(target)
            assert new[(0, 1)] <= d2 and new[(2, 3)] <= d2
            assert new[(0, 3)] <= d2 and new[(1, 2)] <= d2
            # Nondegenerate, disjoint old bars: shortening just one suffices.
            if min(new[(0, 1)], new[(2, 3)]) < d2:
                assert new[(0, 3)] < d2 and new[(1, 2)] < d2
                strict_checks += 2
            upper_checks += 2
    return len(vectors), len(translations), upper_checks, strict_checks


def uncovered_upper_packet(n):
    t = F(1, 2 * n - 1)
    c, s = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
    r = F(n) * c, F(n) * s
    wx, wy = r[0] - 1, r[1]
    q = (1 + F(1, n)) * wy / wx
    v = (1 - q * q) / (1 + q * q), 2 * q / (1 + q * q)
    delta = v[0] - 1, v[1]
    rho = F(n) - F(1, 2 * n)
    z = F(3, 5) * rho, F(4, 5) * rho
    source = [(F(k), F(0)) for k in range(n)]
    source += [(F(n), F(0)), r, (r[0], -r[1]),
               (r[0] - 1, r[1]), (r[0] - 1, -r[1]),
               z, (z[0] - 1, z[1])]
    moving = {n, n + 1, n + 2, n + 5}
    target = [add(p, delta) if i in moving else p
              for i, p in enumerate(source)]
    old, new = distances(source), distances(target)
    assert min(old.values()) == min(new.values()) == 1
    assert max(old.values()) == n * n
    old_c = contacts(old)
    assert old_c == contacts(new)
    assert len(old_c) == n + 3
    assert triangle_free(old_c, len(source))
    assert {i for e in old_c for i in e} == set(range(len(source)))
    old_h = {e for e, value in old.items() if value == n * n}
    assert old_h == {(0, n), (0, n + 1), (0, n + 2)}
    assert all(new[e] < n * n for e in old_h)
    assert {e for e, value in new.items() if value > n * n} == {(0, n + 5)}
    cut_contacts = {e for e in old_c if len(set(e) & moving) == 1}
    assert len(cut_contacts) == 4
    for i, j in cut_contacts:
        if i not in moving:
            i, j = j, i
        assert sub(source[i], source[j]) == (F(1), F(0))
        assert sub(target[i], target[j]) == v
    assert norm(source[n + 5]) < n * n
    # The only upper blocker is nonisolated, but its old diameter degree is 0.
    assert any(n + 5 in e for e in old_c)
    assert not any(n + 5 in e for e in old_h)
    return len(old) + len(new), len(cut_contacts)


def lower_collision_packet():
    source = [(F(0), F(0)), (F(0), F(1)),
              (F(4), F(0)), (F(4), F(1))]
    target = source[:2] + [(F(0), F(0)), (F(0), F(1))]
    old, new = distances(source), distances(target)
    assert max(old.values()) == 17
    assert max(new.values()) == 1
    assert all(new[e] == 1 for e in contacts(old))
    assert new[(0, 2)] == new[(1, 3)] == 0


def main():
    sources, endpoints, upper, strict = lens_census()
    print(f"PASS: {sources} actual four-point sources x {endpoints} lens "
          f"endpoints; {upper} cross-upper checks; {strict} strict checks")
    pairs = cut = 0
    for n in [16, 32, 64, 128, 256]:
        checked, preserved = uncovered_upper_packet(n)
        pairs += checked
        cut += preserved
    print(f"PASS: 5 uncovered-upper source packets; {pairs} exact pair checks; "
          f"{cut} preserved cut contacts; every moving old diameter shortens")
    lower_collision_packet()
    print("PASS: exact lower-collision regression despite upper feasibility "
          "and preservation of every old contact")
    print("SCOPE: finite geometry/regressions; no canonical source or Level I certificate")


if __name__ == "__main__":
    main()
