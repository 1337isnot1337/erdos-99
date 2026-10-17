#!/usr/bin/env python3
"""
Exact finite regression for the support-six reciprocal H5 reduction.

The calculation uses only integer signs and finite enumeration. It:
  * enumerates all uniform rank-3 chirotope extensions of a convex pentagon
    by two interior points;
  * imposes the ground 3+3 sign-order lemma and the hull-vertex 2+3
    alternation rule;
  * imposes the regular five-ray cross-tournament forced by the strict
    two-turn inequality at every non-ground physical pentagon;
  * quotients the uniform survivors by reflection fixing the ground hull
    vertex, interchange of the two interior points, and global sign reversal;
  * enumerates every simple allowed ground collinearity wall 0-i-j, with ij
    a missing matching edge, and repeats the same exact sign test.

No floating point, coordinates, or numerical tolerances are used.
"""

from collections import Counter
from functools import cmp_to_key
from itertools import combinations, permutations, product

V = tuple(range(7))
HULL = tuple(range(5))
NONGROUND = tuple(range(1, 7))
INTERIOR = (5, 6)
TRIPLES = list(combinations(V, 3))
TINDEX = {t: i for i, t in enumerate(TRIPLES)}


def parity_to_sorted(t):
    inv = sum(t[i] > t[j] for i in range(len(t)) for j in range(i + 1, len(t)))
    return -1 if inv & 1 else 1


def edge(a, b):
    return tuple(sorted((a, b)))


# Convex hull 0,1,2,3,4 in CCW order. For each interior point p, positivity
# against every directed hull edge is necessary and sufficient for p to lie
# in the interior of the convex pentagon at the chirotope level.
FIXED = {}
for t in combinations(HULL, 3):
    FIXED[t] = 1
for p in INTERIOR:
    for i in range(4):
        FIXED[(i, i + 1, p)] = 1
    FIXED[(0, 4, p)] = -1

FREE = [t for t in TRIPLES if t not in FIXED]
assert len(FREE) == 15


def chi(signs, a, b, c):
    if len({a, b, c}) < 3:
        return 0
    t = (a, b, c)
    s = tuple(sorted(t))
    return parity_to_sorted(t) * signs[TINDEX[s]]


# Exhaustive rank-3 B2 tests. The duplication is harmless and keeps the
# verifier transparent.
GP_TESTS = []
for subset in combinations(V, 5):
    for a in subset:
        rest = [x for x in subset if x != a]
        seen = set()
        for b, c, d, e in permutations(rest):
            raw = (
                ((a, b, c), (a, d, e), 1),
                ((a, b, d), (a, c, e), -1),
                ((a, b, e), (a, c, d), 1),
            )
            term = []
            for t1, t2, sgn in raw:
                s1 = tuple(sorted(t1))
                s2 = tuple(sorted(t2))
                term.append(
                    (
                        TINDEX[s1],
                        TINDEX[s2],
                        sgn * parity_to_sorted(t1) * parity_to_sorted(t2),
                    )
                )
            key = tuple(term)
            if key not in seen:
                seen.add(key)
                GP_TESTS.append(key)


def grassmann_pluecker_ok(signs):
    for term in GP_TESTS:
        vals = [sgn * signs[i] * signs[j] for i, j, sgn in term]
        if vals[0] == vals[1] == vals[2]:
            return False
    return True


def enumerate_uniform_extensions():
    base = [0] * len(TRIPLES)
    for t, s in FIXED.items():
        base[TINDEX[t]] = s

    out = []
    for bits in product((1, -1), repeat=len(FREE)):
        signs = base.copy()
        for t, b in zip(FREE, bits):
            signs[TINDEX[t]] = b
        if grassmann_pluecker_ok(signs):
            out.append(tuple(signs))
    return out


