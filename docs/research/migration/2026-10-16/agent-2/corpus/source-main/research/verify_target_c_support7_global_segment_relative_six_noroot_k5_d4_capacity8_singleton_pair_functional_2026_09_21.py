#!/usr/bin/env python3
"""Exact d6=4 singleton-plus-pair functional audit for k=7 C:(4,11,10).

The remaining eight-no-root k=7 profile

    C: D=-1, p=12, (d_v,q,s)=(4,11,10)

has ten singleton changed blocks and one pair changed block.  A committed good
p-retaining deletion pair gives a synchronized six-row k=5 shadow.  If its
virtual-canonical deficiency is d6=4, then D6=3 and the containment inequality
forces at least nine changed virtual-complete blocks.  If the global pair block
is not among those nine, the shadow has at least nine singleton replacements
and is already excluded by the committed d=4 singleton-functional audit.  The
only unresolved form therefore has at least eight compatible singleton blocks
plus one pair replacement.

For a six-row d=4 state the replacement-functional identity gives

    D6 >= 6 + p + 3*d6 - 3*s_f,

where s_f is the rank gained by the selected replacement functionals modulo the
canonical relation-column span.  With D6=3, p=12, d6=4, one needs s_f>=9.

This audit exhausts every synchronized six-row rank-one d=4 state with
singleton capacity at least eight.  For each state it computes all compatible
singleton replacement functionals.  It then overapproximates the one-pair case
by allowing any pair state (3,5,6) on any canonical-complete block, dropping the
singleton functional of that block when necessary.  Thus a global maximum
combined extra rank at most eight excludes the d6=4 side of C:(4,11,10).

All ranks use P=2^127-1 and are exact over Q by the same Lucas-Lehmer/Hadamard
certificate as the committed singleton-functional audit.
"""

from collections import Counter
from pathlib import Path
import argparse
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_six_noroot_k5_d4_capacity9_functional_2026_09_21.py"
spec = importlib.util.spec_from_file_location("e99_C_d4q11_d4_functional_base", BASE)
F = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(F)
B, S, R = F.B, F.S, F.R
MOD = R.P


