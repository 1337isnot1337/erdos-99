#!/usr/bin/env python3
"""Exact t=4, k=3 rank-density barrier for the Target-C four-cycle system.

This closes the remaining dangerous p=2,3,4 cases after the companion p<=1
verifier. A deletion-minimal reduction cuts the 56,449,352 canonical p=2..4
states to 6,996,236 states that can still be minimal counterexamples.

For fixed four no-root rows and a rank-one external constraint space P:
* complete touched blocks whose empty constraint lies in P may be emptied;
* an incomplete selected row may be deleted whenever the resulting local
  constraint still lies in P and the global constraint remains P.

Both operations preserve negativity of |A|-3*delta if it was present.
The resulting deletion-minimal states are then checked exactly.

Small T-ranks are computed modulo 2^61-1. Lucas-Lehmer plus an explicit
Hadamard bound makes every modular rank decision exact over Q.
"""
from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import contextlib, importlib.util, io, json

BASE = Path("research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py")
spec = importlib.util.spec_from_file_location("relative_four_noroot_k2_for_k3full", BASE)
R = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(R)

P = (1 << 61) - 1


def lucas_lehmer_61():
    assert all(61 % d for d in range(2, 8))
    s = 4
    for _ in range(59):
        s = (s * s - 2) % P
    return s == 0


