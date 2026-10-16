#!/usr/bin/env python3
"""Exact fixed-face-(2,3) saturation of the current 4,158-cell generic-H6 endpoint.

The committed 298-state candidate ledger was obtained by an exhaustive numerical
scan of the earlier 4,276-state reflection-closed endpoint. Extension VI then
proved and removed 59 direct face-(2,3) states together with their 59 reflected
partners, leaving 4,158 states. This verifier reconstructs that current endpoint
first and exactifies only candidate-ledger states that still survive it.

Numerical LPs are used only to recover sparse supports. For every selected state
this verifier checks over exact rational arithmetic that every physical branch
product at faces 2 and 3 is impossible. Hull reflection then transports each
new direct exclusion to its reflected state.

Use --start/--stop to rerun contiguous slices of the fresh candidate list. A
full invocation exactifies every fresh direct candidate before reporting the new
reflection-closed endpoint. --inventory-only reconstructs the 4,158-state
endpoint and reports the stale/fresh split without attempting new certificates.
"""
from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


E5 = load(
    "h6_two_face_23_extension5_reflection",
    "verify_target_c_support7_h6_two_face_23_extension5_reflection_2026_09_19.py",
)
E6 = load(
    "h6_two_face_23_extension6_reflection",
    "verify_target_c_support7_h6_two_face_23_extension6_reflection_2026_09_19.py",
)
A = E5.A
O = E5.O
BRANCH_KEYS = E5.BRANCH_KEYS

# Exhaustive numerical discovery on the exact 4,276-state predecessor produced
# 298 candidates and no LP solver failures. Some are now stale because
# Extension VI independently certified 118 states (59 direct plus reflection).
# Exactification below, not this numerical ledger, is the proof of impossibility.
CANDIDATE_IDX_4276 = (
    5354,5411,5415,5423,5444,5445,5449,5451,5478,5480,5483,5488,5499,5501,5503,5513,5514,5516,5523,5524,5529,5532,5541,5544,5566,5568,5576,5598,5666,5680,5689,5855,5859,5864,5869,5906,5919,6043,6064,6067,6106,6136,6206,6211,6214,6219,6225,6226,6230,6231,6314,6362,
    6419,6440,6453,6473,6475,6481,6491,6496,6498,6503,6511,6517,6520,6522,6525,6532,6534,6579,6588,6592,6602,6603,6609,6610,6611,6614,6617,6620,6623,6634,6639,6655,6659,6669,6677,6684,6690,6691,6693,6710,6713,6744,6760,6769,6771,6779,6836,6842,6855,6889,6892,6895,6901,6988,7004,7012,7014,7026,7031,7051,7053,7062,7063,7076,7083,7145,7214,7754,7767,7921,7923,7959,7963,7969,7979,7988,7989,7996,8023,8035,8057,8058,8399,8497,8540,8547,8577,8608,8616,8641,8644,8653,8659,
    8676,8762,9237,9254,9260,9267,9272,9277,9284,9297,9301,9315,9328,9343,9352,9375,9383,9386,9388,9416,9502,9506,9516,9531,9540,9548,9598,9600,9621,9712,9721,9722,10302,10370,10375,10380,10386,10418,10420,10445,10447,10459,10461,10466,10498,10502,10517,10519,10522,10525,10529,10544,10768,
    10808,10828,10845,10936,10944,10951,10953,10966,10972,10980,10985,10991,11014,11017,11029,11036,11045,11047,11049,11060,11062,11064,11070,11073,11077,11083,11203,11223,11226,11283,11320,11321,11324,11333,11335,11336,11340,11347,11353,11358,11360,11366,11368,11374,11377,11386,11411,11435,11437,11438,11444,11446,11450,11459,11462,11463,11465,11466,11473,11477,11478,11485,11501,11512,11517,11519,11528,11529,11551,11554,11563,11603,11608,11671,11678,11687,11695,11710,11716,11726,11729,11808,11810,11826,11853,12008,12041,
    12491,12503,12842,13078,13088,13116,13157,13171,13185,13186,13251,13789,13818,
)
assert len(CANDIDATE_IDX_4276) == 298 == len(set(CANDIDATE_IDX_4276))

START_GRAPH = {"C7": 3316, "C3+C4": 842}
START_PATTERN = {
    "145": 4, "156": 16, "235": 556, "236": 1046, "237": 16,
    "245": 449, "256": 1046, "345": 16, "346": 449, "347": 4,
    "356": 556,
}


def predecessor_endpoint(states):
    """Reconstruct the exact current 4,158-state reflection-closed endpoint."""
    previous = O.complete_angle_survivors(states)
    assert len(previous) == 5692
    reflected, closure4464 = E5.reflection_data(states)

    direct5 = {previous[q] for q in E5.CANDIDATE_Q}
    image5 = {reflected[i] for i in direct5}
    endpoint4276 = closure4464 - direct5 - image5
    assert len(endpoint4276) == 4276
    assert {reflected[i] for i in endpoint4276} == endpoint4276

    direct6 = {previous[q] for q in E6.CANDIDATE_Q}
    image6 = {reflected[i] for i in direct6}
    assert len(direct6) == len(image6) == 59
    assert direct6.isdisjoint(image6)
    assert direct6 | image6 <= endpoint4276

    current = endpoint4276 - direct6 - image6
    assert len(current) == 4158
    assert {reflected[i] for i in current} == current
    assert Counter(states[i][1] for i in current) == Counter(START_GRAPH)
    assert Counter("".join(map(str, states[i][5])) for i in current) == Counter(START_PATTERN)
    return reflected, current, direct6 | image6


