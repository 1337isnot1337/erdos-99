#!/usr/bin/env python3
"""Deletion-shadow verifier for seven-no-root D=-1,k=3,d=0,p=1.

A hypothetical state in this branch has a rank-four coefficient-constraint
space P_7. The previously proved depth-two synchronization theorem says that
projection after deleting any one or any two external coordinates preserves
rank four. Every five-row pair-deletion shadow therefore has
D=3,k=1,d=0,p=1.

This verifier classifies those five-row shadows, extends them to synchronized
six-row shadows, then extends once more to seven rows and applies the required
pair-deletion rank test. The root configuration is relaxed canonically: one
specified touched block is kept as the unique singleton, every other touched
block whose empty constraint lies in P is made empty, and the remaining
blocks are mandatory complete blocks. Any actual d=0,p=1 state maps to one of
these canonical states because the mandatory complete set is a subset of the
actual complete set. Thus eliminating the canonical extension cover is enough.

Coefficient-space operations are exact rational row-space operations inherited
from the committed seven-no-root D=-2 verifier. Complete-block independence
uses the already certified 2^127-1 modular/Hadamard framework and introduces
no new T-relation row type.
"""
from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import contextlib
import importlib.util
import io
import json
import pickle
import time

HERE = Path(__file__).resolve().parent
RESEARCH = HERE if HERE.name == "research" else HERE / "research"
BASE = RESEARCH / "verify_target_c_support7_global_segment_relative_seven_noroot_k3_dminus2_2026_09_20.py"
spec = importlib.util.spec_from_file_location("seven_noroot_k3_dminus1_base", BASE)
B = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(B)

G = B.G
R = B.R
K = B.K


def singleton_touch_count(ext, block):
    return sum(R.QCOMP[e][block] != (0, 0) for e in ext)


def canonical_complete(ext, touched, P, singleton_block):
    return tuple(
        b
        for b in touched
        if b != singleton_block
        and not R.is_subspace(R.local_constraint_key(ext, b, 0), P)
    )


def canonical_generated(ext, touched, P, singleton_block, singleton_state):
    generated = R.local_constraint_key(ext, singleton_block, singleton_state)
    if not R.is_subspace(generated, P):
        return ()
    for b in touched:
        if b == singleton_block:
            continue
        empty = R.local_constraint_key(ext, b, 0)
        if R.is_subspace(empty, P):
            generated = R.union_key(generated, empty)
    return generated


def candidate_rank4_spaces_p1(ext, touched):
    """All rank-four P realizable using empty constraints and <=1 singleton."""
    # Value: minimum number of singleton blocks needed by a generating state.
    best = {(): 0}
    for b in touched:
        empty = R.local_constraint_key(ext, b, 0)
        singles = {
            R.local_constraint_key(ext, b, state)
            for state in (1, 2, 4)
        }
        new = dict(best)  # complete this block
        for space, cost in best.items():
            joined = R.union_key(space, empty)
            if len(joined) <= 4:
                old = new.get(joined)
                if old is None or cost < old:
                    new[joined] = cost
            if cost == 0:
                for singleton in singles:
                    joined = R.union_key(space, singleton)
                    if len(joined) <= 4:
                        old = new.get(joined)
                        if old is None or 1 < old:
                            new[joined] = 1
        best = new
    return tuple(space for space, cost in best.items() if len(space) == 4 and cost <= 1)


def five_parent_candidates(ext, deficiency):
    touched = B.touched_blocks(ext)
    spaces = candidate_rank4_spaces_p1(ext, touched)
    out = []
    seen = set()
    for P in spaces:
        for singleton_block in touched:
            for singleton_state in (1, 2, 4):
                singleton = R.local_constraint_key(ext, singleton_block, singleton_state)
                if not R.is_subspace(singleton, P):
                    continue
                generated = canonical_generated(
                    ext, touched, P, singleton_block, singleton_state
                )
                if generated != P:
                    continue
                complete = canonical_complete(ext, touched, P, singleton_block)
                if deficiency(complete) != 0:
                    continue
                key = (P, singleton_block, singleton_state)
                if key in seen:
                    continue
                seen.add(key)
                out.append((P, singleton_block, singleton_state, complete, touched))
    return tuple(out), len(spaces)


def scan_five(start, end):
    keys, orbits, orbit_sizes, augmentation_candidates = K.five_no_root_orbits()
    assert len(orbits) == 20451
    assert sum(orbit_sizes) == 96560646
    assert augmentation_candidates == 20475
    assert 0 <= start <= end <= len(orbits)
    key_to_global = {B.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}
    deficiency = B.DeficiencyCache()
    parents = []
    state_dist = Counter()
    space_dist = Counter()
    singleton_touch_dist = Counter()
    max_spaces = 0
    t0 = time.time()
    for oi in range(start, end):
        local = orbits[oi]
        ext = tuple(key_to_global[keys[i]] for i in local)
        cand, nspaces = five_parent_candidates(ext, deficiency)
        max_spaces = max(max_spaces, nspaces)
        state_dist[len(cand)] += 1
        space_dist[nspaces] += 1
        for P, sb, ss, complete, touched in cand:
            singleton_touch_dist[singleton_touch_count(ext, sb)] += 1
            parents.append((oi, tuple(local), ext, P, sb, ss, complete, touched))
    return {
        "parents": tuple(parents),
        "state_dist": state_dist,
        "space_dist": space_dist,
        "singleton_touch_dist": singleton_touch_dist,
        "deficiency_cache_size": len(deficiency.cache),
        "max_spaces": max_spaces,
        "seconds": time.time() - t0,
    }


