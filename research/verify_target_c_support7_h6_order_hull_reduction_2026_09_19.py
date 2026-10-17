#!/usr/bin/env python3
"""Exact-checking H6 reduction using physical pentagon gap-order hulls.

Starting point: the committed 5,692-cell generic support-seven H6 complete-angle
endpoint.  For each cell and each physical non-ground face, retain the ten
possible closed physical gap-order cones.  On one order cone add the four
rank-forced exact 2/5 secants and the two exact median-threshold convex-hull
facets.  If all ten order cones at one face are incompatible with the global
85-variable complete-angle system, the cell is impossible.

The LP solver is only a discovery mechanism.  Every excluded order branch is
accepted only after its dual is converted to fractions.Fraction and checked
coefficientwise in all 85 variables.  A cell is counted as excluded only when
all ten closed order branches at one physical face have exact rational Farkas
certificates.
"""

from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import contextlib
import importlib.util
import io

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


A = load(
    "h6_complete_census",
    "verify_target_c_support7_h6_complete_angle_affine_census_2026_09_19.py",
)
P = load(
    "pentagon_orders",
    "verify_target_c_pentagon_gap_order_2026_09_19.py",
)
M = load(
    "pentagon_median_hull",
    "verify_target_c_pentagon_median_hull_2026_09_19.py",
)

C = A.C
tri = A.tri
NG = tuple(tri.NG)
NVAR = C.NVAR
VIDX = tri.VIDX
STRICT_ORDERS = tuple(P.STRICT)
assert len(STRICT_ORDERS) == 10
assert M.ORDER == STRICT_ORDERS[0]


def complete_angle_survivors(states):
    """Reproduce the committed 5,692-cell exact affine endpoint."""
    remaining = A.ground_coupled_survivors(states)
    assert len(remaining) == 6308

    excluded = set()
    solver_failures = []
    exact_failures = []
    for i in remaining:
        system = C.build_system(states[i])
        margin, result = C.numerical_candidate(system)
        if margin is None:
            solver_failures.append(i)
            continue
        if margin > 1e-8:
            continue
        exact = C.exactify(system, result)
        if exact is None:
            exact_failures.append(i)
            continue
        excluded.add(i)

    assert solver_failures == []
    assert exact_failures == []
    assert len(excluded) == 616
    final = [i for i in remaining if i not in excluded]
    assert len(final) == 5692
    assert Counter(states[i][1] for i in final) == Counter({
        "C7": 4464,
        "C3+C4": 1228,
    })
    assert Counter(
        "".join(map(str, states[i][5])) for i in final
    ) == Counter({
        "145": 8,
        "156": 16,
        "235": 772,
        "236": 1524,
        "237": 16,
        "245": 514,
        "256": 1524,
        "345": 24,
        "346": 514,
        "347": 8,
        "356": 772,
    })
    return final


