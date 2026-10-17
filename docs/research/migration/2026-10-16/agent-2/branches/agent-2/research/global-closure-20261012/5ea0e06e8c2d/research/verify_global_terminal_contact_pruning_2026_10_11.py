#!/usr/bin/env python3
"""Exact rational pruning fixtures; no global-optimality or Level I oracle."""

from itertools import combinations
import json
import sympy as sp

Q = sp.Rational


def sub(p, q):
    return tuple(a - b for a, b in zip(p, q))


def norm2(p):
    return sum(a * a for a in p)


def ledger(points):
    return {(i, j): norm2(sub(points[i], points[j]))
            for i, j in combinations(range(len(points)), 2)}


def triangle_free(size, contacts):
    return not any(all(tuple(sorted(edge)) in contacts
                       for edge in combinations(triple, 2))
                   for triple in combinations(range(size), 3))


def rigidity(points, contacts, pins):
    rows = []
    for i, j in sorted(contacts):
        r, row = sub(points[i], points[j]), [Q(0)] * (2 * len(points))
        for a in range(2):
            row[2 * i + a], row[2 * j + a] = r[a], -r[a]
        rows.append(row)
    for i in sorted(pins):
        for a in range(2):
            row = [Q(0)] * (2 * len(points))
            row[2 * i + a] = Q(1)
            rows.append(row)
    return sp.Matrix(rows) if rows else sp.zeros(0, 2 * len(points))


def generic_velocity(points, contacts, pins):
    basis = rigidity(points, contacts, pins).nullspace()
    frozen = {edge for edge in contacts
              if all(all(v[2 * edge[0] + a] == v[2 * edge[1] + a]
                         for a in range(2)) for v in basis)}
    moving = contacts - frozen
    if not moving:
        return None, frozen
    # Each forbidden relative-velocity map is a nonzero polynomial on this
    # moment curve. Their union has at most (dim-1)*|moving| integer roots.
    for x in range(1, (len(basis) - 1) * len(moving) + 2):
        candidate = sp.zeros(2 * len(points), 1)
        for k, vector in enumerate(basis):
            candidate += x ** k * vector
        if all(any(candidate[2 * i + a] != candidate[2 * j + a]
                   for a in range(2)) for i, j in moving):
            candidate /= 1 + max(abs(value) for value in candidate)
            velocities = [tuple(candidate[2 * i + a] for a in range(2))
                          for i in range(len(points))]
            assert all(velocities[i] == (0, 0) for i in pins)
            for i, j in contacts:
                assert sum(a * b for a, b in zip(sub(points[i], points[j]),
                                                sub(velocities[i], velocities[j]))) == 0
            return velocities, frozen
    raise AssertionError("generic-vector root-count bound failed")


def interval_lower_margins(points, velocities, old, new, contacts, t):
    for (i, j), initial in old.items():
        r, dv = sub(points[i], points[j]), sub(velocities[i], velocities[j])
        b, c = sum(a * z for a, z in zip(r, dv)), norm2(dv)
        minimum = min(initial, new[i, j])
        if c > 0 and 0 < -b / c < t:
            minimum = min(minimum, initial - b * b / c)
        if minimum < 1 or ((i, j) not in contacts and minimum == 1):
            return False
    # Upper squared-distance polynomials are convex, so their interval maxima
    # are already covered by the old and new endpoint checks.
    return True


