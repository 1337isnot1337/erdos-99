#!/usr/bin/env python3
"""Exact nonglobal geometry/flow fixtures for harmonic-cell cap extraction.

Boundary terminals are artificial pins, not certified diameter endpoints.
This checks finite crops and actual contact suffixes; it does not certify
canonical source stress, pseudosegment extraction, or global optimality.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import json

from verify_target_c_train_cut_hull_bank_2026_10_08 import contact_separator


def edge(a, b):
    return tuple(sorted((a, b)))


def metric2(a, b):
    i, j = a[0] - b[0], a[1] - b[1]
    return 13*i*i + 13*j*j + 10*i*j  # 13 times squared physical distance.


def quad(i, j):
    return [(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]


def perimeter(cells):
    counts = Counter()
    for i, j in cells:
        w = quad(i, j)
        counts.update(edge(w[t], w[(t + 1) % 4]) for t in range(4))
    assert all(c in (1, 2) for c in counts.values())
    return sum(c == 1 for c in counts.values())


def ceiling(x):
    return -(-x.numerator // x.denominator)


def check_suffixes(paths, crop, h, contacts, terminals):
    used, total = set(), 0
    for path in paths:
        last = max(i for i, p in enumerate(path) if p in crop)
        suffix = path[last:]
        assert suffix[-1] in terminals and suffix[0] in crop
        assert all(p not in crop for p in suffix[1:])
        assert all(edge(a, b) in contacts for a, b in zip(suffix, suffix[1:]))
        # The Euclidean start-to-terminal distance is at least h.
        assert F(metric2(suffix[0], suffix[-1]), 13) >= h*h
        assert len(suffix) - 1 >= ceiling(h)
        interior = set(suffix[1:-1])
        assert not (interior & used) and not (interior & terminals)
        assert len(interior) >= ceiling(h) - 1
        used.update(interior)
        total += len(interior)
    assert total >= len(paths)*(ceiling(h) - 1)
    return total


def check(m):
    assert m % 8 == 0
    k = m//8
    points = {(i, j) for i in range(m + 1) for j in range(m + 1)}
    contacts = {
        edge(a, b) for a in points
        for b in ((a[0] + 1, a[1]), (a[0], a[1] + 1)) if b in points
    }
    pair_count = 0
    diameter_numerator, actual_loaded = 0, set()
    for a, b in combinations(sorted(points), 2):
        d = metric2(a, b)
        assert d >= 13
        assert (d == 13) == (edge(a, b) in contacts)
        if d > diameter_numerator:
            diameter_numerator, actual_loaded = d, {a, b}
        elif d == diameter_numerator:
            actual_loaded.update((a, b))
        pair_count += 1
    assert all((sum(a) - sum(b)) % 2 for a, b in contacts)
    terminals = {p for p in points if 0 in p or m in p}
    cells = {(i, j) for i in range(m) for j in range(m)}
    # Physical basis u=(1,0), v=(5/13,12/13). Every square label cell
    # is a strict unit rhombus of rational area 12/13.
    for i, j in cells:
        w = quad(i, j)
        assert all(edge(w[t], w[(t + 1) % 4]) in contacts for t in range(4))
        assert metric2(w[0], w[2]) > 13 and metric2(w[1], w[3]) > 13
    assert F(12, 13)**2 > F(3, 4)
    assert perimeter(cells) == 4*m

    # Proper hull chord from (0,m) to (m,0); selected cap i+j<=m.
    crossing = {(i, j) for i, j in cells if i + j <= m <= i + j + 2}
    cap_cells = {(i, j) for i, j in cells if i + j + 2 < m}
    other_cells = {(i, j) for i, j in cells if i + j > m}
    assert cells == crossing | cap_cells | other_cells
    assert len(cap_cells) == len(other_cells) == (m - 1)*(m - 2)//2
    assert len(crossing) <= 3*m
    assert len(cap_cells) >= F(len(cells), 2) - len(crossing)
    assert perimeter(cap_cells) <= perimeter(cells) + 4*len(crossing)
    # eta=(3/sqrt(13))*(m-i-j), with a_*=(0,0), so H=3m/sqrt(13).
    # H^2 >= (area(cap grain)/D)^2; D^2=36m^2/13.
    area_g = F(12, 13)*len(cap_cells)
    diameter2 = F(36, 13)*m*m
    assert F(9, 13)*m*m >= area_g*area_g/diameter2
    # This whole source is nonglobal: the same square-label board in an
    # orthogonal unit basis has squared diameter 2m^2 < diameter2.
    assert 2*m*m < diameter2
    assert diameter_numerator == 36*m*m
    assert actual_loaded == {(0, 0), (m, m)}
    assert terminals - actual_loaded

    # A complete k-by-k crossing grid in both cropped regions.
    grid_cells = {(i, j) for i in range(2*k, 3*k) for j in range(2*k, 3*k)}
    roots = {p for i, j in grid_cells for p in quad(i, j)}
    assert grid_cells <= cap_cells and len(grid_cells) == k*k
    assert perimeter(grid_cells) == 4*k
    cell_crop = {p for p in points if k <= p[0] <= m - k and k <= p[1] <= m - k}
    cap_crop = {p for p in points if p[0] >= k and p[1] >= k and sum(p) <= m - k}
    assert roots <= cell_crop & cap_crop
    assert not terminals & cell_crop and not terminals & cap_crop
    cell_h, cap_h = F(12*k, 13), F(k, 2)
    # Squared distances to both unit-side support lines and the cap chord.
    for i, j in cap_crop:
        assert F(12*i, 13)**2 > cap_h*cap_h
        assert F(12*j, 13)**2 > cap_h*cap_h
        assert F(9, 13)*(m - i - j)**2 > cap_h*cap_h
        assert F(13*i*i + 13*j*j + 10*i*j, 13) > cap_h*cap_h
    for i, j in cell_crop:
        assert min(i, j, m - i, m - j)*F(12, 13) >= cell_h
    # The exact full-cell strip-area bound in this parallelogram.
    strip_area = F(12, 13)*(m*m - (m - 2*k)**2)
    assert strip_area <= cell_h*4*m

    separator, paths, _ = contact_separator(contacts, roots, terminals)
    assert len(separator) == len(paths) == 4*k
    # Check the analytic F(R) inequality at these finite fixtures using
    # pi>3 and sqrt(3)<7/4, so 8*pi/sqrt(3)>96/7.
    assert len(grid_cells) <= 5*len(paths) + F(96, 7)*len(paths)**2
    cell_outside = check_suffixes(paths, cell_crop, cell_h, contacts, terminals)
    cap_outside = check_suffixes(paths, cap_crop, cap_h, contacts, terminals)
    return {
        "m": m, "source_pairs": pair_count, "rhombi": len(cells),
        "chord_crossing_faces": len(crossing), "cap_rhombi": len(cap_cells),
        "complete_grid_crossings": len(grid_cells), "disjoint_contact_returns": len(paths),
        "cell_strip_distinct_internal_vertices": cell_outside,
        "outside_cap_crop_distinct_internal_vertices": cap_outside,
        "actual_loaded_endpoints": len(actual_loaded),
        "artificial_boundary_terminals": len(terminals),
    }


def main():
    print(json.dumps({
        "status": "PASS",
        "cases": [check(m) for m in (16, 24, 32)],
        "scope": "nonglobal artificial-pin geometry/flow fixtures; no KKT or Level I certification",
    }, indent=2))


if __name__ == "__main__":
    main()
