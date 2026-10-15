#!/usr/bin/env python3
"""Finite unit-grid checks of joint physical separator/perimeter capacity.

Pinned square grids have exact positive unloaded equilibrium and full pinned
rank, but their boundary pins are not all actual diameter endpoints. They are
not canonical global minimizers. Exact interval arithmetic and integral flows
check the finite perimeter proof ingredients, not the universal theorem or
the Type-II asymptotic assumptions.
"""

from fractions import Fraction as F
from verify_target_c_global_face_return_quotas_2026_10_04 import (
    edge, components, face_walks, separator,
)


def atan_interval(x, terms):
    partial = sum(((-1)**j)*x**(2*j+1)/F(2*j+1) for j in range(terms))
    following = ((-1)**terms)*x**(2*terms+1)/F(2*terms+1)
    return min(partial, partial+following), max(partial, partial+following)


def constants():
    a, b = atan_interval(F(1, 5), 24)
    c, d = atan_interval(F(1, 239), 8)
    pi_lo, pi_hi = 16*a-4*d, 16*b-4*c
    rt_lo, rt_hi = F(17, 10), F(18, 10)
    for _ in range(70):
        middle = (rt_lo+rt_hi)/2
        if middle*middle < 3:
            rt_lo = middle
        else:
            rt_hi = middle
    assert F(314159, 100000) < pi_lo < pi_hi < F(314160, 100000)
    return pi_lo, pi_hi, rt_lo, rt_hi


def check_grid(side, bounds):
    vertices = {(i, j) for i in range(side) for j in range(side)}
    pins = {v for v in vertices if min(v) == 0 or max(v) == side-1}
    contacts = {edge(v, w) for v in vertices for w in ((v[0]+1, v[1]), (v[0], v[1]+1)) if w in vertices}
    rhombi = [frozenset(((i, j), (i+1, j), (i+1, j+1), (i, j+1)))
              for i in range(1, side-2) for j in range(1, side-2)]
    starts = set().union(*rhombi)
    # All interior vertices have four neighbors with opposite unit directions
    # and positive coefficient one. Pinned rank follows exactly: every row's
    # horizontal x velocities propagate to zero at its two boundary pins,
    # and every column's vertical y velocities propagate to zero likewise.
    positions = {v: v for v in vertices}
    minimal = separator(vertices, contacts, pins, starts)
    checked = 0
    for cut in (minimal, pins, minimal | {(side//2, side//2)}):
        remaining = vertices-cut
        remaining_edges = {e for e in contacts if set(e) <= remaining}
        unpinned = [comp for comp in components(remaining, remaining_edges) if comp & (starts-cut)]
        assert all(not (comp & pins) for comp in unpinned)
        bulk = set().union(*unpinned) if unpinned else set()
        retained = bulk | cut
        k_edges = {e for e in contacts if set(e) <= retained}
        k_components = components(retained, k_edges)
        walks = face_walks(retained, k_edges, positions)
        b = sum(len(walk) for walk, area in walks if area <= 0)
        q = sum(len(walk)-4 for walk, area in walks if area > 0)
        assert q >= 0
        e_s = sum(set(e) <= cut for e in k_edges)
        r0 = sum(not (face & cut) for face in rhombi)
        assert all(face <= bulk for face in rhombi if not (face & cut))
        k_i = len(cut-pins)
        assert len(rhombi)-r0 <= 5*k_i
        budget = 4*len(cut)-2*len(unpinned)-4*len(k_components)-2*e_s
        assert b+q == 4*len(retained)-2*len(k_edges)-4*len(k_components)
        assert b+q <= budget
        _, pi_hi, _, rt_hi = bounds
        assert 2*pi_hi*rt_hi*r0 <= b*b
        if len(rhombi) > 5*k_i:
            assert 2*pi_hi*rt_hi*(len(rhombi)-5*k_i) <= (4*len(cut)-6)**2
        checked += 1
    return checked, len(rhombi)


if __name__ == '__main__':
    interval_bounds = constants()
    packets = 0
    largest = 0
    for width in (5, 8, 15, 30):
        count, rhombus_count = check_grid(width, interval_bounds)
        packets += count
        largest = max(largest, rhombus_count)
    # Closed finite circular-cut arithmetic, independent of source realization.
    for j in range(1001):
        r = F(j, 100)
        outer = 4*((r+F(3, 2))**2-max(F(0), r-F(1, 2))**2)
        assert outer <= 16*r+9
    print(f'PASS: {packets} exact unit-grid separator packets; largest bulk {largest} rhombi')
    print('PASS: 1001 annular packing bounds; pi/sqrt(3) interval perimeter-capacity checks')
    print('Scope: fixed pinned unit grids, not all pins actual diameter endpoints, not global minimizers or Level I closure.')
