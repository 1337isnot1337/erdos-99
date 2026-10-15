#!/usr/bin/env python3
"""Two deleted side-wall labels fund a strict full-interior refill.

Every finite packet checks all source pairs, both moved funding labels,
all exterior guards and the maximum diameter. Global optimality and
near-wall source existence are analytic hypotheses, not certified here.
"""
from fractions import Fraction as F

from verify_target_c_loaded_flat_pentagon_second_depletion_2026_10_05 import (
    dot, rational, sign, sub,
)
from verify_target_c_vacancy_funded_unit_wall_activation_2026_10_05 import (
    RAD, V0, basis_v, full_replacement, grid_point, inside, squared, two_vacancy_packet,
)


if __name__ == "__main__":
    move_checks, strict_checks, source_checks, contact_losses = 0, 0, 0, 0
    wall_halvings = []
    for m, n in [(3, 3), (3, 4), (4, 3), (4, 4)]:
        points, wall, interior, checked, strict, halves = two_vacancy_packet(m, n, boundary_holes=True)
        assert len(interior) == (m-1)*(n-1)
        move_checks += checked
        strict_checks += strict
        target = [points[x] for x in sorted(interior)]
        for x in interior:
            assert sign(sub(rational(F(1, 10000)), squared(points[x], grid_point(*x, V0))), RAD) > 0
        gaps = [sub(squared(p, grid_point(*w, V0)), rational(1)) for p in target for w in wall]
        least = gaps[0]
        for gap in gaps:
            if sign(sub(gap, least), RAD) < 0:
                least = gap
        t, halvings = F(1, 100*m*n*(m+n)), 0
        coefficient = 8*n*(m+n+1)
        while sign(sub(least, rational(coefficient*t)), RAD) <= 0:
            t /= 2
            halvings += 1
        v = basis_v(t)
        assert dot(v, v, RAD) == rational(1)
        assert all(inside(p, m, n, v) for p in target)
        checked, lost = full_replacement(m, n, target, {(1, 1), (2, 1)}, v,
                                        funded_labels=((1, 0), (2, 0)), require_all_wall=False)
        source_checks += checked
        contact_losses += lost
        wall_halvings.append(halvings)
    # Exact relaxed crossing lower bound at tolerance eta=1/20.
    assert 4*F(19, 20)**2-1 == F(261, 100)
    assert F(261, 100) > F(151, 100)**2
    print(f"PASS: {move_checks} sequential pair checks; {strict_checks} strict final interior pairs")
    print(f"PASS: {source_checks} complete guarded source-pair checks; {contact_losses} contacts removed")
    print("PASS: both wall funding labels retained in the strict interior; all exterior labels fixed")
    print("PASS: full maximum diameter unchanged; every new/exterior distance >= 3/2")
    print(f"PASS: full triangular interior retained behind the opened wall; wall halvings {wall_halvings}")
    print("PASS: displacement < 1/100 and exact relaxed shield bound sqrt(261)/10 > 151/100")
    print("SCOPE: no packet is certified globally optimal; no uniform tolerance in growing frames")
