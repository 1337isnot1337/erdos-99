#!/usr/bin/env python3
"""Exact full-source replacement certificates; no optimality inference.

Coordinates are ((xa + xb*sqrt(3))/2, (ya + yb*sqrt(3))/2).
Every source, candidate, mixed lower pair and mixed upper pair is checked.
The matching is certified by an equally sized vertex cover, and the final
configuration is checked independently of the graph construction.
"""

if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from collections import deque
from itertools import combinations
import json


def sign3(a, b):
    """Sign of a + b*sqrt(3), using integer comparisons only."""
    if not b:
        return (a > 0) - (a < 0)
    if not a or (a > 0) == (b > 0):
        return (b > 0) - (b < 0)
    # Nonzero integer a,b cannot satisfy a*a == 3*b*b.
    c = (a * a > 3 * b * b) - (a * a < 3 * b * b)
    assert c
    return c if a > 0 else -c


def distance2(p, q):
    dx, ex, dy, ey = (p[i] - q[i] for i in range(4))
    return dx * dx + 3 * ex * ex + dy * dy + 3 * ey * ey, 2 * (dx * ex + dy * ey)


def compare_distance(p, q, threshold):
    a, b = distance2(p, q)
    return sign3(a - 4 * threshold, b)


def check_cloud(points, diameter2, strict):
    maximum = (0, 0)
    for p, q in combinations(points, 2):
        assert compare_distance(p, q, 1) >= 0, "lower pair failure"
        s = compare_distance(p, q, diameter2)
        assert s < 0 if strict else s <= 0, "upper pair failure"
        a, b = distance2(p, q)
        if sign3(a - maximum[0], b - maximum[1]) > 0:
            maximum = a, b
    return maximum


def maximum_matching_and_cover(neighbors, right_count):
    """Hopcroft--Karp, followed by an exact Konig dual certificate."""
    left_count = len(neighbors)
    ml, mr = [-1] * left_count, [-1] * right_count

    while True:
        depth = [-1] * left_count
        queue = deque()
        for u in range(left_count):
            if ml[u] < 0:
                depth[u] = 0
                queue.append(u)
        terminal = None
        while queue:
            u = queue.popleft()
            if terminal is not None and depth[u] >= terminal:
                continue
            for v in neighbors[u]:
                mate = mr[v]
                if mate < 0:
                    terminal = depth[u] + 1
                elif depth[mate] < 0:
                    depth[mate] = depth[u] + 1
                    queue.append(mate)
        if terminal is None:
            break

        def augment(u):
            for v in neighbors[u]:
                mate = mr[v]
                if (mate < 0 and depth[u] + 1 == terminal) or (
                    mate >= 0 and depth[mate] == depth[u] + 1 and augment(mate)
                ):
                    ml[u], mr[v] = v, u
                    return True
            depth[u] = -1
            return False

        for u in range(left_count):
            if ml[u] < 0:
                augment(u)

    reached_l = {u for u in range(left_count) if ml[u] < 0}
    reached_r = set()
    queue = deque(reached_l)
    while queue:
        u = queue.popleft()
        for v in neighbors[u]:
            if ml[u] == v or v in reached_r:
                continue
            reached_r.add(v)
            if mr[v] >= 0 and mr[v] not in reached_l:
                reached_l.add(mr[v])
                queue.append(mr[v])
    cover_l = set(range(left_count)) - reached_l
    cover_r = reached_r
    matching = {(u, v) for u, v in enumerate(ml) if v >= 0}
    assert len({v for _, v in matching}) == len(matching)
    assert all(v in neighbors[u] for u, v in matching)
    assert all(u in cover_l or v in cover_r for u, ns in enumerate(neighbors) for v in ns)
    assert len(matching) == len(cover_l) + len(cover_r)
    return matching, cover_l, cover_r


