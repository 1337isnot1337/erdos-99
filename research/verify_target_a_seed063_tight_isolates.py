#!/usr/bin/env python3
"""Exact finite certificates for the seed-63 Target A report.

No dependencies. Lattice coordinates use Q(a,b)=a*a+a*b+b*b.
The arbitrary-size/all-phase/global exchange results are proved in the report;
this program certifies the stated fixtures and negative controls only.
"""

from fractions import Fraction as F
from itertools import combinations


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def scale(t, p):
    return t * p[0], t * p[1]


def norm2(p):
    a, b = p
    return a * a + a * b + b * b


def dot(p, q):
    return p[0] * q[0] + p[1] * q[1] + F(1, 2) * (
        p[0] * q[1] + p[1] * q[0]
    )


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def all_pairs(points, lower=1, upper=None, strict_lower=False):
    count = 0
    maximum = 0
    for p, q in combinations(points, 2):
        squared = norm2(sub(p, q))
        require(squared > lower if strict_lower else squared >= lower,
                ("lower pair", p, q, squared))
        if upper is not None:
            require(squared < upper, ("upper pair", p, q, squared))
        maximum = max(maximum, squared)
        count += 1
    return count, maximum


PHASE = (F(1, 5), F(1, 7))
UNIT = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))
NEIGHBOR_OFFSETS = ((0, 0), (-1, 0), (0, -1))


def phase_neighbors(x):
    return {add(x, w) for w in NEIGHBOR_OFFSETS}


def distance_to_segment2(p, a, b):
    edge = sub(b, a)
    t = dot(sub(p, a), edge) / norm2(edge)
    t = min(F(1), max(F(0), t))
    return norm2(sub(p, add(a, scale(t, edge))))


def distance_to_triangle2(p, m):
    if p[0] >= 0 and p[1] >= 0 and p[0] + p[1] <= m:
        return F(0)
    corners = ((0, 0), (m, 0), (0, m))
    return min(distance_to_segment2(p, corners[i], corners[(i + 1) % 3])
               for i in range(3))


def segments_meet(a, b, c, d):
    def orient(p, q, r):
        u, v = sub(q, p), sub(r, p)
        return u[0]*v[1] - u[1]*v[0]

    def on_segment(p, q, r):
        return (orient(p, q, r) == 0
                and all(min(p[i], q[i]) <= r[i] <= max(p[i], q[i])
                        for i in (0, 1)))

    o1, o2 = orient(a, b, c), orient(a, b, d)
    o3, o4 = orient(c, d, a), orient(c, d, b)
    return ((o1*o2 < 0 and o3*o4 < 0)
            or on_segment(a, b, c) or on_segment(a, b, d)
            or on_segment(c, d, a) or on_segment(c, d, b))


