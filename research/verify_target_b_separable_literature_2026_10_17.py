#!/usr/bin/env python3
"""Exact finite controls for the Target B separable-literature transfer audit.

No floating point, network, third-party modules, or optimization.  The all-size
arguments are in the companion report; these controls do not certify globality.
"""

from fractions import Fraction as Q
from itertools import combinations
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def distance_squared(a, b, cosine):
    return a * a + b * b + 2 * cosine * a * b


def difference_check(m, cosine):
    """Every possible label difference of the full (m+1)^2-label patch."""
    contacts = set()
    largest = Q(0)
    for a in range(-m, m + 1):
        for b in range(-m, m + 1):
            if a == b == 0:
                continue
            squared = distance_squared(a, b, cosine)
            require(squared >= 1, f"lower pair violation: {(a, b)}")
            if squared == 1:
                contacts.add((a, b))
            largest = max(largest, squared)
    return contacts, largest


def direct_graph_check(m, cosine):
    """Separate label-pair enumeration, independent of the difference loops."""
    labels = [(i, j) for i in range(m + 1) for j in range(m + 1)]
    adjacency = {p: set() for p in labels}
    pair_count = 0
    for p, r in combinations(labels, 2):
        squared = distance_squared(p[0] - r[0], p[1] - r[1], cosine)
        require(squared >= 1, "direct lower pair violation")
        pair_count += 1
        if squared == 1:
            adjacency[p].add(r)
            adjacency[r].add(p)
    for p in labels:
        for r in adjacency[p]:
            require(not adjacency[p].intersection(adjacency[r]), "unit triangle")
    edges = sum(map(len, adjacency.values())) // 2
    require(edges == 2 * m * (m + 1), "contact count")
    require(len(labels) - edges + m * m == 1, "disk Euler characteristic")
    require(-edges == -3 * len(labels) + 4 * m + 3 + m * m,
            "HR identity on rhombic disk")
    return pair_count


def must_reject(operation, label):
    try:
        operation()
    except ValueError:
        return
    raise ValueError(f"failure control was accepted: {label}")


def main():
    pi_upper = Q(22, 7)
    root3_upper = Q(26, 15)
    require(root3_upper**2 > 3, "sqrt(3) upper bound")
    threshold_upper = pi_upper * (24 + 14 * root3_upper)
    require(threshold_upper == Q(15928, 105) < 152, "n >= 153 cutoff")
    pair_count = 0
    difference_cases = 0
    for m in range(2, 65):
        cosine = Q(m * m - 1, 2 * m * m)
        contacts, diameter_squared = difference_check(m, cosine)
        require(contacts == {(1, 0), (-1, 0), (0, 1), (0, -1)},
                "unexpected unit difference")
        require(diameter_squared == 3 * m * m - 1, "source diameter")
        square_contacts, square_diameter = difference_check(m, Q(0))
        require(square_contacts == contacts, "square contacts")
        require(square_diameter == 2 * m * m < diameter_squared,
                "same-label strict competitor")
        # sin(theta)^2 - (sqrt(3)/2)^2; numerator after rationalization.
        sin_squared = 1 - cosine**2
        delta = sin_squared - Q(3, 4)
        numerator = m * m * delta
        require(numerator == Q(1, 2) - Q(1, 4 * m * m), "surplus numerator")
        require(0 < numerator < Q(1, 2), "bounded positive surplus")
        # E < numerator/sqrt(3) < 1/(2 sqrt(3)); target is sqrt(3)*m.
        require(numerator < 3 * m, "shell target comparison")
        require(abs(cosine - Q(1, 2)) < Q(1, 2),
                "unique separator of tangent pair cuts third radius-1/2 disk")
        if m <= 12:
            pair_count += direct_graph_check(m, cosine)
        difference_cases += 1

    # Near-triangular limit: the missing diagonal becomes a genuine unit edge.
    at_equality, _ = difference_check(3, Q(1, 2))
    require((1, -1) in at_equality, "equality control lost its triangle")
    must_reject(lambda: direct_graph_check(3, Q(1, 2)), "unit triangle at equality")
    must_reject(lambda: difference_check(3, Q(3, 4)), "overlap beyond 60 degrees")

    # Exact topology control: 3x3 rhombi with the central face omitted.
    # All 16 vertices and 24 contact edges remain; the omitted square is a
    # bounded quadrilateral face of the contact graph, not a removed graph face.
    n, edges, rhombi, hole_boundary, holes, outer_boundary = 16, 24, 8, 4, 1, 12
    chi_rhombi = n - edges + rhombi
    mu = rhombi + hole_boundary - 3 * holes
    chi_filled_graph = chi_rhombi + holes
    require(chi_rhombi == 0 and chi_filled_graph == 1, "hole Euler control")
    require(-edges == -3 * n + outer_boundary + 3 * chi_filled_graph + mu,
            "filled-hole HR identity")
    require(-edges != -3 * n + outer_boundary + 3 * chi_rhombi + mu,
            "wrong Euler characteristic must fail")

    print(json.dumps({
        "result": "PASS (finite controls only)",
        "patch_sizes": "m=2..64",
        "complete_difference_cases": difference_cases,
        "independent_label_pairs_m_2_to_12": pair_count,
        "global_separable_exclusion": "n >= 153; analytic proof in report",
        "global_subset_and_partition_bounds": "analytic inequalities (5a)-(5b) in report",
        "cutoff_rational_upper": str(threshold_upper),
        "failure_controls": ["triangle at cosine=1/2", "overlap at cosine=3/4",
                             "unfilled-hole Euler substitution"],
        "does_not_certify": ["global optimality", "jammed source extraction",
                             "Target B shell closure", "full certificate replay"],
    }, indent=2))


if __name__ == "__main__":
    main()
