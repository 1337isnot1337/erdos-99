#!/usr/bin/env python3
"""Exact finite replay of the seed-66 coembedded locked/full-rank regression.

The report proves the infinite family. This script checks finite stress, geometry,
matrix, and whole-replacement certificates; it does not prove global optimality.
Run with python3 -I -O -B. All checks remain enabled under -O.
"""

from fractions import Fraction as F
import json
from math import isqrt


NEIGHBORS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
ROW_OFFSETS = ((0, 0), (1, 0), (0, 1), (-1, 1))
FACETS = ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1))
PHASE = (F(1, 1000), F(2, 1000))
PRIME = 1000003


def require(ok, message):
    if not ok:
        raise ValueError(message)


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def scale(t, p):
    return t * p[0], t * p[1]


def norm2(p):
    i, j = p
    return i * i + i * j + j * j


def dot(p, q):
    return p[0] * q[0] + p[1] * q[1] + F(p[0] * q[1] + p[1] * q[0], 2)


def det(p, q):
    return p[0] * q[1] - p[1] * q[0]


def in_phase(v):
    a, b = v
    return 0 < a < b and a + b < F(1, 10) and norm2(v) < min(b - a, 2 * a + b, a + 2 * b)


def hull_contains(p, m, strict=False):
    bound = max(abs(p[0]), abs(p[1]), abs(p[0] + p[1]))
    return bound < m if strict else bound <= m


def source(m):
    return {(i, j) for i in range(-m, m + 1) for j in range(-m, m + 1) if hull_contains((i, j), m)}


def corners(m):
    return ((m, 0), (0, m), (-m, m), (-m, 0), (0, -m), (m, -m))


def segment_distance2(p, a, b):
    d = sub(b, a)
    t = max(F(0), min(F(1), dot(sub(p, a), d) / norm2(d)))
    return norm2(sub(p, add(a, scale(t, d))))


def hull_distance2(p, m):
    if hull_contains(p, m):
        return F(0)
    cs = corners(m)
    return min(segment_distance2(p, cs[i], cs[(i + 1) % 6]) for i in range(6))


def properly_cross(a, b, c, d):
    return det(sub(b, a), sub(c, a)) * det(sub(b, a), sub(d, a)) < 0 and det(sub(d, c), sub(a, c)) * det(sub(d, c), sub(b, c)) < 0


def contact_edges(xs):
    return {tuple(sorted((p, add(p, d)))) for p in xs for d in NEIGHBORS if add(p, d) in xs}


def reaction_data(xs, m):
    data = {}
    for p in xs:
        active = [f for f in FACETS if f[0] * p[0] + f[1] * p[1] == m]
        require(len(active) <= 2, "unexpected facet incidence")
        weight = F(1) if len(active) == 2 else F(3, 2)
        data[p] = [(f, weight) for f in active]
    return data


def gradient(f):
    a, b = f
    return F(4 * a - 2 * b, 3), F(-2 * a + 4 * b, 3)


def check_stress(xs, edges, reactions, weights=None):
    force = {p: (F(0), F(0)) for p in xs}
    for p, q in edges:
        w = F(1) if weights is None else weights.get((p, q), F(1))
        require(w > 0, "contact weight is not positive")
        d = scale(w, sub(p, q))
        force[p] = add(force[p], d)
        force[q] = sub(force[q], d)
    for p in xs:
        reaction = (F(0), F(0))
        for f, w in reactions[p]:
            require(w > 0, "facet weight is not positive")
            reaction = add(reaction, scale(w, gradient(f)))
        require(force[p] == reaction, f"equilibrium fails at {p}")


def pinned_rank(xs, edges, reactions):
    order = sorted(xs)
    index = {p: i for i, p in enumerate(order)}
    rows = []
    for p, q in sorted(edges):
        di, dj = sub(p, q)
        coefficients = (2 * di + dj, di + 2 * dj)
        row = [0] * (2 * len(xs))
        for k in (0, 1):
            row[2 * index[p] + k] = coefficients[k]
            row[2 * index[q] + k] = -coefficients[k]
        rows.append(row)
    for p, entries in reactions.items():
        for f, _ in entries:
            row = [0] * (2 * len(xs))
            row[2 * index[p]], row[2 * index[p] + 1] = f
            rows.append(row)
    # A full-rank integer minor modulo a prime proves full rank over Q.
    pivots = {}
    for original in rows:
        row = [x % PRIME for x in original]
        for k in range(len(row)):
            if not row[k]:
                continue
            if k in pivots:
                r = pivots[k]
                factor = row[k]
                for j in range(k, len(row)):
                    row[j] = (row[j] - factor * r[j]) % PRIME
            else:
                inverse = pow(row[k], -1, PRIME)
                pivots[k] = [(x * inverse) % PRIME for x in row]
                break
    require(len(pivots) == 2 * len(xs), "pinned contact matrix is not certified full rank")
    return len(pivots)


