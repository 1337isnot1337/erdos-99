#!/usr/bin/env python3
"""Exact high-capacity six-row regression and its clean one-row lift audit.

This is one explicit finite cycle-space state, not an eight-row Profile B
source or a planar global minimizer.  All rank decisions in this certificate
use rational arithmetic.  No orbit cover is generated.
"""

from collections import Counter
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_global_lift_2026_09_22.py"
spec = importlib.util.spec_from_file_location("profile_b_lift_for_capacity10_regression", BASE)
L = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(L)
B, R, S, G, P0 = L.B, L.R, L.S, L.G, L.P0

EXT = (106, 109, 112, 115, 105, 107)
SPACE = R.rowspace_key(((1, 1, 1, 1, 0, 1), (0, 0, 0, 0, 1, 1)))
COMPLETE = (1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 17, 18)
GOOD = (2, 3, 4, 6, 7, 8, 15, 16, 17, 18)
CHILDREN = ((3, 10, 6), (2, 7, 5), (2, 7, 5), (2, 7, 5), (3, 12, 6), (3, 12, 6))


def profile(ext, space):
    touched, complete = S.canonical_complete_set(ext, space)
    states = G.virtual_canonical(ext, touched, space)
    rows = L.generic_relation_rows(ext, touched, states, space)
    complete_rank = R.exact_rank([P0.COMPLETE_T[b] for b in complete])
    assert R.exact_rank(rows) == complete_rank
    span = L.exact_singleton_span(ext, space, complete, rows)
    assert span is not None
    return touched, complete, states, rows, len(complete) - complete_rank, span


def minimum_support_at_least(space, size):
    """Exact puncture criterion, avoiding any search over rational scalars."""
    n = len(space[0])
    for removed in combinations(range(n), size - 1):
        kept = tuple(i for i in range(n) if i not in removed)
        if len(R.rowspace_key(tuple(tuple(row[i] for i in kept) for row in space))) != len(space):
            return False
    return True


def main():
    touched, complete, canonical, rows, deficiency, span = profile(EXT, SPACE)
    assert complete == COMPLETE
    assert deficiency == 3 and span == (10, 7)
    assert minimum_support_at_least(SPACE, 2)
    good = B.A.compatible_singleton_blocks(EXT, SPACE, complete)
    assert good == GOOD
    assert R.local_constraint_key(EXT, 0, 0) == SPACE
    assert tuple(b for b, state in zip(touched, canonical) if state == 0) == (0,)

    columns = [tuple(row[k] for row in rows) for k in range(15)]
    complete_index = {b: i for i, b in enumerate(complete)}
    functionals = {}
    singleton_states = {}
    for block in good:
        options = B.singleton_options(EXT, block, SPACE)
        assert len(options) == 1
        singleton_states[block] = options[0]
        functionals[block] = B.replacement_functional(
            EXT, block, options[0], SPACE, complete_index, len(complete)
        )
    assert R.exact_rank(columns) == 9
    assert R.exact_rank(columns + list(functionals.values())) == 16

    children = []
    for i in range(6):
        ext_i = EXT[:i] + EXT[i + 1:]
        projected = S.project_space(SPACE, i)
        assert len(projected) == 2
        _ti, _ci, _si, _ri, d_i, span_i = profile(ext_i, projected)
        children.append((d_i, *span_i))
    assert tuple(children) == CHILDREN

    # Realize a nine-singleton six-row state, retaining the canonical empty
    # block that generates exactly SPACE.  This verifies that the example is
    # more than an enlarged compatible-singleton list.
    realizations = []
    for selected in combinations(good, 9):
        if R.exact_rank(columns + [functionals[b] for b in selected]) != 16:
            continue
        selected_set = set(selected)
        states = tuple(singleton_states[b] if b in selected_set else state for b, state in zip(touched, canonical))
        actual_space = R.rowspace_key(tuple(
            row
            for block, state in zip(touched, states)
            for row in R.local_constraint_key(EXT, block, state)
        ))
        assert actual_space == SPACE
        root_ids = tuple(
            row_id
            for block, state in zip(touched, states)
            for j, row_id in enumerate(R.BLOCKS[block])
            if state & (1 << j)
        )
        ids = root_ids + EXT
        rm = R.exact_rank([R.MCOORD[e] for e in ids])
        rq = R.exact_rank([R.QCOORD[e] for e in ids])
        delta = rm - rq
        assert (len(ids), rm, rq, delta, len(ids) - 3 * delta) == (24, 24, 17, 7, 3)
        root_delta = R.exact_rank([R.MCOORD[e] for e in root_ids]) - R.exact_rank([R.QCOORD[e] for e in root_ids])
        assert sum(state == 7 for state in states) - root_delta == 0
        realizations.append(selected)
    assert realizations

    # Every source with minimum coefficient support four extending this seed
    # has a seven-row deletion with minimum support at least three, d=3, and
    # full singleton-functional extra rank eight.  Exhaust every realizable
    # rank-two one-row lift and test these necessary conditions over Q.
    counts = Counter()
    seven_census = Counter()
    survivors = []
    for extra in R.NO_ROOT:
        if extra in EXT:
            continue
        counts["external_rows"] += 1
        ext7 = EXT + (extra,)
        touched7 = S.touched_blocks(ext7)
        for space7 in L.candidate_rank2_lifts(ext7, touched7, SPACE):
            counts["planes"] += 1
            if not minimum_support_at_least(space7, 3):
                continue
            counts["minimum_support3"] += 1
            touched7, complete7 = S.canonical_complete_set(ext7, space7)
            d7 = len(complete7) - R.exact_rank([P0.COMPLETE_T[b] for b in complete7])
            if d7 != 3:
                continue
            counts["deficiency3"] += 1
            states7 = G.virtual_canonical(ext7, touched7, space7)
            rows7 = L.generic_relation_rows(ext7, touched7, states7, space7)
            span7 = L.exact_singleton_span(ext7, space7, complete7, rows7)
            assert span7 is not None
            seven_census[span7] += 1
            if span7[1] == 8:
                survivors.append((extra, space7, span7))
    assert counts["external_rows"] == 99
    assert dict(counts) == {"external_rows": 99, "planes": 123, "minimum_support3": 18, "deficiency3": 6}
    assert dict(seven_census) == {(6, 4): 6}
    assert not survivors, survivors

    print("PASS: exact capacity-ten six-row regression; no qualifying clean one-row lift")
    print("external_rows", EXT)
    print("coefficient_space", SPACE)
    print("canonical_complete", complete)
    print("compatible_singleton_states", tuple(singleton_states.items()))
    print("six_profile", (deficiency, *span))
    print("five_profiles", tuple(children))
    print("nine_singleton_realizations", tuple(realizations))
    print("actual_state_ranks", (24, 24, 17, 7, 3))
    print("lift_counts", dict(counts))
    print("seven_profile_census", dict(sorted(seven_census.items())))


if __name__ == "__main__":
    main()