def rank_mod(rows, p=P):
    a = [[x % p for x in row] for row in rows]
    r = 0
    n = len(a)
    for c in range(15):
        piv = next((i for i in range(r, n) if a[i][c]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        pv = a[r][c]
        for i in range(r + 1, n):
            q = a[i][c]
            if q:
                a[i] = [(pv * x - q * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == n:
            break
    return r


def candidate_lines(ext, touched):
    out = set()
    for b in touched:
        for state in (0, 1, 2, 4):
            key = R.local_constraint_key(ext, b, state)
            if len(key) == 1:
                out.add(key)
    return tuple(sorted(out, key=repr))


def key_type(ext, b, state, line):
    key = R.local_constraint_key(ext, b, state)
    if not R.is_subspace(key, line):
        return None
    return 1 if key == line else 0


def removal_types(ext, b, state, line):
    out = []
    for j in range(3):
        if (state >> j) & 1:
            smaller = state & ~(1 << j)
            key = R.local_constraint_key(ext, b, smaller)
            if not R.is_subspace(key, line):
                out.append(None)
            else:
                out.append(1 if key == line else 0)
    return tuple(out)


def minimal_options(ext, b, line, sole_realizer):
    """Local options in a deletion-minimal canonical state."""
    empty = R.local_constraint_key(ext, b, 0)
    base = 0 if R.is_subspace(empty, line) else 7
    out = [(base, key_type(ext, b, base, line))]
    for state in range(1, 7):
        kt = key_type(ext, b, state, line)
        if kt is None:
            continue
        rem = removal_types(ext, b, state, line)
        if kt == 1 and sole_realizer:
            if all(x != 1 for x in rem):
                out.append((state, kt))
        else:
            if all(x is None for x in rem):
                out.append((state, kt))
    return tuple(out)


def generate_minimal_states(ext, touched, line):
    """Yield every deletion-minimal p=2,3,4 state with c<=12 exactly once."""
    options = [minimal_options(ext, b, line, False) for b in touched]
    current = [0] * len(touched)

    def rec(q, pcount, complete_count, realizers):
        if pcount > 4 or complete_count > 12:
            return
        if q == len(touched):
            if pcount >= 2 and realizers >= 2:
                yield tuple(current)
            return
        for state, kt in options[q]:
            current[q] = state
            yield from rec(
                q + 1,
                pcount + R.STATES[state][5],
                complete_count + (state == 7),
                min(2, realizers + kt),
            )

    yield from rec(0, 0, 0, 0)

    for sole_index, sole_block in enumerate(touched):
        sole_states = [
            state
            for state, kt in minimal_options(ext, sole_block, line, True)
            if kt == 1
        ]
        if not sole_states:
            continue
        other_options = []
        possible = True
        for q, b in enumerate(touched):
            if q == sole_index:
                other_options.append(None)
                continue
            opts = [
                state
                for state, kt in minimal_options(ext, b, line, False)
                if kt == 0
            ]
            if not opts:
                possible = False
                break
            other_options.append(opts)
        if not possible:
            continue

        for sole_state in sole_states:
            current = [0] * len(touched)
            current[sole_index] = sole_state

            def rec_one(q, pcount, complete_count):
                if pcount > 4 or complete_count > 12:
                    return
                if q == len(touched):
                    if pcount >= 2:
                        yield tuple(current)
                    return
                if q == sole_index:
                    yield from rec_one(
                        q + 1,
                        pcount + R.STATES[sole_state][5],
                        complete_count + (sole_state == 7),
                    )
                else:
                    for state in other_options[q]:
                        current[q] = state
                        yield from rec_one(
                            q + 1,
                            pcount + R.STATES[state][5],
                            complete_count + (state == 7),
                        )

            yield from rec_one(0, 0, 0)


def add_vec(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub_vec(a, b):
    return tuple(x - y for x, y in zip(a, b))


def block_correction(ext, b, state, alpha):
    vx = sum(alpha[i] * R.QCOMP[e][b][0] for i, e in enumerate(ext))
    vy = sum(alpha[i] * R.QCOMP[e][b][1] for i, e in enumerate(ext))
    beta = R.solve_local_coeffs_int(R.STATES[state][0], (-vx, -vy))
    ids = R.BLOCKS[b]
    out = [0] * 15
    for j0, q in enumerate(beta):
        if q:
            tv = R.MCOORD[ids[j0]][70:]
            for jj in range(15):
                out[jj] += q * tv[jj]
    return tuple(out)


COMPLETE_T = []
for ids in R.BLOCKS:
    COMPLETE_T.append(tuple(
        R.MCOORD[ids[0]][70 + j]
        - R.MCOORD[ids[1]][70 + j]
        - R.MCOORD[ids[2]][70 + j]
        for j in range(15)
    ))


def line_data(ext, touched, line):
    alphas = R.nullspace_int(line, 4)
    assert len(alphas) == 3
    base = tuple(
        0 if R.is_subspace(R.local_constraint_key(ext, b, 0), line) else 7
        for b in touched
    )
    ext_base = []
    for alpha in alphas:
        tv = tuple(
            sum(alpha[i] * R.MCOORD[e][70 + j] for i, e in enumerate(ext))
            for j in range(15)
        )
        for b, state in zip(touched, base):
            tv = add_vec(tv, block_correction(ext, b, state, alpha))
        ext_base.append(tv)

    deltas = {}
    for q, (b, base_state) in enumerate(zip(touched, base)):
        for state in range(1, 7):
            if not R.is_subspace(R.local_constraint_key(ext, b, state), line):
                continue
            ds = []
            for alpha in alphas:
                ds.append(sub_vec(
                    block_correction(ext, b, state, alpha),
                    block_correction(ext, b, base_state, alpha),
                ))
            deltas[(q, state)] = tuple(ds)
    return base, tuple(ext_base), deltas


def scan(orbits, start, stop):
    counts = Counter()
    exact_ranked = Counter()
    dependent_complete = Counter()
    min_exact_defect = {2: None, 3: None, 4: None}
    max_relation_norm2 = 0
    max_complete_norm2 = max(sum(x * x for x in row) for row in COMPLETE_T)
    complete_rank_cache = {}
    negatives = []

    for oi in range(start, stop):
        ext, _orbit_size, touched = orbits[oi]
        for line in candidate_lines(ext, touched):
            base, ext_base, deltas = line_data(ext, touched, line)
            for states in generate_minimal_states(ext, touched, line):
                pcount = sum(R.STATES[state][5] for state in states)
                complete_set = tuple(
                    touched[q] for q, state in enumerate(states) if state == 7
                )
                c = len(complete_set)
                counts[pcount] += 1

                r_complete = complete_rank_cache.get(complete_set)
                if r_complete is None:
                    r_complete = rank_mod([COMPLETE_T[b] for b in complete_set])
                    complete_rank_cache[complete_set] = r_complete

                if r_complete < c:
                    dependent_complete[pcount] += 1
                    continue

                ext_rows = [list(row) for row in ext_base]
                for q, state in enumerate(states):
                    if state == base[q]:
                        continue
                    for a, delta_row in enumerate(deltas[(q, state)]):
                        ext_rows[a] = [
                            x + y for x, y in zip(ext_rows[a], delta_row)
                        ]

                rows = [COMPLETE_T[b] for b in complete_set] + ext_rows
                assert len(rows) == c + 3 <= 15
                for row in rows:
                    max_relation_norm2 = max(
                        max_relation_norm2, sum(x * x for x in row)
                    )

                delta = rank_mod(rows)
                defect = 4 + 3 * c + pcount - 3 * delta
                exact_ranked[pcount] += 1
                old = min_exact_defect[pcount]
                min_exact_defect[pcount] = defect if old is None else min(old, defect)
                if defect < 0:
                    negatives.append((
                        oi, pcount, defect, c, delta,
                        ext, touched, line, states,
                    ))
                    return {
                        "counts": counts,
                        "exact_ranked": exact_ranked,
                        "dependent_complete": dependent_complete,
                        "min_exact_defect": min_exact_defect,
                        "negative_states": len(negatives),
                        "first_negative": negatives[0],
                        "max_relation_norm2": max_relation_norm2,
                        "max_complete_norm2": max_complete_norm2,
                        "complete_rank_cache_size": len(complete_rank_cache),
                    }

    return {
        "counts": counts,
        "exact_ranked": exact_ranked,
        "dependent_complete": dependent_complete,
        "min_exact_defect": min_exact_defect,
        "negative_states": 0,
        "first_negative": None,
        "max_relation_norm2": max_relation_norm2,
        "max_complete_norm2": max_complete_norm2,
        "complete_rank_cache_size": len(complete_rank_cache),
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--orbit-start", type=int, default=0)
    parser.add_argument("--orbit-end", type=int)
    parser.add_argument("--json-output")
    args = parser.parse_args()

    assert lucas_lehmer_61()
    orbits = R.four_no_root_orbits()
    end = len(orbits) if args.orbit_end is None else args.orbit_end
    assert 0 <= args.orbit_start <= end <= len(orbits)

    result = scan(orbits, args.orbit_start, end)
    assert result["negative_states"] == 0, result["first_negative"]

    assert P * P > max(1, result["max_complete_norm2"]) ** 15
    assert P * P > max(1, result["max_relation_norm2"]) ** 15

    if args.orbit_start == 0 and end == len(orbits):
        assert dict(result["counts"]) == {
            2: 336759,
            3: 1494744,
            4: 5164733,
        }

    print("PASS: four-no-root k=3,p=2..4 rank-density branch")
    print("four_no_root_subsets", 4_780_230)
    print("S7_orbits", len(orbits))
    print("orbit_range", args.orbit_start, end)
    print("deletion_minimal_states_by_p", dict(sorted(result["counts"].items())))
    print("deletion_minimal_states", sum(result["counts"].values()))
    print("exact_ranked_by_p", dict(sorted(result["exact_ranked"].items())))
    print("complete_dependent_by_p", dict(sorted(result["dependent_complete"].items())))
    print("min_exact_defect_by_p", result["min_exact_defect"])
    print("negative_states", result["negative_states"])
    print("max_complete_row_norm_squared", result["max_complete_norm2"])
    print("max_relation_row_norm_squared", result["max_relation_norm2"])
    print("hadamard_exact_rank_bound", P * P > max(
        max(1, result["max_complete_norm2"]) ** 15,
        max(1, result["max_relation_norm2"]) ** 15,
    ))
    print("complete_rank_cache_size", result["complete_rank_cache_size"])

    if args.json_output:
        payload = {
            k: (dict(v) if isinstance(v, Counter) else v)
            for k, v in result.items()
        }
        Path(args.json_output).write_text(
            json.dumps(payload, sort_keys=True, default=str) + "\n"
        )


if __name__ == "__main__":
    main()