def all_matchings(items):
    items = list(items)
    if not items:
        yield []
        return
    a = items[0]
    for k in range(1, len(items)):
        b = items[k]
        rest = items[1:k] + items[k + 1 :]
        for tail in all_matchings(rest):
            yield [(a, b)] + tail


MATCHINGS = list(all_matchings(NONGROUND))
assert len(MATCHINGS) == 15


def hull_radial_order(signs, i):
    """CCW order of the other six rays inside the hull cone at hull vertex i."""
    pts = [j for j in V if j != i]

    def cmp(a, b):
        c = chi(signs, i, a, b)
        if c > 0:
            return -1
        if c < 0:
            return 1
        return 0

    arr = sorted(pts, key=cmp_to_key(cmp))
    nxt = (i + 1) % 5
    prev = (i - 1) % 5
    if arr[0] != nxt or arr[-1] != prev:
        arr2 = list(reversed(arr))
        assert arr2[0] == nxt and arr2[-1] == prev
        arr = arr2
    return arr


def regular_force_tournament(signs, v, edge_signs, missing):
    """
    Necessary combinatorial form of the strict two-turn inequality.

    For five force directions in cyclic order, delta_i+delta_{i+1}<pi makes
    each direction have positive cross product with exactly the next two and
    negative cross product with the previous two. Thus the pairwise cross
    tournament is the regular 5-tournament: every outdegree is exactly two.
    """
    neigh = [j for j in V if j != v and edge(v, j) not in missing]
    assert len(neigh) == 5
    outdeg = {j: 0 for j in neigh}

    for a_i, a in enumerate(neigh):
        for b in neigh[a_i + 1 :]:
            sa = 1 if edge_signs[edge(v, a)] else -1
            sb = 1 if edge_signs[edge(v, b)] else -1
            cross = sa * sb * chi(signs, v, a, b)
            if cross == 0:
                return False
            if cross > 0:
                outdeg[a] += 1
            else:
                outdeg[b] += 1

    return all(d == 2 for d in outdeg.values())


def uniform_survivors(uniform):
    hull_stage = []
    full = []

    for oi, signs in enumerate(uniform):
        orders = {i: hull_radial_order(signs, i) for i in HULL}
        order0 = orders[0]

        # Distinct-ray ground 3+3 equilibrium in an open semicircle: +--++-
        # or its global complement. In zero-based positions, the base positive
        # set is {0,3,4}.
        base_plus = {order0[k] for k in (0, 3, 4)}

        for ground_complement in (False, True):
            ground_plus = set(order0) - base_plus if ground_complement else base_plus
            ground_signs = {edge(0, j): (j in ground_plus) for j in NONGROUND}

            for matching in MATCHINGS:
                missing = {edge(*e) for e in matching}
                local = {}
                for i in range(1, 5):
                    mate = next(j for j in NONGROUND if j != i and edge(i, j) in missing)
                    order = [j for j in orders[i] if j != mate]
                    assert len(order) == 5
                    two = {order[1], order[3]}
                    local[i] = (order, two)

                for phases in product((0, 1), repeat=4):
                    edge_signs = dict(ground_signs)
                    ok = True
                    for phase, i in zip(phases, range(1, 5)):
                        order, two = local[i]
                        plus = two if phase == 0 else set(order) - two
                        for j in order:
                            e = edge(i, j)
                            value = j in plus
                            if e in edge_signs and edge_signs[e] != value:
                                ok = False
                                break
                            edge_signs[e] = value
                        if not ok:
                            break
                    if not ok:
                        continue

                    hull_stage.append((oi, matching, ground_complement, phases))

                    e56 = edge(5, 6)
                    values = [None] if e56 in missing else ([edge_signs[e56]] if e56 in edge_signs else [False, True])
                    for v56 in values:
                        complete = dict(edge_signs)
                        if e56 not in missing and e56 not in complete:
                            complete[e56] = v56
                        if all(
                            regular_force_tournament(signs, v, complete, missing)
                            for v in NONGROUND
                        ):
                            full.append((signs, frozenset(missing), complete))

    return hull_stage, full


