#!/usr/bin/env python3
"""Exact five-no-root k=2,p=1 slack theorem for Target C.

For five no-root four-cycles and k=2, the global coefficient-constraint
space P has rank 3. If p=1 then exactly one touched root-0 quotient block is
a singleton and every other incomplete touched block is empty. For fixed P
and fixed singleton choice, the canonical least-row realization keeps every
other compatible block empty and completes the rest. Any other realization
with the same data is obtained by completing some canonical-empty blocks, and
each such completion adds three rows while increasing the relative T-rank by
at most one. Hence the defect D=|A|-3*delta(A) cannot decrease away from the
canonical state.

This verifier enumerates every realizable canonical rank-3 P with one
singleton over the exact 20,451 S7 orbit representatives of five no-root
cycles. A small prime field is used only to canonicalize coefficient spaces;
a Hadamard bound proves those rank/span decisions agree with Q. Complete T
ranks and the residual d=0 states are reranked with the repository's existing
2^127-1 exact-rank certificate.

Full census:
  canonical p=1 states       8,590,316
  complete deficiency d=0       3,492
  d=1                        2,325,470
  d=2                        6,239,198
  d=3                           22,040
  d=4                              108
  d=5                                8

All 3,492 d=0 states have total relation rank exactly c, where c is the
number of complete blocks, and therefore D=6. For d>=1 the general bound
D>=3d applies. Thus every five-no-root k=2,p=1 family has D>=3.
"""
from argparse import ArgumentParser
from collections import Counter
from functools import lru_cache
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py"
K5 = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k5_2026_09_20.py"

spec = importlib.util.spec_from_file_location("five_k2_p1_base", BASE)
R = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(R)

spec = importlib.util.spec_from_file_location("five_k2_p1_orbits", K5)
K = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(K)

COMPLETE_T = tuple(
    tuple(
        R.MCOORD[ids[0]][70 + j]
        - R.MCOORD[ids[1]][70 + j]
        - R.MCOORD[ids[2]][70 + j]
        for j in range(15)
    )
    for ids in R.BLOCKS
)

# M_31 = 2^31-1 is ample for the length-five local coefficient rows.
SMALL_P = (1 << 31) - 1


def lucas_lehmer_mersenne(exponent):
    m = (1 << exponent) - 1
    s = 4
    for _ in range(exponent - 2):
        s = (s * s - 2) % m
    return s == 0


def rref_small(rows):
    basis = {}
    for row in rows:
        v = [int(x) % SMALL_P for x in row]
        for pivot in sorted(basis):
            if v[pivot]:
                q = v[pivot]
                br = basis[pivot]
                v = [(x - q * y) % SMALL_P for x, y in zip(v, br)]
        pivot = next((j for j, x in enumerate(v) if x), None)
        if pivot is None:
            continue
        inv = pow(v[pivot], SMALL_P - 2, SMALL_P)
        v = [x * inv % SMALL_P for x in v]
        for old in list(basis):
            if basis[old][pivot]:
                q = basis[old][pivot]
                basis[old] = tuple(
                    (x - q * y) % SMALL_P for x, y in zip(basis[old], v)
                )
        basis[pivot] = tuple(v)
    return tuple(basis[p] for p in sorted(basis))


@lru_cache(maxsize=1_000_000)
def union_small(a, b):
    return rref_small(a + b)


def is_subspace_small(a, b):
    return len(union_small(a, b)) == len(b)


def local_keys_small(ext, block):
    vals = [R.QCOMP[e][block] for e in ext]
    empty = rref_small(
        (
            tuple(v[0] for v in vals),
            tuple(v[1] for v in vals),
        )
    )
    singletons = []
    for state in (1, 2, 4):
        lx, ly = R.STATES[state][4]
        singletons.append(
            rref_small((tuple(lx * v[1] - ly * v[0] for v in vals),))
        )
    return empty, tuple(singletons)


def candidate_rank3_spaces(local):
    """All rank-three P realizable with at most one singleton constraint."""
    # Value = minimum number of singleton blocks used in a generating state.
    best = {(): 0}
    for empty, singletons in local.values():
        new = dict(best)  # complete this block
        for space, cost in best.items():
            joined = union_small(space, empty)
            if len(joined) <= 3:
                old = new.get(joined)
                if old is None or cost < old:
                    new[joined] = cost
            if cost == 0:
                for singleton in singletons:
                    joined = union_small(space, singleton)
                    if len(joined) <= 3:
                        old = new.get(joined)
                        if old is None or 1 < old:
                            new[joined] = 1
        best = new
    return tuple(space for space, cost in best.items() if len(space) == 3 and cost <= 1)


