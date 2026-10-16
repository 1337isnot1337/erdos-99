#!/usr/bin/env python3
"""Check the rounded arithmetic in Theorem SC.

The proof is in
docs/reports/target_c_sparse_split_fullcore_closure_2026-09-12.md.  This
certificate checks the conservative Q(.0088)<.072 bound, the correlated product
bound's endpoint arithmetic, and the final strict margin.

It does not certify the proof-only sparse/directional return theorem, the inherited
Section-118 geometry, or the inactive-container branch.  A passing run is not a
C-II or Level-I proof.
"""

from __future__ import annotations

import math


def tooth_q(y: float) -> float:
    lo, hi = 0.0, 0.072
    for _ in range(100):
        q = (lo + hi) / 2.0
        f = math.sin(q) + math.sqrt(3.0) * (1.0 - math.cos(q)) - q - y / 2.0
        if f < 0.0:
            lo = q
        else:
            hi = q
    return (lo + hi) / 2.0


def main() -> None:
    sigma = 0.0088
    theta = 2.70477923521549347
    lam = 0.976243913742568741
    U = 3.0 * theta - 2.0 * math.pi
    kappa = 2.0 - math.sqrt(3.0)
    area_floor = 0.470375286800424054

    q_sigma = tooth_q(sigma)
    q_at_point = math.sin(0.072) + math.sqrt(3.0) * (1.0 - math.cos(0.072)) - 0.072
    print(f"U_endpoint={U:.16f}")
    print(f"tooth_q_sigma={q_sigma:.16f}")
    print(f"tooth_F_at_0.072={q_at_point:.16f}")
    assert q_sigma < 0.072
    assert q_at_point > sigma / 2.0

    product_upper = (1.8312 - sigma) * (0.072 + sigma)
    print(f"product_upper={product_upper:.16f}")
    assert product_upper < 0.1473

    penalty = 0.9763 * (10.0 + 1.0 / kappa) * sigma
    margin = 0.4703 - penalty - 2.0 * 0.1473
    print(f"worst_penalty={penalty:.16f}")
    print(f"strict_margin={margin:.16f}")
    assert margin > 0.057

    # Independent direct evaluation at the least favorable vertex used in the
    # monotonicity proof is also safely below the rounded product bound.
    direct_product = (U - sigma) * (q_sigma + sigma)
    print(f"direct_endpoint_product={direct_product:.16f}")
    assert direct_product < product_upper


if __name__ == "__main__":
    main()

