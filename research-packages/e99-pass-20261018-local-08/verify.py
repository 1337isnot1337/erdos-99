#!/usr/bin/env python3
"""Exact full-pair and stress checks for the supplied-W restoration fixture."""

from fractions import Fraction as F
from itertools import combinations
import json


def require(condition):
    if not condition:
        raise AssertionError("exact stress-deletion restoration check failed")


def point(x, y):
    return (F(x), F(y))


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def dist2(a, b):
    d = sub(a, b)
    return d[0] * d[0] + d[1] * d[1]


def pair_table(order, coords):
    return {
        f"{i}-{j}": dist2(coords[i], coords[j])
        for i, j in combinations(order, 2)
    }


def graph_edges(table, value):
    return [pair for pair, d2 in table.items() if d2 == value]


def rank(rows):
    matrix = [[F(x) for x in row] for row in rows]
    if not matrix:
        return 0
    columns = len(matrix[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (r for r in range(pivot_row, len(matrix)) if matrix[r][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [x / scale for x in matrix[pivot_row]]
        for r in range(len(matrix)):
            if r == pivot_row:
                continue
            scale = matrix[r][column]
            matrix[r] = [x - scale * y for x, y in zip(matrix[r], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def force_balance(order, coords, lower, upper):
    forces = {i: [F(0), F(0)] for i in order}
    for (i, j), weight in upper.items():
        delta = sub(coords[i], coords[j])
        for axis in range(2):
            forces[i][axis] += weight * delta[axis]
            forces[j][axis] -= weight * delta[axis]
    for (i, j), weight in lower.items():
        delta = sub(coords[i], coords[j])
        for axis in range(2):
            forces[i][axis] -= weight * delta[axis]
            forces[j][axis] += weight * delta[axis]
    return forces


def triangle_count(edges):
    adjacency = {}
    for edge in edges:
        i, j = edge.split("-")
        adjacency.setdefault(i, set()).add(j)
        adjacency.setdefault(j, set()).add(i)
    vertices = sorted(adjacency)
    return sum(
        1
        for i, j, k in combinations(vertices, 3)
        if j in adjacency.get(i, ())
        and k in adjacency.get(i, ())
        and k in adjacency.get(j, ())
    )


def contact_isolates(order, edges):
    incident = set()
    for edge in edges:
        incident.update(edge.split("-"))
    return [label for label in order if label not in incident]


def check_source():
    source = {f"p{i}": point(i, 0) for i in range(10)}
    source["q"] = point(F(1, 2), F(11, 10))
    source_order = [f"p{i}" for i in range(10)] + ["q"]
    source_pairs = pair_table(source_order, source)
    expected_source_pairs = {
        f"p{i}-p{j}": F((j - i) ** 2)
        for i, j in combinations(range(10), 2)
    }
    expected_source_pairs.update(
        {
            f"p{i}-q": (F(i) - F(1, 2)) ** 2 + F(121, 100)
            for i in range(10)
        }
    )
    require(source_pairs == expected_source_pairs)
    old_d2 = max(source_pairs.values())
    old_contacts = graph_edges(source_pairs, F(1))
    old_diameters = graph_edges(source_pairs, old_d2)
    expected_contacts = [f"p{i}-p{i + 1}" for i in range(9)]
    require(old_d2 == 81)
    require(old_contacts == expected_contacts)
    require(old_diameters == ["p0-p9"])
    require(triangle_count(old_contacts) == 0)
    require(all(F(1) <= d2 <= old_d2 for d2 in source_pairs.values()))
    require(contact_isolates(source_order, old_contacts) == ["q"])
    require(all(source_pairs[f"p{i}-q"] not in (F(1), old_d2) for i in range(10)))

    # Unknowns are nine contact weights followed by beta_09. The equilibrium
    # matrix has rank 9; adding beta_09=1 has rank 10, so s_Z=0.
    equilibrium = []
    first = [0] * 10
    first[0], first[9] = 1, -9
    equilibrium.append(first)
    for i in range(1, 9):
        row = [0] * 10
        row[i - 1], row[i] = -1, 1
        equilibrium.append(row)
    last = [0] * 10
    last[8], last[9] = -1, 9
    equilibrium.append(last)
    require(rank(equilibrium) == 9)
    normalization = [0] * 10
    normalization[9] = 1
    require(rank(equilibrium + [normalization]) == 10)
    lower = {(f"p{i}", f"p{i + 1}"): F(9) for i in range(9)}
    upper = {("p0", "p9"): F(1)}
    require(sum(upper.values()) == 1)
    require(force_balance(source_order, source, lower, upper) == {
        label: [F(0), F(0)] for label in source_order
    })

    # W={p0} subset B={p0,p9}; R={p0} has size s_Z+1 and kills the only
    # old-D row. This is a finite stress-row fixture, not a global minimizer.
    W, B, R = {"p0"}, {"p0", "p9"}, {"p0"}
    require(W and W <= B and R <= W and len(R) == 1)
    deleted_order = [f"p{i}" for i in range(1, 10)] + ["q"]
    deleted_pairs = pair_table(deleted_order, source)
    expected_deleted_pairs = {
        f"p{i}-p{j}": F((j - i) ** 2)
        for i, j in combinations(range(1, 10), 2)
    }
    expected_deleted_pairs.update(
        {
            f"p{i}-q": (F(i) - F(1, 2)) ** 2 + F(121, 100)
            for i in range(1, 10)
        }
    )
    require(deleted_pairs == expected_deleted_pairs)
    require(all(F(1) <= d2 < old_d2 for d2 in deleted_pairs.values()))
    require(graph_edges(deleted_pairs, old_d2) == [])
    deleted_contacts = graph_edges(deleted_pairs, F(1))
    require(deleted_contacts == [f"p{i}-p{i + 1}" for i in range(1, 9)])
    require(contact_isolates(deleted_order, deleted_contacts) == ["q"])

    # Velocities (i,0) for p_i, i=1,...,9, open every retained contact.
    # The retained old-D row set is empty, so no first-order upper condition remains.
    for i in range(1, 9):
        edge = sub(source[f"p{i + 1}"], source[f"p{i}"])
        relative_velocity = sub(point(i + 1, 0), point(i, 0))
        derivative = 2 * (edge[0] * relative_velocity[0] + edge[1] * relative_velocity[1])
        require(derivative == 2)

    # Replace p0 by r. Every r-pair with the retained source, including q,
    # lies strictly between squared distances 1 and 81.
    strict_source = dict(source)
    strict_source["r"] = point(F(8, 5), F(11, 10))
    strict_order = [f"p{i}" for i in range(1, 10)] + ["q", "r"]
    strict_pairs = pair_table(strict_order, strict_source)
    expected_strict_pairs = dict(expected_deleted_pairs)
    expected_strict_pairs.update(
        {
            f"p{i}-r": (F(i) - F(8, 5)) ** 2 + F(121, 100)
            for i in range(1, 10)
        }
    )
    expected_strict_pairs["q-r"] = F(121, 100)
    require(strict_pairs == expected_strict_pairs)
    replacement_pairs = {f"p{i}-r" for i in range(1, 10)} | {"q-r"}
    require(all(F(1) < strict_pairs[pair] < old_d2 for pair in replacement_pairs))
    require(all(F(1) <= d2 < old_d2 for d2 in strict_pairs.values()))
    strict_contacts = graph_edges(strict_pairs, F(1))
    strict_d2 = max(strict_pairs.values())
    strict_diameters = graph_edges(strict_pairs, strict_d2)
    require(strict_contacts == [f"p{i}-p{i + 1}" for i in range(1, 9)])
    strict_isolates = contact_isolates(strict_order, strict_contacts)
    require(strict_isolates == ["q", "r"])
    require(triangle_count(strict_contacts) == 0)
    require(strict_d2 == F(3673, 50) < old_d2)
    require(strict_diameters == ["p9-q"])

    # Weak restoration at p0 itself reintroduces all contacts and p0-p9 at D.
    weak_pairs = pair_table(source_order, source)
    require(weak_pairs == source_pairs)
    require(graph_edges(weak_pairs, F(1)) == old_contacts)
    require(graph_edges(weak_pairs, old_d2) == old_diameters)

    return {
        "source_label_count": len(source_order),
        "source_pair_count": len(source_pairs),
        "source_D_squared": str(old_d2),
        "source_contacts": len(old_contacts),
        "source_actual_D_pairs": old_diameters,
        "contact_isolates_before_deletion": ["q"],
        "stress_each_alpha": "9",
        "stress_beta_09": "1",
        "stress_affine_dimension": 0,
        "supplied_W": ["p0"],
        "stress_deletion_R": ["p0"],
        "deleted_source_pair_count": len(deleted_pairs),
        "deleted_source_actual_old_D_pairs": [],
        "strict_restored_pair_count": len(strict_pairs),
        "strict_restored_contacts": len(strict_contacts),
        "strict_restored_contact_isolates": strict_isolates,
        "old_D_pairs_removed": old_diameters,
        "new_actual_D_prime_pairs": strict_diameters,
        "new_D_prime_squared": f"{strict_d2.numerator}/{strict_d2.denominator}",
        "new_D_prime_strictly_below_old_D": strict_d2 < old_d2,
        "weak_restore_contacts": len(graph_edges(weak_pairs, F(1))),
        "weak_restore_old_D_pairs": graph_edges(weak_pairs, old_d2),
    }


print(json.dumps(check_source(), indent=2, sort_keys=True))
