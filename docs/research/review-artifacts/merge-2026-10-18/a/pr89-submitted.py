#!/usr/bin/env python3
"""Independent exact geometric full-tube ledger; no predecessor imports.

All coordinates are axial. A translated point has integer numerators over D.
The metric is Q(i,j)=i*i+i*j+j*j; determinants preserve planar orientation.
Checks use explicit exceptions, including under optimized Python.
"""
from collections import defaultdict
from fractions import Fraction
from functools import cmp_to_key
import json

D = 1000
PHASES = ((1, 2), (20, 40), (10, 80))
DIRECTIONS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def require(value, message):
    if not value:
        raise ValueError(message)


def plus(a, b):
    return a[0] + b[0], a[1] + b[1]


def minus(a, b):
    return a[0] - b[0], a[1] - b[1]


def times(t, a):
    return t * a[0], t * a[1]


def q(a):
    return a[0] * a[0] + a[0] * a[1] + a[1] * a[1]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def dot2(a, b):
    return 2 * a[0] * b[0] + a[0] * b[1] + a[1] * b[0] + 2 * a[1] * b[1]


def translated(z, phase):
    return plus(times(D, z), phase)


def hull_inside_num(p, m, strict=False):
    bound = max(abs(p[0]), abs(p[1]), abs(sum(p)))
    return bound < D * m if strict else bound <= D * m


def near_segment_num(p, a, b):
    """Whether distance(p/D, [a,b]) < 1, with integer operations only."""
    delta = minus(b, a)
    r = minus(p, times(D, a))
    h = dot2(r, delta)
    length2 = q(delta)
    require(length2 > 0, 'zero-length segment')
    if h <= 0:
        return q(r) < D * D
    if h >= 2 * D * length2:
        return q(minus(p, times(D, b))) < D * D
    return 4 * length2 * q(r) - h * h < 4 * length2 * D * D


def hull_corners(m):
    return ((m, 0), (0, m), (-m, m), (-m, 0), (0, -m), (m, -m))


def edge(a, b):
    return tuple(sorted((a, b)))


def fan(m):
    paths = (
        [(i, 0) for i in range(0, -m - 1, -1)],
        [(i, 0) for i in range(1, m + 1)],
        [(-i, 1 + i) for i in range(m)],
    )
    vertices = set()
    edges = set()
    for path in paths:
        require(not vertices.intersection(path), 'spokes are not vertex disjoint')
        vertices.update(path)
        edges.update(edge(a, b) for a, b in zip(path, path[1:]))
    tri = ((0, 0), (1, 0), (0, 1))
    edges.update(edge(tri[k], tri[(k + 1) % 3]) for k in range(3))
    require(len(vertices) == len(edges) == 3 * m + 1, 'fan census')
    require(all(q(minus(a, b)) == 1 for a, b in edges), 'nonunit fan edge')
    return vertices, edges


def direction_order(a, b):
    def half(v):
        return 0 if v[1] > 0 or (v[1] == 0 and v[0] > 0) else 1
    ha, hb = half(a), half(b)
    if ha != hb:
        return ha - hb
    c = cross(a, b)
    return -1 if c > 0 else 1 if c < 0 else 0