def exactify_idx(states, idx):
    system = O.C.build_system(states[idx])
    live = {}
    cert_count = 0
    forced = Counter()
    max_den = 1

    for face in (2, 3):
        live_here = []
        for branch_index, (order, side) in enumerate(BRANCH_KEYS):
            closed = A.BRANCH[(face, order, side)]
            margin, result = O.numerical_candidate(system, closed)
            assert margin is not None, (idx, face, branch_index, result.message)
            if margin > 1e-8:
                live_here.append(branch_index)
                continue
            cert = A.exactify_support(system, closed, result)
            assert cert is not None, (idx, "one-face", face, branch_index, margin)
            value, denominator = cert
            cert_count += 1
            forced["zero" if value == 0 else "negative"] += 1
            max_den = max(max_den, denominator)
        assert live_here, (idx, "unexpected one-face contradiction", face)
        live[face] = live_here

    for i2 in live[2]:
        o2, s2 = BRANCH_KEYS[i2]
        for i3 in live[3]:
            o3, s3 = BRANCH_KEYS[i3]
            closed = A.BRANCH[(2, o2, s2)] + A.BRANCH[(3, o3, s3)]
            margin, result = O.numerical_candidate(system, closed)
            assert margin is not None, (idx, i2, i3, result.message)
            assert margin <= 1e-8, (idx, "live pair", i2, i3, margin)
            cert = A.exactify_support(system, closed, result)
            assert cert is not None, (idx, "pair exactification", i2, i3, margin)
            value, denominator = cert
            cert_count += 1
            forced["zero" if value == 0 else "negative"] += 1
            max_den = max(max_den, denominator)

    return cert_count, forced, max_den, len(live[2]), len(live[3])


def main():
    parser = ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int)
    parser.add_argument("--inventory-only", action="store_true")
    args = parser.parse_args()

    states = O.tri.collect_survivors()
    assert len(states) == 14174
    reflected, current, removed6 = predecessor_endpoint(states)

    stale = tuple(i for i in CANDIDATE_IDX_4276 if i not in current)
    fresh = tuple(i for i in CANDIDATE_IDX_4276 if i in current)
    assert len(stale) + len(fresh) == len(CANDIDATE_IDX_4276)
    assert set(stale) <= removed6
    assert set(fresh).isdisjoint(removed6)
    assert len(fresh) >= 180

    print("candidate_ledger_4276", len(CANDIDATE_IDX_4276))
    print("stale_after_extension6", len(stale))
    print("fresh_on_4158", len(fresh))
    print("stale_idx", stale)
    if args.inventory_only:
        print("PASS inventory")
        return

    stop = len(fresh) if args.stop is None else args.stop
    assert 0 <= args.start <= stop <= len(fresh)

    certs = 0
    forced = Counter()
    max_den = 1
    for k in range(args.start, stop):
        idx = fresh[k]
        count, f, den, live2, live3 = exactify_idx(states, idx)
        certs += count
        forced.update(f)
        max_den = max(max_den, den)
        print("GOOD", k, idx, count, dict(f), den, live2, live3, flush=True)

    print("EXACT_DONE")
    print("range", args.start, stop)
    print("good_count", stop - args.start)
    print("certificates", certs)
    print("forced", dict(forced))
    print("max_denominator", max_den)

    if args.start == 0 and stop == len(fresh):
        direct = set(fresh)
        image = {reflected[i] for i in direct}
        removed = direct | image
        assert removed <= current
        survivors = current - removed
        assert len(survivors) == 4158 - len(removed)
        assert {reflected[i] for i in removed} == removed
        assert {reflected[i] for i in survivors} == survivors

        graph_removed = Counter(states[i][1] for i in removed)
        pattern_removed = Counter("".join(map(str, states[i][5])) for i in removed)
        graph_survivors = {k: START_GRAPH[k] - graph_removed[k] for k in START_GRAPH}
        pattern_survivors = {
            k: START_PATTERN[k] - pattern_removed[k] for k in START_PATTERN
        }
        assert sum(graph_survivors.values()) == len(survivors)
        assert sum(pattern_survivors.values()) == len(survivors)
        assert pattern_survivors["145"] == pattern_survivors["347"]
        assert pattern_survivors["156"] == pattern_survivors["237"]
        assert pattern_survivors["235"] == pattern_survivors["356"]
        assert pattern_survivors["236"] == pattern_survivors["256"]
        assert pattern_survivors["245"] == pattern_survivors["346"]

        print("fresh_direct", len(direct))
        print("reflected_image", len(image))
        print("direct_image_overlap", len(direct & image))
        print("removed_union", len(removed))
        print("survivors", len(survivors))
        print("graph_removed", dict(sorted(graph_removed.items())))
        print("pattern_removed", dict(sorted(pattern_removed.items())))
        print("graph_survivors", graph_survivors)
        print("pattern_survivors", pattern_survivors)
        print("PASS")


if __name__ == "__main__":
    main()
