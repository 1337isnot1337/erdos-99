#!/usr/bin/env python3
"""Exact support-level certificate closing e=8 in the final p=6 branch.

Committed inputs used by the certificate:
  * eight distinct no-root four-cycles, with at most three orientations on any
    fixed tetrahedral 4-support;
  * rank(P)=3 and generalized weights (d1,d2,d3)>=(2,4,5);
  * exactly six touched actual-singleton triangle blocks and eight touched
    actual-empty triangle blocks;
  * for an empty block b, dim(E_b)=2 iff some containing tetrahedral support
    occurs with multiplicity >=2; otherwise dim(E_b)=1;
  * the already-proved incidence lemma z<=3, where z counts rank-one empty
    blocks touched by exactly two external cycle coordinates.

The search intentionally ignores the additional face-nullity condition nu(T)<=9
and all phase/orientation restrictions. Thus it enumerates a strict superset of
actual e=8 states. Every retained support multiset fails z<=3.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product
from math import factorial

VERTICES = tuple(range(7))
SUPPORTS = tuple(combinations(VERTICES, 4))
SUPPORT_INDEX = {s: i for i, s in enumerate(SUPPORTS)}
TRIANGLES = tuple(combinations(VERTICES, 3))
EXPECTED_ORBITS = (1, 1, 4, 14, 61, 268, 1283, 6032, 27763)


def support_perm(vertex_perm):
    return tuple(
        SUPPORT_INDEX[tuple(sorted(vertex_perm[v] for v in s))]
        for s in SUPPORTS
    )


def burnside_orbit_counts():
    """Independent Burnside count for multisets of size <=8, multiplicity <=3."""
    fixed_totals = [0] * 9
    for p in permutations(VERTICES):
        smap = support_perm(p)
        seen = [False] * 35
        cycle_lengths = []
        for i in range(35):
            if seen[i]:
                continue
            j = i
            length = 0
            while not seen[j]:
                seen[j] = True
                length += 1
                j = smap[j]
            cycle_lengths.append(length)

        dp = [0] * 9
        dp[0] = 1
        for length in cycle_lengths:
            ndp = [0] * 9
            for total, ways in enumerate(dp):
                if not ways:
                    continue
                for multiplicity in range(4):
                    nxt = total + multiplicity * length
                    if nxt <= 8:
                        ndp[nxt] += ways
            dp = ndp
        for k in range(9):
            fixed_totals[k] += dp[k]

    order = factorial(7)
    assert all(x % order == 0 for x in fixed_totals)
    out = tuple(x // order for x in fixed_totals)
    assert out == EXPECTED_ORBITS, out
    return out


@lru_cache(maxsize=None)
def canonical(multiset):
    """Canonical S7 representative using the invariant vertex-degree partition."""
    degree = [0] * 7
    for si in multiset:
        for v in SUPPORTS[si]:
            degree[v] += 1

    values = sorted(set(degree), reverse=True)
    groups = []
    positions = []
    offset = 0
    for value in values:
        group = tuple(v for v in VERTICES if degree[v] == value)
        groups.append(group)
        positions.append(tuple(range(offset, offset + len(group))))
        offset += len(group)

    best = None
    for choices in product(*(permutations(group) for group in groups)):
        relabel = [None] * 7
        for old_order, new_positions in zip(choices, positions):
            for old, new in zip(old_order, new_positions):
                relabel[old] = new
        image = tuple(sorted(
            SUPPORT_INDEX[tuple(sorted(relabel[v] for v in SUPPORTS[si]))]
            for si in multiset
        ))
        if best is None or image < best:
            best = image
    return best


def support_multiset_orbits():
    """Canonical augmentation through size eight, independently checked by Burnside."""
    reps = {()}
    counts = [1]
    for _size in range(1, 9):
        out = set()
        for multiset in reps:
            multiplicities = Counter(multiset)
            for si in range(35):
                if multiplicities[si] >= 3:
                    continue
                out.add(canonical(tuple(sorted(multiset + (si,)))))
        reps = out
        counts.append(len(reps))
    counts = tuple(counts)
    assert counts == EXPECTED_ORBITS, counts
    return tuple(sorted(reps))


def block_data(multiset):
    """Return touched blocks and individually eligible empty blocks."""
    multiplicities = Counter(multiset)
    touched = []
    eligible = {}
    for b, tri in enumerate(TRIANGLES):
        incidence = frozenset(
            occurrence
            for occurrence, si in enumerate(multiset)
            if set(tri).issubset(SUPPORTS[si])
        )
        if not incidence:
            continue
        touched.append(b)
        rank_two = any(
            multiplicities[si] >= 2
            for si in set(multiset[i] for i in incidence)
        )
        n = len(incidence)
        dimension = 2 if rank_two else 1
        if (dimension == 2 and n >= 4) or (dimension == 1 and n >= 2):
            eligible[b] = (incidence, dimension, n)
    return tuple(touched), eligible


def pair_compatible(a, b, eligible):
    Ia, da, na = eligible[a]
    Ib, db, nb = eligible[b]
    intersection = len(Ia & Ib)
    union = na + nb - intersection
    if da == db == 2:
        return intersection >= 2
    if da != db:
        return intersection >= 2 or union >= 5
    return intersection >= 2 or union >= 4


def empty_octuples(eligible):
    """Enumerate 8-cliques in the pairwise generalized-weight compatibility graph."""
    vertices = tuple(sorted(eligible))
    later_neighbors = {
        v: {
            w for w in vertices
            if w > v and pair_compatible(v, w, eligible)
        }
        for v in vertices
    }
    out = []

    def extend(chosen, candidates):
        need = 8 - len(chosen)
        if need == 0:
            out.append(tuple(chosen))
            return
        if len(candidates) < need:
            return
        ordered = sorted(candidates)
        for i, v in enumerate(ordered):
            if len(ordered) - i < need:
                break
            nxt = set(ordered[i + 1:]) & later_neighbors[v]
            extend(chosen + [v], nxt)

    extend([], set(vertices))
    return tuple(out)


def main():
    burnside = burnside_orbit_counts()
    reps = support_multiset_orbits()

    counts = Counter()
    residual = []
    z_census = Counter()

    for multiset in reps:
        touched, eligible = block_data(multiset)
        if len(touched) < 14:
            continue
        counts["touch_at_least_14"] += 1

        if len(eligible) < 8:
            continue
        counts["at_least_8_individually_eligible"] += 1

        octuples = empty_octuples(eligible)
        if not octuples:
            continue
        counts["pairwise_compatible_orbits"] += 1
        counts["pairwise_compatible_octuples"] += len(octuples)

        zs = []
        for octuple in octuples:
            z = sum(
                eligible[b][1] == 1 and eligible[b][2] == 2
                for b in octuple
            )
            zs.append(z)
            z_census[z] += 1
            if z <= 3:
                counts["z_le_3_survivors"] += 1
        residual.append((multiset, octuples, tuple(zs)))

    assert burnside == EXPECTED_ORBITS
    assert len(reps) == 27763
    assert counts["touch_at_least_14"] == 27590, counts
    assert counts["at_least_8_individually_eligible"] == 3105, counts
    assert counts["pairwise_compatible_orbits"] == 2, counts
    assert counts["pairwise_compatible_octuples"] == 3, counts
    assert dict(z_census) == {4: 3}, z_census
    assert counts["z_le_3_survivors"] == 0, counts

    expected_residual = {
        (
            (0, 1, 2, 4, 5, 10, 13, 16),
            (
                (0, 1, 2, 3, 5, 6, 9, 12),
                (0, 1, 2, 5, 6, 7, 9, 10),
            ),
            (4, 4),
        ),
        (
            (0, 1, 2, 4, 5, 10, 14, 17),
            ((0, 1, 2, 3, 5, 6, 9, 13),),
            (4,),
        ),
    }
    assert set(residual) == expected_residual, residual

    print("PASS: p=6 e=8 support-level closure")
    print("orbit_counts_size_0_through_8", EXPECTED_ORBITS)
    print("support_multiset_orbits_size_8", len(reps))
    print("touch_at_least_14", counts["touch_at_least_14"])
    print("at_least_8_individually_eligible", counts["at_least_8_individually_eligible"])
    print("pairwise_compatible_support_orbits", counts["pairwise_compatible_orbits"])
    print("pairwise_compatible_empty_octuples", counts["pairwise_compatible_octuples"])
    print("z_census", dict(sorted(z_census.items())))
    print("z_le_3_survivors", counts["z_le_3_survivors"])


if __name__ == "__main__":
    main()
