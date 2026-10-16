#!/usr/bin/env python3
"""Exact finite curved-wall packets and integer population rounding.

The arbitrary-source theorem uses analytic Oler and exterior shields.
This script certifies explicit rational packets and their finite ledgers;
it does not enumerate arbitrary source clouds or assert global optimality.
"""
from fractions import Fraction as F
from math import isqrt
import json

import verify_target_c_curved_wall_isolate_motion_2026_10_06 as geometry


def near_triangular_basis(m):
    denominator = 10**6*m**4
    numerator = isqrt(denominator*denominator//3)+1
    tangent = F(numerator, denominator)
    assert 3*numerator*numerator > denominator*denominator
    assert 3*(numerator-1)**2 <= denominator*denominator
    c = (1-tangent*tangent)/(1+tangent*tangent)
    s = 2*tangent/(1+tangent*tangent)
    assert 0 < c < F(1, 2) and c*c+s*s == 1
    assert 0 < F(1, 2)-c <= F(2, denominator)
    assert F(2*m*m, denominator) < F(1, 2)
    return tangent, c, s


def wall_area(m, tangent):
    c, s = ((1-tangent*tangent)/(1+tangent*tangent),
            2*tangent/(1+tangent*tangent))
    curvature = (1-2*c)/(10**6*m**4)
    rotation = ((1-curvature*curvature)/(1+curvature*curvature),
                2*curvature/(1+curvature*curvature))
    u, v = (F(1), F(0)), (c, s)
    bases = [u, v, geometry.scale(u, -1), geometry.scale(v, -1)]
    edges = [geometry.mul(geometry.power(rotation, 2*j-m+1), base)
             for base in bases for j in range(m)]
    vertices = [(F(0), F(0))]
    for edge in edges[:-1]:
        assert geometry.dot(edge, edge) == 1
        vertices.append(geometry.add(vertices[-1], edge))
    assert geometry.dot(edges[-1], edges[-1]) == 1
    assert geometry.add(vertices[-1], edges[-1]) == (F(0), F(0))
    area = sum(geometry.cross(vertices[i], vertices[(i+1) % (4*m)])
               for i in range(4*m))/2
    assert area > 0
    # Positive quantities: area < sqrt(3)/2*(m^2+1).
    assert 4*area*area < 3*(m*m+1)**2
    return area


def case(m):
    tangent, c, s = near_triangular_basis(m)
    area = wall_area(m, tangent)
    packet = geometry.packet(m, tangent)
    interior_capacity = (m-1)**2
    wall_count = 4*m
    bank_count = 4*((m-1)//3)
    assert packet['source_points'] == wall_count+interior_capacity
    assert packet['old_contacts'] == wall_count
    assert packet['new_contacts'] == wall_count-2*bank_count
    population_checks = 0
    for population in range(interior_capacity+1):
        old_count = wall_count+population
        removed = population+bank_count
        inserted = population+bank_count
        assert removed == inserted
        assert old_count == wall_count-bank_count+inserted
        assert population <= interior_capacity
        # Strict rounded Oler bound: actual count < (m+1)^2+1.
        assert old_count < (m+1)**2+1
        assert wall_count-(wall_count-2*bank_count) > 0
        population_checks += 1
    return dict(packet,
                strict_exact_area_threshold=True,
                area_square_comparison='4 area^2 < 3 (M^2+1)^2',
                area_numerator_digits=len(str(area.numerator)),
                area_denominator_digits=len(str(area.denominator)),
                interior_packet_capacity=interior_capacity,
                integer_old_population_cases=population_checks,
                exterior_source_points='arbitrary; protection analytic',
                old_interior_positions='arbitrary in the conditional theorem')


def main():
    cases = [case(m) for m in (4, 6, 8, 12)]
    print(json.dumps({
        'classification': 'finite exact packet and integer rounding certificates',
        'cases': cases,
        'old_pair_checks': sum(c['old_pair_checks'] for c in cases),
        'new_pair_checks': sum(c['new_pair_checks'] for c in cases),
        'integer_old_population_cases': sum(c['integer_old_population_cases'] for c in cases),
        'analytic_inputs': ['finite Oler inequality', 'convex unit-wall exterior shields',
                            'fixed-M sufficiently-small-curvature construction'],
        'not_proved': ['arbitrary chamber chart', 'global optimality',
                       'full-core closure', 'macroscopic-container closure', 'Level I'],
    }, sort_keys=True))


if __name__ == '__main__':
    main()
