#!/usr/bin/env python3
"""Exact closure of the synchronized t=6, k=5 Target-C density branch.

A hypothetical six-no-root counterexample with k=5 has rank-one global
coefficient-constraint space P and, by the deletion-shadow synchronization
theorem, is in exactly one of the two cases

    D=-2, p=7,   or   D=-1, p=8.

Every deletion shadow has five no-root rows, k=4, and the same p.  Hence the
line P projects nontrivially after deleting every external coordinate, so a
primitive generator of P has support at least two.

For fixed six no-root rows and P, define the same virtual canonical state used
in the established five-no-root k=4 containment theorem: a touched root-0 block
is empty iff its empty-state constraint is contained in P, and complete
otherwise.  Let C be its complete-block set and

    d = |C| - rank H(C),

where H(C) is the span of the complete-block T-relation rows.

The five-no-root containment theorem lifts through deletion: for each deleted
external coordinate i, the deletion-canonical complete set C_i is contained in
C, has deficiency at least 2, and every deletion null(P_i) relation lies in
H(C_i).  The six-row null(P) hyperplane is spanned by its coordinate-zero
subspaces, so every six-row external relation lies in H(C).  Consequently

d >= 2 and delta(A) <= |C|-d

(up to extra canonical-empty completions, whose +3 rows and at-most +1 delta
cancel in the defect bound).  If q canonical-complete blocks are replaced by
compatible incomplete states, then

    D(A) >= 6 + p + 3d - 3q.

For d>=4 this already excludes both p=7 and p=8.  This verifier exhausts only
the low-deficiency canonical states needed to finish d=2,3.  It constructs an
S7-cover of six-subsets by canonical augmentation from the exact 20,451
five-subset orbits.  The cover has 325,955 representatives (44 excess
representatives over the independently established 325,911 S7 orbit count).
Across all obtainable rank-one lines it finds 3,702,924 virtual canonical
states.  Only 148 have d=2 and 18,600 have d=3.  After imposing the necessary
support(P)>=2 condition from deletion synchronization, only 39 d=2 and 2,825
d=3 cover states remain.

The support-overlap corollary says every nonempty incomplete block in a
counterexample is touched by at least two of the six no-root cycles.  Among
canonical-complete blocks satisfying that overlap, the maximum number that can
be replaced by a compatible singleton is 2 for d=2 and 3 for d=3.  Therefore
at fixed p the number q of canonical-complete incomplete blocks obeys

    2q - min(q,s) <= p,

where s<=2 for d=2 and s<=3 for d=3.  This gives q<=4 at (d,p)=(2,7), q<=5
at (2,8), q<=5 at (3,7), and q<=5 at (3,8).  The defect lower bounds are then
respectively 7, 5, 7, and 8.  For d>=4 they are at least 4 and 2.

Hence neither synchronized k=5 boundary can contain a counterexample.

All complete-block ranks are computed modulo P=2^127-1.  The imported base
verifier checks primality by Lucas-Lehmer; complete-block relation rows have
squared norm at most 12, and P^2>12^15, so Hadamard makes every modular rank
used here exact over Q.
"""
from collections import Counter
from itertools import permutations
from math import comb, gcd
from pathlib import Path
import contextlib
import importlib.util
import io
import tempfile

import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k5_2026_09_20.py"
spec = importlib.util.spec_from_file_location("relative_five_noroot_k5_for_t6_k5", BASE)
K = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(K)
R = K.R

COMPLETE_T = tuple(
    tuple(
        R.MCOORD[ids[0]][70 + j]
        - R.MCOORD[ids[1]][70 + j]
        - R.MCOORD[ids[2]][70 + j]
        for j in range(15)
    )
    for ids in R.BLOCKS
)
assert max(sum(x * x for x in row) for row in COMPLETE_T) == 12


