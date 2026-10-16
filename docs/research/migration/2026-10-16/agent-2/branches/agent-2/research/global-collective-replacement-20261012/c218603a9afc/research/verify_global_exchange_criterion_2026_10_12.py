#!/usr/bin/env python3
"""Exact exhaustive check of the exchange formula and binding full-pair guards."""

from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path

from global_exchange_pool_2026_10_12 import (
    conflicts, dist2, verify_selection,
)


def cover_number(edges, vertices):
    return min(mask.bit_count() for mask in range(1 << vertices)
               if all((mask >> i & 1) or (mask >> j & 1) for i, j in edges))


def exhaustive_formula():
    n, m = 3, 3
    old_pairs = list(combinations(range(n), 2))
    cross_pairs = [(i, j) for i in range(n) for j in range(m)]
    count = 0
    for hbits in range(1 << len(old_pairs)):
        old = [edge for bit, edge in enumerate(old_pairs) if hbits >> bit & 1]
        for bbits in range(1 << len(cross_pairs)):
            cross = [edge for bit, edge in enumerate(cross_pairs) if bbits >> bit & 1]
            graph = old + [(i, n + j) for i, j in cross]
            expected = n + m - cover_number(graph, n + m)
            best = -n
            for ybits in range(1 << m):
                neighbors = {i for i, j in cross if ybits >> j & 1}
                residual = [(i, j) for i, j in old if i not in neighbors and j not in neighbors]
                score = ybits.bit_count() - len(neighbors) - cover_number(residual, n)
                best = max(best, score)
            assert expected == n + best
            count += 1
    return count


def upper_guard():
    source = [(F(x), F(y)) for x, y in [(0, 0), (1, 0), (0, 1), (1, 1)]]
    proposals = [(F(10), F(10)), (F(11), F(10))]
    selected = [0, 1, 4, 5]
    assert all(dist2(a, b) >= 1 for a, b in combinations([*(source[i] for i in [0, 1]), *proposals], 2))
    try:
        verify_selection(source, proposals, F(7, 4), selected)
    except ValueError as error:
        assert "pair constraint" in str(error)
    else:
        raise AssertionError("omitted cross-upper guard was accepted")


def isolate_guard():
    retained = [(F(0), F(0)), (F(1), F(0)), (F(3), F(3))]
    inserted = (F(3), F(7, 2))
    assert min(dist2(inserted, p) for p in retained[:2]) > 1
    assert dist2(inserted, retained[2]) == F(1, 4)
    assert (2, 3) in conflicts(retained + [inserted], F(100))


def fixture():
    source = [(F(i), F(j)) for i in range(-4, 5) for j in range(-4, 5)]
    # Unit basis angle > pi/3. Its entire lattice is unit separated and bipartite.
    cloud = [(F(i) + F(8, 17)*j, F(15, 17)*j)
             for i in range(-8, 9) for j in range(-8, 9)
             if (F(i) + F(8, 17)*j)**2 + (F(15, 17)*j)**2 <= 25
             and (i, j) != (0, 0)]
    assert len(cloud) >= 80
    # The source origin fills the deliberately omitted proposal site.
    proposals = cloud[:80]
    center = source.index((F(0), F(0)))
    selected = [center] + list(range(len(source), len(source) + len(proposals)))
    result = verify_selection(source, proposals, F(100), selected)
    assert result["deleted_source_labels"] == 80
    assert result["strict_squared_diameter_margin"] != "0"
    return {"source": [[str(x), str(y)] for x, y in source],
            "proposals": [[str(x), str(y)] for x, y in proposals],
            "target_diameter_squared": "100", "selected": selected,
            "verification": result}


if __name__ == "__main__":
    print("Exhaustive abstract conflict graphs:", exhaustive_formula())
    upper_guard()
    isolate_guard()
    data = fixture()
    destination = Path(__file__).parent / "certificates/global_exchange_square81_2026_10_12.json"
    if "--write" in __import__("sys").argv:
        destination.parent.mkdir(exist_ok=True)
        destination.write_text(json.dumps(data, indent=2) + "\n")
    else:
        assert json.loads(destination.read_text()) == data
    print(json.dumps(data["verification"], indent=2))
    print("PASS: exact formula, all upper pairs, isolate guard, whole-source replacement")
