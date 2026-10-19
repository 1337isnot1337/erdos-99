#!/usr/bin/env python3
"""Exact finite controls for the conditional endpoint-inclusive cut audit."""

from itertools import combinations


def check(condition, message):
    if not condition:
        raise SystemExit("FAIL: " + message)


def flood(adjacency, starts, allowed):
    reached = starts & allowed
    frontier = reached
    while frontier:
        neighbors = 0
        todo = frontier
        while todo:
            bit = todo & -todo
            todo -= bit
            neighbors |= adjacency[bit.bit_length() - 1]
        frontier = neighbors & allowed & ~reached
        reached |= frontier
    return reached


def components(adjacency, allowed):
    count = 0
    unseen = allowed
    while unseen:
        bit = unseen & -unseen
        component = flood(adjacency, bit, unseen)
        unseen &= ~component
        count += 1
    return count


def bit_count(mask):
    return mask.bit_count()


def lattice_fixture():
    inner = [(x, y) for y in range(3) for x in range(3)]
    inner_set = set(inner)
    outer = sorted({(x + dx, y + dy)
                    for x, y in inner
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                    if (x + dx, y + dy) not in inner_set})
    points = inner + outer
    index = {p: i for i, p in enumerate(points)}
    adjacency = [0] * len(points)
    for i, p in enumerate(points):
        for j in range(i):
            q = points[j]
            squared = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
            check(squared >= 1, "fixture violates unit separation")
            if squared == 1:
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i

    check(max(bit_count(row) for row in adjacency) <= 5,
          "fixture contact degree exceeds five")
    check(not any(all(adjacency[v] & (1 << w) for v, w in combinations(t, 2))
                  for t in combinations(range(len(points)), 3)),
          "fixture contact graph contains a triangle")

    inner_adjacency = []
    for p in inner:
        neighbors = 0
        for j, q in enumerate(inner):
            if sum((a - b) ** 2 for a, b in zip(p, q)) == 1:
                neighbors |= 1 << j
        inner_adjacency.append(neighbors)

    all_inner = (1 << len(inner)) - 1
    check(components(inner_adjacency, all_inner) == 1,
          "grid contact subgraph is disconnected")
    brace_cases = 0
    for subset in range(1, all_inner + 1):
        if components(inner_adjacency, subset) != 1:
            continue
        boundary = 0
        vertices = [i for i in range(len(inner)) if subset & (1 << i)]
        diameter_squared = max(
            (inner[i][0] - inner[j][0]) ** 2 + (inner[i][1] - inner[j][1]) ** 2
            for i, j in combinations(vertices, 2)
        ) if len(vertices) > 1 else 0
        full_subset = sum(1 << index[inner[i]] for i in vertices)
        for i in vertices:
            boundary += bit_count(adjacency[index[inner[i]]] & ~full_subset)
        check(boundary >= 2 and (boundary - 2) ** 2 >= diameter_squared,
              "a connected unloaded subset violates the brace")
        brace_cases += 1

    inner_mask = sum(1 << index[p] for p in inner)
    outer_mask = sum(1 << index[p] for p in outer)
    check(not inner_mask & outer_mask, "terminal sets overlap")
    all_vertices = (1 << len(points)) - 1
    diameter_squared = 8
    separators = 0
    partial_outer = full_outer = full_inner = split_inner = 0
    remaining_both = endpoint_deleted = 0
    for deleted in range(1 << len(points)):
        allowed = all_vertices & ~deleted
        reachable = flood(adjacency, outer_mask & allowed, allowed)
        if reachable & inner_mask:
            continue
        separators += 1
        size = bit_count(deleted)
        check(diameter_squared <= 25 * size * size,
              "an endpoint-inclusive separator violates the cut bound")
        removed_outer = deleted & outer_mask
        removed_inner = deleted & inner_mask
        partial_outer += bool(removed_outer and removed_outer != outer_mask)
        full_outer += removed_outer == outer_mask
        full_inner += removed_inner == inner_mask
        remaining_both += bool(outer_mask & allowed and inner_mask & allowed)
        endpoints = (1 << index[(0, 0)]) | (1 << index[(2, 2)])
        endpoint_deleted += bool(deleted & endpoints)
        inner_left = all_inner & ~sum(
            1 << i for i, p in enumerate(inner) if deleted & (1 << index[p]))
        split_inner += components(inner_adjacency, inner_left) >= 2

    check(separators > 0, "fixture produced no separator cases")
    check(partial_outer and full_outer and full_inner,
          "terminal deletion controls were not covered")
    check(split_inner and remaining_both and endpoint_deleted,
          "grid split or endpoint-deletion controls were not covered")
    return len(points), len(outer), brace_cases, separators, partial_outer, full_outer, full_inner, split_inner, remaining_both, endpoint_deleted


def missing_brace_control():
    points = list(range(10))
    targets = set(range(3, 10))
    separator = {2}
    diameter = max(targets) - min(targets)
    check(diameter == 6 and 5 * len(separator) == 5,
          "missing-brace path control has the wrong dimensions")
    check(all(abs(a - b) >= 1 for a, b in combinations(points, 2)),
          "missing-brace path control violates unit separation")
    path_adjacency = [0] * len(points)
    for i in range(len(points) - 1):
        path_adjacency[i] |= 1 << (i + 1)
        path_adjacency[i + 1] |= 1 << i
    reachable = flood(path_adjacency, 1 << 0,
                      ((1 << len(points)) - 1) & ~(1 << 2))
    check(not reachable & sum(1 << v for v in targets),
          "the declared path separator does not separate the terminals")
    # U={4,...,9} has only one contact leaving it, so the brace fails.
    u = set(range(4, 10))
    boundary = sum(abs(v - w) == 1 for v in u for w in points if w not in u)
    check(boundary == 1, "missing-brace control has the wrong boundary size")
    check(boundary < (max(u) - min(u)) + 2,
          "the negative control unexpectedly satisfies the brace")
    return diameter, len(separator), boundary, max(u) - min(u)


def main():
    result = lattice_fixture()
    (vertices, attachments, brace_cases, separators, partial_outer,
     full_outer, full_inner, split_inner, remaining_both,
     endpoint_deleted) = result
    print(f"PASS: {vertices}-vertex unit square-lattice fixture, {attachments} loaded attachments, "
          f"{brace_cases} connected unloaded subsets satisfy the exact brace check")
    print(f"PASS: all {1 << vertices} deletion sets enumerated; {separators} are separators, "
          f"including {partial_outer} partial-terminal, {full_outer} full-attachment, "
          f"{full_inner} full-grid, {split_inner} grid-splitting, {remaining_both} "
          f"with both terminal sets remaining, and {endpoint_deleted} deleting a diametral endpoint")
    diameter, cut_size, boundary, brace_diameter = missing_brace_control()
    print(f"PASS: missing-brace control has diam(X)={diameter} > 5|S|={5 * cut_size}; "
          f"the chosen connected U has boundary {boundary} < diam(U)+2={brace_diameter + 2}")
    print("SCOPE: finite controls only; they do not establish the universal analytic brace or source extraction")


main()
