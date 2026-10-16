#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product

V = tuple(range(1, 8))
EDGES = tuple(combinations(V, 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}

SUPPORTS = (
    (1, 2, 3, 4),
    (1, 2, 3, 5),
    (1, 4, 5, 6),
    (2, 4, 5, 7),
)
HIDDEN = (1, 2, 4, 5)


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


def cycle_edges(support):
    a = min(support)
    rest = tuple(x for x in support if x != a)
    out = set()
    for p in permutations(rest):
        if p[0] >= p[-1]:
            continue
        seq = (a,) + p
        out.add(tuple(sorted(tuple(sorted((seq[i], seq[(i + 1) % 4]))) for i in range(4))))
    assert len(out) == 3
    return tuple(sorted(out))


CYCLES = {F: cycle_edges(F) for F in SUPPORTS}
SUPPORT_SET = set(SUPPORTS)


def support_stabilizer():
    out = []
    for p in permutations(V):
        mp = {i + 1: p[i] for i in range(7)}
        image = {tuple(sorted(mp[x] for x in F)) for F in SUPPORTS}
        if image == SUPPORT_SET:
            out.append(mp)
    return tuple(out)


def map_cycle(c, mp):
    return tuple(sorted(tuple(sorted((mp[a], mp[b]))) for a, b in c))


def orbit_count(states, stabilizer):
    unseen = set(states)
    count = 0
    while unseen:
        x = min(unseen)
        orbit = {
            tuple(sorted(map_cycle(c, mp) for c in x))
            for mp in stabilizer
        }
        unseen.difference_update(orbit)
        count += 1
    return count


def profile_2222_states():
    states = []
    for omitted in product(range(3), repeat=4):
        ext = []
        for F, o in zip(SUPPORTS, omitted):
            ext.extend(c for i, c in enumerate(CYCLES[F]) if i != o)
        states.append(tuple(sorted(ext)))
    assert len(set(states)) == 81
    return tuple(states)


def profile_3221_states():
    states = []
    for triple_support in range(4):
        for singleton_support in range(4):
            if singleton_support == triple_support:
                continue
            double_supports = [i for i in range(4) if i not in (triple_support, singleton_support)]
            for singleton_choice in range(3):
                for omitted_a in range(3):
                    for omitted_b in range(3):
                        ext = []
                        for i, F in enumerate(SUPPORTS):
                            if i == triple_support:
                                ext.extend(CYCLES[F])
                            elif i == singleton_support:
                                ext.append(CYCLES[F][singleton_choice])
                            elif i == double_supports[0]:
                                ext.extend(c for j, c in enumerate(CYCLES[F]) if j != omitted_a)
                            else:
                                ext.extend(c for j, c in enumerate(CYCLES[F]) if j != omitted_b)
                        states.append(tuple(sorted(ext)))
    assert len(set(states)) == 324
    return tuple(states)


def main():
    touched = tuple(sorted({t for F in SUPPORTS for t in combinations(F, 3)}))
    assert len(touched) == 15
    assert set(combinations(HIDDEN, 3)).issubset(touched)

    full_rank = rank_q(tuple(tri_row(t) for t in touched))
    full_nullity = len(touched) - full_rank
    assert full_rank == 10
    assert full_nullity == 5

    complement_nullities = Counter()
    for singleton_triple in combinations(touched, 3):
        complete = tuple(t for t in touched if t not in singleton_triple)
        nullity = len(complete) - rank_q(tuple(tri_row(t) for t in complete))
        complement_nullities[nullity] += 1
        assert nullity >= 2
    assert complement_nullities == Counter({2: 350, 3: 103, 4: 2})

    stabilizer = support_stabilizer()
    assert len(stabilizer) == 4
    support_orbit_size = 5040 // len(stabilizer)
    assert support_orbit_size == 1260

    states_2222 = profile_2222_states()
    states_3221 = profile_3221_states()
    assert orbit_count(states_2222, stabilizer) == 24
    assert orbit_count(states_3221, stabilizer) == 84

    raw_2222 = support_orbit_size * len(set(states_2222))
    raw_3221 = support_orbit_size * len(set(states_3221))
    assert raw_2222 == 102_060
    assert raw_3221 == 408_240

    print('PASS: hidden-tetrahedron support orbit is impossible in the p=3,m=4 branch')
    print('support_representative', SUPPORTS)
    print('hidden_tetrahedron', HIDDEN)
    print('touched_triangles', len(touched))
    print('touched_rank', full_rank)
    print('touched_nullity', full_nullity)
    print('singleton_complement_nullity_census', dict(sorted(complement_nullities.items())))
    print('support_stabilizer_order', len(stabilizer))
    print('support_orbit_size', support_orbit_size)
    print('2222_cycle_set_orbits', 24)
    print('3221_cycle_set_orbits', 84)
    print('2222_raw_cycle_sets', raw_2222)
    print('3221_raw_cycle_sets', raw_3221)


if __name__ == '__main__':
    main()
