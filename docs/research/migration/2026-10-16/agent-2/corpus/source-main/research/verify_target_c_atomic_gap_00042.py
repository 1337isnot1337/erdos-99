#!/usr/bin/env python3
"""High-precision scalar certificate for the proof-only eta_grid=0.00042 refinement.

This certifies only the numerical inequalities in the existing audited Section-168
robust-grid bookkeeping. It does not re-prove the geometric/pseudosegment inputs.
"""
from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
ETA = D("0.00042")
PI = D("3.141592653589793238462643383279502884197169399375105820974944592307816406286")
SQRT3 = D(3).sqrt()
S2 = (PI / (D(2) * SQRT3)).sqrt()
GRID_CAP = D(2) / SQRT3


def quantities(eta: Decimal):
    abar = D(2) * S2 + eta
    m0 = D(4) * S2 * S2 / abar
    r0 = abar - m0
    d0 = abar * abar / D(4) - S2 * S2 + r0 * r0 / D(4)
    p0 = (D(2) * d0).sqrt()
    s0 = m0 / D(2) - d0.sqrt() - (D(6) * d0).sqrt()
    a_keep = s0 - D(2) * p0
    b_keep = s0 / D(2) - D(2) * p0
    triple = D(3) * p0
    eff = D("1.5") * s0 - D(6) * p0
    projected = SQRT3 / D(2) * eff
    return abar, m0, r0, d0, p0, s0, a_keep, b_keep, triple, eff, projected


def f(eta: Decimal) -> Decimal:
    return quantities(eta)[9] - GRID_CAP


def main():
    vals = quantities(ETA)
    names = ["Abar", "M0", "R0", "d0", "p0", "S0", "A_keep", "B_keep", "triple", "effective", "projected"]
    print(f"s2={S2}")
    for n, v in zip(names, vals):
        print(f"{n}={v}")
    print(f"grid_cap={GRID_CAP}")
    print(f"diameter_margin={vals[-1]-D(1)}")

    lo, hi = D("0.0004205"), D("0.0004207")
    assert f(lo) > 0 and f(hi) < 0
    for _ in range(180):
        mid = (lo + hi) / D(2)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    print(f"bookkeeping_root_interval=[{lo},{hi}]")

    # Safe eta=0.00042 inequalities needed by the Section-168 proof.
    abar, m0, r0, d0, p0, s0, a_keep, b_keep, triple, eff, projected = vals
    assert ETA < lo
    assert projected > D("1.00017")
    assert b_keep > triple
    assert a_keep > triple
    assert b_keep > D("0.3849")
    assert eff > GRID_CAP

    # Immediate rhombic-only consequences when the audited proof is restricted to G_R.
    sigma_gap = D(2) * ETA
    mantel_gap = sigma_gap * (D(4) * S2 + ETA) / D(8)
    mu_gain = sigma_gap / D(10)
    chamber_gain = (D(3) * (SQRT3 / D(4)) / D(5)) * sigma_gap
    oler_slack_gain = chamber_gain / (SQRT3 / D(2))
    print(f"sigma_R_gap={sigma_gap}")
    print(f"mantel_gap={mantel_gap}")
    print(f"mu_gain={mu_gain}")
    print(f"chamber_surplus_gain={chamber_gain}")
    print(f"chamber_oler_slack_gain={oler_slack_gain}")

    assert sigma_gap == D("0.00084")
    assert mantel_gap > D("0.0003999")
    assert mu_gain == D("0.000084")
    assert oler_slack_gain == D("0.000252")
    print("PASS: eta_grid=0.00042 scalar refinement")

if __name__ == "__main__":
    main()
