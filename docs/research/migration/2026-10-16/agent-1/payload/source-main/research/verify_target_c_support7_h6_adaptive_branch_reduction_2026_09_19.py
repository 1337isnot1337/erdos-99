#!/usr/bin/env python3
"""Exact certificate for 32 further generic-H6 exclusions.

Starting point: the committed 4,976-cell generic support-seven H6 endpoint from
verify_target_c_support7_h6_order_hull_reduction_2026_09_19.py.

For a physical pentagon face, retain all ten admissible cyclic gap orders and
split each order into the two closed median branches x_c <= 2/5 and x_c >= 2/5.
On each branch use the five exact branch-adaptive closure secants certified by
verify_target_c_pentagon_branch_adaptive_secants_2026_09_19.py.

A cell is impossible if all 20 branches at one face have exact rational Farkas
contradictions against the global 85-variable complete-angle system.

The LP solver is used only to discover a dual support. Acceptance is entirely
exact over fractions.Fraction: nonnegative strict/closed multipliers, strict
weights summing to one, coefficientwise cancellation in all 85 variables, and
a forced constant <= 0.
"""

from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


O = load(
    "h6_order_hull",
    "verify_target_c_support7_h6_order_hull_reduction_2026_09_19.py",
)
B = load(
    "pentagon_branch_adaptive",
    "verify_target_c_pentagon_branch_adaptive_secants_2026_09_19.py",
)

NVAR = O.NVAR
NG = O.NG
VIDX = O.VIDX
STRICT_ORDERS = O.STRICT_ORDERS
LOW_LINES = tuple(B.LOW_LINES)
HIGH_LINES = tuple(B.HIGH_LINES)

assert len(STRICT_ORDERS) == 10
assert len(LOW_LINES) == len(HIGH_LINES) == 5


def adaptive_branch(face, order, side):
    """Closed necessary facets for one order/median branch.

    Every triple is (row,const,label) and means const + row*x >= 0.
    """
    assert side in ("low", "high")
    out = []

    for a, b in zip(order, order[1:]):
        row = [F(0)] * NVAR
        row[VIDX[(face, b)]] += 1
        row[VIDX[(face, a)]] -= 1
        out.append((tuple(row), F(0), ("ORDER", face, a, b)))

    rank = {k: r for r, k in enumerate(order)}
    lines = LOW_LINES if side == "low" else HIGH_LINES
    for k in range(5):
        m, c = lines[rank[k]]
        row = [F(0)] * NVAR
        row[VIDX[(face, k)]] += m
        row[VIDX[(face, (k + 2) % 5)]] -= 1
        row[VIDX[(face, (k + 3) % 5)]] -= 1
        out.append((tuple(row), F(c), ("SECANT", face, k, rank[k], side)))

    cidx = order[2]
    row = [F(0)] * NVAR
    if side == "low":
        row[VIDX[(face, cidx)]] -= 1
        const = F(2, 5)
    else:
        row[VIDX[(face, cidx)]] += 1
        const = F(-2, 5)
    out.append((tuple(row), const, ("MEDIAN", face, cidx, side)))

    assert len(out) == 10
    return tuple(out)


BRANCH = {
    (face, order, side): adaptive_branch(face, order, side)
    for face in NG
    for order in STRICT_ORDERS
    for side in ("low", "high")
}


def solve_full_column_rank(columns, target):
    """Solve C*x=target exactly when the supplied columns are independent."""
    m = len(columns)
    n = len(target)
    if m == 0:
        return None
    mat = [
        [F(columns[j][i]) for j in range(m)] + [F(target[i])]
        for i in range(n)
    ]
    prow = 0
    pivots = {}
    for col in range(m):
        pivot = next((r for r in range(prow, n) if mat[r][col]), None)
        if pivot is None:
            return None
        mat[prow], mat[pivot] = mat[pivot], mat[prow]
        z = mat[prow][col]
        mat[prow] = [x / z for x in mat[prow]]
        for r in range(n):
            if r == prow or not mat[r][col]:
                continue
            q = mat[r][col]
            mat[r] = [a - q*b for a, b in zip(mat[r], mat[prow])]
        pivots[col] = prow
        prow += 1
    for r in range(n):
        if all(mat[r][c] == 0 for c in range(m)) and mat[r][-1] != 0:
            return None
    return [mat[pivots[c]][-1] for c in range(m)]


def exactify_support(system, closed, result):
    """Recover and verify one exact strict/closed Farkas certificate.

    Thresholding is only a way to guess the active support. The final solve and
    all certificate checks are exact rational arithmetic.
    """
    rows, rhs, _, strict = system
    ns = len(strict)
    w = [float(-z) for z in result.ineqlin.marginals]
    ym = [float(z) for z in result.eqlin.marginals]

    for tol in (1e-7, 1e-8, 1e-9, 1e-10, 1e-11, 1e-12, 1e-13, 1e-14, 1e-15):
        desc = []
        cols = []
        for i, a in enumerate(w[:ns]):
            if a > tol:
                cols.append([F(z) for z in strict[i][0]] + [F(1)])
                desc.append(("a", i))
        for k, b in enumerate(w[ns:]):
            if b > tol:
                cols.append([F(z) for z in closed[k][0]] + [F(0)])
                desc.append(("b", k))
        for r, m in enumerate(ym):
            if abs(m) > tol:
                cols.append([F(z) for z in rows[r]] + [F(0)])
                desc.append(("m", r))

        sol = solve_full_column_rank(cols, [F(0)] * NVAR + [F(1)])
        if sol is None:
            continue

        alpha = [F(0)] * ns
        beta = [F(0)] * len(closed)
        mu = [F(0)] * len(rows)
        for d, x in zip(desc, sol):
            if d[0] == "a":
                alpha[d[1]] = x
            elif d[0] == "b":
                beta[d[1]] = x
            else:
                mu[d[1]] = x

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


