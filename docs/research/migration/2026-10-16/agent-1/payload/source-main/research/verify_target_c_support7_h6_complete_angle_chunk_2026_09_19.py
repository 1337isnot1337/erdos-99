#!/usr/bin/env python3
"""Chunkable exact verifier for the generic support-seven H6 complete-angle lift.

The 14,174 input states are the post-interior-force/chirotope cells produced by
verify_target_c_support7_h6_triangle_simplex_reduction_2026_09_19.py.

For a requested half-open state-index range, this script builds the full
85-variable affine angular relaxation:
  * 35 force-turn variables;
  * six ordered reciprocal-ray gaps at each hull vertex 0..5;
  * seven cyclic reciprocal-ray gaps at each interior vertex 6,7;
  * all 56 reciprocal triangle angle-sum equations;
  * all pairwise angle ties among the five present force rays at each of the
    seven non-ground physical vertices;
  * all strict turn-simplex, ray-order, hull-span, and interior-chirotope
    facets.

scipy is used only to discover a dual support.  Every reported exclusion is
converted to fractions.Fraction and checked coefficientwise exactly.  A
floating-point failure cannot exclude a state.

Default range 0:500 is a fixed regression block and must reproduce 270 exact
Farkas exclusions and 230 affine survivors.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io
import sys

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
PREV_PATH = HERE / "verify_target_c_support7_h6_triangle_simplex_reduction_2026_09_19.py"
spec = importlib.util.spec_from_file_location("h6_tri", PREV_PATH)
tri = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(tri)

base = tri.base
NG = tri.NG
ALL = tuple(range(8))
edge = tri.edge
NX = tri.NVAR
assert NX == 35


def interior_order(chi, v):
    others = [a for a in ALL if a != v]
    anchor = min(others)
    pos = [
        a for a in others
        if a != anchor and base.chi_value(chi, v, anchor, a) > 0
    ]
    neg = [
        a for a in others
        if a != anchor and base.chi_value(chi, v, anchor, a) < 0
    ]

    def ordered(group):
        ranks = {
            a: sum(
                base.chi_value(chi, v, b, a) > 0
                for b in group if b != a
            )
            for a in group
        }
        assert sorted(ranks.values()) == list(range(len(group)))
        out = sorted(group, key=lambda a: ranks[a])
        assert all(
            base.chi_value(chi, v, out[i], out[j]) > 0
            for i in range(len(out))
            for j in range(i + 1, len(out))
        )
        return out

    out = (anchor, *ordered(pos), *ordered(neg))
    assert len(out) == 7 and set(out) == set(others)
    assert all(
        base.chi_value(chi, v, out[i], out[(i + 1) % 7]) > 0
        for i in range(7)
    )
    return out


def orders_for_state(state):
    _, _, _, raws, chi, _, _ = state
    return {
        **{v: raws[v] for v in range(6)},
        6: interior_order(chi, 6),
        7: interior_order(chi, 7),
    }


START = {}
cur = NX
for v in range(8):
    START[v] = cur
    cur += 7 if v in (6, 7) else 6
NVAR = cur
assert NVAR == 85


def gap_idx(v, k):
    return START[v] + k


def zero_row():
    return [0] * NVAR


def directed_arc_row(orders, v, a, b):
    order = orders[v]
    pa = order.index(a)
    pb = order.index(b)
    row = zero_row()
    if v <= 5:
        assert pa <= pb
        for k in range(pa, pb):
            row[gap_idx(v, k)] += 1
    else:
        k = pa
        while k != pb:
            row[gap_idx(v, k)] += 1
            k = (k + 1) % 7
    return row


def ordinary_angle(orders, chi, v, a, b):
    """Return (row,const) for the normalized ordinary angle in (0,1)."""
    if v <= 5:
        if orders[v].index(a) > orders[v].index(b):
            a, b = b, a
        return directed_arc_row(orders, v, a, b), Fraction(0)

    arc = directed_arc_row(orders, v, a, b)
    if base.chi_value(chi, v, a, b) > 0:
        return arc, Fraction(0)
    return [-z for z in arc], Fraction(2)


def add_eq(rows, rhs, labels, row, const, target, label):
    rows.append(row)
    rhs.append(Fraction(target) - Fraction(const))
    labels.append(label)


def build_system(state):
    _, _, missing, _, chi, _, signs = state
    cycles = {
        v: tri.force_cycle(v, missing, chi, signs)
        for v in NG
    }
    orders = orders_for_state(state)
    rows, rhs, labels = [], [], []

    # Seven physical pentagon turn sums.
    for v in NG:
        row = zero_row()
        for k in range(5):
            row[tri.VIDX[(v, k)]] = 1
        add_eq(rows, rhs, labels, row, 0, 2, ("F", v))

    # Interior reciprocal full-circle sums.
    for v in (6, 7):
        row = zero_row()
        for k in range(7):
            row[gap_idx(v, k)] = 1
        add_eq(rows, rhs, labels, row, 0, 2, ("RCIRCLE", v))

    # At each physical non-ground vertex, tie every pair of its five present
    # reciprocal rays to the exact signed-force raw angle.
    for v in NG:
        present = [0] + [
            j for j in NG
            if j != v and edge(v, j) not in missing
        ]
        assert len(present) == 5
        for a, b in combinations(present, 2):
            rr, rc = ordinary_angle(orders, chi, v, a, b)
            xr, xc = tri.raw_angle_affine(v, a, b, chi, signs, cycles)
            for j, z in enumerate(xr):
                rr[j] -= z
            add_eq(rows, rhs, labels, rr, rc - xc, 0, ("TIE", v, a, b))

    # All 56 reciprocal triangle angle sums, including missing relation pairs.
    for a, b, c in combinations(ALL, 3):
        row = zero_row()
        const = Fraction(0)
        for v, j, k in ((a, b, c), (b, a, c), (c, a, b)):
            ar, ac = ordinary_angle(orders, chi, v, j, k)
            row = [x + y for x, y in zip(row, ar)]
            const += ac
        add_eq(rows, rhs, labels, row, const, 1, ("TRI", a, b, c))

    facets = []

    # Physical pentagon turn-simplex facets q_k - 1/3 > 0.
    for v in NG:
        for k in range(5):
            row = zero_row()
            row[tri.VIDX[(v, k)]] += 1
            row[tri.VIDX[(v, (k + 1) % 5)]] += 1
            row[tri.VIDX[(v, (k + 3) % 5)]] -= 1
            facets.append((row, Fraction(-1, 3), ("Q", v, k)))

    # Strict reciprocal ray-gap positivity.
    for v in range(8):
        count = 7 if v in (6, 7) else 6
        for k in range(count):
            row = zero_row()
            row[gap_idx(v, k)] = 1
            facets.append((row, Fraction(0), ("RGAP", v, k)))

    # Hull interior-wedge bounds; H6 gives the stronger ground bound 2/3.
    for v in range(6):
        row = zero_row()
        for k in range(6):
            row[gap_idx(v, k)] -= 1
        facets.append((
            row,
            Fraction(2, 3) if v == 0 else Fraction(1),
            ("RSPAN", v),
        ))

    # At an interior reciprocal vertex, the chirotope chooses the ordinary
    # (< pi) member of the two complementary directed arcs.
    for v in (6, 7):
        others = [a for a in ALL if a != v]
        for a, b in combinations(others, 2):
            ar, ac = ordinary_angle(orders, chi, v, a, b)
            facets.append((
                [-z for z in ar],
                Fraction(1) - ac,
                ("RCHI", v, a, b),
            ))

    return rows, rhs, labels, facets


def numerical_candidate(system):
    rows, rhs, _, facets = system
    aeq = np.zeros((len(rows), NVAR + 1), dtype=float)
    aeq[:, :NVAR] = np.asarray(rows, dtype=float)
    beq = np.asarray(rhs, dtype=float)

    aub = np.zeros((len(facets), NVAR + 1), dtype=float)
    bub = np.zeros(len(facets), dtype=float)
    for i, (row, const, _) in enumerate(facets):
        aub[i, :NVAR] = -np.asarray(row, dtype=float)
        aub[i, -1] = 1.0
        bub[i] = float(const)

    objective = np.zeros(NVAR + 1, dtype=float)
    objective[-1] = -1.0
    result = linprog(
        objective,
        A_ub=aub,
        b_ub=bub,
        A_eq=aeq,
        b_eq=beq,
        bounds=[(None, None)] * (NVAR + 1),
        method="highs-ds",
    )
    if not result.success:
        return None, result
    return -result.fun, result


def exactify(system, result):
    rows, rhs, _, facets = system
    alpha = tuple(
        Fraction(float(-m)).limit_denominator(1_000_000)
        for m in result.ineqlin.marginals
    )
    mu = tuple(
        Fraction(float(m)).limit_denominator(1_000_000)
        for m in result.eqlin.marginals
    )
    if any(a < 0 for a in alpha) or sum(alpha) != 1:
        return None

    coeff = [Fraction(0) for _ in range(NVAR)]
    for a, (row, _, _) in zip(alpha, facets):
        if not a:
            continue
        for j, z in enumerate(row):
            if z:
                coeff[j] += a * Fraction(z)
    for m, row in zip(mu, rows):
        if not m:
            continue
        for j, z in enumerate(row):
            if z:
                coeff[j] += m * Fraction(z)
    if any(coeff):
        return None

    forced = (
        sum(a * Fraction(c) for a, (_, c, _) in zip(alpha, facets))
        - sum(m * Fraction(b) for m, b in zip(mu, rhs))
    )
    if forced > 0:
        return None
    active = [z for z in alpha + mu if z]
    den = max((z.denominator for z in active), default=1)
    return forced, den


def main():
    states = tri.collect_survivors()
    assert len(states) == 14174

    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 500
    assert 0 <= start <= end <= len(states)

    counts = Counter()
    by_type = Counter()
    by_pattern = Counter()
    values = Counter()
    max_denominator = 1
    bad = []

    for idx in range(start, end):
        state = states[idx]
        system = build_system(state)
        margin, result = numerical_candidate(system)
        if margin is None:
            counts["solver_failure"] += 1
            bad.append((idx, "solver_failure"))
            continue
        if margin > 1e-8:
            counts["affine_survivor"] += 1
            continue

        exact = exactify(system, result)
        if exact is None:
            counts["unexactified"] += 1
            bad.append((idx, "unexactified"))
            continue

        forced, den = exact
        counts["exact_exclusion"] += 1
        by_type[state[1]] += 1
        by_pattern["".join(map(str, state[5]))] += 1
        values["zero" if forced == 0 else "negative"] += 1
        max_denominator = max(max_denominator, den)

    if (start, end) == (0, 500):
        assert counts == Counter({
            "exact_exclusion": 270,
            "affine_survivor": 230,
        })
        assert not bad

    print("PASS")
    print(f"range: [{start},{end})")
    print("counts:", dict(counts))
    print("exact exclusions by missing type:", dict(by_type))
    print("exact exclusions by ground pattern:", dict(sorted(by_pattern.items())))
    print("certificate values:", dict(values))
    print("maximum exact dual denominator:", max_denominator)
    if bad:
        print("non-exclusions requiring attention:", bad)


if __name__ == "__main__":
    main()