# Symmetries preserving the labelled H5 setup: reflection of the pentagon
# fixing ground 0, interchange of the two interior points, and global sign
# reversal (handled when canonicalizing edge signs).
SYMMETRIES = []
for reflect in (False, True):
    for swap_interiors in (False, True):
        p = {i: i for i in V}  # new label -> old label
        if reflect:
            p.update({1: 4, 4: 1, 2: 3, 3: 2})
        if swap_interiors:
            p[5], p[6] = p[6], p[5]
        SYMMETRIES.append(p)


def transform_chirotope(signs, p):
    # Normalize the reflected orientation so hull triple 0,1,2 is positive.
    g = chi(signs, p[0], p[1], p[2])
    assert g in (-1, 1)
    return tuple(g * chi(signs, p[a], p[b], p[c]) for a, b, c in TRIPLES)


def transform_edges(edges, p):
    inv = {p[k]: k for k in p}
    return frozenset(edge(inv[a], inv[b]) for a, b in edges)


def canonical_candidate(signs, missing, edge_signs):
    all_edges = frozenset(edge(i, j) for i in V for j in V if i < j and edge(i, j) not in missing)
    plus = frozenset(e for e, value in edge_signs.items() if value)
    assert set(edge_signs) == set(all_edges)

    reps = []
    for p in SYMMETRIES:
        ct = transform_chirotope(signs, p)
        mt = transform_edges(missing, p)
        pt = transform_edges(plus, p)
        et = frozenset(edge(i, j) for i in V for j in V if i < j and edge(i, j) not in mt)
        sign_rep = min(tuple(sorted(pt)), tuple(sorted(et - pt)))
        reps.append((ct, tuple(sorted(mt)), sign_rep))
    return min(reps)


# The only possible simple nonuniformities are 0-i-j with ij missing. The
# free ground-collinearity triples in this H5 parametrization are exactly:
WALL_TARGETS = ((0, 2, 5), (0, 2, 6), (0, 3, 5), (0, 3, 6), (0, 5, 6))


def enumerate_simple_walls(uniform):
    by = {tuple(s): i for i, s in enumerate(uniform)}
    walls = []
    seen = set()
    for t in WALL_TARGETS:
        ti = TINDEX[t]
        for ai, a in enumerate(uniform):
            b = list(a)
            b[ti] *= -1
            b = tuple(b)
            if b not in by:
                continue
            bi = by[b]
            key = (t, min(ai, bi), max(ai, bi))
            if key in seen:
                continue
            seen.add(key)
            walls.append((t, ai, bi))
    return walls


def wall_chirotope(uniform, target, ai):
    signs = list(uniform[ai])
    signs[TINDEX[target]] = 0
    return tuple(signs)


