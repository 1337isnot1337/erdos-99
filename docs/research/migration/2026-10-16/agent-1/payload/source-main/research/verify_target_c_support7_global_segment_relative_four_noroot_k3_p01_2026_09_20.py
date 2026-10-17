#!/usr/bin/env python3
"""Exact t=4, k=3, p<=1 rank-density barrier for the Target-C four-cycle system.

For four no-root four-cycles in the k=3 branch, the external coefficient
constraint space is a line.  This verifier handles p=0 and p=1 exactly.
For a fixed line and fixed singleton choice, leave every other touched block
empty whenever its empty-block constraint lies in the line and complete it
otherwise.  Every other state in the same class is obtained by completing
additional compatible empty blocks; each such completion adds three selected
rows and at most one T-rank, so |A|-3*delta cannot decrease.

The coordinate/rank engine is imported from the audited k=2 verifier.  Its
small integer T-ranks are computed modulo P=2^127-1 with Lucas-Lehmer and
Hadamard checks, so the rank decisions are exact over Q.
"""
from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import contextlib, importlib.util, io

BASE = Path('research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py')
spec = importlib.util.spec_from_file_location('relative_four_noroot_k2_for_k3p01', BASE)
R = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(R)


def candidate_lines(ext, touched):
    out = set()
    for b in touched:
        for state in (0, 1, 2, 4):
            key = R.local_constraint_key(ext, b, state)
            if len(key) == 1:
                out.add(key)
    return tuple(sorted(out, key=repr))


def canonical_baseline(ext, touched, line):
    states = []
    for b in touched:
        empty = R.local_constraint_key(ext, b, 0)
        states.append(0 if R.is_subspace(empty, line) else 7)
    key = ()
    for b, state in zip(touched, states):
        key = R.union_key(key, R.local_constraint_key(ext, b, state))
    return tuple(states) if key == line else None


def singleton_states(ext, touched, line):
    base = [0 if R.is_subspace(R.local_constraint_key(ext, b, 0), line) else 7 for b in touched]
    for q, b in enumerate(touched):
        for state in (1, 2, 4):
            key = R.local_constraint_key(ext, b, state)
            if not R.is_subspace(key, line):
                continue
            states = list(base)
            states[q] = state
            union = ()
            for bb, ss in zip(touched, states):
                union = R.union_key(union, R.local_constraint_key(ext, bb, ss))
            if union == line:
                yield tuple(states)


def scan(orbits, start, stop):
    R.MAX_NORM2 = 0
    counts = Counter()
    minima = {0: None, 1: None}
    line_count = Counter()
    touched_count = Counter()
    orbit_size_count = Counter()
    negatives = []
    for oi in range(start, stop):
        ext, orbit_size, touched = orbits[oi]
        orbit_size_count[orbit_size] += 1
        touched_count[len(touched)] += 1
        lines = candidate_lines(ext, touched)
        line_count[len(lines)] += 1
        seen = set()
        for line in lines:
            states = canonical_baseline(ext, touched, line)
            if states is not None:
                sig = (line, states)
                if sig not in seen:
                    seen.add(sig)
                    defect, delta, nrel = R.relation_defect(ext, touched, states, line)
                    counts[0] += 1
                    minima[0] = defect if minima[0] is None else min(minima[0], defect)
                    if defect < 0:
                        negatives.append((oi, 0, defect, ext, touched, line, states, delta, nrel))
                        break
            for states in singleton_states(ext, touched, line):
                sig = (line, states)
                if sig in seen:
                    continue
                seen.add(sig)
                defect, delta, nrel = R.relation_defect(ext, touched, states, line)
                counts[1] += 1
                minima[1] = defect if minima[1] is None else min(minima[1], defect)
                if defect < 0:
                    negatives.append((oi, 1, defect, ext, touched, line, states, delta, nrel))
                    break
            if negatives:
                break
        if negatives:
            break
    return {
        'start': start,
        'stop': stop,
        'orbits_checked': stop - start,
        'canonical_p0_states': counts[0],
        'canonical_p1_states': counts[1],
        'canonical_states': counts[0] + counts[1],
        'min_defect_p0': minima[0],
        'min_defect_p1': minima[1],
        'negative_states': len(negatives),
        'first_negative': negatives[0] if negatives else None,
        'candidate_line_count': sum(k * v for k, v in line_count.items()),
        'line_count_distribution': dict(sorted(line_count.items())),
        'touched_block_distribution': dict(sorted(touched_count.items())),
        'orbit_size_distribution': dict(sorted(orbit_size_count.items())),
        'max_relation_row_norm_squared': R.MAX_NORM2,
    }


def main():
    p = ArgumentParser()
    p.add_argument('--orbit-start', type=int, default=0)
    p.add_argument('--orbit-end', type=int)
    a = p.parse_args()
    assert R.lucas_lehmer_127()
    orbits = R.four_no_root_orbits()
    end = len(orbits) if a.orbit_end is None else a.orbit_end
    assert 0 <= a.orbit_start <= end <= len(orbits)
    result = scan(orbits, a.orbit_start, end)
    assert result['negative_states'] == 0, result['first_negative']
    B = max(1, result['max_relation_row_norm_squared'])
    assert R.P * R.P > B ** 15
    if a.orbit_start == 0 and end == len(orbits):
        assert result['candidate_line_count'] == 7474
        assert result['canonical_p0_states'] == 5120
        assert result['canonical_p1_states'] == 95903
    print('PASS: four-no-root k=3,p<=1 rank-density branch')
    print('four_no_root_subsets', 4_780_230)
    print('S7_orbits', len(orbits))
    print('orbit_range', a.orbit_start, end)
    print('orbits_checked', result['orbits_checked'])
    print('candidate_lines', result['candidate_line_count'])
    print('canonical_p0_states', result['canonical_p0_states'])
    print('canonical_p1_states', result['canonical_p1_states'])
    print('canonical_states', result['canonical_states'])
    print('min_defect_p0', result['min_defect_p0'])
    print('min_defect_p1', result['min_defect_p1'])
    print('negative_states', result['negative_states'])
    print('max_relation_row_norm_squared', result['max_relation_row_norm_squared'])
    print('hadamard_exact_rank_bound', R.P * R.P > B ** 15)
    print('line_count_distribution', result['line_count_distribution'])
    print('touched_block_distribution', result['touched_block_distribution'])
    print('orbit_size_distribution', result['orbit_size_distribution'])


if __name__ == '__main__':
    main()
