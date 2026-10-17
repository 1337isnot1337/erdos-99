#!/usr/bin/env python3
"""Exact full-tube ledger for the seed-63 chamber, independently implemented.

Standard library only; checks remain enabled under -O. See README for the
all-M proof. This executable checks its declared finite domain.
"""
from collections import Counter, deque
from fractions import Fraction as F
import json

PHASE = (F(1, 5), F(1, 7))
OFFSETS = {(0, 0), (-1, 0), (0, -1)}
SIZES = tuple(range(5, 21)) + (24, 32)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def plus(a, b):
    return a[0] + b[0], a[1] + b[1]


def minus(a, b):
    return a[0] - b[0], a[1] - b[1]


def norm2(a):
    return a[0]**2 + a[0]*a[1] + a[1]**2


def segment_distance2(p, a, b):
    d, w = minus(b, a), minus(p, a)
    twice_dot = 2*w[0]*d[0] + 2*w[1]*d[1] + w[0]*d[1] + w[1]*d[0]
    t = max(F(0), min(F(1), F(twice_dot, 2*norm2(d))))
    return norm2((w[0] - t*d[0], w[1] - t*d[1]))


def orientation(a, b, p):
    d, w = minus(b, a), minus(p, a)
    return d[0]*w[1] - d[1]*w[0]


def in_polygon(p, polygon):
    """Independent ray test, including the hull portion of a sector boundary."""
    odd = False
    for a, b in zip(polygon, polygon[1:] + polygon[:1]):
        if orientation(a, b, p) == 0 and all(
            min(a[k], b[k]) <= p[k] <= max(a[k], b[k]) for k in (0, 1)
        ):
            return True
        if (a[1] > p[1]) != (b[1] > p[1]):
            crossing = a[0] + F(p[1]-a[1], b[1]-a[1])*(b[0]-a[0])
            odd ^= p[0] < crossing
    return odd


def local_geometry():
    """Finite local tables, with analytic outside-box exclusion in README."""
    box = [(i, j) for i in range(-3, 4) for j in range(-3, 4)]
    actual = {w for w in box if norm2(plus(w, PHASE)) < 1}
    require(actual == OFFSETS, "three-neighbor phase rule")
    require(all(norm2(plus(w, PHASE)) != 1 for w in box), "cross genericity")
    tables = {
        (1, 0): {(-1, 0), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0)},
        (0, 1): {(-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1)},
        (-1, 1): {(-2, 1), (-1, 0), (-1, 1), (0, -1), (0, 0)},
    }
    for direction, expected in tables.items():
        distances = {w: segment_distance2(plus(w, PHASE), (0, 0), direction)
                     for w in box}
        require(all(d != 1 for d in distances.values()), "tube genericity")
        require({w for w, d in distances.items() if d < 1} == expected,
                f"local tube table {direction}")
    return {str(d): sorted(rows) for d, rows in tables.items()}


def linkage_size(source, shore, basis_by_row, terminals, neighbors):
    """Split-vertex integral flow in the actual alternating digraph."""
    residual = {}

    def arc(a, b):
        residual.setdefault(a, {})[b] = 1
        residual.setdefault(b, {}).setdefault(a, 0)

    def node(side, point, end):
        return side, point, end

    start, finish = ("start",), ("finish",)
    for side, points in (("x", source), ("y", shore)):
        for point in sorted(points):
            arc(node(side, point, 0), node(side, point, 1))
    for x in sorted(terminals):
        arc(start, node("x", x, 0))
    for y in sorted(shore - basis_by_row.keys()):
        arc(node("y", y, 1), finish)
    for x in sorted(source):
        for y in sorted(neighbors[x]):
            if basis_by_row.get(y) == x:
                arc(node("y", y, 1), node("x", x, 0))
            else:
                arc(node("x", x, 1), node("y", y, 0))
    value = 0
    while True:
        parent, queue = {start: None}, deque([start])
        while queue and finish not in parent:
            a = queue.popleft()
            for b, capacity in residual[a].items():
                if capacity and b not in parent:
                    parent[b] = a
                    queue.append(b)
        if finish not in parent:
            return value
        b = finish
        while parent[b] is not None:
            a = parent[b]
            residual[a][b] -= 1
            residual[b][a] += 1
            b = a
        value += 1


