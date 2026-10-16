#!/usr/bin/env python3
"""Exact all-touch singleton-capacity audit for synchronized six-row rank-one P.

This reuses the committed exact six-no-root k=5 orbit cover and local-constraint
machinery, but deliberately does NOT impose the six-row counterexample
support-overlap condition on individual root blocks.  It is therefore valid for
generic six-row shadows of a seven-row state, where a selected singleton block
may be touched by only one of the six surviving no-root rows.

For every S7-cover representative of six no-root cycles and every obtainable
rank-one coefficient line P whose primitive generator has support at least two,
we form the virtual-canonical complete set C and count all blocks in C that can
be replaced by a singleton compatible with P.  Exact complete-block deficiency
is computed modulo 2^127-1 under the same Hadamard certificate as the committed
six-row verifier.

The only statistics needed downstream are:
  * no deficiency-two state has singleton capacity >= 4;
  * deficiency-three states with capacity >= 6 have the exact census below;
  * deficiency-four states with capacity >= 8 have the exact census below.
"""

from collections import Counter
import contextlib
import importlib.util
import io
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_six_noroot_k5_2026_09_20.py"
spec = importlib.util.spec_from_file_location("relative_six_noroot_k5_alltouch_base", BASE)
S = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(S)
R = S.R


def main():
    assert R.lucas_lehmer_127()
    assert max(sum(x * x for x in row) for row in S.COMPLETE_T) == 12
    assert R.P * R.P > 12 ** 15

    keys, five_orbits, orbit_sizes, augmentation_candidates = S.K.five_no_root_orbits()
    assert len(five_orbits) == 20451
    assert sum(orbit_sizes) == 96560646
    assert augmentation_candidates == 20475

    six_cover = S.six_augmentation_cover(keys, five_orbits)
    assert len(six_cover) == 325955
    _local_to_global, info = S.local_cycle_data(keys)

    rank_cache = {}
    synchronized_states = 0
    capacity_ge4_states = 0
    d2_capacity_ge4 = Counter()
    d3_capacity_ge6 = Counter()
    d4_capacity_ge8 = Counter()

    def deficiency(complete_set):
        cached = rank_cache.get(complete_set)
        if cached is not None:
            return cached
        d = len(complete_set) - R.rank_mod([S.COMPLETE_T[b] for b in complete_set])
        rank_cache[complete_set] = d
        return d

    for ext_local in six_cover:
        values, lines, empty_line, singleton_lines = S.block_profile(ext_local, info)
        for line in lines:
            # Exactly the synchronized condition needed by the six-row
            # containment theorem.  No per-block touch multiplicity filter is
            # used in this audit.
            if sum(x != 0 for x in line) < 2:
                continue
            synchronized_states += 1

            complete_set = tuple(
                sorted(block for block in values if empty_line[block] != line)
            )
            capable = sum(
                any(local is None or local == line for local in singleton_lines[block])
                for block in complete_set
            )
            if capable < 4:
                continue
            capacity_ge4_states += 1

            d = deficiency(complete_set)
            if d == 2:
                d2_capacity_ge4[capable] += 1
            if d == 3 and capable >= 6:
                d3_capacity_ge6[capable] += 1
            if d == 4 and capable >= 8:
                d4_capacity_ge8[capable] += 1

    assert synchronized_states == 1751870
    assert capacity_ge4_states == 1750684
    assert len(rank_cache) == 70978
    assert dict(d2_capacity_ge4) == {}
    assert dict(sorted(d3_capacity_ge6.items())) == {
        6: 485,
        7: 78,
        8: 116,
        9: 144,
        10: 64,
    }
    assert dict(sorted(d4_capacity_ge8.items())) == {
        8: 15366,
        9: 13536,
        10: 12922,
        11: 11898,
        12: 8614,
        13: 3733,
        14: 762,
    }

    print("PASS: synchronized six-row all-touch singleton-capacity audit")
    print("six_augmentation_cover", len(six_cover))
    print("synchronized_rank_one_states", synchronized_states)
    print("capacity_ge4_states", capacity_ge4_states)
    print("unique_complete_sets_ranked", len(rank_cache))
    print("d2_capacity_ge4", dict(d2_capacity_ge4))
    print("d3_capacity_ge6", dict(sorted(d3_capacity_ge6.items())))
    print("d3_capacity_ge7_total", sum(v for c, v in d3_capacity_ge6.items() if c >= 7))
    print("d3_capacity_ge8_total", sum(v for c, v in d3_capacity_ge6.items() if c >= 8))
    print("d4_capacity_ge8", dict(sorted(d4_capacity_ge8.items())))
    print("d4_capacity_ge9_total", sum(v for c, v in d4_capacity_ge8.items() if c >= 9))
    print("max_complete_relation_row_norm_squared", 12)
    print("hadamard_exact_rank_bound", R.P * R.P > 12 ** 15)


if __name__ == "__main__":
    main()
