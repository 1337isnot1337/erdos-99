#!/usr/bin/env python3
"""Independent exact-Q cross-check of the t=4,k=4 rank-density barrier.

This verifier intentionally uses a different pruning argument from the primary
k=4 verifier and reranks every retained matrix with Fraction arithmetic over
Q.  It is a durable check of the production modular/Hadamard certificate.

For four fixed no-root rows, k=4 means the global external coefficient-
constraint space has rank zero.  Let A0 complete every touched root-0 quotient
block.  Any k=4 state A is a row-subset of A0, so delta(A)<=delta(A0).
If s touched blocks are singletons and d are doubletons, then

    p = s + 2d,             removed rows R = 2s + d.

Only p<=7 can violate the crude t=4,k=4 bound.  The exact all-complete defect
D0 over the 1,186 S7 orbit representatives lies in {10,13,16,19}.  Since
p<=7 implies R<=14, only R>D0 can still be dangerous under the subset bound.
That leaves (s,d)=(5,1),(6,0),(7,0) when D0=10 and (7,0) when D0=13.
The actual orbit profiles leave exactly 367 states.  All are reranked here over
Q with RationalBasis/Fraction, with no floating-point or modular rank decision.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py"
spec = importlib.util.spec_from_file_location("relative_four_noroot_k2_for_k4_fraction", BASE)
R = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(R)

EXPECTED_ALLOWED = {
    (1, 3, 5, 6, 7),
    (2, 3, 5, 6, 7),
    (3, 4, 5, 6, 7),
    (3, 5, 6, 7),
}
EXPECTED_BASE_DEFECTS = {10: 10, 13: 156, 16: 971, 19: 49}
EXPECTED_DANGEROUS_PATTERNS = {
    10: ((5, 1), (6, 0), (7, 0)),
    13: ((7, 0),),
    16: (),
    19: (),
}


def exact_relation_defect(ext, touched, states):
    rows = R.relation_rows_int(ext, touched, states, ())
    delta = R.exact_rank(rows)
    n = 4 + sum(R.STATES[state][1] for state in states)
    return n - 3 * delta, delta, len(rows)


def singleton_state(ext, block):
    out = tuple(
        state
        for state in (1, 2, 4)
        if R.local_constraint_key(ext, block, state) == ()
    )
    assert len(out) in (0, 1)
    return out[0] if out else None


def dangerous_patterns(base_defect):
    out = []
    for singletons in range(8):
        for doubletons in range(4):
            p = singletons + 2 * doubletons
            removed = 2 * singletons + doubletons
            if p <= 7 and removed > base_defect:
                out.append((singletons, doubletons))
    return tuple(sorted(out))


def dangerous_states(ext, touched, base_defect):
    singleton_positions = tuple(
        q
        for q, block in enumerate(touched)
        if singleton_state(ext, block) is not None
    )
    m = len(touched)

    for s, d in dangerous_patterns(base_defect):
        assert d <= 1, (base_defect, s, d)
        for singles in combinations(singleton_positions, s):
            single_set = set(singles)
            if d == 0:
                states = [7] * m
                for q in singles:
                    states[q] = singleton_state(ext, touched[q])
                yield tuple(states)
                continue

            for qd in range(m):
                if qd in single_set:
                    continue
                for double_state in (3, 5, 6):
                    assert R.local_constraint_key(ext, touched[qd], double_state) == ()
                    states = [7] * m
                    for q in singles:
                        states[q] = singleton_state(ext, touched[q])
                    states[qd] = double_state
                    yield tuple(states)


def main():
    assert {
        d: dangerous_patterns(d) for d in EXPECTED_BASE_DEFECTS
    } == EXPECTED_DANGEROUS_PATTERNS

    orbits = R.four_no_root_orbits()
    assert len(orbits) == 1186

    allowed_sets = Counter()
    base_defects = Counter()
    dangerous_classes = Counter()
    dangerous_orbits = set()
    dangerous_count = 0
    min_dangerous_defect = None
    min_record = None

    for orbit_index, (ext, orbit_size, touched) in enumerate(orbits):
        for block in touched:
            allowed = tuple(
                state
                for state in range(8)
                if R.local_constraint_key(ext, block, state) == ()
            )
            assert allowed in EXPECTED_ALLOWED, (orbit_index, block, allowed)
            allowed_sets[allowed] += 1

        complete = tuple(7 for _ in touched)
        base_defect, base_delta, _ = exact_relation_defect(ext, touched, complete)
        base_defects[base_defect] += 1

        seen = set()
        for states in dangerous_states(ext, touched, base_defect):
            if states in seen:
                continue
            seen.add(states)

            p = sum(R.STATES[state][5] for state in states)
            removed = sum(
                3 - R.STATES[state][1]
                for state in states
                if state != 7
            )
            assert p <= 7
            assert removed > base_defect

            defect, delta, _ = exact_relation_defect(ext, touched, states)
            dangerous_count += 1
            dangerous_orbits.add(orbit_index)
            dangerous_classes[(base_defect, p, removed)] += 1
            if min_dangerous_defect is None or defect < min_dangerous_defect:
                min_dangerous_defect = defect
                min_record = (
                    orbit_index,
                    orbit_size,
                    tuple(touched),
                    base_defect,
                    base_delta,
                    p,
                    removed,
                    defect,
                    delta,
                    states,
                )
            assert defect >= 0, min_record

    assert dict(sorted(base_defects.items())) == EXPECTED_BASE_DEFECTS
    assert set(allowed_sets) == EXPECTED_ALLOWED
    assert dangerous_count == 367
    assert len(dangerous_orbits) == 101
    assert dict(dangerous_classes) == {(13, 7, 14): 367}
    assert min_dangerous_defect == 8

    print("PASS: exact-Q cross-check of four-no-root k=4 rank-density branch")
    print("four_no_root_subsets", 4_780_230)
    print("S7_orbits", len(orbits))
    print("allowed_local_state_sets", dict(sorted(allowed_sets.items(), key=lambda item: repr(item[0]))))
    print("all_complete_defects", dict(sorted(base_defects.items())))
    print("dangerous_patterns", EXPECTED_DANGEROUS_PATTERNS)
    print("dangerous_orbits", len(dangerous_orbits))
    print("dangerous_classes", dict(sorted(dangerous_classes.items())))
    print("dangerous_states", dangerous_count)
    print("min_exact_defect", min_dangerous_defect)
    print("min_record", min_record)
    print("rank_arithmetic", "Fraction/Q")


if __name__ == "__main__":
    main()
