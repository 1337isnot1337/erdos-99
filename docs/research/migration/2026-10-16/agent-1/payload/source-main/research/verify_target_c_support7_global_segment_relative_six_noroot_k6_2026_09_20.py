#!/usr/bin/env python3
"""Exact closure of the t=6,k=6 Target-C four-cycle density branch.

The preceding deletion-shadow synchronization theorem reduces a hypothetical
six-no-root counterexample with k=6 to p=10 (defect -2) or p=11 (defect -1).
For k=6 the external coefficient-constraint space is zero, so every touched
block is complete, a pair, or a singleton whose six local external components
all lie on that singleton direction. Empty touched blocks are impossible.
The synchronization theorem also forces every nonempty incomplete block to be
touched by at least two of the six no-root cycles.

This verifier covers every S7 orbit of six no-root cycles without constructing
the full 325,911-orbit canonical list. It first constructs a 20,475-element
augmentation cover of the 20,451 five-cycle orbits. Extending every cover
member by each of the other 100 no-root cycles covers every six-cycle orbit.
Literal duplicate six-sets are discarded only after the k=6 local prefilter.

For each surviving six-set, every touched block is then completed. The resulting
superfamily F contains every admissible k=6 state A, so

    delta(A) <= delta(F).

The relation rows for F are ranked modulo P=2^127-1. A Lucas-Lehmer check and
an explicit Hadamard bound certify that these modular ranks equal rational
ranks. The resulting all-complete bound has minimum defect 7 at p=10 and 8 at
p=11. Hence neither synchronized k=6 boundary can contain a counterexample.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py"
spec = importlib.util.spec_from_file_location("relative_four_noroot_k2_for_t6_k6", BASE)
R = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(R)


def cycle_key(desc):
    d = list(desc)
    return tuple(
        sorted(tuple(sorted((d[i], d[(i + 1) % 4]))) for i in range(4))
    )


def five_cover_candidates():
    """Return an S7-cover of five-subsets, not a duplicate-free orbit list.

    Four-subset orbits are enumerated exactly. For each four-orbit representative
    we augment by stabilizer orbits and keep augmentations whose parent orbit is
    minimal among the five deletions. Every five-subset orbit has such a minimal
    parent, so the resulting 20,475 candidates cover all five-subset orbits.
    The 24 duplicate orbit representatives are harmless here and deliberately
    avoid the more expensive final canonicalization used by the t=5 verifier.
    """
    keys = sorted(cycle_key(R.DESC[e]) for e in R.NO_ROOT)
    key_to_local = {key: i for i, key in enumerate(keys)}

    perm_maps = []
    for perm in permutations(range(1, 8)):
        pmap = {i + 1: perm[i] for i in range(7)}
        arr = []
        for key in keys:
            mapped = tuple(
                sorted(tuple(sorted((pmap[a], pmap[b]))) for a, b in key)
            )
            arr.append(key_to_local[mapped])
        perm_maps.append(tuple(arr))
    assert len(perm_maps) == 5040

    C2 = [comb(i, 2) for i in range(106)]
    C3 = [comb(i, 3) for i in range(106)]
    C4 = [comb(i, 4) for i in range(106)]

    def rank4(t):
        a, b, c, d = t
        return a + C2[b] + C3[c] + C4[d]

    seen = bytearray(comb(105, 4))
    orbit_id = [-1] * len(seen)
    four_reps = []
    for t in combinations(range(105), 4):
        rt = rank4(t)
        if seen[rt]:
            continue
        orbit = {
            tuple(sorted(arr[i] for i in t))
            for arr in perm_maps
        }
        oid = len(four_reps)
        for u in orbit:
            ru = rank4(u)
            seen[ru] = 1
            orbit_id[ru] = oid
        four_reps.append(t)
    assert len(four_reps) == 1186
    assert all(x >= 0 for x in orbit_id)

    five = []
    for oid, parent in enumerate(four_reps):
        stabilizer = [
            arr
            for arr in perm_maps
            if tuple(sorted(arr[x] for x in parent)) == parent
        ]
        remaining = set(range(105)) - set(parent)
        while remaining:
            x = min(remaining)
            orbit = {arr[x] for arr in stabilizer}
            remaining.difference_update(orbit)
            child = tuple(sorted(parent + (x,)))
            parent_types = [
                orbit_id[rank4(child[:j] + child[j + 1 :])]
                for j in range(5)
            ]
            if oid == min(parent_types):
                five.append(child)

    assert len(five) == 20475
    return keys, five


def line_index(v):
    """Project a nonzero local quotient vector to one of the three root lines."""
    x, y = v
    if x == 0:
        assert y != 0
        return 1
    if y == 0:
        return 0
    assert x == -y
    return 2


def complete_block_row(b):
    ids = R.BLOCKS[b]
    return [
        R.MCOORD[ids[0]][70 + j]
        - R.MCOORD[ids[1]][70 + j]
        - R.MCOORD[ids[2]][70 + j]
        for j in range(15)
    ]


HROWS = [complete_block_row(b) for b in range(35)]


def all_complete_rows(ext, touched):
    """T-relation rows for the superfamily with every touched block complete."""
    rows = [HROWS[b] for b in touched]
    for e in ext:
        tv = list(R.MCOORD[e][70:])
        for b in touched:
            vx, vy = R.QCOMP[e][b]
            beta = R.solve_local_coeffs_int(7, (-vx, -vy))
            ids = R.BLOCKS[b]
            for local_index, q in enumerate(beta):
                if not q:
                    continue
                tr = R.MCOORD[ids[local_index]][70:]
                for j in range(15):
                    tv[j] += q * tr[j]
        rows.append(tv)
    return rows


def profile(ext, info):
    count = [0] * 35
    dirs = [0] * 35
    for e in ext:
        for b, d in info[e]:
            count[b] += 1
            dirs[b] |= 1 << d
    touched = tuple(b for b, n in enumerate(count) if n)
    shared = sum(count[b] >= 2 for b in touched)
    singleton = sum(
        count[b] >= 2 and dirs[b] & (dirs[b] - 1) == 0
        for b in touched
    )
    return touched, shared, singleton


def q_options(U, shared, singleton, p):
    """Possible (incomplete blocks, singleton blocks, complete blocks)."""
    out = []
    for q in range((p + 1) // 2, p + 1):
        s = 2 * q - p
        if q <= shared and s <= singleton:
            out.append((q, s, U - q))
    return tuple(out)


def main():
    assert R.lucas_lehmer_127()

    keys, parents = five_cover_candidates()
    key_to_global = {cycle_key(R.DESC[e]): e for e in R.NO_ROOT}
    local_to_global = tuple(key_to_global[key] for key in keys)

    # Each no-root cycle touches four quotient blocks. Record only the block and
    # projective local direction needed for the k=6 singleton compatibility test.
    info = []
    for e in local_to_global:
        data = []
        for b, v in enumerate(R.QCOMP[e]):
            if v != (0, 0):
                data.append((b, line_index(v)))
        assert len(data) == 4
        info.append(tuple(data))

    raw_extensions = 0
    eligible = set()
    admit10 = set()
    admit11 = set()

    # Increment each five-parent profile by one cycle rather than rebuilding all
    # 24 support incidences for every one of the 2,047,500 raw extensions.
    for parent in parents:
        parent_set = set(parent)
        count = [0] * 35
        dirs = [0] * 35
        for e in parent:
            for b, d in info[e]:
                count[b] += 1
                dirs[b] |= 1 << d

        U0 = sum(n > 0 for n in count)
        shared0 = sum(n >= 2 for n in count)
        singleton0 = sum(
            n >= 2 and dirs[b] & (dirs[b] - 1) == 0
            for b, n in enumerate(count)
        )

        for x in range(105):
            if x in parent_set:
                continue
            raw_extensions += 1
            U = U0
            shared = shared0
            singleton = singleton0
            for b, d in info[x]:
                n = count[b]
                mask = dirs[b]
                old_single = n >= 2 and mask & (mask - 1) == 0
                nn = n + 1
                newmask = mask | (1 << d)
                new_single = nn >= 2 and newmask & (newmask - 1) == 0
                if n == 0:
                    U += 1
                if n == 1:
                    shared += 1
                singleton += int(new_single) - int(old_single)

            ext = tuple(sorted(parent + (x,)))

            # For c>=10, the ambient 15-dimensional T bound already gives
            # D>=6+3c+p-45 >= 1 at p=10, so only c<=9 can threaten k=6.
            opt10 = tuple(
                opt for opt in q_options(U, shared, singleton, 10)
                if opt[2] <= 9
            )
            opt11 = tuple(
                opt for opt in q_options(U, shared, singleton, 11)
                if opt[2] <= 9
            )
            if opt10 or opt11:
                eligible.add(ext)
                if opt10:
                    admit10.add(ext)
                if opt11:
                    admit11.add(ext)

    assert raw_extensions == 2047500
    assert len(eligible) == 68780
    assert len(admit10) == 46849
    assert len(admit11) == 46792

    rank_census = Counter()
    defect_census = {10: Counter(), 11: Counter()}
    minima = {10: None, 11: None}
    max_norm2 = 0

    for ext_local in eligible:
        ext = tuple(local_to_global[i] for i in ext_local)
        touched, shared, singleton = profile(ext_local, info)
        rows = all_complete_rows(ext, touched)
        for row in rows:
            max_norm2 = max(max_norm2, sum(x * x for x in row))
        full_rank = R.rank_mod(rows)
        rank_census[full_rank] += 1

        U = len(touched)
        for p in (10, 11):
            for _q, _s, c in q_options(U, shared, singleton, p):
                lower = 6 + 3 * c + p - 3 * full_rank
                defect_census[p][lower] += 1
                minima[p] = (
                    lower if minima[p] is None else min(minima[p], lower)
                )

    assert dict(sorted(rank_census.items())) == {
        5: 1,
        6: 243,
        7: 154,
        8: 6171,
        9: 20079,
        10: 40256,
        11: 1876,
    }
    assert dict(sorted(defect_census[10].items())) == {
        7: 92,
        10: 2123,
        13: 37230,
        16: 45082,
        19: 11731,
        22: 326,
    }
    assert dict(sorted(defect_census[11].items())) == {
        8: 374,
        11: 8073,
        14: 39799,
        17: 11731,
        20: 326,
    }
    assert minima == {10: 7, 11: 8}
    assert max_norm2 == 12
    assert R.P * R.P > 12 ** 15

    print("PASS: six-no-root k=6 synchronized boundary branch")
    print("five_cover_candidates", len(parents))
    print("raw_six_extensions", raw_extensions)
    print("eligible_unique_six_sets", len(eligible))
    print("eligible_p10", len(admit10))
    print("eligible_p11", len(admit11))
    print("all_complete_rank_census", dict(sorted(rank_census.items())))
    print("p10_coarse_defect_census", dict(sorted(defect_census[10].items())))
    print("p11_coarse_defect_census", dict(sorted(defect_census[11].items())))
    print("min_p10_coarse_defect", minima[10])
    print("min_p11_coarse_defect", minima[11])
    print("max_relation_row_norm_squared", max_norm2)
    print("hadamard_exact_rank_bound", R.P * R.P > 12 ** 15)


if __name__ == "__main__":
    main()
