#!/usr/bin/env python3
"""Exact finite reduction and guardrail for the large-face fold candidate.

This verifies the seven-case arithmetic and a rational short-cycle chord.
Canonical source hypotheses, pinned-rank universality, and geometric neighbor
disjointness are analytic claims in the report, not encoded by this script.
"""

from fractions import Fraction as F
from itertools import product
from math import isqrt
import json
import verify_target_c_quarter_fold_face_obstructions_2026_10_10 as g


def finite_arc_reduction():
    # delta<=5 and chord>(sqrt(3)/2)*r give 3*r^2<100.
    assert 3*5**2 < 100 < 3*6**2
    admissible = []
    for r in product(range(2, 6), repeat=4):
        if any(3*max(r[i],r[i+2])**2 >= 4*min(r[i],r[i+2])**2
               for i in (0,1)):
            continue
        assert r[0] == r[2] and r[1] == r[3]
        if 3*(r[0]**2+r[1]**2) >= 100:
            continue
        admissible.append(r)
    pairs = sorted({tuple(sorted(r[:2])) for r in admissible})
    assert pairs == [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,4)]
    scale = 10**15
    root = isqrt(3*scale*scale)
    sqrt_lo, sqrt_hi = F(root,scale), F(root+1,scale)
    assert sqrt_lo**2 < 3 < sqrt_hi**2
    rows = []
    for a,b in pairs:
        wall = 2*(a+b)
        if a == b == 2:
            distinct = 4
        elif a == 2:
            distinct = b+1
        else:
            distinct = wall-4
        needed = wall+distinct
        constant, coefficient = a+b+1, 2*a*b
        gap_integer = needed-constant
        assert gap_integer > 0
        assert 3*gap_integer**2 > coefficient**2
        upper_lo = F(coefficient)/sqrt_hi + constant
        upper_hi = F(coefficient)/sqrt_lo + constant
        assert upper_lo < upper_hi < needed
        rows.append({'opposite_arc_counts': [a,b,a,b],
                     'wall_labels': wall,
                     'minimum_distinct_intruding_labels': distinct,
                     'minimum_total_labels_in_hull': needed,
                     'strict_Oler_upper_bound': f'{coefficient}/sqrt(3)+{constant}',
                     'strict_Oler_upper_rational_enclosure': [str(upper_lo),str(upper_hi)],
                     'squared_gap_certificate': {'left':3*gap_integer**2,
                                                'right':coefficient**2}})
    return {'ordered_arc_vectors_examined': 4**4,
            'ordered_admissible_vectors': admissible,
            'unordered_seven_cases': rows,
            'scope': 'arithmetic reduction assuming analytic four-pin and neighbor claims'}


def short_cycle_chord_guardrail():
    # Two unit rhombi glued along A--B. Their outer six-cycle is nonconvex
    # and contains the A--B chord; no extra vertex is inside that cycle.
    points = [g.point(-F(12,13),F(5,13)),
              g.point(-F(12,13),F(18,13)),
              g.point(0,1),
              g.point(F(12,13),F(18,13)),
              g.point(F(12,13),F(5,13)),
              g.point(0,0)]
    ledger, contacts, diameter = g.ledger(points)
    assert contacts == g.cycle_edges(6) | {(2,5)}
    assert g.area(points).sign() < 0
    turns = g.turns(points)
    assert turns[2] > 0
    assert any(t < 0 for t in turns)
    return {'labels': [[str(q.a) for q in p] for p in points],
            'full_pair_checks': len(ledger),
            'contact_edges': sorted(contacts),
            'interior_chord': [2,5],
            'signed_area': g.area(points).encode(),
            'turn_signs': turns, 'diameter_squared': diameter.encode(),
            'scope': 'unit-separated triangle-free finite guardrail; not a canonical minimizer'}


def main():
    print(json.dumps({'seven_case_reduction':finite_arc_reduction(),
                      'short_cycle_with_chord':short_cycle_chord_guardrail(),
                      'scope':'exact finite arithmetic; universal geometry remains analytic'},
                     indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
