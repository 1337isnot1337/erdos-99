#!/usr/bin/env python3
"""Exact diameter-conflict cover and finite triangular-lattice packet checks.

All metric predicates use integer values of m^2+m*n+n^2. A bipartite
matching plus an exhaustive search over a small supplied deletion set proves
the maximum cardinality of a strict-sub-D subset of each finite input packet.
It does not prove unrestricted packing optimality, the circle discrepancy
theorem, or Level I. See the associated report for the general geometric proof.
"""

from collections import deque
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import combinations
from math import gcd, lcm
import json


def norm(u, v):
    return u * u + u * v + v * v


def hull(points):
    """Convex hull in lattice coordinates; physical linear map has positive det."""
    points = sorted(set(points))

    def cross(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    lower, upper = [], []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def bipartition(graph, allowed):
    colors = {}
    for root in sorted(allowed):
        if root in colors:
            continue
        colors[root] = 0
        queue = deque([root])
        while queue:
            vertex = queue.popleft()
            for neighbor in sorted(graph[vertex] & allowed):
                if neighbor in colors:
                    if colors[neighbor] == colors[vertex]:
                        return None
                else:
                    colors[neighbor] = 1 - colors[vertex]
                    queue.append(neighbor)
    return colors


def matching_cover(graph, allowed):
    """Certify maximum matching by a vertex cover of equal cardinality."""
    colors = bipartition(graph, allowed)
    assert colors is not None
    left = {v for v in allowed if colors[v] == 0}
    matched_right = {}

    def augment(vertex, seen):
        for neighbor in sorted(graph[vertex] & allowed):
            if neighbor in seen:
                continue
            seen.add(neighbor)
            if neighbor not in matched_right or augment(matched_right[neighbor], seen):
                matched_right[neighbor] = vertex
                return True
        return False

    for vertex in sorted(left):
        augment(vertex, set())

    matched_left = {vertex: neighbor for neighbor, vertex in matched_right.items()}
    reached_left = left - matched_left.keys()
    reached_right = set()
    queue = deque(sorted(reached_left))
    while queue:
        vertex = queue.popleft()
        for neighbor in sorted(graph[vertex] & allowed):
            if matched_left.get(vertex) == neighbor or neighbor in reached_right:
                continue
            reached_right.add(neighbor)
            if neighbor in matched_right:
                mate = matched_right[neighbor]
                if mate not in reached_left:
                    reached_left.add(mate)
                    queue.append(mate)
    cover = (left - reached_left) | reached_right
    assert len(cover) == len(matched_right)
    assert len(set(matched_right.values())) == len(matched_right)
    assert all(vertex in graph[neighbor] for neighbor, vertex in matched_right.items())
    assert all(vertex in cover or neighbor in cover
               for vertex in allowed for neighbor in graph[vertex] & allowed)
    return cover


def find_cut(graph, points, endpoint_set):
    """Find and exactly verify a geometric ray deletion; no float predicates."""
    if bipartition(graph, endpoint_set) is not None:
        return set()
    rays = set()
    for vertex in endpoint_set:
        u, v = points[vertex]
        divisor = gcd(abs(u), abs(v))
        assert divisor > 0
        rays.update(((u // divisor, v // divisor), (-u // divisor, -v // divisor)))

    def compare(a, b):
        first_half = int(not (a[1] > 0 or (a[1] == 0 and a[0] > 0)))
        second_half = int(not (b[1] > 0 or (b[1] == 0 and b[0] > 0)))
        if first_half != second_half:
            return first_half - second_half
        determinant = a[0] * b[1] - a[1] * b[0]
        return -1 if determinant > 0 else 1 if determinant < 0 else 0

    directions = sorted(rays, key=cmp_to_key(compare))
    candidates = []
    for first, second in zip(directions, directions[1:] + directions[:1]):
        determinant = first[0] * second[1] - first[1] * second[0]
        assert determinant >= 0  # Antipodal directions make every empty gap <=pi.
        if determinant:
            a, b = first[0] + second[0], first[1] + second[1]
        else:
            # Physical quarter-turn of first, expressed up to positive scalar.
            a, b = -first[0] - 2 * first[1], 2 * first[0] + first[1]
        side = {i: a * points[i][1] - b * points[i][0] for i in endpoint_set}
        assert all(side.values())
        projection = {i: (2 * a + b) * points[i][0] + (a + 2 * b) * points[i][1]
                      for i in endpoint_set}
        cut = set()
        for i in endpoint_set:
            for j in graph[i]:
                if i >= j or side[i] * side[j] < 0:
                    continue
                assert projection[i] * projection[j] < 0
                cut.add(i if projection[i] > 0 else j)
        remaining = endpoint_set - cut
        assert all(side[i] * side[j] < 0
                   for i in remaining for j in graph[i] & remaining)
        candidates.append(cut)
    assert candidates
    return min(candidates, key=lambda cut: (len(cut), tuple(sorted(cut))))


def exact_cover(graph, endpoint_set, cut):
    """Exhaust all independent retained subsets of cut; optimize rest by matching."""
    cut_list = sorted(cut)
    assert len(cut_list) <= 12, "This finite suite bounds exhaustive cut search"
    outside = endpoint_set - cut
    best = None
    branches = 0
    for mask in range(1 << len(cut_list)):
        retained = {vertex for index, vertex in enumerate(cut_list) if mask & (1 << index)}
        if any(graph[v] & retained for v in retained):
            continue
        forced = set().union(*(graph[v] & outside for v in retained)) if retained else set()
        residual = outside - forced
        cover = (cut - retained) | forced | matching_cover(graph, residual)
        assert all(i in cover or j in cover for i in endpoint_set for j in graph[i])
        branches += 1
        if best is None or len(cover) < len(best):
            best = cover
    assert best is not None
    return best, branches


def packet(k, phase):
    diameter = 8 * k ** 3
    radius = F(diameter, 2) + F(1, 4 * k)
    scale = lcm(radius.denominator, phase[0].denominator, phase[1].denominator)
    radius_scaled = int(radius * scale)
    inner_scaled = int((diameter - radius) * scale)
    bound = int(2 * radius) + 2
    points, labels, halo = [], [], []
    first = [(i, int((i - phase[0]) * scale)) for i in range(-bound, bound + 1)]
    second = [(j, int((j - phase[1]) * scale)) for j in range(-bound, bound + 1)]
    for i, u in first:
        for j, v in second:
            squared = norm(u, v)
            if squared < radius_scaled ** 2:
                index = len(points)
                points.append((u, v))
                labels.append((i, j))
                if squared >= inner_scaled ** 2:
                    halo.append(index)
    assert len(set(labels)) == len(labels)
    assert all(norm(*point) < radius_scaled ** 2 for point in points)
    halo_set = set(halo)
    assert all(index in halo_set or norm(*point) < inner_scaled ** 2
               for index, point in enumerate(points))
    # A pair outside halo has distance < (D-S)+S = D, by the triangle inequality.
    threshold = (diameter * scale) ** 2
    graph = {vertex: set() for vertex in halo}
    edges = []
    for i, j in combinations(halo, 2):
        u, v = points[i][0] - points[j][0], points[i][1] - points[j][1]
        if norm(u, v) >= threshold:
            graph[i].add(j)
            graph[j].add(i)
            edges.append((i, j))
    endpoint_set = {i for i in halo if graph[i]}
    cut = find_cut(graph, points, endpoint_set)
    cover, branches = exact_cover(graph, endpoint_set, cut)
    assert all(i in cover or j in cover for i, j in edges)
    assert all(norm(points[i][0] - points[j][0], points[i][1] - points[j][1]) < threshold
               for i, j in combinations([v for v in halo if v not in cover], 2))
    # Unit separation of all retained labels follows from positive integral norm:
    # norm(m,n)=((2m+n)^2+3n^2)/4 is an integer >=1 for every nonzero integer pair.
    retained = len(points) - len(cover)
    retained_labels = {label for index, label in enumerate(labels) if index not in cover}
    assert any((i + 1, j) in retained_labels or (i, j + 1) in retained_labels
               for i, j in retained_labels)
    vertices = hull(retained_labels)
    diameter_squared = max(norm(a[0] - b[0], a[1] - b[1]) for a, b in combinations(vertices, 2))
    assert diameter_squared < diameter * diameter
    first_span = max(p[0] for p in vertices) - min(p[0] for p in vertices)
    second_span = max(p[1] for p in vertices) - min(p[1] for p in vertices)
    product_bound = first_span * second_span
    rho = min(F(1, 4), F(diameter * diameter - diameter_squared, 4 * (product_bound + 1)))
    cosine = F(1, 2) - rho
    assert 0 < cosine < F(1, 2)
    deformed_squared = max(F(a[0] - b[0]) ** 2 + F(a[1] - b[1]) ** 2
                           + 2 * cosine * (a[0] - b[0]) * (a[1] - b[1])
                           for a, b in combinations(vertices, 2))
    assert deformed_squared <= diameter_squared + 2 * rho * product_bound < diameter * diameter
    # For mn>=1 the new norm is >1; for mn<0 it strictly exceeds old norm.
    # Therefore all unit edges change just one index by +/-1: a bipartite graph.
    return {"k": k, "D": diameter, "phase": [str(x) for x in phase],
            "input_population": len(points), "halo_population": len(halo),
            "conflict_edges": len(edges), "cut_size": len(cut),
            "exhaustive_cut_branches": branches, "optimal_packet_deletions": len(cover),
            "strict_sub_D_population": retained,
            "packet_diameter_squared": diameter_squared,
            "packet_hull_vertices": len(vertices),
            "triangle_free_basis_cosine": str(cosine),
            "triangle_free_packet_diameter_squared": str(deformed_squared),
            "gain_over_edge_count_deletion_bound": len(edges) - len(cover)}


def odd_cycle_regression():
    labels = [(0, 0), (2, 0), (2, 2), (0, 3), (-1, 2)]
    # Center is (3/4,5/4) in lattice coordinates; multiply coordinates by four.
    points = [(4 * i - 3, 4 * j - 5) for i, j in labels]
    graph = {i: set() for i in range(5)}
    edges = []
    for i, j in combinations(range(5), 2):
        difference = (points[i][0] - points[j][0], points[i][1] - points[j][1])
        assert norm(*difference) >= 16
        if norm(*difference) >= 16 * 7:
            graph[i].add(j)
            graph[j].add(i)
            edges.append((i, j))
    # S=7/4 and D=sqrt(7): S^2<D^2/2; all five points are in that disk.
    assert max(norm(*point) for point in points) == 49 and 2 * 49 < 16 * 7
    assert len(edges) == 5 and all(len(neighbors) == 2 for neighbors in graph.values())
    assert bipartition(graph, set(graph)) is None
    cut = find_cut(graph, points, set(graph))
    assert len(cut) == 1
    cover, branches = exact_cover(graph, set(graph), cut)
    assert len(cover) == 3 and branches == 2
    brute_cover = 5
    for mask in range(32):
        subset = {v for v in range(5) if mask & (1 << v)}
        if all(i in subset or j in subset for i, j in edges):
            brute_cover = min(brute_cover, len(subset))
    assert brute_cover == len(cover)
    return {"vertices": 5, "edges": 5, "cut_size": 1,
            "branches": branches, "minimum_deletions": len(cover)}


def complete_bipartite_regression(k):
    """Triangular-lattice columns: D=2sqrt(3)k^3, threshold D^2=12k^6."""
    m = k ** 3
    # Physical coordinates are (j, +/-sqrt(3)m), written in the standard basis.
    points = [(j - sign * m, 2 * sign * m)
              for sign in (-1, 1) for j in range(-k, k + 1)]
    graph = {i: set() for i in range(len(points))}
    edges = []
    for i, j in combinations(range(len(points)), 2):
        difference = (points[i][0] - points[j][0], points[i][1] - points[j][1])
        squared = norm(*difference)
        assert squared >= 1
        if squared >= 12 * m * m:
            graph[i].add(j)
            graph[j].add(i)
            edges.append((i, j))
    assert len(edges) == (2 * k + 1) ** 2
    cover = matching_cover(graph, set(graph))
    assert len(cover) == 2 * k + 1
    # S=sqrt(3)(m+1/(6k)); each radius is strictly smaller than S.
    radius_squared = 3 * (F(m) + F(1, 6 * k)) ** 2
    assert all(F(norm(*point)) < radius_squared for point in points)
    return {"k": k, "conflicts": len(edges), "minimum_deletions": len(cover),
            "edge_overcount": len(edges) - len(cover)}


def full_column_packet_regression(k):
    """Check induced shared conflicts inside the complete lattice disk packet."""
    m = k ** 3
    radius_squared = 3 * (F(m) + F(1, 6 * k)) ** 2
    inner_squared = 3 * (F(m) - F(1, 6 * k)) ** 2
    threshold = 12 * m * m
    labels, halo = [], []
    bound = 2 * m + 2
    for i in range(-bound, bound + 1):
        for j in range(-bound, bound + 1):
            squared = norm(i, j)
            if squared * radius_squared.denominator < radius_squared.numerator:
                index = len(labels)
                labels.append((i, j))
                if squared * inner_squared.denominator >= inner_squared.numerator:
                    halo.append(index)
    graph = {i: set() for i in halo}
    edges = []
    for i, j in combinations(halo, 2):
        if norm(labels[i][0] - labels[j][0], labels[i][1] - labels[j][1]) >= threshold:
            graph[i].add(j)
            graph[j].add(i)
            edges.append((i, j))
    positions = {label: i for i, label in enumerate(labels)}
    first_row = {positions[(j + m, -2 * m)] for j in range(-k, k + 1)}
    second_row = {positions[(j - m, 2 * m)] for j in range(-k, k + 1)}
    assert all(j in graph[i] for i in first_row for j in second_row)
    star_cover = set(first_row)
    for i, j in edges:
        if i not in star_cover and j not in star_cover:
            star_cover.add(i)
    guaranteed_saving = (2 * k + 1) ** 2 - (2 * k + 1)
    assert len(edges) - len(star_cover) >= guaranteed_saving
    endpoints = {i for i in halo if graph[i]}
    cut = find_cut(graph, labels, endpoints)
    cover, branches = exact_cover(graph, endpoints, cut)
    assert len(cover) <= len(star_cover)
    assert all(i in cover or j in cover for i, j in edges)
    vertices = hull(label for i, label in enumerate(labels) if i not in cover)
    diameter_squared = max(norm(a[0] - b[0], a[1] - b[1]) for a, b in combinations(vertices, 2))
    assert diameter_squared < threshold
    return {"k": k, "D_squared": threshold, "input_population": len(labels),
            "conflicts": len(edges), "optimal_deletions": len(cover),
            "cut_size": len(cut), "cut_branches": branches,
            "strict_sub_D_population": len(labels) - len(cover),
            "packet_diameter_squared": diameter_squared,
            "guaranteed_shared_conflict_saving": guaranteed_saving,
            "actual_edge_count_saving": len(edges) - len(cover)}


def circular_sharpness_regression(k):
    """Exact index graph of regular q=k^3 polygon at alpha=2*pi*k/q.

    The report proves optimality of the independent-set bound by a circle
    measure argument. This checks the index graph, matching and attained cover.
    """
    q, length = k ** 3, k
    assert q % 2 == 1 and 4 * length < q
    graph = {i: set() for i in range(q)}
    for i, j in combinations(range(q), 2):
        step = min(j - i, q - (j - i))
        if 2 * step >= q - 2 * length:
            graph[i].add(j)
            graph[j].add(i)
    independent_count = (q + 1) // 2 - length
    retained = set(range(independent_count))
    assert all(not (graph[i] & retained) for i in retained)
    cover = set(graph) - retained
    assert all(i in cover or j in cover for i in graph for j in graph[i])
    step = (q - 1) // 2
    walk = [(i * step) % q for i in range(q)]
    assert len(set(walk)) == q
    matching = [(walk[i], walk[i + 1]) for i in range(0, q - 1, 2)]
    assert all(j in graph[i] for i, j in matching)
    assert len({v for edge in matching for v in edge}) == 2 * len(matching)
    assert len(matching) == q // 2 and len(cover) - len(matching) == length
    return {"q": q, "angular_steps": length, "maximum_matching": len(matching),
            "attained_vertex_cover": len(cover),
            "cover_lower_bound_by_report_circle_measure": len(cover),
            "cover_minus_matching": length}


def main():
    # All population values are exact. No floating point reference-density fit.
    phases = [(F(i, 4), F(j, 4)) for i in range(4) for j in range(4)]
    packets = [packet(k, phase) for k in (1, 2, 3) for phase in phases]
    regressions = [complete_bipartite_regression(k) for k in (2, 4, 8, 16)]
    best = {diameter: max((p for p in packets if p["D"] == diameter),
                         key=lambda p: p["strict_sub_D_population"])
            for diameter in sorted({p["D"] for p in packets})}
    for result in best.values():
        # The undeformed packing is a strictly smaller same-cardinality rival.
        assert F(result["triangle_free_packet_diameter_squared"]) > result["packet_diameter_squared"]
        result["triangle_free_variant_certified_nonglobal"] = True
    print(json.dumps({"classification": "exact finite global comparison packets",
                      "packet_cases": len(packets), "best_packets": best,
                      "complete_bipartite_regressions": regressions,
                      "full_lattice_column_packets": [full_column_packet_regression(k) for k in (2, 3, 4)],
                      "circular_sharpness_regressions": [circular_sharpness_regression(k) for k in (3, 5, 7)],
                      "odd_cycle_regression": odd_cycle_regression(),
                      "largest_cut": max(p["cut_size"] for p in packets),
                      "largest_deletion_improvement": max(p["gain_over_edge_count_deletion_bound"]
                                                          for p in packets),
                      "not_proved": ["unrestricted global optimality", "a larger asymptotic reserve coefficient",
                                     "exclusion of all triangle-free global minimizers", "Level I"]},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
