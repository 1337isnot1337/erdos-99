#!/usr/bin/env python3
"""Exact witness that the current k=3 p=2 verifier's candidate-P list is not exhaustive.

This does not give a density counterexample.  The omitted state below has exact
defect 7.  It proves only that the existing p=2 proof must be supplemented by
an audit of rank-two coefficient spaces generated partly by singleton states,
rather than only by canonical p=0 empty-state constraints.
"""
from fractions import Fraction
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k3_p0_2026_09_20.py"
spec = importlib.util.spec_from_file_location("relative_five_noroot_k3_gap_base", BASE)
P0 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(P0)
R = P0.R

EXT = (106, 109, 112, 105, 107)
TOUCHED = (0, 1, 2, 3, 5, 6, 7, 15, 16, 17)
SPACE = (
    (Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(1)),
)
STATES = (4, 7, 1, 0, 7, 7, 0, 7, 7, 0)


def main():
    assert R.lucas_lehmer_127()
    union = ()
    for block, state in zip(TOUCHED, STATES):
        union = R.union_key(union, R.local_constraint_key(EXT, block, state))
    assert union == SPACE

    p0_spaces = set(P0.candidate_rank2_constraint_spaces(EXT, TOUCHED))
    assert SPACE not in p0_spaces

    complete = tuple(block for block, state in zip(TOUCHED, STATES) if state == 7)
    assert complete == (1, 5, 6, 15, 16)
    assert R.rank_mod([P0.COMPLETE_T[block] for block in complete]) == 5
    assert sum(R.STATES[state][5] for state in STATES) == 2

    rows = P0.relation_rows(EXT, TOUCHED, STATES, SPACE)
    max_norm2 = max(sum(x * x for x in row) for row in rows)
    delta = R.rank_mod(rows)
    defect = 5 + 3 * len(complete) + 2 - 3 * delta
    assert delta == 5
    assert defect == 7
    assert R.P * R.P > max(12, max_norm2) ** 15

    print("PASS: k=3 p=2 candidate-space omission witness")
    print("external_cycles", EXT)
    print("touched_blocks", TOUCHED)
    print("complete_blocks", complete)
    print("p", 2)
    print("global_constraint_rank", len(SPACE))
    print("listed_by_p0_candidate_spaces", False)
    print("delta", delta)
    print("defect", defect)
    print("max_relation_row_norm_squared", max_norm2)


if __name__ == "__main__":
    main()
