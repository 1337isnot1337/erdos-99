#!/usr/bin/env python3
"""Exact nonglobal fixtures for finite isolate diameter normalization.

This checks simultaneous all-pair feasibility in rational examples and two
necessary hypotheses. It does not prove the analytic lemma, source optimality,
the core replacement theorem, the cubic moment, or a C-II endpoint.
"""

from fractions import Fraction as F
from itertools import combinations
import json


def dist2(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def pairs(points):
    return list(combinations(range(len(points)), 2))


def contacts(points):
    return {ij for ij in pairs(points) if dist2(*(points[i] for i in ij)) == 1}


def diameters(points, diameter2):
    return {
        ij for ij in pairs(points) if dist2(*(points[i] for i in ij)) == diameter2
    }


def normalize(points, core, diameter2, t=None):
    core = tuple(core)
    if not core:
        raise ValueError("a nonempty retained core is required")
    core_set = set(core)
    isolates = set(range(len(points))) - core_set
    if any(
        dist2(*(points[i] for i in ij)) < 1
        or dist2(*(points[i] for i in ij)) > diameter2
        for ij in pairs(points)
    ):
        raise ValueError("initial source pair bounds fail")
    if any(set(ij) & isolates for ij in contacts(points)):
        raise ValueError("a proposed isolate has a unit contact")
    if not isolates:
        return tuple(points), F(0), None
    sigma = min(
        dist2(*(points[i] for i in ij)) - 1
        for ij in pairs(points)
        if set(ij) & isolates
    )
    if sigma <= 0:
        raise ValueError("strict isolate lower slack is required")
    t0 = sigma / (8 * diameter2)
    if t is None:
        t = t0
    if not 0 < t <= t0:
        raise ValueError("contraction is outside the certified interval")
    anchor = tuple(
        sum(points[i][axis] for i in core) / len(core) for axis in range(2)
    )
    result = tuple(
        p if i in core_set else tuple((1 - t) * x + t * y for x, y in zip(p, anchor))
        for i, p in enumerate(points)
    )
    return result, t, sigma


def verify():
    core = tuple(range(6))
    points = tuple((F(i), F(0)) for i in core) + (
        (F(3), F(4)),
        (F(1), F(3)),
    )
    diameter2 = F(25)
    isolates = {6, 7}
    old_contacts = contacts(points)
    old_diameters = diameters(points, diameter2)
    assert old_contacts == {(i, i + 1) for i in range(5)}
    assert old_diameters == {(0, 5), (0, 6), (5, 7)}
    assert max(dist2(points[i], points[j]) for i, j in pairs(points)) == diameter2
    normalized, t0, sigma = normalize(points, core, diameter2)
    assert t0 == F(1, 50) and sigma == 4
    checked_pairs = 0
    for t in (t0, t0 / 2, t0 / 100):
        moved, used_t, used_sigma = normalize(points, core, diameter2, t)
        assert used_t == t and used_sigma == sigma
        assert contacts(moved) == old_contacts
        assert diameters(moved, diameter2) == {(0, 5)}
        assert all(moved[i] == points[i] for i in core)
        for i, j in pairs(points):
            value = dist2(moved[i], moved[j])
            assert 1 <= value <= diameter2
            if {i, j} & isolates:
                assert value >= 1 + sigma / 2
                assert value < diameter2
                upper_factor = 1 - t if {i, j} <= isolates else 1 - t / len(core)
                assert value <= diameter2 * upper_factor ** 2
            if {i, j} <= isolates:
                assert value == (1 - t) ** 2 * dist2(points[i], points[j])
            checked_pairs += 1
    assert normalized == normalize(points, core, diameter2, t0)[0]

    # A unit neighbor cannot be treated as a contact isolate.
    nonisolate_fixture = points[:6] + ((F(1), F(1)),)
    try:
        normalize(nonisolate_fixture, core, diameter2)
    except ValueError as error:
        assert "unit contact" in str(error)
    else:
        raise AssertionError("the nonisolate fixture should be rejected")
    anchor = (F(5, 2), F(0))
    p = nonisolate_fixture[-1]
    illegally_moved = tuple((1 - t0) * x + t0 * y for x, y in zip(p, anchor))
    assert dist2(illegally_moved, nonisolate_fixture[1]) < 1

    # An arbitrary external anchor can violate an active diameter upper bound.
    bad_anchor = (F(100), F(0))
    p = points[6]
    badly_moved = tuple((1 - t0) * x + t0 * y for x, y in zip(p, bad_anchor))
    assert dist2(badly_moved, points[0]) > diameter2

    unchanged, t, empty_sigma = normalize(points[:6], core, diameter2)
    assert unchanged == points[:6] and t == 0 and empty_sigma is None
    print(
        json.dumps(
            {
                "status": "PASS",
                "arithmetic": "exact rational squared distances",
                "source_labels": len(points),
                "simultaneously_moved_isolates": len(isolates),
                "all_pair_checks": checked_pairs,
                "contacts_preserved": len(old_contacts),
                "isolate_diameter_pairs_opened": len(old_diameters) - 1,
                "negative_hypothesis_fixtures": 2,
                "global_optimality_certified": False,
                "endpoint_constructed": False,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    verify()