def extend_parent(ext, parent_P, singleton_block, singleton_state, target_n, deficiency):
    """Extend a rank-four parent by one final coordinate.

    `ext` has target_n coordinates and the parent occupies ext[:-1]. Every
    local generator chosen for P must project into parent_P. Canonical complete
    deficiency zero is a necessary condition for an actual d=0 extension.
    """
    assert len(ext) == target_n
    drop = target_n - 1
    touched = B.touched_blocks(ext)
    if singleton_block not in touched:
        return (), 0, 0

    singleton = R.local_constraint_key(ext, singleton_block, singleton_state)
    if not R.is_subspace(B.project_space(singleton, drop), parent_P):
        return (), 0, 0

    eligible = []
    for b in touched:
        if b == singleton_block:
            continue
        empty = R.local_constraint_key(ext, b, 0)
        if R.is_subspace(B.project_space(empty, drop), parent_P):
            eligible.append((b, empty))

    spaces = {singleton}
    for _b, empty in eligible:
        nxt = set(spaces)
        for space in spaces:
            joined = R.union_key(space, empty)
            if len(joined) <= 4:
                nxt.add(joined)
        spaces = nxt

    out = []
    for P in spaces:
        if len(P) != 4 or B.project_space(P, drop) != parent_P:
            continue
        # The synchronized six- and seven-row shadows preserve rank four after
        # every single-coordinate deletion.
        if any(len(B.project_space(P, i)) != 4 for i in range(target_n)):
            continue
        generated = canonical_generated(
            ext, touched, P, singleton_block, singleton_state
        )
        if generated != P:
            continue
        complete = canonical_complete(ext, touched, P, singleton_block)
        if deficiency(complete) != 0:
            continue
        out.append((P, complete, touched))
    return tuple(out), len(spaces), len(eligible)


def scan_six(five_parents):
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
            # Any six-row deletion shadow of a seven-row p=1 state must keep
            # the singleton touched after deleting any one further row.
            if singleton_touch_count(ext6, sb) < 2:
                counts["singleton_touch_reject"] += 1
                continue
            cand, nspaces, neligible = extend_parent(
                ext6, P5, sb, ss, 6, deficiency
            )
            max_spaces = max(max_spaces, nspaces)
            max_eligible = max(max_eligible, neligible)
            counts["raw_candidates"] += len(cand)
            for P6, C6, T6 in cand:
                sext = tuple(sorted(ext6))
                normalized = B.permute_space(P6, ext6, sext)
                raw.append((sext, normalized, sb, ss, C6, T6))
                touch_dist[singleton_touch_count(sext, sb)] += 1
    unique = {(x[0], x[1], x[2], x[3]): x for x in raw}
    return {
        "parents": tuple(unique.values()),
        "counts": counts,
        "max_spaces": max_spaces,
        "max_eligible": max_eligible,
        "deficiency_cache_size": len(deficiency.cache),
        "singleton_touch_dist_raw": touch_dist,
        "seconds": time.time() - t0,
    }