def prune(points):
    initial = ledger(points)
    d2 = max(initial.values())
    diameters = {edge for edge, length in initial.items() if length == d2}
    pins = {i for edge in diameters for i in edge}
    history, initial_contacts = [], {e for e, length in initial.items() if length == 1}
    assert min(initial.values()) >= 1 and triangle_free(len(points), initial_contacts)
    original = points[:]
    for _ in range(len(initial_contacts) + 1):
        old = ledger(points)
        contacts = {e for e, length in old.items() if length == 1}
        velocities, frozen = generic_velocity(points, contacts, pins)
        if velocities is None:
            return points, original, pins, diameters, d2, history
        t, halvings = Q(1, 1000), 0
        while True:
            moved = [tuple(p[a] + t * v[a] for a in range(2))
                     for p, v in zip(points, velocities)]
            new = ledger(moved)
            if (min(new.values()) >= 1 and max(new.values()) == d2
                    and {e for e, length in new.items() if length == d2} == diameters
                    and {e for e, length in new.items() if length == 1} == frozen
                    and interval_lower_margins(points, velocities, old, new,
                                               contacts, t)):
                break
            t /= 2
            halvings += 1
            assert halvings < 4096, "finite-margin search exceeded fixture limit"
        assert len(set(moved)) == len(original)
        assert all(moved[i] == original[i] for i in pins)
        assert triangle_free(len(points), frozen)
        for i, j in contacts:
            assert new[i, j] == 1 + t * t * norm2(sub(velocities[i], velocities[j]))
        history.append({"contacts_before": len(contacts), "contacts_after": len(frozen),
                        "pairs_checked": len(new), "margin_halvings": halvings,
                        "whole_interval_certified": True})
        points = moved
    raise AssertionError("contact pruning exceeded its finite edge-count bound")


def terminal_rank_checks(points, original, pins):
    values = ledger(points)
    contacts = {e for e, length in values.items() if length == 1}
    neighbors = [set() for _ in points]
    for i, j in contacts:
        neighbors[i].add(j)
        neighbors[j].add(i)
    pending, summaries = set(range(len(points))), []
    while pending:
        root, component, stack = min(pending), set(), [min(pending)]
        while stack:
            i = stack.pop()
            if i in component:
                continue
            component.add(i)
            stack.extend(neighbors[i] - component)
        pending -= component
        if len(component) == 1:
            continue
        assert component & pins
        assert all(points[i] == original[i] for i in component)
        edges = {e for e in contacts if set(e) <= component}
        free = sorted(component - pins)
        cols = [2 * i + a for i in free for a in range(2)]
        rank = rigidity(points, edges, set()).extract(range(len(edges)), cols).rank()
        assert rank == 2 * len(free)
        distances = []
        for i in component:
            found, frontier, depth = {i}, {i}, 0
            while frontier:
                next_frontier = set().union(*(neighbors[j] for j in frontier)) - found
                if next_frontier:
                    depth += 1
                    found |= next_frontier
                frontier = next_frontier
            assert found == component
            distances.append(depth)
        d, s, q = max(distances), len(component), len(component & pins)
        e_pp = sum(set(edge) <= pins for edge in edges)
        assert len(edges) <= 2 * s - d - 2
        assert 2 * q >= d + 2 + e_pp
        summaries.append({"vertices": s, "pins": q, "graph_diameter": d,
                          "edges": len(edges), "pin_pin_edges": e_pp,
                          "moving_column_rank": rank})
    return summaries


def equilibrium_matrix(points, contacts, diameters):
    columns = []
    for edges, sign in ((sorted(contacts), 1), (sorted(diameters), -1)):
        for i, j in edges:
            r, col = sub(points[i], points[j]), [Q(0)] * (2 * len(points))
            for a in range(2):
                col[2 * i + a], col[2 * j + a] = sign * r[a], -sign * r[a]
            columns.append(sp.Matrix(col))
    return sp.Matrix.hstack(*columns)


def check_kkt(points, width, height):
    values = ledger(points)
    contacts = {e for e, length in values.items() if length == 1}
    d2 = max(values.values())
    diameters = {e for e, length in values.items() if length == d2}
    alpha = {}
    for edge in contacts:
        p, q = (points[i] for i in edge)
        if p[0] == q[0] and p[0] in (0, width):
            alpha[edge] = height / 2
        elif p[1] == q[1] and p[1] in (0, height):
            alpha[edge] = width / 2
    beta = dict.fromkeys(diameters, Q(1, 2))
    weights = [alpha.get(e, Q(0)) for e in sorted(contacts)] + [beta[e] for e in sorted(diameters)]
    assert sum(alpha.values()) == d2 and sum(beta.values()) == 1
    assert equilibrium_matrix(points, contacts, diameters) * sp.Matrix(weights) == sp.zeros(2 * len(points), 1)