def matrix_rank(rows):
    matrix = [list(map(F, row)) for row in rows]
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next((i for i in range(rank, len(matrix))
                      if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        lead = matrix[rank][column]
        matrix[rank] = [value/lead for value in matrix[rank]]
        for i in range(rank+1, len(matrix)):
            factor = matrix[i][column]
            if factor:
                matrix[i] = [a-factor*b for a, b in zip(matrix[i], matrix[rank])]
        rank += 1
    return rank


def phase_rule():
    tested = {(0, 0), *UNIT}
    actual = {w for w in tested if norm2(add(w, PHASE)) < 1}
    require(actual == set(NEIGHBOR_OFFSETS), "phase neighbor rule")
    require([norm2(add(w, PHASE)) for w in NEIGHBOR_OFFSETS]
            == [F(109, 1225), F(669, 1225), F(739, 1225)],
            "exact neighbor distances")
    require(all(norm2(add(w, PHASE)) != 1 for w in tested), "unit equality")
    require(norm2(PHASE) < F(1, 9), "nonunit lattice exclusion margin")
    # All other nonzero lattice vectors have norm >= sqrt(3), by Q mod 3.
    # Therefore their phase distance is > sqrt(3)-1/3 > 1.
    for a in range(-6, 7):
        for b in range(-6, 7):
            require((a*a+a*b+b*b) % 3 in (0, 1), "quadratic residue rule")
            if (a, b) not in tested:
                require(norm2(add((a, b), PHASE)) > 1,
                        ("nonneighbor", a, b))


def chamber(m, exhaustive=False):
    source = {(i, j) for i in range(m + 1) for j in range(m + 1 - i)}
    z_rows = {(i, j) for i in range(m) for j in range(m - i)}
    y_rows = set().union(*(phase_neighbors(x) for x in source))
    n = (m + 1) * (m + 2) // 2
    require(len(source) == n, "population")
    require(len(z_rows) == m * (m + 1) // 2, "interior population")
    pairs, diameter2 = all_pairs(sorted(source))
    require(diameter2 == m*m, "actual diameter")
    require(F(m*m, 2) + F(3*m, 2) + 1 == n, "Oler capacity arithmetic")

    # Independent exact convex-distance enumeration of the full response shore.
    actual_y = set()
    for i in range(-2, m + 3):
        for j in range(-2, m + 3):
            distance2 = distance_to_triangle2(add((i, j), PHASE), m)
            require(distance2 != 1, "collar boundary equality")
            if distance2 < 1:
                actual_y.add((i, j))
    require(actual_y == y_rows, "full collar shore")
    o_rows = y_rows - z_rows
    require(len(o_rows) == 3*(m+1), "exterior population")

    # All contact/facet equilibrium equations, in rational lattice coordinates.
    normals = ((F(-4, 3), F(2, 3)), (F(2, 3), F(-4, 3)),
               (F(2, 3), F(2, 3)))
    contacts = []
    for x in sorted(source):
        neighbors = {add(x, w) for w in UNIT} & source
        force = (0, 0)
        for q in neighbors:
            force = add(force, sub(x, q))
            if x < q:
                contacts.append((x, q))
        reaction = (0, 0)
        for active, normal in zip((x[0] == 0, x[1] == 0, sum(x) == m), normals):
            if active:
                reaction = add(reaction, scale(F(3, 2), normal))
        require(force == reaction, ("force balance", m, x, force, reaction))
    require(len(contacts) == 3*m*(m+1)//2, "contact edge count")
    if m in (4, 5):
        indices = {x: i for i, x in enumerate(sorted(source))}
        rows = []
        for p, q in contacts:
            da, db = sub(p, q)
            row = [0]*(2*n)
            for vertex, sign in ((p, 1), (q, -1)):
                row[2*indices[vertex]] = sign*(2*da+db)
                row[2*indices[vertex]+1] = sign*(da+2*db)
            rows.append(row)
        for x in sorted(source):
            for active, covector in zip((x[0] == 0, x[1] == 0, sum(x) == m),
                                       ((-1, 0), (0, -1), (1, 1))):
                if active:
                    row = [0]*(2*n)
                    row[2*indices[x]:2*indices[x]+2] = covector
                    rows.append(row)
        require(matrix_rank(rows) == 2*n, "exact full mixed rank")

    # The explicitly stated fan and its lens rows.
    t1, t2, t3 = (1, 1), (2, 1), (1, 2)
    spokes = [[t1, (0, 1)], [t2, (2, 0)],
              [(1, j) for j in range(2, m)]]
    require(all(set(spokes[i]).isdisjoint(spokes[j])
                for i in range(3) for j in range(i+1, 3)), "disjoint channels")
    fan_vertices = set().union(*(set(path) for path in spokes))
    fan_edges = [(t1, t2), (t1, t3), (t2, t3)]
    for path in spokes:
        fan_edges.extend(zip(path, path[1:]))
    require(len(fan_edges) == len(fan_vertices) == m+2, "unicyclic fan")
    require(all(norm2(sub(p, q)) == 1 for p, q in fan_edges), "fan contacts")
    lens_rows = set().union(*(phase_neighbors(p) & phase_neighbors(q)
                              for p, q in fan_edges))
    expected_lens = {(1, 1), (0, 1), (2, 0)} | {(1, j) for j in range(2, m-1)}
    require(lens_rows == expected_lens and len(lens_rows) == m,
            "exact fan lenses")
    require(lens_rows <= z_rows, "interior-only lens")

    # Equation (8): row -> source, a complete Z-perfect matching.
    matching = {z: z for z in z_rows}
    matching[(0, 1)] = t1
    matching[(2, 0)] = t2
    for j in range(1, m-2):
        matching[(1, j)] = (1, j+1)
    matching[(1, m-2)] = (2, m-2)
    for i in range(2, m-1):
        matching[(i, 1)] = (i+1, 1)
    basis = set(matching.values())
    require(len(basis) == len(z_rows), "injective matching")
    require(all(x in source and z in phase_neighbors(x)
                for z, x in matching.items()), "matched conflict edges")
    deep = {x for x in source if phase_neighbors(x) <= z_rows}
    require(deep <= basis, "deep-first basis")
    require(len(deep) == (m-1)*(m-2)//2, "deep population")
    terminals = source - basis
    reactions = {path[-1] for path in spokes}
    require(reactions <= terminals, "three reaction terminals")
    require(terminals & fan_vertices == reactions, "shielded terminal count")
    inverse = {x: z for z, x in matching.items()}
    require(all(inverse[x] in lens_rows for x in basis & fan_vertices),
            "beta equals zero")
    surviving_terminals = terminals - fan_vertices
    # Each direct sink x+v is exterior and avoids every deleted lens pair.
    require(all(x in o_rows and x not in lens_rows for x in surviving_terminals),
            "surviving direct sink linkages")
    require(all(not segments_meet(x, add(x, PHASE), p, q)
                for x in surviving_terminals for p, q in fan_edges),
            "actual direct paths avoid the geometric fan")
    require(len(surviving_terminals) == m-2, "coarse Hall saturation size")
    require(len(terminals) == m+1, "Schur full column rank")

    if exhaustive:
        ordered_z = sorted(z_rows)
        ordered_x = sorted(source)
        bit_neighbors = [sum(1 << i for i, x in enumerate(ordered_x)
                             if z in phase_neighbors(x)) for z in ordered_z]
        minimum_surplus = n
        for mask in range(1, 1 << len(ordered_z)):
            neighborhood = 0
            for i, neighbors in enumerate(bit_neighbors):
                if mask & (1 << i):
                    neighborhood |= neighbors
            surplus = neighborhood.bit_count() - mask.bit_count()
            require(surplus >= 1, ("strict Hall", mask, surplus))
            minimum_surplus = min(minimum_surplus, surplus)
        require(minimum_surplus >= 1, "active coloop absence")

    return pairs, n, len(z_rows), len(surviving_terminals)


def restoration_fixture():
    c = (F(1, 3), F(1, 3))
    rows = [(0, 0), (1, 0), (0, 1)]
    deleted = [add(c, scale(F(11, 10), sub(q, c))) for q in rows]
    retained = [(-4, -4), (4, -4), (4, 4), (-4, 4)]
    source = retained + deleted
    neighbors = {i for i, x in enumerate(source)
                 if any(norm2(sub(x, z)) < 1 for z in rows)}
    require(neighbors == {4, 5, 6}, "tight isolate fixture")
    require(all(norm2(sub(x, z)) != 1 for x in source for z in rows),
            "fixture cross genericity")
    require(all(norm2(sub(p, q)) > 1 for p, q in combinations(source, 2)),
            "old strict contacts")
    new_rows = [add(c, scale(F(101, 100), sub(q, c))) for q in rows]
    old_pairs, old_diameter2 = all_pairs(source, strict_lower=True)
    new_pairs, new_diameter2 = all_pairs(retained + new_rows, strict_lower=True)
    require(old_diameter2 == new_diameter2 == 192, "retained upper pair")
    require(all(norm2(sub(q, x)) < 192 for q in new_rows for x in retained),
            "all new-retained upper margins")
    require(all(norm2(sub(p, q)) < 192 for p, q in combinations(new_rows, 2)),
            "all new-new upper margins")
    return old_pairs + new_pairs


def controls_and_small_global_case():
    triangle = {(0, 0), (1, 0), (0, 1)}
    # Global D(3)=1 fixture; the unique interior row has all three neighbors.
    q = PHASE
    require(all(norm2(sub(q, x)) < 1 for x in triangle), "U_1,3 row")
    require(all(norm2(sub(p, r)) == 1 for p, r in combinations(triangle, 2)),
            "global unit triangle")
    require(len(triangle) - 1 == 2, "only two nonbasis terminals")
    # Dropping interior placement, while retaining generic cross clearance, fails.
    outside = scale(-1, PHASE)
    neighbors = {x for x in triangle if norm2(sub(outside, x)) < 1}
    require(neighbors == {(0, 0)}, "outside tight active neighborhood")
    require(all(norm2(sub(outside, x)) != 1 for x in triangle), "outside generic")
    require(max(norm2(sub(outside, x)) for x in triangle - neighbors) > 1,
            "outside replacement violates global upper bound")
    # Dropping cross genericity in an exact capacity chamber also fails:
    # an interior old lattice point has only itself as a strict neighbor.
    m = 4
    source = {(i, j) for i in range(m+1) for j in range(m+1-i)}
    same = (1, 1)
    require({x for x in source if norm2(sub(same, x)) < 1} == {same},
            "nongeneric tight singleton")
    require(all(add(same, w) in source for w in UNIT), "six equality blockers")


def strict_competitor(m):
    r, s = (2*m + 2)//3 + 1, (3*m + 3)//4 + 2
    population = (m+1)*(m+2)//2
    packet = [(i-j//2, j) for j in range(s) for i in range(r)]
    require(len(packet) >= population, "competitor population")
    box2 = (F(r)-F(1, 2))**2 + F(3, 4)*(s-1)**2
    bound = F(499, 576)*m*m + F(17, 4)*m + F(21, 4)
    require(box2 < bound < m*m, "strict diameter bound")
    pairs, actual2 = all_pairs(packet, upper=m*m)
    require(actual2 <= box2, "actual packet box bound")
    selected_pairs, _ = all_pairs(packet[:population], upper=m*m)
    return pairs + selected_pairs, population, len(packet), actual2


def main():
    phase_rule()
    source_pair_count = 0
    for m in (4, 5, 8, 15, 33):
        pairs, n, z, direct = chamber(m, exhaustive=(m == 4))
        source_pair_count += pairs
        print(f"M={m}: n={n}, |Z|={z}, Schur rank={m+1}, beta=0, "
              f"coarse deficiency=0, surviving direct paths={direct}")
    packet_pair_count = 0
    for m in (33, 40):
        pairs, n, available, diameter2 = strict_competitor(m)
        packet_pair_count += pairs
        print(f"competitor M={m}: retains {n} labels from {available}; "
              f"full-packet diameter squared={diameter2} < {m*m}")
    require(F(77, 576)*33*33-F(17, 4)*33-F(21, 4) == F(5, 64),
            "infinite-family threshold base")
    require(F(77, 576)*(2*33+1)-F(17, 4) > 0,
            "integer threshold gap increases for all M>=33")
    exchange_pairs = restoration_fixture()
    controls_and_small_global_case()
    print(f"PASS: {source_pair_count} source pairs, {packet_pair_count} packet "
          f"pairs, {exchange_pairs} exchange pairs; 1023 nonempty right subsets; "
          "global three-point and two hypothesis controls")
    print("Scope: exact finite certificates; general proofs are in the report. "
          "No Level I or large-source global-optimality claim.")


if __name__ == "__main__":
    main()
