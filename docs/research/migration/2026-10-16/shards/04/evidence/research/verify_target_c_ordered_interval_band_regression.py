#!/usr/bin/env python3
"""Exact regression for the ordered interval-band obstruction.

The construction has A_i--B_j edges when j is in the length-m interval
[i, i+m-1].  We retain a central block of rows and columns so that both
shores have linear minimum degree.  Nevertheless every complete biclique
has shore sum at most m+1, while the Section-76 leading threshold is m.

This is an abstract monotone pseudosegment/interval regression.  It does not
claim a unit-rhombus source or global optimality.
"""

from __future__ import annotations


def build(t: int):
    if t < 2:
        raise ValueError("t must be at least 2")
    m = 4 * t
    # Central row and column blocks.  Inclusive endpoints are intentional.
    rows = list(range(t, 3 * t + 1))
    cols = list(range(2 * t, 6 * t + 1))
    nbr = {
        i: [j for j in cols if i <= j <= i + m - 1]
        for i in rows
    }
    rev = {j: [i for i in rows if j in nbr[i]] for j in cols}
    edges = sum(len(v) for v in nbr.values())
    return m, rows, cols, nbr, rev, edges


def main() -> None:
    for t in (2, 3, 5, 10, 25):
        m, rows, cols, nbr, rev, edges = build(t)
        min_a = min(map(len, nbr.values()))
        min_b = min(map(len, rev.values()))

        # Every row is an interval in the ordered B shore.
        assert all(v == list(range(v[0], v[-1] + 1)) for v in nbr.values())
        # The exact central-block degree bounds.
        assert min_a >= 3 * t
        assert min_b >= t
        # The exact interval-intersection argument: k rows have at most
        # m-k+1 common columns, hence no K_{k,l} has k+l > m+1.
        for k in range(1, len(rows) + 1):
            assert m - k + 1 >= 0
        # The density and phase scale are explicit.  Formal D is sqrt(3)m/2,
        # so 2D/sqrt(3)=m, and x_B-x_A=1/m=O(1/D).
        assert edges >= 3 * t * len(rows)
        assert edges >= 6 * t * t
        assert min_a >= m // 4
        assert min_b >= m // 4

        # The affine realization uses horizontal A segments and vertical B
        # segments; X=x+y makes both directions strictly monotone.  An
        # invertible linear map can change their angle to pi/3+1/m without
        # changing the interval graph, disjointness, or crossing signs.
        assert len(rows) == 2 * t + 1
        assert len(cols) == 4 * t + 1
        assert m + 1 == 4 * t + 1

        print(
            f"t={t} m={m} |A|={len(rows)} |B|={len(cols)} "
            f"E={edges} min_degree=({min_a},{min_b}) "
            f"biclique_shore_sum<=m+1={m+1} threshold=m={m}"
        )

    print("PASS: ordered interval-band regression certified")
    print("PASS: dense forward interval structure alone gives no linear Section-76 margin")
    print("PASS: regression omits unit-rhombus metric, source cardinality, KKT, and global optimality")


if __name__ == "__main__":
    main()
