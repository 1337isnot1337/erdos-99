#!/usr/bin/env python3
"""Exact one-cycle seven-row functional audit for C:(5,12,12), d6=5.

An actual target has D7=1,p7=12,d7=5 after restoring either member of the
good deletion pair, hence needs singleton-functional extra rank 11.  This scan
starts from every six-row d6=5/full-rank-10 witness, enumerates every compatible
d7=5/capacity>=11 lift retaining the six-row rank-10 span, and computes an
upper bound on seven-row singleton-functional rank by including every compatible
singleton state from every virtual-complete block.  Zero rank-11 lifts closes
the remaining d6=5 branch.  Modular ranks are certified over Q by Hadamard.
"""
from collections import Counter
from pathlib import Path
import argparse, contextlib, importlib.util, io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k7_C_d5q12_d5_full_span_lift_multiplicity_2026_09_22.py"
spec = importlib.util.spec_from_file_location("e99_d5_span", BASE)
P = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(P)
D5, B, S, R = P.D5, P.B, P.S, P.R


def singleton_functional(ext, block, state, index, c, alphas):
    out = [0] * (c + len(alphas))
    out[index[block]] = 1
    for i, alpha in enumerate(alphas):
        vx = sum(alpha[j] * R.QCOMP[e][block][0] for j, e in enumerate(ext))
        vy = sum(alpha[j] * R.QCOMP[e][block][1] for j, e in enumerate(ext))
        full = R.solve_local_coeffs_int(7, (-vx, -vy))
        single = R.solve_local_coeffs_int(state, (-vx, -vy))
        diff = [single[j] - full[j] for j in range(3)]
        lam = diff[0]
        assert diff == [lam, -lam, -lam]
        out[c + i] = -lam
    return tuple(out)