def replacement_functional(ext_global, block, state, line, complete_index, c):
    """Functional for replacing one canonical-complete block by any local state."""
    out = [0] * (c + 5)
    out[complete_index[block]] = 1
    line_key = R.rowspace_key((line,))
    for i, alpha in enumerate(R.nullspace_int(line_key, 6)):
        vx = sum(alpha[j] * R.QCOMP[e][block][0] for j, e in enumerate(ext_global))
        vy = sum(alpha[j] * R.QCOMP[e][block][1] for j, e in enumerate(ext_global))
        beta_complete = R.solve_local_coeffs_int(7, (-vx, -vy))
        beta_new = R.solve_local_coeffs_int(state, (-vx, -vy))
        diff = [beta_new[j] - beta_complete[j] for j in range(3)]
        lam = diff[0]
        assert diff == [lam, -lam, -lam]
        out[c + i] = -lam
    return tuple(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--cover-cache",
        help="optional pickle containing (keys, six_augmentation_cover, local_cycle_info)",
    )
    ap.add_argument("--cover-start", type=int, default=0)
    ap.add_argument("--cover-end", type=int)
    args = ap.parse_args()

    assert R.lucas_lehmer_127()
    assert max(sum(x * x for x in row) for row in S.COMPLETE_T) == 12
    assert MOD * MOD > 12 ** 15

    keys, cover, info = B.load_cover(args.cover_cache)
    local_to_global, _ = S.local_cycle_data(keys)
    assert len(cover) == 325955

    start = args.cover_start
    end = len(cover) if args.cover_end is None else args.cover_end
    assert 0 <= start <= end <= len(cover)

    rank_cache = {}
    candidate_census = Counter()
    singleton_extra_census = Counter()
    combined_extra_census = Counter()
    synchronized_states = 0
    candidate_states = 0
    pair_audited_states = 0
    max_singleton_extra = 0
    max_combined_extra = 0
    max_norm2 = 0
    max_width = 0
    max_singleton_multiplicity = 0
    witnesses = []

    for ext_local in cover[start:end]:
        values, lines, empty_line, singleton_lines = S.block_profile(ext_local, info)
        ext_global = tuple(local_to_global[i] for i in ext_local)
        for line in lines:
            if sum(x != 0 for x in line) < 2:
                continue
            synchronized_states += 1
            complete = tuple(sorted(block for block in values if empty_line[block] != line))
            rank_complete = rank_cache.get(complete)
            if rank_complete is None:
                rank_complete = R.rank_mod([S.COMPLETE_T[block] for block in complete])
                rank_cache[complete] = rank_complete
            if len(complete) - rank_complete != 4:
                continue

            singleton_state = {}
            for block in complete:
                options = tuple(
                    (1, 2, 4)[i]
                    for i, local_line in enumerate(singleton_lines[block])
                    if local_line is None or local_line == line
                )
                max_singleton_multiplicity = max(max_singleton_multiplicity, len(options))
                if options:
                    assert len(options) == 1
                    singleton_state[block] = options[0]
            capacity = len(singleton_state)
            if capacity < 8:
                continue

            candidate_states += 1
            candidate_census[capacity] += 1
            touched = tuple(sorted(values))
            complete_set = set(complete)
            states = tuple(7 if block in complete_set else 0 for block in touched)
            rows = F.relation_rows_line(ext_global, touched, states, line)
            assert R.rank_mod(rows) == rank_complete
            transposed = [
                tuple(rows[j][k] for j in range(len(rows)))
                for k in range(15)
            ]
            assert F.rank_mod_rows(transposed) == rank_complete

            c = len(complete)
            complete_index = {block: i for i, block in enumerate(complete)}
            singleton_functionals = {
                block: replacement_functional(
                    ext_global, block, state, line, complete_index, c
                )
                for block, state in singleton_state.items()
            }
            singleton_extra = (
                F.rank_mod_rows(transposed + list(singleton_functionals.values()))
                - rank_complete
            )
            singleton_extra_census[(capacity, singleton_extra)] += 1
            max_singleton_extra = max(max_singleton_extra, singleton_extra)

            # One additional pair functional can raise rank by at most one.  If
            # the full singleton span is <=7, the combined span is automatically
            # <=8 and cannot reach the required threshold nine.
            best_combined = min(singleton_extra + 1, 8)
            if singleton_extra >= 8:
                pair_audited_states += 1
                best_combined = 0
                for pair_block in complete:
                    others = [
                        vec for block, vec in singleton_functionals.items()
                        if block != pair_block
                    ]
                    for pair_state in (3, 5, 6):
                        pair_vec = replacement_functional(
                            ext_global, pair_block, pair_state, line,
                            complete_index, c,
                        )
                        extra = (
                            F.rank_mod_rows(transposed + others + [pair_vec])
                            - rank_complete
                        )
                        best_combined = max(best_combined, extra)
                        max_norm2 = max(max_norm2, sum(x * x for x in pair_vec))
                if best_combined >= 9 and len(witnesses) < 20:
                    witnesses.append((ext_local, line, capacity, singleton_extra, best_combined))

            combined_extra_census[(capacity, singleton_extra, best_combined)] += 1
            max_combined_extra = max(max_combined_extra, best_combined)
            max_width = max(max_width, len(rows))
            for row in transposed + list(singleton_functionals.values()):
                max_norm2 = max(max_norm2, sum(x * x for x in row))

    assert max_singleton_multiplicity <= 1
    if max_width:
        assert MOD * MOD > max_norm2 ** max_width

    print("PASS: completed six-no-root d4/capacity>=8 singleton-plus-pair audit")
    print("cover_range", (start, end))
    print("synchronized_states", synchronized_states)
    print("candidate_count", candidate_states)
    print("candidate_capacity", dict(sorted(candidate_census.items())))
    print("singleton_extra_census", dict(sorted(singleton_extra_census.items())))
    print("combined_extra_census", dict(sorted(combined_extra_census.items())))
    print("pair_audited_states", pair_audited_states)
    print("max_singleton_extra_rank", max_singleton_extra)
    print("max_combined_extra_rank", max_combined_extra)
    print("required_combined_extra_rank", 9)
    print("witnesses_ge9", witnesses)
    print("max_singleton_multiplicity", max_singleton_multiplicity)
    print("unique_complete_sets_ranked", len(rank_cache))
    print("max_row_norm_squared", max_norm2)
    print("max_functional_width", max_width)
    print("hadamard_exact_rank_bound", (not max_width) or MOD * MOD > max_norm2 ** max_width)


if __name__ == "__main__":
    main()