def exchange(source, cloud, source_diameter2, deleted, diameter2=None):
    diameter2 = source_diameter2 if diameter2 is None else diameter2
    assert 1 < diameter2 <= source_diameter2
    check_cloud(source, source_diameter2, False)
    check_cloud(cloud, diameter2, True)
    diameter_pairs = {
        (i, j) for i, j in combinations(range(len(source)), 2)
        if compare_distance(source[i], source[j], source_diameter2) == 0
    }
    assert diameter_pairs, "the proposed diameter must be attained by the source"
    upper_pairs = {
        (i, j) for i, j in combinations(range(len(source)), 2)
        if compare_distance(source[i], source[j], diameter2) >= 0
    }
    assert all(i in deleted or j in deleted for i, j in upper_pairs), "uncovered upper pair"
    remaining = [i for i in range(len(source)) if i not in deleted]
    neighbors = []
    lower_count = upper_count = 0
    for i in remaining:
        ns = []
        for j, q in enumerate(cloud):
            low = compare_distance(source[i], q, 1) < 0
            high = compare_distance(source[i], q, diameter2) >= 0
            lower_count += low
            upper_count += high
            if low or high:
                ns.append(j)
        neighbors.append(ns)
    matching, cover_l, cover_r = maximum_matching_and_cover(neighbors, len(cloud))
    retained = [i for k, i in enumerate(remaining) if k not in cover_l]
    inserted = [j for j in range(len(cloud)) if j not in cover_r]
    points = [source[i] for i in retained] + [cloud[j] for j in inserted]
    check_cloud(points, diameter2, True)
    certified_count = len(source) - len(deleted) + len(cloud) - len(matching)
    assert len(points) == certified_count
    # Drop surplus candidate labels, then surplus source labels if necessary.
    witness = points[:len(source)] if certified_count >= len(source) else None
    if witness is not None:
        assert len(witness) == len(source)
        maximum = check_cloud(witness, diameter2, True)
        margin = [4 * source_diameter2 - maximum[0], -maximum[1]]
        assert sign3(*margin) > 0
    else:
        maximum = margin = None
    return {
        "source_count": len(source), "cloud_count": len(cloud),
        "deleted_diameter_cover": len(deleted), "actual_diameter_pairs": len(diameter_pairs),
        "source_upper_conflicts": len(upper_pairs), "target_diameter_squared": diameter2,
        "mixed_lower_conflicts": lower_count, "mixed_upper_conflicts": upper_count,
        "matching_and_cover_size": len(matching), "hall_deficiency": len(cloud) - len(matching),
        "independent_count": certified_count, "retained_source_count": len(retained),
        "inserted_cloud_count": len(inserted), "strict_competitor": witness is not None,
        "witness_diameter_squared_times_four": maximum,
        "source_to_witness_squared_margin_times_four": margin,
        "certificate": {
            "deleted_source_labels": sorted(deleted),
            "matching": [[remaining[u], v] for u, v in sorted(matching)],
            "cover_source_labels": sorted(remaining[u] for u in cover_l),
            "cover_cloud_labels": sorted(cover_r),
            "retained_source_labels": retained,
            "inserted_cloud_labels": inserted,
        },
    }


def replay_certificate(source, cloud, source_diameter2, diameter2, certificate):
    """Check serialized labels and dual witnesses without running matching."""
    assert 1 < diameter2 <= source_diameter2
    check_cloud(source, source_diameter2, False)
    assert any(compare_distance(p, q, source_diameter2) == 0
               for p, q in combinations(source, 2))
    check_cloud(cloud, diameter2, True)
    fields = ["deleted_source_labels", "cover_source_labels", "cover_cloud_labels",
              "retained_source_labels", "inserted_cloud_labels"]
    sets = {}
    for name in fields:
        values = certificate[name]
        assert all(type(v) is int for v in values)
        assert len(set(values)) == len(values)
        count = len(cloud) if "cloud" in name else len(source)
        assert all(0 <= v < count for v in values)
        sets[name] = set(values)
    deleted = sets[fields[0]]
    remaining = set(range(len(source))) - deleted
    cl, cr = sets[fields[1]], sets[fields[2]]
    assert cl <= remaining
    assert sets[fields[3]] == remaining-cl
    assert sets[fields[4]] == set(range(len(cloud)))-cr
    for i, j in combinations(sorted(remaining), 2):
        assert compare_distance(source[i], source[j], diameter2) < 0
    conflicts = {(i, j) for i in remaining for j in range(len(cloud))
                 if compare_distance(source[i], cloud[j], 1) < 0
                 or compare_distance(source[i], cloud[j], diameter2) >= 0}
    assert all(i in cl or j in cr for i, j in conflicts)
    matching = certificate["matching"]
    assert all(len(e) == 2 and all(type(v) is int for v in e) for e in matching)
    assert len({i for i, _ in matching}) == len(matching)
    assert len({j for _, j in matching}) == len(matching)
    assert all(tuple(e) in conflicts for e in matching)
    assert len(matching) == len(cl)+len(cr)
    labels = ([source[i] for i in certificate[fields[3]]]
              + [cloud[j] for j in certificate[fields[4]]])
    assert len(labels) == len(source)-len(deleted)+len(cloud)-len(matching)
    check_cloud(labels, diameter2, True)
    if len(labels) >= len(source):
        check_cloud(labels[:len(source)], diameter2, True)
    return len(labels)