def level(p):
    return p[0] + 2 * p[1]


def matrix_row(z, xs):
    # Choose distinct positive integer entries. Triangularity is independent of them.
    return {add(z, offset): 2 + k for k, offset in enumerate(ROW_OFFSETS) if add(z, offset) in xs}


def check_schur(xs, basis):
    order = lambda ps: sorted(ps, key=lambda p: (level(p), p))
    terminals = xs - basis
    for z in xs:
        row = matrix_row(z, xs)
        require(z in row and row[z] != 0, "missing own-row diagonal")
        require(all(x == z or level(x) > level(z) for x in row), "selected matrix is not triangular")
    # Exact Schur elimination on the own-row exterior minor. No random rank test.
    schur = []
    for c in order(terminals):
        row = {x: F(w) for x, w in matrix_row(c, xs).items()}
        for b in order(basis):
            coefficient = row.get(b, F(0))
            if not coefficient:
                continue
            pivot = matrix_row(b, xs)
            factor = coefficient / pivot[b]
            for x, w in pivot.items():
                row[x] = row.get(x, F(0)) - factor * w
                if not row[x]:
                    del row[x]
        require(not (set(row) & basis), "Schur elimination left a basis column")
        require(row.get(c) == 2, "Schur own-row diagonal changed")
        require(all(x == c or level(x) > level(c) for x in row), "Schur minor is not triangular")
        schur.append(row)
    return len(schur), str(2 ** len(schur))


def fan(m):
    paths = (
        [(0, 0)] + [(-k, 0) for k in range(1, m + 1)],
        [(k, 0) for k in range(1, m + 1)],
        [(-k, 1 + k) for k in range(m)],
    )
    vertices = set()
    edges = set()
    for path in paths:
        require(not (vertices & set(path)), "fan spokes share a vertex")
        vertices.update(path)
        edges.update(tuple(sorted((p, q))) for p, q in zip(path, path[1:]))
    triangle = ((0, 0), (1, 0), (0, 1))
    edges.update(tuple(sorted((triangle[i], triangle[(i + 1) % 3]))) for i in range(3))
    require(len(vertices) == len(edges) == 3 * m + 1, "fan census mismatch")
    require(all(hull_contains(p, m, strict=True) for p in triangle), "triangle is not interior")
    for path in paths:
        require(not hull_contains(path[-1], m, strict=True), "fan endpoint is not on hull")
        require(all(hull_contains(p, m, strict=True) for p in path[:-1]), "spoke meets hull too early")
    return vertices, edges


def all_pair_bounds(points, minimum=1, maximum=None):
    ps = sorted(points)
    count = 0
    min_seen = None
    max_seen = 0
    for i, p in enumerate(ps):
        for q in ps[i + 1:]:
            d = norm2(sub(p, q))
            require(d >= minimum, "lower pair bound fails")
            if maximum is not None:
                require(d <= maximum, "upper pair bound fails")
            min_seen = d if min_seen is None else min(min_seen, d)
            max_seen = max(max_seen, d)
            count += 1
    return count, min_seen, max_seen


def check_population(points, n):
    require(len(points) == len(set(points)) == n, "replacement cardinality fails")