def geometric_faces(m, fan_edges):
    """Exact half-edge traversal of the hull plus embedded contact fan."""
    corners = hull_corners(m)
    edges = set(fan_edges)
    for a, b in zip(corners, corners[1:] + corners[:1]):
        direction = ((b[0] - a[0]) // m, (b[1] - a[1]) // m)
        chain = [plus(a, times(k, direction)) for k in range(m + 1)]
        edges.update(edge(p, r) for p, r in zip(chain, chain[1:]))
    adj = defaultdict(list)
    for a, b in sorted(edges):
        adj[a].append(b)
        adj[b].append(a)
    for a in adj:
        adj[a].sort(key=cmp_to_key(lambda b, c: direction_order(minus(b, a), minus(c, a))))
    used = set()
    faces = []
    for a, b in sorted((a, b) for a in adj for b in adj[a]):
        if (a, b) in used:
            continue
        start = (a, b)
        polygon = []
        while (a, b) not in used:
            used.add((a, b))
            polygon.append(a)
            neighbors = adj[b]
            c = neighbors[(neighbors.index(a) - 1) % len(neighbors)]
            a, b = b, c
        require((a, b) == start, 'half-edge face did not close')
        area2 = sum(cross(p, r) for p, r in zip(polygon, polygon[1:] + polygon[:1]))
        if area2 > 0:
            faces.append((area2, polygon))
    require(len(used) == 2 * len(edges), 'missing half edge')
    require(len(faces) == 4, 'fan must have three outer sectors and its triangle face')
    require(sum(area for area, _ in faces) == 6 * m * m, 'face areas do not partition hexagon')
    central = [poly for area, poly in faces if area == 1]
    lower = [poly for _, poly in faces if (0, -m) in poly]
    upper_left = [poly for _, poly in faces if (-m, m) in poly]
    require(len(central) == len(lower) == len(upper_left) == 1, 'face naming')
    upper_right = [poly for _, poly in faces if poly not in central + lower + upper_left]
    require(len(upper_right) == 1, 'fourth face naming')
    return central + upper_left + upper_right + lower


def in_closed_polygon_num(p, polygon):
    winding = 0
    for a0, b0 in zip(polygon, polygon[1:] + polygon[:1]):
        a, b = times(D, a0), times(D, b0)
        c = cross(minus(b, a), minus(p, a))
        if c == 0 and all(min(a[k], b[k]) <= p[k] <= max(a[k], b[k]) for k in (0, 1)):
            return True
        if a[1] <= p[1] < b[1] and c > 0:
            winding += 1
        if b[1] <= p[1] < a[1] and c < 0:
            winding -= 1
    return winding != 0


def sector_of_num(p, faces):
    found = [k for k, poly in enumerate(faces) if in_closed_polygon_num(p, poly)]
    require(len(found) == 1, f'nonunique sector for {p}: {found}')
    return found[0]


def check_phase(phase):
    a, b = phase
    require(0 < a < b and a + b < D // 10, 'phase not in predecessor chamber')
    require(q(phase) < D * min(b - a, 2 * a + b, a + 2 * b), 'phase chamber metric inequality')
    require(q(phase) < D * D // 100, 'phase displacement bound')
    offsets = {(i, j) for i in range(-2, 3) for j in range(-2, 3)
               if q(translated((i, j), phase)) < D * D}
    require(offsets == {(0, 0), (-1, 0), (0, -1), (1, -1)}, 'radial offset classification')
    require(all(q(translated((i, j), phase)) not in (0, D * D)
                for i in range(-2, 3) for j in range(-2, 3)), 'distance equality')
    return offsets


def ledger(m, phase, close_basis=True, drop_exterior_tube=False):
    offsets = check_phase(phase)
    xs = {(i, j) for i in range(-m, m + 1) for j in range(-m, m + 1)
          if max(abs(i), abs(j), abs(i + j)) <= m}
    corners = hull_corners(m)
    hull_edges = list(zip(corners, corners[1:] + corners[:1]))
    ys = set()
    for i in range(-m - 2, m + 3):
        for j in range(-m - 2, m + 3):
            z = (i, j)
            p = translated(z, phase)
            if hull_inside_num(p, m) or any(near_segment_num(p, a, b) for a, b in hull_edges):
                ys.add(z)
    shell = {(i, j) for i in range(-m - 1, m + 2) for j in range(-m - 1, m + 2)
             if max(abs(i), abs(j), abs(i + j)) == m + 1}
    expected_ys = xs | (shell - set(hull_corners(m + 1)))
    expected_ys |= {(-m - 1, 0), (0, -m - 1), (m + 1, -m - 1)}
    require(ys == expected_ys, 'complete collar shell certificate')
    zs = {z for z in ys if hull_inside_num(translated(z, phase), m, strict=True)}
    require(zs == {z for z in xs if -m <= min(z[0], z[1], sum(z))
                   and max(z[0], z[1], sum(z)) <= m - 1}, 'interior integer inequalities')
    os = ys - zs
    require(zs <= xs, 'interior row has no own source label')
    bs = set(zs)
    cs = xs - bs
    require(len(xs) == 3 * m * m + 3 * m + 1 and len(zs) == 3 * m * m, 'source/interior census')
    require(xs <= ys, 'own rows absent from full collar')
    adj = {x: {plus(x, d) for d in offsets} for x in xs}
    require(all(neighbors <= ys for neighbors in adj.values()), 'truncated radial neighborhood')
    if m <= 4:
        exhaustive = {x: {z for z in ys if q(minus(translated(z, phase), times(D, x))) < D * D}
                      for x in xs}
        require(adj == exhaustive, 'all-pair radial replay disagrees')
    # Own-row square minor and its Z-by-B restriction are triangular in i+2j.
    require(all(z == x or z[0] + 2 * z[1] < x[0] + 2 * x[1]
                for x in xs for z in adj[x] & xs), 'nontriangular own-row minor')
    require(all(x in adj[x] for x in xs), 'zero diagonal in own-row minor')
    fv, fe = fan(m)
    require(fv <= xs, 'fan leaves source')
    faces = geometric_faces(m, fe)
    tube = {z for z in ys if any(near_segment_num(translated(z, phase), a, b) for a, b in fe)}
    horizontal = {(i, -1) for i in range(-m, m + 2)}
    horizontal |= {(i, 0) for i in range(-m - 1, m + 1)}
    horizontal |= {(i, 1) for i in range(-m, m)}
    diagonal = {(-j, j) for j in range(-1, m + 1)}
    diagonal |= {(1 - j, j) for j in range(-1, m + 1)}
    diagonal |= {(2 - j, j) for j in range(1, m + 1)}
    require(len(horizontal & diagonal) == 7, 'long tube overlap')
    require(tube == horizontal | diagonal, 'long tube interval certificate')
    if drop_exterior_tube:
        tube &= zs
    tz, to = tube & zs, tube & os
    require(fv & bs <= tz, 'basis fan vertex own row not in tube')
    removed = fv | (tz if close_basis else set())
    surviving = xs - removed
    sector = {x: sector_of_num(times(D, x), faces) for x in surviving}
    ci = [set() for _ in faces]
    bi = [set() for _ in faces]
    zi = [set() for _ in faces]
    oi = [set() for _ in faces]
    for x in surviving:
        (ci if x in cs else bi)[sector[x]].add(x)
    for z in zs - tube:
        zi[sector_of_num(translated(z, phase), faces)].add(z)
    require(all(len(bi[k]) == len(zi[k]) for k in range(4)), 'sector basis balance fails')
    require(all(sector[x] == sector_of_num(translated(x, phase), faces) for x in surviving & bs),
            'basis pair leaves sector')
    for x in surviving:
        for z in (adj[x] & os) - tube:
            oi[sector[x]].add(z)
    require(all(not oi[k] & oi[l] for k in range(4) for l in range(k)), 'exterior sinks shared')
    oiso = os - tube - set().union(*oi)
    require(len(os) == len(to) + len(oiso) + sum(map(len, oi)), 'exterior shore partition')
    require(len(cs) == len(cs & fv) + sum(map(len, ci)), 'terminal partition')
    if not drop_exterior_tube:
        expected_c = [set(), {(-m, m)},
                      {(i, m) for i in range(2 - m, 1)} | {(i, m - i) for i in range(1, m)},
                      {(m, j) for j in range(-m, 0)}]
        expected_o = [set(), {(-m - 1, j) for j in range(2, m + 1)},
                      {(i, m) for i in range(3 - m, 1)} | {(i, m - i) for i in range(1, m - 1)},
                      {(m, j) for j in range(-m, -1)} |
                      {(m + 1, j) for j in range(-m - 1, -1)} |
                      {(i, -m - 1) for i in range(m + 1)} |
                      {(i, -m - 1 - i) for i in range(1 - m, 0)}]
        expected_b = [set(),
                      {(i, j) for j in range(2, m) for i in range(-m, -j)},
                      {(s - j, j) for j in range(2, m) for s in range(3, m)},
                      {(i, -r) for r in range(2, m + 1) for i in range(r - m, m)}]
        require(ci == expected_c, 'terminal interval certificate')
        require(oi == expected_o, 'exterior sink interval certificate')
        require(bi == zi == expected_b, 'surviving basis interval certificate')
    globally_isolated = ys - set().union(*adj.values())
    require(globally_isolated <= oiso, 'globally isolated rows lost')
    expected_isolated = {(i, m + 1) for i in range(-m, 0)}
    expected_isolated |= {(i, m + 1 - i) for i in range(1, m + 1)}
    require(globally_isolated == expected_isolated, 'global isolated-row interval certificate')
    if not drop_exterior_tube:
        require(oiso == expected_isolated | {(-m - 1, 1)}, 'isolated exterior sink certificate')
    p = sum(max(0, len(c) - len(o)) for c, o in zip(ci, oi))
    surplus = sum(max(0, len(o) - len(c)) for c, o in zip(ci, oi))
    rank = len(cs)
    cut_rank = len(tube) + sum(min(len(c), len(o)) for c, o in zip(ci, oi))
    h = len(os) - rank
    bound = len(oiso) + surplus - len(tz)
    require(cut_rank - rank == h - bound >= 0, 'cut slack identity fails')
    require(len(cs & fv) + p - len(tube) == rank - cut_rank, 'left/right dual cut mismatch')
    return {
        'm': m, 'phase_numerators': list(phase), 'phase_denominator': D,
        'source_points': len(xs), 'response_rows': len(ys), 'interior_rows': len(zs),
        'exterior_rows': len(os), 'fan_vertices': len(fv), 'fan_edges': len(fe),
        'tube_interior': len(tz), 'tube_exterior': len(to),
        'removed_basis': len(removed & bs), 'shield_terminals': len(cs & fv),
        'sectors': [{'C': len(c), 'O': len(o), 'B': len(b), 'Z': len(z)}
                    for c, o, b, z in zip(ci, oi, bi, zi)],
        'isolated_exterior_sinks': len(oiso), 'globally_isolated_rows': len(globally_isolated),
        'newly_isolated_rows': len(oiso - globally_isolated), 'positive_terminal_mass': p,
        'positive_sink_mass': surplus, 'Xi': len(oiso) + surplus,
        'right_deficiency_bound': bound, 'schur_rank': rank,
        'true_right_deficiency': h, 'cut_slack': cut_rank - rank,
    }


def primitive_checks():
    """Replay the local proof certificate with a separate Fraction calculation."""
    directions = ((1, 0), (0, 1), (-1, 1))
    expected = (
        {(-1, 0), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (2, -1)},
        {(-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0)},
        {(-2, 1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1)},
    )
    comparisons = 0
    margin = Fraction(1)
    for phase in PHASES:
        for direction, advertised in zip(directions, expected):
            observed = set()
            for i in range(-3, 4):
                for j in range(-3, 4):
                    p = translated((i, j), phase)
                    # Independent scalar projection in rational coordinates.
                    x, y = Fraction(p[0], D), Fraction(p[1], D)
                    u, v = direction
                    t = (x * u + y * v + (x * v + y * u) / 2) / (u * u + u * v + v * v)
                    t = max(Fraction(0), min(Fraction(1), t))
                    rx, ry = x - t * u, y - t * v
                    distance2 = rx * rx + rx * ry + ry * ry
                    margin = min(margin, abs(distance2 - 1))
                    reference = distance2 < 1
                    actual = near_segment_num(p, (0, 0), direction)
                    require(actual == reference, 'integer/Fraction segment metric mismatch')
                    comparisons += 1
                    if actual:
                        observed.add((i, j))
            require(observed == advertised, 'primitive tube offset certificate')
    require(not near_segment_num((-D, 0), (0, 0), (1, 0)), 'unit-distance boundary included')
    require(near_segment_num((1 - D, 0), (0, 0), (1, 0)), 'strictly interior tube point omitted')
    return {'segment_metric_comparisons': comparisons, 'primitive_tubes': 9,
            'sites_per_primitive_tube': 7, 'minimum_squared_distance_margin': str(margin),
            'strict_boundary_control': 'passed'}


def expected_ledger(m):
    return {
        'source_points': 3 * m * m + 3 * m + 1,
        'response_rows': 3 * m * m + 9 * m + 4,
        'interior_rows': 3 * m * m, 'exterior_rows': 9 * m + 4,
        'fan_vertices': 3 * m + 1, 'fan_edges': 3 * m + 1,
        'tube_interior': 9 * m - 8, 'tube_exterior': 9,
        'removed_basis': 9 * m - 8, 'shield_terminals': 2,
        'sectors': [
            {'C': 0, 'O': 0, 'B': 0, 'Z': 0},
            {'C': 1, 'O': m - 1, 'B': (m - 1) * (m - 2) // 2, 'Z': (m - 1) * (m - 2) // 2},
            {'C': 2 * m - 2, 'O': 2 * m - 4, 'B': (m - 2) * (m - 3), 'Z': (m - 2) * (m - 3)},
            {'C': m, 'O': 4 * m - 1, 'B': (3 * m * m - 5 * m + 2) // 2, 'Z': (3 * m * m - 5 * m + 2) // 2},
        ],
        'isolated_exterior_sinks': 2 * m + 1, 'globally_isolated_rows': 2 * m,
        'newly_isolated_rows': 1, 'positive_terminal_mass': 2,
        'positive_sink_mass': 4 * m - 3, 'Xi': 6 * m - 2,
        'right_deficiency_bound': 6 - 3 * m, 'schur_rank': 3 * m + 1,
        'true_right_deficiency': 6 * m + 3, 'cut_slack': 9 * m - 3,
    }


def check_advertised_ledger(case):
    for key, value in expected_ledger(case['m']).items():
        require(case[key] == value, 'advertised ledger differs: ' + key)


def main():
    primitives = primitive_checks()
    cases = [ledger(m, phase) for phase in PHASES for m in range(2, 13)]
    cases.append(ledger(32, PHASES[0]))
    for case in cases:
        check_advertised_ledger(case)
    controls = []
    for case in cases:
        m = case['m']
        if m >= 7:
            # pi<22/7 and sqrt(3)>19/11 bound the Section-175 mean cost.
            require(133 * case['tube_interior'] > 924 * m + 792,
                    'phase must exceed the translation-average upper bound')
    controls.append({'mutation': 'use the translation-average cost as a pointwise cap',
                     'counterexample_m': 7, 'actual_interior_tube': 55,
                     'strict_upper_bound_for_mean_cost': '7260/133',
                     'integer_gap_numerator': 55})
    try:
        ledger(4, PHASES[0], close_basis=False)
    except ValueError as exc:
        require(str(exc) == 'sector basis balance fails', 'wrong basis failure control')
        controls.append({'mutation': 'omit basis closure', 'rejected_by': str(exc)})
    else:
        raise ValueError('basis closure negative control survived')
    # Dropping exterior tube rows can be a different valid cut on this family;
    # it must not silently be reported as the Section-175 full-tube ledger.
    changed = ledger(4, PHASES[0], drop_exterior_tube=True)
    try:
        check_advertised_ledger(changed)
    except ValueError as exc:
        require(str(exc) == 'advertised ledger differs: tube_exterior', 'wrong tube identity failure')
        controls.append({'mutation': 'report an interior-only tube as the full tube',
                         'rejected_by': str(exc)})
    else:
        raise ValueError('tube identity negative control survived')
    result = {'status': 'passed', 'classification': 'unreviewed exact finite evidence',
              'case_count': len(cases), 'cases': cases, 'primitive_checks': primitives,
              'negative_controls': controls}
    print(json.dumps(result, indent=2, sort_keys=True))


# Standalone entry point; no dynamic capability is required by this package.
main()