def closed_order_hull(face, order):
    """Return necessary closed facets for one physical gap-order branch.

    Each triple (row,const,label) means const + row*x >= 0.  The global system
    already contains the strict turn-simplex inequalities, so only the order,
    four rank-forced secants, and two median-hull facets are added here.
    """
    out = []

    # Weak closure of x_order[0] <= ... <= x_order[4].  Closed cones cover the
    # physical equality cases by the exact gap-order verifier.
    for a, b in zip(order, order[1:]):
        row = [F(0)] * NVAR
        row[VIDX[(face, b)]] += 1
        row[VIDX[(face, a)]] -= 1
        out.append((tuple(row), F(0), ("ORDER", face, a, b)))

    rank = {k: r for r, k in enumerate(order)}
    for k in range(5):
        r = rank[k]
        if r == 2:
            continue
        row = [F(0)] * NVAR
        if r <= 1:
            # x_{k+2}+x_{k+3} <= 2/3 + x_k/3.
            row[VIDX[(face, k)]] += F(1, 3)
            row[VIDX[(face, (k + 2) % 5)]] -= 1
            row[VIDX[(face, (k + 3) % 5)]] -= 1
            out.append((tuple(row), F(2, 3), ("LOW_SECANT", face, k)))
        else:
            # x_{k+2}+x_{k+3} <= 1/2 + 3*x_k/4.
            row[VIDX[(face, k)]] += F(3, 4)
            row[VIDX[(face, (k + 2) % 5)]] -= 1
            row[VIDX[(face, (k + 3) % 5)]] -= 1
            out.append((tuple(row), F(1, 2), ("HIGH_SECANT", face, k)))

    # Rank notation a <= b <= c <= d <= e.  These are exactly the two extra
    # facets of the convex hull of the low/high median branches inside a fixed
    # order cone, proved by verify_target_c_pentagon_median_hull_2026_09_19.py.
    a, b, c, d, e = order

    # H1: 5*b + 7*c + 4*d >= 6 + a.
    row = [F(0)] * NVAR
    row[VIDX[(face, a)]] -= 1
    row[VIDX[(face, b)]] += 5
    row[VIDX[(face, c)]] += 7
    row[VIDX[(face, d)]] += 4
    out.append((tuple(row), F(-6), ("H1", face)))

    # H2: 8*b + 13*c + 9*d >= 12.
    row = [F(0)] * NVAR
    row[VIDX[(face, b)]] += 8
    row[VIDX[(face, c)]] += 13
    row[VIDX[(face, d)]] += 9
    out.append((tuple(row), F(-12), ("H2", face)))

    return tuple(out)


BRANCH = {
    (face, order): closed_order_hull(face, order)
    for face in NG
    for order in STRICT_ORDERS
}


def numerical_candidate(system, closed):
    """Maximize the common margin on the original strict facets only."""
    rows, rhs, _, strict = system
    ns = len(strict)
    nc = len(closed)

    aeq = np.zeros((len(rows), NVAR + 1), dtype=float)
    aeq[:, :NVAR] = np.asarray(rows, dtype=float)
    beq = np.asarray(rhs, dtype=float)

    aub = np.zeros((ns + nc, NVAR + 1), dtype=float)
    bub = np.zeros(ns + nc, dtype=float)
    for i, (row, const, _) in enumerate(strict):
        aub[i, :NVAR] = -np.asarray(row, dtype=float)
        aub[i, -1] = 1.0
        bub[i] = float(const)
    for i, (row, const, _) in enumerate(closed, ns):
        aub[i, :NVAR] = -np.asarray(row, dtype=float)
        # Closed branch facets receive no strictness margin.
        aub[i, -1] = 0.0
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


def exactify(system, closed, result):
    """Check an exact rational strict/closed Farkas contradiction."""
    rows, rhs, _, strict = system
    ns = len(strict)

    # Denominator limiting reconstructs a rational candidate only.  Acceptance
    # below is by exact arithmetic: nonnegative multipliers, strict weights
    # summing to one, coefficientwise cancellation, and forced value <= 0.
    for limit in (10_000, 100_000, 1_000_000, 10_000_000):
        alpha = [
            F(float(-m)).limit_denominator(limit)
            for m in result.ineqlin.marginals[:ns]
        ]
        beta = [
            F(float(-m)).limit_denominator(limit)
            for m in result.ineqlin.marginals[ns:]
        ]
        mu = [
            F(float(m)).limit_denominator(limit)
            for m in result.eqlin.marginals
        ]

        if any(a < 0 for a in alpha) or any(b < 0 for b in beta):
            continue
        if sum(alpha) != 1:
            continue

        coeff = [F(0)] * NVAR
        for mult, (row, _, _) in zip(alpha, strict):
            if mult:
                for j, z in enumerate(row):
                    if z:
                        coeff[j] += mult * F(z)
        for mult, (row, _, _) in zip(beta, closed):
            if mult:
                for j, z in enumerate(row):
                    if z:
                        coeff[j] += mult * F(z)
        for mult, row in zip(mu, rows):
            if mult:
                for j, z in enumerate(row):
                    if z:
                        coeff[j] += mult * F(z)
        if any(coeff):
            continue

        forced = (
            sum(a * F(c) for a, (_, c, _) in zip(alpha, strict))
            + sum(b * F(c) for b, (_, c, _) in zip(beta, closed))
            - sum(m * F(r) for m, r in zip(mu, rhs))
        )
        if forced > 0:
            continue

        active = [z for z in alpha + beta + mu if z]
        denominator = max((z.denominator for z in active), default=1)
        return forced, denominator

    return None