CANDIDATES = (
    (110, 226, 2, "256"),
    (121, 258, 2, "256"),
    (413, 876, 4, "346"),
    (417, 889, 4, "346"),
    (967, 2001, 7, "145"),
    (970, 2008, 6, "145"),
    (1166, 2512, 4, "346"),
    (1173, 2545, 4, "346"),
    (1216, 2729, 2, "256"),
    (1225, 2759, 2, "256"),
    (1269, 3001, 4, "346"),
    (1595, 3939, 4, "346"),
    (1701, 4388, 4, "346"),
    (1734, 4483, 4, "346"),
    (1743, 4513, 4, "346"),
    (2190, 5716, 4, "346"),
    (2908, 7410, 2, "245"),
    (2910, 7417, 2, "245"),
    (3003, 7854, 2, "245"),
    (3126, 8268, 2, "245"),
    (3154, 8414, 4, "236"),
    (3160, 8428, 4, "236"),
    (3276, 8747, 2, "245"),
    (3286, 8784, 2, "245"),
    (3367, 9118, 2, "245"),
    (3473, 9401, 2, "245"),
    (4684, 12107, 4, "236"),
    (4686, 12119, 4, "236"),
    (4975, 12704, 2, "245"),
    (4988, 12758, 2, "245"),
    (5665, 14112, 6, "347"),
    (5668, 14120, 7, "347"),
)


def survives_previous_order_hull(system):
    """Apply the committed 10-order exact exclusion rule to one cell."""
    for face in NG:
        branch_results = []
        numerically_dead = True
        for order in STRICT_ORDERS:
            margin, result = O.numerical_candidate(system, O.BRANCH[(face, order)])
            assert margin is not None, result.message
            branch_results.append((order, result))
            if margin > 1e-8:
                numerically_dead = False
                break
        if not numerically_dead:
            continue
        exact = []
        for order, result in branch_results:
            cert = O.exactify(system, O.BRANCH[(face, order)], result)
            if cert is None:
                exact = []
                break
            exact.append(cert)
        if len(exact) == 10:
            return False
    return True


def main():
    states = O.tri.collect_survivors()
    assert len(states) == 14174
    previous = O.complete_angle_survivors(states)
    assert len(previous) == 5692

    assert len(CANDIDATES) == len({q for q, _, _, _ in CANDIDATES}) == 32

    graph = Counter()
    pattern = Counter()
    faces = Counter()
    forced = Counter()
    max_denominator = 1
    exact_count = 0

    for q, expected_idx, face, expected_pattern in CANDIDATES:
        idx = previous[q]
        assert idx == expected_idx
        st = states[idx]
        assert st[1] == "C7"
        pat = "".join(map(str, st[5]))
        assert pat == expected_pattern
        system = O.C.build_system(st)

        assert survives_previous_order_hull(system)

        for order in STRICT_ORDERS:
            for side in ("low", "high"):
                closed = BRANCH[(face, order, side)]
                margin, result = O.numerical_candidate(system, closed)
                assert margin is not None, result.message
                assert margin <= 1e-8
                cert = exactify_support(system, closed, result)
                assert cert is not None
                value, denominator = cert
                forced["zero" if value == 0 else "negative"] += 1
                max_denominator = max(max_denominator, denominator)
                exact_count += 1

        graph[st[1]] += 1
        pattern[pat] += 1
        faces[face] += 1

    assert graph == Counter({"C7": 32})
    assert pattern == Counter({
        "145": 2,
        "236": 4,
        "245": 10,
        "256": 4,
        "346": 10,
        "347": 2,
    })
    assert faces == Counter({2: 14, 4: 14, 6: 2, 7: 2})
    assert exact_count == 640
    assert forced == Counter({"negative": 480, "zero": 160})
    assert max_denominator == 41150022497377

    print("PASS")
    print("previous generic H6 endpoint: 4976 = 3972 C7 + 1004 C3+C4")
    print("new exact adaptive-branch exclusions: 32 = 32 C7")
    print("exact rational branch certificates:", exact_count)
    print("certificate forced values:", dict(forced))
    print("maximum exact dual denominator:", max_denominator)
    print("remaining certified endpoint: 4944 = 3940 C7 + 1004 C3+C4")
    print("excluded by ground pattern:", dict(sorted(pattern.items())))
    print("witness physical face counts:", dict(sorted(faces.items())))


if __name__ == "__main__":
    main()
