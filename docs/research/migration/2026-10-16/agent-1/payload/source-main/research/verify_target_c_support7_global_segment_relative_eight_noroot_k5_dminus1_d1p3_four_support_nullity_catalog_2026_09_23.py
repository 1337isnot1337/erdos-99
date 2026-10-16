#!/usr/bin/env python3
"""Exact S7 catalog for the four-support nullity obstruction in Target C p=3,m=4.

This finite certificate enumerates all four-element sets of tetrahedral supports
on seven vertices up to S7, computes the exact row-nullity of the touched
triangle-boundary matrix over Q, and checks every deletion of three touched
triangle rows. It also counts the (3,2,2,1) and (2,2,2,2) cycle-set orbits on
the three exceptional support classes.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product

V = tuple(range(1, 8))
SUPPORTS = tuple(combinations(V, 4))
EDGES = tuple(combinations(V, 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
PERMS = tuple(permutations(V))


def tri_row(t):
    a, b, c = t
    r = [0] * len(EDGES)
    r[EDGE_INDEX[(a, b)]] = 1
    r[EDGE_INDEX[(a, c)]] = -1
    r[EDGE_INDEX[(b, c)]] = 1
    return tuple(r)


def rank_q(rows):
    if not rows:
        return 0
    a = [list(map(Fraction, row)) for row in rows]
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(r + 1, len(a)):
            if a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def image_support_set(state, p):
    mp = {i + 1: p[i] for i in range(7)}
    return tuple(sorted(tuple(sorted(mp[x] for x in F)) for F in state))


def support_orbit_reps():
    unseen = set(combinations(SUPPORTS, 4))
    reps = []
    orbit_total = 0
    while unseen:
        state = min(unseen)
        orbit = {image_support_set(state, p) for p in PERMS}
        reps.append(min(orbit))
        orbit_total += len(orbit)
        unseen.difference_update(orbit)
    assert len(reps) == 38
    assert orbit_total == 52_360
    return tuple(sorted(reps))


def support_stabilizer(rep):
    target = set(rep)
    out = []
    for p in PERMS:
        mp = {i + 1: p[i] for i in range(7)}
        image = {tuple(sorted(mp[x] for x in F)) for F in rep}
        if image == target:
            out.append(mp)
    return tuple(out)


def touched_triangles(rep):
    return tuple(sorted({t for F in rep for t in combinations(F, 3)}))


def cycle_edges(F):
    a = min(F)
    rest = tuple(x for x in F if x != a)
    out = set()
    for p in permutations(rest):
        if p[0] >= p[-1]:
            continue
        seq = (a,) + p
        out.add(tuple(sorted(
            tuple(sorted((seq[i], seq[(i + 1) % 4])))
            for i in range(4)
        )))
    assert len(out) == 3
    return tuple(sorted(out))


def profile_3221_states(rep):
    cycles = {F: cycle_edges(F) for F in rep}
    out = set()
    for triple_support in range(4):
        for singleton_support in range(4):
            if singleton_support == triple_support:
                continue
            doubles = [i for i in range(4) if i not in (triple_support, singleton_support)]
            for singleton_choice in range(3):
                for omit_a in range(3):
                    for omit_b in range(3):
                        ext = []
                        for i, F in enumerate(rep):
                            es = cycles[F]
                            if i == triple_support:
                                ext.extend(es)
                            elif i == singleton_support:
                                ext.append(es[singleton_choice])
                            elif i == doubles[0]:
                                ext.extend(e for j, e in enumerate(es) if j != omit_a)
                            else:
                                ext.extend(e for j, e in enumerate(es) if j != omit_b)
                        out.add(tuple(sorted(ext)))
    assert len(out) == 324
    return out


def profile_2222_states(rep):
    cycles = {F: cycle_edges(F) for F in rep}
    out = set()
    for omissions in product(range(3), repeat=4):
        ext = []
        for F, omit in zip(rep, omissions):
            ext.extend(e for j, e in enumerate(cycles[F]) if j != omit)
        out.add(tuple(sorted(ext)))
    assert len(out) == 81
    return out


def map_cycle(c, mp):
    return tuple(sorted(tuple(sorted((mp[a], mp[b]))) for a, b in c))


def cycle_orbit_count(states, stabilizer):
    unseen = set(states)
    count = 0
    sizes = Counter()
    while unseen:
        x = min(unseen)
        orbit = {tuple(sorted(map_cycle(c, mp) for c in x)) for mp in stabilizer}
        sizes[len(orbit)] += 1
        unseen.difference_update(orbit)
        count += 1
    return count, sizes


def main():
    reps = support_orbit_reps()
    records = []
    for rep in reps:
        T = touched_triangles(rep)
        rank = rank_q(tuple(tri_row(t) for t in T))
        nullity = len(T) - rank
        complement_census = Counter()
        for deleted in combinations(T, 3):
            deleted = set(deleted)
            complete = tuple(t for t in T if t not in deleted)
            nu = len(complete) - rank_q(tuple(tri_row(t) for t in complete))
            complement_census[nu] += 1
        stabilizer = support_stabilizer(rep)
        records.append((rep, len(stabilizer), len(T), rank, nullity, complement_census, stabilizer))

    assert Counter(r[1] for r in records) == Counter({
        1: 2, 2: 8, 4: 12, 6: 2, 8: 5, 12: 2,
        16: 2, 24: 2, 36: 1, 48: 1, 144: 1,
    })
    assert Counter(r[4] for r in records) == Counter({4: 35, 5: 3})
    assert Counter(min(r[5]) for r in records) == Counter({1: 35, 2: 3})

    exceptional = tuple(r for r in records if r[4] == 5)
    expected_reps = (
        ((1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 4, 5), (3, 4, 5, 6)),
        ((1, 2, 3, 4), (1, 2, 3, 5), (1, 4, 5, 6), (2, 4, 5, 6)),
        ((1, 2, 3, 4), (1, 2, 3, 5), (1, 4, 5, 6), (2, 4, 5, 7)),
    )
    assert tuple(sorted(r[0] for r in exceptional)) == tuple(sorted(expected_reps))
    assert Counter(r[1] for r in exceptional) == Counter({4: 1, 8: 1, 12: 1})

    profile_rows = []
    for rep, stab_order, _nt, _rank, _nu, census, stabilizer in exceptional:
        assert min(census) >= 2
        o3221, sizes3221 = cycle_orbit_count(profile_3221_states(rep), stabilizer)
        o2222, sizes2222 = cycle_orbit_count(profile_2222_states(rep), stabilizer)
        support_orbit_size = 5040 // stab_order
        profile_rows.append((
            rep, stab_order, support_orbit_size,
            o3221, support_orbit_size * 324, dict(sorted(sizes3221.items())),
            o2222, support_orbit_size * 81, dict(sorted(sizes2222.items())),
            dict(sorted(census.items())),
        ))

    by_stab = {row[1]: row for row in profile_rows}
    assert by_stab[4][3:5] == (84, 408_240)
    assert by_stab[8][3:5] == (42, 204_120)
    assert by_stab[12][3:5] == (34, 136_080)
    assert by_stab[4][6:8] == (24, 102_060)
    assert by_stab[8][6:8] == (15, 51_030)
    assert by_stab[12][6:8] == (10, 34_020)

    print("PASS: complete four-support nullity catalog")
    print("support_set_orbits", len(records))
    print("support_stabilizer_distribution", dict(sorted(Counter(r[1] for r in records).items())))
    print("touched_nullity_distribution", dict(sorted(Counter(r[4] for r in records).items())))
    print("minimum_three_deletion_complement_nullity_distribution", dict(sorted(Counter(min(r[5]) for r in records).items())))
    print("exceptional_support_orbits", len(exceptional))
    for row in sorted(profile_rows, key=lambda x: x[1]):
        print("exceptional", row)
    print("3221_nullity5_cycle_set_orbits", sum(row[3] for row in profile_rows))
    print("3221_nullity5_raw_cycle_sets", sum(row[4] for row in profile_rows))
    print("3221_new_beyond_order4_orbit_reps", by_stab[8][3] + by_stab[12][3])
    print("3221_new_beyond_order4_raw_cycle_sets", by_stab[8][4] + by_stab[12][4])
    print("2222_nullity5_cycle_set_orbits", sum(row[6] for row in profile_rows))
    print("2222_nullity5_raw_cycle_sets", sum(row[7] for row in profile_rows))


if __name__ == "__main__":
    main()