def append0(line):
    return None if line is None else tuple(line) + (0,)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cover-cache")
    ap.add_argument("--cover-start", type=int, default=0)
    ap.add_argument("--cover-end", type=int)
    a = ap.parse_args()

    assert R.lucas_lehmer_127()
    assert max(sum(x*x for x in row) for row in S.COMPLETE_T) == 12
    assert R.P * R.P > 12 ** 15
    keys, cover, info = B.load_cover(a.cover_cache)
    info = tuple(tuple((b, int(x), int(y)) for b, x, y in cyc) for cyc in info)
    local_to_global, _ = S.local_cycle_data(keys)
    assert len(cover) == 325955
    start = a.cover_start
    end = len(cover) if a.cover_end is None else a.cover_end
    assert 0 <= start <= end <= len(cover)

    all_cycles = set(range(105))
    cycle_maps = tuple({b: (x, y) for b, x, y in cyc} for cyc in info)
    cycle_blocks = tuple(set(m) for m in cycle_maps)
    dcache = {}
    def deficiency(blocks):
        key = tuple(sorted(blocks))
        if key not in dcache:
            dcache[key] = len(key) - R.rank_mod([S.COMPLETE_T[b] for b in key])
        return dcache[key]

    sync = witnesses = lifts = retained_lifts = full11 = 0
    extra_census = Counter()
    cap_census = Counter()
    examples = []
    max_fn_norm2 = max_fn_width = max_rel_norm2 = max_rel_rows = 0

    for ci, ext6 in enumerate(cover[start:end], start=start):
        vals6, lines6, empty6, singles6 = S.block_profile(ext6, info)
        ext6g = tuple(local_to_global[i] for i in ext6)
        blocks6 = set(vals6)
        for line6 in lines6:
            if sum(x != 0 for x in line6) < 2:
                continue
            sync += 1
            complete6 = tuple(sorted(b for b in vals6 if empty6[b] != line6))
            if deficiency(complete6) != 5:
                continue
            rank6 = len(complete6) - 5
            sstate6 = {}
            for b in complete6:
                opts = tuple((1,2,4)[i] for i, L in enumerate(singles6[b]) if L is None or L == line6)
                if opts:
                    assert len(opts) == 1
                    sstate6[b] = opts[0]
            if len(sstate6) < 10:
                continue

            touched6 = tuple(sorted(vals6))
            cset6 = set(complete6)
            states6 = tuple(7 if b in cset6 else 0 for b in touched6)
            alpha6 = R.nullspace_int(R.rowspace_key((line6,)), 6)
            rows6 = P.relation_rows_line_with_alphas(ext6g, touched6, states6, alpha6)
            assert len(alpha6) == 5 and R.rank_mod(rows6) == rank6
            trans6 = [tuple(rows6[j][k] for j in range(len(rows6))) for k in range(15)]
            assert D5.F.rank_mod_rows(trans6) == rank6
            idx6 = {b:i for i,b in enumerate(complete6)}
            fn6 = {b: singleton_functional(ext6g,b,s,idx6,len(complete6),alpha6) for b,s in sstate6.items()}
            if D5.F.rank_mod_rows(trans6 + list(fn6.values())) - rank6 < 10:
                continue
            witnesses += 1
            max_fn_width = max(max_fn_width, len(rows6))
            for row in trans6 + list(fn6.values()):
                max_fn_norm2 = max(max_fn_norm2, sum(x*x for x in row))

            empty_blocks = {b for b in vals6 if empty6[b] == line6}
            generators = {b for b in vals6 if empty6[b] == line6 or any(L == line6 for L in singles6[b])}
            zero = tuple(line6) + (0,)
            for cyc in all_cycles.difference(ext6):
                cmap, cb = cycle_maps[cyc], cycle_blocks[cyc]
                profiles = {b: P.extended_block_profile(vals6.get(b), xy) for b,xy in cmap.items()}
                candidates = set()
                if generators - cb:
                    candidates.add(zero)
                for b in cb & blocks6:
                    e7, s7 = profiles[b]
                    if empty6[b] == line6 and e7 is not None:
                        candidates.add(e7)
                    for i,L in enumerate(singles6[b]):
                        if L == line6 and s7[i] is not None:
                            candidates.add(s7[i])
                candidates = {L for L in candidates if S.primitive_line(L[:6]) == line6}

                for line7 in candidates:
                    added = set(cb - blocks6)
                    for b in empty_blocks:
                        if (profiles[b][0] if b in cb else zero) != line7:
                            added.add(b)
                    complete7 = cset6 | added
                    if deficiency(complete7) != 5:
                        continue
                    sline7 = {}
                    cap7 = 0
                    for b in complete7:
                        lines = profiles[b][1] if b in cb else tuple(append0(L) for L in singles6[b])
                        sline7[b] = lines
                        cap7 += any(L is None or L == line7 for L in lines)
                    if cap7 < 11:
                        continue
                    lifts += 1
                    cap_census[cap7] += 1

                    kept = []
                    for b,state in sstate6.items():
                        L = sline7[b][P.STATE_INDEX[state]]
                        if L is None or L == line7:
                            kept.append(b)
                    if len(kept) < 10 or D5.F.rank_mod_rows(trans6 + [fn6[b] for b in kept]) - rank6 < 10:
                        continue
                    retained_lifts += 1

                    complete7 = tuple(sorted(complete7))
                    touched7 = tuple(sorted(blocks6 | cb))
                    states7 = tuple(7 if b in set(complete7) else 0 for b in touched7)
                    ext7g = ext6g + (local_to_global[cyc],)
                    alpha7 = R.nullspace_int(R.rowspace_key((line7,)), 7)
                    rows7 = P.relation_rows_line_with_alphas(ext7g, touched7, states7, alpha7)
                    rank7 = len(complete7) - 5
                    assert len(alpha7) == 6 and R.rank_mod(rows7) == rank7
                    trans7 = [tuple(rows7[j][k] for j in range(len(rows7))) for k in range(15)]
                    assert D5.F.rank_mod_rows(trans7) == rank7
                    idx7 = {b:i for i,b in enumerate(complete7)}
                    fn7 = []
                    option_count = 0
                    for b in complete7:
                        opts = tuple((1,2,4)[i] for i,L in enumerate(sline7[b]) if L is None or L == line7)
                        option_count += len(opts)
                        fn7.extend(singleton_functional(ext7g,b,s,idx7,len(complete7),alpha7) for s in opts)
                    rows = trans7 + fn7
                    extra = D5.F.rank_mod_rows(rows) - rank7
                    assert extra <= 11
                    extra_census[(cap7, option_count, extra)] += 1
                    if extra == 11:
                        full11 += 1
                        if len(examples) < 20:
                            examples.append((ci, ext6, line6, cyc, line7, cap7, option_count))
                    max_fn_width = max(max_fn_width, len(rows7))
                    for row in rows:
                        max_fn_norm2 = max(max_fn_norm2, sum(x*x for x in row))
                    max_rel_rows = max(max_rel_rows, len(rows7))
                    for row in rows7:
                        max_rel_norm2 = max(max_rel_norm2, sum(x*x for x in row))

    if max_fn_width:
        assert R.P * R.P > max_fn_norm2 ** max_fn_width
    if max_rel_rows:
        assert R.P * R.P > max_rel_norm2 ** 15
    print("cover_range", (start,end))
    print("synchronized_states", sync)
    print("six_full_rank_witnesses", witnesses)
    print("seven_d5_capacity_ge11_lifts", lifts)
    print("retained_six_full_span_lifts", retained_lifts)
    print("seven_capacity_census", dict(sorted(cap_census.items())))
    print("seven_extra_census", dict(sorted(extra_census.items())))
    print("max_seven_extra_rank", max((k[2] for k in extra_census), default=0))
    print("seven_full_rank_lifts", full11)
    print("examples", examples)
    print("max_functional_row_norm_squared", max_fn_norm2)
    print("max_functional_width", max_fn_width)
    print("max_relation_row_norm_squared", max_rel_norm2)
    print("functional_hadamard_exact_rank_bound", (not max_fn_width) or R.P*R.P > max_fn_norm2**max_fn_width)
    print("relation_hadamard_exact_rank_bound", (not max_rel_rows) or R.P*R.P > max_rel_norm2**15)
    if full11:
        raise SystemExit("FAIL: seven-row singleton-functional rank 11 is attainable")
    print("PASS: no qualifying one-cycle lift reaches seven-row functional rank 11")


if __name__ == "__main__":
    main()
