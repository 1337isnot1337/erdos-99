#!/usr/bin/env python3
"""Exact closure certificate for the two-rank-two Profile B branch.

The preceding Profile B reductions prove a dependency-active aligned block b
with exactly three source touches T and at most two rank-two local-empty
singleton blocks globally. This verifier handles the case of exactly two such
rank-two blocks c,d. Analytically their two coefficient lines force a zero
column inside T, hence d2(P) in {6,7}. The remaining normalized cases are
small and are enumerated exactly over Q below.

A zero occurrence of source virtual deficiency d8=3 excludes the branch.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_touch4_alternative_closure_2026_09_22.py"
spec = importlib.util.spec_from_file_location("e99_profile_b_touch4", BASE)
G = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(G)
R = G.R

RANK_CACHE = {}


def source_deficiency(ext, plane):
    complete = tuple(
        b for b in G.touched_blocks(ext)
        if not G.is_subspace(G.local_empty_space(ext, b), plane)
    )
    rank = RANK_CACHE.get(complete)
    if rank is None:
        rank = len(R.rowspace_key(tuple(G.COMPLETE_T[b] for b in complete)))
        RANK_CACHE[complete] = rank
    return len(complete) - rank, complete


def sig(e, c, sc, d, sd):
    rc = G.singleton_row((e,), c, R.LOCAL[sc])[0]
    rd = G.singleton_row((e,), d, R.LOCAL[sd])[0]
    return int(rc != 0), int(rd != 0)


def state_ok(ext, plane, b, sb, c, sc, d, sd, support_size):
    if len(plane) != 2:
        return None
    zero, multiplicities = G.projective_column_profile(plane)
    if 8 - zero != support_size:
        return None
    if support_size - max(multiplicities) < 4:
        return None

    e_b = G.local_empty_space(ext, b)
    e_c = G.local_empty_space(ext, c)
    e_d = G.local_empty_space(ext, d)
    if (len(e_b), len(e_c), len(e_d)) != (1, 2, 2):
        return None
    if G.singleton_row(ext, b, R.LOCAL[sb]) != (Fraction(0),) * 8:
        return None
    if any(G.is_subspace(e, plane) for e in (e_b, e_c, e_d)):
        return None
    deficiency, complete = source_deficiency(ext, plane)
    return (
        (zero, support_size, multiplicities, support_size - max(multiplicities)),
        deficiency,
        len(complete),
    )


def aligned_touch_triple(b, sb):
    star = tuple(sorted(G.aligned_star(b, R.LOCAL[sb])))
    by_fourth = {
        next(iter(set(R.DESC[e]) - set(R.BLOCK_LABELS[b]))): e
        for e in star
    }
    return (by_fourth[4], by_fourth[5], by_fourth[6])


def common_two_set_census(support_size):
    """d2=7, or d2=6 with exactly one zero column in T."""
    b = R.BLOCK_INDEX[(1, 2, 3)]
    c = R.BLOCK_INDEX[(1, 2, 4)]
    d = R.BLOCK_INDEX[(1, 2, 5)]
    counts = Counter()

    if support_size == 7:
        requests = (
            {(1, 1): 1, (1, 0): 2, (0, 1): 2, (0, 0): 0},
            {(1, 1): 2, (1, 0): 2, (0, 1): 1, (0, 0): 0},
            {(1, 1): 2, (1, 0): 1, (0, 1): 2, (0, 0): 0},
        )
    elif support_size == 6:
        requests = (
            {(1, 1): 2, (1, 0): 1, (0, 1): 1, (0, 0): 1},
        )
    else:
        raise ValueError(support_size)

    for sb, sc, sd in product(range(3), repeat=3):
        T = aligned_touch_triple(b, sb)
        if [sig(e, c, sc, d, sd) for e in T] != [(1, 0), (0, 1), (0, 0)]:
            continue
        outside = tuple(e for e in R.NO_ROOT if R.QCOMP[e][b] == (0, 0))
        cats = {k: [] for k in ((0, 0), (1, 0), (0, 1), (1, 1))}
        for e in outside:
            cats[sig(e, c, sc, d, sd)].append(e)

        for request in requests:
            pools = []
            for key, amount in request.items():
                pools.append(tuple(combinations(cats[key], amount)))
            if any(not pool for pool in pools):
                continue
            for pieces in product(*pools):
                ext = T + tuple(e for piece in pieces for e in piece)
                if len(ext) != 8 or len(set(ext)) != 8:
                    continue
                plane = R.rowspace_key((
                    G.singleton_row(ext, c, R.LOCAL[sc]),
                    G.singleton_row(ext, d, R.LOCAL[sd]),
                ))
                item = state_ok(ext, plane, b, sb, c, sc, d, sd, support_size)
                if item is not None:
                    counts[item] += 1
    return counts


def two_zero_touch_census():
    """d2=6 with both coefficient-zero columns inside touch triple T."""
    b = R.BLOCK_INDEX[(1, 2, 3)]
    both_patterns = 0
    max_outside_both = 0
    counts = Counter()

    for sb in range(3):
        T = aligned_touch_triple(b, sb)
        e4 = T[0]
        faces = tuple(
            R.BLOCK_INDEX[tuple(face)]
            for face in combinations(sorted(set(R.DESC[e4])), 3)
        )
        other_faces = tuple(c for c in faces if c != b)
        outside = tuple(e for e in R.NO_ROOT if R.QCOMP[e][b] == (0, 0))

        for c in other_faces:
            for d in other_faces:
                if c == d:
                    continue
                for sc, sd in product(range(3), repeat=2):
                    if [sig(e, c, sc, d, sd) for e in T] != [(1, 1), (0, 0), (0, 0)]:
                        continue
                    both_patterns += 1
                    max_outside_both = max(
                        max_outside_both,
                        sum(sig(e, c, sc, d, sd) == (1, 1) for e in outside),
                    )

        for c in other_faces:
            roots_c = set(R.BLOCK_LABELS[c])
            candidates_d = tuple(
                d for d in range(35)
                if d not in (b, c)
                and len(roots_c & set(R.BLOCK_LABELS[d])) == 2
            )
            for d in candidates_d:
                for sc, sd in product(range(3), repeat=2):
                    if [sig(e, c, sc, d, sd) for e in T] != [(1, 0), (0, 0), (0, 0)]:
                        continue
                    cats = {k: [] for k in ((0, 0), (1, 0), (0, 1), (1, 1))}
                    for e in outside:
                        cats[sig(e, c, sc, d, sd)].append(e)
                    request = {(1, 1): 2, (1, 0): 1, (0, 1): 2}
                    pools = tuple(
                        tuple(combinations(cats[key], amount))
                        for key, amount in request.items()
                    )
                    if any(not pool for pool in pools):
                        continue
                    for pieces in product(*pools):
                        ext = T + tuple(e for piece in pieces for e in piece)
                        if len(ext) != 8 or len(set(ext)) != 8:
                            continue
                        plane = R.rowspace_key((
                            G.singleton_row(ext, c, R.LOCAL[sc]),
                            G.singleton_row(ext, d, R.LOCAL[sd]),
                        ))
                        item = state_ok(ext, plane, b, sb, c, sc, d, sd, 6)
                        if item is not None:
                            counts[item] += 1

    return both_patterns, max_outside_both, counts


def deficiency_histogram(counts):
    out = Counter()
    for (_profile, deficiency, _complete_count), amount in counts.items():
        out[deficiency] += amount
    return out


def main():
    n7 = common_two_set_census(7)
    n6_one_zero = common_two_set_census(6)
    both_patterns, max_outside_both, n6_two_zero = two_zero_touch_census()

    h7 = deficiency_histogram(n7)
    h6_one = deficiency_histogram(n6_one_zero)
    h6_two = deficiency_histogram(n6_two_zero)

    assert sum(n7.values()) == 1188
    assert h7 == Counter({7: 608, 6: 384, 8: 196})

    assert sum(n6_one_zero.values()) == 5312
    assert h6_one == Counter({7: 4448, 8: 480, 6: 192, 9: 144, 10: 48})

    assert both_patterns == 72
    assert max_outside_both == 0
    assert sum(n6_two_zero.values()) == 7200
    assert h6_two == Counter({7: 5664, 6: 1536})

    assert 3 not in h7 and 3 not in h6_one and 3 not in h6_two

    print("PASS: Profile B two-rank-two singleton branch excluded")
    print("d2_7_states", sum(n7.values()))
    print("d2_7_deficiency_histogram", dict(sorted(h7.items())))
    print("d2_6_one_zero_in_touch_states", sum(n6_one_zero.values()))
    print("d2_6_one_zero_in_touch_deficiency_histogram", dict(sorted(h6_one.items())))
    print("d2_6_both_support_touch_patterns", both_patterns)
    print("d2_6_both_support_max_outside_common_cycles", max_outside_both)
    print("d2_6_two_zero_in_touch_c_only_states", sum(n6_two_zero.values()))
    print("d2_6_two_zero_in_touch_c_only_deficiency_histogram", dict(sorted(h6_two.items())))
    print("consequence", "at most one rank-two singleton block; at least eight aligned singleton blocks")


if __name__ == "__main__":
    main()
