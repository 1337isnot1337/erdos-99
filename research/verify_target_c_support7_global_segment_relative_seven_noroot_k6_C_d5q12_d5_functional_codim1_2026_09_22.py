#!/usr/bin/env python3
"""Codimension-one seven-row functional audit for C:(5,12,12), d6=5.

This is an optimized exact verifier for the sole remaining six-row-shadow
branch in the current eight-no-root k=7 split.  It uses two structural facts:

1. Along a compatible six-to-seven coefficient-line lift with d6=d7=5, the
   ten-dimensional six-row canonical left kernel embeds as a codimension-one
   subspace of the eleven-dimensional seven-row kernel.
2. A singleton state compatible on an old six-row canonical-complete block at
   seven rows was already compatible at six rows.  Therefore, once the
   retained old singleton functionals still span the six-row quotient, the
   only possible eleventh functional direction can come from a newly complete
   block.

For each qualifying lift the verifier chooses ten retained old singleton
functionals that form a basis modulo the six-row canonical relation columns,
rebuilds their seven-row functionals in a nullspace basis adapted to the
six-row embedding, and tests only compatible singleton functionals on newly
complete blocks for one additional modular rank.  A full-cover result with no
rank increment closes the d6=5 branch.  Modular ranks are certified over Q by
the same P=2^127-1 Lucas-Lehmer/Hadamard argument as the preceding audits.
"""

from collections import Counter
from pathlib import Path
import argparse
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_seven_noroot_k6_C_d5q12_d5_functional_lift_2026_09_22.py"
spec = importlib.util.spec_from_file_location("e99_d5_seven_functional", BASE)
P = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(P)
D5, B, S, R = P.D5, P.B, P.S, P.R
LIFT = P.P
MOD = R.P


class ModBasis:
    """Incremental row basis over F_MOD with normalized pivots."""

    def __init__(self, rows=()):
        self.rows = {}
        for row in rows:
            self.add(row)

    def reduce(self, row):
        out = [int(x) % MOD for x in row]
        for pivot in sorted(self.rows):
            q = out[pivot]
            if q:
                base = self.rows[pivot]
                out = [(x - q * y) % MOD for x, y in zip(out, base)]
        return out

    def add(self, row):
        out = self.reduce(row)
        pivot = next((i for i, x in enumerate(out) if x), None)
        if pivot is None:
            return False
        inv = pow(out[pivot], MOD - 2, MOD)
        out = [(x * inv) % MOD for x in out]
        self.rows[pivot] = out
        return True

    @property
    def rank(self):
        return len(self.rows)


def append0(line):
    return None if line is None else tuple(line) + (0,)


def adapted_alphas(line6, line7):
    """Return a seven-row nullspace basis whose first five vectors are N6 x {0}."""
    alpha6 = tuple(R.nullspace_int(R.rowspace_key((line6,)), 6))
    assert len(alpha6) == 5
    embedded = tuple(tuple(a) + (0,) for a in alpha6)
    for a in embedded:
        assert sum(x * y for x, y in zip(a, line7)) == 0

    standard7 = tuple(R.nullspace_int(R.rowspace_key((line7,)), 7))
    assert len(standard7) == 6
    base = ModBasis(embedded)
    assert base.rank == 5
    extra = None
    for a in standard7:
        trial = ModBasis(embedded)
        if trial.add(a):
            extra = tuple(a)
            break
    assert extra is not None
    out = embedded + (extra,)
    assert R.rank_mod(out) == 6
    return alpha6, out


