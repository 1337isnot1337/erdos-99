#!/usr/bin/env python3
"""Exact corrected closure audit for seven-no-root D=-1,k=3,d=0,p=1.

This verifier fixes a scope gap in the earlier direct six-shadow audit.  The
old direct audit rejected a singleton root block unless it was touched by at
least three of the seven no-root cycles.  Pair-puncturing does not justify
that rejection: after deleting both touching rows, the singleton can become
untouched while the unstripped five-row shadow still has total incomplete-root
cost p=1.

The corrected route needs no touch lower bound.

A hypothetical seven-row state in this branch has a rank-four coefficient
space P_7 and every one- and two-coordinate puncture has rank four.  Its unique
incomplete root row cannot be globally untouched: removing such an inert row
would give the already-closed seven-no-root D=-2,k=3,d=0,p=0 branch.  Hence the
singleton is touched at least once.  There is always some pair of no-root rows
whose deletion leaves it touched: for touch size at most five delete two
non-touching rows, while for touch size six or seven every pair leaves a touch.
That five-row shadow has D=3,k=1,d=0,p=1 and a touched singleton.

Stage ``five`` enumerates the canonical d=0 five-row p=1 states with the
committed exact-rational coefficient-space code, forms the one external
T-relation exactly, and retains precisely defect D=3 states.  Stages ``six``
and ``seven`` add arbitrary no-root rows without any singleton-touch filter.
The final stage enforces the required rank-four projection after all 21 pair
deletions.

Complete-block and external T ranks use the established 2^127-1
Lucas-Lehmer/Hadamard certificate.  Coefficient-space ranks are the exact
rational operations inherited from the committed D=-2 verifier.
"""

from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import contextlib
import importlib.util
import io
import pickle
import time

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_seven_noroot_k3_dminus1_2026_09_20.py"
spec = importlib.util.spec_from_file_location("seven_k3_dminus1_lowtouch_base", BASE)
V = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(V)

R = V.R
B = V.B
K = V.K

COMPLETE_T = tuple(
    tuple(
        R.MCOORD[ids[0]][70 + j]
        - R.MCOORD[ids[1]][70 + j]
        - R.MCOORD[ids[2]][70 + j]
        for j in range(15)
    )
    for ids in R.BLOCKS
)


def total_relation_rows(ext, P, singleton_block, singleton_state, complete, touched):
    """Complete-block rows plus the unique five-row external relation."""
    states = []
    complete_set = set(complete)
    for block in touched:
        if block == singleton_block:
            states.append(singleton_state)
        elif block in complete_set:
            states.append(7)
        else:
            states.append(0)

    rows = [COMPLETE_T[block] for block in complete]
    alphas = R.nullspace_int(P, 5)
    assert len(alphas) == 1
    alpha = alphas[0]
    tv = [
        sum(alpha[i] * R.MCOORD[e][70 + j] for i, e in enumerate(ext))
        for j in range(15)
    ]
    for block, state in zip(touched, states):
        vx = sum(alpha[i] * R.QCOMP[e][block][0] for i, e in enumerate(ext))
        vy = sum(alpha[i] * R.QCOMP[e][block][1] for i, e in enumerate(ext))
        beta = R.solve_local_coeffs_int(R.STATES[state][0], (-vx, -vy))
        ids = R.BLOCKS[block]
        for local_index, coeff in enumerate(beta):
            if not coeff:
                continue
            for j in range(15):
                tv[j] += coeff * R.MCOORD[ids[local_index]][70 + j]
    rows.append(tuple(tv))
    return tuple(rows)


def scan_five_exact(start, end):
    """Filter committed canonical d=0 parents to the exact D=3 boundary."""
    base = V.scan_five(start, end)
    defect_census = Counter()
    parents = []
    max_relation_norm2 = 0
    t0 = time.time()
    for parent in base["parents"]:
        oi, local, ext, P, sb, ss, complete, touched = parent
        rows = total_relation_rows(ext, P, sb, ss, complete, touched)
        for row in rows:
            max_relation_norm2 = max(max_relation_norm2, sum(x * x for x in row))
        rank = R.rank_mod(rows)
        c = len(complete)
        defect = 6 + 3 * c - 3 * rank
        assert defect in (3, 6), (oi, defect, ext, sb, ss, complete)
        defect_census[defect] += 1
        if defect == 3:
            parents.append(parent)
    return {
        "range": (start, end),
        "canonical_d0_states": len(base["parents"]),
        "defect_census": defect_census,
        "parents": tuple(parents),
        "max_relation_norm2": max_relation_norm2,
        "seconds": base["seconds"] + (time.time() - t0),
    }


