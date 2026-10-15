#!/usr/bin/env python3
"""Exact finite scope checks for exterior loaded-tip and paired shielding.

The universal cone, face, and cross-packet theorems are analytic. This
script checks their rational sharpness examples, actual pairs/contact
ledgers, positive equilibria, and a shared-loaded-tip failure. It proves
neither canonical cap extraction nor the missing packet population.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from pathlib import Path


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def dist2(a, b):
    d = sub(a, b)
    return dot(d, d)


def pair_check(points):
    contacts = []
    maximum = F(0)
    diameters = []
    values = []
    for i, a in enumerate(points):
        for j in range(i):
            q = dist2(a, points[j])
            dx, dy = a[0] - points[j][0], a[1] - points[j][1]
            # Independent expanded Cartesian expression.
            expanded = (a[0] ** 2 + points[j][0] ** 2
                        - 2 * a[0] * points[j][0]
                        + a[1] ** 2 + points[j][1] ** 2
                        - 2 * a[1] * points[j][1])
            assert q == dx * dx + dy * dy == expanded
            assert q >= 1, (j, i, q)
            values.append((j, i, q))
            if q == 1:
                contacts.append((j, i))
            maximum = max(maximum, q)
    diameters = [(j, i) for j, i, q in values if q == maximum]
    edges = set(contacts)
    triangles = [(a, b, c) for a in range(len(points))
                 for b in range(a + 1, len(points))
                 for c in range(b + 1, len(points))
                 if {(a, b), (a, c), (b, c)} <= edges]
    return {"pair_checks": len(values), "contacts": contacts,
            "diameter_squared": maximum, "diameters": diameters,
            "triangles": triangles}


def inside_convex(x, polygon):
    return all(cross(sub(polygon[(i + 1) % len(polygon)], a), sub(x, a)) > 0
               for i, a in enumerate(polygon))


def right_angle_tip():
    v, w = (F(0), F(0)), (F(1), F(0))
    polygon = [v, w, (F(0), F(10))]
    samples = []
    for denominator in (10, 100, 1000, 10000):
        t = F(1, denominator)
        x = (t * t / 4, t)
        assert inside_convex(x, polygon)
        assert dist2(x, w) == 1 + t * t / 2 + t ** 4 / 16 > 1
        assert dist2(x, v) < 1
        samples.append({"t": t, "site": x, "guard_squared": dist2(x, w)})
    # Acute arctan(4/3) cone: the analytic radius gap is 2*cos(theta).
    tangent = (F(3, 5), F(4, 5))
    assert dot(tangent, tangent) == 1
    assert 2 * tangent[0] == F(6, 5)
    return {"samples": samples, "acute_cone_cosine": tangent[0],
            "acute_cone_radius_gap": F(6, 5)}


def sharp_half_turn():
    a, b, c = ((F(24, 25), F(7, 25)),
               (F(-24, 25), F(7, 25)), (F(0), F(-1)))
    wall = [b, add(b, c), c, add(c, a), a]
    x = (F(0), F(0))
    assert inside_convex(x, wall)
    edges = [sub(wall[i + 1], wall[i]) for i in range(4)]
    assert all(dot(e, e) == 1 for e in edges)
    assert all(cross(edges[i], edges[i + 1]) > 0 for i in range(3))
    # Monotone directions from downward to upward sweep exactly pi.
    assert edges[0] == (F(0), F(-1))
    assert edges[-1] == (F(0), F(1))
    result = pair_check(wall + [x])
    assert result["pair_checks"] == 15
    assert len(result["contacts"]) == 7
    assert not result["triangles"]
    assert [dist2(x, w) for w in wall] == [1, F(36, 25), 1, F(36, 25), 1]
    weights = [F(25, 14), F(25, 14), F(1)]
    neighbors = [a, b, c]
    equilibrium = tuple(sum(weight * p[k] for weight, p in zip(weights, neighbors))
                        for k in (0, 1))
    assert equilibrium == (0, 0)
    assert cross(a, b) != 0
    # Guard inequalities imply |X|<=2*r^2/3 and |Y|<=25*r^2/14.
    # At r<1/2 these bounds contradict r^2=X^2+Y^2.
    isolation_coefficient = (F(2, 3) ** 2 + F(25, 14) ** 2) / 4
    assert isolation_coefficient < 1
    result.update({"wall": wall, "site": x, "anchor_weights": weights,
                   "equilibrium": equilibrium, "wall_turn": "pi",
                   "isolated_neighborhood_radius": F(1, 2),
                   "isolation_coefficient": isolation_coefficient})
    return result


def shared_loaded_tip(length):
    assert length >= 26
    chain = [(F(k), F(0)) for k in range(length + 1)]
    hp, hm = (F(1), F(7)), (F(1), F(-7))
    old = chain + [hp, hm]
    result = pair_check(old)
    assert result["diameter_squared"] == length * length
    assert result["diameters"] == [(0, length)]
    assert result["contacts"] == [(k, k + 1) for k in range(length)]
    assert not result["triangles"]
    assert all(i <= length and j <= length for i, j in result["contacts"])
    xp, xm = (F(1, 20), F(1, 3)), (F(1, 20), F(-1, 3))
    qp = [chain[0], chain[-1], hp]
    qm = [chain[0], hm, chain[-1]]
    assert inside_convex(xp, qp) and inside_convex(xm, qm)
    assert dist2(xp, chain[1]) == dist2(xm, chain[1]) == F(3649, 3600) > 1
    assert dist2(xp, chain[0]) == dist2(xm, chain[0]) == F(409, 3600) < 1
    assert dist2(xp, xm) == F(4, 9) < 1
    endpoint_counts = []
    for x in (xp, xm):
        endpoint = [x] + old[1:]
        checked = pair_check(endpoint)
        assert checked["diameter_squared"] < length * length
        assert len(checked["contacts"]) == length - 1
        assert not checked["triangles"]
        endpoint_counts.append(checked)
    # Positive normalized mixed equilibrium on the original collinear core.
    for i, p in enumerate(chain):
        force = [F(0), F(0)]
        for j in (i - 1, i + 1):
            if 0 <= j <= length:
                d = sub(p, chain[j])
                force = [force[k] + length * d[k] for k in (0, 1)]
        if i in (0, length):
            other = chain[length if i == 0 else 0]
            d = sub(p, other)
            force = [force[k] - d[k] for k in (0, 1)]
        assert force == [0, 0]
    result.update({"length": length, "source": old,
                   "new_sites": [xp, xm], "cross_squared": F(4, 9),
                   "single_site_endpoints": endpoint_counts,
                   "mixed_rank": length, "canonical_required_rank": 2 * length - 1,
                   "missing_canonical_hypotheses": ["two-dimensional force hull",
                                                    "unloaded degree at least three",
                                                    "full mixed core rigidity",
                                                    "global minimum diameter"]})
    return result


def serial(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {k: serial(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serial(v) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    record = {"classification": "exact finite scope regressions; not cap closure",
              "right_angle_tip": right_angle_tip(),
              "half_turn_sharpness": sharp_half_turn(),
              "shared_loaded_tips": [shared_loaded_tip(length) for length in (26, 40)]}
    pair_total = record["half_turn_sharpness"]["pair_checks"]
    for example in record["shared_loaded_tips"]:
        pair_total += example["pair_checks"]
        pair_total += sum(endpoint["pair_checks"] for endpoint in example["single_site_endpoints"])
    record["total_pair_checks"] = pair_total
    record["limits"] = ["universal cone and gluing implications require analytic proofs",
                        "no canonical cap packet population is supplied",
                        "shared-tip source is collinear and nonglobal",
                        "no asymptotic optimality or Level I conclusion"]
    if args.output:
        args.output.write_text(json.dumps(serial(record), indent=2) + "\n")
    print(f"PASS: {pair_total} exact old/endpoint pair checks; right-angle opening, "
          "sharp half-turn pin, and shared-loaded-tip cross failure")


if __name__ == "__main__":
    main()
