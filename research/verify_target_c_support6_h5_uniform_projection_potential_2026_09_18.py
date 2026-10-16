#!/usr/bin/env python3
"""Exact projection-potential exclusion of the six uniform H5 cases.

For a present reciprocal edge ij with sign s_ij, the full signed unit-force
equilibrium implies, for every scalar potential a and projection vector u,

    sum_ij s_ij (a_i-a_j) u.(y_i-y_j)/|y_i-y_j| = 0.

If the directed constraints

    a_i > a_j  iff  s_ij (x_i-x_j) > 0,
    x_i = u.y_i,

are acyclic, a topological ordering supplies a, and every summand is strictly
positive.  This is therefore an exact contradiction.

The six uniform H5 order types are represented below by integer coordinates.
The verifier checks that each coordinate array has exactly the target
chirotope, computes all generic projection orders by the exact critical-ray
sweep, and checks the signed constraint graph for every order.  For a uniform
rank-three order type the allowable generic projection orders are invariant
under realization (the standard dual-line/allowable-sequence fact), so the
integer arrays are finite certificates for the order-type calculation, not
numerical guesses.
"""

from functools import cmp_to_key
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "verify_target_c_support6_h5_metric_normal_form_2026_09_18.py"
spec = spec_from_file_location("h5_metric_normal_form", SOURCE)
metric = module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(metric)
h5 = metric.h5


# Each array is a strict rank-three realization of one canonical uniform
# representative.  The common convex hull is deliberately integer-valued;
# the two interior points distinguish the six chirotopes.
REALIZATIONS = (
    (
        (0, 1000000), (-951057, 309017), (-587785, -809017),
        (587785, -809017), (951057, 309017),
        (-353089, 357654), (-379050, 392197),
    ),
    (
        (0, 1000000), (-951057, 309017), (-587785, -809017),
        (587785, -809017), (951057, 309017),
        (-247804, 330034), (-444768, 368738),
    ),
    (
        (0, 1000000), (-951057, 309017), (-587785, -809017),
        (587785, -809017), (951057, 309017),
        (-363879, 364806), (-527652, 361454),
    ),
    (
        (0, 1000000), (-951057, 309017), (-587785, -809017),
        (587785, -809017), (951057, 309017),
        (-432895, 227430), (-445430, 409636),
    ),
    (
        (0, 1000000), (-951057, 309017), (-587785, -809017),
        (587785, -809017), (951057, 309017),
        (-339486, 243141), (-715979, 344584),
    ),
    (
        (0, 1000000), (-951057, 309017), (-587785, -809017),
        (587785, -809017), (951057, 309017),
        (-481300, -103980), (-563536, 333890),
    ),
)


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def verify_chirotope(points, signs):
    assert len(points) == 7
    values = []
    for sign, (a, b, c) in zip(signs, h5.TRIPLES):
        value = cross(points[a], points[b], points[c])
        assert value != 0
        assert value * sign > 0
        values.append(abs(value))
    return min(values)


def half(v):
    return 0 if v[1] > 0 or (v[1] == 0 and v[0] >= 0) else 1


def ray_compare(a, b):
    ha, hb = half(a), half(b)
    if ha != hb:
        return -1 if ha < hb else 1
    z = a[0] * b[1] - a[1] * b[0]
    if z:
        return -1 if z > 0 else 1
    return 0


def critical_rays(points):
    rays = []
    for i in range(7):
        for j in range(i + 1, 7):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            normal = (-dy, dx)
            assert normal != (0, 0)
            rays.extend((normal, (-normal[0], -normal[1])))
    rays.sort(key=cmp_to_key(ray_compare))
    unique = []
    for ray in rays:
        if not unique or ray_compare(unique[-1], ray) != 0:
            unique.append(ray)
    return tuple(unique)


def projection_orders(points):
    rays = critical_rays(points)
    orders = set()
    for k, ray in enumerate(rays):
        nxt = rays[(k + 1) % len(rays)]
        direction = (ray[0] + nxt[0], ray[1] + nxt[1])
        assert direction != (0, 0)
        order = tuple(sorted(range(7), key=lambda i: points[i][0] * direction[0] + points[i][1] * direction[1]))
        projections = [
            points[i][0] * direction[0] + points[i][1] * direction[1]
            for i in order
        ]
        assert all(a < b for a, b in zip(projections, projections[1:]))
        orders.add(order)
    return tuple(sorted(orders))


def is_acyclic(order, edge_signs):
    position = {vertex: k for k, vertex in enumerate(order)}
    outgoing = [[] for _ in range(7)]
    for (i, j), sign in edge_signs.items():
        # The desired potential difference has the sign of
        # s_ij (x_i-x_j).  Direct an inequality from low potential to high.
        if sign == (position[i] > position[j]):
            outgoing[j].append(i)
        else:
            outgoing[i].append(j)

    indegree = [0] * 7
    for i in range(7):
        for j in outgoing[i]:
            indegree[j] += 1
    stack = [i for i in range(7) if indegree[i] == 0]
    removed = 0
    while stack:
        i = stack.pop()
        removed += 1
        for j in outgoing[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                stack.append(j)
    return removed == 7


def main():
    uniform = h5.enumerate_uniform_extensions()
    _, full = h5.uniform_survivors(uniform)
    representatives = {}
    for signs, missing, edge_signs in full:
        representatives[h5.canonical_candidate(signs, missing, edge_signs)] = (
            signs, missing, edge_signs
        )
    representatives = list(representatives.values())
    assert len(representatives) == 6
    assert len(REALIZATIONS) == len(representatives)

    rows = []
    for (signs, missing, edge_signs), points in zip(representatives, REALIZATIONS):
        minimum_chirotope_minor = verify_chirotope(points, signs)
        orders = projection_orders(points)
        assert len(orders) == 40
        assert all(not is_acyclic(order, edge_signs) for order in orders)
        rows.append((len(orders), minimum_chirotope_minor))

    print("uniform_metric_orbits", len(representatives))
    print("generic_projection_orders_in_integer_witness", [count for count, _ in rows])
    print("minimum_absolute_chirotope_minors", [minor for _, minor in rows])
    print("acyclic_signed_projection_orders", [0] * len(rows))
    print("PASS: all six uniform H5 metric cases are excluded by projection potentials")


if __name__ == "__main__":
    main()