def scan_six_complete(five_parents):
    """Extend exact D=3 parents once, with no singleton-touch rejection."""
    deficiency = B.DeficiencyCache()
    counts = Counter()
    raw = []
    max_spaces = 0
    max_eligible = 0
    touch_dist = Counter()
    t0 = time.time()
    for _oi, _local, ext5, P5, sb, ss, _C5, _T5 in five_parents:
        for extra in R.NO_ROOT:
            if extra in ext5:
                continue
            ext6 = tuple(ext5) + (extra,)
            counts["extensions"] += 1
            cand, nspaces, neligible = V.extend_parent(
                ext6, P5, sb, ss, 6, deficiency
            )
            max_spaces = max(max_spaces, nspaces)
            max_eligible = max(max_eligible, neligible)
            counts["raw_candidates"] += len(cand)
            for P6, C6, T6 in cand:
                sext = tuple(sorted(ext6))
                normalized = B.permute_space(P6, ext6, sext)
                raw.append((sext, normalized, sb, ss, C6, T6))
                touch_dist[V.singleton_touch_count(sext, sb)] += 1
    unique = {(x[0], x[1], x[2], x[3]): x for x in raw}
    counts["duplicates"] = len(raw) - len(unique)
    return {
        "parents": tuple(unique.values()),
        "counts": counts,
        "max_spaces": max_spaces,
        "max_eligible": max_eligible,
        "deficiency_cache_size": len(deficiency.cache),
        "singleton_touch_dist_raw": touch_dist,
        "seconds": time.time() - t0,
    }


def scan_seven_complete(six_parents):
    """Extend once more and enforce all 21 pair-puncture rank conditions."""
    deficiency = B.DeficiencyCache()
    counts = Counter()
    min_pair_rank = Counter()
    bad_pair_count = Counter()
    touch_dist = Counter()
    survivors = []
    seen = set()
    max_spaces = 0
    max_eligible = 0
    t0 = time.time()
    for ext6, P6, sb, ss, _C6, _T6 in six_parents:
        assert tuple(ext6) == tuple(sorted(ext6))
        for extra in R.NO_ROOT:
            if extra in ext6:
                continue
            ext7 = tuple(ext6) + (extra,)
            counts["extensions"] += 1
            cand, nspaces, neligible = V.extend_parent(
                ext7, P6, sb, ss, 7, deficiency
            )
            max_spaces = max(max_spaces, nspaces)
            max_eligible = max(max_eligible, neligible)
            counts["single_deletion_synchronized_candidates"] += len(cand)
            for P7, C7, T7 in cand:
                sevent = tuple(sorted(ext7))
                normalized = B.permute_space(P7, ext7, sevent)
                signature = (sevent, normalized, sb, ss)
                if signature in seen:
                    counts["duplicates"] += 1
                    continue
                seen.add(signature)
                touch_dist[V.singleton_touch_count(sevent, sb)] += 1
                ranks = [
                    len(B.project_space(normalized, (i, j)))
                    for i in range(7)
                    for j in range(i + 1, 7)
                ]
                minimum = min(ranks)
                bad = sum(rank < 4 for rank in ranks)
                min_pair_rank[minimum] += 1
                bad_pair_count[bad] += 1
                if bad == 0:
                    survivors.append((sevent, normalized, sb, ss, C7, T7))
    return {
        "counts": counts,
        "unique_candidates": len(seen),
        "min_pair_rank": min_pair_rank,
        "bad_pair_count": bad_pair_count,
        "singleton_touch_dist": touch_dist,
        "survivors": tuple(survivors),
        "max_spaces": max_spaces,
        "max_eligible": max_eligible,
        "deficiency_cache_size": len(deficiency.cache),
        "seconds": time.time() - t0,
    }


def save(path, value):
    with open(path, "wb") as f:
        pickle.dump(value, f, protocol=pickle.HIGHEST_PROTOCOL)


def load(path):
    with open(path, "rb") as f:
        return pickle.load(f)


def merge_five(paths):
    shards = [load(path) for path in paths]
    shards.sort(key=lambda s: s["range"])
    assert shards
    assert shards[0]["range"][0] == 0
    assert shards[-1]["range"][1] == 20451
    for left, right in zip(shards, shards[1:]):
        assert left["range"][1] == right["range"][0]

    parents = []
    defects = Counter()
    canonical_d0_states = 0
    max_relation_norm2 = 0
    for shard in shards:
        parents.extend(shard["parents"])
        defects.update(shard["defect_census"])
        canonical_d0_states += shard["canonical_d0_states"]
        max_relation_norm2 = max(max_relation_norm2, shard["max_relation_norm2"])

    result = {
        "range": (0, 20451),
        "parents": tuple(parents),
        "canonical_d0_states": canonical_d0_states,
        "defect_census": defects,
        "max_relation_norm2": max_relation_norm2,
    }
    assert canonical_d0_states == 639484
    assert dict(sorted(defects.items())) == {3: 1030, 6: 638454}
    assert len(parents) == 1030
    assert len({(p[0], p[3], p[4], p[5]) for p in parents}) == 1030
    assert max_relation_norm2 == 84
    return result


