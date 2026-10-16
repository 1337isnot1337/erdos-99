#!/usr/bin/env python3
"""Independent Decimal certificate for AG58 outer-shadow/transverse constants."""
from decimal import Decimal, getcontext

getcontext().prec = 90
D = Decimal
PI = D("3.141592653589793238462643383279502884197169399375105820974944592307816406286")


def sin(x: Decimal) -> Decimal:
    term = x
    total = x
    n = 1
    while True:
        term *= -(x * x) / D((2 * n) * (2 * n + 1))
        n += 1
        old = total
        total += term
        if total == old:
            return total


def cos(x: Decimal) -> Decimal:
    term = D(1)
    total = term
    n = 1
    while True:
        term *= -(x * x) / D((2 * n - 1) * (2 * n))
        n += 1
        old = total
        total += term
        if total == old:
            return total


SQ3 = D(3).sqrt()
DELTA = PI / (2 * SQ3)
S2 = DELTA.sqrt()
G = D("0.00058")
EPS = D("0.0014085")
C146 = D(4) / D(9) * (PI + S2)
T58 = C146 + EPS
C0 = 2 * S2 + G
R58 = D("4.5") * T58 - 2 * PI - C0
assert abs(R58 - D("0.00575825")) < D("1e-70")

# Exact low-t endpoint currencies.
XMIN = PI - T58 - 2 * R58
assert XMIN > D("1.3091541156")

# Transverse matching with alpha=pi/13.
ALPHA = PI / D(13)
COST = 1 - cos(ALPHA)
DELTA_WORST = R58 / 2
G13 = PI - T58 + DELTA_WORST - R58 / COST
Y13 = sin(PI / 3 - ALPHA)
assert G13 > D("1.1253869688")
assert G13 / 6 > D("0.1875644948")
assert Y13 > D("0.7212024473")

# The endpoint minimization really occurs at maximal detour for alpha=pi/13.
DELTA_COEFF = 5 - 2 / COST
assert DELTA_COEFF < 0

# Tooth/long-side split and shallow penetration updates.
M_TOOTH = XMIN / 3
DOUT_MAX = R58 / 2
for eta_s, e_floor, y_floor in [
    ("0.02", "0.0731071138", "0.7868314698"),
    ("0.061", "0.0972964836", "0.7170659742"),
    ("0.068", "0.0985111579", "0.7073095069"),
]:
    eta = D(eta_s)
    n_sh = M_TOOTH - DOUT_MAX / eta
    e_pen = n_sh / 4
    y_eta = SQ3 / 2 * (1 - eta / 2) - D("0.5") * (eta - eta * eta / 4).sqrt()
    assert e_pen > D(e_floor)
    assert y_eta > D(y_floor)

print("PASS: AG58 outer-shadow/transverse Decimal certificate")
print("t58 =", T58)
print("R58 =", R58)
print("x_B-2d floor =", XMIN)
print("alpha=pi/13 G =", G13)
print("alpha=pi/13 symmetric branch floor =", G13 / 6)
print("alpha=pi/13 transverse component =", Y13)
print("tooth/long-side max floor =", M_TOOTH)
