#!/usr/bin/env python3
"""Separate exact coordinate engine for seed 54, with direct small pair ledgers.

This deliberately imports no source-generation, metric, hull, or verification code
from the primary engine. The larger fixtures use convexity to certify upper pairs
and the proved integral norm classification for lower pairs.
"""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


def make_vertices(k, radius):
    result = set()
    m = 3 * k * k + 4 * k - 4
    bound = 2 * radius + 4
    for i in range(-bound, bound + 1):
        for j in range(-bound, bound + 1):
            for a, b in ((i - 1, j - 1), (i - 1, j), (i, j - 1), (i, j)):
                if -2 <= a <= 1 and -2 <= b <= 1:
                    continue
                # Cell center has Cartesian coordinates
                # (X/(4k), Y*sqrt(m)/(4k)).
                x = 2 * k * (2 * a + 1) + (k - 2) * (2 * b + 1)
                y = 2 * b + 1
                if x * x + m * y * y <= 16 * k * k * radius * radius:
                    result.add((i, j))
                    break
    return result


def coordinates(vertices, k):
    # The stored pair means (X/(2k), Y*sqrt(m)/(2k)).
    return [(2 * k * i + (k - 2) * j, j) for i, j in sorted(vertices)]


def jarvis(points):
    start = min(points)
    current, result = start, []
    while True:
        result.append(current)
        candidate = next(p for p in points if p != current)
        for p in points:
            dx, dy = candidate[0] - current[0], candidate[1] - current[1]
            ex, ey = p[0] - current[0], p[1] - current[1]
            cross = dx * ey - dy * ex
            if cross < 0 or (cross == 0 and ex * ex + ey * ey > dx * dx + dy * dy):
                candidate = p
        current = candidate
        if current == start:
            return result


def max_squared(points, m, denominator):
    h = jarvis(points)
    maximum = max((a[0] - b[0]) ** 2 + m * (a[1] - b[1]) ** 2
                  for a in h for b in h)
    return Fraction(maximum, denominator), len(h)


def sha(vertices):
    return hashlib.sha256(json.dumps(sorted(vertices), separators=(",", ":"))
                          .encode()).hexdigest()


def direct_pair_ledger(vertices, coords, k, source_d2):
    m, denominator = 3 * k * k + 4 * k - 4, 4 * k * k
    ordered_vertices = sorted(vertices)
    maximum, contact_count, pairs = 0, 0, 0
    for i, a in enumerate(coords):
        for j in range(i):
            b = coords[j]
            d = (a[0] - b[0]) ** 2 + m * (a[1] - b[1]) ** 2
            assert d >= denominator
            assert d * source_d2.denominator <= source_d2.numerator * denominator
            maximum = max(maximum, d)
            if d == denominator:
                p, q = ordered_vertices[i], ordered_vertices[j]
                assert (p[0] + p[1] - q[0] - q[1]) % 2 == 1
                contact_count += 1
            pairs += 1
    assert Fraction(maximum, denominator) == source_d2
    return pairs, contact_count