def independent_old_blocks(trans6, fn6, blocks, target=10):
    """Choose target old singleton functionals independent modulo trans6."""
    basis = ModBasis(trans6)
    base_rank = basis.rank
    chosen = []
    for block in blocks:
        if basis.add(fn6[block]):
            chosen.append(block)
            if len(chosen) == target:
                break
    return tuple(chosen), basis.rank - base_rank


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cover-cache")
    ap.add_argument("--cover-start", type=int, default=0)
    ap.add_argument("--cover-end", type=int)
    ap.add_argument("--crosscheck", action="store_true")
    a = ap.parse_args()

    assert R.lucas_lehmer_127()
    assert max(sum(x * x for x in row) for row in S.COMPLETE_T) == 12
    assert MOD * MOD > 12 ** 15

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

    sync = witnesses = lifts = retained_full = 0
    new_singleton_tests = full11 = 0
    cap_census = Counter()
    new_complete_census = Counter()
    new_singleton_census = Counter()
    examples = []
    max_fn_norm2 = max_fn_width = max_rel_norm2 = 0

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
            cset6 = set(complete6)

            sstate6 = {}
            for b in complete6:
                opts = tuple(
                    (1, 2, 4)[i]
                    for i, local_line in enumerate(singles6[b])
                    if local_line is None or local_line == line6
                )
                # Any two singleton constraints in one canonical-complete block
                # would force both quotient component rows into P6, making the
                # block canonical-empty.
                assert len(opts) <= 1
                if opts:
                    sstate6[b] = opts[0]
            if len(sstate6) < 10:
                continue

            touched6 = tuple(sorted(vals6))
            states6 = tuple(7 if b in cset6 else 0 for b in touched6)
            alpha6 = tuple(R.nullspace_int(R.rowspace_key((line6,)), 6))
            assert len(alpha6) == 5
            rows6 = LIFT.relation_rows_line_with_alphas(ext6g, touched6, states6, alpha6)
            assert R.rank_mod(rows6) == rank6
            trans6 = [tuple(rows6[j][k] for j in range(len(rows6))) for k in range(15)]
            assert D5.F.rank_mod_rows(trans6) == rank6
            idx6 = {b: i for i, b in enumerate(complete6)}
            fn6 = {
                b: P.singleton_functional(ext6g, b, state, idx6, len(complete6), alpha6)
                for b, state in sstate6.items()
            }
            if D5.F.rank_mod_rows(trans6 + list(fn6.values())) - rank6 < 10:
                continue
            witnesses += 1

            max_fn_width = max(max_fn_width, len(rows6))
            for row in trans6 + list(fn6.values()):
                max_fn_norm2 = max(max_fn_norm2, sum(x * x for x in row))

            empty_blocks = {b for b in vals6 if empty6[b] == line6}
            generators = {
                b
                for b in vals6
                if empty6[b] == line6 or any(local_line == line6 for local_line in singles6[b])
            }
            zero = tuple(line6) + (0,)

            for cyc in all_cycles.difference(ext6):
                cmap, cb = cycle_maps[cyc], cycle_blocks[cyc]
                profiles = {b: LIFT.extended_block_profile(vals6.get(b), xy) for b, xy in cmap.items()}
                candidates = set()
                if generators - cb:
                    candidates.add(zero)
                for b in cb & blocks6:
                    e7, s7 = profiles[b]
                    if empty6[b] == line6 and e7 is not None:
                        candidates.add(e7)
                    for i, local6 in enumerate(singles6[b]):
                        if local6 == line6 and s7[i] is not None:
                            candidates.add(s7[i])
                candidates = {line7 for line7 in candidates if S.primitive_line(line7[:6]) == line6}

                for line7 in candidates:
                    added = set(cb - blocks6)
                    for b in empty_blocks:
                        empty7 = profiles[b][0] if b in cb else zero
                        if empty7 != line7:
                            added.add(b)
                    complete7_set = cset6 | added
                    if deficiency(complete7_set) != 5:
                        continue

                    compatible_state7 = {}
                    cap7 = 0
                    for b in complete7_set:
                        lines = profiles[b][1] if b in cb else tuple(append0(L) for L in singles6[b])
                        opts = tuple(
                            (1, 2, 4)[i]
                            for i, local_line in enumerate(lines)
                            if local_line is None or local_line == line7
                        )
                        # Universal singleton uniqueness on a canonical-complete
                        # block: two compatible singleton directions imply the
                        # empty constraint is contained in P7.
                        assert len(opts) <= 1
                        if opts:
                            compatible_state7[b] = opts[0]
                            cap7 += 1
                    if cap7 < 11:
                        continue
                    lifts += 1
                    cap_census[cap7] += 1

                    kept = tuple(sorted(b for b, state in sstate6.items() if compatible_state7.get(b) == state))
                    if len(kept) < 10:
                        continue
                    chosen, old_extra = independent_old_blocks(trans6, fn6, kept, 10)
                    if old_extra < 10:
                        continue
                    assert len(chosen) == 10
                    retained_full += 1

                    complete7 = tuple(sorted(complete7_set))
                    new_complete = tuple(sorted(complete7_set - cset6))
                    new_complete_census[len(new_complete)] += 1
                    new_compatible = tuple(b for b in new_complete if b in compatible_state7)
                    new_singleton_census[len(new_compatible)] += 1

                    touched7 = tuple(sorted(blocks6 | cb))
                    states7 = tuple(7 if b in complete7_set else 0 for b in touched7)
                    ext7g = ext6g + (local_to_global[cyc],)
                    alpha6_check, alpha7 = adapted_alphas(line6, line7)
                    assert alpha6_check == alpha6
                    rows7 = LIFT.relation_rows_line_with_alphas(ext7g, touched7, states7, alpha7)
                    rank7 = len(complete7) - 5
                    assert R.rank_mod(rows7) == rank7
                    trans7 = [tuple(rows7[j][k] for j in range(len(rows7))) for k in range(15)]
                    assert D5.F.rank_mod_rows(trans7) == rank7
                    idx7 = {b: i for i, b in enumerate(complete7)}

                    retained_fn7 = [
                        P.singleton_functional(
                            ext7g,
                            b,
                            sstate6[b],
                            idx7,
                            len(complete7),
                            alpha7,
                        )
                        for b in chosen
                    ]
                    base_rows = trans7 + retained_fn7
                    base_basis = ModBasis(base_rows)
                    # Kernel-injection/codimension-one lemma guarantees these
                    # ten old functionals remain independent modulo the seven-
                    # row canonical relation columns.  Keep the assertion as an
                    # implementation-level audit of the adapted basis.
                    assert base_basis.rank == rank7 + 10

                    max_fn_width = max(max_fn_width, len(rows7))
                    for row in base_rows:
                        max_fn_norm2 = max(max_fn_norm2, sum(x * x for x in row))
                    for row in rows7:
                        max_rel_norm2 = max(max_rel_norm2, sum(x * x for x in row))

                    hit = None
                    for b in new_compatible:
                        state = compatible_state7[b]
                        fn = P.singleton_functional(
                            ext7g,
                            b,
                            state,
                            idx7,
                            len(complete7),
                            alpha7,
                        )
                        new_singleton_tests += 1
                        max_fn_norm2 = max(max_fn_norm2, sum(x * x for x in fn))
                        if any(base_basis.reduce(fn)):
                            hit = (b, state)
                            break
                    if a.crosscheck:
                        all_fn7 = [
                            P.singleton_functional(
                                ext7g,
                                b,
                                state,
                                idx7,
                                len(complete7),
                                alpha7,
                            )
                            for b, state in compatible_state7.items()
                        ]
                        full_extra = D5.F.rank_mod_rows(trans7 + all_fn7) - rank7
                        assert full_extra in (10, 11)
                        assert (full_extra == 11) == (hit is not None)

                    if hit is not None:
                        full11 += 1
                        if len(examples) < 20:
                            examples.append(
                                (ci, ext6, line6, cyc, line7, cap7, new_complete, hit)
                            )

    if max_fn_width:
        assert MOD * MOD > max_fn_norm2 ** max_fn_width
    if max_rel_norm2:
        assert MOD * MOD > max_rel_norm2 ** 15

    print("cover_range", (start, end))
    print("synchronized_states", sync)
    print("six_full_rank_witnesses", witnesses)
    print("seven_d5_capacity_ge11_lifts", lifts)
    print("retained_six_full_span_lifts", retained_full)
    print("seven_capacity_census", dict(sorted(cap_census.items())))
    print("new_complete_block_census", dict(sorted(new_complete_census.items())))
    print("new_compatible_singleton_census", dict(sorted(new_singleton_census.items())))
    print("new_singleton_functionals_tested", new_singleton_tests)
    print("seven_full_rank_lifts", full11)
    print("examples", examples)
    print("max_functional_row_norm_squared", max_fn_norm2)
    print("max_functional_width", max_fn_width)
    print("max_relation_row_norm_squared", max_rel_norm2)
    print("functional_hadamard_exact_rank_bound", (not max_fn_width) or MOD * MOD > max_fn_norm2 ** max_fn_width)
    print("relation_hadamard_exact_rank_bound", (not max_rel_norm2) or MOD * MOD > max_rel_norm2 ** 15)
    if full11:
        raise SystemExit("FAIL: a newly complete singleton supplies the eleventh seven-row functional direction")
    print("PASS: no newly complete singleton supplies the eleventh seven-row functional direction")


if __name__ == "__main__":
    main()
