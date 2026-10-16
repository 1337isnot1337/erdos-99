#!/usr/bin/env python3
"""Exact-checking certificate for the generic support-seven H6 triangle/simplex reduction.

This verifier starts from the 14,174 generic H6 cells certified by
verify_target_c_support7_h6_interior_force_chirotope_reduction_2026_09_19.py.
For every cell it reconstructs the full signed force cyclic order at each of the
seven non-ground physical pentagons.  It then imposes two kinds of necessary
conditions in normalized angles (angle/pi):

  * every pentagon has sum x_k = 2 and the audited strict simplex facets
        q_k = x_k + x_{k+1} - x_{k+3} > 1/3;
  * every present reciprocal triangle among vertices 1,...,7 has angle sum 1.

The triangle-angle equations are exact integer-affine equations in the 35 turn
variables.  scipy.optimize.linprog is used only to FIND a dual support.  Every
claimed exclusion is then re-read as rational numbers and checked exactly with
fractions.Fraction.  A numerical answer by itself never excludes a cell.

An exact certificate has nonnegative coefficients alpha_j with sum alpha_j=1
and equality multipliers mu_r such that

    sum_j alpha_j q_j + sum_r mu_r E_r = 0

coefficientwise.  On the equality space this forces

    sum_j alpha_j q_j = -sum_r mu_r b_r <= 1/3,

contradicting q_j > 1/3 for every j.

The script also checks a simpler exact sub-obstruction: 2,952 cells already
contain one reciprocal triangle whose three angle minima over the closed local
turn simplices sum to at least 1.  Because each relevant angle functional is
nonconstant and physical pentagons lie in the strict simplex interior, the
physical triangle-angle sum would be strictly greater than 1.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
import contextlib
import importlib.util
import io

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "verify_target_c_support7_h6_interior_force_chirotope_reduction_2026_09_19.py"
spec = importlib.util.spec_from_file_location("h6_base", BASE_PATH)
base = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(base)

NG = tuple(range(1, 8))
HULL_NG = tuple(range(1, 6))
INTERIOR = (6, 7)
NVAR = 35
VIDX = {(v, k): (v - 1) * 5 + k for v in NG for k in range(5)}
edge = base.edge


def collect_survivors():
    """Rebuild the preceding 14,174 cells, retaining their complete edge signs."""
    out = []
    for order_index, (raws, chi) in enumerate(base.ORDER_TYPES.items()):
        for graph_type, missing in base.MISSING_GRAPHS:
            local = {
                i: base.local_base_signs_all(i, raws[i], missing)
                for i in HULL_NG
            }
            hull_constraints = [
                (i, j, local[i][j] * local[j][i])
                for i, j in combinations(HULL_NG, 2)
                if edge(i, j) not in missing
            ]
            for pattern, ground_signs in base.GROUND_CASES[raws[0]]:
                if not all(
                    ground_signs[i] * ground_signs[j] == required
                    for i, j, required in hull_constraints
                ):
                    continue

                fixed = {}
                compatible = True
                for h in HULL_NG:
                    for j, local_sign in local[h].items():
                        e = edge(h, j)
                        sign = ground_signs[h] * local_sign
                        if e in fixed and fixed[e] != sign:
                            compatible = False
                            break
                        fixed[e] = sign
                    if not compatible:
                        break
                if not compatible:
                    continue

                has_67 = edge(6, 7) not in missing
                good_67 = []
                for sign_67 in ((1, -1) if has_67 else (None,)):
                    good = True
                    for v in INTERIOR:
                        neighbors = [0] + [
                            j for j in NG
                            if j != v and edge(v, j) not in missing
                        ]
                        signs_v = {0: ground_signs[v]}
                        for j in neighbors:
                            if j == 0:
                                continue
                            e = edge(v, j)
                            signs_v[j] = sign_67 if e == edge(6, 7) else fixed[e]
                        if not base.force_rank2_balanced(chi, v, neighbors, signs_v):
                            good = False
                            break
                    if good:
                        good_67.append(sign_67)
                if not good_67:
                    continue
                assert len(good_67) == 1

                signs = {edge(0, v): ground_signs[v] for v in NG}
                for e, sign in fixed.items():
                    if e in signs:
                        assert signs[e] == sign
                    signs[e] = sign
                if has_67:
                    signs[edge(6, 7)] = good_67[0]

                present = (
                    {edge(0, v) for v in NG}
                    | {e for e in combinations(NG, 2) if e not in missing}
                )
                assert set(signs) == present and len(signs) == 21
                out.append((
                    order_index, graph_type, missing, raws, chi,
                    tuple(pattern), signs,
                ))
    return out


def force_cycle(v, missing, chi, signs):
    """Recover the unique CCW order of the five signed force rays."""
    neighbors = [0] + [
        j for j in NG if j != v and edge(v, j) not in missing
    ]
    assert len(neighbors) == 5
    local_signs = {j: signs[edge(v, j)] for j in neighbors}

    def det_sign(a, b):
        return (
            local_signs[a]
            * local_signs[b]
            * base.chi_value(chi, v, a, b)
        )

    start = min(neighbors)
    rest = [x for x in neighbors if x != start]
    good = []
    for perm in permutations(rest):
        cycle = (start,) + perm
        if all(
            det_sign(cycle[i], cycle[(i + step) % 5])
            == (1 if step in (1, 2) else -1)
            for i in range(5)
            for step in (1, 2, 3, 4)
        ):
            good.append(cycle)
    assert len(good) == 1
    return good[0]


def force_arc(cycle, v, a, b):
    row = [0] * NVAR
    k = cycle.index(a)
    stop = cycle.index(b)
    while k != stop:
        row[VIDX[(v, k)]] += 1
        k = (k + 1) % 5
    return row


def raw_angle_affine(v, a, b, chi, signs, cycles):
    """Return the reciprocal angle angle(avb)/pi as row*x + constant."""
    arc = force_arc(cycles[v], v, a, b)
    same_sign = signs[edge(v, a)] == signs[edge(v, b)]
    raw_chi = base.chi_value(chi, v, a, b)
    if same_sign and raw_chi > 0:
        return arc, 0
    if same_sign and raw_chi < 0:
        return [-z for z in arc], 2
    if (not same_sign) and raw_chi > 0:
        return arc, -1
    return [-z for z in arc], 1


def exact_system(state):
    _, _, missing, _, chi, _, signs = state
    cycles = {v: force_cycle(v, missing, chi, signs) for v in NG}

    rows = []
    rhs = []
    labels = []

    for v in NG:
        row = [0] * NVAR
        for k in range(5):
            row[VIDX[(v, k)]] = 1
        rows.append(row)
        rhs.append(2)
        labels.append(("F", v))

    for a, b, c in combinations(NG, 3):
        if any(
            edge(*e) in missing
            for e in ((a, b), (a, c), (b, c))
        ):
            continue
        row = [0] * NVAR
        constant = 0
        for v, j, k in ((a, b, c), (b, a, c), (c, a, b)):
            angle_row, angle_constant = raw_angle_affine(
                v, j, k, chi, signs, cycles
            )
            row = [x + y for x, y in zip(row, angle_row)]
            constant += angle_constant
        rows.append(row)
        rhs.append(1 - constant)
        labels.append(("T", a, b, c))

    qrows = []
    qlabels = []
    for v in NG:
        for k in range(5):
            row = [0] * NVAR
            row[VIDX[(v, k)]] += 1
            row[VIDX[(v, (k + 1) % 5)]] += 1
            row[VIDX[(v, (k + 3) % 5)]] -= 1
            qrows.append(row)
            qlabels.append(("Q", v, k))

    return rows, rhs, labels, qrows, qlabels, cycles


def system_key(system):
    rows, rhs, _, qrows, _, _ = system
    return (
        tuple(tuple(row) for row in rows),
        tuple(rhs),
        tuple(tuple(row) for row in qrows),
    )


# Five vertices of the closed local turn simplex in x coordinates.
BASE_X = (
    Fraction(0), Fraction(2, 3), Fraction(1, 3),
    Fraction(1, 3), Fraction(2, 3),
)
X_VERTICES = tuple(BASE_X[r:] + BASE_X[:r] for r in range(5))


def angle_range(row, constant, v):
    block = row[(v - 1) * 5:v * 5]
    values = tuple(
        Fraction(constant) + sum(Fraction(c) * x for c, x in zip(block, xv))
        for xv in X_VERTICES
    )
    return min(values), max(values)


def has_single_triangle_obstruction(state, system):
    """Exact local test: sum of the three closed-simplex angle minima >= 1."""
    _, _, missing, _, chi, _, signs = state
    cycles = system[-1]
    for a, b, c in combinations(NG, 3):
        if any(
            edge(*e) in missing
            for e in ((a, b), (a, c), (b, c))
        ):
            continue
        minima = []
        for v, j, k in ((a, b, c), (b, a, c), (c, a, b)):
            row, constant = raw_angle_affine(v, j, k, chi, signs, cycles)
            mn, mx = angle_range(row, constant, v)
            assert mn < mx  # strict-simplex points are strictly above the minimum
            minima.append(mn)
        if sum(minima) >= 1:
            return True
    return False


def numerical_dual_candidate(system):
    """Find a dual candidate. This function has no authority to certify a cell."""
    rows, rhs, _, qrows, _, _ = system
    aeq = np.zeros((len(rows), NVAR + 1), dtype=float)
    aeq[:, :NVAR] = np.asarray(rows, dtype=float)
    beq = np.asarray(rhs, dtype=float)

    aub = np.zeros((len(qrows), NVAR + 1), dtype=float)
    aub[:, :NVAR] = -np.asarray(qrows, dtype=float)
    aub[:, -1] = 1.0
    bub = np.full(len(qrows), -1.0 / 3.0, dtype=float)

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
    """Convert a numerical dual to rationals and accept only an exact identity."""
    rows, rhs, _, qrows, _, _ = system
    alpha = tuple(
        Fraction(float(-m)).limit_denominator(1_000_000)
        for m in result.ineqlin.marginals
    )
    # scipy reports equality marginals with exactly the sign needed in
    #     sum alpha*q + sum mu*E = 0
    # for the primal convention used above.
    mu = tuple(
        Fraction(float(m)).limit_denominator(1_000_000)
        for m in result.eqlin.marginals
    )

    if any(a < 0 for a in alpha) or sum(alpha) != 1:
        return None

    coeff = [Fraction(0) for _ in range(NVAR)]
    for a, qrow in zip(alpha, qrows):
        for j, value in enumerate(qrow):
            coeff[j] += a * value
    for m, row in zip(mu, rows):
        for j, value in enumerate(row):
            coeff[j] += m * value
    if any(coeff):
        return None

    forced_value = -sum(m * Fraction(b) for m, b in zip(mu, rhs))
    if forced_value > Fraction(1, 3):
        return None

    active = [x for x in alpha + mu if x]
    max_denominator = max((x.denominator for x in active), default=1)
    return forced_value, max_denominator


def main():
    states = collect_survivors()
    assert len(states) == 14174
    assert Counter(state[1] for state in states) == Counter({
        "C7": 10670,
        "C3+C4": 3504,
    })

    systems = [exact_system(state) for state in states]
    assert Counter(len(system[0]) - 7 for system in systems) == Counter({
        7: 10670,
        6: 3504,
    })

    local = [
        i for i, (state, system) in enumerate(zip(states, systems))
        if has_single_triangle_obstruction(state, system)
    ]
    assert len(local) == 2952
    assert Counter(states[i][1] for i in local) == Counter({
        "C7": 2368,
        "C3+C4": 584,
    })

    first_by_key = {}
    state_keys = []
    for i, system in enumerate(systems):
        key = system_key(system)
        state_keys.append(key)
        first_by_key.setdefault(key, i)
    assert len(first_by_key) == 6018

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

    # These assertions concern exact identities only. If the numerical support
    # finder behaves differently, the script fails instead of accepting an
    # uncertified exclusion.
    assert len(certified) == 2072
    assert Counter(value_by_key.values()) == Counter({
        Fraction(1, 3): 2056,
        Fraction(3, 10): 16,
    })
    assert max_denominator == 51

    excluded = [i for i, key in enumerate(state_keys) if key in certified]
    remaining = [i for i, key in enumerate(state_keys) if key not in certified]
    assert len(excluded) == 3684
    assert len(remaining) == 10490
    assert Counter(states[i][1] for i in excluded) == Counter({
        "C7": 2960,
        "C3+C4": 724,
    })
    assert Counter(states[i][1] for i in remaining) == Counter({
        "C7": 7710,
        "C3+C4": 2780,
    })
    assert Counter(value_by_key[state_keys[i]] for i in excluded) == Counter({
        Fraction(1, 3): 3656,
        Fraction(3, 10): 28,
    })

    remaining_by_pattern = Counter(
        "".join(map(str, states[i][5])) for i in remaining
    )
    assert remaining_by_pattern == Counter({
        "145": 88,
        "156": 80,
        "235": 1252,
        "236": 2810,
        "237": 80,
        "245": 976,
        "256": 2810,
        "345": 78,
        "346": 976,
        "347": 88,
        "356": 1252,
    })

    print("PASS")
    print("generic H6 input cells: 14174 = 10670 C7 + 3504 C3+C4")
    print("single-triangle exact obstructions: 2952 = 2368 C7 + 584 C3+C4")
    print("exact Farkas-certified exclusions: 3684 = 2960 C7 + 724 C3+C4")
    print("  boundary certificates (forced value 1/3): 3656 cells")
    print("  strict certificates (forced value 3/10): 28 cells")
    print("distinct affine systems certified: 2072 / 6018")
    print("maximum exact dual denominator: 51")
    print("remaining generic H6 cells: 10490 = 7710 C7 + 2780 C3+C4")


if __name__ == "__main__":
    main()