def verify(row):
    k, radius, n = row["k"], row["R"], row["n"]
    vertices = make_vertices(k, radius)
    assert len(vertices) + 1 == n and sha(vertices) == row["source_sha256"]
    coords = coordinates(vertices, k)
    m, denominator = 3 * k * k + 4 * k - 4, 4 * k * k
    d2, hull_count = max_squared(coords, m, denominator)
    assert str(d2) == row["source_diameter_squared"]
    assert hull_count == row["source_hull_vertices"]
    assert row["local_growth_cells_required_at_comparison_diameter"] == (radius + 7) // 8

    # Coordinates of the extra isolate, on the same field/denominator scale,
    # are X=k/5, Y=0. Multiply all coordinates by five for integral checks.
    minimum = min(Fraction((5 * x - k) ** 2 + 25 * m * y * y,
                           25 * denominator) for x, y in coords)
    assert minimum > 1 and str(minimum) == row["isolate_min_squared"]
    all_pair_diameter = d2
    # The isolate's upper pairs are also checked individually by this engine.
    for x, y in coords:
        assert Fraction((5 * x - k) ** 2 + 25 * m * y * y,
                        25 * denominator) <= all_pair_diameter

    rp, packet = radius - 1, []
    for i in range(-2 * rp - 2, 2 * rp + 3):
        for j in range(-2 * rp - 2, 2 * rp + 3):
            # Cartesian triangular coordinates ((2i+j)/2, j*sqrt(3)/2).
            if (2 * i + j) ** 2 + 3 * j * j <= 4 * rp * rp:
                packet.append((i, j))
    assert len(packet) == row["available_replacement_sites"] >= n
    replacement = set(sorted(packet)[:n])
    assert sha(replacement) == row["replacement_sha256"]
    assignment = dict(zip(sorted(vertices), sorted(replacement)[:-1]))
    bad_cells, grown_pairs = 0, set()
    for i, j in vertices:
        if -2 <= i <= 1 and -2 <= j <= 1:
            continue
        cx = 2 * k * (2 * i + 1) + (k - 2) * (2 * j + 1)
        cy = 2 * j + 1
        if cx * cx + m * cy * cy > 16 * k * k * radius * radius:
            continue
        corners = ((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1))
        assert all(p in vertices for p in corners)
        bad = False
        for a_index, a in enumerate(corners):
            for b in corners[a_index + 1:]:
                da, db = a[0] - b[0], a[1] - b[1]
                original = (2 * k * da + (k - 2) * db) ** 2 + m * db * db
                ap, bp = assignment[a], assignment[b]
                x, y = ap[0] - bp[0], ap[1] - bp[1]
                endpoint = (2 * x + y) ** 2 + 3 * y * y
                if endpoint * k * k > original:
                    bad = True
                    grown_pairs.add(tuple(sorted((a, b))))
        bad_cells += bad
    assert bad_cells == row["bad_cells_of_lexicographic_replacement"]
    assert len(grown_pairs) == row["grown_local_pairs_of_lexicographic_replacement"]
    assert bad_cells >= (radius + 7) // 8
    replacement_coords = [(2 * i + j, j) for i, j in replacement]
    rd2, rh = max_squared(replacement_coords, 3, 4)
    assert str(rd2) == row["replacement_diameter_squared"] and rd2 < d2
    assert rh == row["replacement_hull_vertices"]

    # Symbolic lower classification in actual coordinates, independent of
    # the primary formula. For all integer differences a,b, this identity is
    # (a-b)^2+2(1-c)ab when the signs oppose; otherwise >=a^2+b^2.
    for a in range(-20, 21):
        for b in range(-20, 21):
            physical = (2 * k * a + (k - 2) * b) ** 2 + m * b * b
            assert physical == denominator * (a * a + b * b) + 4 * k * (k - 2) * a * b
            if a or b:
                assert physical >= denominator
                if physical == denominator:
                    assert abs(a) + abs(b) == 1
    direct_pairs = 0
    if (k, radius) in ((2, 24), (3, 40)):
        direct_pairs, contacts = direct_pair_ledger(vertices, coords, k, d2)
        assert contacts == row["contacts"]
        # Independent direct ledger for every replacement pair as well.
        maximum, contacts = 0, 0
        for i, a in enumerate(replacement_coords):
            for b in replacement_coords[:i]:
                d = (a[0] - b[0]) ** 2 + 3 * (a[1] - b[1]) ** 2
                assert d >= 4 and Fraction(d, 4) <= rd2
                maximum = max(maximum, d)
                contacts += d == 4
        assert Fraction(maximum, 4) == rd2 and contacts > 0
    return {"k": k, "R": radius, "n": n, "direct_lattice_source_pairs": direct_pairs,
            "isolate_pairs": len(vertices), "diameter_margin_squared": str(d2 - rd2),
            "bad_cells_in_verified_endpoint": bad_cells}


def main():
    path = Path(__file__).with_name("seed054_rhombus_mesh_certificate.json")
    certificate = json.loads(path.read_text())
    output = [verify(row) for row in certificate["fixtures"]]
    print(json.dumps({"independent_cartesian_checks": output,
                      "global_optimality_proved": False}, indent=2))


if __name__ == "__main__":
    main()
