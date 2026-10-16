"""Certify the finite circulant covariance regression for the train-cut note.

This is an algebraic/metric regression only.  It does not construct a full contact
complex, a global minimizer, or a C-II counterexample.  The construction is designed
to show that the covariance/nullspace equations need the strict-rhombus crossing
geometry before they can imply a contradiction.
"""

from __future__ import annotations

import math


def regression(q: int, ell: int) -> None:
    if q % 2 != 1 or not (2 <= ell < q // 2 + 1):
        raise ValueError("q must be odd and 2 <= ell < q/2")
    r = (q - 1) // 2
    u = [complex(math.cos(2 * math.pi * s / q), math.sin(2 * math.pi * s / q)) for s in range(q)]

    def chi(s: int, i: int) -> float:
        return float((i - s) % q < ell)

    p = [sum(chi(s, i) * u[s] for s in range(q)) for i in range(q)]
    E = [[chi(s, (i + r) % q) - chi(s, i) for s in range(q)] for i in range(q)]
    R = [sum(E[i][s] * u[s] for s in range(q)) for i in range(q)]
    d = abs(R[0])

    assert max(abs(abs(z) - d) for z in R) < 2e-10
    assert max(abs((p[(i + r) % q] - p[i]) - R[i]) for i in range(q)) < 2e-10
    # The regular shell has its adjacent side as the shortest pair distance.
    side = abs(p[1] - p[0])
    assert side > 1.0
    assert min(abs(p[j] - p[i]) for i in range(q) for j in range(i + 1, q)) > 1.0
    assert abs(max(abs(p[j] - p[i]) for i in range(q) for j in range(i + 1, q)) - d) < 2e-10

    # Uniform beta gives W U = (d^2/q) U; evaluate it directly in complex form.
    wb_u = []
    for s in range(q):
        wb_u.append(sum(E[i][s] * R[i] for i in range(q)) / q)
    lam = d * d / q
    assert max(abs(wb_u[s] - lam * u[s]) for s in range(q)) < 2e-9
    assert abs(q / d - math.pi / math.sqrt(3)) < 0.03
    print(f"q={q}, ell={ell}, D={d:.12f}, q/D={q/d:.12f}: covariance regression OK")


if __name__ == "__main__":
    for q, ell in ((101, 34), (301, 100), (601, 200)):
        regression(q, ell)