def exact_constraint_space(ext, touched, states):
    space = ()
    for block, state in zip(touched, states):
        space = R.union_key(space, R.local_constraint_key(ext, block, state))
    return space


def external_relation_rows(ext, touched, states, exact_space):
    rows = []
    for block, state in zip(touched, states):
        if state == 7:
            rows.append(COMPLETE_T[block])

    alphas = R.nullspace_int(exact_space, 5)
    assert len(alphas) == 2
    for alpha in alphas:
        tv = [
            sum(alpha[i] * R.MCOORD[e][70 + j] for i, e in enumerate(ext))
            for j in range(15)
        ]
        for block, state in zip(touched, states):
            vx = sum(alpha[i] * R.QCOMP[e][block][0] for i, e in enumerate(ext))
            vy = sum(alpha[i] * R.QCOMP[e][block][1] for i, e in enumerate(ext))
            beta = R.solve_local_coeffs_int(R.STATES[state][0], (-vx, -vy))
            ids = R.BLOCKS[block]
            for local_index, q in enumerate(beta):
                if q:
                    for j in range(15):
                        tv[j] += q * R.MCOORD[ids[local_index]][70 + j]
        rows.append(tuple(tv))
    return tuple(rows)


def scan(keys, orbits, start, stop):
    key_to_global = {K.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}
    complete_rank_cache = {}
    counts = Counter()
    deficiency_census = Counter()
    complete_count_census = Counter()
    exact_defect_census = Counter()
    exact_rank_census = Counter()
    max_relation_norm2 = 0
    first_failure = None
    max_spaces = 0

    for orbit_index in range(start, stop):
        ext = tuple(key_to_global[keys[i]] for i in orbits[orbit_index])
        touched = tuple(
            b
            for b in range(35)
            if any(R.QCOMP[e][b] != (0, 0) for e in ext)
        )
        local = {b: local_keys_small(ext, b) for b in touched}
        spaces = candidate_rank3_spaces(local)
        counts["coefficient_spaces"] += len(spaces)
        max_spaces = max(max_spaces, len(spaces))
        seen = set()

        for space in spaces:
            for singleton_block in touched:
                for singleton_state, singleton_key in zip(
                    (1, 2, 4), local[singleton_block][1]
                ):
                    if not is_subspace_small(singleton_key, space):
                        continue

                    states = []
                    generated = ()
                    for block in touched:
                        if block == singleton_block:
                            state = singleton_state
                            key = singleton_key
                        else:
                            empty = local[block][0]
                            if is_subspace_small(empty, space):
                                state = 0
                                key = empty
                            else:
                                state = 7
                                key = ()
                        states.append(state)
                        generated = union_small(generated, key)
                    if generated != space:
                        continue

                    states = tuple(states)
                    signature = (space, singleton_block, singleton_state, states)
                    if signature in seen:
                        continue
                    seen.add(signature)
                    counts["canonical_p1_states"] += 1

                    complete = tuple(
                        block for block, state in zip(touched, states) if state == 7
                    )
                    c = len(complete)
                    complete_count_census[c] += 1
                    rank = complete_rank_cache.get(complete)
                    if rank is None:
                        rank = R.rank_mod([COMPLETE_T[b] for b in complete])
                        complete_rank_cache[complete] = rank
                    deficiency = c - rank
                    deficiency_census[deficiency] += 1

                    if deficiency >= 1:
                        # rank(all T relations) <= (c-d)+2, so D>=3d.
                        continue

                    # Only d=0 states need exact external-relation reranking.
                    exact_space = exact_constraint_space(ext, touched, states)
                    if len(exact_space) != 3:
                        first_failure = (
                            "coefficient-rank mismatch",
                            orbit_index,
                            ext,
                            touched,
                            singleton_block,
                            singleton_state,
                            states,
                            exact_space,
                        )
                        break
                    rows = external_relation_rows(ext, touched, states, exact_space)
                    for row in rows:
                        max_relation_norm2 = max(
                            max_relation_norm2, sum(x * x for x in row)
                        )
                    total_rank = R.rank_mod(rows)
                    defect = 6 + 3 * c - 3 * total_rank
                    exact_defect_census[defect] += 1
                    exact_rank_census[(c, rank, total_rank)] += 1
                    if defect < 3:
                        first_failure = (
                            "defect below theorem",
                            orbit_index,
                            defect,
                            ext,
                            touched,
                            singleton_block,
                            singleton_state,
                            exact_space,
                            states,
                            complete,
                            total_rank,
                        )
                        break
                if first_failure is not None:
                    break
            if first_failure is not None:
                break
        if first_failure is not None:
            break

    return {
        "coefficient_spaces": counts["coefficient_spaces"],
        "canonical_p1_states": counts["canonical_p1_states"],
        "deficiency_census": deficiency_census,
        "complete_count_census": complete_count_census,
        "exact_defect_census": exact_defect_census,
        "exact_rank_census": exact_rank_census,
        "max_relation_norm2": max_relation_norm2,
        "complete_rank_cache_size": len(complete_rank_cache),
        "max_spaces_per_orbit": max_spaces,
        "first_failure": first_failure,
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--orbit-start", type=int, default=0)
    parser.add_argument("--orbit-end", type=int)
    args = parser.parse_args()

    assert lucas_lehmer_mersenne(31)
    assert R.lucas_lehmer_127()

    # Raw coefficient rows have length five. Empty rows have entries <=1;
    # singleton rows are 2x2 determinants against LOCAL and have entries <=2.
    assert R.LOCAL == ((1, 0), (0, 1), (1, -1))
    max_q_component = max(
        abs(x) for e in R.NO_ROOT for pair in R.QCOMP[e] for x in pair
    )
    assert max_q_component == 1
    max_local_row_norm2 = 5 * 2 * 2
    assert SMALL_P * SMALL_P > max_local_row_norm2 ** 5

    keys, orbits, orbit_sizes, augmentation_candidates = K.five_no_root_orbits()
    end = len(orbits) if args.orbit_end is None else args.orbit_end
    assert 0 <= args.orbit_start <= end <= len(orbits)

    result = scan(keys, orbits, args.orbit_start, end)
    assert result["first_failure"] is None, result["first_failure"]

    max_complete_norm2 = max(sum(x * x for x in row) for row in COMPLETE_T)
    t_bound = max(max_complete_norm2, result["max_relation_norm2"])
    assert R.P * R.P > max(1, t_bound) ** 15

    if args.orbit_start == 0 and end == len(orbits):
        assert len(orbits) == 20451
        assert sum(orbit_sizes) == 96560646
        assert augmentation_candidates == 20475
        assert result["coefficient_spaces"] == 503112
        assert result["canonical_p1_states"] == 8590316
        assert dict(sorted(result["deficiency_census"].items())) == {
            0: 3492,
            1: 2325470,
            2: 6239198,
            3: 22040,
            4: 108,
            5: 8,
        }
        assert dict(sorted(result["exact_defect_census"].items())) == {6: 3492}
        assert dict(sorted(result["exact_rank_census"].items())) == {
            (3, 3, 3): 840,
            (5, 5, 5): 698,
            (6, 6, 6): 1616,
            (7, 7, 7): 90,
            (8, 8, 8): 248,
        }
        assert result["max_relation_norm2"] == 44
        assert result["max_spaces_per_orbit"] == 75

    print("PASS: five-no-root k=2,p=1 has defect at least 3")
    print("five_no_root_subsets", 96560646)
    print("S7_orbits", len(orbits))
    print("orbit_range", args.orbit_start, end)
    print("coefficient_spaces", result["coefficient_spaces"])
    print("canonical_p1_states", result["canonical_p1_states"])
    print(
        "complete_rank_deficiency_census",
        dict(sorted(result["deficiency_census"].items())),
    )
    print("exact_defect_census", dict(sorted(result["exact_defect_census"].items())))
    print("exact_rank_census", dict(sorted(result["exact_rank_census"].items())))
    print("max_spaces_per_orbit", result["max_spaces_per_orbit"])
    print("max_local_coefficient_row_norm_squared", max_local_row_norm2)
    print("small_field_exact_rank_bound", SMALL_P * SMALL_P > max_local_row_norm2 ** 5)
    print("max_complete_row_norm_squared", max_complete_norm2)
    print("max_relation_row_norm_squared", result["max_relation_norm2"])
    print("large_field_exact_rank_bound", R.P * R.P > max(1, t_bound) ** 15)
    print("complete_rank_cache_size", result["complete_rank_cache_size"])


if __name__ == "__main__":
    main()