def main():
    states = tri.collect_survivors()
    assert len(states) == 14174
    previous = complete_angle_survivors(states)

    excluded = []
    witness_face = {}
    certs = {}
    solver_failures = []
    lp_count = 0

    # Discovery pass.  A face is a candidate witness only if every one of its
    # ten closed order hulls has nonpositive common strict margin.
    for idx in previous:
        system = C.build_system(states[idx])
        for face in NG:
            branch_results = []
            numerically_dead = True
            for order in STRICT_ORDERS:
                margin, result = numerical_candidate(system, BRANCH[(face, order)])
                lp_count += 1
                if margin is None:
                    solver_failures.append((idx, face, order))
                    numerically_dead = False
                    break
                branch_results.append((order, result))
                if margin > 1e-8:
                    numerically_dead = False
                    break
            if not numerically_dead:
                continue

            # Exactify all ten branches.  Failure to exactify even one branch
            # leaves the cell alive; numerical infeasibility is never enough.
            exact = []
            for order, result in branch_results:
                cert = exactify(system, BRANCH[(face, order)], result)
                if cert is None:
                    exact = []
                    break
                exact.append((order, cert))
            if len(exact) != 10:
                continue

            excluded.append(idx)
            witness_face[idx] = face
            certs[idx] = exact
            break

    assert solver_failures == []
    assert lp_count == 88514
    assert len(excluded) == 716
    assert len(set(excluded)) == 716

    graph = Counter(states[i][1] for i in excluded)
    pattern = Counter("".join(map(str, states[i][5])) for i in excluded)
    faces = Counter(witness_face[i] for i in excluded)
    forced = Counter()
    max_denominator = 1
    for i in excluded:
        for _, (value, denominator) in certs[i]:
            forced["zero" if value == 0 else "negative"] += 1
            max_denominator = max(max_denominator, denominator)

    assert graph == Counter({"C7": 492, "C3+C4": 224})
    assert pattern == Counter({
        "145": 2,
        "235": 98,
        "236": 238,
        "245": 20,
        "256": 238,
        "346": 20,
        "347": 2,
        "356": 98,
    })
    assert faces == Counter({2: 377, 3: 94, 4: 122, 6: 61, 7: 62})
    assert forced == Counter({"negative": 5863, "zero": 1297})
    assert max_denominator == 16088

    excluded_set = set(excluded)
    final = [i for i in previous if i not in excluded_set]
    assert len(final) == 4976
    assert Counter(states[i][1] for i in final) == Counter({
        "C7": 3972,
        "C3+C4": 1004,
    })
    assert Counter(
        "".join(map(str, states[i][5])) for i in final
    ) == Counter({
        "145": 6,
        "156": 16,
        "235": 674,
        "236": 1286,
        "237": 16,
        "245": 494,
        "256": 1286,
        "345": 24,
        "346": 494,
        "347": 6,
        "356": 674,
    })

    print("PASS")
    print("previous generic H6 endpoint: 5692 = 4464 C7 + 1228 C3+C4")
    print("new exact order-hull exclusions: 716 = 492 C7 + 224 C3+C4")
    print("order-branch LPs inspected:", lp_count)
    print("exact rational branch certificates:", 10 * len(excluded))
    print("certificate forced values:", dict(forced))
    print("maximum exact dual denominator:", max_denominator)
    print("remaining generic H6 cells: 4976 = 3972 C7 + 1004 C3+C4")
    print("excluded by ground pattern:", dict(sorted(pattern.items())))
    print("witness physical face counts:", dict(sorted(faces.items())))


if __name__ == "__main__":
    main()
