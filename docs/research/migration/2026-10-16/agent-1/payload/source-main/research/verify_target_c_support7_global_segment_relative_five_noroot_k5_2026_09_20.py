#!/usr/bin/env python3
"""Exact t=5,k=5 branch of the Target-C four-cycle rank-density audit.

Let M be the 85-dimensional four-cycle space modulo the automatic side-triangle
identities, T the 15-dimensional ground-root space, Q=M/T, and
    delta(A)=r_M(A)-r_Q(A).
For five no-root four-cycles, a possible violation of 3*delta(A)<=|A| has
(k,p) in {(2,0),(3,p<=3),(4,p<=6),(5,p<=9)} after stripping harmless
untouched blocks. This verifier closes the k=5,p<=9 branch.

For k=5 the global external coefficient-constraint space is zero. Hence every
touched root-0 quotient block must locally impose zero constraint. A complete
local triple or any two-row pair always works; a singleton works exactly when
all five external local components lie on its direction. Completing every
touched block gives a row-superfamily F, so delta(A)<=delta(F). That bound
leaves only 79,944 local states over 2,634 S7 orbit representatives; every one
is reranked exactly and has nonnegative defect.

The 96,560,646 five-subsets of the 105 no-root four-cycles are reduced to
20,451 exact S7 orbits. Orbit canonicalization uses only integer permutation
combinatorics. Rank decisions use P=2^127-1, with a Lucas-Lehmer primality
check and an explicit Hadamard bound; therefore the modular ranks equal ranks
over Q rather than being probabilistic finite-field evidence.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb
from pathlib import Path
import contextlib
import importlib.util
import io

import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py"
spec = importlib.util.spec_from_file_location("relative_four_noroot_k2_for_t5_k5", BASE)
R = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(R)


def cycle_key(desc):
    d = list(desc)
    return tuple(sorted(tuple(sorted((d[i], d[(i + 1) % 4]))) for i in range(4)))


def five_no_root_orbits():
    """Return exact S7 orbit representatives of 5-subsets of no-root cycles."""
    keys = sorted(cycle_key(R.DESC[e]) for e in R.NO_ROOT)
    key_to_local = {key: i for i, key in enumerate(keys)}

    perm_maps = []
    for perm in permutations(range(1, 8)):
        pmap = {i + 1: perm[i] for i in range(7)}
        arr = []
        for key in keys:
            mapped = tuple(sorted(tuple(sorted((pmap[a], pmap[b]))) for a, b in key))
            arr.append(key_to_local[mapped])
        perm_maps.append(tuple(arr))
    assert len(perm_maps) == 5040

    C2 = [comb(i, 2) for i in range(106)]
    C3 = [comb(i, 3) for i in range(106)]
    C4 = [comb(i, 4) for i in range(106)]
    C5 = [comb(i, 5) for i in range(106)]

    def rank4(t):
        a, b, c, d = t
        return a + C2[b] + C3[c] + C4[d]

    total4 = comb(105, 4)
    seen4 = bytearray(total4)
    orbit_id = [-1] * total4
    four_reps = []
    for t in combinations(range(105), 4):
        r = rank4(t)
        if seen4[r]:
            continue
        orbit = {
            tuple(sorted((arr[t[0]], arr[t[1]], arr[t[2]], arr[t[3]])))
            for arr in perm_maps
        }
        oid = len(four_reps)
        for u in orbit:
            ru = rank4(u)
            seen4[ru] = 1
            orbit_id[ru] = oid
        four_reps.append(t)
    assert len(four_reps) == 1186
    assert all(x >= 0 for x in orbit_id)

    candidates = []
    for oid, parent in enumerate(four_reps):
        parent_set = set(parent)
        stabilizer = [
            arr
            for arr in perm_maps
            if tuple(sorted(arr[x] for x in parent)) == parent
        ]
        remaining = set(range(105)) - parent_set
        extra_reps = []
        while remaining:
            c = min(remaining)
            orbit = {arr[c] for arr in stabilizer}
            remaining.difference_update(orbit)
            extra_reps.append(c)

        for c in extra_reps:
            five = tuple(sorted(parent + (c,)))
            parent_types = [
                orbit_id[rank4(five[:j] + five[j + 1 :])]
                for j in range(5)
            ]
            if oid == min(parent_types):
                candidates.append(five)
    assert len(candidates) == 20475

    P = np.array(perm_maps, dtype=np.uint8)
    S = np.array(candidates, dtype=np.uint8)
    C2n = np.array(C2, dtype=np.int64)
    C3n = np.array(C3, dtype=np.int64)
    C4n = np.array(C4, dtype=np.int64)
    C5n = np.array(C5, dtype=np.int64)
    canonical = []
    stabilizer_sizes = []
    for start in range(0, len(S), 512):
        batch = S[start : start + 512]
        images = np.sort(P[:, batch], axis=2)
        ranks = (
            images[:, :, 0].astype(np.int64)
            + C2n[images[:, :, 1]]
            + C3n[images[:, :, 2]]
            + C4n[images[:, :, 3]]
            + C5n[images[:, :, 4]]
        )
        canonical.extend(np.min(ranks, axis=0).tolist())
        stabilizer_sizes.extend(
            np.sum(np.all(images == batch[None, :, :], axis=2), axis=0).tolist()
        )

    unique = {}
    for i, key in enumerate(canonical):
        if key not in unique:
            unique[key] = i
        else:
            assert stabilizer_sizes[unique[key]] == stabilizer_sizes[i]

    indices = list(unique.values())
    representatives = [candidates[i] for i in indices]
    orbit_sizes = [5040 // stabilizer_sizes[i] for i in indices]
    assert len(representatives) == 20451
    assert sum(orbit_sizes) == comb(105, 5) == 96560646
    return keys, representatives, orbit_sizes, len(candidates)


def relation_rows_zero(ext, touched, states):
    """Integer T-relation rows for zero external constraint space (k=t=5)."""
    rows = []
    for b, state in zip(touched, states):
        if R.STATES[state][2]:
            ids = R.BLOCKS[b]
            rows.append(
                [
                    R.MCOORD[ids[0]][70 + j]
                    - R.MCOORD[ids[1]][70 + j]
                    - R.MCOORD[ids[2]][70 + j]
                    for j in range(15)
                ]
            )

    for e in ext:
        tv = list(R.MCOORD[e][70:])
        for b, state in zip(touched, states):
            vx, vy = R.QCOMP[e][b]
            beta = R.solve_local_coeffs_int(R.STATES[state][0], (-vx, -vy))
            ids = R.BLOCKS[b]
            for local_index, q in enumerate(beta):
                if q:
                    for j in range(15):
                        tv[j] += q * R.MCOORD[ids[local_index]][70 + j]
        rows.append(tv)
    return rows


def singleton_options(ext, b):
    out = tuple(
        state
        for state in (1, 2, 4)
        if R.local_constraint_key(ext, b, state) == ()
    )
    assert len(out) <= 1
    assert R.local_constraint_key(ext, b, 0) != ()
    return out


def min_p_for_q(q, singleton_count):
    use_singletons = min(q, singleton_count)
    return use_singletons + 2 * (q - use_singletons)


def main():
    assert R.lucas_lehmer_127()
    keys, orbits, orbit_sizes, augmentation_candidates = five_no_root_orbits()
    key_to_global = {cycle_key(R.DESC[e]): e for e in R.NO_ROOT}

    max_norm2 = 0
    coarse_defect_census = Counter()
    dangerous_class_census = Counter()
    dangerous = []

    for orbit_index, five in enumerate(orbits):
        ext = tuple(key_to_global[keys[i]] for i in five)
        touched = tuple(
            sorted(
                b
                for b in range(35)
                if any(R.QCOMP[e][b] != (0, 0) for e in ext)
            )
        )
        m = len(touched)
        singleton_data = []
        for pos, b in enumerate(touched):
            opts = singleton_options(ext, b)
            if opts:
                singleton_data.append((pos, opts[0]))
        s = len(singleton_data)

        full_states = (7,) * m
        rows = relation_rows_zero(ext, touched, full_states)
        for row in rows:
            max_norm2 = max(max_norm2, sum(x * x for x in row))
        full_rank = R.rank_mod(rows)

        best = None
        best_qp = []
        for q in range(m + 1):
            p = min_p_for_q(q, s)
            if p > 9:
                continue
            defect_lb = 5 + 3 * (m - q) + p - 3 * full_rank
            if best is None or defect_lb < best:
                best = defect_lb
                best_qp = [(q, p)]
            elif defect_lb == best:
                best_qp.append((q, p))
        assert best is not None
        coarse_defect_census[best] += 1

        if best < 0:
            signature = (m, s, full_rank, best, tuple(best_qp))
            dangerous_class_census[signature] += 1
            dangerous.append(
                (
                    orbit_index,
                    ext,
                    touched,
                    full_rank,
                    tuple(singleton_data),
                    tuple(best_qp),
                )
            )

    assert dict(sorted(coarse_defect_census.items())) == {
        -2: 16,
        -1: 2618,
        1: 576,
        2: 13770,
        4: 247,
        5: 3089,
        7: 36,
        8: 96,
        10: 2,
        13: 1,
    }
    assert dict(dangerous_class_census) == {
        (11, 7, 8, -1, ((8, 9),)): 27,
        (12, 8, 9, -2, ((8, 8),)): 16,
        (13, 9, 9, -1, ((9, 9),)): 226,
        (14, 9, 10, -1, ((9, 9),)): 673,
        (14, 10, 10, -1, ((9, 9),)): 687,
        (15, 10, 11, -1, ((9, 9),)): 270,
        (15, 11, 11, -1, ((9, 9),)): 561,
        (16, 12, 12, -1, ((9, 9),)): 174,
    }
    assert len(dangerous) == 2634

    exact_defect_census = Counter()
    exact_rank_census = Counter()
    dangerous_states = 0
    min_exact_defect = None

    for orbit_index, ext, touched, full_rank, singleton_data, best_qp in dangerous:
        m = len(touched)
        singleton_map = dict(singleton_data)
        singleton_positions = tuple(sorted(singleton_map))

        for q, p in best_qp:
            if p == q:
                state_iter = []
                for singles in combinations(singleton_positions, q):
                    states = [7] * m
                    for pos in singles:
                        states[pos] = singleton_map[pos]
                    state_iter.append(tuple(states))
            else:
                assert (q, p) == (8, 9)
                assert len(singleton_positions) == 7
                singleton_set = set(singleton_positions)
                state_iter = []
                for pair_pos in range(m):
                    if pair_pos in singleton_set:
                        continue
                    for pair_state in (3, 5, 6):
                        states = [7] * m
                        for pos in singleton_positions:
                            states[pos] = singleton_map[pos]
                        states[pair_pos] = pair_state
                        state_iter.append(tuple(states))

            for states in state_iter:
                rows = relation_rows_zero(ext, touched, states)
                for row in rows:
                    max_norm2 = max(max_norm2, sum(x * x for x in row))
                delta = R.rank_mod(rows)
                n = 5 + sum(R.STATES[state][1] for state in states)
                defect = n - 3 * delta
                dangerous_states += 1
                exact_defect_census[defect] += 1
                exact_rank_census[(m, full_rank, delta, q, p)] += 1
                min_exact_defect = (
                    defect
                    if min_exact_defect is None
                    else min(min_exact_defect, defect)
                )
                assert defect >= 0, (
                    orbit_index,
                    defect,
                    delta,
                    ext,
                    touched,
                    states,
                )

    assert dangerous_states == 79944
    assert dict(sorted(exact_defect_census.items())) == {
        8: 60637,
        10: 16,
        11: 19291,
    }
    assert min_exact_defect == 8
    assert dict(sorted(exact_rank_census.items())) == {
        (11, 8, 5, 8, 9): 324,
        (12, 9, 5, 8, 8): 16,
        (13, 9, 5, 9, 9): 28,
        (13, 9, 6, 9, 9): 198,
        (14, 10, 6, 9, 9): 1140,
        (14, 10, 7, 9, 9): 6403,
        (15, 11, 7, 9, 9): 7683,
        (15, 11, 8, 9, 9): 25872,
        (16, 12, 8, 9, 9): 10440,
        (16, 12, 9, 9, 9): 27840,
    }

    B = max(1, max_norm2)
    assert max_norm2 == 24
    assert R.P * R.P > B**15

    print("PASS: five-no-root k=5,p<=9 rank-density branch")
    print("five_no_root_subsets", comb(105, 5))
    print("S7_orbits", len(orbits))
    print("augmentation_candidates", augmentation_candidates)
    print("augmentation_duplicates", augmentation_candidates - len(orbits))
    print("orbit_size_census", dict(sorted(Counter(orbit_sizes).items())))
    print("coarse_defect_census", dict(sorted(coarse_defect_census.items())))
    print("dangerous_orbits", len(dangerous))
    print("dangerous_class_census", dict(sorted(dangerous_class_census.items())))
    print("dangerous_states_exactified", dangerous_states)
    print("exact_defect_census", dict(sorted(exact_defect_census.items())))
    print("min_exact_defect", min_exact_defect)
    print("exact_rank_census", dict(sorted(exact_rank_census.items())))
    print("max_relation_row_norm_squared", max_norm2)
    print("hadamard_exact_rank_bound", R.P * R.P > B**15)


if __name__ == "__main__":
    main()
