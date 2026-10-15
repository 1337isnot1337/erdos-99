#!/usr/bin/env python3
"""Exact exterior-cap discovery packet, not a canonical-source certificate.

Uses the spoke/isolate family defined in the accompanying reports. Deletes
two unloaded seam guards, translates both retained core shores by 1/10,
retains every isolate, and adds two interior exact-contact sites. All source
and endpoint pairs are independently checked in integer triangular-basis
and Cartesian-radical arithmetic. No numerical rank/optimality assertion.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from verify_target_c_paired_cap_spoke_comparison_2026_10_06 import (
    NEIGHBORS, RAYS, add, cartesian_norm2_times4, mul, norm2, sub,
)


def check_pairs(points, den, old_diam2):
    contacts, diameters = [], []
    minimum, maximum, checked = None, 0, 0
    for i, p in enumerate(points):
        for j in range(i):
            delta = sub(p, points[j])
            q = norm2(delta)
            assert cartesian_norm2_times4(delta) == 4 * q
            assert q >= den * den, (i, j, q, den * den)
            assert q <= old_diam2
            minimum = q if minimum is None else min(minimum, q)
            maximum = max(maximum, q)
            if q == den * den:
                contacts.append((j, i))
            if q == old_diam2:
                diameters.append((j, i))
            checked += 1
    return contacts, diameters, minimum, maximum, checked


def run(m):
    assert m >= 20
    den = 100 * m * m
    snum = den + 1
    core = [mul(k, v) for v in RAYS for k in range(1, m + 1)]
    guards = {add(p, d) for p in core for d in NEIGHBORS}
    cloud_indices = [(i, j) for i in range(-2 * m, 2 * m + 1)
                     for j in range(-2 * m, 2 * m + 1)
                     if 16 * norm2((i, j)) <= (4 * m - 1) ** 2
                     and (i, j) not in guards]
    old = [mul(den, p) for p in core]
    old += [mul(snum, p) for p in cloud_indices]
    diam2 = 4 * m * m * den * den
    old_c, old_h, _, old_max, old_checks = check_pairs(old, den, diam2)
    assert old_max == diam2 and len(old_c) == 6 * m and len(old_h) == 3

    # w=(-1,1) in the triangular basis; w dot (i,j)=(j-i)/2.
    # Exactly two old contacts cross w dot p=0. Delete their left ends.
    crossing = [(i, j) for i, j in old_c
                if (old[i][1] - old[i][0]) * (old[j][1] - old[j][0]) < 0]
    assert len(crossing) == 2
    removed = {i if old[i][1] - old[i][0] < 0 else j
               for i, j in crossing}
    assert {core[i] for i in removed} == {(1, 0), (0, -1)}
    assert all(i < 6 * m for i in removed)
    assert not any(i in removed or j in removed for i, j in old_h)

    endpoint, old_labels = [], []
    for i, p in enumerate(old):
        if i in removed:
            continue
        if i < 6 * m:
            side = 1 if p[1] - p[0] > 0 else -1
            p = add(p, mul(-side * den // 10, (-1, 1)))
        endpoint.append(p)
        old_labels.append(i)
    sites = [add(mul(den, (k + 1, -1)), mul(den // 10, (-1, 1)))
             for k in (3, 5)]
    endpoint += sites
    assert len(endpoint) == len(old) == len(set(endpoint))
    new_c, new_h, _, new_max, new_checks = check_pairs(endpoint, den, diam2)
    assert not new_h and new_max < diam2
    expected_max = 4 * m * m * den * den - (2 * m * den * den) // 5 + den * den // 25
    assert new_max == expected_max

    old_to_new = {label: i for i, label in enumerate(old_labels)}
    surviving = {(old_to_new[i], old_to_new[j]) for i, j in old_c
                 if i not in removed and j not in removed}
    assert surviving <= set(new_c)
    lost_contacts = len(old_c) - len(surviving)
    packet_contacts = set(new_c) - surviving
    assert lost_contacts == 6 and len(packet_contacts) == 4
    assert len(new_c) == 6 * m - 2
    assert all(i >= len(endpoint) - 2 or j >= len(endpoint) - 2
               for i, j in packet_contacts)
    assert all(endpoint[old_to_new[i]] == old[i]
               for i in range(6 * m, len(old)))

    adjacency = [set() for _ in endpoint]
    for i, j in new_c:
        adjacency[i].add(j)
        adjacency[j].add(i)
    triangles = {tuple(sorted((i, j, k))) for i, j in new_c
                 for k in adjacency[i] & adjacency[j]}
    assert len(triangles) == 2  # Allowed: every full-source upper distance is <D.

    # Independently open every new contact using a common downward motion.
    # A finite bound from all nonunit pairs gives a rational safe step.
    # The derivative on each of the four packet contacts is strictly positive.
    velocity = (1, -2)  # Cartesian (0,-sqrt(3)).
    new_unit2 = den * den
    active_derivatives = []
    for i, j in packet_contacts:
        pi = i if i >= len(endpoint) - 2 else j
        pj = j if pi == i else i
        d = sub(endpoint[pi], endpoint[pj])
        derivative_times2 = (2 * d[0] + d[1]) * velocity[0] + (d[0] + 2 * d[1]) * velocity[1]
        assert derivative_times2 > 0
        active_derivatives.append(derivative_times2)
    # The exact continuity bound chooses t=1/(large integer), without floating
    # distances: |d|<2M, |v|<2; squared variation <=8M t+4t^2.
    strict_lower_gap_num = min(norm2(sub(endpoint[i], endpoint[j])) - new_unit2
                               for i in range(len(endpoint) - 2, len(endpoint))
                               for j in range(len(endpoint) - 2)
                               if norm2(sub(endpoint[i], endpoint[j])) > new_unit2)
    upper_gap_num = diam2 - new_max
    gap_num = min(strict_lower_gap_num, upper_gap_num)
    step_den = (16 * m + 8) * den * den
    # t = gap_num/step_den; scale coordinates by step_den to verify the actual
    # finite endpoint. This is <=1/2 since all gaps are at most D^2 in this case.
    assert 0 < 2 * gap_num <= step_den
    opened = [mul(step_den, p) for p in endpoint]
    for i in range(len(opened) - 2, len(opened)):
        opened[i] = add(opened[i], mul(den * gap_num, velocity))
    opened_den = den * step_den
    opened_diam2 = 4 * m * m * opened_den * opened_den
    op_c, op_h, _, op_max, op_checks = check_pairs(opened, opened_den, opened_diam2)
    assert len(op_c) == 6 * m - 6 and not op_h and op_max < opened_diam2
    assert set(op_c) == surviving

    record = {
        "M": m, "source_population": len(old), "original_D": 2 * m,
        "deleted_unloaded_core_sites": [list(core[i]) for i in sorted(removed)],
        "isolate_population_retained": len(cloud_indices),
        "shore_translation": {"unit_vector_basis": [-1, 1], "amplitude": [1, 10]},
        "inserted_site_basis_coordinates": [[[10 * (k + 1) - 1, -9], 10] for k in (3, 5)],
        "old_contacts": len(old_c), "old_actual_diameters": len(old_h),
        "old_contact_loss": lost_contacts, "packet_contact_count": len(packet_contacts),
        "initial_competitor_triangles": len(triangles),
        "competitor_diameter_squared": [new_max, den * den],
        "triangle_free_competitor_contacts": len(op_c),
        "triangle_free_packet_step": [gap_num, step_den],
        "old_pair_checks": old_checks, "competitor_pair_checks": new_checks,
        "triangle_free_endpoint_pair_checks": op_checks,
        "canonical_rank_count_failure": {"e_plus_h": 6 * m + 3, "required": 12 * m - 2},
    }
    finite = {
        "coordinate_basis": ["(1,0)", "(1/2,sqrt(3)/2)"],
        "coordinate_denominator": den,
        "old_coordinates": old, "new_coordinates": endpoint,
        "new_to_old_retained_labels": old_labels,
        "new_contact_pairs": new_c,
        "triangle_free_coordinate_denominator": opened_den,
        "triangle_free_coordinates": opened,
    }
    return record, finite


def rhombus_regression():
    # |d|^2=1; q dot d=(3+2sqrt(30))/14. Squaring the positive
    # rational endpoints certifies 2<sqrt(30)<11/2, so 0<gap<1.
    assert 3 * 3 + 40 == 7 * 7
    assert 4 < 30 and 4 * 30 < 121
    assert 8 > 7 and 20 > 7
    return {
        "rhombus_cartesian_coordinates": ["(0,0)", "(1,0)",
                                           "(10/7,2*sqrt(10)/7)",
                                           "(3/7,2*sqrt(10)/7)"],
        "unit_boundary_squared_length": 1,
        "diagonal_squared_lengths": [[8, 7], [20, 7]],
        "equilateral_completion": "(1/2,sqrt(3)/2)",
        "blocked_squared_distance": "(11-2*sqrt(30))/7",
        "certified_range": "0 < squared distance < 1",
        "scope": "local strict-rhombus regression, not a canonical source",
    }


def partial_wall_regression():
    points = [(0, 0), (10, 0), (20, 0), (0, 10), (20, 10), (10, 17)]
    candidate = (10, 8)
    sq = lambda p, q: (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
    pairs = [sq(points[i], points[j]) for i in range(len(points)) for j in range(i)]
    assert len(pairs) == 15 and min(pairs) == 100 and pairs.count(100) == 4
    assert all(sq(points[-1], p) > 100 for p in points[:-1])
    guard_squared = [sq(candidate, points[i]) for i in (0, 2, 3, 4)]
    assert guard_squared == [164, 164, 104, 104]
    assert sq(candidate, points[-1]) == 81 < 100
    assert 0 < candidate[0] < 20 and 0 < candidate[1] < 10
    assert points[-1][1] > 10  # The nonunit top side is not on partial(K).
    return {
        "coordinate_denominator": 10, "old_cartesian_numerators": points,
        "candidate_cartesian_numerator": candidate, "deleted_label": 1,
        "guard_squared_distances": [[q, 100] for q in guard_squared],
        "retained_isolate_label": 5, "failed_squared_distance": [81, 100],
        "old_pair_checks": len(pairs), "old_contact_count": pairs.count(100),
        "violated_hypothesis": "nonunit unguarded top side is inside the source hull",
        "scope": "rational local partial-wall regression, not a canonical source",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    records, finite = [], None
    for m in (20, 32):
        record, packet = run(m)
        records.append(record)
        if m == 20:
            finite = packet
        print(f"M={m}: n={record['source_population']}; remove 2, add 2; "
              f"old contacts lost 6, new contacts 4; strict D; "
              f"all {3 * record['old_pair_checks']} exact pair checks PASS", flush=True)
    result = {
        "status": "proved finite nonglobal exterior-cap discovery packet",
        "not_proved": ["canonical source realization", "forced interior vacancies",
                       "universal cap-fed seam refill", "C-II or Level I closure"],
        "instances": records, "finite_M20_instance": finite,
        "rejected_edge_to_vacancy_inference": rhombus_regression(),
        "rejected_interior_nonunit_wall_opening": partial_wall_regression(),
    }
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
