#!/usr/bin/env python3
"""Exact leaf-fan/collar regressions; see research/README.md and the report.

All coordinates and multipliers are rational. The finite packets satisfy every
source separation/diameter constraint and interior equilibrium, but omit KKT
equilibrium at the carrier and the four collar endpoints. They are not global
minimizers and do not certify a completed positive stress or PSD stress matrix.
"""

from fractions import Fraction as F
from itertools import combinations


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def scale(k, p):
    return k * p[0], k * p[1]


def dot(p, q):
    return p[0] * q[0] + p[1] * q[1]


def cross(p, q):
    return p[0] * q[1] - p[1] * q[0]


def norm2(p):
    return dot(p, p)


def rotate(p, c, s):
    return c * p[0] - s * p[1], s * p[0] + c * p[1]


def packet(size):
    t = F(1, 4 * size)
    ch = (1 - t * t) / (1 + t * t)
    sh = 2 * t / (1 + t * t)
    cc, ss = ch * ch - sh * sh, 2 * ch * sh
    diameter = 1 / (2 * sh)
    radius2 = diameter * diameter
    half_length = size // 8
    p = {0: (diameter, F(0))}
    for i in range(1, half_length + 1):
        p[i] = rotate(p[i - 1], cc, ss)
        p[-i] = p[i][0], -p[i][1]
    z = {i: sub(v, (F(1), F(0))) for i, v in p.items()}
    indices = sorted(p)
    points = {('a', 0): (F(0), F(0))}
    points.update({('p', i): p[i] for i in indices})
    points.update({('z', i): z[i] for i in indices})
    contacts, diameters = set(), set()
    pair_checks = 0
    for left, right in combinations(points, 2):
        distance2 = norm2(sub(points[left], points[right]))
        assert 1 <= distance2 <= radius2, (size, left, right)
        pair_checks += 1
        if distance2 == 1:
            contacts.add(frozenset((left, right)))
        if distance2 == radius2:
            diameters.add(frozenset((left, right)))
    expected_contacts = {
        frozenset((('p', i), ('z', i))) for i in indices
    }
    for i in indices[:-1]:
        for tier in ('p', 'z'):
            expected_contacts.add(frozenset(((tier, i), (tier, i + 1))))
    assert contacts == expected_contacts
    assert diameters == {
        frozenset((('a', 0), ('p', i))) for i in indices
    }
    for x, y, w in combinations(points, 3):
        assert not all(frozenset(edge) in contacts for edge in ((x, y), (y, w), (w, x)))

    mu, lam, tangent = {}, {}, {}
    area_sum = F(0)
    for i in indices[:-1]:
        chord = sub(p[i + 1], p[i])
        assert norm2(chord) == 1
        mid_cos, mid_sin = chord[1], -chord[0]
        assert mid_cos > 0 and mid_cos * mid_cos + mid_sin * mid_sin == 1
        mu[i] = 1 / mid_cos
        lam[i] = 2 - mu[i]
        tangent[i] = mid_sin / mid_cos
        assert mu[i] > 0 and lam[i] > 0
        # The inner face is a strict convex unit rhombus.
        vertices = (p[i], p[i + 1], z[i + 1], z[i])
        edges = [sub(vertices[(j + 1) % 4], vertices[j]) for j in range(4)]
        assert all(norm2(e) == 1 for e in edges)
        assert all(cross(edges[j], edges[(j + 1) % 4]) > 0 for j in range(4))
        assert all(norm2(sub(vertices[j], vertices[j + 2])) > 1 for j in range(2))
        area = abs(cross(chord, (F(-1), F(0))))
        assert 4 * area * area > 3
        area_sum += area
        # Unique opposite support, checked against every point of this packet.
        raw_normal = add(p[i], p[i + 1])
        assert all(dot(raw_normal, v) > 0 for key, v in points.items() if key != ('a', 0))

    equilibrium_checks = 0
    beta = 2 / radius2
    for i in indices[1:-1]:
        gamma = tangent[i] - tangent[i - 1]
        assert gamma > 0
        left, right = sub(p[i], p[i - 1]), sub(p[i], p[i + 1])
        upper = add(add(scale(lam[i - 1], left), scale(lam[i], right)), (gamma, F(0)))
        lower = sub(add(scale(mu[i - 1], left), scale(mu[i], right)), (gamma, F(0)))
        assert upper == scale(beta, p[i])
        assert lower == (0, 0)
        equilibrium_checks += 2
        # z_i lies strictly inside conv(a,p_{i-1},p_{i+1}).
        triangle = ((F(0), F(0)), p[i - 1], p[i + 1])
        signs = [cross(sub(triangle[(j + 1) % 3], triangle[j]), sub(z[i], triangle[j])) for j in range(3)]
        assert all(v > 0 for v in signs) or all(v < 0 for v in signs)

    # Exact check of the weaker rational consequence of the analytic surcharge.
    edge_count = len(indices) - 1
    lower_bound = F(edge_count * (edge_count - 1), 8) / diameter
    excess_base = area_sum - lower_bound
    assert excess_base > 0 and 4 * excess_base * excess_base >= 3 * edge_count * edge_count
    # Exact inequality used for the interior-triangle proof at D>=2.
    assert diameter >= 2
    assert 2 * (3 * diameter - 1) * (diameter - 2) >= 0
    return pair_checks, equilibrium_checks, edge_count


def main():
    pair_checks = equilibrium_checks = rhombi = 0
    for size in (8, 16, 32, 64, 128):
        p, e, r = packet(size)
        pair_checks += p
        equilibrium_checks += e
        rhombi += r
    print(f'PASS: 5 rational collars; {pair_checks} full-source pair checks; '
          f'{equilibrium_checks} exact interior equilibrium rows; {rhombi} strict rhombi')
    print('Scope: local collar regression only; no endpoint/carrier equilibrium, PSD, or global-optimality certificate.')


if __name__ == '__main__':
    main()