def wall_survivors(uniform, walls):
    hull_stage = []
    full = []

    for target, ai, _bi in walls:
        _, u, v = target
        tied = edge(u, v)
        side = uniform[ai]
        wall = wall_chirotope(uniform, target, ai)

        for matching in MATCHINGS:
            missing = {edge(*e) for e in matching}
            if tied not in missing:
                continue

            # The tied mate is deleted before the local five-ray hull rule is
            # applied at a tied hull endpoint. Hence either adjacent uniform
            # side gives the same relevant order after deletion.
            orders = {i: hull_radial_order(side, i) for i in range(1, 5)}

            # At ground, coincident rays u,v cannot have opposite signs: they
            # would cancel and leave equality of two disjoint pairs of unit
            # rays in the same open semicircle. Hence they have the same sign.
            # After global reversal take u,v positive and choose exactly one
            # other positive ray; then also check the global complement.
            others = [x for x in NONGROUND if x not in (u, v)]
            for extra in others:
                base_plus = {u, v, extra}
                for ground_complement in (False, True):
                    ground_plus = set(NONGROUND) - base_plus if ground_complement else base_plus
                    edge_signs0 = {edge(0, j): (j in ground_plus) for j in NONGROUND}

                    for phases in product((0, 1), repeat=4):
                        edge_signs = dict(edge_signs0)
                        ok = True
                        for phase, i in zip(phases, range(1, 5)):
                            mate = next(j for j in NONGROUND if j != i and edge(i, j) in missing)
                            order = [j for j in orders[i] if j != mate]
                            assert len(order) == 5
                            two = {order[1], order[3]}
                            plus = two if phase == 0 else set(order) - two
                            for j in order:
                                e = edge(i, j)
                                value = j in plus
                                if e in edge_signs and edge_signs[e] != value:
                                    ok = False
                                    break
                                edge_signs[e] = value
                            if not ok:
                                break
                        if not ok:
                            continue

                        hull_stage.append((target, ai, matching, extra, ground_complement, phases))

                        e56 = edge(5, 6)
                        values = [None] if e56 in missing else ([edge_signs[e56]] if e56 in edge_signs else [False, True])
                        for v56 in values:
                            complete = dict(edge_signs)
                            if e56 not in missing and e56 not in complete:
                                complete[e56] = v56
                            if all(
                                regular_force_tournament(wall, w, complete, missing)
                                for w in NONGROUND
                            ):
                                full.append((target, wall, frozenset(missing), complete))

    return hull_stage, full


def main():
    uniform = enumerate_uniform_extensions()
    assert len(uniform) == 370

    uniform_hull, uniform_full = uniform_survivors(uniform)
    assert len(uniform_hull) == 600
    assert len(uniform_full) == 48

    uniform_orbits = {
        canonical_candidate(signs, missing, edge_signs)
        for signs, missing, edge_signs in uniform_full
    }
    assert len(uniform_orbits) == 6

    uniform_matchings = Counter(tuple(sorted(missing)) for _, missing, _ in uniform_full)
    assert sorted(uniform_matchings.values()) == [12, 12, 12, 12]

    walls = enumerate_simple_walls(uniform)
    wall_counts = Counter(t for t, _, _ in walls)
    assert wall_counts == Counter(
        {
            (0, 2, 5): 66,
            (0, 2, 6): 66,
            (0, 3, 5): 66,
            (0, 3, 6): 66,
            (0, 5, 6): 52,
        }
    )
    assert len(walls) == 316

    wall_hull, wall_full = wall_survivors(uniform, walls)
    assert len(wall_hull) == 488
    assert len(wall_full) == 80

    wall_full_counts = Counter(t for t, _, _, _ in wall_full)
    assert wall_full_counts[(0, 5, 6)] == 0
    for t in ((0, 2, 5), (0, 2, 6), (0, 3, 5), (0, 3, 6)):
        assert wall_full_counts[t] == 20

    wall_orbits = {
        canonical_candidate(signs, missing, edge_signs)
        for _target, signs, missing, edge_signs in wall_full
    }
    assert len(wall_orbits) == 10

    print("uniform_rank3_extensions", len(uniform))
    print("uniform_hull_sign_survivors", len(uniform_hull))
    print("uniform_regular_force_survivors", len(uniform_full))
    print("uniform_symmetry_orbits", len(uniform_orbits))
    print("uniform_matching_families", len(uniform_matchings), sorted(uniform_matchings.values()))
    print("simple_ground_collinearity_walls", len(walls), dict(sorted(wall_counts.items())))
    print("wall_hull_sign_survivors", len(wall_hull))
    print("wall_regular_force_survivors", len(wall_full))
    print("wall_symmetry_orbits", len(wall_orbits))
    print("interior_pair_collinear_survivors", wall_full_counts[(0, 5, 6)])
    print("PASS: support-six reciprocal H5 branch reduced to 6 uniform and 10 simple-wall exact sign/order orbits")


if __name__ == "__main__":
    main()
