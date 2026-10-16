#!/usr/bin/env python3
"""Numerical regression certificate for the shore-balanced atomic-gap refinement.

The proof is in target_c_atomic_gap_shore_balance_00059_2026-09-15.md.
This script checks the displayed Decimal constants, the inherited common-neighbor
slack, the final projected-diameter contradiction at eta=0.00059, and brackets the
bookkeeping root.  It is a regression certificate, not a substitute for the proof.
"""

from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
PI = D("3.141592653589793238462643383279502884197169399375105820974944592307816406286")
SQRT3 = D(3).sqrt()
DELTA2 = PI / (D(2) * SQRT3)
S2 = DELTA2.sqrt()


def data(eta: Decimal):
    abar = D(2) * S2 + eta
    m0 = D(4) * S2 * S2 / abar
    r0 = abar - m0
    d0 = abar * abar / D(4) - S2 * S2 + r0 * r0 / D(4)
    sd = d0.sqrt()
    p0 = (D(2) * d0).sqrt()
    l0 = (D(6) * d0).sqrt()
    s0 = m0 / D(2) - sd - l0
    g0 = D(3) * m0 / D(4) - sd / D(2) - l0
    ebal = g0 - D(6) * p0
    projected = SQRT3 * ebal / D(2)
    triple_margin = s0 / D(2) - D(5) * p0
    return {
        "abar": abar,
        "m0": m0,
        "r0": r0,
        "d0": d0,
        "sqrt_d0": sd,
        "p0": p0,
        "l0": l0,
        "s0": s0,
        "g0": g0,
        "ebal": ebal,
        "projected": projected,
        "triple_margin": triple_margin,
    }


eta = D("0.00059")
v = data(eta)

# Deliberately coarse safety thresholds, well inside the displayed margins.
assert v["projected"] > D("1.0018")
assert v["triple_margin"] > D("0.26")
assert v["m0"] > D("1.9040")
assert v["d0"] < D("0.000563")

# Bracket the zero of the revised bookkeeping.  The sampled formula is monotone
# decreasing over this tiny interval; the proof only uses the safe eta=0.00059 point.
lo = D("0.00059946")
hi = D("0.00059947")
assert data(lo)["projected"] > D(1)
assert data(hi)["projected"] < D(1)

print(f"s2={S2}")
print(f"eta={eta}")
for key in ("abar", "m0", "r0", "d0", "sqrt_d0", "p0", "l0", "s0", "g0", "ebal", "projected", "triple_margin"):
    print(f"{key}={v[key]}")
print(f"root bracket: {lo} < eta_* < {hi}")
print("PASS: shore-balanced eta_grid=0.00059 certificate")