def scan_seven(six_parents):
    deficiency = B.DeficiencyCache()
    counts = Counter()
    min_pair_rank = Counter()
    bad_pair_count = Counter()
    bad_pair_added = Counter()
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
            if singleton_touch_count(ext7, sb) < 3:
                counts["singleton_touch_reject"] += 1
                continue
            cand, nspaces, neligible = extend_parent(
                ext7, P6, sb, ss, 7, deficiency
            )
            max_spaces = max(max_spaces, nspaces)
            max_eligible = max(max_eligible, neligible)
            counts["single_deletion_synchronized_candidates"] += len(cand)
            for P7, C7, T7 in cand:
                # Normalize by the labeled cycle set to remove duplicate paths
                # through different six-row shadows.
                sevent = tuple(sorted(ext7))
                normalized = B.permute_space(P7, ext7, sevent)
                signature = (sevent, normalized, sb, ss)
                if signature in seen:
                    counts["duplicate_candidates"] += 1
                    continue
                seen.add(signature)
                touch_dist[singleton_touch_count(sevent, sb)] += 1
                ranks = [
                    (i, j, len(B.project_space(normalized, (i, j))))
                    for i in range(7)
                    for j in range(i + 1, 7)
                ]
                minimum = min(r for _i, _j, r in ranks)
                bad = tuple((i, j) for i, j, r in ranks if r < 4)
                min_pair_rank[minimum] += 1
                bad_pair_count[len(bad)] += 1
                # `sevent` is sorted, so there is no distinguished added
                # coordinate after normalization. Retain instead whether every
                # bad pair deletes two singleton-touching cycles.
                singleton_touch_positions = {
                    i for i, e in enumerate(sevent) if R.QCOMP[e][sb] != (0, 0)
                }
                bad_pair_added[
                    sum(i in singleton_touch_positions and j in singleton_touch_positions for i, j in bad)
                ] += 1
                if not bad:
                    survivors.append((sevent, normalized, sb, ss, C7, T7))
    return {
        "counts": counts,
        "min_pair_rank": min_pair_rank,
        "bad_pair_count": bad_pair_count,
        "bad_pair_both_singleton_touching": bad_pair_added,
        "singleton_touch_dist": touch_dist,
        "survivors": tuple(survivors),
        "unique_candidates": len(seen),
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


def counter_dict(c):
    return {str(k): v for k, v in sorted(c.items(), key=lambda kv: str(kv[0]))}


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
    max_complete_norm2 = max(sum(x * x for x in row) for row in G.P0.COMPLETE_T)
    assert max_complete_norm2 == 12
    assert R.P * R.P > max_complete_norm2 ** 15

    if args.stage == "five":
        assert args.parts >= 1 and 0 <= args.part < args.parts
        n = 20451
        start = n * args.part // args.parts
        end = n * (args.part + 1) // args.parts
        result = scan_five(start, end)
        save(args.output, result["parents"])
        print("PASS: five-row D=3,k=1,d=0,p=1 boundary shard")
        print("orbit_range", start, end)
        print("states", len(result["parents"]))
        print("orbits_with_states", sum(v for k, v in result["state_dist"].items() if k))
        print("states_per_orbit_distribution", dict(sorted(result["state_dist"].items())))
        print("candidate_space_distribution", dict(sorted(result["space_dist"].items())))
        print("singleton_touch_census", dict(sorted(result["singleton_touch_dist"].items())))
        print("max_candidate_spaces_per_orbit", result["max_spaces"])
        print("complete_rank_cache_size", result["deficiency_cache_size"])
        print("seconds", round(result["seconds"], 3))
        print("output", args.output)
        return

    if args.stage == "merge-five":
        parents = tuple(x for path in args.inputs for x in load(path))
        keys = {(x[0], x[3], x[4], x[5]) for x in parents}
        assert len(keys) == len(parents)
        save(args.output, parents)
        print("PASS: merged five-row p=1 boundary shards")
        print("states", len(parents))
        print("orbit_representatives_with_states", len({x[0] for x in parents}))
        print("singleton_block_count", len({(x[0], x[4]) for x in parents}))
        print("output", args.output)
        return

    if args.stage == "six":
        five = tuple(load(args.input))
        result = scan_six(five)
        save(args.output, result["parents"])
        print("PASS: six-row synchronized p=1 extension")
        print("five_parent_states", len(five))
        print("counts", dict(result["counts"]))
        print("normalized_six_states", len(result["parents"]))
        print("six_cycle_sets", len({x[0] for x in result["parents"]}))
        print("singleton_state_keys", len({(x[0], x[2], x[3]) for x in result["parents"]}))
        print("singleton_touch_census_raw", dict(sorted(result["singleton_touch_dist_raw"].items())))
        print("max_intermediate_spaces", result["max_spaces"])
        print("max_eligible_blocks", result["max_eligible"])
        print("complete_rank_cache_size", result["deficiency_cache_size"])
        print("seconds", round(result["seconds"], 3))
        print("output", args.output)
        return

    if args.stage == "seven":
        six = tuple(load(args.input))
        result = scan_seven(six)
        summary = {
            "six_parent_states": len(six),
            "counts": dict(result["counts"]),
            "unique_candidates": result["unique_candidates"],
            "min_pair_rank": counter_dict(result["min_pair_rank"]),
            "bad_pair_count": counter_dict(result["bad_pair_count"]),
            "bad_pair_both_singleton_touching": counter_dict(result["bad_pair_both_singleton_touching"]),
            "singleton_touch_dist": counter_dict(result["singleton_touch_dist"]),
            "depth_two_survivors": len(result["survivors"]),
            "max_intermediate_spaces": result["max_spaces"],
            "max_eligible_blocks": result["max_eligible"],
            "complete_rank_cache_size": len(deficiency.cache) if False else result["deficiency_cache_size"],
            "seconds": round(result["seconds"], 3),
        }
        if result["survivors"]:
            summary["first_survivor"] = repr(result["survivors"][0])
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(summary, f, indent=2, sort_keys=True)
                f.write("\n")
        print("PASS: seven-row p=1 synchronized extension scan completed")
        for key, value in summary.items():
            print(key, value)
        return


if __name__ == "__main__":
    main()
