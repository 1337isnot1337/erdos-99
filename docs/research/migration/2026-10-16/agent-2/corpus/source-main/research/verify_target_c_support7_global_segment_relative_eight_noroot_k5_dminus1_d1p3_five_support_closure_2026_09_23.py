#!/usr/bin/env python3
"""Exact closure of the m=5 subbranch of eight-no-root k=5,D=-1,d_root=1,p=3.

Earlier proof reductions force, in the five-support case:

* one five-vertex set W whose five tetrahedra are exactly the used supports;
* support multiplicities (3,2,1,1,1) or (2,2,2,1,1);
* three singleton root blocks among the ten triangles of W, not sharing one edge;
* every other touched root block complete;
* the three singleton coefficient rows form a rank-three space P with
  generalized weights (d1,d2,d3)>=(2,4,5).

The seven touched complete-root relation rows have rank six and nullity one.
For D=-1, the five null(P) relation rows would therefore have to contribute
five new T-directions, for total relation rank 11. This verifier exhausts the
finite five-support direction geometry and proves that every generalized-
weight-admissible state has total relation rank exactly six instead.

All relation rows are integral. Rank is computed modulo 2^127-1 and certified
as exact over Q by the same Hadamard argument used by the base verifier.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py"
spec = importlib.util.spec_from_file_location("eight_k5_p3_five_support_base", BASE)
R = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(R)

LOCAL = ((1, 0), (0, 1), (1, -1))
DIR_MASK = {(1, 0): 1, (0, 1): 2, (1, -1): 4}
W = (1, 2, 3, 4, 5)
SUPPORTS = tuple(combinations(W, 4))
TRIANGLES = tuple(combinations(W, 3))
BLOCK_INDEX = {b: i for i, b in enumerate(R.BLOCK_LABELS)}
TOUCHED = tuple(BLOCK_INDEX[t] for t in TRIANGLES)
SUPPORT_CYCLES = {
    F: tuple(e for e in R.NO_ROOT if set(R.DESC[e]) == set(F))
    for F in SUPPORTS
}
assert all(len(es) == 3 for es in SUPPORT_CYCLES.values())


def cycle_key(desc):
    d = list(desc)
    return tuple(sorted(
        tuple(sorted((d[i], d[(i + 1) % 4])))
        for i in range(4)
    ))


KEY_TO_CYCLE = {
    cycle_key(R.DESC[e]): e
    for e in R.NO_ROOT
    if set(R.DESC[e]) <= set(W)
}
W_CYCLES = tuple(sorted(KEY_TO_CYCLE.values()))
assert len(W_CYCLES) == 15


PERM_MAPS = []
for perm in permutations(W):
    pmap = dict(zip(W, perm))
    mapping = {}
    for e in W_CYCLES:
        mapped_desc = tuple(pmap[x] for x in R.DESC[e])
        mapping[e] = KEY_TO_CYCLE[cycle_key(mapped_desc)]
    PERM_MAPS.append(mapping)
assert len(PERM_MAPS) == 120


def canonical_ext(ext):
    return min(
        tuple(sorted(mapping[e] for e in ext))
        for mapping in PERM_MAPS
    )


def five_support_cycle_orbits():
    all_ext = set()
    for profile in ((3, 2, 1, 1, 1), (2, 2, 2, 1, 1)):
        for mults in set(permutations(profile)):
            choices = [
                tuple(combinations(SUPPORT_CYCLES[F], q))
                for F, q in zip(SUPPORTS, mults)
            ]
            for chosen in product(*choices):
                all_ext.add(tuple(sorted(e for subset in chosen for e in subset)))
    assert len(all_ext) == 4050
    reps = tuple(sorted({canonical_ext(ext) for ext in all_ext}))
    assert len(reps) == 43
    return reps


def singleton_triples():
    out = []
    for tris in combinations(TRIANGLES, 3):
        if len(set(tris[0]) & set(tris[1]) & set(tris[2])) >= 2:
            continue
        out.append(tuple(BLOCK_INDEX[t] for t in tris))
    assert len(out) == 110
    return tuple(out)


def singleton_row(ext, block, direction):
    lx, ly = direction
    return tuple(
        lx * R.QCOMP[e][block][1] - ly * R.QCOMP[e][block][0]
        for e in ext
    )


def primitive(v):
    g = 0
    for x in v:
        g = gcd(g, abs(x))
    assert g
    q = tuple(x // g for x in v)
    for x in q:
        if x:
            return tuple(-y for y in q) if x < 0 else q
    raise AssertionError("zero vector")


def generalized_weights(rows):
    """Exact generalized weights of a rank-three length-eight row code."""
    assert R.exact_rank(rows) == 3
    cols = [tuple(row[j] for row in rows) for j in range(8)]
    zero_count = cols.count((0, 0, 0))
    d3 = 8 - zero_count

    directions = Counter(
        primitive(c) for c in cols if c != (0, 0, 0)
    )
    d2 = 8 - (zero_count + max(directions.values()))

    nonzero = [c for c in cols if c != (0, 0, 0)]
    normals = set()
    for a, b in combinations(nonzero, 2):
        n = (
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0],
        )
        if n != (0, 0, 0):
            normals.add(primitive(n))
    assert normals
    max_plane_count = max(
        sum(n[0] * c[0] + n[1] * c[1] + n[2] * c[2] == 0 for c in cols)
        for n in normals
    )
    d1 = 8 - max_plane_count
    return d1, d2, d3


def relation_rank(ext, singleton_blocks, directions, constraint_key, norm_tracker):
    singletons = dict(zip(singleton_blocks, directions))
    states = tuple(
        DIR_MASK[singletons[b]] if b in singletons else 7
        for b in TOUCHED
    )
    rows = R.relation_rows_int(ext, TOUCHED, states, constraint_key)
    for row in rows:
        norm_tracker[0] = max(norm_tracker[0], sum(x * x for x in row))
    return R.rank_mod(rows)


def main():
    assert R.lucas_lehmer_127()
    reps = five_support_cycle_orbits()
    singleton_sets = singleton_triples()

    candidate_count = 0
    rank_three_count = 0
    generalized_weight_count = 0
    relation_rank_census = Counter()
    norm_tracker = [0]

    for ext in reps:
        local_rows = {
            (b, d): singleton_row(ext, b, d)
            for b in TOUCHED
            for d in LOCAL
        }
        for singleton_blocks in singleton_sets:
            for directions in product(LOCAL, repeat=3):
                candidate_count += 1
                rows = tuple(
                    local_rows[(b, d)]
                    for b, d in zip(singleton_blocks, directions)
                )
                if R.exact_rank(rows) != 3:
                    continue
                rank_three_count += 1
                d1, d2, d3 = generalized_weights(rows)
                if not (d1 >= 2 and d2 >= 4 and d3 >= 5):
                    continue
                generalized_weight_count += 1

                constraint_key = R.rowspace_key(rows)
                rank = relation_rank(
                    ext,
                    singleton_blocks,
                    directions,
                    constraint_key,
                    norm_tracker,
                )
                relation_rank_census[rank] += 1
                assert rank == 6, (
                    ext,
                    singleton_blocks,
                    directions,
                    (d1, d2, d3),
                    rank,
                )

    assert candidate_count == 127710
    assert rank_three_count == 118838
    assert generalized_weight_count == 36106
    assert dict(relation_rank_census) == {6: 36106}
    assert norm_tracker[0] == 84
    assert R.P * R.P > norm_tracker[0] ** 15

    print("PASS: eight-no-root k=5,D=-1,d_root=1,p=3 five-support closure")
    print("raw_eight_cycle_sets", 4050)
    print("S5_cycle_set_orbits", len(reps))
    print("valid_singleton_triples", len(singleton_sets))
    print("orbit_direction_candidates", candidate_count)
    print("rank_three_candidates", rank_three_count)
    print("generalized_weight_survivors", generalized_weight_count)
    print("relation_rank_census", dict(relation_rank_census))
    print("max_relation_row_norm_squared", norm_tracker[0])
    print("hadamard_exact_rank_bound", R.P * R.P > norm_tracker[0] ** 15)


if __name__ == "__main__":
    main()