def main():
    ap = ArgumentParser()
    sub = ap.add_subparsers(dest="stage", required=True)

    p = sub.add_parser("five")
    p.add_argument("--part", type=int, default=0)
    p.add_argument("--parts", type=int, default=1)
    p.add_argument("--output", required=True)

    p = sub.add_parser("merge-five")
    p.add_argument("--inputs", nargs="+", required=True)
    p.add_argument("--output", required=True)

    p = sub.add_parser("six")
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)

    p = sub.add_parser("seven")
    p.add_argument("--input", required=True)
    p.add_argument("--output")

    args = ap.parse_args()

    assert R.lucas_lehmer_127()
    max_complete_norm2 = max(sum(x * x for x in row) for row in COMPLETE_T)
    assert max_complete_norm2 == 12
    assert R.P * R.P > max_complete_norm2 ** 15

    if args.stage == "five":
        assert args.parts >= 1 and 0 <= args.part < args.parts
        n = 20451
        start = n * args.part // args.parts
        end = n * (args.part + 1) // args.parts
        result = scan_five_exact(start, end)
        assert R.P * R.P > max(1, result["max_relation_norm2"]) ** 15
        save(args.output, result)
        print("PASS: exact five-row D=3,k=1,d=0,p=1 shard")
        print("orbit_range", start, end)
        print("canonical_d0_states", result["canonical_d0_states"])
        print("defect_census", dict(sorted(result["defect_census"].items())))
        print("D3_parents", len(result["parents"]))
        print("max_relation_row_norm_squared", result["max_relation_norm2"])
        print("seconds", round(result["seconds"], 3))
        return

    if args.stage == "merge-five":
        result = merge_five(args.inputs)
        assert R.P * R.P > result["max_relation_norm2"] ** 15
        save(args.output, result)
        print("PASS: merged exact five-row D=3 boundary")
        print("canonical_d0_states", result["canonical_d0_states"])
        print("defect_census", dict(sorted(result["defect_census"].items())))
        print("D3_parents", len(result["parents"]))
        print("max_relation_row_norm_squared", result["max_relation_norm2"])
        return

    if args.stage == "six":
        five = load(args.input)
        parents = tuple(five["parents"] if isinstance(five, dict) else five)
        assert len(parents) == 1030
        result = scan_six_complete(parents)
        assert dict(result["counts"]) == {
            "extensions": 103000,
            "raw_candidates": 817,
            "duplicates": 112,
        }
        assert len(result["parents"]) == 705
        assert len({x[0] for x in result["parents"]}) == 267
        assert dict(sorted(result["singleton_touch_dist_raw"].items())) == {
            1: 106, 2: 78, 3: 430, 4: 191, 5: 9, 6: 3,
        }
        assert result["max_spaces"] == 43
        assert result["max_eligible"] == 13
        save(args.output, result)
        print("PASS: corrected synchronized six-row extension")
        print("five_D3_parents", len(parents))
        print("counts", dict(result["counts"]))
        print("normalized_six_states", len(result["parents"]))
        print("six_cycle_sets", len({x[0] for x in result["parents"]}))
        print("singleton_touch_census_raw", dict(sorted(result["singleton_touch_dist_raw"].items())))
        print("max_intermediate_spaces", result["max_spaces"])
        print("max_eligible_blocks", result["max_eligible"])
        print("complete_rank_cache_size", result["deficiency_cache_size"])
        print("seconds", round(result["seconds"], 3))
        return

    if args.stage == "seven":
        six = load(args.input)
        parents = tuple(six["parents"] if isinstance(six, dict) else six)
        assert len(parents) == 705
        result = scan_seven_complete(parents)
        assert dict(result["counts"]) == {
            "extensions": 69795,
            "single_deletion_synchronized_candidates": 908,
            "duplicates": 86,
        }
        assert result["unique_candidates"] == 822
        assert dict(sorted(result["min_pair_rank"].items())) == {3: 822}
        assert dict(sorted(result["bad_pair_count"].items())) == {
            1: 24, 2: 33, 4: 406, 6: 354, 7: 5,
        }
        assert dict(sorted(result["singleton_touch_dist"].items())) == {
            1: 7, 3: 388, 4: 405, 6: 16, 7: 6,
        }
        assert not result["survivors"]
        assert result["max_spaces"] == 43
        assert result["max_eligible"] == 10
        summary = {
            "six_parent_states": len(parents),
            "counts": dict(result["counts"]),
            "unique_candidates": result["unique_candidates"],
            "minimum_pair_projection_rank_census": dict(sorted(result["min_pair_rank"].items())),
            "bad_pair_count_census": dict(sorted(result["bad_pair_count"].items())),
            "singleton_touch_census": dict(sorted(result["singleton_touch_dist"].items())),
            "depth_two_survivors": len(result["survivors"]),
            "max_intermediate_spaces": result["max_spaces"],
            "max_eligible_blocks": result["max_eligible"],
            "complete_rank_cache_size": result["deficiency_cache_size"],
            "seconds": round(result["seconds"], 3),
        }
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                for key, value in summary.items():
                    f.write(f"{key} {value}\n")
        print("PASS: corrected seven-row D=-1,k=3,d=0,p=1 branch has no synchronized extension")
        for key, value in summary.items():
            print(key, value)
        return


if __name__ == "__main__":
    main()
