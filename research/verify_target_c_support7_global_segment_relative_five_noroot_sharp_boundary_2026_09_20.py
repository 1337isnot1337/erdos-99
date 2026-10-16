#!/usr/bin/env python3
"""Exhibit exact D=0 and D=1 five-no-root boundary families.

The proposed uniform five-no-root slack-two theorem is false.  This verifier
constructs one k=5,p=10 family with

    D(A)=|A|-3*delta(A)=0

and one k=5,p=11 family with D(A)=1.  All ranks are recomputed directly over
Q from the committed 85-dimensional M and 70-dimensional quotient coordinate
models.  It also tests every one of the other 100 no-root four-cycles against
each fixed root-0 selection: each addition raises both r_M and r_Q by one, so
neither displayed boundary family has a delta-increasing no-root extension
without changing its root-0 rows.

The examples prove that the established global five-no-root inequality D>=0
is sharp and rule out the blanket D>=2 deletion shortcut for the six-no-root
layer.  The extension check is a statement about these two explicit families,
not a classification of every D=0 or D=1 five-no-root family.
"""
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k5_2026_09_20.py"
spec = importlib.util.spec_from_file_location("relative_five_noroot_k5_sharp", BASE)
K = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(K)
R = K.R

EXAMPLES = {
    "D0": {
        "ext": (106, 109, 112, 118, 121),
        "touched": (0, 1, 2, 3, 5, 6, 7, 9, 10, 15, 16, 17, 19, 20),
        "states": (4, 7, 1, 1, 1, 7, 1, 1, 7, 2, 7, 2, 2, 2),
        "expected": (27, 27, 18, 9, 0, 10),
    },
    "D1": {
        "ext": (106, 109, 112, 115, 184),
        "touched": (
            0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 17, 18, 19, 20, 22, 31,
        ),
        "states": (7, 1, 1, 7, 7, 7, 7, 1, 1, 2, 2, 2, 2, 4, 1, 1, 7),
        "expected": (34, 34, 23, 11, 1, 11),
    },
}


def selected_rows(ext, touched, states):
    selected = list(ext)
    p = 0
    for block, state in zip(touched, states):
        assert R.local_constraint_key(ext, block, state) == ()
        mask = R.STATES[state][0]
        if state != 7:
            p += R.STATES[state][1]
        for local_index, row_id in enumerate(R.BLOCKS[block]):
            if mask & (1 << local_index):
                selected.append(row_id)
    return tuple(selected), p


def main():
    for name, data in EXAMPLES.items():
        ext = data["ext"]
        touched = data["touched"]
        states = data["states"]
        assert len(ext) == 5
        assert len(touched) == len(states)
        assert touched == tuple(sorted(
            block
            for block in range(35)
            if any(R.QCOMP[e][block] != (0, 0) for e in ext)
        ))

        selected, p = selected_rows(ext, touched, states)
        assert len(selected) == len(set(selected))
        assert sum(e in R.NO_ROOT for e in selected) == 5

        r_m = R.exact_rank([R.MCOORD[e] for e in selected])
        r_q = R.exact_rank([R.QCOORD[e] for e in selected])
        delta = r_m - r_q
        defect = len(selected) - 3 * delta
        relation_delta = R.exact_rank(
            K.relation_rows_zero(ext, touched, states)
        )
        assert relation_delta == delta

        got = (len(selected), r_m, r_q, delta, defect, p)
        assert got == data["expected"], (name, got)

        extension_census = {}
        for e in R.NO_ROOT:
            if e in selected:
                continue
            extended = selected + (e,)
            ext_r_m = R.exact_rank([R.MCOORD[x] for x in extended])
            ext_r_q = R.exact_rank([R.QCOORD[x] for x in extended])
            ext_delta = ext_r_m - ext_r_q
            key = (ext_r_m - r_m, ext_r_q - r_q, ext_delta - delta)
            extension_census[key] = extension_census.get(key, 0) + 1

        assert extension_census == {(1, 1, 0): 100}

        print(
            name,
            "rows", len(selected),
            "p", p,
            "rM", r_m,
            "rQ", r_q,
            "delta", delta,
            "defect", defect,
        )
        print(name, "no_root_extension_increment_census", extension_census)

    print("PASS: sharp five-no-root boundary examples")
    print("consequence", "the global five-no-root D>=0 theorem is sharp")
    print("consequence", "a universal five-no-root D>=2 theorem is false")


if __name__ == "__main__":
    main()