def ledger(m, basis_kind):
    require(basis_kind in {"predecessor", "relaxed-optimum"}, "known basis class")
    source = {(i, j) for i in range(m+1) for j in range(m+1-i)}
    neighbors = {x: {plus(x, d) for d in OFFSETS} for x in source}
    shore = set().union(*neighbors.values())
    interior = {x for x in source if sum(x) < m}
    exterior = shore - interior
    corners, collar = [(0, 0), (m, 0), (0, m)], set()
    for i in range(-2, m+3):
        for j in range(-2, m+3):
            p = plus((i, j), PHASE)
            distance = (F(0) if p[0] >= 0 and p[1] >= 0 and sum(p) <= m else
                        min(segment_distance2(p, a, b) for a, b in
                            zip(corners, corners[1:] + corners[:1])))
            require(distance != 1, "outer collar genericity")
            if distance < 1:
                collar.add((i, j))
    require(collar == shore, f"complete convex collar M={m}")

    a, b, c = (1, 1), (2, 1), (1, 2)
    edges = [(a, b), (b, c), (c, a), ((0, 1), a), ((2, 0), b)]
    edges += [((1, j), (1, j+1)) for j in range(2, m-1)]
    fan = {x for edge in edges for x in edge}
    require(len(edges) == len(fan) == m+2, "unicyclic fan size")
    require(all(norm2(minus(x, y)) == 1 for x, y in edges), "unit fan edges")

    basis_by_row = {z: z for z in interior}
    basis_by_row[(0, 1)], basis_by_row[(2, 0)] = (1, 1), (2, 1)
    for j in range(1, m-2):
        basis_by_row[(1, j)] = (1, j+1)
    basis_by_row[(1, m-2)] = (2, m-2)
    for i in range(2, m-1):
        basis_by_row[(i, 1)] = (i+1, 1)
    if basis_kind == "relaxed-optimum":
        basis_by_row = {}
        for i, j in sorted(interior):
            if i == 0 and j >= 1:
                basis_by_row[(i, j)] = (0, j+1)
            elif (j <= 1 and i >= 2) or (j >= 2 and i >= 1):
                basis_by_row[(i, j)] = (i+1, j)
            else:
                basis_by_row[(i, j)] = (i, j)
    basis = set(basis_by_row.values())
    require(len(basis) == len(interior), "injective basis")
    require(all(z in neighbors[x] for z, x in basis_by_row.items()), "basis edges")
    terminals = source - basis
    # Section 102 defines depth by incidence, not distance from the hull.
    deep = {x for x in source if neighbors[x] <= interior}
    expected_deep = {x for x in source if min(x) >= 1 and sum(x) <= m-1}
    require(deep == expected_deep, "Section-102 deep-column identity")
    require(all(x in interior and x in neighbors[x] for x in deep),
            "identity matching makes the whole deep restriction independent")
    missing_deep = deep - basis
    canonical_admissible = not missing_deep
    geometric_deep = {x for x in source if F(3, 4)*min(x[0], x[1], m-sum(x))**2 > 1}
    require(geometric_deep <= basis, "historical geometric predicate")
    if basis_kind == "predecessor":
        require(canonical_admissible, "Section-102 admissible predecessor")
        require(terminals & fan == {(0, 1), (2, 0), (1, m-1)}, "fan terminals")
    else:
        require(not canonical_admissible, "control: reject the relaxed basis")
        require(missing_deep == {(2, 1)} | {(1, j) for j in range(2, m-1)},
                "exact omitted Section-102 deep columns")
        require(len(missing_deep) == m-2, "omitted deep-column count")
        if m == 5:
            require(missing_deep == {(1, 2), (1, 3), (2, 1)} and not geometric_deep,
                    "M=5 counterexample to the historical admissibility predicate")
        require(terminals == fan - {a}, "relaxed basis puts all terminals on fan")

    tube = {y for y in shore if
            min(segment_distance2(plus(y, PHASE), x, z) for x, z in edges) < 1}
    tz, to = tube & interior, tube & exterior
    expected_tz = ({(0, j) for j in range(m)} |
                   {(1, j) for j in range(m-1)} | {(2, 0), (2, 1)})
    require(tz == expected_tz, "exact interior tube rows")
    require(to == {(-1, 1), (2, -1), (1, m-1)}, "exact exterior tube rows")
    removed = fan | {basis_by_row[z] for z in tz}
    surviving = source - removed
    polygons = [
        [(0, 1), (0, 0), (2, 0), b, a],
        [(2, 0), (m, 0), (1, m-1), c, b],
        [(1, m-1), (0, m), (0, 1), a, c], [a, b, c],
    ]

    def sector(x):
        found = [i for i, polygon in enumerate(polygons) if in_polygon(x, polygon)]
        require(len(found) == 1, f"unique geometric sector for {x}")
        return found[0]

    ci = Counter(sector(x) for x in terminals - removed)
    bi = Counter(sector(x) for x in basis - removed)
    zi = Counter(sector(plus(z, PHASE)) for z in interior - tube)
    require(bi == zi, "basis closure balances every sector")
    oi, isolated = [set() for _ in polygons], set()
    for o in exterior - tube:
        sectors = {sector(x) for x in surviving if o in neighbors[x]}
        require(len(sectors) <= 1, "no shared surviving sink")
        if sectors:
            oi[next(iter(sectors))].add(o)
        else:
            isolated.add(o)
    expected_bc = {(i, -1) for i in range(3, m+1)}
    expected_bc |= {(i, m-i) for i in range(3, m+1)}
    expected_iso = {(-1, j) for j in range(m) if j != 1}
    expected_iso |= {(0, -1), (1, -1), (2, m-2)}
    expected_ca = {(-1, m), (0, m)}
    expected_ci = [0, m-3, 1, 0]
    if basis_kind == "relaxed-optimum":
        expected_bc.remove((3, -1))
        expected_iso |= expected_ca | {(3, -1)}
        expected_ca = set()
        expected_ci = [0, 0, 0, 0]
    require(oi == [set(), expected_bc, expected_ca, set()], "sector sink sets")
    require(isolated == expected_iso, "complete isolated sink set")
    require([ci[i] for i in range(4)] == expected_ci, "sector terminals")
    require(exterior == to | isolated | set().union(*oi), "complete exterior partition")
    require(len(exterior) == len(to) + len(isolated) + sum(map(len, oi)),
            "disjoint exterior partition")
    xi = len(isolated) + sum(max(0, len(oi[i])-ci[i]) for i in range(4))
    bound = xi - len(tz)
    flow = linkage_size(source, shore, basis_by_row, terminals, neighbors)
    require(flow == len(terminals) == m+1, "full generic Schur column rank")
    actual_h = len(exterior) - flow
    require(actual_h == 2*m+2, "exact right deficiency")
    if basis_kind == "predecessor":
        require(xi == 2*m+2 and bound == 1, "predecessor cut value")
        require(all(len(oi[i]) >= ci[i] for i in range(4)),
                "each surviving boundary terminal has a sector sink")
        require(bound == len(terminals & fan)-2 <= 1,
                "Section-102 admissible upper bound is attained")
    else:
        require(xi == 3*m and bound == m-1, "relaxed optimal cut value")
    require(bound <= len(exterior)-len(tube) == m-1, "basis-independent upper bound")
    require([bi[i] for i in range(4)] == [0, (m*m-3*m-2)//2, 0, 0],
            "complete sector basis counts")

    # Intentionally incomplete ledgers, rejected by independent checks.
    unclosed_bi = Counter(sector(x) for x in basis - fan)
    imbalance = [unclosed_bi[i]-zi[i] for i in range(4)]
    require(any(imbalance), "control: missing basis closure must fail")
    direct_only = interior | {x for x in source if sum(x) == m}
    omitted = collar - direct_only
    require(len(omitted) == 2*m+2, "control: direct sinks omit two full strips")
    return {
        "M": m, "basis": basis_kind, "source_labels": len(source), "Z": len(interior),
        "O": len(exterior), "fan_vertices": len(fan), "T_Z": len(tz),
        "T_O": len(to), "C_i": [ci[i] for i in range(4)], "O_i": list(map(len, oi)),
        "O_iso": len(isolated), "Xi": xi, "certified_h_lower_bound": bound,
        "section102_admissible": canonical_admissible,
        "deep_columns": len(deep), "omitted_deep_columns": sorted(missing_deep),
        "boundary_terminals": len(terminals-deep),
        "canonical_admissible_cut_optimum": 1,
        "B_i": [bi[i] for i in range(4)], "Z_i": [zi[i] for i in range(4)],
        "X_i": [bi[i]+ci[i] for i in range(4)],
        "basis_independent_cut_upper_bound": len(exterior)-len(tube),
        "generic_rank_full_schur": flow, "actual_h": actual_h, "bound_slack": actual_h-bound,
        "canonical_boundary_schur": canonical_admissible,
        "controls": {"unclosed_sector_B_minus_Z": imbalance,
                     "direct_sink_only_missing_rows": len(omitted)},
    }


def main():
    tables = local_geometry()
    rows = [ledger(m, kind) for m in SIZES for kind in ("predecessor", "relaxed-optimum")]
    result = {
        "result": "PASS", "counts": {"ledgers": len(rows), "ledger_failure_controls": 2*len(rows),
                                       "admissibility_failure_controls": len(SIZES)},
        "classification": "exact finite evidence; unreviewed all-M proof in README",
        "phase": [str(x) for x in PHASE], "finite_sizes": list(SIZES),
        "sector_order": ["AB", "BC", "CA", "triangle"],
        "local_unit_edge_tube_tables": tables, "ledgers": rows,
        "canonical_global_source": False, "canonical_j_star_supplied": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


# Standalone replay entrypoint; this file is never imported as a library.
main()
