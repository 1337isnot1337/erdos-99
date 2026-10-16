#!/usr/bin/env python3
"""Exact full-pair certificates for the joint diameter-cover exchange theorem.

This verifies supplied finite packets, not the existence of a successful packet
for every sufficiently large triangle-free global minimizer.
"""

if not __debug__:
    raise RuntimeError("Certificate assertions are required; run Python without -O.")

from fractions import Fraction as Q
from copy import deepcopy
from itertools import combinations, product
import json


def point(x, y):
    return Q(x), Q(y)


def distance2(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def diameter2(points):
    return max((distance2(p, q) for p, q in combinations(points, 2)), default=Q(0))


def feasible(points, threshold):
    return all(1 <= distance2(p, q) < threshold for p, q in combinations(points, 2))


def maximum_matching_cover(adjacency, right, *, witness=None):
    """Return maximum matching and minimum cover via alternating reachability."""
    mates = {}

    def augment(b, seen):
        for a in sorted(adjacency[b] & right):
            if a in seen:
                continue
            seen.add(a)
            if a not in mates or augment(mates[a], seen):
                mates[a] = b
                return True
        return False

    for b in range(len(adjacency)):
        augment(b, set())
    matched_b = {b: a for a, b in mates.items()}
    reached_b = set(range(len(adjacency))) - set(matched_b)
    reached_a = set()
    queue = list(reached_b)
    while queue:
        b = queue.pop()
        for a in adjacency[b] & right:
            if matched_b.get(b) == a or a in reached_a:
                continue
            reached_a.add(a)
            assert a in mates, "An augmenting path remains."
            next_b = mates[a]
            if next_b not in reached_b:
                reached_b.add(next_b)
                queue.append(next_b)
    cover_b = set(range(len(adjacency))) - reached_b
    cover_a = reached_a
    assert len(cover_b) + len(cover_a) == len(mates)
    assert all(b in cover_b or a in cover_a for b, ns in enumerate(adjacency)
               for a in ns & right)
    assert all(a in adjacency[b] and a in right for a, b in mates.items())
    assert len(set(mates.values())) == len(mates)
    if witness is not None:
        witness.update(left_labels=len(adjacency), right=sorted(right),
                       matching=[[b, a] for a, b in sorted(mates.items())],
                       cover_source=sorted(cover_a), cover_packet=sorted(cover_b))
    return len(mates), cover_a, cover_b


def replay_matching_cover(adjacency, right, witness):
    """Check an equal-size matching/cover certificate without optimization."""
    assert witness["left_labels"] == len(adjacency)
    assert witness["right"] == sorted(right)
    pairs = witness["matching"]
    assert all(0 <= b < len(adjacency) and a in right and a in adjacency[b]
               for b, a in pairs)
    assert len({b for b, _ in pairs}) == len(pairs)
    assert len({a for _, a in pairs}) == len(pairs)
    a_list, b_list = witness["cover_source"], witness["cover_packet"]
    cover_a, cover_b = set(a_list), set(b_list)
    assert len(a_list) == len(cover_a) and len(b_list) == len(cover_b)
    assert cover_a <= right and cover_b <= set(range(len(adjacency)))
    assert all(b in cover_b or a in cover_a for b, neighbours in enumerate(adjacency)
               for a in neighbours & right)
    assert len(cover_a) + len(cover_b) == len(pairs)
    return len(pairs)


def verify_matching_kernel():
    cases = 0
    for mask in range(1 << 9):
        adjacency = [{a for a in range(3) if mask & (1 << (3*b+a))}
                     for b in range(3)]
        for right in subsets(3):
            witness = {}
            size, _, _ = maximum_matching_cover(adjacency, right, witness=witness)
            direct = max(sum(a >= 0 for a in assignment)
                         for assignment in product([-1]+sorted(right), repeat=3)
                         if len([a for a in assignment if a >= 0]) ==
                            len({a for a in assignment if a >= 0})
                         and all(a < 0 or a in adjacency[b]
                                 for b, a in enumerate(assignment)))
            assert size == direct
            assert replay_matching_cover(adjacency, right,
                                         json.loads(json.dumps(witness))) == size
            cases += 1
    adjacency, right = [{0, 1}, {0, 1}], {0, 1}
    witness = {}
    maximum_matching_cover(adjacency, right, witness=witness)
    bad_edge = deepcopy(witness)
    bad_edge["matching"][0][1] = -1
    duplicate = deepcopy(witness)
    duplicate["matching"].append(duplicate["matching"][0][:])
    bad_cover = deepcopy(witness)
    bad_cover["cover_packet"].pop()
    bad_population = deepcopy(witness)
    bad_population["right"].pop()
    for bad in (bad_edge, duplicate, bad_cover, bad_population):
        try:
            replay_matching_cover(adjacency, right, bad)
        except AssertionError:
            continue
        raise AssertionError("Corrupted matching/cover certificate accepted")
    print(f"PASS: {cases} matching/deletion cases against direct enumeration; "
          "JSON replay and four corruption controls")


def subsets(n):
    for mask in range(1 << n):
        yield {i for i in range(n) if mask & (1 << i)}


def verify_fixture(name, source, packet, expected_size):
    n, m = len(source), len(packet)
    d2 = diameter2(source)
    assert d2 > 0
    assert all(distance2(p, q) >= 1 for p, q in combinations(source, 2))
    assert all(distance2(p, q) >= 1 for p, q in combinations(packet, 2))
    assert diameter2(packet) < d2
    diameter_edges = {(i, j) for i, j in combinations(range(n), 2)
                      if distance2(source[i], source[j]) == d2}
    adjacency = [{i for i, a in enumerate(source)
                  if distance2(a, b) < 1 or distance2(a, b) >= d2}
                 for b in packet]
    lower_only = [{i for i, a in enumerate(source) if distance2(a, b) < 1}
                  for b in packet]
    rows = []
    all_source = set(range(n))
    for forced in subsets(n):
        if not all(i in forced or j in forced for i, j in diameter_edges):
            continue
        witness = {}
        nu, cover_a, cover_b = maximum_matching_cover(
            adjacency, all_source - forced, witness=witness)
        witness = json.loads(json.dumps(witness))
        assert replay_matching_cover(adjacency, all_source - forced, witness) == nu
        selected_a = all_source - forced - cover_a
        selected_b = set(range(m)) - cover_b
        candidate = [source[i] for i in sorted(selected_a)]
        candidate += [packet[j] for j in sorted(selected_b)]
        assert feasible(candidate, d2), "Full coordinate ledger rejected graph packet."
        assert len(candidate) == n + m - len(forced) - nu
        rows.append((len(candidate), forced, nu, selected_a, selected_b, witness))
    best = max(rows, key=lambda row: row[0])

    # Independent geometric enumeration checks every pair directly, rather than
    # reusing H, cross-conflict edges, matching, or the joint-cover formula.
    combined = source + packet
    geometric_best = max(len(s) for s in subsets(n + m)
                         if feasible([combined[i] for i in s], d2))
    assert best[0] == geometric_best == expected_size
    min_cover_size = min(len(row[1]) for row in rows)
    minimum_cover_best = max(row[0] for row in rows if len(row[1]) == min_cover_size)
    lower_only_prediction = max(
        n + m - len(row[1])
        - maximum_matching_cover(lower_only, all_source - row[1])[0]
        for row in rows)
    winning = [source[i] for i in sorted(best[3])]
    winning += [packet[j] for j in sorted(best[4])]
    result = {
        "fixture": name,
        "source_labels": n,
        "comparison_labels": m,
        "source_diameter_squared": str(d2),
        "maximum_mixed_labels": best[0],
        "maximum_profit": best[0] - n,
        "winning_forced_cover": sorted(best[1]),
        "winning_matching_size": best[2],
        "matching_cover_certificate": best[5],
        "winning_source_labels": sorted(best[3]),
        "winning_packet_labels": sorted(best[4]),
        "winning_diameter_squared": str(diameter2(winning)),
        "minimum_cardinality_cover_best": minimum_cover_best,
        "lower_only_prediction": lower_only_prediction,
        "all_pairs_and_exhaustive_geometry": "PASS",
    }
    if name == "nonminimum_cover_required":
        assert minimum_cover_best == n - 1
        assert best[1] == {1, 2}
        assert diameter2(winning) == Q(53, 50)
    if name == "smaller_packet_augments":
        assert m < n and best[0] > n
        assert diameter2(winning) == 4
    if name == "square_global_regression":
        assert best[0] == n - 1
    if name == "upper_conflicts_required":
        assert all(len(ns) == n for ns in adjacency)
        assert lower_only_prediction == 5 > n
    print(json.dumps(result, sort_keys=True))


def main():
    verify_matching_kernel()
    square = [point(0, 0), point(1, 0), point(0, 1), point(1, 1)]
    triangle_packet = [point(0, "1/10"), point(1, "1/10"), point("1/2", "11/10")]
    verify_fixture(
        "nonminimum_cover_required",
        [point(0, 0), point("-1/2", 1), point("1/2", 1)],
        [point("-1/2", "9/10"), point("1/2", "9/10")],
        3,
    )
    verify_fixture(
        "smaller_packet_augments",
        [point(0, 0), point(2, 0), point(0, 1), point(2, 1)],
        [point("1/2", 0), point("3/2", 0), point(1, 1)],
        5,
    )
    verify_fixture("square_global_regression", square, triangle_packet, 3)
    far_packet = [(x + 10, y) for x, y in triangle_packet]
    verify_fixture("upper_conflicts_required", square, far_packet, 3)
    print("PASS: exact joint exchange identity and four full-source geometric fixtures")


if __name__ == "__main__":
    main()
