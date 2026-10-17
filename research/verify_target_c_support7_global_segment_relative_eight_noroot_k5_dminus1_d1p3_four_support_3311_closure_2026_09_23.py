#!/usr/bin/env python3
"""Exact closure of the (3,3,1,1) four-support subbranch in eight-no-root k=5,D=-1,d_root=1,p=3.

Structural reductions already proved in the repository force exactly three singleton
root blocks, every other touched root block complete, coefficient rank three with
(d1,d2,d3)>=(2,4,5), and touched-complete root nullity exactly one in the m=4 case.
For D=-1,d_root=1, all five dimensions of the coefficient nullspace would have to
survive modulo the complete-root relation span. This verifier proves that for every
(3,3,1,1) four-support state the external rank increment is actually zero.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, gcd, lcm
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py"
spec = importlib.util.spec_from_file_location("eight_k5_p3_m4_3311_base", BASE)
R = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(R)

LOCAL = ((1, 0), (0, 1), (1, -1))
DIR_MASK = {(1, 0): 1, (0, 1): 2, (1, -1): 4}
SUPPORTS = tuple(combinations(range(1, 8), 4))
SUPPORT_INDEX = {F: i for i, F in enumerate(SUPPORTS)}
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


KEY_TO_CYCLE = {cycle_key(R.DESC[e]): e for e in R.NO_ROOT}
PERM_DATA = []
for perm in permutations(range(1, 8)):
    pmap = {i + 1: perm[i] for i in range(7)}
    support_map = tuple(
        SUPPORT_INDEX[tuple(sorted(pmap[x] for x in F))]
        for F in SUPPORTS
    )
    cycle_map = {}
    for e in R.NO_ROOT:
        mapped_desc = tuple(pmap[x] for x in R.DESC[e])
        cycle_map[e] = KEY_TO_CYCLE[cycle_key(mapped_desc)]
    PERM_DATA.append((support_map, cycle_map))
assert len(PERM_DATA) == 5040


def four_support_orbits():
    unseen = set(combinations(range(35), 4))
    reps = []
    orbit_total = 0
    while unseen:
        supports = min(unseen)
        orbit = {
            tuple(sorted(smap[i] for i in supports))
            for smap, _cmap in PERM_DATA
        }
        reps.append(supports)
        orbit_total += len(orbit)
        unseen.difference_update(orbit)
    assert len(reps) == 38
    assert orbit_total == comb(35, 4) == 52360
    return tuple(reps)


def profile_3311_candidates(support_indices):
    faces = tuple(SUPPORTS[i] for i in support_indices)
    out = set()
    for triple_positions in combinations(range(4), 2):
        triple_positions = set(triple_positions)
        singles = tuple(i for i in range(4) if i not in triple_positions)
        for singleton_choices in product(range(3), repeat=2):
            ext = []
            for i, F in enumerate(faces):
                es = SUPPORT_CYCLES[F]
                if i in triple_positions:
                    ext.extend(es)
                else:
                    ext.append(es[singleton_choices[singles.index(i)]])
            out.add(tuple(sorted(ext)))
    assert len(out) == comb(4, 2) * 3**2 == 54
    return out


def four_support_3311_cycle_orbits():
    reps = []
    for supports in four_support_orbits():
        stabilizer = [
            cmap
            for smap, cmap in PERM_DATA
            if tuple(sorted(smap[i] for i in supports)) == supports
        ]
        unseen = profile_3311_candidates(supports)
        while unseen:
            ext = min(unseen)
            reps.append(ext)
            orbit = {
                tuple(sorted(cmap[e] for e in ext))
                for cmap in stabilizer
            }
            unseen.difference_update(orbit)
    assert len(reps) == 754
    return tuple(reps)


def touched_blocks(ext):
    return tuple(sorted(
        b for b in range(35)
        if any(R.QCOMP[e][b] != (0, 0) for e in ext)
    ))


def complete_root_row(block):
    ids = R.BLOCKS[block]
    return tuple(
        R.MCOORD[ids[0]][70 + j]
        - R.MCOORD[ids[1]][70 + j]
        - R.MCOORD[ids[2]][70 + j]
        for j in range(15)
    )


HROW = tuple(complete_root_row(b) for b in range(35))
ROOT_MAX_NORM2 = max(sum(x * x for x in row) for row in HROW)
assert ROOT_MAX_NORM2 == 12


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


def rank_three(rows):
    a, b, c = rows
    for i, j, k in combinations(range(8), 3):
        det = (
            a[i] * (b[j] * c[k] - b[k] * c[j])
            - a[j] * (b[i] * c[k] - b[k] * c[i])
            + a[k] * (b[i] * c[j] - b[j] * c[i])
        )
        if det:
            return True
    return False


def generalized_weights(rows):
    assert rank_three(rows)
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


def primitive_int(v):
    scale = 1
    for x in v:
        scale = lcm(scale, x.denominator)
    a = [int(x * scale) for x in v]
    g = 0
    for x in a:
        g = gcd(g, abs(x))
    if g:
        a = [x // g for x in a]
    for x in a:
        if x:
            if x < 0:
                a = [-y for y in a]
            break
    return tuple(a)


def nullspace_int(key, n):
    pivots = [next(i for i, x in enumerate(row) if x) for row in key]
    free = [j for j in range(n) if j not in pivots]
    out = []
    for f in free:
        v = [Fraction(0)] * n
        v[f] = 1
        for row, p in zip(key, pivots):
            v[p] = -row[f]
        out.append(primitive_int(v))
    return out


def relation_rows_int8(ext, touched, states, constraint_key):
    rows = []
    for b, s in zip(touched, states):
        if R.STATES[s][2]:
            rows.append(HROW[b])

    for alpha in nullspace_int(constraint_key, len(ext)):
        tv = [
            sum(alpha[i] * R.MCOORD[e][70 + j] for i, e in enumerate(ext))
            for j in range(15)
        ]
        for b, s in zip(touched, states):
            vx = sum(alpha[i] * R.QCOMP[e][b][0] for i, e in enumerate(ext))
            vy = sum(alpha[i] * R.QCOMP[e][b][1] for i, e in enumerate(ext))
            beta = R.solve_local_coeffs_int(R.STATES[s][0], (-vx, -vy))
            ids = R.BLOCKS[b]
            for j0, q in enumerate(beta):
                if q:
                    for jj in range(15):
                        tv[jj] += q * R.MCOORD[ids[j0]][70 + jj]
        rows.append(tuple(tv))
    return rows


def main():
    assert R.lucas_lehmer_127()
    assert R.P * R.P > ROOT_MAX_NORM2 ** 15

    reps = four_support_3311_cycle_orbits()
    raw_cycle_sets = comb(35, 4) * comb(4, 2) * 3**2
    assert raw_cycle_sets == 2_827_440

    singleton_triples = 0
    direction_states = 0
    rank_three_states = 0
    generalized_weight_states = 0
    increment_census = Counter()
    max_norm2 = 0

    for ext in reps:
        touched = touched_blocks(ext)
        local_rows = {
            (b, d): singleton_row(ext, b, d)
            for b in touched
            for d in LOCAL
        }

        for singleton_blocks in combinations(touched, 3):
            complete = tuple(b for b in touched if b not in singleton_blocks)
            root_rank = R.rank_mod(tuple(HROW[b] for b in complete))
            root_nullity = len(complete) - root_rank
            if root_nullity != 1:
                continue
            singleton_triples += 1

            for directions in product(LOCAL, repeat=3):
                direction_states += 1
                rows = tuple(
                    local_rows[(b, d)]
                    for b, d in zip(singleton_blocks, directions)
                )
                if not rank_three(rows):
                    continue
                rank_three_states += 1

                d1, d2, d3 = generalized_weights(rows)
                if not (d1 >= 2 and d2 >= 4 and d3 >= 5):
                    continue
                generalized_weight_states += 1

                constraint_key = R.rowspace_key(rows)
                singletons = dict(zip(singleton_blocks, directions))
                states = tuple(
                    DIR_MASK[singletons[b]] if b in singletons else 7
                    for b in touched
                )
                rel_rows = relation_rows_int8(ext, touched, states, constraint_key)
                for row in rel_rows:
                    max_norm2 = max(max_norm2, sum(x * x for x in row))
                increment = R.rank_mod(rel_rows) - root_rank
                increment_census[increment] += 1
                assert increment == 0

    assert singleton_triples == 148_014
    assert direction_states == 3_996_378
    assert rank_three_states == 2_416_118
    assert generalized_weight_states == 192_611
    assert dict(increment_census) == {0: 192_611}
    assert max_norm2 == 70
    assert R.P * R.P > max_norm2 ** 15

    print("PASS: eight-no-root k=5,D=-1,d_root=1,p=3 four-support (3,3,1,1) closure")
    print("raw_cycle_sets", raw_cycle_sets)
    print("S7_cycle_set_orbits", len(reps))
    print("admissible_singleton_triples", singleton_triples)
    print("direction_states", direction_states)
    print("rank_three_states", rank_three_states)
    print("generalized_weight_states", generalized_weight_states)
    print("external_rank_increment_census", dict(increment_census))
    print("max_relation_row_norm_squared", max_norm2)
    print("hadamard_exact_rank_bound", R.P * R.P > max_norm2 ** 15)


if __name__ == "__main__":
    main()