def check_fixture(name, points, expected_rounds, contraction_mode, perimeter=None):
    if perimeter is not None:
        check_kkt(points, *(Q(x) for x in perimeter))
    final, original, pins, diameters, d2, history = prune(points)
    assert len(history) == expected_rounds
    summaries = terminal_rank_checks(final, original, pins)
    values = ledger(final)
    if contraction_mode == "uniform":
        m = min(values.values())
        assert m > 1
        scale = 1 - (m - 1) / (4 * m)
        result = ledger([tuple(scale * x for x in p) for p in final])
        assert min(result.values()) > 1 and max(result.values()) < d2
    elif contraction_mode == "vertical":
        delta = Q(1, 1000)
        while True:
            result = ledger([(p[0], (1 - delta) * p[1]) for p in final])
            if min(result.values()) >= 1 and max(result.values()) < d2:
                break
            delta /= 2
    elif contraction_mode == "independent_triangular":
        contacts = {e for e, length in values.items() if length == 1}
        matrix = equilibrium_matrix(final, contacts, diameters)
        assert matrix.rank() == matrix.cols
        packet = [(0, 0), (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1)]
        distances = [a * a + a * b + b * b
                     for i, j in combinations(range(6), 2)
                     for a, b in [sub(packet[i], packet[j])]]
        assert min(distances) == 1 and max(distances) == 4 < d2
    else:
        assert name == "unit_square_control" and final == original
    return {"name": name, "labels_retained": len(final), "pairs_each_round": len(values),
            "diameter_pairs_fixed": len(diameters), "rounds": history,
            "terminal_components": summaries,
            "strict_competitor_certified": contraction_mode != "control"}


def main():
    fixtures = []
    for m, k, name, rounds, mode in ((2, 2, "unit_square_control", 0, "control"),
                                   (2, 3, "two_round_product", 2, "vertical")):
        points = [(Q(a), Q(b)) for a in range(m) for b in range(k)]
        fixtures.append(check_fixture(name, points, rounds, mode, (m - 1, k - 1)))
    hexagon = [(Q(0), Q(0)), (Q(1), Q(0)), (Q(25, 17), Q(15, 17)),
               (Q(1), Q(30, 17)), (Q(0), Q(30, 17)), (Q(-8, 17), Q(15, 17))]
    fixtures.append(check_fixture("three_direction_rigid_nonoptimal_hexagon", hexagon,
                                  0, "independent_triangular"))
    points = [(Q(a), Q(b)) for a in range(7) for b in range(7)
              if not (2 <= a <= 4 and 2 <= b <= 4)]
    points.extend([(Q(25, 13), Q(44, 13)), (Q(22, 7), Q(34, 11))])
    initial = ledger(points)
    contacts = {e for e, length in initial.items() if length == 1}
    assert sum(all(i not in edge for edge in contacts) for i in range(len(points))) == 1
    directions = set()
    for i, j in contacts:
        r = sub(points[i], points[j])
        directions.add(r if r[0] > 0 or (r[0] == 0 and r[1] > 0)
                       else tuple(-x for x in r))
    assert len(directions) == 3
    fixtures.append(check_fixture("three_directions_hole_and_isolate", points,
                                  1, "uniform", (6, 6)))
    print(json.dumps({"status": "PASS", "arithmetic": "exact SymPy rational",
                      "fixtures": fixtures,
                      "general_pruning_proof_certified_by_finite_output": False,
                      "global_optimality_certified": False,
                      "level_i_resolved": False}, sort_keys=True))


if __name__ == "__main__":
    main()
