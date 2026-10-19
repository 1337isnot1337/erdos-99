#!/usr/bin/env python3
"""Exact finite control for the safe-core source-extraction condition."""

if not __debug__:
    raise SystemExit("This checker requires assertions; do not run with -O")

from fractions import Fraction as F
from itertools import combinations


def q60(u, v):
    """Squared norm in the unit triangular lattice basis."""
    return u * u + u * v + v * v


def q_deformed(u, v, cosine):
    """Squared norm for unit basis vectors with dot product cosine."""
    return u * u + v * v + 2 * cosine * u * v


def minimum_cover(edges):
    """Brute-force the minimum cover on the conflict endpoints only."""
    vertices = sorted({v for edge in edges for v in edge})
    for size in range(len(vertices) + 1):
        for chosen in combinations(vertices, size):
            cover = set(chosen)
            if all(a in cover or b in cover for a, b in edges):
                return cover
    raise AssertionError("finite graph has no vertex cover")


def annular_control():
    # The pinned PR #955 D=8 packet: radius 17/4 and translation (1/4,1/4).
    packet = {}
    for i in range(-10, 11):
        for j in range(-10, 11):
            u, v = 4 * i - 1, 4 * j - 1
            if q60(u, v) < 17**2:
                packet[(i, j)] = (u, v)
    assert len(packet) == 67

    halo = {
        label for label, (u, v) in packet.items()
        if q60(u, v) >= 15**2
    }
    conflicts = []
    for a, b in combinations(sorted(halo), 2):
        au, av = packet[a]
        bu, bv = packet[b]
        if q60(au - bu, av - bv) >= 32**2:
            conflicts.append((a, b))
    assert len(halo) == 15
    assert len(conflicts) == 8

    cover_labels = minimum_cover(conflicts)
    expected_cover = {(-4, 4), (-3, 5), (1, 4), (4, 1)}
    assert cover_labels == expected_cover
    assert len(cover_labels) == 4
    retained = set(packet) - cover_labels
    assert len(retained) == 63

    # Deform only the metric, retaining every label. The contact graph is
    # bipartite by parity, and every pair is checked with exact fractions.
    cosine = F(163, 328)
    assert 0 < cosine < F(1, 2)
    labels = sorted(retained)
    pair_data = []
    for a, b in combinations(labels, 2):
        di, dj = a[0] - b[0], a[1] - b[1]
        old_sq = F(di * di + di * dj + dj * dj)
        new_sq = q_deformed(F(di), F(dj), cosine)
        assert old_sq >= 1
        assert new_sq >= 1
        pair_data.append((a, b, old_sq, new_sq))

    original_diameter_sq = max(row[2] for row in pair_data)
    diameter_sq = max(row[3] for row in pair_data)
    diameter_pairs = [(a, b) for a, b, _, new_sq in pair_data
                      if new_sq == diameter_sq]
    assert original_diameter_sq == 63
    assert diameter_sq == F(5193, 82)
    assert original_diameter_sq < diameter_sq
    assert len(diameter_pairs) == 2

    contact_edges = [(a, b) for a, b, _, new_sq in pair_data if new_sq == 1]
    assert contact_edges
    assert all(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1
               for a, b in contact_edges)
    assert all((sum(a) - sum(b)) % 2 == 1 for a, b in contact_edges)
    tau = len(minimum_cover(diameter_pairs))
    assert tau >= 1

    # The source fits in the Jung disk of radius D/sqrt(3), centered at 0.
    radial_sq = [
        q_deformed(F(4 * i - 1), F(4 * j - 1), cosine) / 16
        for i, j in retained
    ]
    assert max(radial_sq) == F(46659, 2624)
    assert max(radial_sq) < diameter_sq / 3

    # Positive finite scalar excess; this nonglobal control is not an
    # application of the global-minimizer reserve theorem.
    reserve_lower = F(62) - F(110, 119) * diameter_sq
    assert reserve_lower == F(16883, 4879)
    assert reserve_lower > 0

    # Cover-radius certificate for the translated deformed triangular lattice.
    rho_sq = F(1, 2 * (1 + cosine))
    assert rho_sq == F(164, 491)
    assert rho_sq < F(9, 25)  # hence rho < 3/5

    # D < 8 and sqrt(3) < 26/15 imply
    # D(1-1/sqrt(3)) < 44/13; adding rho < 3/5 stays below 4.
    assert F(44, 13) + F(3, 5) == F(259, 65) < 4

    # Enumerate every translated-lattice site with radius < 4. The positive
    # definite metric gives |u|,|v| < 6 there, so this index range is complete.
    radius_four_sites = set()
    for i in range(-6, 7):
        for j in range(-6, 7):
            u, v = F(4 * i - 1, 4), F(4 * j - 1, 4)
            if q_deformed(u, v, cosine) < 16:
                radius_four_sites.add((i, j))
    assert len(radius_four_sites) == 57
    assert radius_four_sites <= retained

    # A missing site would invalidate the coverage certificate; exercise that
    # failure boundary without modifying the pinned fixture.
    corrupted = retained - {min(radius_four_sites)}
    assert not radius_four_sites <= corrupted

    return {
        "packet_labels": len(packet),
        "halo_labels": len(halo),
        "conflicts": len(conflicts),
        "deleted_cover": len(cover_labels),
        "source_labels": len(retained),
        "contact_edges": len(contact_edges),
        "actual_diameter_edges": len(diameter_pairs),
        "actual_diameter_cover": tau,
        "diameter_squared": str(diameter_sq),
        "strict_same_cardinality_control_squared": str(original_diameter_sq),
        "reserve_lower_bound": str(reserve_lower),
        "safe_core_lattice_sites": len(radius_four_sites),
        "safe_core_vacancy": 0,
    }


def positive_conditional_control():
    # A={(-1,0),(1,0)}, D=2, Y={(0,1/2)}.
    # Jung radius is 2/sqrt(3); Y lies in its safe core.
    d2 = F(4)
    jung_radius_sq = F(4, 3)
    cross_sq = F(5, 4)
    assert F(1) < jung_radius_sq < d2 / 2
    assert F(1) <= cross_sq < d2
    # Since sqrt(3)>3/2, the safe-core radius exceeds 2/3.
    assert F(1, 2) < F(2, 3)
    source_edges = [(0, 1)]
    tau = len(minimum_cover(source_edges))
    packet_size = 3
    assert tau == 1 and packet_size - tau == 2
    return {"source_labels": 2, "vacancy_labels": 1, "cover": tau,
            "M_D_lower_bound": packet_size - tau}


def main():
    positive = positive_conditional_control()
    regression = annular_control()
    print("PASS: safe-core conditional packet arithmetic")
    print("positive exact control:", positive)
    print("nonglobal annular control:", regression)
    print("The nonglobal control has positive scalar excess but zero safe-core "
          "vacancy; no conclusion about global sources follows.")


main()
