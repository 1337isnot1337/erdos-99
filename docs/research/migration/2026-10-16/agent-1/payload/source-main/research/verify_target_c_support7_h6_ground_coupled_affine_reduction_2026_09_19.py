#!/usr/bin/env python3
"""Exact-checking certificate for the generic support-seven H6 ground-coupled affine reduction.

Input: the 14,174 generic H6 cells from the interior-force/chirotope reduction.

This verifier strengthens the non-ground triangle/simplex relaxation by adding
six normalized consecutive angular gaps at reciprocal ground vertex 0.  If

    r_1, ..., r_7

are the seven raw reciprocal rays in the certified strict order at 0, write

    g_p = angle(r_p, r_{p+1}) / pi,      p=1,...,6.

The existing H6 ground-cone theorem gives the strict conditions

    g_p > 0,
    sum_p g_p < 2/3.

For every PRESENT non-ground relation edge ab, triangle 0ab has two angles that
are exact affine functions of the equilateral-pentagon turn variables at a and
b.  Its angle at 0 is the sum of the appropriate consecutive g_p because the
whole ground cone has width < 2*pi/3 < pi.  Thus each present edge supplies one
additional exact affine triangle equation.

The full relaxation used here consists of:

  * seven pentagon turn-sum equations sum x = 2;
  * every present non-ground reciprocal-triangle angle-sum equation;
  * fourteen ground-coupled triangle equations for triangles 0ab;
  * strict pentagon facets q = x_k+x_{k+1}-x_{k+3}-1/3 > 0;
  * six strict ground-gap facets g_p > 0;
  * the strict cone-width facet 2/3-sum g_p > 0.

As in the preceding verifier, scipy.optimize.linprog is only a dual-support
finder.  A cell is excluded only after its proposed Farkas certificate is
converted to fractions.Fraction and checked coefficientwise exactly.  If the
floating-point solver fails to reproduce the expected support, the verifier
fails; no numerical result is itself accepted as a proof.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import contextlib
import importlib.util
import io
from itertools import combinations

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
PREV_PATH = HERE / "verify_target_c_support7_h6_triangle_simplex_reduction_2026_09_19.py"
spec = importlib.util.spec_from_file_location("h6_tri", PREV_PATH)
tri = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(tri)

NG = tri.NG
N_TURN = tri.NVAR
N_GAP = 6
NVAR = N_TURN + N_GAP
GIDX = {p: N_TURN + p for p in range(N_GAP)}
edge = tri.edge


def extend_turn_row(row):
    return list(row) + [0] * N_GAP


def ground_arc_row(raw_ground_order, a, b):
    """Normalized smaller angle at 0 between rays 0a and 0b, as a gap sum."""
    pa = raw_ground_order.index(a)
    pb = raw_ground_order.index(b)
    lo, hi = sorted((pa, pb))
    row = [0] * NVAR
    for p in range(lo, hi):
        row[GIDX[p]] += 1
    return row


def extended_system(state, previous_system):
    _, _, missing, raws, chi, _, signs = state
    old_rows, old_rhs, old_labels, qrows, qlabels, cycles = previous_system

    rows = [extend_turn_row(row) for row in old_rows]
    rhs = list(old_rhs)
    labels = list(old_labels)

    # There are 21 possible non-ground edges and the missing 2-regular graph
    # has 7 edges, hence exactly 14 present relation edges.
    present_edge_count = 0
    for a, b in combinations(NG, 2):
        if edge(a, b) in missing:
            continue
        present_edge_count += 1

        row = ground_arc_row(raws[0], a, b)
        row_a, const_a = tri.raw_angle_affine(
            a, 0, b, chi, signs, cycles
        )
        row_b, const_b = tri.raw_angle_affine(
            b, 0, a, chi, signs, cycles
        )
        for j, value in enumerate(row_a):
            row[j] += value
        for j, value in enumerate(row_b):
            row[j] += value

        # ground_angle + angle_at_a + angle_at_b = 1
        rows.append(row)
        rhs.append(1 - const_a - const_b)
        labels.append(("GTRI", a, b))

    assert present_edge_count == 14
    assert len(rows) == len(old_rows) + 14

    # Every facet is represented as f(z) = constant + row*z > 0.
    facets = []
    for qrow, label in zip(qrows, qlabels):
        facets.append((
            extend_turn_row(qrow),
            Fraction(-1, 3),
            label,
        ))

    for p in range(N_GAP):
        row = [0] * NVAR
        row[GIDX[p]] = 1
        facets.append((row, Fraction(0), ("GGAP", p)))

    row = [0] * NVAR
    for p in range(N_GAP):
        row[GIDX[p]] = -1
    facets.append((row, Fraction(2, 3), ("GSPAN",)))

    assert len(facets) == 42
    return rows, rhs, labels, facets


def system_key(system):
    rows, rhs, _, facets = system
    return (
        tuple(tuple(row) for row in rows),
        tuple(rhs),
        tuple((tuple(row), constant) for row, constant, _ in facets),
    )


def numerical_dual_candidate(system):
    """Find a possible strict-feasibility obstruction; it is not a certificate."""
    rows, rhs, _, facets = system

    aeq = np.zeros((len(rows), NVAR + 1), dtype=float)
    aeq[:, :NVAR] = np.asarray(rows, dtype=float)
    beq = np.asarray(rhs, dtype=float)

    aub = np.zeros((len(facets), NVAR + 1), dtype=float)
    bub = np.zeros(len(facets), dtype=float)
    for i, (facet_row, constant, _) in enumerate(facets):
        # constant + facet_row*z >= t
        # <=> -facet_row*z + t <= constant.
        aub[i, :NVAR] = -np.asarray(facet_row, dtype=float)
        aub[i, -1] = 1.0
        bub[i] = float(constant)

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
    if not result.success or -result.fun > 1e-8:
        return None
    return result


def exactify_and_check(system, result):
    """Accept only an exact rational Farkas identity."""
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
    for a, (facet_row, _, _) in zip(alpha, facets):
        for j, value in enumerate(facet_row):
            coeff[j] += a * value
    for m, row in zip(mu, rows):
        for j, value in enumerate(row):
            coeff[j] += m * value
    if any(coeff):
        return None

    # On the equality space, the weighted sum of the strict positive facets is
    # forced to this exact constant.
    forced_value = (
        sum(a * constant for a, (_, constant, _) in zip(alpha, facets))
        - sum(m * Fraction(b) for m, b in zip(mu, rhs))
    )
    if forced_value > 0:
        return None

    active = [x for x in alpha + mu if x]
    max_denominator = max((x.denominator for x in active), default=1)
    return forced_value, max_denominator


def main():
    states = tri.collect_survivors()
    assert len(states) == 14174
    previous_systems = [tri.exact_system(state) for state in states]
    systems = [
        extended_system(state, previous)
        for state, previous in zip(states, previous_systems)
    ]

    first_by_key = {}
    state_keys = []
    for i, system in enumerate(systems):
        key = system_key(system)
        state_keys.append(key)
        first_by_key.setdefault(key, i)
    assert len(first_by_key) == 9038

    certified = {}
    value_by_key = {}
    max_denominator = 1
    for key, i in first_by_key.items():
        candidate = numerical_dual_candidate(systems[i])
        if candidate is None:
            continue
        exact = exactify_and_check(systems[i], candidate)
        if exact is None:
            continue
        forced_value, denominator = exact
        certified[key] = i
        value_by_key[key] = forced_value
        max_denominator = max(max_denominator, denominator)

    # All assertions below are exact-certificate counts.  The optimizer only
    # proposes supports; failure to exactify a support cannot exclude anything.
    assert len(certified) == 5854
    assert Counter(
        "zero" if value == 0 else "negative"
        for value in value_by_key.values()
    ) == Counter({
        "zero": 3576,
        "negative": 2278,
    })
    assert max_denominator == 231

    excluded = [i for i, key in enumerate(state_keys) if key in certified]
    remaining = [i for i, key in enumerate(state_keys) if key not in certified]

    assert len(excluded) == 7866
    assert len(remaining) == 6308
    assert Counter(states[i][1] for i in excluded) == Counter({
        "C7": 5734,
        "C3+C4": 2132,
    })
    assert Counter(states[i][1] for i in remaining) == Counter({
        "C7": 4936,
        "C3+C4": 1372,
    })
    assert Counter(
        "zero" if value_by_key[state_keys[i]] == 0 else "negative"
        for i in excluded
    ) == Counter({
        "zero": 5256,
        "negative": 2610,
    })

    remaining_by_pattern = Counter(
        "".join(map(str, states[i][5])) for i in remaining
    )
    assert remaining_by_pattern == Counter({
        "145": 12,
        "156": 16,
        "235": 830,
        "236": 1726,
        "237": 16,
        "245": 558,
        "256": 1726,
        "345": 24,
        "346": 558,
        "347": 12,
        "356": 830,
    })

    # The preceding non-ground-only affine reduction excluded 3,684 cells.
    # Recompute that exact subset and assert that the stronger ground-coupled
    # layer contains all of it, rather than trading one relaxation for another.
    old_first = {}
    old_keys = []
    for i, previous in enumerate(previous_systems):
        key = tri.system_key(previous)
        old_keys.append(key)
        old_first.setdefault(key, i)

    old_certified = set()
    for key, i in old_first.items():
        candidate = tri.numerical_dual_candidate(previous_systems[i])
        if candidate is None:
            continue
        if tri.exactify_and_check(previous_systems[i], candidate) is not None:
            old_certified.add(key)
    old_excluded = {i for i, key in enumerate(old_keys) if key in old_certified}
    new_excluded = set(excluded)
    assert len(old_excluded) == 3684
    assert old_excluded <= new_excluded
    assert len(new_excluded - old_excluded) == 4182

    print("PASS")
    print("generic H6 input cells: 14174 = 10670 C7 + 3504 C3+C4")
    print("ground-coupled exact Farkas exclusions: 7866 = 5734 C7 + 2132 C3+C4")
    print("  boundary certificates (forced facet average 0): 5256 cells")
    print("  strict negative certificates: 2610 cells")
    print("distinct affine systems certified: 5854 / 9038")
    print("maximum exact dual denominator: 231")
    print("new exclusions beyond the non-ground-only affine layer: 4182")
    print("remaining generic H6 cells: 6308 = 4936 C7 + 1372 C3+C4")


if __name__ == "__main__":
    main()
