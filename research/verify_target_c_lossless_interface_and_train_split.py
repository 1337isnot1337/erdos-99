#!/usr/bin/env python3
"""Arithmetic/bookkeeping regression for the 2026-09-14 lossless interface note.

This script verifies constants and exact scalar identities only. It does not prove the
AG42 or Section-171 geometric inputs and does not certify global optimality.
"""

from decimal import Decimal, getcontext

getcontext().prec = 60

PI = Decimal("3.14159265358979323846264338327950288419716939937510582097494")
SQRT3 = Decimal(3).sqrt()
DELTA = PI / (Decimal(2) * SQRT3)
SQRT_DELTA = DELTA.sqrt()
G = Decimal("0.00042")
C = Decimal(2) * SQRT_DELTA + G
C146 = Decimal(4) * (PI + SQRT_DELTA) / Decimal(9)
T0 = C146 + Decimal("0.0013751")

J = T0 + Decimal(2) * C - PI
H = Decimal("1.5") * T0 + C - PI
H_COARSE = Decimal(3) * J / Decimal(5)
F = SQRT_DELTA - PI / Decimal(4) + G / Decimal(2)
PHASE = C - PI / Decimal(2)
LOW22 = PHASE / Decimal(2) - PI / Decimal(19)
A0 = SQRT3 / Decimal(2)
C0 = SQRT3 / Decimal(4)
CORE_GAP = PI / Decimal(2) + H / Decimal(2)
CHAMBER = C0 * H
SIGMA_CH = (H + J) / Decimal(2) + F
R_DEF = H / Decimal(2)
TRAIN_DEF = T0 + Decimal(2) * G
BRANCH = TRAIN_DEF / Decimal(2)
SINGLETON = BRANCH / Decimal(2)
MANTEL = BRANCH * (Decimal(4) * SQRT_DELTA + BRANCH / Decimal(2)) / Decimal(8)

assert H > H_COARSE
assert abs((H - H_COARSE) - Decimal("0.00115359")) < Decimal("1e-25")
assert abs(PHASE / Decimal(2) - F) < Decimal("1e-50")
assert abs(CHAMBER - A0 * R_DEF) < Decimal("1e-50")
assert TRAIN_DEF == T0 + Decimal("0.00084")

# Symbolic coefficient check for H = T + U - P:
# T >= U/2 + C D gives H >= 3U/2 + C D - P.
for U in [Decimal("1.9"), Decimal("2.2")]:
    T = U / Decimal(2) + C
    P = PI
    h_from_identity = T + U - P
    h_from_bound = Decimal("1.5") * U + C - P
    assert h_from_identity == h_from_bound

# Exact scalar identity for the train defect. Normalize sqrt(R4) to sqrt(Delta).
# At the lower envelope T = U/2 + C, rho+sigma = 2T - 4sqrt(Delta).
U = T0
T = U / Decimal(2) + C
assert abs((Decimal(2) * T - Decimal(4) * SQRT_DELTA) - TRAIN_DEF) < Decimal("1e-50")

print("PASS lossless interface/train-split arithmetic")
for name, value in [
    ("Delta_2", DELTA),
    ("C_star", C),
    ("t_star", T0),
    ("J_floor", J),
    ("H_floor", H),
    ("H_coarse", H_COARSE),
    ("H_gain", H - H_COARSE),
    ("phase_gap", PHASE),
    ("f_floor", F),
    ("f_le_22_floor", LOW22),
    ("m_minus_R4_floor", CORE_GAP),
    ("chamber_surplus_floor", CHAMBER),
    ("Sigma_ch_floor", SIGMA_CH),
    ("R4_count_deficit_floor", R_DEF),
    ("rho_plus_sigma_floor", TRAIN_DEF),
    ("max_train_defect_floor", BRANCH),
    ("singleton_floor_if_branch", SINGLETON),
    ("Mantel_floor_if_sigma_branch", MANTEL),
]:
    print(f"{name}={value}")
