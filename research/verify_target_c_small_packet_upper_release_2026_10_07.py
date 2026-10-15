#!/usr/bin/env python3
"""Rational nonglobal fixtures for simultaneous small-packet upper release.

Checks a common certified time interval, every source pair, and two failures
outside the hypotheses. Does not prove global optimality, the general analytic
lemma, arbitrary-source packet existence, C-II, or Level I.
"""

from fractions import Fraction as F
from itertools import combinations
import json


def vector(a, b):
    return tuple(x - y for x, y in zip(a, b))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def dist2(a, b):
    difference = vector(a, b)
    return dot(difference, difference)


def pair_set(points, value):
    return {
        (i, j)
        for i, j in combinations(range(len(points)), 2)
        if dist2(points[i], points[j]) == value
    }


def certify(points, retained, packets, centers, origin, radius, rho, diameter):
    retained = set(retained)
    owner = {}
    for packet_id, packet in enumerate(packets):
        assert packet
        for index in packet:
            assert index not in retained and index not in owner
            owner[index] = packet_id
    assert retained | set(owner) == set(range(len(points)))
    assert len(centers) == len(packets)
    assert diameter > 0 and radius >= diameter / 2
    assert radius + 2 * rho < diameter
    diameter2 = diameter ** 2
    assert all(dist2(p, origin) <= radius ** 2 for p in points)
    assert all(
        dist2(points[index], centers[packet_id]) <= rho ** 2
        for index, packet_id in owner.items()
    )
    pairs = list(combinations(range(len(points)), 2))
    initial = {ij: dist2(points[ij[0]], points[ij[1]]) for ij in pairs}
    assert min(initial.values()) >= 1
    assert max(initial.values()) == diameter2
    involving = [ij for ij in pairs if any(i in owner for i in ij)]
    strict_lower = [
        ij for ij in involving
        if not all(i in owner for i in ij)
        or owner[ij[0]] != owner[ij[1]]
    ]
    assert all(initial[ij] > 1 for ij in strict_lower)
    lower_slacks = [initial[ij] - 1 for ij in strict_lower]
    upper_slacks = [
        diameter2 - initial[ij] for ij in involving if initial[ij] < diameter2
    ]
    alpha = min(
        diameter * (diameter - radius - 2 * rho),
        diameter * (diameter - 4 * rho),
    )
    assert alpha > 0
    bounds = [F(1, 2), alpha / (4 * diameter2)]
    sigma = min(lower_slacks) if lower_slacks else None
    lam = min(upper_slacks) if upper_slacks else None
    if sigma is not None:
        bounds.append(sigma / (8 * diameter2))
    if lam is not None:
        bounds.append(lam / (16 * diameter2))
    time = min(bounds)
    assert time > 0
    velocities = tuple(
        (F(0), F(0)) if i in retained else tuple(
            origin[axis] + p[axis] - 2 * centers[owner[i]][axis]
            for axis in range(2)
        )
        for i, p in enumerate(points)
    )
    assert all(dot(v, v) < diameter2 for i, v in enumerate(velocities) if i in owner)
    for i, j in involving:
        if initial[i, j] == diameter2:
            linear = dot(vector(points[i], points[j]),
                         vector(velocities[i], velocities[j]))
            assert linear <= -alpha
    return time, sigma, lam, alpha, velocities, involving, strict_lower


def fixture(points, retained, packets, centers, expected_diameters):
    points = tuple(tuple(F(x) for x in p) for p in points)
    origin = (F(0), F(0))
    radius, rho, diameter = F(32), F(1), F(64)
    assert pair_set(points, diameter ** 2) == expected_diameters
    old_contacts = pair_set(points, F(1))
    assert len(old_contacts) == 4
    time, sigma, lam, alpha, velocities, involving, strict_lower = certify(
        points, retained, packets, centers, origin, radius, rho, diameter
    )
    checked = 0
    for t in (time, time / 2, time / 100):
        moved = tuple(
            tuple(p[axis] + t * velocities[i][axis] for axis in range(2))
            for i, p in enumerate(points)
        )
        assert all(moved[i] == points[i] for i in retained)
        for i, j in combinations(range(len(points)), 2):
            value = dist2(moved[i], moved[j])
            assert 1 <= value <= diameter ** 2
            if (i, j) in involving:
                assert 1 < value < diameter ** 2
                old_value = dist2(points[i], points[j])
                if old_value == diameter ** 2:
                    assert value <= diameter ** 2 - alpha * t
                else:
                    assert value <= diameter ** 2 - lam / 2
            if (i, j) in strict_lower:
                assert value >= 1 + sigma / 2
            checked += 1
        assert pair_set(moved, F(1)) == set()
        assert pair_set(moved, diameter ** 2) == {
            ij for ij in expected_diameters if set(ij) <= set(retained)
        }
    return checked, str(time), len(expected_diameters)


def verify():
    packets = ((2, 3, 4), (5, 6, 7))
    first = fixture(
        ((0, -32), (32, 0), (0, 32), (0, 31), (1, 31),
         (-32, 0), (-31, 0), (-31, 1)),
        (0, 1), packets,
        ((F(1, 2), F(63, 2)), (F(-63, 2), F(1, 2))),
        {(0, 2), (1, 5)},
    )
    second = fixture(
        ((-32, 0), (32, 0), (0, 32), (0, 31), (1, 31),
         (0, -32), (0, -31), (1, -31)),
        (0, 1), packets,
        ((F(1, 2), F(63, 2)), (F(1, 2), F(-63, 2))),
        {(0, 1), (2, 5)},
    )

    # Strict cross lower slack is essential even for a singleton packet.
    anchor = (F(0), F(0))
    singleton = (F(0), F(1))
    origin = (F(1, 2), F(1, 2))
    t = F(1, 100)
    moved_singleton = tuple((1 - t) * p + t * o
                            for p, o in zip(singleton, origin))
    assert dist2(singleton, anchor) == 1
    assert dist2(moved_singleton, anchor) == 1 - t + t * t / 2 < 1

    # Without the size condition, internal dilation can enlarge the diameter.
    square = tuple((F(x), F(y)) for x, y in ((0, 0), (1, 0), (1, 1), (0, 1)))
    center = (F(1, 2), F(1, 2))
    dilated = tuple(tuple(c + (1 + t) * (p - c) for p, c in zip(point, center))
                    for point in square)
    assert max(dist2(a, b) for a, b in combinations(square, 2)) == 2
    assert max(dist2(a, b) for a, b in combinations(dilated, 2)) == 2 * (1 + t) ** 2 > 2

    return {
        "status": "PASS",
        "arithmetic": "exact rational",
        "scope": "finite nonglobal fixtures; no packet existence or Level I claim",
        "all_pair_checks": first[0] + second[0],
        "certified_times": [first[1], second[1]],
        "initial_unit_contacts_per_fixture": 4,
        "initial_diameter_pairs_per_fixture": [first[2], second[2]],
        "hypothesis_failure_fixtures": 2,
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