def primitive_line(row):
    """Primitive sign-normalized integer generator, or None for the zero row."""
    g = 0
    for x in row:
        g = gcd(g, abs(int(x)))
    if g == 0:
        return None
    out = tuple(int(x) // g for x in row)
    for x in out:
        if x:
            if x < 0:
                out = tuple(-y for y in out)
            break
    return out


def local_cycle_data(keys):
    key_to_global = {K.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}
    local_to_global = tuple(key_to_global[key] for key in keys)
    info = []
    for e in local_to_global:
        data = []
        for block, (x, y) in enumerate(R.QCOMP[e]):
            if (x, y) != (0, 0):
                data.append((block, x, y))
        assert len(data) == 4
        info.append(tuple(data))
    return local_to_global, tuple(info)


def block_profile(ext_local, info):
    """Return touched-block data and every obtainable rank-one line P.

    For each touched block we store its six local quotient vectors, its empty
    constraint line when the empty constraint has rank one (None means rank
    two here), and the three singleton constraint lines (None means rank zero).
    """
    values = {}
    for pos, local_cycle in enumerate(ext_local):
        for block, x, y in info[local_cycle]:
            if block not in values:
                values[block] = [[0, 0] for _ in range(6)]
            values[block][pos] = [x, y]

    obtainable = set()
    empty_line = {}
    singleton_lines = {}

    for block, local_values in values.items():
        xrow = tuple(v[0] for v in local_values)
        yrow = tuple(v[1] for v in local_values)
        px = primitive_line(xrow)
        py = primitive_line(yrow)
        if px is None:
            empty = py
        elif py is None or px == py:
            empty = px
        else:
            empty = None  # rank-two empty constraint
        empty_line[block] = empty
        if empty is not None:
            obtainable.add(empty)

        singles = []
        for lx, ly in R.LOCAL:
            normal = tuple(lx * v[1] - ly * v[0] for v in local_values)
            line = primitive_line(normal)
            singles.append(line)
            if line is not None:
                obtainable.add(line)
        singleton_lines[block] = tuple(singles)

    return values, tuple(obtainable), empty_line, singleton_lines


def build_permutation_maps(keys):
    key_to_local = {key: i for i, key in enumerate(keys)}
    maps = []
    for perm in permutations(range(1, 8)):
        pmap = {i + 1: perm[i] for i in range(7)}
        arr = []
        for key in keys:
            mapped = tuple(
                sorted(tuple(sorted((pmap[a], pmap[b]))) for a, b in key)
            )
            arr.append(key_to_local[mapped])
        maps.append(tuple(arr))
    assert len(maps) == 5040
    return np.array(maps, dtype=np.uint8)


def six_augmentation_cover(keys, five_orbits):
    """Canonical-augmentation cover of all S7 orbits of six-subsets.

    We first label every one of C(105,5) five-subsets by its exact orbit id in a
    temporary int32 memmap.  For each canonical five-parent, extensions are
    reduced by the parent stabilizer and retained only when that parent orbit id
    is minimal among the six deletion parents.  Standard canonical augmentation
    then guarantees at least one retained representative for every six-orbit.
    """
    perm_maps = build_permutation_maps(keys)
    c2 = np.array([comb(i, 2) for i in range(106)], dtype=np.int64)
    c3 = np.array([comb(i, 3) for i in range(106)], dtype=np.int64)
    c4 = np.array([comb(i, 4) for i in range(106)], dtype=np.int64)
    c5 = np.array([comb(i, 5) for i in range(106)], dtype=np.int64)

    def rank5_tuple(t):
        a, b, c, d, e = t
        return int(a + c2[b] + c3[c] + c4[d] + c5[e])

    with tempfile.TemporaryDirectory(prefix="e99-six-k5-") as tmp:
        orbit_path = Path(tmp) / "five_orbit_ids.i32"
        orbit_id = np.memmap(
            orbit_path,
            dtype=np.int32,
            mode="w+",
            shape=(comb(105, 5),),
        )
        orbit_id[:] = -1

        for oid, parent in enumerate(five_orbits):
            images = np.sort(perm_maps[:, parent], axis=1)
            ranks = (
                images[:, 0].astype(np.int64)
                + c2[images[:, 1]]
                + c3[images[:, 2]]
                + c4[images[:, 3]]
                + c5[images[:, 4]]
            )
            orbit_id[ranks] = oid

        assert np.count_nonzero(orbit_id < 0) == 0

        six = []
        for oid, parent in enumerate(five_orbits):
            images = np.sort(perm_maps[:, parent], axis=1)
            stabilizer = perm_maps[
                np.all(images == np.array(parent, dtype=np.uint8), axis=1)
            ]
            remaining = set(range(105)) - set(parent)
            while remaining:
                x = min(remaining)
                orbit = {int(v) for v in stabilizer[:, x].tolist()}
                remaining.difference_update(orbit)
                child = tuple(sorted(parent + (x,)))
                parent_types = []
                for j in range(6):
                    deletion = child[:j] + child[j + 1 :]
                    parent_type = int(orbit_id[rank5_tuple(deletion)])
                    assert parent_type >= 0
                    parent_types.append(parent_type)
                if oid == min(parent_types):
                    six.append(child)

        del orbit_id

    assert len(six) == 325955
    return tuple(six)


def max_q_from_cost(p, singleton_capacity):
    """Largest q whose q canonical-complete incomplete blocks can fit in p rows."""
    q = 0
    while 2 * (q + 1) - min(q + 1, singleton_capacity) <= p:
        q += 1
    return q


def main():
    assert R.lucas_lehmer_127()
    assert R.P * R.P > 12 ** 15

    keys, five_orbits, orbit_sizes, augmentation_candidates = K.five_no_root_orbits()
    assert len(five_orbits) == 20451
    assert sum(orbit_sizes) == comb(105, 5) == 96560646
    assert augmentation_candidates == 20475

    six_cover = six_augmentation_cover(keys, five_orbits)
    _local_to_global, info = local_cycle_data(keys)

    rank_cache = {}
    deficiency = Counter()
    low_d_support = Counter()
    singleton_capacity = {2: Counter(), 3: Counter()}
    canonical_states = 0

    def complete_deficiency(complete_set):
        cached = rank_cache.get(complete_set)
        if cached is not None:
            return cached
        rank = R.rank_mod([COMPLETE_T[b] for b in complete_set])
        d = len(complete_set) - rank
        rank_cache[complete_set] = d
        return d

    for ext_local in six_cover:
        values, lines, empty_line, singleton_lines = block_profile(ext_local, info)
        for line in lines:
            complete_set = tuple(
                sorted(block for block in values if empty_line[block] != line)
            )
            d = complete_deficiency(complete_set)
            canonical_states += 1
            deficiency[d] += 1
            assert d >= 2

            # A synchronized k=5 counterexample has k=4 after every deletion.
            # Therefore the rank-one line must remain nonzero after deleting any
            # coordinate, equivalently its primitive generator has support >=2.
            if sum(x != 0 for x in line) < 2 or d > 3:
                continue

            low_d_support[d] += 1
            capable = 0
            for block in complete_set:
                support = sum(1 for v in values[block] if v != [0, 0])
                if support < 2:
                    continue
                # A singleton is compatible with P iff its local constraint is
                # zero or is exactly P.  Count blocks, not orientations.
                if any(local is None or local == line for local in singleton_lines[block]):
                    capable += 1
            singleton_capacity[d][capable] += 1

    assert canonical_states == 3702924
    assert dict(sorted(deficiency.items())) == {
        2: 148,
        3: 18600,
        4: 422241,
        5: 1933839,
        6: 1018539,
        7: 277487,
        8: 31217,
        9: 785,
        10: 68,
    }
    assert dict(sorted(low_d_support.items())) == {2: 39, 3: 2825}
    assert dict(sorted(singleton_capacity[2].items())) == {1: 9, 2: 30}
    assert dict(sorted(singleton_capacity[3].items())) == {
        0: 969,
        1: 906,
        2: 942,
        3: 8,
    }

    max_singletons = {
        d: max(census) for d, census in singleton_capacity.items()
    }
    assert max_singletons == {2: 2, 3: 3}

    # Uniform lower bounds D >= 6+p+3d-3q.  For d=2,3, q is also bounded by
    # the minimum row cost 2q-min(q,s) forced by the singleton-capacity scan.
    low_bounds = {}
    for d in (2, 3):
        s = max_singletons[d]
        for p in (7, 8):
            q = max_q_from_cost(p, s)
            low_bounds[(d, p)] = 6 + p + 3 * d - 3 * q

    # For d>=4, q<=p alone gives these minima.
    low_bounds[(4, 7)] = 6 + 7 + 3 * 4 - 3 * 7
    low_bounds[(4, 8)] = 6 + 8 + 3 * 4 - 3 * 8

    assert low_bounds == {
        (2, 7): 7,
        (2, 8): 5,
        (3, 7): 7,
        (3, 8): 8,
        (4, 7): 4,
        (4, 8): 2,
    }

    print("PASS: six-no-root k=5 synchronized boundary closure")
    print("five_orbits", len(five_orbits))
    print("six_augmentation_cover", len(six_cover))
    print("known_six_orbits", 325911)
    print("augmentation_excess_representatives", len(six_cover) - 325911)
    print("rank_one_virtual_canonical_states", canonical_states)
    print("deficiency_census_cover", dict(sorted(deficiency.items())))
    print("support_ge_2_low_d", dict(sorted(low_d_support.items())))
    print("d2_singleton_capacity", dict(sorted(singleton_capacity[2].items())))
    print("d3_singleton_capacity", dict(sorted(singleton_capacity[3].items())))
    print("defect_lower_bounds", dict(sorted(low_bounds.items())))
    print("max_complete_relation_row_norm_squared", 12)
    print("hadamard_exact_rank_bound", R.P * R.P > 12 ** 15)


if __name__ == "__main__":
    main()