def bipartite_upper_cover(source, left_labels, diameter2):
    """Certify a minimum cover of *all* old upper violations at the target."""
    left = sorted(left_labels)
    right = [i for i in range(len(source)) if i not in left_labels]
    for side in (left, right):
        assert all(compare_distance(source[i], source[j], diameter2) < 0
                   for i, j in combinations(side, 2)), "upper graph is not bipartite in this partition"
    neighbors = [[v for v, j in enumerate(right)
                  if compare_distance(source[i], source[j], diameter2) >= 0]
                 for i in left]
    _, cl, cr = maximum_matching_and_cover(neighbors, len(right))
    return {left[u] for u in cl} | {right[v] for v in cr}


def square(k):
    return [(2 * x, 0, 2 * y, 0) for x in range(k) for y in range(k)]


def lattice_disk(center, radius):
    c = 2 * center
    return [
        (2 * i + j + c, 0, c, j)
        for i in range(-2 * radius, 2 * radius + 1)
        for j in range(-2 * radius, 2 * radius + 1)
        if i * i + i * j + j * j < radius * radius
    ]


def must_fail(callback):
    try:
        callback()
    except AssertionError:
        return
    raise AssertionError("hostile input unexpectedly accepted")


def main():
    assert sum(x * x + y * y < 256 for x in range(-16, 17) for y in range(-16, 17)) == 793
    assert len(lattice_disk(0, 15)) == 817
    # Both signs and both magnitude cases for the quadratic field comparison.
    for a, b, expected in [(2, -1, 1), (1, -1, -1), (-2, 1, -1), (-1, 1, 1), (0, -1, -1)]:
        assert sign3(a, b) == expected
    source = square(2)
    triangle = [(0, 0, 0, 0), (2, 0, 0, 0), (1, 0, 0, 1)]
    negative = exchange(source, triangle, 2, {0, 1})
    assert not negative["strict_competitor"]
    must_fail(lambda: exchange(source, source, 2, {0, 1}))  # equal upper pair in cloud
    must_fail(lambda: exchange(source, triangle, 2, {0}))  # uncovered actual diameter
    must_fail(lambda: check_cloud([(0, 0, 0, 0), (1, 0, 0, 0)], 2, True))
    # The label (3,0) is an actual contact isolate, and blocks the insertion.
    full_source = triangle + [(6, 0, 0, 0)]
    assert all(compare_distance(full_source[-1], p, 1) > 0 for p in triangle)
    isolate_block = exchange(full_source, [(5, 0, 0, 0)], 9, {0})
    assert isolate_block["mixed_lower_conflicts"] == 1
    assert isolate_block["matching_and_cover_size"] == 1
    upper_block = exchange(full_source, [(8, 0, 0, 0)], 9, {0})
    assert upper_block["mixed_upper_conflicts"] == 2
    certificate = json.loads(json.dumps(isolate_block["certificate"]))
    assert replay_certificate(full_source, [(5, 0, 0, 0)], 9, 9, certificate) == 3
    # Dropping an isolate or repeating a matching endpoint is not preservation.
    dropped = json.loads(json.dumps(certificate))
    dropped["retained_source_labels"].pop()
    must_fail(lambda: replay_certificate(full_source, [(5, 0, 0, 0)], 9, 9, dropped))
    repeated = json.loads(json.dumps(certificate))
    repeated["matching"] *= 2
    must_fail(lambda: replay_certificate(full_source, [(5, 0, 0, 0)], 9, 9, repeated))
    fixtures = [
        {"name": "globally_optimal_square_regression", **negative},
        {"name": "actual_contact_isolate_blocker", **isolate_block},
        {"name": "inactive_and_equal_upper_blockers", **upper_block},
    ]
    for k, radius, target in [(31, 15, 38), (41, 18, 52)]:
        old = square(k)
        cloud = lattice_disk((k - 1) // 2, radius)
        left = {i for i, p in enumerate(old) if p[0] < k - 1}
        deleted = bipartite_upper_cover(old, left, target * target)
        result = exchange(old, cloud, 2 * (k - 1) ** 2, deleted, target * target)
        assert result["strict_competitor"], result
        assert result["cloud_count"] < result["source_count"]
        assert result["retained_source_count"] > 0
        assert replay_certificate(old, cloud, 2*(k-1)**2, target*target,
                                  json.loads(json.dumps(result["certificate"]))) == result["independent_count"]
        fixtures.append({"name": f"whole_source_square_{k}", **result})
    print(json.dumps({
        "arithmetic": "integer comparisons in Q(sqrt(3)); no floats",
        "classification": "proved candidate certificate plus nonglobal regressions",
        "level_i_closed": False,
        "fixtures": fixtures,
    }, indent=2))


if __name__ == "__main__":
    main()