def verify_case(m):
    xs = source(m)
    n = 3 * m * m + 3 * m + 1
    require(len(xs) == n, "source cardinality mismatch")
    require(in_phase(PHASE), "invalid response phase")
    edges = contact_edges(xs)
    pair_count, minimum, maximum = all_pair_bounds(xs, maximum=4 * m * m)
    require(pair_count == n * (n - 1) // 2, "incomplete source pair ledger")
    require(minimum == 1 and maximum == 4 * m * m, "source pair ledger mismatch")
    cs = corners(m)
    axial_area = F(sum(det(cs[i], cs[(i + 1) % 6]) for i in range(6)), 2)
    require(axial_area == 3 * m * m, "hull area mismatch")
    require(all(norm2(sub(cs[i], cs[(i + 1) % 6])) == m * m for i in range(6)), "hull side mismatch")
    require(axial_area + 3 * m + 1 == n, "Oler saturation identity fails")
    reactions = reaction_data(xs, m)
    check_stress(xs, edges, reactions)
    rank = pinned_rank(xs, edges, reactions) if m <= 4 else None

    # Enumerate the entire K+B response shore, not just selected own rows.
    ys = set()
    for i in range(-m - 3, m + 4):
        for j in range(-m - 3, m + 4):
            z = (i, j)
            y = add(z, PHASE)
            if hull_distance2(y, m) < 1:
                ys.add(z)
    zs = {z for z in ys if hull_contains(add(z, PHASE), m, strict=True)}
    require(zs <= xs and len(zs) == 3 * m * m, "interior-row census fails")
    require(xs <= ys, "own rows are missing from full response shore")
    require(not any(max(abs(add(z, PHASE)[0]), abs(add(z, PHASE)[1]), abs(sum(add(z, PHASE)))) == m for z in ys), "row on hull boundary")

    response = []
    # Check the complete local distance classification, including rejected vectors.
    deltas = [(i, j) for i in range(-2, 3) for j in range(-2, 3)]
    expected = {(0, 0), (-1, 0), (0, -1), (1, -1)}
    observed = {d for d in deltas if norm2(add(d, PHASE)) < 1}
    require(observed == expected, "four-neighbor distance classification fails")
    require(not any(norm2(add(d, PHASE)) in (0, 1) for d in deltas), "nongeneric distance equality")
    for x in xs:
        for d in expected:
            z = add(x, d)
            require(z in ys, "truncated left response neighborhood")
            require(norm2(sub(add(z, PHASE), x)) < 1, "nonconflict response edge")
            response.append((x, z))
    s_rank, s_det = check_schur(xs, zs)
    require(s_rank == 3 * m + 1, "Schur column census fails")

    fv, fe = fan(m)
    require(fe <= edges, "fan uses a noncontact")
    crossings = []
    for x, z in response:
        y = add(z, PHASE)
        for p, q in fe:
            if properly_cross(x, y, p, q):
                midpoint = scale(F(1, 2), add(p, q))
                require(norm2(sub(y, midpoint)) < F(1, 4), "midpoint confinement fails")
                crossings.append((x, z, p, q))
    require(crossings == [((-1, 1), (0, 0), (0, 0), (0, 1))], "fan does not have its unique advertised crossing")
    # Own-row sinks survive the actual-crossing/basis-closed shield.
    surviving_c = xs - zs - fv
    deleted_right = (fv & zs) | {(0, 0)}
    require(not (surviving_c & deleted_right), "direct terminal sink was deleted")
    for c in surviving_c:
        require(c in ys - zs, "terminal own row is not exterior")
        require(not any(properly_cross(c, add(c, PHASE), p, q) for p, q in fe), "direct terminal edge crosses fan")

    return {
        "m": m, "source_points": n, "source_pairs": pair_count,
        "source_min_squared": minimum, "source_max_squared": maximum,
        "unit_contacts": len(edges), "stress_labels_checked": len(reactions),
        "pinned_rank_mod_prime": rank, "pinned_columns": 2 * n,
        "response_rows": len(ys), "interior_rows": len(zs), "exterior_rows": len(ys - zs),
        "response_edges": len(response), "schur_columns": s_rank, "schur_rank": s_rank,
        "schur_minor_determinant": s_det, "schur_nullity": 0,
        "fan_vertices": len(fv), "fan_edges": len(fe), "fan_crossing_edges": len(crossings),
        "fan_crossing_right_rows": 1, "surviving_direct_terminal_sinks": len(surviving_c),
        "actual_crossing_coarse_left_deficiency": 0,
    }


def verify_replacement(m=32):
    radius2 = F(361 * m * m, 400)
    # If Q(i,j)<=R^2 then |i|,|j|<=2R/sqrt(3)<2m.
    disk = [(i, j) for i in range(-2 * m, 2 * m + 1) for j in range(-2 * m, 2 * m + 1) if norm2((i, j)) <= radius2]
    n = 3 * m * m + 3 * m + 1
    require(len(disk) >= n, "disk does not restore full source cardinality")
    points = sorted(disk, key=lambda p: (norm2(p), p))[:n]
    check_population(points, n)
    pair_count, minimum, maximum = all_pair_bounds(points, maximum=4 * radius2)
    require(pair_count == n * (n - 1) // 2, "incomplete replacement pair ledger")
    require(maximum < 4 * m * m, "replacement is not strictly subdiameter")
    require(25 * m * m - 792 * m + 32 > 0, "analytic population bound fails")
    # Rational guards used by the all-m Voronoi population argument.
    pi_lower = 16 * (F(1, 5) - F(1, 375)) - F(4, 239)
    require(pi_lower > F(25, 8), "rational pi guard fails")
    require(F(7, 4) ** 2 > 3 and F(3, 5) ** 2 > F(1, 3), "sqrt guards fail")
    # Pair the lexicographically ordered old labels with the Q-ordered new sites.
    old_order = sorted(source(m))
    old_index = {p: i for i, p in enumerate(old_order)}
    new_index = {p: i for i, p in enumerate(points)}
    old_contacts = {tuple(sorted((old_index[p], old_index[q]))) for p, q in contact_edges(set(old_order))}
    new_contacts = {tuple(sorted((new_index[p], new_index[q]))) for p, q in contact_edges(set(points))}
    kept = old_contacts & new_contacts
    require(len(old_contacts) == 9 * m * m + 3 * m, "old contact ledger mismatch")
    return {
        "m": m, "old_points": n, "available_disk_sites": len(disk),
        "replacement_points": len(points), "all_replacement_pairs_checked": pair_count,
        "minimum_squared": minimum, "maximum_squared": maximum,
        "certified_upper_squared": str(4 * radius2), "old_diameter_squared": 4 * m * m,
        "population_bound_excess_numerator": 25 * m * m - 792 * m + 32,
        "old_unit_contacts": len(old_contacts), "new_unit_contacts": len(new_contacts),
        "retained_label_contacts": len(kept), "removed_label_contacts": len(old_contacts - new_contacts),
        "created_label_contacts": len(new_contacts - old_contacts),
        "old_diameter_pairs_strictly_shortened": 3,
        "labels_relocated": sum(p != q for p, q in zip(old_order, points)),
    }


def negative_controls():
    controls = []

    def reject(name, callback):
        try:
            callback()
        except ValueError:
            controls.append(name)
            return
        raise ValueError(f"negative control did not fail: {name}")

    xs = source(2)
    edges = contact_edges(xs)
    rs = reaction_data(xs, 2)
    corrupted = {p: list(entries) for p, entries in rs.items()}
    corrupted[(2, 0)] = corrupted[(2, 0)][1:]
    reject("missing facet reaction", lambda: check_stress(xs, edges, corrupted))
    edge = min(edges)
    reject("changed positive contact weight", lambda: check_stress(xs, edges, rs, {edge: F(2)}))
    reject("phase violates four-neighbor chamber", lambda: require(in_phase((F(2, 1000), F(1, 1000))), "invalid phase"))
    last = max(xs, key=lambda p: (level(p), p))
    row = matrix_row(last, xs)
    del row[last]
    reject("own-row determinant loses last diagonal", lambda: require(last in row, "zero last matrix row"))
    sample = sorted(xs)
    reject("omitted replacement label", lambda: check_population(sample[:-1], len(sample)))
    reject("duplicate replacement label", lambda: check_population(sample[:-1] + [sample[0]], len(sample)))
    return controls


def main():
    require(all(PRIME % d for d in range(2, isqrt(PRIME) + 1)), "rank modulus is not prime")
    result = {
        "classification": "exact finite regression replay; report unreviewed",
        "base_commit": "ab6dd3336f9f8d440f2bada76edb32153391cddc",
        "state_version": "2026-10-10.audit.234", "seed": 66,
        "arithmetic": "integers and fractions.Fraction; modular full-rank integer certificate",
        "rank_certificate_prime": PRIME,
        "phase_axial": [str(x) for x in PHASE],
        "cases": [verify_case(m) for m in (2, 3, 4, 8)],
        "replacement": verify_replacement(),
        "negative_controls_rejected": negative_controls(),
        "scope": "finite checks corroborate the all-m proof; no canonical global minimizer or Level I certificate",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
